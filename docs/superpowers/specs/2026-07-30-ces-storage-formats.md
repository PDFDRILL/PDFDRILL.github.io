# CES matrix storage and the RAG-shaped formats around it

Date: 2026-07-30
Status: **reference** — describes conceptdrill as it stands today, ahead of the
pdfdrill integration.

Read from `~/conceptdrill` at commit `c66dd25`. Every field name below is taken
from the code, not from prose. Two format families are in play and they are
deliberately *not* the same file.

---

## 1. Where things live, and why the split exists

```
~/pdfdrill-library/<bibkey>/          per document — joins pdfdrill's model.* family
    model.docmodel.json               INPUT. read-only, never modified
    model.ces.json                    section tree + summaries
    <bibkey>.drill.json               gains fact CES_BUILT + a content-hash proof

<corpus_dir>/                         per corpus — deliberately NOT in a drill folder
    ces-basis.json                    rows, document order, tau, basis_version
    ces-basis.npz                     the matrix M, float64
    ces-index.json                    one record per stored sentence
    ces-vectors.npz                   sentence CES vectors, float64
    queries.jsonl                     append-only query log

<cwd>/.conceptdrill_cache/            content-addressed embedding cache
    emb-<model>-<hash>.npz
    summaries.json
```

**The split is the load-bearing design decision.** A shared basis belongs to the
corpus. Writing it beside one document would make that document silently
authoritative for every other one. Per-document artefacts go in the drill
folder; the basis does not.

---

## 2. `model.ces.json` — per document

`format: "conceptdrill.ces"`, `format_version: 1`.

```json
{
  "format": "conceptdrill.ces",
  "format_version": 1,
  "bibkey": "2209.00445",
  "source": { "…source_fingerprint of model.docmodel.json…" },
  "created_at": "…",
  "section_tree": {
    "stats": { … },
    "roots": ["…"],
    "orphan_paragraph_ids": ["…"],
    "nodes": [
      {
        "id": "…", "title": "…", "title_raw": "…",
        "level": 2, "flow_index": 7, "is_appendix": false,
        "parent_id": "…", "children": ["…"],
        "lost_macros": ["\\ALG"],
        "paragraph_ids": ["…"],
        "body_chars": 1234, "subtree_chars": 5678
      }
    ]
  },
  "summaries": { "<node_id>": { "summary": "…", "abstraction": "…", "label": "…" } },
  "content_hash": "…"
}
```

Three things worth knowing before consuming it:

- **`title` vs `title_raw`.** DocModel section captions carry unresolved LaTeX
  macros. `captions.py` cleans them and records what it dropped in
  `lost_macros`, so the loss is visible rather than silent.
- **`parent_id` is reconstructed.** The DocModel has `parent: null` on every
  Section; the tree is rebuilt from `level` + `flow_index`. Do not assume a root
  level — 89 of 251 usable documents start at level 1 and 103 at level 2.
- **Three summary tiers, only one is the basis tier.** Measured at 1.604 BERT
  tokens per word:

  | tier | words | tokens | role |
  |---|---|---|---|
  | `summary` | 80–150 | 128–241 | document-faithful |
  | `abstraction` | ~70 | 96–128 | document-independent |
  | **`label`** | **30–42** | **48–67** | **the only one that fits a 50–70 token window** |

### The sidecar capability

`CES_BUILT` is registered in `<bibkey>.drill.json` with a proof recording a hash
per input file. `capability_valid()` re-hashes them, so **re-drilling a document
invalidates its CES output automatically**. Writes are additive and preserve
every sidecar key they do not understand. A proof with no inputs is valid — there
is nothing that could invalidate it.

---

## 3. The corpus store — the RAG-shaped part

`format: "conceptdrill.ces.corpus"`, `format_version: 1`.

### `ces-basis.json` + `ces-basis.npz` — the matrix M

JSON side:

```json
{
  "format": "conceptdrill.ces.corpus", "format_version": 1,
  "basis_version": "…", "tau": 0.65,
  "document_order": ["2209.00445", "…"],
  "embedding_model": "sentencebert", "embedding_revision": "1110a243…",
  "summarizer": "…",
  "stats": { … },
  "rows": [
    { "row_id": "…", "level": 2, "label": "…",
      "support": 3, "documents": ["…"], "merged_labels": ["…", "…"] }
  ]
}
```

Vectors are **excluded from the JSON** (`to_dict(include_vector=False)`) and
live in the NPZ:

| array | dtype | meaning |
|---|---|---|
| `matrix` | float64 | M — one unit-norm row per concept, in canonical row order |
| `row_ids` | str | row identity, parallel to `matrix` |
| `basis_version` | str | written into the NPZ too, so the pair cannot be split |

**Row order is canonical: `(level, -support, label)`.** `row_id` is
content-addressed so identity survives reordering, and `basis_version` hashes the
ordered ids — which is what lets a stored vector detect that its coordinates
moved. That is the entire reason the version exists, and it is checked on load:
vectors left behind by an earlier basis are **refused, not silently misread**.

`merged_labels` keeps every label folded into a row. The row's own `label` and
`row_id` never change on merge, so the canonical name is stable while the
evidence for it accumulates.

### `ces-index.json` + `ces-vectors.npz` — the sentence index

```json
{
  "format": "conceptdrill.ces.corpus", "format_version": 1,
  "basis_version": "…", "n_sentences": 1489,
  "records": [
    { "sentence_id": "…", "text": "…",
      "section_id": "…", "source_id": "…", "document": "2209.00445",
      "top_concepts": [
        { "row_id": "…", "label": "…", "level": 2,
          "similarity": 0.438, "rank": 1 }
      ],
      "margin": 0.0369 }
  ]
}
```

`ces-vectors.npz` holds `vectors`, float64, one CES row per record.

**`margin` is stored deliberately** — top-1 minus top-2. A high top-1 with a
near-zero margin is ambiguity, not confidence, and the two are indistinguishable
from the similarity alone.

### `queries.jsonl`

Append-only log, one JSON object per line, written by `QueryLog.append`.

---

## 4. How this differs from a conventional RAG store

This is the part worth being precise about, because the file layout looks
familiar and the semantics are not.

| | conventional vector RAG | conceptdrill CES |
|---|---|---|
| Stored vector | raw embedding, dim 384–1024 | **CES vector, dim = number of basis rows** |
| Coordinate meaning | none individually | **cosine to one named concept** |
| Retrieval space | embedding space | **CES space** |
| Explanation | post-hoc, via the retrieved text | `shared_concepts` — which named concepts query and sentence agree on |
| Dimensionality | fixed by the model | grows with the corpus, bounded by the merge rule |
| Stale vectors | usually silently reused | **refused** via `basis_version` |

Two consequences:

- **Search happens in CES space, not embedding space.** Cosine rather than dot
  product, so a sentence matching every concept weakly cannot outrank one
  matching a single concept strongly on magnitude alone.
- **A bare CES vector is not interpretable.** Coordinate 4 means whatever row 4
  was. Every vector therefore records `basis_version` and the embedding model.

### The number that matters for integration

The basis is built by an adaptive merge: per level, a candidate merges into its
nearest row when cosine ≥ `TAU`, else becomes a new row.

**`TAU` defaults to 0.65, measured rather than guessed.** The design spec
proposed 0.85; across three topically related papers that produced *zero*
merges, because the highest cross-document similarity observed was **0.647** —
and that pair was genuinely related. 0.85 is a near-paraphrase threshold and the
wrong scale for this. `basis.calibrate()` reports within- and cross-document
distributions separately, because they answer different questions.

Basis arithmetic is **float64 throughout**: a merge decision is one comparison
against `TAU`, and a wrong cosine adds a row that should have merged,
unrecoverably. On this host that is not paranoia — `blasfix.py` exists because
float32 GEMM is miscomputed in roughly one process in three.

### Known limit, stated plainly

Measured on 1489 sentences from three papers against a 38-row basis:

| | p10 | median | p90 |
|---|---|---|---|
| top-1 similarity | 0.239 | 0.438 | 0.647 |
| margin | 0.0056 | 0.0369 | 0.1339 |

**For 60% of sentences the margin is below 0.05.** All 38 rows win at least
once and the most frequent takes 12%, so the machinery is sound — but a 38-row
basis from three documents, 30 of them singletons, is too thin to discriminate.

### The basis does not stay small — measured, `0ce9b92`

This was open when the section above was written and is now answered, on the
full library rather than three papers. It is the single most important number
for sizing an integration.

Over 416 docmodels (278 usable), τ=0.65, batches of 100:

| | |
|---|---|
| candidates → rows | 8694 → **5923**, a factor of 1.47 |
| rows per document | **rises** 10.40 → 21.31 |
| singleton rows | 4861 |
| rows spanning >1 document | 275 — **4.6% of the basis** |

Roughly three quarters of all merging happens *inside* a single paper. τ scales
the constant, not the slope: on a fixed 120-document sample, 0.55 / 0.65 / 0.75
give 6.19 / 8.60 / 10.53 rows per document.

The run used `ExtractiveSummarizer`, not an LLM, and the proxy is **optimistic**
— extractive labels measured *more* cross-document similar than LLM ones (0.723
vs 0.647), so the real pipeline should merge less, not more.

**The consequence for storage is the opposite of what a vector store usually
assumes.** `M @ l` takes a 384-dim sentence embedding to 5923 dims — the
projection *expands*, by about 15×:

| | uncompressed |
|---|---|
| one CES vector, dense float64 | 46.3 KiB |
| 1489 sentences | 67.3 MiB |
| the same sentences as raw 384-dim embeddings | 4.36 MiB |
| basis matrix M (5923 × 384) | 17.4 MiB |

`ces-basis.npz` and `ces-vectors.npz` are written with `np.savez_compressed`,
and CES vectors are mostly near-zero, so on-disk figures will be well below
these — but they have not been measured at library scale and should not be
guessed at. The embedding cache uses plain `np.savez`, uncompressed.

**The adaptive basis buys interpretable axes, not compression.** Anything
planning to hold CES vectors for a whole corpus needs a sparse representation or
a top-k truncation, not a dense float64 matrix. Note that `ces-index.json`
already stores `top_concepts` per sentence — a truncated view exists in the
format today, and for retrieval it may be the one worth using.

---

## 5. The embedding cache

`.conceptdrill_cache/emb-<model>-<hash>.npz`, keyed by
`cache_key(text, model_name, model_revision)` so an entry can never be served to
a different model or revision. `summaries.json` caches summariser output.

`np.savez` appends `.npz` to a path that lacks it, which breaks atomic rename —
both the cache and the corpus store write through an open file object instead.
Worth carrying into any new writer.

---

## 6. What pdfdrill would consume

For the integration, the smallest useful contract:

- **Read** `model.ces.json` for a document's section tree and `label` summaries.
- **Check** `CES_BUILT` in the sidecar before trusting it; `capability_valid()`
  re-hashes inputs.
- **Never** write into `model.docmodel.json`. conceptdrill treats it as
  read-only input and the same discipline should hold from the other side.
- **Resolve** any CES vector against the basis named by its `basis_version`, or
  refuse it. Do not interpret coordinates without one.
- **Do not** put the corpus basis in a drill folder.

Concepts and embeddings are **realizations and alignments over** a DocObject,
not fields on it. Flattening them into the object would contradict the DocModel's
own design — source streams immutable, modules only add — and would make the CES
output unremovable.

from (4.57), $\left\langle\mathbf{s}_{\|}, \mathbf{s}_{\perp}\right\rangle=0$, hence $\|\mathbf{s}\|^{2}=\left\|\mathbf{s}_{\|}\right\|^{2}+\left\|\mathbf{s}_{\perp}\right\|^{2}$ (4.44). Analogously, the maximum-likelihood estimate is

$$
s^{r e c}=s_{\|}=\sum_{m=1}^{|M|} O_{m} p_{m}
$$

Notably, the change of a single $O_{m}$ does not change any of the other projections of $\mathrm{s}^{\text {rec }}$ to $\left\{\mathrm{q}_{\mathrm{m}}\right\}_{\mathrm{x}_{\mathrm{m}} \in \mathcal{M}}$ (4.56); this comes directly from (4.54).

Now we are prepared to calculate $O^{r e c}(\mathbf{x})(4.45)$ :

$$
O^{\text {rec }}(\mathbf{x})=\left(\hat{\mathbf{x}}, \mathbf{O}^{*} \sum_{m=1}^{|\mathcal{M}|} O_{m} \mathbf{p}_{m}\right)=\sum_{m=1}^{|\mathcal{M}|} O_{m}\left(\hat{\mathbf{x}}, \mathrm{O}^{*} \mathbf{p}_{m}\right)=\sum_{m=1}^{\mid \mathcal{M}} O_{m} a_{m}(\mathbf{x})
$$

with

$$
a_{m}(\mathbf{x}) \equiv\left(\hat{\mathbf{x}}, \mathbf{O}^{*} \mathbf{p}_{m}\right)
$$

Analogously to (4.46), the magnitude of the terms of the reconstruction are proportional to $O_{m}$, and their x dependence is given by the inner product of x with the action of O* on the dual-basis vectors $\left\{\mathbf{p}_{m}\right\}_{\mathbf{x}_{m}} \in \mathcal{M}$, only this time, the formula for the dual basis (4.53) is not as straightforward as (4.40).

We are now well motivated to inquire into the meaning of B (4.53). From (4.54),

$$
\delta_{m, l}=\left\langle\mathbf{q}_{m}, \sum_{n=1}^{|\mathcal{M}|} \mathbf{B}_{l n} \mathbf{q}_{n}\right\rangle=\sum_{n=1}^{\mathcal{M} \mid} \mathbf{B}_{l n}\left\langle\mathbf{q}_{m}, \mathbf{q}_{n}\right\rangle=\sum_{n=1}^{|\mathcal{M}|} \mathbf{B}_{l n} \mathbf{Q}_{m n}
$$

with $\mathbf{Q}_{n m}=\left\langle\mathbf{q}_{n}, \mathbf{q}_{m}\right\rangle$. Therefore, $\mathbf{B}=\mathbf{Q}^{1}$ and

$$
\mathrm{p}_{l}=\sum_{\mathrm{n}=1}^{|\mathcal{M}|} \mathrm{Q}^{-1}{ }_{\mathrm{ln}} \mathrm{q}_{\mathrm{n}} .
$$

Now, from (4.47)

$$
\mathbf{Q}_{n m}=\left\langle\mathbf{q}_{n}, \mathbf{q}_{m}\right\rangle=\left\langle\mathbf{O} \hat{\mathbf{x}}_{n}, \mathbf{q}_{m}\right\rangle=P_{m}\left(\mathbf{x}_{n}\right)
$$

with

$$
P_{m}(\mathrm{x}) \equiv P_{\mathrm{x}_{\mathrm{m}}}(\mathrm{x}) .
$$

Notably, the matrix $\mathbf{Q}$ is the restriction of the matrix $\mathbf{P}$ on the set of reference points, $\mathcal{M}$ :

$$
\mathbf{Q}=\left.\mathbf{P}\right|_{\mathcal{M}} .
$$

With (4.62), we can calculate

$$
a_{m}(\mathbf{x})=\left\langle\hat{\mathbf{x}}, \mathbf{O}^{*} \mathbf{p}_{m}\right\rangle=\sum_{n=1}^{|\mathcal{M}|} \mathbf{Q}_{m n}^{-1}\left(\hat{\mathbf{x}}, \mathbf{O}^{*} \mathbf{q}_{n}\right)=\sum_{n=1}^{|\mathcal{M}|} \mathbf{Q}_{m n}^{-1} P_{n}(\mathbf{x}) .
$$

79
Finally,

$$
O^{r e n}(\mathbf{x})=\sum_{m=1}^{|\mathcal{M}|} O_{m} a_{m}(\mathbf{x})
$$

with

$$
a_{m}(\mathbf{x})=\sum_{n=1}^{|\mathcal{M}|} \mathbf{Q}^{-1}{ }_{m n} P_{n}(\mathbf{x}) .
$$

Analogously to (4.48-4.49), the $\mathbf{x}$ dependence of the reconstructors $a_{m}(\mathbf{x})$ depends only on the locations of the reference points $\mathcal{M}$, but not on $\phi$ itself.

The reconstructors $a_{m}(\mathbf{x})$ (4.68) are indeed interpolating-with (4.63),

$$
a_{m}\left(\mathbf{x}_{l}\right)=\sum_{n=1}^{|\mathcal{M}|} \mathbf{Q}^{-1}{ }_{m n} P_{n}\left(\mathbf{x}_{l}\right)=\sum_{n=1}^{|\mathcal{M}|} \mathbf{Q}^{-1}{ }_{m n} \mathbf{Q}_{n l}=\delta_{m l} .
$$

The reconstruction of the example $\phi \mathrm{is}^{35}$

$$
\phi^{r e c}(\mathrm{x})=\sum_{m=1}^{|\mathcal{M}|} O_{m} \sum_{n=1}^{|\mathcal{M}|} \mathrm{Q}_{m n}^{-1} K^{(-1)}{ }_{n}(\mathrm{x})
$$

with $K^{(-1)}{ }_{n}(\mathrm{x})=\left(\tilde{\mathrm{x}}, \mathrm{K}^{(-1)} \hat{\mathrm{x}}_{n}\right)$.
Analogously to (4.48-4.49), the full LFA reconstruction (4.67-4.68) uses the local topographic LFA projector (4.29), but this time uses also Q ${ }^{1}$. At first, this might not seem natural-when $|\mathcal{M}|$ is large, $\mathbf{Q}$ is also large, and inverting it is difficult. Nevertheless, $Q$ is a special matrix-most of its values are vanishingly small; because the supports of $\left\{P_{\mathrm{m}}(\mathrm{x})\right\}_{\mathrm{x}_{\mathrm{m}} \in \mathcal{M}}$ are local, Q is sparse. For each point $\mathrm{x}_{m}$, the $m$-th column of Q has substantially nonvanishing values for only a few other reference points-the ones that fall in the support of $P_{\mathrm{m}}\left(\mathrm{x}_{\mathrm{m} \mathrm{n}}\right)$. Moreover, this is true even when the volume of the receptor grid $V$ increases-adding more and more receptors distant to $\mathbf{x}_{m}$ does not add nonzero elements to the $m$-th column of $\mathbf{Q}$. Therefore, only local computations will be need to invert it, and the dimensionality of those computations will be small, regardless of $N$ and $V .{ }^{36}$

In this Section, we have shown how to represent a sensory stimulus $\phi(\mathrm{x})$ and its probability $\mathcal{P}[\phi(\mathbf{x})]$, in the context of an ensemble with low dimensionality, as a linear combination (4.67) of a small number of reconstructors (4.68). Because the information about the original example is distributed among all

[^0]reconstructors, whose centers are located sparsely on the receptor grid, the LFA representation (4.67-4.68) is sparse-distributed. ${ }^{37}$

### 4.4.4 Serial Sparsification: An Efficient Algorithm

So far, we have addressed the question, given a sparsification $\left\{O\left(\mathrm{x}_{m}\right)\right\}_{\mathrm{x}_{m} \in \mathcal{M}}$, how to reconstruct $O(\mathbf{x})$ and, from there, the example $\phi$ and its probability $\mathcal{P}[\phi]$.

Because of the local nature of the LFA computations, in both their dense (4.29), and sparsifying (4.67-4.68), stages, it is reasonable to assume that the parallel cortical circuitry can allow for a good LFA implementation. In Section 4.4.6 we will, indeed, propose a neural network for the implementation of LFA.

In order to develop some insight into the nature of the sparse-distributed LFA representation, at first we will offer an iterative sparsification algorithm, which has the important property that it is efficient on serial machines, such as those readily available to the contemporary researcher.

Given an example $\phi$, we first calculate the dense LFA outputs $O(\mathbf{x})$, using (4.29). This finishes the dense stage of LFA.

In the sparsification stage, we start with the empty set $\mathcal{M}^{(0)}=\emptyset$ and perform a series of iterative steps; at the $n$-th step, we add to $\mathcal{M}^{(n)}$ one reference point according to the procedure described bellow; when a certain criterion is met, we stop the algorithm.

The resulting set $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$ is an LFA representation of $\phi$.
We proceed to define the criteria for addition of new references point to $\mathcal{M}$ and for termination of the algorithm. At the $n$-th step, we do three things. First, given the current set $\mathcal{M}=\mathcal{M}^{(n)}$, we calculate the current maximumlikelihood estimate $O^{r e c}(\mathrm{x})$ by (4.67-4.68) and calculate the current error

$$
O^{\text {err }}(\mathbf{x})=O(\mathbf{x})-O^{\text {rec }}(\mathbf{x}) .
$$

Second, we look for the grid point $\mathrm{x}_{m+1}$, such that the value of $O^{\text {err }}\left(\mathrm{x}_{m+1}\right)$ is maximum. If its square, $O^{\text {err }}\left(\mathbf{x}_{m+1}\right)^{2}$, is below a predetermined threshold, we terminate the sparsification. ${ }^{38}$

[^1]![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-02.jpg?height=413&width=841&top_left_y=110&top_left_x=110)
Figure 4.4: Resource Allocation by the Serial Sparsification Algorithm The building of the mask $\mathcal{M}$ for Example $\mathbb{I}$, reconstructed in the context of Ensemble 1. $N=220, n=\sigma_{400}$ (see Fig. 4.1). $a$ : the first 25 points- $\mathcal{M}^{(25)}$, overlayed on $\phi(\mathbf{x})$ and numbered sequentially. (The label for point 11, in the lower right corner, was sticking outside the picture, so it is not shown on $a$; it is the bottommost point on the right edge, shown on $b$.) $b$ : the points in $\mathcal{M}^{(64)}$. The reconstruction with these points is shown on the top row of Fig. 4.5b.

the LFA ones $O(\mathbf{x})$ (4.31) for $N=220$, then sparsified to get $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$. We calculated the reconstruction $\phi^{r e c}(\mathbf{x})$ either (a), from (2.50) with $N=64$, or (b), from (4.70) with $O^{\text {rec }}(\mathbf{x})$ derived from (4.67 4.68) with the points in $\mathcal{M}^{(64)}$. For comparison, we subsampled $\phi(\mathbf{x})$ on a uniform $8 \times 8$ grid and reconstructed it with those 64 points (c). In all cases we reconstructed about $\Psi_{1}$ the average of the ensemble; we kept $a_{1}$ fixed. Evidentially, the perceptual quality of the reconstruction $\phi^{\text {rec }}(\mathbf{x})$ (top row) is the best, and the error $\phi(\mathbf{x})-\phi^{\text {rec }}(\mathbf{x})$ (bottom row) contains the least identity information for the LFA representation (b). ${ }^{40}$ This makes the sparse-distributed representation a promising candidate
${ }^{40}$ One would like to know how the perceptually better sparsified LFA representation compares in terms of m.s.e. with the global PCA one. The m.s.e. in Fig. 4.5 is 184, 227, and 508 for ( $a$ ), ( $b$ ), and ( $c$ ), respectively, out of 560 total power in $\left(\phi(\mathrm{x})-a_{1} \Psi_{1}\right.$ ). Notably, the larger m.s.e. of 227 (b) belongs the perceptually better picture.

Curiously, the error on (b), has a global component-positive in the center and negative near the borders; it is very much like an error in a strong global mode, which we identify as $\Psi_{2}$ on Fig. 3.9. Indeed, the m.s.e. due to the error in $a_{2}$ in (b) is 75. If one fixes not only $a_{1}$, but also $a_{2}$, the m.s.e. of the sparsified LFA is 152, compared to 184 for PCA. This suggests that from m.s.e. point of view the optimal representation is a hybrid between PCA and LFA-an idea which we exploit in Appendix A.4. Interestingly, the LFA representation of the example $\phi$ on Fig. 4.5-original, with $a_{1}$ and $a_{2}$ fixed, has a better fidelity at this dimensionality than the PCA representation!

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-02.jpg?height=685&width=651&top_left_y=1435&top_left_x=217)
Figure 4.5: Reconstruction with a Fixed Number of Values (64) The reconstruction (top row) and the error (bottom row) for $\phi(\mathbf{x})$ of Example 1 (original) in the context of Ensemble 1. Reconstruction in all cases is about the average face $\Psi_{1}$. $a$ : reconstruction from the first 64 PCA coefficients, $N=64$ (2.48). $b$ : reconstruction from the sparsification $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}(4.674 .68)$ with $\mathcal{M}=\mathcal{M}^{(64)}$ shown on Fig. 4.4b, which was produced by the serial algorithm outlined in the text for $O(\mathbf{x})$ calculated with $N=220, n=\sigma_{400}$ (cf. Fig. 4.3). $c$ reconstruction from a subsampling on a regular $8 \times 8$ grid (64 points). The error on (a) is exactly equal to $\phi_{64}^{e r r}$, and the error on (b) is perceptually somewhere between $\phi_{100}^{e r r}$ and $\phi_{200}^{e r r}$ (cf. also the reconstruction with $\phi_{200}^{r e c}$ ), both are magnified $5 \times$ (cf. Fig. 3.12, Fig. 4.3). The error on (c) is not magnified.

for practical applications, such as compression and object recognition.
The algorithm works relatively quickly ${ }^{41}$ and extremely robustly in practice;

[^2]we have produced sparse-distributed representations for all ensembles described previously in the paper, for various values of $N$, with great success. In all cases $O(\mathbf{x})$ was recovered practically to machine precision after choosing, usually much less than $N$ points. In Appendix A. 5 we speculate where the observed numerical stability could be coming from.

The observation that the LFA representation produces perceptually better reconstructions, compared to the PCA representation with the same number of values, is intriguing. We have already suggested that signal power may not be the perceptually relevant measure (see discussion on page 27). This is in good agreement with Information Theory (Shannon and Weaver 1949), which derives $-\log \mathcal{P}[\phi]$ as the information content of, as well as the length of the optimal code for, $\phi$; the ideas of Barlow (1961b), Attneave (1954), Pearson (1892), and Mach (1914); and the experimental evidence that the visual system (the retina at least) is interested in, and coding in accordance with, $-\log \mathcal{P}[\phi]$ (Atick and Redlich 1992), as outlined in Section 4.2.

Fig. 4.6 shows a comparison between the information content captured by PCA (2.49) and LFA (4.67-4.68) as a function of the number of terms in the respective representations. The average information per term (in the regime of the genuine modes) is constant for PCA by construction (2.42). Interestingly, the first few terms of the LFA representation pull off a sizeable percentage of the total information content of $\phi$. A modest increase is observed thereafter, and almost nothing is gained for the last 50\% of the terms.

A more quantitative comparison is shown on Fig. 4.7. It is evident that 90\% of the information is contained in representations with number of refer- ence points $|\mathcal{M}| 20 \%-25 \%$ of their respective PCA dimensionalities $N ; 99 \%$, with $45 \%-50 \%$. Therefore, the necessary LFA dimensionality for a given "information fidelity" is about half of the corresponding PCA dimensionality. ${ }^{42}$

We need to emphasize that the information content and, therefore, the optimal length of the code are exactly the same for the PCA and the LFA representations. ${ }^{43}$ What has happened, is that the dimensionality of the rep-

[^3]![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-03.jpg?height=580&width=820&top_left_y=103&top_left_x=130)
Figure 4.6: Comparison Between P A and LFA S-N Diagrams The total information of the PCA reconstruction (2.49) of Example 1 (Fig. 4.5original) in the context of Ensemble 1 (Fig. 3.9) as a function of the number of terms $N$ is show with a solid line (cf. F.g. 3.11). Note that each term contributes on the average $\approx 1$.
The total information (4.22) of the LFA reco struction (4.67 4.68), sparsified with the serial algorithm outlined in the text, as a function of the number referce points $|\mathcal{M}|$ is shown with dashed lines for $N \in$ \{600, 400, 30, 220, 110, 64, 32\}, from top to bottom respectively.

resentation has been reduced, but the information content and, therefore, the needed pricision of the representational variables have increased accordingly. This is " ood"-the running time of various higher-levil algorithms depends very strugly on the dimensionality of the representation, but very weakly, practic ly not at all, on the precision of the calculations themselves.

Th representation produced by the described sparsification algorithm, utilizin the residual correlations $\mathbf{P}$ to reconstruct $O(\mathbf{x})$, contalns all of the informatren in $O(\mathbf{x})$ and so possesses all of its desirable properties best reconstruction, generalization and object constancy. In addition, it is sparse-distributed, instead of dense, which reveals the low dimensionality of the object space.

Finally, in ensembles wherein the images contain a relatively large amount background, the most prominent "features" are the transitions from the back-

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-03.jpg?height=599&width=800&top_left_y=1439&top_left_x=137)
Figure 4.7: Scaling of LFA $S-N$ Diagrams The ratio of residual LFA information, $\left\|O^{\text {err }}\right\|_{U}^{2}$, to the total information, $\|O\|_{U}^{2}=\left\|\Phi^{*+} \phi\right\|_{S}^{2}$ (4.22), as a function of $|\mathcal{M}| / N$, the relative dimensionalities of the LFA and PCA representations for $N \in\{600,400,300,220,110,64,32\}$ (cf. Fig. 4.6).

ground to the objects. The application of the serial sparsification algorithm to such an ensemble, Ensemble 3 (see Appendix A. 1 for definition), is shown on Fig. 4.8. Almost all of the points in the respective sets $\mathcal{M}^{(50)}$ are on the boundaries of the heads, which are pinpointed with great precision. This suggests the possibility of the application of LFA to roughly aligned ensembles for segmentation, followed by the application of a subsequent, high-fidelity LFA module to extract the internal features of the segmented objects.

### 4.4.5 Feature Templates with LFA

In Section 4.4.3 we derived the maximum-likelihood reconstruction (4.67-4.68), given a sparsification $\left\{O\left(x_{m}\right)\right\}_{x_{m} \in \mathcal{M}}$ of the dense LFA outputs $O(x)$ for an example $\phi$. It is a linear combination with coefficients $O_{m}$ and x-dependence given by the set of interpolating reconstructors $\left\{a_{m}(\mathbf{x})\right\}_{x_{m} \in \mathcal{M}}$ (4.68).

Analogously, the reconstruction of $\phi$ (4.70) was given as the same linear combination, only with a different set of reconstructors, $\sum_{n=1}^{\mathcal{M}} \mathrm{Q}^{-1}{ }_{n n n} K^{(-1)}{ }_{n}(\mathbf{x})$.

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-03.jpg?height=418&width=813&top_left_y=94&top_left_x=1046)
Figure 4.8: Segmentation by Sparsification The sparsifications $\mathcal{M}^{(50)}$, produced by the serial algorithm outlined in the text, for Example 1 (a) and Example 2 (b), overlayed on their respective $\phi(\mathbf{x})$, in the context of Ensemble 3 (see Appendix A. 1 for definition) with $V=8640$, $T=1038, N=400, n=\sigma_{400}$ (see Fig. 4.1).

Although, on one hand, the actual reconstruction of $\phi$ may not be always needed, and, on the other, dynamically calculating and storing two sets of a small number of reconstructors may be feasible, it is still of interest to explore the possibility of a unified set of reconstruction coefficients.

Indeed, (4.70) is a double sum; we have interpreted it in (4.67 4.68) as the reconstructors $a_{m}(\mathbf{x})$, which are scaled by the magnitudes $O_{m}$. Nevertheless, nothing prevents us from taking the other sum first; thus, we can define an alternative set of representational variables

$$
\mathcal{O}_{l} \equiv \mathbf{Q}^{-1}{ }_{l m} O_{m} .
$$

With them,

$$
\begin{aligned}
& O^{r e x}(\mathbf{x})=\sum_{i=1}^{|\mathcal{M}|} \mathcal{O}_{l} P_{l}(\mathbf{x}) \\
& \phi^{r e c}(\mathbf{x})=\sum_{l=1}^{|\mathcal{M}|} \mathcal{O}_{l} K_{l}^{-1}(\mathbf{x})
\end{aligned}
$$

This is a remarkable result. It tells us that LFA reconstructions can be made that utilize a small number of coefficients which depend on the example $\phi$ (4.72), but the $\mathbf{x}$-dependence of the reconstructors, which are themselves local, is fixed for the whole ensemble in advance. This is interesting, because they can

## 88

be stored in relatively permanent storage, such as the strength of the lateral connections in the cortex, which opens the possibility for biologically plausible implementations.

We argued that, since $\mathbf{Q}$ is sparse, inverting it may turn out to be a local operation. By the same argument, $\mathbf{Q}^{-\mathbf{1}}$ will be sparse, and acting with it on $O_{m}$ will be a local operation too. Moreover, one may try to solve for $\mathcal{O}_{I}$ directly and never explicitly store $\mathbf{Q}^{-1}$, which will eliminate one computational step and one set of variables to store.

Some intuition into what is involved in the calculation of $\mathcal{O}_{1}$ may be developed by looking at Fig. 4.4b. It is evident that the activity, apart for the spuriousness in the background, is concentrated in a few clusters, each comprised of a small number (1-4) of reference points. It is easy to imagine that Q will have almost vanishing entries for all pairs of points that have one member from the cluster and one, from the outside, and also that increasing the volume of the system will just add more non-interacting clusters. In such situations,

$$
\sum_{l=1}^{|\mathcal{M}|} \mathrm{Q}_{m l} \mathcal{O}_{l}=O_{m}
$$

may be solved for $\mathcal{O}_{l}$ (cf. 4.72) by a rapid iteration.
Note that the elements of $\mathbf{Q}$ are the elements of $\mathbf{P}$ (4.65), and $\mathbf{P}$ is already propagated anyway, arguably by the lateral connections. In such situations the weak interactions from the distant clusters will contribute to the solution, but will not perturb it substantially.

Very importantly, (4.74) is a restriction of (4.73) on $\mathcal{M}$. We will use this fact in Section 4.4.6 to propose a neural network implementation of LFA.

The notion of clusters leads to the idea that the sums in the reconstructions (4.73) may be taken only over a given cluster; they will, then, represent only the information in a local region, thereby forming a representation of the corresponding local feature, which needs not be a "simple" feature this time.

Now, the features may be manipulated separately from the rest of the representation and, therefore, may participate in algorithms that utilize features, instead of whole objects. One potentially interesting such algorithm is Flexible Template Matching, which has been hypothesized to be a good algorithm for face recognition (Yuille 1991).

There are several explicit benefits in using the LFA representation (4.73) for Flexible Template Matching: the features are statistically matched to the ensemble; all of them are calculated synchronously for the whole object; the difference in two such features is directly related to its probability in the context of the ensemble; and last, but not least, each feature is extremely low-dimensional, facilitating fast computations. ${ }^{44}$

[^4]
### 4.4.6 Parallel Sparsification: A Biologically Plausible Model

In Section 4.4.4 we proposed an efficient serial algorithm for finding a suitable sparsification $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$. Although it did not explicitly optimize anything, it was based on the theoretically understandable principle to look for the strongest "surprise"-the place where the expectations fail the most; it performed extremely well in practice.

Nevertheless, there is one operation in it-the search for a global maximum- that was nonlocal. This is not a problem on a serial machine, but it will be, in a biologically plausible implementation. Also, in Section 4.4.5 we argued that the representation (4.72) is based on weakly-interacting feature clusters; intuitively, there is no real need for finding such global maxima.

Moreover, the biological wet-ware can perform parallel computations, in which many elements of the representation can be calculated concurrently and asynchronously. An obvious idea is to propose a neural network to carry the LFA calculations iteratively and in parallel.

Algorithms for sparsification have been proposed in the literature-for example, competitive learning or a winner-take-all strategy (Malsburg 1973; Grossberg 1987; Rumelhart and McClelland 1982; McClelland and Rumelhart 1981; Kohonen 1984; Touretzky 1989; Földiák 1990). Also, sparse representations have been argued to have some desirable properties, and sparseness has been previously postulated as a design principle for visual coding by many groups (Barlow 1972; Palm 1980; Barlow 1985; Baum et al. 1988; Zetzcshe 1990; Field 1994; Olshausen and Field 1996b).

In Fig. 4.9 we have described a neural network for the implementation of sparsification. The dynamics of the network is given by

$$
-\tau \frac{d}{d t} \mathcal{O}(\mathbf{x})=\mathrm{K} \phi-\mathbf{P} G(\mathcal{O})
$$

where $G(\mathcal{O})(\mathbf{x})=\mathrm{g}(\mathcal{O}(\mathbf{x}))$ with g, a suitably chosen sigmoid function, ${ }^{45}$ and $\tau$ is the characteristic time scale.

One way to choose g is such as to bring to 0 all values that are "small," and to pass the large ones intact. Then, if all $\mathcal{O}(\mathbf{x})$ either vanish, or are sufficiently large, g will be the identity. In this regime, for the steady states, $\frac{d}{d t} \mathcal{O}(\mathbf{x})=0$, we have

$$
\mathbf{P O}=\mathbf{K} \phi .
$$

The steady-state equation (4.76) is equivalent to $O^{\mathrm{rec}}=\mathrm{P} \mathcal{O}=\mathrm{K} \phi=O$ (4.73), and its restriction to $\mathcal{M}$, to the condition for the inversion of $\mathbf{Q}$ (4.74); hence, the sparsified outputs $\left\{\mathcal{O}_{m}\right\}_{x_{m} \in \mathcal{M}}$ are solutions of (4.76) and, therefore, constitute a steady state of the network.
${ }^{45}$ A sigmoid function is a monotonic nondecreasing function $\mathrm{g}: \mathcal{R} \rightarrow[a, b]$, often $a=-b$, and usually $\mathrm{g}^{\prime}$ is non-zero only near the origin, or a suitably chosen threshold $\theta$.

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-04.jpg?height=480&width=758&top_left_y=1439&top_left_x=169)
Figure 4.9: The Sparsifying LFA Neural Network
The input layer stores the example $\phi(\mathbf{x})$; the output layer, $\{\mathcal{O}(\mathbf{u})\}_{\mathbf{u} \in V}$.
The output layer unit centered at $\mathbf{u}$ has a feed-forward receptive field $\mathbf{K}_{\mathbf{u}}(\mathbf{x})$ (cf. Fig. 4.1-4.2); these are optimally matched to the object class and decorrelate as much as possible, while obeying the topography. The dense LFA outputs $O(\mathbf{x})$ are interpreted as the hidden variables of the output layer.
The current error signal $O^{\text {err }}(\mathbf{u})$ (4.71) is calculated from the current output variables $\mathcal{O}(\mathbf{u})$ by (4.72); the residual correlations $\mathbf{P}_{\mathbf{u}}(\mathbf{v})$ (cf. Fig. 4.1 4.2) serve as the basis for lateral inhibition.
Updates to $\mathcal{O}(\mathbf{u})$ are made on the basis of $O^{\text {err }}(\mathbf{u})$ until the dynamics settles to $\mathcal{O}(\mathbf{u})=0$ everywhere on the grid, with the exception of $\left\{\mathcal{O}_{m}\right\}_{m=\mathbf{I}}^{|\mathcal{M}|}$ (4.74).

Since there are many ways to choose $\mathcal{M}$ that will reconstruct $O(\mathbf{x})$ exactly, there is a whole class of solutions to (4.76). The exact fixing of this symmetry will depend on external criteria and may be implemented by a judicious choice for g, for example.

One possible requirement would be that no output variable $\mathcal{O}_{l}$ exceeds the available dynamic range of the given unit. Evidently from Fig. 4.6, the first few variables have a large dynamic range, and the rest increasingly smaller. If output dynamic range equalization is required, $g$ may be chosen to preclude large $\mathcal{O}_{i}$.

The interest in networks of this type goes beyond their ability to produce sparsification. Their underlying architecture resembles that of the prototypical cortical circuitry; hence, such methods could be a biologically plausible model for cortical coding. It would be interesting to try to see if the relationships between lateral connections, feed-forward connections, and the statistics of the input, predicted by the theory, are realized in cortical circuitry.

## Chapter 5

## Symmetries and LFA

In Chapter 4 we developed LFA-a statistically-derived low-dimensional sparsedistributed representation of objects in terms of their local features.

One of the key aspects of LFA was topography, which we hypothesized to be the condition that allows the symmetries that are not captured in PCA to manifest themselves in LFA.

In this Chapter, we will begin to explore the relationship between various symmetries of some sensory ensembles and their LFA representations.

### 5.1 Partial Re-Symmetrization of Object Ensembles

So far, we have considered two very different classes of ensembles of images. The first is ensembles of objects (Section 3.1), whose correlation functions have an exponential regime in their spectra, and are, arguably, amenable to dimensionality reduction (2.45).

The second class is ensembles with explicit translational symmetry, such as the ensemble of static natural scenes (Section 4.2), whose correlation functions have only a power-law regime in their spectra.

Interestingly, both classes of ensembles are derived from the same source- images of natural scenes (images that contain faces are natural). Arguably, there is no need look at ensembles of objects all the information in their probability distribution, $\mathcal{P}_{\text {objects }}$, is entirely contained in the probability distribution of natural images, $\mathcal{P}_{\text {images }}$.

Although true in principle, this fact is unhelpful in practice; we argued that $\mathcal{P}_{\text {images }}$ (and $\mathcal{P}_{\text {objects }}$, for that matter) are enormously hage (see discussion in footnote 6 on page 10) and that any practical dealing with them involves their approximation and parameterization. In that sense, $\mathcal{P}_{\text {object }} \mathrm{can}$ be considered a part of the explicit parameterization of $\mathcal{P}_{\text {images }}$, and the original statement becomes trivial.

Notably, the extraction of information about $\mathcal{P}_{\text {objects }}$ directly from $\mathcal{P}_{\text {images }}$ is a difficult problem. The second-order statistics of $\mathcal{P}_{\text {images }}$ (4.3-4.4) contain almost no information about $\mathcal{P}_{\text {objects }}$ (cf. Fig. 4.1-4.2); necessarily, almost all of it is contained in the higher-order statistics.

In Section 3.1 we saw that, even for ensembles of small $V$, the reliable measurement of second-order statistics is somewhat of a problem. Therefore, a proposition to embark on a project to measure higher-order statistics seems unpromising, at best.

On the other hand, the second-order statistics of $\mathcal{P}_{\text {objects }}$ are measurable, rich, and profoundly different from that of $\mathcal{P}_{\text {images }}$. How did we manage to shift this information from higher order, in $\mathcal{P}_{\text {images }}$, to second order, in $\mathcal{P}_{\text {objects }}$ ?

We argue that it is the symmetry breaking that causes the shift; indeed, the translational, scale, and rotational global symmetries have been explicitly broken in the preparation of the object ensembles we dealt with so far.

An interesting question is, How do we break the global symmetry-in general and automatically?

In trying to answer this question, we will revisit the preparation procedure for the ensembles of faces that were used in Section 3.1. First, an ensemble of images $\left\{I^{t}\right\}_{t \in T}$ was prepared, wherein each image contained a human face in a relatively frontal pose. For each image in the ensemble, $I^{t}$, the locations $\left(X_{l}^{t}, Y_{l}^{t}\right)$ and $\left(X_{r}^{t}, Y_{r}^{t}\right)$ of the left and right eye, respectively (see discussion in footnote 3 on page 24) were found. ${ }^{1}$

Subsequently, the image $I^{t}$ was rotated, by the angle $\theta^{i}$, to line the eyes horizontally; scaled, by the scale factor $S^{i}$, to bring the inter-eye distance to a pre-defined length; and translated, horizontally by $X^{t}$ and vertically by $Y^{t}$, to bring the center of segment that connects the eyes to the origin. ${ }^{2}$ Therefore, for a given cropping, the example $\phi^{t}$ depends on the image $I^{t}$, as well as on the four parameters

$$
\alpha^{t}=\left(\theta^{t}, S^{t}, X^{t}, Y^{t}\right) .
$$

This dependence can be signified by

$$
\phi^{t}=H\left(I^{t} ; \alpha^{t}\right)
$$

where $H$ is the (highly monlinear) operator of symmetry-breaking.

### 5.1.1 Re-Symmetrization and PCA

Notably, with this approach, the unavoidable errors in the determination of the eye locations, $\left(X_{l}, Y_{l}\right)$ and $\left(X_{r}, Y_{r}\right)$, lead to errors in $\alpha$. Also, if $H\left(I^{t} ; \alpha^{t}\right)$ is in the ensemble of faces, then $H\left(I^{t} ; \alpha^{t}+\Delta \alpha\right)$ will also be in it, provided that $\Delta \alpha$
${ }^{1}$ See footnote 8 on page 101.
${ }^{2}$ The aligned images have been subsequently cropped, as outlined in Appendix A.1.

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-05.jpg?height=432&width=866&top_left_y=94&top_left_x=1039)
Figure 5.1: PCA Analysis of Ensemble $6(T=10944, V=3840)$

The first 16 eigenmodes $\left\{\Psi_{r}(\mathbf{x})\right\}_{r=1}^{16}$ of Ensemble 6 (top and middle) and eight of the rest (bottom). See Appendix A. 1 for description of the images in it. This figure is reproduced on Plate $2 A$. For comparison, part of Fig. 3.9 is reproduced on Plate $2 B$.

Notably, the first eyebrow mode is now very strong $\Psi_{8}$. This is due to an important fact: the weak scaling (at most 10\%) that was applied in the preparation of the ensemble changes the characteristic sizes of the local features only weakly; what changes most is the location of the features, especially the ones that are most distant from the origin. ${ }^{3}$

A very interesting effect on the asymmetric $\Psi_{12}$ (Fig. 3.9), the first strong feature therein, can be observed-it has moved one mode down to $\Psi_{13}$ in the symmetrized ensemble, has weakened, and has spread to two more modes: $\Psi_{14}$ and $\Psi_{18}$. The same has happened to $\Psi_{14}$, the "Nixon" mode (footnote 11 on page 34) weak vestiges of it can be observed on $\Psi_{14}, \Psi_{15}, \Psi_{16}$, and $\Psi_{18}$.

This weakening and mixing of modes is something to be expected under symmetry transformations. ${ }^{4}$ It has one important consequence-even if a cer-

[^5]![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-06.jpg?height=281&width=870&top_left_y=94&top_left_x=103)
Figure 5.2: Successive reconstruction in the cross-over regime of Ensemble 6

The successive reconstructions $\phi_{N}^{\text {rec }}$ labeled with their SNR (top) and their respective residual errors $\phi_{N}^{\text {err }}$ (bottom) for Example 1 (Fig. 3.10-original).
The first four errors are magnified 5× and the last 20×.
The same dependency is shown on Fig. 3.12 for Ensemble 1.
This figure is reproduced on Plate 2C.

### 5.1.2 Re-Symmetrization and LFA

The fact that enforcing scale symmetry, which acts locally as translational symmetry, ${ }^{6}$ helps reveal the structure of $\mathcal{P}[\phi(\mathbf{x})]$, suggests also that there might be components in this structure that are even simpler and lower-dimensional than apparent from the symmetrized PCA representation.

One obvious idea is to check the dense LFA receptive fields and correlators (4.29). One intuitive result would be that, because of the imposed scale/translational symmetry, the receptive fields will look more like the retinal receptive fields wider and more "circular."

The LFA analysis of Ensemble 6, shown on Fig. 5.4, supports quite a different conclusion. Although some circularizing has happened, most pronounced on (d) and (a), also on (b), and, arguably, on (c), the main development from Ensemble 1 (bottom row) is that the topographic kernels (4.29) have much tighter local supports.

On a second though, this is not entirely unexpected. Indeed, in both the asymmetric and the symmetrized ensembles, the most substantial contribution of the variability at location (a) is due to mouths; at location (b), to noses; at (d), to object-background transitions; hence, the receptive fields have not changed substantially. ${ }^{7}$

[^6]![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-06.jpg?height=861&width=873&top_left_y=153&top_left_x=1037)
Figure 5.4: Receptive Fields K and Residual Correlations P for Images of Faces, Ensemble 6
positions: $\Psi_{1}$, the "average" of the examples, of Ensemble 6 (Appendix A.1), is marked with the respective positions $\mathbf{x}_{0}$ for $a \quad e$.
a $e$ : Five receptive fields $K\left(\mathbf{x}_{0}, \mathbf{y}\right)=\mathbf{K}_{\mathbf{x}_{0}}(\mathbf{y})=\left(\mathbf{K}, \hat{\mathbf{x}}_{0}\right)$ (cf. 4.25) (top row) and correlators $\mathbf{P}_{\mathbf{x}_{0}}(\mathbf{y})$ (middle row) at the five choices for $\mathbf{x}_{0}$. The parameters are $(T=10944, V=3840), N=400$, and $n=\sigma_{400}$ (see Fig. 4.1).
The locations $\left\{\mathrm{x}_{0}\right\}$ were chosen to be the same as those on Fig. 4.1, whose bottom row, $\mathbf{P}_{\mathbf{x}_{0}}(\mathbf{y})$, is reproduced here (bottom row) for comparison.
Part of this figure is reproduced on Plate 2D.

100
"topography" with the understanding and the hope that, if such symmetries, indeed, existed, they would manifest themselves in the LFA representation.

In the light of this discussion, the results on Fig. 5.4 tell us two things: first, that such symmetries do, indeed, exist; and, second, that LFA has done at least a moderately good job in preserving and exposing them.

### 5.2 Bootstrapping the Local Symmetry Breaking

In Section 5.1 we understood the preparation of a particular ensemble of images of objects as the result of the action of the global-symmetry-breaking operator $H(I ; \alpha)(5.2)$ on the set of images $\left\{I^{t}\right\}_{t \in T}$. In the restricted sense, used for the ensembles in Chapter 3, the symmetry breaking was parameterized by the set of coefficients $\left\{\alpha^{t}\right\}_{t \in T}(5.1),{ }^{8}$ and one example $\phi^{t}$ was included in the respective ensembles for each image $I^{i}$.

Later in Section 5.1, we argued that a given ensemble contains not only the objects $\left\{\phi^{t}\left(\alpha^{t}\right)\right\}_{t \in T}$, but also all objects $\left\{\phi^{i}(\alpha)\right\}_{t \in T^{\prime}, \alpha \in \Delta_{\alpha^{l}}}$, where $\Delta_{\alpha^{i}}$ is suitably chosen closely around $\alpha^{t}$. In all cases, the probabilities $\mathcal{P}\left[\phi^{t}(\alpha)\right]$ were determined in the context of PCA by the projector on the PCA $S$-subspace $\mathbf{P}^{\prime}$ (2.33), suitably truncated to dimensionality $N$ (2.45).

Although it has always been clear that the locations of the eyes are only a "good hint" for the parameter of the symmetry breaking $\alpha$ (see discussion in footnote 3 on page 24), in the context of symmetrization, one can try to find the parameter for a "best" breaking.

### 5.2.1 Automatic Symmetry Breaking for a Single Example

Again, it is possible to employ the idea of finding a maximum likelihood estimate of $\alpha$ : in the context of any given ensemble with dimensionality $N$ (2.45), for a given image $I$ and an initial guess $\alpha_{0}$, calculate the entropic costs (2.49)

$$
N\langle S\rangle(N, \alpha)=\left\|\Phi_{N}^{*+} \phi(\alpha)\right\|_{S}^{2} .
$$

for all images $\{\phi(\alpha)\}_{\alpha \in \Delta_{\alpha_{0}}}$. The maximum likelihood estimate is $\alpha$ that minimizes $\langle S\rangle(5.4)$ and, therefore, maximizes the probability $\mathcal{P}[\phi(\alpha)]$ (2.20).

[^7]![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-07.jpg?height=578&width=820&top_left_y=101&top_left_x=130)
Figure 5.5: $S-N$ Diagrams and Scale Symmetry Breaking ( + )

The average entropic cost $\langle S\rangle\left(N, \alpha_{h}^{t}\right)$ (5.4) is plotted as a function of $N$ for 7 different choices of $\alpha_{h}^{t}$ (5.5) for one of the images $I^{t}$ in Ensemble 6 (see Appendix A. 1 for definition).
The vertical axis is additionally scaled so that the in-sample example $\phi^{t}(0)(==)$ has $\langle S\rangle(N) \rightarrow \frac{\sigma_{0}{ }^{2}}{\sum_{r=1}^{N} \sigma_{r}{ }^{2}}$ when $N \rightarrow T$, instead of the more usual, 1.
The six out-of-sample examples $\phi^{t}\left(h_{n}\right)$ were produced with $h_{n}=1-s_{n}, s_{n}=$ $1.05^{n / 2}$, for $n \in\{-3,-2,-1,1,2,3\}$, as outlined in Appendix A.1.

The results of this approach in the context of Ensemble 6 (see Appendix A. 1 for definition) are shown on Fig. 5.5. For all 1216 images $I^{t}, \alpha^{t}$ was determined. From each $\alpha^{t}$, several examples $\phi^{t}(h)=H\left(I^{t} ; \alpha_{h}^{t}\right)$ were produced with

$$
\alpha_{h}^{t}=\left(\theta^{t},(1+h) S^{t}, X^{t}, Y^{t}\right)
$$

as outlined in Appendix A.1. Only the examples $\left\{\phi^{t}(0)\right\}$ were used to derive the modes, hence $T=1216$.

Two effects can be observed. First, the in-sample effect causes $\langle S\rangle(N) \rightarrow 1$ with $N \rightarrow T$ for $h=0$. Also, for smaller deviations from in-sample-ness $|h|$, the entropic cost of the un-truncated representation, $\langle S\rangle\left(T_{i} \alpha_{h}\right)$, is generally smaller than, for larger deviations.

Second, for the "reasonable regime" $N \in[350,750]$, the out-of-sample example $\phi^{t}\left(h_{+1}\right)$ is more probable than the in-sample example $\phi^{t}(0)$. Therefore,

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-07.jpg?height=601&width=809&top_left_y=1437&top_left_x=137)
Figure 5.6: $S-\log N$ Diagrams and Scale Symmetry Breaking ( + )

The dependencies from Fig. 5.5 are plotted on a log scale for $N$. Four of the examples $\phi^{t}\left(h_{n}\right)$, with $n \in\{-4,-3,3,4\}$, have been substituted with the examples $\phi^{t}\left(h_{m}\right)$ from Ensemble 7 (see Appendix A. 1 for definition) with $h_{m}=$ $1-s_{m}, s_{m}=1.025^{m / 3}$. In this notation, $n=1$ produces almost the same example as $m=3$.
The values of $m$ are: -2 , labeled with $(--) ;-1(-=) ;+1(+=)$; and $+2(++)$.
for a reasonable truncation $\alpha_{+1}^{t}$ is a better parameter of symmetry breaking than $\alpha^{i}$.

Fig. 5.6 is an illustration of the fact that, unless there is a procedure for determining the dimensionality $N$ for the "best" truncation (2.45), and unless the in-sample effect is accounted for, one cannot easily determine an exact optimal value for $h$.

Evidently, due to the in-sample effect, different values for $\alpha_{h}^{t}$ are best for different regimes of $N$. Nevertheless, the asymmetry is obvious-for all dimensionalities $N, h_{\text {best }}(N)>0$. Also, very big values of $|h|$ result in very improbable examples.

From the discussion so far, one can conclude that, for any given value of $N$ in the "reasonable" regime, $\langle S\rangle\left(N, \alpha_{h}^{t}\right)$ has a local minimum as a function of $h$, and, therefore, an optimal breaking of the symmetry can be determined. This is shown on Fig. 5.7.

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-07.jpg?height=580&width=809&top_left_y=91&top_left_x=1065)
Figure 5.7: Representational Entropy and Scale Symmetry Breaking (+) The average entropic cost $\langle S\rangle\left(N, \alpha_{h}^{t}\right)$ (5.4) for the image $I^{i}$ from Fig. 5.5 is plotted as a function of $h$ for several different choices of $N$.

Evidently, for all $N,\langle S\rangle\left(N, \alpha_{h}^{t}\right)$ has a local minimum for $h>0$. As $N$ increases, this minimum is achieved for $h \approx+1.5 \%$, and is forced to $h=0$ as the in-sample effect takes over. Therefore, one can conclude that $h=1.5 \%$ is close to the optimal symmetry breaking of this example for a wide range of dimensionalities $N$.

A similar situation can observed on Fig. 5.8 for another image, $I^{t}$; this time, the optimal scaling is in the other direction.

It is encouraging to assume that, once the in-sample effect has been taken into account (for example by symmetrization of the ensemble as in Section 5.1, which will result in $T>N$ ), there will be one optimal value of $h$ for all $N$. A weaker result, equally useful in practice, is more plausible: for a large regime of $N$, the optimal value of $h$ changes very little.

### 5.2.2 Bootstrap Mechanism for Spontaneous Symmetry Breaking

In Section 5.2.1 we parameterized the symmetry breaking $\alpha$ with one parameter, the deviation $h$ from the hand-determined scale, and, for a given image $I^{t}$,

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-07.jpg?height=601&width=809&top_left_y=1430&top_left_x=1074)
Figure 5.8: Representational Entropy and Scale Symmetry Breaking (-) The same dependencies as on Fig. 5.7 are plotted for another image, $I^{t}$.

studied $\phi^{i}(h)$. In this manner, for each image $I^{t}$, we produced the trajectory $\left\{\Phi^{*+} \phi^{t}(h)\right\} \subset S$.

We interpreted the square of the distance between the points on the trajectory and the origin, $\left\|\Phi^{*+} \phi^{t}(h)\right\|_{S}^{2}$ as the entropy (2.20) of the example $\phi^{t}(h)$ in the context of a given ensemble. Further, according to the principle of the maximum likelihood, we decided that the point on the trajectory that is closest to the origin constitutes the "best" symmetry breaking.

In general, $\alpha$ has $k$, more than one, independent components for the special case discussed in Section 5.1 they are four (5.1)-and $\phi^{l}(\alpha)$ is a $k$ dimensional manifold, embedded in the $N$-dimensional PCA $S$-subspace (2.33). ${ }^{9}$

For a given image $I$, the entropic cost of the PCA representation of the points on the manifold $\Phi^{*+} \phi(\alpha)$ is a function of $\alpha-S(\alpha)$. On one hand, for values of $\alpha$ that are very wrong, the probability that $\phi(\alpha)$ is in the ensemble will be very low and $S(\alpha)$ will be very large a tree is not a face, as well as a large nose is not a face, as well as a tilted face is not a vertical face-and one can find a reasonable threshold $S_{\text {max }}$ and a finite compact region on the manifold $\Delta$, such that $\left\{\alpha \mid S(\alpha)<S_{\max }\right\} \subset \Delta$.

[^8]On the other hand, $S$ is a square of a length and is always positive, therefore it is bounded from below by 0 . For many systems, $S(\alpha)$ will be continuous, and with $S(\alpha)$, bounded from both above and below on $\Delta$, there will be at least one $\alpha$ for which $S(\alpha)$ will have a global minimum. This value will be the optimal parameter for the symmetry breaking.

In general, the "landscape" $S(\alpha)$ could be extremely "rugged"-with many local minima-and finding the global one could be difficult. Nevertheless, we showed that, for an ensemble of faces, and for a simplistic parameterization of $\alpha$, and for a reasonable choice for $N$, and for a reasonable initial estimate $\alpha_{G M}^{t}$. (footnote 8 on page 101), there was one well-defined, smooth local minimum, which was also global (Fig. 5.7 and Fig. 5.8).

Therefore, it is not unreasonable to assume that, given an image $I$, once a good initial estimate $\alpha_{0}$ has been generated, a rapid gradient-descend iteration can be performed, by a method with good convergence and with knowledge of the shape of the minimum, to find a well-aligned example $\phi$.

What could serve as the $\alpha_{0}$-hypothesis generator? Fig. 5.6 shows that the projection of $\phi(\alpha)$ to the first few eigenmodes is almost the same for a broad range of values for $\alpha$. One could imagine a fast scan of the visual field utilizing them, or even, only $\Psi_{1}$, to generate an $\alpha_{0}$-hypothesis. Also, since these are exactly the modes that are smooth (Fig. 5.1), subsampling them aggressively would produce only small errors in the result, therefore a fast scan may be possible indeed. ${ }^{10}$

We have argued so far, that, given prior knowledge of a sensory ensemble of objects, good alignments can be performed robustly and self-consistently. What will happen if the prior knowledge of the ensemble is not very good? Suppose that the knowledge extends only up to $N \approx 10$. In that context, only moderately good alignments can be found, and much of the signal power and, therefore, identity, of the examples will not be accounted for.

Nevertheless, from the source of images $I^{t}$, an ensemble $\phi^{t}$ will be created. It will be a heavily-symmetrized ensemble (Section 5.1), and, as such, highly-dimensional. By monitoring $\phi^{t}$ for some time, the sensory system can learn the statistics of the symmetrized ensemble and reliably increase the dimensionality $N$. In the context of the new ensemble, subsequent examples will be represented better (with more signal power accounted for, and at a lower entropic cost), and their aligument will be better.

The better ensemble will produce even better-aligned examples, which in turn will produce an even better ensemble, and so on. At the end, the process will converge to a high-quality ensemble that can break the symmetry and represent the examples very well. The whole process of representing examples and redefining the ensemble may be an iterative process of learning-developmental algorithms have been proposed both for finding the first $N$ Principal Compo-
${ }^{10}$ Of course, once a head is located, it can be tracked the old value of $\alpha$ can serve as the $\alpha_{0}$-hypothesis for the current one.

106 nents (Oja 1989; Földiák 1989) and for the finding of the LFA receptive fields in the non-degenerate case (Atick and Redlich 1993).

How much information is needed to seed the bootstrap? Turk and Pentland (1991) report head tracking with $N$, as low as 8. Judging from the quality of the ensemble they have used (Fig. A.3), we believe that what is at work there is just $\Psi_{1}$, a very poorly defined version of $\Psi_{1}$. Thus, we believe that a low-resolution version of $\Psi_{1}$ can be used to seed the bootstrap for the ensemble of human faces.

Is, then, $\Psi_{1}$ stored in our genes somehow? On one hand, here is a face-specific area in the cortex of primates (Nachson 1995), so at least something may be, indeed, genetically stored.

On the other hand, there is a possibility that the representation of faces can be learned almost entirely from visual experience. Indeed, under natural conlitions, the post-natal life of a human baby begins with nursing; human babies initially nurse throughout the most part of their alert time, and the nursing positions are such, that the mother and the baby have constant eye contact from a close distance (Pryor and Pryor 1991). Therefore, it is reasonable to say that the ensemble of visual stimuli for a human infant is dominated by a symmetrized ensemble of a human face Mommy's.

Notably, this ensemble is surprisingly well aligned. First, because of the close nursing position, the human face usually occupies a good part of the entire visual field, and there is not need to scan it with $\Psi_{1}$. Second, because of the eye contact, the example is centered at the fovea and, therefore, the ( $X, Y$ ) part of the parameter of symmetry-breaking $\alpha$ (5.1) is determined very well. Third, also because of the eye contact, $\theta$ is determined very well. Fourth, the head is usually rendered under diffused lighting conditions, so there is no variability due to the strong "Lambertian" mode $\Psi_{3}$ (Fig. 3.9) and its symmetrizations. Fifth, the bootstrap can be started with a very close cropping, slightly closer that third (Fig. 3.5), more like the one used in (Sirovich and Kirby 1987), so that other strong irrelevant modes the background modes $\Psi_{2}, \Psi_{4}$, and $\Psi_{5}$, and their symmetrizations are out of the way. Sixth, modes due to identity variations, race, and gender, are not present in this ensemble. ${ }^{11}$

The strongest-varying parameter of this initial face ensemble is the scale, which, due to the nursing position, does not vary much. Overall, this ensemble is low-dimensional, symmetrized by a small range of $\alpha$, which, itself, is parameterized one-dimensionally.

Having the controlled nature of the bootstrap ensemble in mind, How much genetic storage is needed? Not very much, we will hypothesize; even a blurry light blob with two darkenings placed symmetrically across the vertical axis

[^9]will suffice-a very frugal definition of $\Psi_{1} .{ }^{12}$

### 5.3 Hierarchical LFA Assemblies

In Chapter 3 we showed that PCA (2.47-2.52), a one-stage redundancy-reducing code, can also be utilized to reduce the dimensionality of ensembles of objects. In Section 5.1 we understood the preparation of such object ensembles as the act of explicit breaking of certain symmetries, present in the more general sensory ensemble of images. Further, we understood this as a parameterization of the symmetric probability density $\mathcal{P}_{\text {images }}$ by the asymmetric object density, $\mathcal{P}_{\text {objects }}$, and the symmetric density of the parameter of the breaking $\alpha, \mathcal{P}_{\alpha}$.

In Section 5.2.1 we argued that, under relatively mild conditions, the process of symmetry breaking is input driven-a crude initial guess $\alpha_{0}$ is necessary for the rapid subsequent finding of the optimal parameter $\alpha$ in an unsupervised manner.

In Chapter 4 we argued that, even after the breaking of the global symmetries, there are local, partial symmetries that are still present in the ensemble of objects, and that cannot be represented naturally in the context of PCA. To cope with this problem, we developed LFA (4.29)-a two-stage redundancy-reducing code, which has all of the desirable properties of PCA, and also preserves some symmetries of the ensemble, which are uncaptured by PCA.

The second stage of LFA, sparsification, reveals those symmetries explicitly, providing a representation of the objects in terms of their local features (4.73). For each example, this representation can be thought of as a set of weakly-interacting features, each represented by a localized cluster of a small number of values and their locations Fig. 4.4.

Here, we want to understand the location of the cluster for a given feature, $\beta_{\text {feature }}$, as a parameter for the breaking of the local symmetry. Analogously, we want to understand this symmetry breaking as a definition of a new sensory ensemble, this time of features, and also, its probability density $\mathcal{P}_{\text {feature }}$, along with the probability density $\mathcal{P}_{\beta}$, as a parameterization of $\mathcal{P}_{\text {objects }}$.

In this scenario, the output of a given LFA representational module for objects will serve as the input for other representational modules for the local features. This is analogous to the way the output of the retinal representation, of images, serves as the input to the cortical representations, of objects. ${ }^{13}$

[^10]statistical knowledge. A possible solution would be to categorize the examples and construct two different ensembles. Notably, they will have the same local statistics at one part of the receptor grid, and profoundly different, at another. Keeping them entirely separated is wasteful. One possibility is to keep separate LFA kernels only at the places where their local statistics differ. Such an arrangement will create two feature representational modules (one, for eyeglasses; the other, for cheekbones) that look at the same place of the receptor grid. ${ }^{17}$

The problem that arises is, how to sort out which one to take control when. In Chapter 3 we developed the $S-U$ diagram-a tool to gauge the probability of an example in the context of a given ensemble. It is easy to imagine that the eyeglasses feature module can have a mechanism to activate itself only upon sufficient evidence of the presence of eyeglasses. It will, then, suppress the cheekbone feature module and take control over the representation.

The full suppression of the cheekbone module may not be very wise, however- eyeglasses are basically thin lines along the rims, and will account for only a small percentage of the variance in the region; the cheekbone module still needs to be activated to account for the rest of it.

The way to resolve this is to have the eyeglasses module project back its notion of what the reconstruction of $O(\mathbf{x})$ should look like. The object module will then calculate $O^{\text {err }}(\mathbf{x})$ and will feed it to the cheekbone module for subsequent representation.

This way, the individual feature modules do not need to interact among themselves; they all sift the input $O(\mathbf{x})$ for the presence of their respective features, represent them internally, and post the reconstruction $O^{\text {rec }}(\mathbf{x})$ to the object module, which aggregates all reconstructions, calculates the residual $O^{\text {err }}(\mathbf{x})$, and posts it for further rounds of "explanation." ${ }^{18}$

In the outlined model of hierarchical LFA interconnections, the object module serves as an active blackboard, analogous to the role of active blackboards in the model of the thalamo-cortical and cortico-cortical loops suggested by Mumford (1991, 1992). This raises the possibility that the actually observed cortical architecture could, efficiently and naturally, implement assemblies of
${ }^{17}$ In this treatment, we are departing from strict topography (4.6). This is not a big problem-we understood topography only as the hope for locality, which was, indeed, achieved by topography and the simplistic fixing of the $U$-symmetry (4.16); as long as we know how to keep the receptive fields local, strict topography is not a strict requirement. This comment is taken a step further in footnote 37 on page 127.
${ }^{18}$ There is one problem associated with this approach the cheekbone module will try to reconstruct the whole region and will, inevitably, make an mistake in the eye rims. The face module needs to know that this error should not be taken seriously, since it is the eyeglasses module that provides the primary description. One way to do this is to mark the regions with their ownership and calculate errors only for the owner module. Transitions in ownership should happen, in general, only at the boundaries of objects. Boundary ownership is a well-known and actively-studied phenomenon (Nakayama 1996); it happens at least as early as V2, most probably in V1-the earliest visual cortical area.

LFA representational modules.
In this section, we have outlined an architectural and functional analogy between a hierarchical system of LFA representational modules and a model of the computational architecture of the neocortex. Does that mean that we are ready to suggest a neurophysiological experiment to test this analogy?

The brain is an actual information processing device, built and operated in practice, and, besides possible computational goals, it has to conform to certain engineering constrains, such as evolutionary history, developmental feasibility, occupied volume in the 3D physical space before and during birth, energy supply, heat dissipation, and many others. Unless we have a clear understanding of the compromises due to the constrains, making predictions at the level of single cell activities is somewhat premature.

Nevertheless, the computational ideas discussed here may be tested in simpler systems, and we will suggest a possibility in Section 5.6.

### 5.4 Dimensionality Reduction in Fully-Symmetric Ensembles by Multi-Scale LFA

In Chapter 3, we applied PCA (Chapter 2) to ensembles of objects, such as the ensemble of images of human faces, to produce representations with reduced dimensionality (Fig. 3.11). In Section 4.4.3 we applied LFA (Chapter 4) to the same ensembles to produce representations whose dimensionality is lower than that of the equivalent PCA representation (Fig. 4.5-4.7).

In Section 4.2 we considered globally symmetric sensory ensembles, such as the ensemble of static natural scenes, for which PCA could not reduce dimensionality. It would be interesting to know whether LFA can be used for dimensionality reduction in such cases.

Key in reducing the PCA dimensionality was the experimental fact that a typical dense topographic output $O(\mathbf{x})$ was reconstructed very well from a few values in a sparse subset $\mathcal{M} \subset V$ of the receptor grid $\{\mathbf{x}\}_{\mathbf{x} \in V}$ (Fig. 4.6). An obvious idea would be to apply the sparsification algorithm (Section 4.4.4) to the dense LFA outputs $O(x)$ in the context of a symmetric ensemble, such as the retinal.

The immediate problem is that the reconstruction $O^{\text {rec }}(\mathbf{x})$ (4.73) uses the residual correlations $\mathbf{P}=\mathbf{O}^{*} \mathbf{O}(4.28)$, and, in the symmetric case, their support collapses to the point in the center, $\mathrm{O} * \mathrm{O}=1(4.12)$. Therefore, the knowledge of the values $\left\{O\left(\mathbf{x}_{\boldsymbol{m}}\right)\right\}_{\mathbf{x}_{\boldsymbol{m}} \in \mathcal{M}}$ does not provide any information about the rest the outputs $O(\mathbf{x})$ are fully decorrelated, which was, actually, the initial design goal of the topographic representation (4.26) (Atick and Redlich 1992).

Since the symmetric ensembles can be fully decorrelated, and, arguably, LFA cannot be applied to sparsify them and reduce their dimensionality, is it already time to abandon the second-order statistics, and start looking into the higher orders?

In answering this question, we turn again to the architecture of the peripheral nervous system. A prominent feature of early neural processing of visual and auditory signals in primates is its multi-scale organization. ${ }^{19}$ Each neuron that participates in a multi-scale representation of the sensory signal is sensitive to only a part of the signal-that lies within a certain frequency band, $\mathrm{f} \in \Delta_{j}$. Therefore, the correlation function of the sensory ensemble $\Phi_{j}$, as seen by a neuron in the $j$-th frequency band, is $\mathbf{R}_{j} \equiv \mathbf{K}_{j}^{(-2)}$ with (cf. 4.27)

$$
\mathbf{K}_{j}^{(n)}=\sum_{\mathbf{f} \in \Delta_{j}} \Psi_{\mathbf{f}}\left(\frac{1}{\sigma_{\mathbf{f}}}\right)^{n}\left(\Psi_{\mathbf{f}},\right) .
$$

The sensory signal that a multi-scale neuron sees is $\phi_{j}=\mathbf{P}_{j} \phi$ with $\mathbf{P}_{j}=\mathbf{K}_{j}^{(0)}$, the projector to the subspace spanned by the frequencies in the $j$-th band. Now, the outputs of the action of $\mathrm{K}_{j}=\mathrm{K}_{j}^{(1)}$ on $\phi_{j}$ is ${ }^{20}$

$$
O_{j}=\mathbf{K}_{j} \phi_{j}=\mathbf{K}_{j} \mathbf{P}_{j} \phi=\mathbf{K}_{j} \phi
$$

and the residual correlations of these outputs are (cf. 4.28) ${ }^{21}$
${ }^{19}$ Most of the cells in the earliest cortical area that processes visual signals, V1, respond selectively, to stimuli of spatial frequencies in a given band-they are silent to stimuli of both higher and lower frequencies (Hubel and Wiesel 1968). Although the bandpass processing is usually associated with cortical processing, even the ganglion cells in the retina have receptive field sizes that vary in size, with eccentricity, (Wässle and Boycott 1991).

The situation is very similar in early auditory processing-the sound pressure waves excite mechanically the sar drum, which, in turn, generates pressure waves in the cochlea; it resonates at different frequencies along its length and stimulates, mechanically, the array of auditory neurons, wherein each neuron receives stimulation only from the part of the signal that lies in the respective frequency band (Dallos 1992).
${ }^{20}$ Notably, $j$ is not a substitute for the receptor grid index x in $O(\mathrm{x})$; there are several bandpassed dense LFA outputs $O_{j}$, which collectively carry the information that was previously carried entirely by $O$. When we want to emphasize their dependence on $\{\mathbf{x}\}$, we will write $\left(\hat{\mathbf{x}}, O_{j}\right)=O_{j}(\mathbf{x})$. For the ensemble of monaural sound, x is the time index $t$; for the static natural images, the pair $(x, y)$; for the dynamic natural "movies," the triplet $(x, y, t)$.
${ }^{21}$ Here, we are not addressing the possibility that the bands $\left\{\Delta_{j}\right\}$ may happen to be nondisjoint, which will generate some cross-talk between different bands; we are not asking the question what $\mathrm{O}_{j}^{*} \mathrm{O}_{k}$ is for $j \neq k$.

Indeed, for the auditory case, neighboring cell are activated from neighboring parts of the cochlea, whose sound-frequency tunings will be overlapping (this is very similar to the overlapping light-frequency tunings of the three visual pigments in humans). For the visual case, the receptive field sizes of cells in cortical area V1 vary gradually, and, therefore, respond with overlapping spatial frequency tuning curves (Hubel and Wiesel 1974). For the degenerate case of object ensembles (footnote 22 on page 113), cross-talk between bands is needed to pick up the information content that is left after the application of sparsification in the "lower" band.

One way to deal uniformly with all cases is through the "noise suppression" factor $F_{r}$ (see Fig. 4.1 and footnote 17 on page 62), which, anyway, has to be present in practical applications.

$$
\mathbf{O}_{j}^{*} \mathbf{O}_{j}=\mathbf{P}_{j} \neq \mathbf{1} .
$$

This is remarkable-the projector to the signal subspace, which is also the residual correlation function of the dense LFA outputs, is no longer 1. Therefore, $O_{j}$ is amenable to sparsification, and there is, indeed, hope for dimensionality reduction of fully-symmetric ensembles (cf. Fig. 4.6).

Let us look back and see what happened. Initially, the sensory ensemble was fully-symmetric and, therefore, non-degenerate (see discussion in footnote 16 on page 61); it could be decorrelated fully $(\mathbf{P}=\mathbf{1})$ by the retinal filters (4.26), but no dimensionality reduction was possible precisely because of that - the support of P had been collapsed to the receptive field center. When the input $\phi$ is split among the bands $\left\{\Delta_{j}\right\}$, resulting in $\left\{\phi_{j}\right\}$, so is the dense LFA output, $\left\{O_{j}\right\}$. So far, the dimensionality has not changed the dimensionalities of the bands sum up to the dimensionality of the original space. Nevertheless, within each band, the output $O_{j}$ is degenerate and, therefore, amenable to sparsification. One can confidently hypothesize that, within each band, the dimensionality can be reduced by sparsification, hence, the total dimensionality of the signal will be reduced. ${ }^{22}$

Notable in this scenario, both the band-passed signal ensembles $\Phi_{j}$, and the respective output ensembles $\mathrm{O}_{j}$, are symmetric. The multi-scale processing neither reduces dimensionality, nor breaks the symmetry by itself; it just produces degenerate enables, thereby setting the stage for sparsification. Only after a specific example $\phi$ has been presented and the degenerate outputs $O_{3}$ have been calculated, dynamic sparsification both reduces the dimensionality and breaks the symmetry. This symmetry breaking happens in an unsupervised manner, therefore we call it input-driven symmetry breaking. ${ }^{23}$

An interesting question is, Does dimensionality reduction happen, because the initial neural processing is multi-scale, or is the initial neural processing multi-scale, because dimensionality reduction has been a design goal for the nervous system?

Reasons for the existence of multi-scale representations have been put forward previously. Li and Atick (1994) argue that multi-scale representations of visual signals posses an important for recognition property: objects constancy

[^11]under changes in scale, the neural activity due to an object preserves its pattern of activation, which only shifts from one group of cells to another. Therefore, although the object can be encountered at any scale in the sensory input, its representation has the same characteristic signature. ${ }^{24}$ With that design goal in mind, Li and Atick (1994) suggested a particular class of multi-scale representations. ${ }^{25}$

Interestingly, to say that objects can appear at all depths in the visual field (and, therefore, scales in the retinal image) and that phonemes can appear at many different frequency bands, is to say that the probability densities of the respective ensembles contain symmetries. LFA is just the mechanism to make those symmetries explicit, break them, reduce the dimensionality, and re-parameterize the underlying probability densities.

### 5.5 Successive Sparsification

In Section 4.4.6 we proposed a neural network (Fig. 4.9) for parallel sparsification. Its goal was, given the dense LFA outputs $O(\mathbf{x})$, to choose a set of active units $\mathcal{M}$, such that the subsampling $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$ is sufficient to reconstruct $O(\mathbf{x})$ up to some pre-determined fidelity measure. We interpreted the reconstruction as either the set of interpolation reconstructors $\left\{a_{m}(\mathbf{x})\right\}_{x_{m} \in \mathcal{M}}(4.68)$ scaled by the values in the subsampling (4.67), or as the set of output layer activities $\left\{\mathcal{O}_{m}\right\}_{x_{m} \in \mathcal{M}}$ (4.72), scaled by the coefficients of lateral interaction $P_{m}(\mathbf{x})(4.73)$.

We defined the dynamics of the network (4.75) with regard to continuous time, thereby implicitly assuming that the activity of the units will change gradually. In most real neurons, information propagation from one neuron to another is triggered by action potentials (spikes), which are discrete events in time, each one carrying a finite amount of information in this sense, we may think that the continuous dynamics happens at the level of sub-threshold activation, and that once a unit is included in the reconstruction set, it emits a spike. ${ }^{26}$

[^12]It would be interesting to know what the changes are to the reconstruction, resulting from the activation of a single additional unit.

### 5.5.1 Successive Inversion

We will consider the case when $|\mathcal{M}|=M-1$ units are currently active and the $M$-th one is being activated. ${ }^{27}$ Then, two things happen in the reconstruction $O^{\text {rec }}(\mathbf{x})$ with (4.67-4.68): an additional, $M$-th, interpolating reconstructor is generated; and corrections to the old $M-1$ reconstructors are made.

The new reconstructor and the corrections to the old ones depend on the inversion of the matrix $\mathbf{Q}(4.63)$ and the correlators $P_{m}(\mathbf{x})(4.68)$; the latter stay the same, but $\mathbf{Q}^{-1}$ needs to be re-calculated each time. Nevertheless, in Section 4.4.4 we mentioned that the inversion can be done iteratively (foottote 41 on page 84). We will proceed to study incremental inversion step of inversion after addition of a single active unit by partitioning $\mathbf{Q}$ (Noble 1992; Press et al. 1992).

In general, for $n=n^{\prime}+n^{\prime \prime}$, any $n \times n$ matrix $W$ can be partitioned as

$$
W=\left[\begin{array}{cc}
w & x \\
y & z
\end{array}\right]=\left[\begin{array}{cc}
1_{n^{\prime}} & 0 \\
y w^{-1} & 1_{n^{\prime \prime}}
\end{array}\right]\left[\begin{array}{cc}
w & x \\
0 & \tilde{z}^{-1}
\end{array}\right]
$$

with

$$
\tilde{z}^{1}=z \quad y w{ }^{1} x
$$

where $\mathbf{1}_{n^{\prime}}$ is the $n^{\prime} \times n^{\prime}$ unit matrix; analogously for $\mathbf{1}_{n^{\prime \prime}}$; and the partitioning sub-matrices, denoted with small letters, have congruent sizes, respectively. From now on, we will drop the notation about the dimensions, implicitly understanding that they are as in (5.9). Then, for the inverse $W^{-1}$, we have

$$
\begin{aligned}
W^{1} & =\left[\begin{array}{cc}
w^{1} & -w^{1} x \tilde{z} \\
0 & \tilde{z}
\end{array}\right]\left[\begin{array}{cc}
1 & 0 \\
-y w^{-1} & 1
\end{array}\right]= \\
& =\left[\begin{array}{cc}
w^{-1}+w^{-1} x \bar{z} y w^{-1} & -w^{-1} x \bar{z} \\
-\tilde{z} y w^{-1} & \bar{z}
\end{array}\right]= \\
& =\left[\begin{array}{cc}
w^{-1} & 0 \\
0 & 0
\end{array}\right]+\left[\begin{array}{cc}
w^{-1} x \tilde{z} y w^{-1} & -w^{-1} x \tilde{z} \\
-\tilde{z} y w^{-1} & \tilde{z}
\end{array}\right] .
\end{aligned}
$$

Thus, $W^{-1}$ is calculated by a correction to $w^{-1}$, and only the quantities $x, y$, and $z$ are needed additionally; $W$ and $w$ are never needed explicitly.

[^13]After the $M$-th unit becomes active, we identify $W$ with the $M \times M$ matrix Q $(n=M)$, whose matrix elements are (4.63)

$$
Q_{m l}=\left.P_{m}\left(\mathbf{x}_{l}\right)\right|_{l, m=1} ^{M} .
$$

Also, we identify $w$ with the $(M-1) \times(M-1)$ matrix from the previous step, $w \equiv q$, comprised by the first $M-1$ rows and columns of $\mathbf{Q}, q_{m l}=\left.Q_{m l}\right|_{l, n s=1} ^{M-1}$.

With these $W$ and $w, n^{\prime}=M-1$, hence $n^{\prime \prime}=1$; then $x$ is a $(M-1)$ - dimensional column vector; $y$, a row vector; $z$ and $\bar{z}$, scalars. Because P (4.29) and, therefore, Q are symmetric, we can define $p$ as the row vector ${ }^{28}$

$$
p^{T}{ }_{l} \equiv y^{T}{ }_{l}=x_{l}=Q_{M l}=\left.P_{M}\left(\mathbf{x}_{l}\right)\right|_{l=1} ^{M-1} .
$$

Also,

$$
z=P_{M}\left(\mathbf{x}_{M}\right) .
$$

Because $Q$ is symmetric and $\tilde{z}$ is a scalar, the second term in (5.11) factorizes into a tensor product of the $M$-dimensional row vector

$$
\left[\begin{array}{cc}
-u & 1
\end{array}\right] \equiv\left[\begin{array}{ll}
-y w^{-1} & 1
\end{array}\right]=\left[\begin{array}{ll}
-p q^{-1} & 1
\end{array}\right]
$$

with itself. Finally,

$$
\mathrm{Q}^{-1}=\left[\begin{array}{cc}
q^{-1} & 0 \\
0 & 0
\end{array}\right]+\bar{z}\left[\begin{array}{c}
-u^{T} \\
1
\end{array}\right]\left[\begin{array}{ll}
-u & 1
\end{array}\right] .
$$

### 5.5.2 Successive Reconstruction

Now, we are ready to study the reconstruction (4.67-4.68) iteratively. In this section, we will denote the quantities that relate to the old reconstruction- with M-1 active points by lowercase letters, and, for the new reconstruction, by uppercase; also, it is useful to adopt the notation of summation across the same lower and upper indices - from 1 to $M$ for the uppercase variables and, to $M-1$, for lowercase. We will interpret the $\mathbf{x}$-dependence of an object as a $V$-dimensional column vector; an upper index $m$ would mean the $m$-th column vector in a collection. In this notation (4.67)

$$
O^{r e c}(\mathbf{x})=A^{m}(\mathbf{x}) O\left(\mathbf{x}_{m}\right)
$$

means that $O^{r e e}(\mathbf{x})$ is a $V$-dimensional column vector, which is a linear combination of the $M$ (uppercase) column vectors $A^{m}(\mathbf{x})$ with the $M$ coefficients $O_{m}=O\left(\mathbf{x}_{m}\right)$. Analogously, the column vector $A^{m}(\mathbf{x})$ for the $m$-th reconstructor (4.68)

$$
A^{m}(\mathbf{x})=P^{l}(\mathbf{x})\left(\mathbf{Q}^{-1}\right)_{l}^{m}
$$

${ }^{28} p^{T}$ is a column vector, which is the transpose of the row vector $p$.

## 116

is a linear combination of the $M$ correlators $P^{l}(\mathbf{x})$, centered at the active grid points, $\mathbf{x}_{l}$, with the coefficients $\left(\mathbf{Q}^{-1}\right)_{l}^{m}$, from the $m$-th column of $\mathbf{Q}^{-1}$.

We substitute (5.16) in (5.18) and we get

$$
\begin{aligned}
A^{m}(\mathbf{x})= & {\left[\begin{array}{ll}
p^{l}(\mathbf{x}) & P^{M}(\mathbf{x})
\end{array}\right]\left[\begin{array}{cc}
\left(q^{-1}\right) r^{m} & \mathbf{0} \\
0 & 0
\end{array}\right]+} \\
& +\bar{z}\left[\begin{array}{ll}
p^{l}(\mathbf{x}) & P^{M}(\mathbf{x})
\end{array}\right]\left(\left[\begin{array}{c}
-u^{T} \\
1
\end{array}\right]\left[\begin{array}{ll}
-u & 1
\end{array}\right]\right)_{1}^{m}= \\
= & {\left[\begin{array}{ll}
p^{l}(\mathbf{x})\left(q^{-1}\right) I^{m} & 0
\end{array}\right]+\tilde{z}\left(P^{M}(\mathbf{x})-p^{l}(\mathbf{x}) u^{T}\right)\left[\begin{array}{ll}
-u^{m} & 1
\end{array}\right]=} \\
= & {\left[\begin{array}{ll}
a^{m}(\mathbf{x}) & \mathbf{0}
\end{array}\right]+\bar{z} A(\mathbf{x})\left[\begin{array}{ll}
-u^{m} & 1
\end{array}\right] }
\end{aligned}
$$

with

$$
A(\mathbf{x}) \equiv P^{M}(\mathbf{x})-p^{l}(\mathbf{x}) u^{T}{ }_{l}
$$

Thus, the new reconstructors $A^{m}(\mathbf{x})$ are the old ones, $\left[a^{m}(\mathbf{x}) \quad 0\right]$, with a correction

$$
\Delta A^{m}(\mathbf{x})=\bar{z} A(\mathbf{x})\left[\begin{array}{ll}
-u^{m} & 1
\end{array}\right]
$$

whose entire $\mathbf{x}$-dependence is given by $A(\mathbf{x})$. Indeed, the new reconstructor $A^{M}(\mathbf{x})$ is proportional to $A(\mathbf{x})$ with a coefficient $\tilde{z}_{1}$

$$
A^{M}(\mathbf{x})=\bar{z} A(\mathbf{x})
$$

and the correction to any old reconstructor $a^{m}(\mathrm{x})$, is proportional to $A^{M}(\mathrm{x})$ with a coefficient $-u^{m}$ :

$$
\Delta A^{m}(\mathbf{x})=A^{M}(\mathbf{x})\left[\begin{array}{ll}
-u^{m} & 1
\end{array}\right] .
$$

Now, we are well motivated to inquire into the meaning of $u=p q{ }^{1}$ (5.15). From (5.13) (cf. 5.18), $u^{m}$ is the old reconstructor $a^{m}(\mathrm{x})$, evaluated at the newly active point, $\mathrm{x}_{M}$,

$$
u^{m}=p^{l}\left(\mathbf{x}_{M}\right)\left(q^{-1}\right)_{l}^{m}=a^{m}\left(\mathbf{x}_{M}\right) .
$$

Also, (cf. 5.20), $p^{l}(\mathbf{x}) u^{T_{l}}=p^{l}(\mathbf{x})\left(q^{-1}\right)_{l}^{m} P^{M}\left(\mathbf{x}_{m}\right)=a^{m}(\mathbf{x}) P^{M}\left(\mathbf{x}_{m}\right)$; hence

$$
A(\mathbf{x})=P^{M}(\mathbf{x})-a^{\mathbf{m}}(\mathbf{x}) P^{M}\left(\mathbf{x}_{\boldsymbol{m}}\right) .
$$

The last term in (5.25), $a^{m}(\mathrm{x}) P^{M}\left(\mathrm{x}_{m}\right)$, is analogous in (5.17) with the difference that the sum is taken on the $(M-1)$-st step and the column vector evaluated at $\left\{\mathrm{x}_{m}\right\}$ is $P^{M}(\mathrm{x})$, rather than $O(\mathrm{x})$. Therefore, it is useful, given the current restriction $\mathcal{M}$, to define, for any vector $V(\mathbf{x})$, the reconstruction operator

$$
\mathcal{R}_{V}^{|\mathcal{M}|}(\mathbf{x})=A^{m}(\mathbf{x}) V\left(\mathbf{x}_{\boldsymbol{m}}\right) .
$$

Notably, because we are using the interpolating reconstructors (4.69), the reconstruction is exact at the active grid points. With (5.26), the reconstruction of $O(\mathbf{x})$ at the $M$-th step (5.17) is

$$
O^{r e c}(\mathbf{x})=\mathcal{R}_{O}^{M}(\mathbf{x})
$$

and the $\mathbf{x}$-dependence of the correction to the reconstructors, at the $M$-th step, (5.25) is

$$
A(\mathbf{x})=P^{M}(\mathbf{x})-\mathcal{R}_{P^{M}}^{M-1}(\mathbf{x}) .
$$

Remarkably, $A(\mathbf{x})$ is the difference between the true value of $P^{M}(\mathbf{x})$ and its reconstructed estimate from the $(M-1)$-st step. It is useful to define a new operator, the reconstruction error operator,

$$
\mathcal{D}_{V}(\mathbf{x})=V(\mathbf{x})-\mathcal{R}_{V}^{|\mathcal{M}|-1}(\mathbf{x})
$$

that calculates such differences for any $V(\mathbf{x})$. In this notation, the $\mathbf{x}$-dependence of the correction to the reconstructors

$$
A(\mathbf{x})=\mathcal{D}_{P^{M}}(\mathbf{x})
$$

is given by the current error in the estimate of $P^{M}(\mathbf{x})$, the correlator at the newly-added active point. Notably, because the reconstruction (5.26) is exact at the grid points from the last step, the error (5.29) vanishes there:

$$
A\left(\mathbf{x}_{m}\right)=\left.0\right|_{m=1} ^{M-1} .
$$

In order to understand fully the nature of the new interpolating predictor $A^{M}(\mathbf{x})$, we need to understand $\bar{z}$. We substitute (5.15) into (5.10) and get $\bar{z}^{-1}=\bar{z}-u p^{T}$, and from (5.14), (5.24), (5.13), and (5.29),

$$
\bar{z}^{1}=P^{M}\left(\mathbf{x}_{M}\right)-a^{m}\left(\mathbf{x}_{M}\right) P^{M}\left(\mathbf{x}_{m}\right)=\mathcal{D}_{P^{M}}\left(\mathbf{x}_{M}\right) .
$$

Then, the reconstructor at the newly-active grid point is (5.22)

$$
A^{M}(\mathbf{x})=\frac{\mathcal{D}_{P M}(\mathbf{x})}{\mathcal{D}_{P M}\left(\mathbf{x}_{M}\right)}
$$

and the correction to the old reconstructors is (5.21)

$$
\Delta A^{m}(\mathbf{x})=A^{M}(\mathbf{x})\left[\begin{array}{ll}
-a^{m}\left(\mathbf{x}_{M}\right) & 1
\end{array}\right] .
$$

This is a reasonable result; the new predictor, $A^{M}(\mathbf{x})$, due to the $M$-th active unit, is the normalized error in the old estimate of $P^{M}(\mathbf{x})$, while the old predictors, $a^{m}(\mathbf{x})$, are corrected by a negative feedback of this error, in proportionality with their original prediction strengths, $a^{m}\left(\mathrm{x}_{M}\right)$.

## 118

With the knowledge (5.34) of the change in the interpolating reconstructors due to the addition of one active point, we can understand what the correction is to the estimate (5.17) of $O(\mathbf{x})$,

$$
\begin{aligned}
\Delta O^{r e c}(\mathbf{x}) & =\Delta A^{m}(\mathbf{x}) O\left(\mathbf{x}_{m}\right)= \\
& =A^{M}(\mathbf{x})\left[-a^{m}\left(\mathbf{x}_{M}\right) \quad 1\right]\left[\begin{array}{l}
O\left(\mathbf{x}_{m}\right) \\
O\left(\mathbf{x}_{M}\right)
\end{array}\right]= \\
& =A^{M}(\mathbf{x}) \mathcal{D}_{O}\left(\mathbf{x}_{M}\right)
\end{aligned}
$$

With (5.33), finally

$$
\Delta O^{r e c}(\mathbf{x})=\frac{\mathcal{D}_{P^{M}}(\mathbf{x})}{\mathcal{D}_{P^{M}}\left(\mathbf{x}_{M}\right)} \mathcal{D}_{O}\left(\mathbf{x}_{M}\right)
$$

We will try to understand this remarkable result (5.36). On the basis of the current estimate $O^{\text {rec }}(\mathbf{x})=\mathcal{R}_{O}^{M-1}(\mathbf{x})$, the current error $O^{\text {err }}(\mathbf{x})=\mathcal{D}_{O}(\mathbf{x})$ is calculated. Regardless of the criterion for the choice of $\mathcal{M}$, the new activity introduces a correction $\Delta O^{\text {rec }}(\mathbf{x})$, which is exactly equal to the error at that grid point, and vanishes exactly at the old grid points.

The $\mathbf{x}$-dependence (5.33) of this correction is determined entirely from the residual output correlation P (4.29) and the mutual positions of the active units, $\mathcal{M}$. Notably, it depends neither on their activation strengths, $O_{m}$, nor on the current reconstruction error, $\mathcal{D}_{O}\left(\mathbf{x}_{M}\right)$.

### 5.6 Spike Generation in Autocorrelated Time Series

### 5.6.1 Predictive Coding as Successive Sparsification

In Section 5.5 we studied the correction $\Delta O^{\text {rec }}(\mathbf{x})$ to the current reconstruction $O^{\text {rec }}(\mathbf{x})$ (5.36) due to the addition of one new grid point to the sparsification $\mathcal{M}$. To calculate this correction, two pieces of information were needed: the location of the new active unit, $\mathrm{x}_{M}$, and the current reconstruction error at that location, $O^{\operatorname{err}}\left(\mathbf{x}_{M}\right)=\mathcal{D}_{O}\left(\mathbf{x}_{M}\right)$.

In the Engineering literature (Gonzalez and Woods 1992), the process of calculating estimates and transmitting the respective error signal is called Predictive Coding. It would be interesting to understand the relationship between successive sparsification (5.36) and Predictive Coding.

The standard diagram of Predictive Coding is shown on Fig. 5.9. In order to be spared from the complications of the 2-dimensional case, we will consider the 1-dimensional case, when the signal is a time series, such as sound. We would like to understand it as an infinite source $f(t)$ (cf. Appendix A.6), from which we will construct finite-dimensional ensembles of examples $\phi^{t_{n}}\left(\mathbf{x}_{k}\right)=f\left(t_{\mathbf{n}-k}\right)$ by imposing a finite discrete window of size $V$ around the time $t_{n}$ (A.13).

![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-11.jpg?height=411&width=800&top_left_y=128&top_left_x=1096)
Figure 5.9: The Predictive Coding Model

The Encoder (a) has access to the signal $\left\{f_{\chi}\right\}_{\chi \in X}$. Based on the part of the signal that has been transmitted already and on a model of the ensemble from which the signal was drawn from, the Predictor calculates, for the current grid location $\mathbf{x}_{n}$, an estimate $f^{r e c}\left(\mathbf{x}_{n}\right) \equiv f_{n}{ }^{r e c}$, and the Quantizer quantizes it to $f_{n}$. The error $e_{n}=f_{n}-\hat{f}_{n}$ is calculated and is fed to the Symbol Encoder, which produces the Compressed signal and sends it optimally over the communication channel.
The Decoder (b) receives the compressed signal over the communication channel and feeds it to the Symbol decoder, wich produces an identical copy of the error signal $e_{n}$. This error is added to the current reconstruction $f_{n}$, which is available to the Decoder from the action of a Predictor and a Quantizer, identical to the ones operated by the Encoder, on the part of the signal that has been transmitted already and, therefore, is also available to the Decoder. The result, $f_{n}=\hat{f}_{n}+e_{n}$, is an identical copy of $f_{n}$.
This figure is essentially Fig. 6.19 from (Gonzalez and Woods 1992).

Typically, Predictive Coding assumes that $f(t)$ has already been transmitted for all times $t$ prior to the current time, $t_{n}$. Then, both the encoder (Fig. 5.9a) and the decoder (Fig. 5.9b) independently calculate identical estimates of the of the current value, $f^{r e c}\left(t_{n}\right)=f_{n}$. The encoder, which has access to the true value $f_{n}$, calculates the error $e_{n}=f_{n}-f_{n}$ and feeds it, via the communication channel, to the decoder, which adds it to the estimate to produce a copy of the true value, $f_{n}=\hat{f}_{n}+e_{n}$.

Typically, the prediction $f_{n}$ is made on the basis of the values of $f(t)$ in only a small time window, preceding $t_{n},\left\{f_{n}(m)=f\left(t_{n-m}\right)=f_{n-m}\right\}_{m=1}^{M}$. The

$$
120
$$

size of this window, $M-1$, is called the order of the predictor. Also, typically, the predictor is a linear function of the $M-1$ preceding values (eq. 6.5-6 in Gonzalez and Woods 1992),

$$
\hat{f}_{n}=\sum_{m=1}^{M-1} \alpha_{m} f_{n-m}
$$

which, after assuming the summation notation of Section 5.5, looks remarkably similar to (5.17)- $\hat{f}_{n}=\alpha^{m} f_{n-m}$.

There are many possible choices for the coefficients $\alpha_{m}$; when they are chosen to minimize the expectation of the square of the error signal, $E\left\{e_{n}{ }^{2}\right\}$, the method is called Differential Pulse Code Modulation (DPCM). Then (eq. 6.5-[8-10] in Gonzalez and Woods 1992)

$$
\alpha^{m}=\left(q^{-1}\right)_{l}^{m} Q_{0}^{l}
$$

with

$$
q_{m l}=\left.Q_{m l}\right|_{m, l=1} ^{M-1}
$$

where

$$
Q_{m l}=\left.E\left\{f_{n-l} f_{n-m}\right\}\right|_{m, l=0} ^{M-1}
$$

is the autocorrelation function of the signal; (5.38) looks remarkably similar to (5.24).

To take the analogy further, we can identify the grid points whose value is known, $\left\{t_{n-m}\right\}_{m=1}^{M-1}$, with $\left\{\mathrm{x}_{m}\right\}_{m=1}^{M-1}$, and the currently reconstructed grid point $t_{n}$, with $\mathbf{x}_{M}$. Then $\mathbf{Q}$ (5.40) is the correlation matrix of the signal, restricted to the reference points $\mathcal{M}$, exactly as in (5.12). Notably, the size of the ensemble window, $V$, does not matter, since reconstruction is attempted only at the newly-active grid point, $\mathrm{x}_{M}$. With this definition, the action of the encoder is

$$
e_{n}=f_{n}-\hat{f}_{n}=\mathcal{D}_{f}\left(\mathbf{x}_{M}\right)
$$

and the action of the decoder is

$$
\Delta f^{r e c}\left(\mathbf{x}_{M}\right)=e_{\mathbf{n}}=1 \times \mathcal{D}_{f}\left(\mathbf{x}_{M}\right) .
$$

There are several very important differences between DPCM (5.41-5.42) and successive sparsification (5.36). Most importantly, DPCM works directly on the signal, instead of on the dense LFA output $O(\mathbf{x})$. Indeed, the fact that $\mathbf{P}$ is a projector was not used in deriving (4.67-4.68); one might hypothesize, that the equations will sparsify well any input signal. In Appendix A.5, we show that this is not the case-sparsification before decorrelation is very susceptible to noise. ${ }^{29}$

[^14]to be addressed at the engineering level, together with other constrains that might be imposed by biology. Nevertheless, there might be systems that are simple enough to be used as a test bed for the methods discussed in this Thesis.

Bialek et al. (1991) study the H1 neuron in the visual system in blowfly; it has a pair of them, and they encode the rigid horizontal movements across the whole visual field. The fly's visual system is presented with an ensemble of experimentally well-controlled sensory stimuli $\Phi$, interpreted as the horizontal velocity $v(t)$; simultaneously, the spike train $\left\{t_{m}\right\}$ that results from this stimulation is recorded.

To measure the information transmission, $v(t)$ is reconstructed from the spike train $\left\{t_{m}\right\}$ with the reconstruction formula (eq. 1 in Bialek et al. 1991)

$$
\Delta v^{r e c}(t)=A^{M}(t) \times 1
$$

which is surprisingly similar to (5.36) (cf. 5.42). When translation invariance is enforced, $A^{M}(t)=F_{1}\left(t-t_{M}\right)$, and the m.s.e., $E\left\{\left(v(t)-v^{r e c}(t)\right)^{2}\right\}$, is minimized over the experimental data set, the best $F(\tau)$ is determined. It is used to calculate the mutual information between $v(t)$ and $v^{\text {rec }}(t)$, which is a lower bound on the information transfer rate of the H1 neuron. ${ }^{35}$

Performing the same analysis simultaneously with measuring the total entropy of the spike train, Rieke, Warland, and Bialek (1992) find that at least 50\% of it is utilized to transmit information about the signal.

Although the reconstruction formula they have used (5.43) seems similar to (5.36), there are two major differences. The reconstructors $A^{m}(t)$ are identical-they are based on a single grid point, $t_{M} .^{36}$

More importantly, the reconstructing coefficient is the same for all active grid points 1, instead of $\mathcal{D}_{O}\left(\mathbf{x}_{M}\right)$.

An obvious idea is to re-do the analysis of the original experiments from the point of view of dynamic sparsification (5.36). If the fly visual system up to H 1 is concerned with optimal use of available resources, we would predict that the utilization of the entropy of the spike train for transmission of information about the actual signal will be much higher, close to $100 \% .^{37}$

[^15]
## Chapter 6

## Discussion

In this Thesis, we have explored a possible design goal for the sensory systems of organisms redundancy reduction. Although redundancy reduction has deep roots in Philosophy and Psychology (Mach 1914; Pearson 1892; Craik 1943; Attneave 1954; MacKay 1956; Barlow 1959; Barlow 1961a), which may be traced back to Plato, who suggested the decomposition of "objects" to "ideas," it has made its way in the quantitative description of sensory systems only recently (for a review see Deco and Obradovic 1996).

Redundancy reduction postulates that a goal for the sensory system is to reduce redundant information and signal only what is "novel" and "unexpected." Mathematically, the concept of information was understood relatively recently, by Shannon and Weaver (1949), inspired by the ideas of Boltzmann, von Neumann, and N. Wiener. Soon after that, Barlow (1961b) made the link between the mathematical formulation of Information Theory on one hand, and Psychology and Physiology, on the other. Later, Barlow et al. (1989) suggested a particular way to reduce redundancy by factorial codes, in which the probability density of complex sensory stimuli factorizes into individual probability densities, of the variables in their representation.

Although redundancy reduction implies efficient representations, biological calculations, which, arguably, utilize them, have to be carried on in real time. Since the execution time of various high-level algorithms depends very strongly on the dimensionality of the representation, another principle has been proposed in the Artificial Intelligence community-dimensionality reduction.

In this Thesis, we have tried to tie the two concepts together by the observation that, in order to reduce both redundancy and dimensionality, one needs a frugal, yet accurate parameterization of the probability density $\mathcal{P}[\phi]$ of ensembles of sensory signals.

In Chapter 2 we studied the best-understood method for dimensionality reduction-Principal Component Analysis (PCA)-and found that it is also a factorial code and, as such, reduces redundancy. In Section 4.2 we showed that, even in the cases when PCA cannot reduce dimensionality, it still reduces
redundancy.
Although PCA, a second-order linear method, is very well understood and easy to apply in practice, in Section 3.2.2 we showed that its one-time application is not enough to make high-level tasks feasible. We suggested a reason for that-PCA cannot capture naturally some symmetries that are present in the sensory ensemble.

In Section 4.2 we studied a symmetric ensemble and saw that, although, in theory, PCA could reduce redundancy, the calculations it entails are global, and are not biologically feasible. Motivated by the full translational symmetry of the ensemble, we developed a topographical formulation of PCA, in which the calculations were carried out locally and, therefore, biologically plausibly.

Motivated by the partial translation symmetry present in ensembles of objects, in Section 4.3, we applied topography to ensembles with reduced dimensionality and produced a topographic extension of PCA, whose representation had the same redundancy reduction properties, but was highly dimensional.

We devoted the rest of Chapter 4 to develop Local Feature Analysis (LFA), which, on the basis of the topographic extension of PCA, builds a sparsedistributed representation of objects in term of their local features. We showed that, although it has exactly the same redundancy-reducing properties as both the global PCA and its topographic extension, LFA reduced dimensionality even further.

In Section 5.1 we studied the relationship between the parameterizations of the probability densities of images, $\mathcal{P}_{\text {images }}$, and of objects, $\mathcal{P}_{\text {ohjects }}$. We understood the preparation of unsymmetric ensembles as a process of finding of a parameter, $\alpha$, of symmetry breaking of the symmetric ensemble; we also understood the probability distributions $\mathcal{P}_{\alpha}$ and $\mathcal{P}_{\text {objects }}$ as part of the explicit parameterizatiou of $\mathcal{P}_{\text {imnges }}$.

In Section 5.3 we carried the analogy further, and understood the localization of a certain feature by the sparsification step of LFA as finding a parameter, $\theta$, for the breaking of the partial local symmetry. We proposed that this be understood as the definition of a new ensemble, of features, and as the re-parameterization of $\mathcal{P}_{o b j e c t s}$ with $\mathcal{P}_{\beta}$ and $\mathcal{P}_{\text {feature }}$. This hierarchical parameterization of the original $\mathcal{P}_{\text {images }}$ prompted the proposal of hierarchical assemblies of representational modules, possibly based on LFA, much like the hierarchical interconnection of cortical areas.

In Section 5.4 we explored the possibility of the application of the sparsification step of LFA to symmetrical ensembles, with full PCA dimensionality, and observed that in multi-scale representations, which are abundant in the peripheral nervous system, LFA has the chance to reduce dimensionality. As usually, we interpreted the symmetry breaking due to sparsification as a definition of an unsymmetric ensemble, and re-parameterization of the underlying probability density.

In Section 5.6 we argued that multi-scale sparsification of 1-dimensional

Another very important difference is that, in DPCM, there is no dimensionality reduction-calculation and transmission of the error signal (5.41) is performed for each grid location $t_{n}$. In the context of sparsification, after the enough reference points are added-their number $M$ reaches the dimensionality $N$-the reconstruction becomes exact. In the context of DPCM, the reconstruction is based on a fixed number of points, $M-1$; old values are forgotten, as new ones come in. Therefore, the DPCM reconstruction is always sub-optimal.

Even if $M-1$ is chosen large enough to cover the dimensionality of the ensemble, and the signal is pre-filtered to get $O(\mathbf{x})$, the fact that the reference grid points are chosen to be consecutive decreases the numerical stability of the method (see Section 4.4.1). ${ }^{30}$

DPCM (5.41 5.42) is a special case of sparsification (5.36), albeit with a sub-optimal choice of the sparsified function, and with a sub-optimal choice of the reference points $\mathcal{M}$. One is tempted to hypothesize that, in general, LFA will achieve better results.

### 5.6.2 Spike Generation by Successive Sparsification

In Section 5.6.1 we interpreted sparsification as Predictive Coding, in which an encoder and a decoder communicate over a channel (Fig. 5.9). They calculate identical reconstructions $O^{r e c}(\mathbf{x})=\mathcal{R}_{O}^{M-1}(\mathbf{x})$; the encoder calculates the reconstruction error $O^{\text {err }}(\mathbf{x})=\mathcal{D}_{O}(\mathbf{x})$ and transmits its value at a suitably chosen point, $\mathrm{x}_{m}$; and both the encoder and the decoder make a correction to their reconstructions by (5.36).

For 1-dimensional (time-varying) signals, when the grid index x is identified with the time axis $t$, it is tempting to identify the encoder as the pre-synaptic neuron; the decoder, as the post-synaptic neuron; the communication channel, as the axon; and the act of choosing the reference times at which the error is communicated, $\left\{t_{m}\right\}$, as the timing of the train of action potentials (spikes) propagated along the axon.

Although tempting, the latter model has one problem. On one hand, besides the mutual location of the reference times $\mathcal{M}$, the reconstruction (5.36) also needs the value of the error at the times of the spikes. On the other hand, spikes are identical voltage impulses, (Adrian 1926; Adrian and Zotterman 1926a; Adrian and Zotterman 1926b), and there is no mechanism to communicate a value with a single spike; spikes carry ouly timing information.

In Section 4.4.4 we suggested an algorithm to choose which grid points to include in the sparsification $\mathcal{M}$, which looked globally for the places where $\mathcal{D}_{\mathcal{O}}(\mathbf{x})$ was largest. Here, we pose the question, Is it possible to find another
${ }^{30}$ Although there are other problems associated with DPCM, among them that only preceding values can be used for prediction, it is outside the scope of this Thesis to discuss DPCM in detail.

122
strategy for choosing the reference points, such that the error will be known by the decoder in advance, and there will be no need to communicate it?

One possible strategy is to pre-determine a threshold $\theta$, which is known to both the encoder and the decoder. Then, the encoder would emit a spike each time the current reconstruction error is equal to the threshold, $\mathcal{D}_{O}\left(\mathbf{x}_{\text {spike }}\right)=\theta$. Indeed, this would obviate the need to transmit the value of $\theta$ with each spike, because it is a constant.

The problem associated with this strategy is depicted on Fig. 4.7 as the total residual error, $\left\|O^{e r r}\right\|_{U}^{2}$, decreases, so do the magnitudes of the errors at the individual grid points, $\mathcal{D}_{O}(\mathbf{x})^{2}$. On one hand, when $\theta$ is relatively large, after picking some small number of points, the total error will be small enough, and all grid point errors will be below $\theta$; the picking process will stop, and there will be a substantial residual error. When $\theta$ is relatively small, on the other hand, the final residual error will be small, but the choice of the initial points will be very bad-they will all be in the periphery of the features, which will decrease the numerical stability of the method (see Section 4.4.1).

An obvious idea is to set $\theta$ dynamically, on an example-by-example basis. One way to do this is to keep track of not only the current reconstruction, $\mathcal{R}_{O}^{M}(\mathbf{x})$, but also, a current expectation of the variance of the error, $D(\mathbf{x})^{2}=E\left\{\mathcal{D}_{O}(\mathbf{x})^{2}\right\}$ (see discussion in footnote 32 on page 77). Then, $\theta$ may be set relatively to this expectation, either as a constant, or as a function that decays with the time since the last spike, $\theta\left(\mathbf{x}-\mathbf{x}_{\text {vpike }}\right)$.

An interesting problem arises when spiking is triggered by the thresholdcrossing of some function of time. The resolution with which the timing of a spike can be effected and measured is, necessarily, finite; there is an error in the timing, which generates an error in the decoder's estimate of $\mathcal{D}_{O}(\mathbf{x})$ and, therefore, of $O^{r e c}(\mathbf{x})$, which depends on the derivative of $O(\mathbf{x}) .^{31}$ One way to cope with this problem is to bound the derivative of $O(\mathbf{x})$ by bounding the derivatives of the individual modes that participate in the sum (4.31).

There is, in our view, a more interesting way to think about the information that is transmitted with a single spike. Because the exact timing of the spike is determined with precision $\Delta t$, we may consider that a spike can be triggered only at certain discrete times, $\Delta t$ apart. At any such time, x , the encoder compares the target function, for example $D(\mathbf{x})$, with the threshold $\theta(\mathbf{x})$. Obviously, their difference will vanish exactly at those discrete moments only very rarely-at times it will be negative, at times, positive. The encoder's signal of the zero-crossing can only be interpreted as a negative-to-positive transition- the difference is positive at the moment of the spike, $\mathrm{x}_{\mathrm{m}}$, but was negative the preceding moment, $\mathbf{x}^{\prime}$.

Fig. 5.10 shows a diagram of the information content of such a message in

[^16]![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-13.jpg?height=459&width=717&top_left_y=91&top_left_x=1115)
Figure 5.10: Information Transmission with Spikes
The grid location $\mathbf{x}_{m}$ determines a vector $\mathbf{q}_{\mathbf{x}_{m}} \in S$ (4.38), which in turn determines a one-dimensional subspace $U_{m} \subset S$ (vertical line), with a projector $\mathbf{Q}_{\mathbf{x}_{m}}$ (4.39).
For the example $\phi=\Phi^{*} s$, in Section 4.4.2 we interpreted the choice of the grid point $\mathbf{x}_{m}$ as the measurement $O\left(\mathbf{x}_{m}\right)=O_{m}=\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}\right\rangle$ (4.37) and we introduced $\mathbf{s}_{\|}=O_{m} \mathbf{p}_{\mathbf{x}_{m}} \in U_{m}$ (4.42) (light vertical arrow, ending at $A$ ).
Analogously, any non-selected grid location $\mathbf{x}^{\prime}$ determines the vector $\mathbf{q}^{\prime} \in S$ (along the light slanted arrow). Together with $\mathrm{q}_{\mathrm{x}}$, they determine a $2-$ dimensional subspace (the plane of the circle), orthogonally decomposed to $U_{m}$ and $U_{m}^{\prime}$.
All other $N-2$ dimensions of the PCA $S$-subspace are collapsed to $U^{\perp}$.
For a given measurement $O_{m}$, we can define $O_{m} \mathrm{P}^{\prime}$ (light slanted arrow, ending at $B$ ). It can be treated as a normal to an $N-1$ dimensional hyper-plane, whose intersection with the plane of the circle is the slanted line $(B-C)$, tangential to the circle, and which intersects with $U_{m}^{\prime}$ at point $C$. This hyper-plane's intersection with $U^{\perp}$ is the ( $N-2$ )-dimensional hyper-plane, collapsed to the slanted line starting at $C$.

the context of sparsification. Given the example $\phi=\Phi^{*}$ s, and the choice of the temporal location $\mathbf{x}_{m}$, on the assumption that we know the results of the measurements infinitely well, we decomposed s as a sum of a vector $\mathrm{s}_{\|}=O_{m} \mathbf{p}_{\mathbf{x}_{\mathrm{m}}} \in U_{m}(4.42)$, point $A$ on Fig. 5.10, and a vector $\mathrm{s}_{\perp}$, orthogonal to it. We interpreted $\mathbf{s}_{\|}$as the maximum likelihood estimate.

When a spiking encoder transmits the information about $\mathcal{D}_{O}(\mathbf{x})$ and, therefore, $O(\mathbf{x})$ with the inaccurate timing of a negative-to-positive transition, the

124
decoder cannot assume that $O\left(\mathbf{x}_{m}\right)=O_{m}$ exactly, but only that $O\left(\mathbf{x}_{m}\right) \geq O_{m}$. This means that su can have any value in the ray of $U_{m}$ that stars at $A$ and has the direction of the bold arrow. ${ }^{32}$

There is another piece of information in the timing of the negative-topositive transition-that the value $O\left(\mathbf{x}^{\prime}\right)$, immediately prior to the spike, was below a certain threshold, $O^{\prime} .{ }^{33}$ We can decompose s into a sum of three mutually orthogonal vectors, $\mathbf{s}_{\|} \in U_{m}, \mathbf{s}^{\prime} \in U_{m}^{\prime}$, and $\mathbf{s}_{\perp} \in U^{\perp}$. Since both $\mathbf{q}^{\prime}$ and $\mathbf{q}_{\mathbf{x}_{m}}$ are orthogonal to $U^{\perp}, \mathrm{s}_{\perp}$ can be anywhere in $U^{\perp}$, and a maximum likelihood estimate of it is $\mathbf{s}_{\perp}=\mathbf{0}$.

On the other hand, $s^{\prime}$ can be anywhere on the ray in $U_{m}^{\prime}$, starting at $C$, in the direction of the bold arrow; hence, the maximum likelihood estimate, which is the mean of the respective distribution, is not $\mathbf{s}^{\prime}=\mathbf{0}$, but is to the left of $A$, at $D$. Also, the line $B C$ intersects with $U_{m}$ at some place, and that is an upper bound for $o_{m}=\left\langle\mathbf{q}_{\mathbf{x}_{\mathbf{m}}}, \mathbf{s}_{\|}\right\rangle$; hence the maximum likelihood estimate for $\mathbf{s}_{\|}$is not $O_{m} \mathrm{p}_{m}(A)$, but is a bit higher. ${ }^{34}$

So far, we have discussed how, in general, the transmission of information with identical spikes can be analyzed. We found out that, because the value of $\mathcal{D}_{O}(\mathbf{x})$ has to be communicated by the encoder with the imprecise timing of a suitably chosen zero crossing, the decoder, necessarily, will make an error in its estimate; we also found that the best strategy in this case is approximation, as opposed to interpolation, which was discussed in Section 4.4.2.

Since spiking neurons are actual devices, operating in practice, the issues of noise in the measurements, the computations, and the communication-have

[^17]ensembles can be utilized as one of the first steps in actual sensory processing the conversion of continuous time-varying sensory stimuli to discrete events, action potentials (spikes), which represent all of the information available to the nervous system about the state of the external to it world, by means of localization of, otherwise identical events, in space and time.

In this Thesis, we have described bits and pieces of a greedy Homunculus that sits inside the brain. It measures the second order statistics of the probability distribution of sensory ensembles and reduces the redundancy that is associated with it. In the process, it exposes the symmetries of the ensemble, breaks them, defines new, less-symmetric ensembles, and re-parameterizes the original probability density. At the end, it builds and maintains a hierarchical parameterization of the probability density $\mathcal{P}_{\text {world }}$. Using this parameterization, it takes the output of the receptors, converts them into spikes, and represents the information about the current state of the world efficiently.

Is this Homunculus the Brain? No. We motivated our research with the need for the organism to make decisions cheaply, quickly, and correctly. To make decisions is to run certain algorithms on the current state of the world. Our Homunculus only represents the information about it, arguably providing the paper, the pen, and the language the active blackboards for those algorithms.

Also, the world has not only a probability distribution and a current state, but also, past states; those algorithms need access to them also. The world has future states, and they are needed for planning. Our Homunculus does not address episodic memory, and does not address what-if scenarios. Finally, it does not address execution of decisions actions.

Nevertheless, all those aspects of the sensory activity have to interact with the current state of the world and, therefore, have to speak the language of our Homunculus. If we know that language, we can start asking questions with a reasonable chance of being understood correctly and being handed a relevant auswer.

Is Local Feature Analysis our Homunculus? In all of Chapter 5, we have argued that much more is going on than just LFA. Nevertheless, we believe that LFA is the basic representational block, around which various algorithms are built.

There are two approaches that can be taken to verify LFA. One is to understand the language of the actual representation, starting at the level of conversion of information to spikes, and work our way up to the cortex.

The other is to try to solve practical problems, analogous to what the brain is solving, and to see what the role in the solution is of LFA, what computational architecture, what algorithms, and what other modules those solutions entail.

Both are interesting, complementary to each other, and the author feels that both will be rewarding.

## Appendix A

## Appendices

## A. 1 The Databases

This Appendix gives details of the object ensembles, as well as the test samples not in them, used to produce the results in the paper.

Ensemble 1 The examples in this ensemble are part of the ARPA/ARL FERET database (Rauss et al. 1996a), which consists of grayscale photographic images of a racially diverse set of human subjects in natural conditions on a plain background. The lighting is roughly diffuse with a single Lambertian source. No attempts have been made to control either the direction or the strength of the source or the expression and the facial hair of the subjects. The photographs have been taken on different days over a six-month period and at greatly varying distances. Most of the subjects appear four times in the database with a couple of months between the pairs of photographs, although. there are some subjects that appear only once. The photographs have been scanned (and some gain control unknown to us has been applied in the process) to produce an 8-bit grayscale format with 256 × 384 samples.

We selected from the FERET database $T=1038$ examples without glasses and in relatively frontal poses as part of our data set and we kept the remaining 7 for out-of-sample but in-database testing.

For each example the locations of both eyes were selected manually. The examples were then rotated so that the inter-eye line is horizontal and scaled down (with smoothing based on the scale factor) so that the inter-eye distance is 28 pixels. The fixed point of the examples was then set to be the middle of that line. Finally, the examples in the data set were cropped through a $64 \times 60$ window centered horizontally about the fixed point and starting 15 rows above it.

Ensemble 2 The examples of this ensemble are part of the U.S. Air Force Mini Survey database (Robinette and Whitestone 1992) which consists of 348 Iaser scans of the 3D surfaces of heads of human subjects. The data samples consist of a representation of the surface in uniformly sampled cylindrical coordinates $r(\theta, \ell)$ with 512 samples spanning a full revolution in the $\theta$ direction and 256 samples in the $\ell$ direction. Anthropological landmarks on the surfaces were selected manually.

The examples were aligned by us, so that the fixed point ( $\theta_{\text {fixed }}, \ell_{\text {fixed }}$ ) was at the sellion-the deepest depression of the vertical center of the nose bone between the eyes. Spikes and missing data points were filled through linear interpolation of known good samples around the patch by an automatic algorithm.

The examples were resampled in a new set of polar coordinates by shifting the vertical axis to pass through the center of masses of five layers up and five layers down the cross-section through the fixed point. The examples were smoothed with a $3 \times 3$ Gaussian filter and under-sampled twice to produce a $256 \times 128$ representation. All examples in the Mini Survey study database were chosen to produce a $T=348$ data set.

Finally, the examples in the data set were cropped through a $128 \times 64$ window centered horizontally about the fixed point and starting 17 rows above it.

Ensemble 3 The examples in this ensemble were produced from the data set of Ensemble 1, the only difference was the cropping. The examples were cropped through a $96 \times 90$ window centered horizontally about the fixed point and starting 30 rows above it. The images in this ensemble include not only faces but the background as well.

Ensemble 4 The examples in this ensemble were produced from the data set of Ensemble 1, the only difference was the cropping. The examples were cropped through a $96 \times 120$ window centered horizontally about the fixed point and starting 60 rows above it. The images in this ensemble include not only faces but the substantial background and hair as well.

Ensernble 5 The examples in this ensemble include all examples in Ensemble 1, the examples in the Yale Face Database, some examples from the Olivetti Database, as well as the examples in a database developed in the Laboratory for Computational Neuroscience at The Rockefeller University.

All images were aligned according to the protocol for Ensemble 1 and were cropped as Ensemble 1 also.

Ensemble 6 The examples in this ensemble are based on all frontal examples in the FERET database (cf. Ensemble 1). Each each image was aligned

## 132

as usual, and then 9 examples were produced from it by varying the scaling parameter $\left\{s_{n}=1.05^{n / 2}\right\}_{n=-4}^{+4}$, i.e., the up and down deviations from the hand-determined scale were $\approx\{10 \%, 7.5 \%, 5 \%, 2.5 \%, 0 \%\}$, resulting in dimensionalities ( $T=10944, V=3840$ ).

Ensemble 7 Besides the examples in Ensemble 6, Ensemble 7 includes four additional scalings $\left\{s_{m}=1.025^{m / 3}\right\}_{m \in\{-2,-1,1,2\}}$; resulting in deviations of $\approx$ \{1.7\%, 0.8\%\}.

The Yale Face Database This database was developed and used for the purposes of human face classification by Belhumeur (1996). It is publicly available at http://giskard.eng.yale.edu/yalefaces/yalefaces.html. It is shown in full on Fig. A.1.

The images underwent the same normalization procedures as Ensembles 1 and 3.

Three croppings were prepared-full with $V=96 \times 120=11,520$, h3q with $V=96 \times 90=8,640$ which is the same as that for Ensemble 3, and with third $V=64 \times 60=3,840$ is the same as Ensemble 1 .

Example 1 This image was taken with a video Hi8 camcorder in almost completely diffuse lighting (there is a weak Lambertian light coming exactly from the left side). The image was captured on a Silicon Graphics IRIS Indigo R3000 workstation with the SVideo capture board. Automatic gain control has been used both on the camcorder and on the capture board.

The image was converted to grayscale, oversampled $10 \times$, and then underwent the same procedure of alignment, rotation, and scaling as the examples in Ensembles 1 and 3. Two croppings were produced as described above to be used with the two ensembles respectively.

Example 2: This example is one of the 7 left aside in preparing the data set for Ensembles 1 and 3.

## A. 2 A Dangerously Small Ensemble

In this Appendix we will illustrate further the looming dangers of the in-sample effect.

Turk and Pentland (1991) pioneered the idea of utilizing the hypothesized low-dimensionality of the "face space" (Sirovich and Kirby 1987) for face recognition. For their seminal paper, they used the database, part of which is shown on Fig. A.2.


[^0]:    ${ }^{35}$ This formula is included for the purpose of serving as a reference to Fig. 4.5. A more natural-looking and intuitive version is given in Section 4.4.5.
    ${ }^{36}$ Now, it is easy to understand why it is unwise to pick all $|\mathcal{M}|$ reference points closely elustered; $Q$ will be dense and slow to invert. Also, the values of this dense matrix will be all positive, on the order of 1, so the matrix will be badly conditioned-a small error in some $O_{m}$ will result in a large error in $O^{\text {rec }}(\mathbf{x})$.

[^1]:    ${ }^{37}$ Note that sparse-distributed coding is somewhat different from population coding, in which a dense set of units are active to code for a given aspect of the stimulus.
    ${ }^{38}$ One might object and say that the value of $O^{\text {err }}\left(\mathbf{x}_{m+1}\right)^{2}$ is a somewhat arbitrary criterion. We will remember that the information content of the example, $-\log \mathcal{P}[\phi]$, is determined by a sum of such squares (4.22). The error in the estimate of the probability, $-\log \mathcal{P}[\phi]-\left(-\log \mathcal{P}\left[\phi^{\text {rec }}\right]\right)$, is equal to $\left\|O^{\text {err }}\right\|_{U}^{2}$. Therefore, by bounding of the maximum term in the sum $\left\|O^{\text {err }}\right\|_{E}^{2}=\frac{1}{V} \sum_{x} O^{\text {err }}(\mathbf{x})^{2}(2.8)$, we bound the whole sum and, therefore, the error in $\mathcal{P}[\phi]$.

    Then, Why not use the sum itself as a criterion, rather than its largest term? For one, the 81
    Third, if the algorithm has not terminated yet, we add $\mathbf{x}_{m+1}$ to $\mathcal{M}^{(\mathbf{n})}$, which results in $\mathcal{M}^{(n+1)}$, and go to step $n+1 .^{39}$

    This algorithm terminates; it picks only points whose value is not predicted well, therefore they are linearly independent, and by the time $|\mathcal{M}|=N$, $O^{e r r}(x)=0$ (4.36).

    The described sparsification algorithm chooses points whose outputs are not predicted well by the already chosen ones, which creates a bias towards allocating resources efficiently; an example of such resource allocation-the result of applying the algorithm to Example 1-is shown on Fig. 4.4.

    The location and the order of first 25 points, those in $\mathcal{M}^{(25)}$ (Fig. 4.4a), show that resources are allocated first at the places with biggest deviations from the expectation-the outlines of the face and the most unusual features, which is a desirable property. The points in $\mathcal{M}^{(64)}$ enough for acceptable reconstruction of Example 1 (see the top row of Fig. 4.5b)-are shown with dots on Fig. 4.4b. We observe that only a few values are needed to represent each individual feature, which is a result of the generalization properties and the locality of the representation.

    On the other hand, it is evident that most of the resources are allocated to describe the background. This is not surprising-the underlying ensemble is one of faces; the exclusion of the information about the statistical properties of the background has been a design goal for this ensemble. Naturally, the predictions based on the statics of one class of objects (faces) will fail to some extent, when applied to a different class of objects (walls).

    A more sophisticated approach would be to segment the objects from the background fully and use two different correlation functions for reconstruction- tailored to the respective different statistics. We will explore this possibility in Section 5.3.

    In Figure 4.5 we compare the quality of reconstruction using the sparse topographic representation (b) with two other strategies-the global PCA representation (a) and a uniform subsampling (c), when all of them use the same number of values 64. We calculated the PCA coefficients $a_{r}$ (2.47 2.52) and

[^2]:    ${ }^{41}$ Note that, since the algorithm is incremental, we never need to compute the inverse of the matrix Q (4.65) explicitly. The inverse at the $m$-th step is related to the inverse at the $(m-1)$-st step through a simple algebraic formula. The algorithm for inversion through partitioning is available in many books on numerical methods, for example, (Noble 1992; Press et al. 1992). The meaning of the incremental inversion step will be understood in Section 5.3.

[^3]:    ${ }^{42}$ An immediate question is obvious, Why include, wastefully, 50\% of the terms in order to get $99 \%$ of the fidelity?-the incremental benefit of adding a reference point in the $50 \%$ regime is really low. Indeed, one might suggest a more sophisticated strategy: first use a relatively-low-dimensional LFA representation, pull off, with a few terms say 10\%, as much information as possible, say 60\%, and then pull off the rest of the information from another LFA representation-on the basis of a larger $N$. The construction of several co-existing LFA representations by taking the sums in (4.29) in several separate bands for $r$, instead of lumping all modes together, will result in a multi-scale representation. Such representations are widely used in, at least, the auditory and visual pathways, and may rival the hybrid representation, discussed in Appendix A.4. We will propose them in Section 5.4 as a way to sparsify the dense LFA representations for symmetric ensembles.
    ${ }^{43}$ This is exactly true, if the assumption of a joint-normal distribution (2.49) holds. In Appendix A. 3 we show that, for the ensemble of images of faces, the marginal distributions are non-Gaussian. It remains to be seen whether LFA would allow a shorter code in such cases.

    ![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-02.jpg?height=596&width=816&top_left_y=1430&top_left_x=1069)
    Figure 4.6: Comparison Between PCA and LFA S-N Diagrams The total information of the PCA reconstruction (2.49) of Example 1 (Fig. 4.5original) in the context of Ensemble 1 (Fig. 3.9) as a function of the number of terms $N$ is shown with a solid line (cf. Fig. 3.11). Note that each term contributes on the average $\approx 1$.
    The total information (4.22) of the LFA reconstruction (4.67-4.68), sparsified with the serial algorithm outlined in the text, as a function of the number of referce points $|\mathcal{M}|$ is shown with dashed lines for $N \in$ \{600, 400, 300, 220, 110, 64, 32\}, from top to bottom, respectively.

    resentation has been reduced, but the information content and, therefore, the needed precision of the representational variables have increased accordingly. This is "good"-the running time of various higher-level algorithms depends very strongly on the dimensionality of the representation, but very weakly, practically not at all, on the precision of the calculations themselves.

    The representation produced by the described sparsification algorithm, utilizing the residual correlations $\mathbf{P}$ to reconstruct $O(\mathbf{x})$, contains all of the information in $O(\mathbf{x})$ and so possesses all of its desirable properties-best reconstruction, generalization and object constancy. In addition, it is sparse-distributed, instead of dense, which reveals the low dimensionality of the object space.

    Finally, in ensembles wherein the images contain a relatively large amount background, the most prominent "features" are the transitions from the back-

[^4]:    ${ }^{44}$ It would be interesting to check the performance of PCA (Section 3.2.2) with that of Flexible Template Matching, based on LFA.

[^5]:    ${ }^{3}$ Even though the eyebrows are close to the origin (the horizontal line through the eyes), they are thin-it is evident from $\boldsymbol{\Psi}_{1}$ and $\boldsymbol{\Psi}_{13}$ that the distance from the eyebrows to the eyes is about 5 eyebrow heights, and a scaling of 10\% will produce a relatively large change in eyebrow location. This degree of freedom is what is observed on $\boldsymbol{\Psi}_{8}$.
    ${ }^{4}$ Intuitively, when the asymmetric ensemble is scaled up or down, its modes are themselves scaled up or down. The symmetrizing is done by, effectively, diagonalizing a new correlation matrix, which is the sum of the original one (2.45) and an analogous one, constructed by the scaled modes. The scaled modes are not orthogonal to the original modes; they are nontrivial linear combinations of them. Therefore, after the combined correlation matrix is diagonalized, almost any particular original mode gets mixed up with some of the others those to which its scaled version projects most.

    96 tain feature, such as $\Psi_{12}$ on Fig. 3.9, happens to correspond to a given mode in a certain ensemble, symmetrization, even partial, spreads it to many other modes.

    This would explain why the simplistic approaches for face classification, attempted in Section 3.2.2, did not work so well-even a simple miss-alignment of the face, an unavoidable, but understandable, low-dimensional operation, will shift information between the PCA coefficients in a non-trivial manner.

    The feature localization problem is very clearly evident in $\Psi_{100}$ and $\Psi_{200}$. We would say that what is observed is "the cosines of the mouth"-repeated, almost identical structures, based on the basic shape of a mouth.

    Interestingly, $\Psi_{500}$ and $\Psi_{1000}$ show quite discernible face content; even $\Psi_{2000}$, arguably deep in the pixel-noise regime, does not seem "random."

    All of this suggests that the underlying dimensionality of the symmetrized ensemble (Fig. 5.1) is higher than that of the corresponding asymmetric one (Fig. 3.9)-not surprising in light of the fullness of the symmetric retinal ensemble.

    Is the symmetrized ensemble a better, or a worse, ensemble?
    One way to try to answer this question is to compare the successive reconstructions of Example 1 (Fig. 3.10-original) in the context of the symmetrized (Fig. 5.2) and the asymmetric (Fig. 3.12) ensembles, respectively.

    Somewhat surprisingly, the reconstruction with the symmetrized ensemble is better for any $N>60$. Also, the respective perceptual identity information in the error is smaller, almost nonexistent in $\phi_{1000}^{e r r}$.

    The same conclusion is supported by the comparison of the respective $S-U$ diagrams on Fig. 5.3. Not only does the symmetrized ensemble have better SNR of the reconstruction (obviously-the ensemble is full, and the example can be reconstructed with arbitrary precision for large enough $N$ ), but it is achieved more cheaply, in terms of both representational entropy and dimensionality, for a given SNR.

    Whereas the entropic cost is rapidly growing after $N \approx 300$ for the asymmetric ensemble, it is relatively flat in the regime $N \in[200,500]$ for the symmetrized one. This means that the genuine information about $\mathcal{P}[\phi(\mathbf{x})]$ extends to much higher $N$ there.

    The discussion so far supports the conclusion that the symmetrizing of the ensemble helps reveal more of the genuine structure of $\mathcal{P}[\phi(\mathbf{x})]$ and is, therefore, "good." ${ }^{5}$

[^6]:    ratio they enforced left-right symmetry and effectively doubled the size of their ensemble; arguably, all other symmetries have been fixed by the mechanical affixing of subjects' heads to the oval opening. We tend to think that slight scale and translational symmetrizing would have helped there too.
    ${ }^{6} \mathrm{cf} . \Psi_{8}$ on Fig. 5.1
    ${ }^{7}$ Since the phenomenon observed on Fig. 5.4e is not due to the symmetrization, we will

    ![](https://cdn.mathpix.com/cropped/5fff204a-b675-4b41-925e-7cb5ba4e9fe4-06.jpg?height=596&width=809&top_left_y=1437&top_left_x=139)
    Figure 5.3: $S-U$ diagram of a reconstruction with Ensemble 6 ( $T=10944$, $V=3840$ )

    The SNR of the reconstruction of the example Fig. 3.10-original is plotted on the horizontal axis, and the average entropy per component (cf. Fig. 3.8) is plotted on the vertical axis.
    The first and every 50-th reconstruction are shown with plusses and crosses for Ensemble 6 and Ensemble 1, respectively, and every 200-th reconstruction is shown with squares and triangles, respectively.
    The $S-U$ diagram of Ensemble 6 saturates to $\mathrm{SNR} \approx \infty$ very quickly after SNR $\approx 16$, leveling off at $\langle S\rangle=2.35$, thereby forming a realtively smooth S-shaped curve after SNR $\approx 7$.

    The fact that the LFA representation is stable under symmetrization is another very important property of LFA, in contrast with PCA (Fig. 5.1). But of course, one might say-since the scale/translation symmetry just applied is what LFA was designed to capture, it is not a big surprise that it does, actually, capture it.

    We will have to agree with this point of view. When we designed LFA (Chapter 4), we believed that there were symmetries in the ensemble that were not naturally represented by PCA. We called this property "locality" a notion that there are relations among the grid locations themselves. We enforced

[^7]:    ${ }^{8}$ There is always the problem, given an image $I^{t}$ that contains a face, how to choose the parameters of the symmetry breaking $\alpha^{2}$. For the ensembles used in Chapter 3, the determination of $\alpha^{t}$ was performed by Gillian Malone; with great care and involvement, she gathered several thousand images, $\left\{I^{t}\right\}_{t \in T}$, and determined the locations of the eyes, $\left\{\left(X_{l}^{t}, Y_{l}^{t} ; X_{r}^{t}, Y_{r}^{t}\right)\right\}_{t \in T}$. From them, the wonderful set of high-quality coefficients $\left\{\alpha_{G, M}^{t}\right\}_{t \in T}$ was determined, which was an indispensable element of the research, whose results are reported in this Thesis.

[^8]:    ${ }^{9}$ From now on, till the end of the section, we will assume that $N$ is fixed to some reasonable, for the purpose at hand, value.

[^9]:    ${ }^{11}$ Very importantly, variations due to pose are missing. They generate an extremely strong effect on the ensemble; this is the reason only examples with frontal poses were considered in this Thesis.

[^10]:    ${ }^{12}$ Actually, due to the close nursing position, when the image of one of the eyes in the bootstrap ensemble is centered on the respective fovea, the image of the other is very close to the periphery, almost invisible. If we ignore for a moment the presence of corpus callosum, the band of commissural fibers uniting the cerebral hemlspheres, and look from the perspective of a single hemisphere, the sensory ensemble contains only one eye, which is always centered at the fovea; this obviates the need for any genetic storage of $\Psi_{r}$.
    ${ }^{13}$ In Chapter 3 we built the PCA analysis of faces directly on the output of the "photo receptors"- $\phi^{t}(\mathbf{x})$ was interpreted as the luminosity value at the grid point $\mathbf{x}$. This worked

    108
    Whenever these feature representational modules also utilize LFA, the step can be iterated. Such object-features LFA representational module assemblies will form a hierarchically connected system, not unlike the structure of the primate neocortex.

    So far, we have drawn an analogy between the forward projections of one cortical area to others, and the forward projections of the object to the feature representational modules. A characteristic property of the cortex is that, under weak assumptions, if area $A$ projects forward to area $B$, then almost always area $B$ projects backward to area $A$ (Mumford 1991 and references therein). ${ }^{14}$

    To explore a possible role for backward projections between LFA representational modules, we will consider the phenomenon observed on Fig. 5.4e. In Ensemble 6, where about $20 \%$ of the faces have eyeglasses, the "cheek-bone" receptive fields have given way to "eyeglasses" receptive fields.

    This is a problem; when we try to reconstruct an example without eyeglasses in the context of the eyeglass-aware ensemble, at least one point in the cheekbone region will have to participate in the sparsified representation (4.73). Unfortunately, its reconstructor $P_{m}(\mathrm{x})$ (Fig. 5.4e) will tend to create an illusion of faint eyeglasses (cf. $\phi_{100}^{\text {err }-} \phi_{500}^{\text {err }}$ on Fig. 5.2), ${ }^{15}$ and it will take many more other reference points to kill it off an unreasonable arrangement, leading to unnecessary high dimensionality. ${ }^{16}$

    This suggests that ensembles of faces with and without eyeglasses have to be somehow separated to prevent attempts at reconstructions with the wrong
    well for two reasons: we had a good initial guess $\left\{\alpha_{G . M .}^{t}\right\}_{t \in T}$ about the symmetry breaking for the ensemble of faces (footnote 8 on page 101); also, we had only one ensemble to deal with, so we could mix information about both the symmetric, $\mathcal{P}_{\text {images }}$, and asymmetric, $\mathcal{P}_{\text {abjects }}$, probability distributions in one representational module (Fig. 5.1). In general, when a sensory system is confronted with many types of objects, replicating the symmetric part of the information in all object representational modules is wasteful.

    Moreover, when we symmetrized the ensemble (Section 5.1), we felt that an intermediate representation, making explicit the global symmetries, will be much better suited for the task than the luminosity representation that was used.
    ${ }^{14}$ Anatomically, the forward and backward projections are quite distinguishable. In a simplistic description (for a review, see Felleman and Vau Essen 1991), the projections of the forward, or ascending, pathway originate in the superficial pyramidal cells of area $A_{3}$ and terminate in layer IV, the standard cortical input layer, of area $B$; the backward, or descending, pathway includes projections that originate in the deep pyramidal cells in layer V of area $B$ and terminate mainly in layers I and VI of area $A$ (see Fig. 1 of Mumford 1992).
    This clear anatomical distinction suggests distinct computational roles for the two types of pathways, an idea explored by Mumford (1991, 1992).
    ${ }^{16}$ Illusory contours have been observed as early as V1 and have been studied actively (Grosof et al. 1993; Hirsch et al. 1995; Ringach and Shapley 1996; Rubin et al. 1996; Rubin et al. 1997). It would be interesting to understand them from the point of view of reconstruction.
    ${ }^{16}$ This is very analogous to the spurious activity in the background, evident of Fig. 4.4 they are both due to the attempt to use statistical knowledge about one category to reconstruct objects in another.

[^11]:    ${ }^{22}$ In Section 4.4.3 we suggested that, even for degenerate object ensembles, a "rnulti-scale" representation of the type $\mathbf{K}_{j}^{(\mathbf{n})}=\sum_{r \in \Delta_{j}} \psi_{r}\left(\frac{1}{\sigma_{r}}\right)^{n}\left(\psi_{r},\right)$ (cf. 4.30) can result in additional dimensionality reduction (see discussion in footnote 42 on page 85).
    ${ }^{23} \mathrm{As}$ with any symmetry breaking, it can be understood as a definition of a restricted cosemble and, therefore, a parameterization of the original probability density $\mathcal{P}[\phi(\mathbf{x})]$, as outlined in Section 5.3.
    It would be interesting to check whether the restricted ensemble in the retinal case can account for the orientation selectivity of the cells in V1. Also, it would be interesting to know what the restricted ensemble is, and what cell properties it entails, for the case of natural sound.

[^12]:    ${ }^{24}$ The same argument can be advanced for speech recognition-since people's heads have different sizes and, therefore, resonate at different frequencies, the sound pressure waves due to a given speech phoneme will have components in different frequency bands; a multi-scale representation may recover its characteristic signature, which would be shifted to the group of cells representing that particular frequency band.
    ${ }^{25}$ The multi-scale representations in (Li and Atick 1994) were derived by explicitly fixing the $U$-symmetry (4.15). In contrast with (5.6), such treatment keeps the number of output variables constant, and, therefore, they continue to be fully-decorrelated. In Section 4.4.1 we called this approach static sparsification; it does not reduce dimensionality.
    ${ }^{26}$ Of course, this view demands changes in the dynamical equation-(4.75) is a simplistic description, and even all the freedom in the choice of g may not be enough to accommodate spiking. Nevertheless, we will refrain from offering more realistic dynamical descriptions, because, anyway, we are dealing with an unrealistic ensemble-of static natural images.

[^13]:    The real ensembles are dynamic, and spikes are generated at some of the first steps of retinal processing; a realistic description would need to start at that level something we will discuss in Section 5.6.
    ${ }^{27}$ The treatment in this, and the following, section is regardless of the mechanism that determines which units to become active. We are interested in the question, once the unit is decided upon, what happens to the representation. In Section 5.6 we will see that the answer to this question can prompt some reasonable decision strategies.

[^14]:    ${ }^{29}$ Actually, this may be the reason the order $M-1$ of DPCM in practical applications is usually kept relatively small.

[^15]:    ${ }^{35}$ For the study of H1, Bialek et al. (1991) find information rates of ~ 300 bits/second, which, at ~100 spikes/second is ~3 bits/spike. In various other sensory systems-the bullfrog sacculus (Rieke et al. 1992) and the cricket cercal system (Warland et al. 1991)similar information transmission rates have been measured.
    ${ }^{36} \mathrm{An}$ attempt to base them on two grid points, $t_{M}$ and $t_{M-1}$, albeit also in a timeinvariant manner, has been made, but it had produced only marginally better estimates ( $5-15 \%$, depending on the system under study).
    ${ }^{37}$ Since (5.36) has more degrees of freedom, obviously, it should do better than (5.43). There are two things to test for Does (5.36) do close to 100\% axon capacity utilization? and, Is there a clear relationship between the statistical properties of the stimulus on one hand, and the optimal reconstructors from the experiment, on the other?

    In general, care should be taken in interpreting the results of measurements in actual systems, since they necessarily depend on various engineerig constrains. The typical pitfall

[^16]:    ${ }^{31}$ Notably, this is the first time in this Thesis, when we equate topography with topology (footnote 3 on page 10), of the time axis $t$. Necessarily so, because time plays a very special role in spiking.

[^17]:    ${ }^{32}$ The values of the projection $a_{m}=\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}_{\|}\right\rangle$will be distributed according to the original probability distribution, normal by assumption (2.49), conditional on $o_{m} \geq O_{m}$. The maximum likelihood estimate in this case is the mean of this conditional distribution. Interestingly, for a normal distribution, and for $O_{m}$ large enough, it is very close to $O_{m}$, slightly larger. The part of the spike's information content, that is due to $U_{m}$, can be calculated by the a priori and the a posteriori probability distributions; interestingly, it grows with $O_{m}$ the higher the threshold $\theta$, the larger the information per spike. Of course, the higher $\theta$, the lower the probability of a spike; in general, a balance between these two criteria should be achieved.
    ${ }^{33}$ For simplicity. $O_{m} p_{m}$ and $O^{\prime} p^{\prime}$ are shown to have the same lengths on Fig. 5.10. In general, this is neither necessary, nor interesting.
    ${ }^{34}$ Interestingly, the lack of a spike at $\mathbf{x}$ can be very informative. First, it changes the probability distribution along $U_{m}^{\prime}$; the smaller the angle $\alpha$ between $\mathrm{q}^{\prime}$ and $\mathrm{q}_{\mathrm{x}_{\mathrm{m}}}$, the more informative the lack of a spike. Ultimately, when $C \rightarrow A$, half of the axis $U_{m}^{\prime}$ is excluded, and up to a whole bit can be transmitted this way. Also, as $\alpha$ decreases, the upper bond for $o_{m}$ approaches $O_{m}$, and the information due to the localization of $s_{\|}$in $U_{m}$ increases.

    This is intuitively correct; $\cos \alpha=P_{m}\left(x^{\prime}\right)$, the output correlation between two adjacent grid points. When the uncertainty of timing, $\Delta t$, decreases, the points can be made closer and, therefore, more correlated, and the information content of the spike increases. Also, this increase in the timing resolution increases the channel capacity of the axon. It would be interesting to know whether these increases are mutually proportional, and any operational point can be chosen, or there is a clearly defined optimal axon channel capacity, based solely on this criterion.


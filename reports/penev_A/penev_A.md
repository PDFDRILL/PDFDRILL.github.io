# Local Feature Analysis: <br> A Statistical Theory for Information Representation and Transmission 

A thesis presented to the faculty of<br>The Rockefeller University<br>in partial fulfillment of the requirements for the degree Doctor of Philosophy<br>Penio S. Penev<br>Laboratory of Computational Neuroscience<br>The Rockefeller University<br>1230 York Avenue<br>New York, NY 10021-6399<br>http://venezia.rockefeller.edu<br>penev@venezia.rockefeller.edu

May, 1998

A wing would be a most mystifying structure if one didn't know that birds flew. One might observe that it could be extended a considerable distance, that it had smooth covering of feathers with conspicuous markings, that it was operated by powerful muscles, and that strength and lightness were prominent features of its construction. These are important facts, but by themselves they do not tell us that birds fly. Yet without knowing this, and without understanding something of the principles of flight, a more detailed examination of the wing itself would probably be unrewarding.

Horace Barlow, Principles (1961b)

## Acknowledgments

The author wishes to express his admiration and gratitude to Dr. William O'Baker.
A true Renaissance Scholar, Dr. Baker has long affirmed that science is interdisciplinary-that intellectual collaboration and exchange on the border of fields will push the frontier further and a new field will be bom.

Dr. Baker's vision that basic research, guided by scientific curiosity and calculated risk, is the driving force of science, his strong commitment to freedom in science, and his passion for education had fallen on the fertile soil at The Rockefeller University, where he has served as a Chairman of the Board, resulting in both the unique Graduate Program, and the establishment, in bis honor, of the William O'Baker Fellowship, so generously extended to the author.

The author is grateful to Professor Mitchell Feigenbaum for the new, inspirational look of Mathematics, which he has willingly shared, as well as for his unobtrusive insistence that people, in general, know what they are talking about-both have been powerful driving forces for the author.

The author is grateful to Dr. Joseph J. Atick, who made possible the author's tenure at The Rockefeller University, for the unfaltering tolerance through the years, as well as for applying the correct pressure at the correct time, which led the author to the rich scientific field presented in this Thesis.

The author is grateful to Dr. Dimitar B. Nikolov, who has constantly provided an example, moral and material support, and advice, at times much needed.

The author wishes to thank Dr. J. J. Atick, Dr. A. Norman Redlich, Dr. Dawei D. Dong, and Dr. Paul A. Griffin for the useful and pleasant conversations.

The understanding and consideration the Graduation Committee, so genrously extended to the author, were much needed and are deeply appreciated.

This Thesis wouldn't have had the current logic and language flows, wasn't it for the dissective sight of Professor Bruce Knight, gratefully accepted.

Various people contributed substantially to various part of this research: Gillian Malone prepared the databases (footnote 8 on page 101); Dr. P. Griffin suggested the treatment, and William Lu helped write some of the programs for Section 3.2.2; discussions with Prof. B. Knight lead to the layout of Chapter 4; with Dr. John Robbins, to the inclusion of Appendix A.2; with Prof. Robert M. Shapley, Fig. 4.6 and Fig. 4.7; with Prof. M. Feigenbaum, Appendix A.3.

Finally, the author expresses his deepest admiration and gratitude to his wonderful wife and daughter, who have sacrificed much for this Thesis to happen.

## Contents

## List of Figures

1 Introduction ..... 2
2 Principal Component Analysis ..... 9
2.1 Redundancy Reduction ..... 9
2.2 PCA as a Factorial Code ..... 11
2.3 Singular Value Decomposition: A Canonical Basis for PCA ..... 16
3 Principal Component Analysis for Face Recognition ..... 22
3.1 PCA of Face Ensembles ..... 23
3.1.1 $T=15$ ..... 23
3.1.2 $T=87$ ..... 28
3.1.3 $T=1038$ ..... 34
3.2 Face Recognition by PCA ..... 41
3.2.1 The Initial Hypothesis ..... 42
3.2.2 In Search of a Discriminability Measure ..... 43
3.3 The Shortcomings of PCA ..... 50
4 Local Feature Analysis ..... 54
4.1 Introduction ..... 54
4.2 Linear Factorial Codes for Symmetric Ensembles ..... 55
4.3 Local Features from Global Modes ..... 65
4.4 Sparse-distributed from Topographic Representations ..... 71
4.4.1 Static vs. Dynamic Sparsification ..... 72
4.4.2 Reconstruction of One Simple Local Feature ..... 74
4.4.3 Full LFA Reconstruction ..... 77
4.4.4 Serial Sparsification: An Efficient Algorithm ..... 81
4.4.5 Feature Templates with LFA ..... 87
4.4.6 Parallel Sparsification: A Biologically Plausible Model ..... 90
5 Symmetries and LFA ..... 93
5.1 Partial Re-Symmetrization of Object Ensembles ..... 93
5.1.1 Re-Symmetrization and PCA ..... 98
5.2 Bootstrapping the Local Symmetry Breaking ..... 101
5.2.1 Automatic Symmetry Breaking for a Single Example ..... 101
5.2.2 Bootstrap Mechanism ..... 104
5.3 Hierarchical LFA Assemblies ..... 108
5.4 Dimensionality Reduction in Fully-Symmetric Ensembles by Multi- Scale LFA ..... 111
5.5 Successive Sparsification ..... 114
5.5.1 Successive Inversion ..... 115
5.5.2 Successive Reconstruction ..... 116
5.6 Spike Generation in Autocorrelated Time Series ..... 119
5.6.1 Predictive Coding as Successive Sparsification ..... 119
5.6.2 Spike Generation by Successive Sparsification ..... 122
6 Discussion ..... 128
A Appendices ..... 131
A. 1 The Databases ..... 131
A. 2 A Dangerously Small Ensemble ..... 133
A. 3 The Distribution of PCA Coefficients for Faces ..... 139
A. 4 The Hybrid Representation ..... 147
A. 5 Sparsification Before vs. After Decorrelation ..... 149
A. 6 LFA and Infinite Translation-Invariant Ensembles ..... 151
3.1 PCA Analysis of the noglasses Ensemble $(T=15)$ ..... 25
3.2 Reconstruction with the noglasses Ensemble ( $T=15$ ) ..... 26
3.3 PCA Analysis of the full Yale Ensemble $(T=87)$ ..... 28
3.4 Reconstruction with the full Yale Ensemble ( $T=87$ ) ..... 29
3.5 PCA Analysis of the h3q and third Yale Ensembles $(T=87)$ ..... 30
3.6 Reconstruction with the h3q and third Yale Ensembles ( $T=87$ ) ..... 31
3.7 SNR with the $T=87$ Yale Ensembles ..... 32
3.8 $S-U$ diagrams of reconstructions with the $T=87$ Yale Ensembles ..... 33
3.9 PCA Analysis of Ensemble 1 ( $T=1038, V=3840$ ) ..... 35
3.10 Reconstruction with Ensemble $1(T=1038, V=3840)$ ..... 37
$3.11 S-U$ diagram of a reconstruction with Ensemble $1(T=1038$, $V=3840$ ) ..... 38
3.12 Successive reconstruction in the cross-over regime of Ensemble 1 ..... 39
$3.13 \log$ Spectrum of Ensemble $1(T=1038, V=3840)$ ..... 40
$3.14 \mathrm{log}-\log$ Spectrum of Ensemble $1(T=1038, V=3840)$ ..... 41
3.15 Discriminability of Ensemble $5(T=3279, V=3840)$, linear $r$ ..... 45
3.16 Discriminability of Ensemble $5(T=3279, V=3840), \log r$ ..... 46
3.17 ROC for individual eigenmodes of Ensemble 5 ..... 48
3.18 ROC for the Fisher discriminability measure ..... 49
3.19 ROC for the "naïve" discriminability measure ..... 50
3.20 ROC for the component probability discriminability measure ..... 51
3.21 PCA Analysis of Ensemble 4 ( $T=1038, V=11520$ ) ..... 52
3.22 log Spectrum of Ensemble $4(T=1038, V=11520)$ ..... 52
4.1 Receptive Fields K and Residual Correlations $P$ for I'mages of Faces, Ensemble 1 ..... 68
4.2 Receptive fields $\mathbf{K}$ and residual correlations $\mathbf{P}$ for surfaces of heads, Ensemble 2 ..... 69
4.3 Successive LFA outputs in the cross-over regime of Ensemble 1 ..... 71
4.4 Resource Allocation by the Serial Sparsification Algorithm ..... 83
4.5 Recunstruction with a Fixed Number of Values (64) ..... 84
4.6 Comparison Between PCA and LFA $S-N$ Diagrams ..... 86
4.7 Scaling of LFA S-N Diagrams ..... 87
4.8 Segmentation by Sparsification ..... 88

## List of Tables

3.1 Statistics for the Face Classification Study $\left(T_{\text {restricted }}=3049\right)$ ..... 44
A. 1 Probability in the Tails of the Normal Distribution ..... 142


#### Abstract

Low-dimensional representations of sensory signals are key to solving many of the computational problems encountered in high-level vision. Principal Component Analysis (PCA) has been used in the past to derive practically useful compact representations for different classes of objects. One major objection to the applicability of PCA is that it invariably leads to global, nontopographic representations that are not amenable to further processing and are not biologically plausible. In this Thesis we present a new mathematical constructionLocal Feature Analysis (LFA)-for deriving local topographic representations for any class of objects. The LFA representations are sparse-distributed and, hence, are effectively low-dimensional and retain all the advantages of the compact representations of PCA. Unlike the global eigenmodes, they give a description of objects in terms of statistically derived local features and their locations. Moreover, the LFA representation exposes partial, local symmetries, which are present in the ensemble, but are not naturally captured by PCA, which allows further reduction of the dimensionality of the representation. We illustrate the LFA theory by using it to extract local features for three ensembles of objects-2D images of faces without background, 3D surfaces of human heads, and, finally, 2D faces on a background.

We understand the preparation of object ensembles as breaking of global symmetries and show how to do it automatically, upon which we base a bootstrap mechanism for symmetry-breaking. We understand the localization of features as breaking of local symmetries, which define new ensembles of features whose representational modules are hierarchically interconnected, in a manner similar to the thalamo-cortical and cortico-cortical computational feedback loops, and serve as active blackboards.

We generalize LFA to the scale- translationally-symmetric ensembles of natural signals, with full PCA dimensionality, and show how to reduce it by the construction of multi-scale representations. We show that the sparsification step of LFA, when applied to 1 -dimensional time-dependent infinite ensembles, results in representation and transmission of the signal with only on type of variables-the sparse set of timings of, otherwise identical, events; this is a key property of the sensory coding of signals with action potentials (spikes) in most biological systems.

Finally, we argue that LFA is applicable to all levels of sensory processingfrom the initial stages of acquisition of natural signals and their representation and transmission with spikes, through the intermediate stages of spatiotemporal sensory processing, all the way up to high-level stages of signal processing categorization and hierarchical object representation in the cortex.


## Chapter 1

## Introduction

In most evolved animals the representation of sensory signals formed by the peripheral receptors is very high-dimensional. For example, in the human retina there are more than six million cones, each capable of discriminating about a hundred shades of light. From the activity of this huge array of receptors the brain has to discover where and what objects there are in the field of view and recover in detail their attributes such as color, texture, and 3D nature.

Moreover, such complex calculations must be carried out and trigger behavioral decisions in real time; for the delay in reactions often makes the difference between life and death for organisms under natural conditions, both for prey and predators.

Since the execution time of signal-processing algorithms critically depends on the dimensionality of the input space, it can be argued that one of the goals of sensory processing should be to reduce this dimensionality. For example, some high-level vision problems become more tractable when formulated in a low-dimensional space, e.g., shape-from-shading (Atick et al. 1996a) and face recognition (Atick et al. 1995). In the more general context of neural networks, it has been found that good generalization critically depends on finding the correct low-dimensional representation (see the review by Geman et ai. 1992).

In codes that represent natural signals, one expects to be able to lower the dimensionality considerably because these signals possess significant statistical regularities, or redundancies (for experimental measurements of various regularities see Burton and Moorhead 1987; Field 1987; Tolhurst et al. 1992; Hancock et al. 1992; Ruderman and Bialek 1994; Ruderman 1994b; Dong and Hancock et al. 1992; Ruderman and Bialek 1994; Ruderman 1994D; Dong and Atick 1995a; Atick et al. 1996b). These are manifested in the fact that the eusemble of actual activatious of sensory receptors in response to natural stimuli occupies a small fraction of the total allowed phase space-the space of all possible receptor activations. Thus, one can hope to lower the dimensionality by finding a suitable parameterization of the subspace occupied by natural stimulation.

The fact that not all sensory signals are equally probable in the context
of natural ensembles has resulted in the proposal of redundancy reduction as a design principle for sensory processing (Barlow 1961b). It builds on the idea that reduction of redundancy is an important operation in the handling of sensory information, an idea advanced by Attneave (1954), MacKay (1956), and Craik (1943) in the context of psychology, Barlow $(1959,1961 \mathrm{a})$ in the context of physiology, and expressed clearly in the writings of Mach (1914) and Pearson (1892) in the context of much higher mental processes. Redundancy reduction postulates that sensory messages should be signaled with codes whose lengths ${ }^{1}$ are proportional to their information content, in the context of Information Theory (Shannon and Weaver 1949) given by the negative logarithm of their respective probabilities.

One way to reduce redundancy has been via factorial codes (Barlow et al. 1989; Linsker 1988; Atick and Redlich 1992; Redlich 1993a)-representations in which the probability of observation of a particular signal is a product of independent factors-the probabilities of observation of the separate variables that code for it. In other words, the goal is for the variables in such a code to be statistically independent of each other and code for statistically independent aspects of the given signal ensemble.

Moreover, it was suggested (Barlow 1989) that if the "strength" of the output variables of a factorial code is proportional to their information content, such a code will represent directly not only the sensory signal itself, but also its probability; hence, it will be trivial to look for "suspicious coincidences" in its output.

Models based on linear factorial codes reducing second-order statistical properties of ensembles of natural stimuli have been extremely successful in deriving exact quantitative psychophysical and some qualitative and quantitative aspects of neuro-physiological properties of the spatial retinal (Atick and Redlich 1992), spacio-temporal LGN (Dong and Atick 1995b; Dan et al. 1996) and color retinal (Atick et al. 1992) and color early cortical (Atick et al. 1993) processing.

Given the success of redundancy reduction based on the second-order statistics of the ensembles of natural stimuli during the early stages of sensory proessing, one might ask the question, What next? What is the guiding principle of higher-level sensory processing? Indeed, if a factorial code for visual stimuli is already achieved at the LGN stage, what is the purpose of the higher neural areas including the cortex? Has the time come to abandon second-order statistics, which by this argument do not exist any more past the LGN, and start reducing redundancy based on some higher-order statistics? And if yes, which type of higher-order statistics?

In trying to answer these questions, we turn to the architecture of the
${ }^{1}$ Barlow (1961b) made the "simplifying assumption" that those lengths are the durations of the trains of nerve impulses that code for sensory messages, noting that "the safe course here is to assume that the nervous system is efficient." We will revisit this point in Section 5.6. et al. 1995). ${ }^{3}$

So far, however, the most practical and systematic method has been Principal Component Analysis (PCA), also known as the Karhunen-Loève Procedure. PCA assumes that the probability density of the input ensemble in the space of receptor activation patterns is significantly nonzero only in a low-dimensional linear subspace, which is subsequently parameterized with a linear expansion in the eigenvectors of the correlation matrix of the ensemble. ${ }^{4}$ The power of PCA stems from its ease of computability and its general applicability, and so far it has been used in many real-world problems. For example, it has been used to produce efficient representations of 2D faces-eigenfaces (Sirovich and Kirby 1987)-and of 3D heads-eigenheads (Atick et al. 1995)-which have been shown to generalize well and hypothesized to be useful representations for face recognition and for shape-from-shading.

Since the initial attempt to use the PCA representation for face classification (Turk and Pentland 1991), linear representations for face recognition has been an active area of research (Belhumeur et al. 1997; Etemad and Chellappa 1997 and references therein). Nevertheless, a general and robust linear method has been elusive so far.

In Chapter 3 we use the method of PCA to study the statistical properties of ensembles of human faces; in this case, we build efficient, low-dimensional representations. In order to study their utility for the task of face classification, we apply to them the method of Linear Discriminant Analysis and find that identity information, although entirely contained in a relatively small number of PCA coefficients, is distributed in a non-trivial manner throughout them.

Having revealed the limitations of PCA for object classification, we argue that this method is incapable of capturing, in a natural way, some of the symmetries present in the original ensemble. For example, PCA is not capable of extracting local-feature-like structures in objects, which have been hypothesized to be important for recognition (Yuille 1991; Yuille et al. 1992). Also, in general, PCA produces global linear filters whose output is not very naturally amenable to subsequent processing. Local representations are desirable since they offer robustness against variability due to changes in localized regions of the objects. Another evidence for the value of local representations is seen in the nervous system itself; the computations in the retina, LGN, and the primary cortical areas are retinotopic and, therefore, local.

Next, we pose the question, Can we rectify these shortcomings of PCA with out resorting to complex, practically noncomputable algorithms? In Chapter 4 we show that the answer is yes. More precisely, for any input ensemble of objects, we show how to construct automatically, from the low-dimensional, but global, PCA basis, an equally low-dimensional representation in terms of the

[^0]mammalian cortex. One of its distinguishing characteristics is that although anatomically very uniform, it is subdivided into distinct functional areas, each processing only a limited subset of the sensory stimuli and/or aspects thereof.

The cortical subdivision into areas, their functional specification, interconnectivity, and possible role in information processing have been an object of vigorous and systematic research (Felleman and Van Essen 1991). There are several lines of evidence that, in the cortex of primates, there are object-class specific functional areas, face-specific among others (Nachson 1995). These include experiments utilizing MRI of cortex activity in humans (Allison et al. 1994), extra-striate cortex neurophysiology in macaque (Desimone 1991; Gross 1992; Rolls 1992; Perrett et al. 1992), and studies of face recognition impairments, prosopagnosia among others, in humans (Young 1992).

Object recognition in general, and face recognition in particular, have also been a long-standing problem in the Engineering and Artificial Intelligence communities (Baron 1981; Chellappa et al. 1995). It would, therefore, be of considerable interest to understand to what degree the success of the redundancy reduction principle applies to the task of object representation and analysis.

Naturally, if one is concerned not with the translation- and scale-invariant ensemble of natural images, but with a limited class of objects, for example the ensemble of correctly aligned and scaled human faces, there is additional expectation for finding a low-dimensional representation. ${ }^{2}$ Indeed, not every natural signal is a human face, so even the limited subspace of the receptor activation space occupied by natural signals, is not uniformly populated with faces. Intuitively, one would expect that there are a small number of variables that can describe an object from the restricted ensemble-much lower than the number of receptor elements needed to represent it, and practical measurements have confirmed that for the case of human faces (Sirovich and Kirby 1987).

Currently, there are many algorithms of varying complexity for attempting to discover low-dimensional representations of signals by relying on their statistical regularities. These include algorithms for Principal Component Analysis (Linsker 1988; Oja 1989; Sanger 1989; Földiák 1990; Plumbey 1991), Gaussian Component Analysis (Goodall 1960; Atick et al. 1993), Independent Component Analysis (Jutten and Herault 1991; Comou 1994; Bell and Sejnowski 1995), Factorial Learning (Barlow et al. 1989; Hentschel and Barlow 1991; Schmidhuber 1992; Redlich 1993a; Redlich 1993b; Atick et al. 1993), Infomax (Linsker 1988), Imax (Becker and Hinton 1992), Projection Pursuit (Intrator 1992), Matching Pursuit (Phillips and Vardi 1995), and symplectic maps (Deco

[^1]objects' local features. The two-step procedure-which we call Local Feature Analysis (LFA)-initially derives a dense set of linear filters with local support that are defined at each point of the receptor grid and are different from each other; the filters are optimally matched to the input ensemble and their outputs are as decorrelated as possible.

At the first step of LFA, the receptor activation pattern due to any incoming object is filtered with this dense set of receptive fields. Because the object ensemble is, in general, with reduced dimensionality, the dense set of LFA outputs, entirely contained in the PCA subspace, is linearly dependent. Therefore, full decorrelation cannot be achieved, and the outputs necessarily contain residual correlations.

At the second step of LFA, those residual correlations are used to sparsify the output; it is represented by a small subset of all output units. The number of active units is on the order of the PCA dimensionality, and the location of the activity changes from one sensory input to another, thereby signaling explicitly additional information about the locations of the current object's features. Thus, the final representation is a local sparse-distributed, explicitly low-dimensional representation.

We propose two methods for sparsification: a practical implementation, which is very efficient on serial computers; and a neural network, which is biologically plausible and takes advantage of parallel computations.

We illustrate LFA by using it to derive local features in several different object ensembles that are similar to ensembles for which global representations have been derived in the past (Sirovich and Kirby 1987; Atick et al. 1996b). One ensemble is comprised of 2D images of faces without background and serves to illustrate the ability of the method to derive local features intrinsic to objects; it yields receptive fields for noses, mouths, eyes, cheeks, and so forth. It is worth noting that we have not put any structural knowledge about human faces in the definition of the input ensemble; we have only broken the translation and scale symmetries by first, applying an affine transformation on the original images so that the two eyes are mapped to standard locations, and then, restricting the image to only a rectangular window centered around them. This symmetry breaking ${ }^{5}$ has proven sufficient to allow the salient local features of the objects to be derived as emergent statistical properties of the ensemble itself.

- Given the success of LFA, it would be of interest to understand what the mathematical reasons behind it are, as well as what its implications are to neural processing and, in general, to signal processing of natural stimuli. In

[^2]Chapter 5, we take a look back and try to give a partial answer to those questions. We realize that part of this success is mathematically due to the novel parameterization of the probability density of the input ensemble, which retains the convenience of the second-order description and adds explicitly, though naturally, the flexibility of non-linearity.

In Section 4.4.5, we return to the problem of face recognition and propose how the positional information about the local features, now uncovered in the LFA representation, could be used for Flexible Template Matching a class of methods that utilize knowledge about local features.

In Section 5.2 we realize that the success of LFA critically depends on the initial breaking of the symmetry in the definition of the ensemble and ask the question how the parameters of this symmetry-breaking influence the properties of the resulting representation. We redefine our ensemble to include some small amount of explicit partial symmetry and find out that the receptive fields change progressively with the amount of symmetry we put back in-the featurelike receptive fields smear and gradually transform into the center-surround receptive fields, familiar from research on scale- and translation-invariant ensembles.

Further, we fix the ensemble and vary the parameters of symmetry-breaking for individual examples and find that from information-theoretic considerations alone, there is a "optimal" breaking of the symmetry for individual objects. The objects with optimally-broken symmetry influence the statistics of the ensemble, sharpening it and decreasing the dimensionality of the representation. This iterative process opens the possibility for a "bootstrap" symmetry-breaking-a strategy that obviates the need for supervision and gives way to evolutionary and developmental scenarios.

For a given object ensemble, we argue that the template representation of an individual feature across the objects in it can be treated as another object ensemble. Since the feature appears at slightly different locations within the objects of the initial ensemble, there will be substantial translation symmetry in the definition of the new ensemble. Nevertheless, the feature localization in the context of the old ensemble may be enough to initiate a round of bootstrap symmetry breaking in the context of the new one, thereby allowing a low-dimensional representations of the individual features to emerge, each operating on the representation of the object. We, therefore, propose a system of hierarchically connected LFA modules, which bears much resemblance to the hierarchical connectivity of primate cortex.

In Section 5.4 we revisit the fully translation- and scale-symmetric twodimensional ensemble of natural scenes from the point of view of sparsification. We argue that one way to take advantage of the more flexible parameterization of the input probability distribution is to construct a multi-scale sparsedistributed representation a strategy widely used in the visual and auditory neural processing.

## 7

Equipped with the notion of input-driven "spontaneons" symmetry breaking, we apply LFA to the translationally-symmetric one-dimensional ensemble of human speech signals, and try to build a multi-scale sparse-distributed representation. The resulting temporal sparseness leads us to questions about information transmission with discrete temporal impulses, which bear much resemblance to neural impulses propagating along axons.

Finally, in Chapter 6 we try to bring everything together and rephrase many of the above questions coherently in the language of LFA. We suggest that the old and time-tested strategy of information theoretic driven secondorder redundancy and dimensionality reduction, coupled with the non-linear steps of categorization and partial symmetry breaking, can be applied at many of the known stages of visual and auditory processing-from the step of initial conversion of the sensory information into, and its representation with, spikes at he single-unit level, through the early stages of spatial, temporal, and spatiotemporal processing in the retina and the thalamus, all the way deep into the cortical processing of complex objects flexibly comprised of features.

## Chapter 2

## Principal Component Analysis

One notable characteristic of natural stimuli is their high data rate. For example, the human retina has $\sim 6 \times 10^{6}$ cones, each capable of signaling about 100 distinct levels, ${ }^{1}$ whose output is changing with a characteristic time of ~ 10 ms, which results in a data rate of ~ 5 Gbytes/sec. Any system for processing sensory information natural or artificial has to face this problem immediately on its input receptor layer.

To address this problem, redundancy reduction has been proposed as a design principle for coding of natural stimuli. It is motivated by the observation that changes in natural signals are usually gradual, both in the spatial and the temporal domains, and, therefore, contain redundancies.

In this Chapter, we will present the problem in rather general mathematical terms and will describe one of the approaches to redundancy reduction- Principal Component Analysis (PCA)-in some detail.

In an attempt to gain better understanding of the method and its application, we will comment how it applies to the ensembles of sensory stimuli which we are studying and will, also, develop the notation that is used throughout the rest of this Thesis.

### 2.1 Redundancy Reduction

Let a sensory signal be given by $\phi(\mathbf{x})$ where $\{\mathbf{x}\}$ is a sampling, or receptor grid which needs not be regular, with $V$ total sampling points -the volume ${ }^{2}$ in the

[^3]physical space-that possess some topography ${ }^{3}$. The index $\mathbf{x}$ can be a spatial, temporal, spatio-temporal, or any other modality index or combination thereof. For still images $\phi(\mathbf{x})=I(\mathbf{x})$ with $I$, the light intensity, and $\{\mathbf{x}\}$, the 2D grid of photo receptors; for one-dimensional temporal signals such as sound, $\{x\}$ is the 1D time axis $t,{ }^{4}$ and $\phi(\mathbf{x})$ is the value of the instantaneous sound pressure at the eardrums $p(t)$; for surfaces of heads $\phi(\mathbf{x})$ is given by the radial map $r(\theta, \ell)$ in cylindrical coordinates.

An ensemble of sensory signals will be denoted by $\left\{\phi^{i}(\mathbf{x}), t=1, \cdots, T\right\}$ where $T$ is the total number of examples in the ensemble. We understand this as an input source of examples $\left\{\phi^{t}(\mathbf{x})\right\}$ which are drawn from an underlying probability distribution. We will denote the density associated with this probability distribution by $\mathcal{P}[\phi(\mathbf{x})]$.

To say that the ensemble has some redundancy is equivalent to saying that $\mathcal{P}[\phi(\mathbf{x})]$ is non-uniform-that not all examples from the ensemble are equally probable. ${ }^{5}$

The principle of redundancy reduction postulates that one should look for a transformation $\mathcal{K}$ of the input ensemble $\left\{\phi^{t}(\mathbf{x})\right\}$ into an output ensemble $\left\{\mathcal{O}^{t}(\chi) \equiv \mathcal{K}\left[\phi^{t}(\mathbf{x})\right]\right\}$, where the set $\{\chi\}$ labels the output variables $\mathcal{O}$ and is possibly different than $\{\mathrm{x}\}$, such that the redundancies are eliminated, and $\mathcal{P}\left[\mathcal{O}^{t}(\chi)\right]$ is uniform (or at least "more" uniform).

Methods for solving this problem, having various degrees of "directness," have been proposed in the literature. Here is the place to note that this challenge is presently intractable and always will be. $\mathcal{P}[\phi(\mathbf{x})]$ is an enormously huge object for even the most trivial ensembles. ${ }^{6}$ Even storing it is impossible,

[^4]not to mention trying to measure it with any degree of statistical confidence. Obviously, in trying to solve the redundancy reduction problem, one has to utilize somehow the redundancy in $\mathcal{P}[\phi(\mathbf{x})]$ itself. Any solution is approximate, because necessarily it can only be based on an approximation of $\mathcal{P}[\phi(\mathbf{x})]$. Ideally, any attempt at a solution should clearly state what this approximation is and what parameterization of $\mathcal{P}[\phi(\mathbf{x})]$ it entails.

### 2.2 PCA as a Factorial Code

For any ensemble $\left\{\phi^{t}(\mathbf{x})\right\}_{1}^{T}$, where $T$ is big enough to ensure stationarity, PCA defines the correlation matrix as the ensemble average

$$
R(\mathbf{x}, \mathbf{y})=\left\langle\phi^{t}(\mathbf{x}) \phi^{t}(\mathbf{y})\right\rangle_{T}
$$

and approximates $\mathcal{P}[\phi(\mathbf{x})]$ with the joint normal density: ${ }^{7}$

$$
\mathcal{P}[\phi(\mathbf{x})] \propto \exp \left\{-\frac{1}{2} \int_{V} d \mathbf{x} \phi(\mathbf{x}) \int_{V} d \mathbf{y} R^{-1}(\mathbf{x}, \mathbf{y}) \phi(\mathbf{y})\right\}
$$

From (2.2) we see that $\mathcal{P}[\phi(\mathbf{x})]$ is parameterized with the values of $R(\mathbf{x}, \mathbf{y})$, which for many ensembles is a manageable parameterization. ${ }^{8}$

The appearance of (2.2) suggests that the complexity of our notation is about get out of hand, so we devote this Section to switching to a more frugal
light intensities can assume one of 100 different values roughly the numbers of shades of gray the human eye is sensitive to $(\phi: 4000 \mapsto 100)$, we have $100^{4000}$ different possible examples $\phi(\mathbf{x})\left(\phi \in \mathbf{1 0 0}{ }^{\mathbf{4 0 0 0}}\right)$ and we need that many memory cells to store the value of $\mathcal{P}[\phi(x)]$ at each $\phi(x)$. If we decide to store only one bit of information-whether the image is "probable" or not-then $\mathcal{P}: 100^{4000} \mapsto 2\left(\mathcal{P} \in 2^{1000^{4000}}\right)$, and we need $100^{4000}=10^{8000}$ bits, or $\sim 10^{7990}$ Gigabytes.

For comparison, at the current pricing of on-line disk storage, the population of the U.S.A. could buy with its annual GNP of $\sim$ USD $5 \times 10^{12}$ about $10^{11}$ Gigabytes, or it would take $10^{7978}$ years to buy just the storage for one instance of $\mathcal{P}[\phi(\mathbf{x})]$. This is far from comparable with the age of the Universe.
${ }^{7}$ PCA can, and has been, derived without any reference to probabilities (Jolliffe 1986). Indeed, one of its earliest derivations has relied on geometric insight (Pearson 1901). Interestingly, in the paper that first offers an algebraic derivation (Hotelling 1933), there is a geometric interpretation in terms of ellipsoids of constant probability.

Since we are coming to PCA from the point of view of redundancy reduction, the discussion of probabilities is central, and, therefore, we emphasize this aspect of PCA from the very beginning.
${ }^{8} \mathbf{R}$ assigns a value for each pair $(\mathbf{x}, \mathbf{y}) \in V^{2}$, so storing it takes at most $V^{2}$ values. Since $R(\mathbf{x}, \mathbf{y})=R(\mathbf{y}, \mathbf{x})$ (R is symmetric), we need to store only about half the values. For our favorite ensemble $V=60 \times 64=3840$, therefore $\mathcal{P}[\phi(x)]$ is parameterized with $7374,720 \approx 10^{7}$ values. The storage of so many values is quite within the reach of the modern researcher, as well as any organism of a moderate size, and we will come to the question of measuring them with some degree of statistical significance later in this thesis.
and elucidating one. ${ }^{9}$
An example $\phi^{t}(\mathbf{x})$ assigns a value at each point of the receptor grid $\{\mathbf{x}\}$; $\phi^{t}: V \mapsto \mathcal{R}$ is the measurement the sensory receptors make at "time" $t$. ${ }^{10}$ This is to say that $\phi^{i} \in \mathcal{R}^{V} \equiv U$, which we will think of as a $V$-dimensional linear vector space. Sometimes we will drop the index $t$ and will write just $\phi \in U$, with the understanding that this is the pattern of the readouts of the receptor grid at some fixed moment of "sampling time."

Given the ensemble $\left\{\phi^{t}(x), t=1, \cdots, T\right\}$, it is useful to understand the drawing of examples $t=1, \cdots, T$ from it as some linear operator

$$
\Phi: U \mapsto S
$$

where $S \equiv \mathcal{R}^{T}$ is a vector space which has as many dimensions as there are xamples drawn.

With $\hat{\mathbf{x}} \in U$ and $\hat{t} \in S$ being the basis vectors corresponding to the point x on the receptor grid and the drawing of the $t$-th example from the ensemble, respectively, we define the inner products on $U$ and $S$ to be

$$
\begin{aligned}
\left(\hat{\mathbf{x}}, \hat{\mathbf{x}}^{\prime}\right)_{V} & \equiv V \delta_{\mathbf{x}, \mathbf{x}^{\prime}} \\
\left\langle\hat{t}, \hat{t}^{\prime}\right\rangle_{S} & \equiv T \delta_{t, t^{\prime}}
\end{aligned}
$$

and therefore the identity operators are

$$
\begin{aligned}
\mathbf{1}_{U} & =\frac{1}{V} \sum_{\mathbf{x}} \hat{\mathbf{x}}(\hat{\mathbf{x}},)_{U} \\
\mathbf{1}_{S} & =\frac{1}{T} \sum_{t} \hat{t}\left\langle\hat{t}_{,}\right\rangle_{S} .
\end{aligned}
$$

We will drop the subscript specifying which space we are in whenever the context makes this clear.

We proceed to look into the meaning of the so-defined inner products. With (2.5), $\phi \equiv \mathbf{1}_{y} \phi=\frac{1}{V} \sum_{x} \hat{\mathbf{x}}(\hat{\mathbf{x}}, \phi)$. We identify ( $\hat{\mathbf{x}}, \phi$ ) with the measurement, or the readout of the receptor value at the grid point $\mathbf{x}$ for the given

[^5]sensory stimulus $\phi$, which we previously denoted with $\phi(\mathbf{x})$. Therefore,
$$
\phi=\frac{1}{V} \sum_{\mathbf{x}} \hat{\mathbf{x}} \phi(\mathbf{x}) \in U
$$
and analogously,
$$
\mathrm{s}=\frac{1}{T} \sum_{t} \hat{t} s(t) \in S .
$$
With the inner products (2.4), and the coordinate expansions (2.6) and (2.7), we define the Euclidean lengths in $U$ and $S$, respectively
$$
\begin{aligned}
\|\phi\|_{U}^{2} & =(\phi, \phi)=\frac{1}{V} \sum_{\mathbf{x}} \phi(\mathbf{x}) \phi(\mathbf{x}) \\
\|\mathbf{s}\|_{S}^{2} & =\langle\mathbf{s}, \mathbf{s}\rangle=\frac{1}{T} \sum_{t} s(t) s(t)
\end{aligned}
$$
The length $\|\phi\|_{U}^{2}$ is sometimes called the signal power of $\phi \in U$.
The inner product on $U$
$$
\left(\phi, \phi^{\prime}\right)=\frac{1}{V} \sum_{\mathbf{x}} \phi(\mathbf{x}) \phi^{\prime}(\mathbf{x})
$$
can be identified with the unnormalized correlator of the two stimuli $\phi$ and $\phi^{\prime} .{ }^{11}$

In order to understand what the inner product on $S$ means, let us consider $\langle\mathbf{s}, \Phi \mathbf{u}\rangle$ with $\Phi$ from (2.3). For a fixed $\mathbf{s}=\mathbf{s}_{\mathbf{0}}$, this is a linear functional on $U$ - to each vector $\mathbf{u} \in U$ it assigns the value $\left\langle\mathbf{s}_{\mathbf{0}}, \Phi \mathbf{u}\right\rangle$. Therefore, there exists some $\mathbf{v}=\Phi^{*}(\mathbf{s}) \in U$, such that $\langle\mathbf{s}, \Phi \mathbf{u}\rangle=(\mathbf{v}, \mathbf{u})$. We note that $\langle\mathbf{s}, \Phi \mathbf{u}\rangle$ is linear in s also, hence $\Phi^{*}(\mathrm{~s})$ is a linear operator $\Phi^{*}: S \mapsto U$ such that

$$
\langle\mathbf{s}, \Phi \mathbf{u}\rangle=\left(\Phi^{*} \mathbf{s}, \mathbf{u}\right) .
$$

Hence, $\Phi^{*}$ is the adjoint of $\Phi$. ${ }^{12}$ Thus, we understand the drawing of examples from our ensemble as the operator $\Phi: U \mapsto S$ such that

$$
\langle\hat{t}, \Phi \hat{\mathbf{x}}\rangle=\left(\Phi^{*} \hat{t}, \hat{\mathbf{x}}\right) \equiv \phi^{t}(\mathbf{x}) .
$$

With this definition of $\Phi(2.12), \Phi \hat{\mathbf{x}} \equiv \mathbf{1}_{s} \Phi \hat{\mathbf{x}}=\frac{1}{T} \sum_{t} \hat{t}(\hat{t}, \Phi \hat{\mathbf{x}})$, and, finally

$$
\Phi \hat{\mathbf{x}}=\frac{1}{T} \sum_{t} \hat{t} \phi^{t}(\mathbf{x}) .
$$

[^6]further assumes what the probability of "unknown" examples is-for any $\mathrm{s} \in S$, PCA postulates that ${ }^{15}$
$$
\mathcal{P}\left[\Phi^{*} \mathbf{s}\right] \propto \exp \left\{-\frac{1}{2}\|\mathbf{s}\|_{S}^{2}\right\}
$$
is a normal distribution whose parameter is the length of the vector $\mathrm{s} \in S$.
The main assumption of PCA (2.16) lets us calculate the probability density around any $\phi \in U$ that we know how to decompose into a linear combination of the reference examples $\Phi^{*} s=\phi$. It would be of interest to be able to to find a general way, given an example $\phi \in U$, to find its respective decomposition $\mathbf{s}(\phi) \in S$, so that we can use (2.16) to calculate $\mathcal{P}[\phi]$. Therefore, we are looking for an "inverse" operator ${ }^{16}$
$$
\Phi^{*+}: U \mapsto S
$$
with the reasonable requirement that if the example $\phi$ was constructed as the linear combination $\phi=\Phi^{*} s$, then using the "inverse" we can get to s again: $\Phi^{*+} \Phi^{*} \mathbf{s}=\mathbf{s}$.

Nevertheless, there are situations in which that is impossible-it might happen that the same example $\phi \in U$ may be represented as many different linear combinations of reference examples $\mathrm{s} \in S .{ }^{17}$ In such situations, $\Phi^{*}$ necessary looses the information about which, exactly, s of the many possible ones we came from, so $\Phi^{*+}$ can give us only one of them, which we hope to be somehow "the best." ${ }^{18}$ Therefore, we need to relax our initial requirement and adopt the weaker one:

$$
\Phi^{*} \Phi^{*+} \Phi^{*} \mathrm{~s}=\Phi^{*} \mathrm{~s} .
$$

We might also hope for another reasonable property of $\Phi^{*+}$ once it produces the linear combination $\mathbf{s}=\Phi^{*} \phi$, we can get back to $\phi$ with $\Phi^{*} \mathbf{s}=$ $\Phi^{*} \Phi^{*+} \phi=\phi$. There are situations when that might fail too given the sampling $\Phi, \Phi^{*}$ can only construct examples that are linear combinations of the
${ }^{15}$ We should note that (2.16) is true only when $T \leq V$. The universally correct statement is given in footnote 18 on page 15.
${ }^{16} \Phi^{*+}$ is also called the generalized Penrose inverse of $\Phi^{*}$.
${ }^{17}$ This will always happen if we make a sampling experiment long enough, so that the number of reference examples is bigger than the number of receptors they activate, $T>V$. For our favorite ensemble, $V=3840$, and for the various ways we decided to form $\Phi$, $T \in[16,3098]$. On the other hand, the pictures on the California driving licenses are scanned and stored electronically; for this database, $T>20,000,000$.

We can safely assume that $T>V$ also happens during the normal lifetime of an organism. ${ }^{18}$ This is again a fortunate fact for PCA; as we collect more and more statistics about our ensemble ( $T$ grows), bigger and bigger regions around the reference examples, $\Phi^{*} t$, closer and closer to them, have the chance of being mapped closer to their "best" places in $S$ by $\Phi^{*+}$.

Also, when $T>V$, even the reference examples get mapped back in $S$ not to the basis vectors, but closer to their "best" places; then, $\Phi^{*+} \Phi^{*} \hat{t} \neq \hat{t}$. This is good, because the length of their representation more truly reflects their actual probabilities. Of course, this implies that (2.16) needs a correction in this case; we derive it from (2.20): $\mathcal{P}\left[\Phi^{*} s\right] \propto \exp \left\{-\frac{1}{2}\left\|\Phi^{*+} \Phi^{*} s\right\|_{S}^{2}\right\}$.
adjoint to each other (footnote 12 on page 13) and consider that

$$
\left(\mathbf{u}^{\prime}, \Phi^{*} \Phi \mathbf{u}\right)=\left\langle\Phi \mathbf{u}^{\prime}, \Phi \mathbf{u}\right\rangle=\left(\Phi^{*} \Phi \mathbf{u}^{\prime}, \mathbf{u}\right) .
$$

Therefore, the adjoint of $\Phi^{*} \Phi$ is $\Phi^{*} \Phi$ itself- $\Phi^{*} \Phi$ is self-adjoint (symmetric). In particular,

$$
\left(\mathbf{u}, \Phi^{*} \Phi \mathbf{u}\right)=\langle\Phi \mathbf{u}, \Phi \mathbf{u}\rangle=\|\Phi \mathbf{u}\|_{S}^{2}
$$

and $\Phi^{*} \Phi \mathbf{u}=0 \Rightarrow\|\Phi \mathbf{u}\|_{S}^{2}=0 \Rightarrow \Phi \mathbf{u}=0$, hence $\operatorname{ker} \Phi^{*} \Phi \subset \operatorname{ker} \Phi$. Conversely, $\Phi \mathbf{u}=0 \Rightarrow \Phi^{*} \Phi \mathbf{u}=\Phi^{*} 0=0$, hence $\operatorname{ker} \Phi \subset \operatorname{ker} \Phi^{*} \Phi$. Therefore,

$$
\operatorname{ker} \Phi^{*} \Phi=\operatorname{ker} \Phi .
$$

Thus, $\Phi^{*} \Phi$ and $\Phi$ have identical null spaces. ${ }^{20}$ Therefore, if we find a basis for the null space of $\Phi^{*} \Phi$, it will also serve for the null space of $\Phi$.

Since $\Phi^{*} \Phi$ is symmetric, we can find (Lang 1984) a complete orthonormal basis of eigenvectors $\left\{\psi_{\sigma}\right\}$ with a non-negative spectrum $\left\{\sigma^{2} \geq 0\right\}$

$$
\Phi^{*} \Phi \psi_{\sigma} \equiv \mathbf{R} \psi_{\sigma}=\sigma^{2} \psi_{\sigma} \text { with }\left(\psi_{\sigma}, \psi_{\sigma^{\prime}}\right)=\delta_{\sigma, \sigma^{\prime}}
$$

which forms a complete spectral decomposion of $\mathbf{R}$ :

$$
\mathbf{R}=\sum_{\sigma} \sigma^{2} \psi_{\sigma}\left(\psi_{\sigma},\right)
$$

From (2.25) we see that the eigenvectors with vanishing eigenvalues, $\left\{\psi_{a} \mid \sigma=0\right\}$, form a basis for $\operatorname{ker} \Phi^{*} \Phi$ and, therefore, for $\operatorname{ker} \Phi$ the part that cannot be reached by constructing linear combinations of reference examples; the rest, $\left\{\psi_{\sigma} \mid \sigma>0\right\}$, form a basis for the part that can, range $\left(\Phi^{*}\right)$. It will be useful to define the projection operator $\mathbf{P}=\mathbf{P}_{\left.\text {rauge( } \Phi^{*}\right)}=\mathbf{P}_{(\text {ker } \Phi)^{\perp}}$ :

$$
\mathbf{P}=\sum_{\sigma>0} \psi_{\sigma}\left(\psi_{\sigma},\right) .
$$

It is also useful to rewrite the eigen decomposition of $\mathbf{R}$ (2.25):

$$
\mathbf{R}=\mathbf{R} \cdot \mathbf{P}=\sum_{\sigma>0} \sigma^{2} \psi_{\sigma}\left(\psi_{\sigma},\right) .
$$

Having found a basis for the domain of $\Phi(\operatorname{ker} \Phi)^{\perp} \in U$, we proceed to define a basis for $\operatorname{range}(\Phi) \in S$. For all $\sigma>0$ we can define

$$
\sigma \mathbf{s}_{\sigma} \equiv \Phi \psi_{\sigma}
$$

to be the (normalized) action of $\Phi$ on its eigenvectors, therefore $\operatorname{range}(\Phi)=$ $\left\{\mathbf{s}_{\sigma}\right\}$. With this definition, $\sigma \sigma^{\prime}\left(\mathbf{s}_{\sigma}, \mathbf{s}_{\sigma^{\prime}}\right\rangle=\left\langle\Phi \psi_{\sigma}, \Phi \psi_{\sigma^{\prime}}\right\rangle=\left(\psi_{\sigma}, \Phi \Phi^{*} \psi_{\sigma^{\prime}}\right)=$ $\sigma^{2} \delta_{\sigma_{x} \sigma^{\prime}}$; therefore

$$
\left\langle\mathrm{s}_{\sigma}, \mathrm{s}_{\sigma^{\prime}}\right\rangle=\delta_{\sigma, \sigma^{\prime}}
$$

${ }^{20}$ In this case the null space of $\Phi$ is exactly that part of $U$ which could not be constructed as a linear combination of the reference examples (see the discussion on page 15).

## 17

and $\left\{\mathrm{s}_{\sigma}\right\}$ is an orthonormal basis of $\operatorname{range}(\Phi)$. Then

$$
\Phi=\Phi \mathbf{P}=\Phi \sum_{\sigma>0} \psi_{\sigma}\left(\psi_{\sigma},\right)=\sum_{\sigma>0} \sigma \mathbf{s}_{\sigma}\left(\psi_{\sigma},\right) .
$$

From the fact that $\Phi^{*}$ is the adjoint of $\Phi$ (2.11), we can see that

$$
\Phi^{*}=\sum_{\sigma>0} \sigma \psi_{\sigma}\left\langle\mathbf{s}_{\sigma},\right\rangle .
$$

We also maintain that the "inverse" operator $\Phi^{*+}$ is given by:

$$
\Phi^{*+}=\sum_{\sigma>0} \sigma^{-1} \mathbf{s}_{\sigma}\left(\psi_{\sigma},\right) .
$$

Indeed, let us construct the "round-trip" operator $\Phi^{*+} \Phi^{*}\left(S \xrightarrow{\Phi^{*}} U \xrightarrow{\Phi^{*+}} S\right)$ and use the spectral decomposition of $\Phi^{*}$ (2.31) and $\Phi^{*+}$ (2.32) to calculate it:

$$
\Phi^{*+} \Phi^{*}=\mathbf{P}_{\mathrm{range}(\Phi)}=\mathbf{P}^{\prime}=\sum_{\sigma>0} \mathbf{s}_{\sigma}\left\langle\mathbf{s}_{\sigma},\right\rangle .
$$

It can be seen that this is the projector to $\operatorname{range}(\Phi)$, which is also $\operatorname{range}\left(\Phi^{*+}\right)$. We will call it $\mathbf{P}^{\prime}: S \mapsto S$ to distinguish it from $\mathbf{P}: U \mapsto U(2.26)$, which happens to be the other "round-trip" operator $\Phi^{*} \Phi^{*+}\left(U^{\Phi^{* *}} S \xrightarrow{\Phi^{*}} U\right)$

$$
\Phi^{*} \Phi^{*+}=\mathbf{P}_{\text {range }}\left(\Phi^{*}\right)=\mathbf{P}=\sum_{\sigma>0} \psi_{\sigma}\left(\psi_{\sigma},\right) .
$$

By plugging in (2.31) and (2.32) into (2.18-2.19) we verify that the initial requirements on $\Phi^{*+}$ are satisfied.

Using $\mathbf{P}^{\prime}(2.33)$, we can also rewrite the PCA probability (2.16) of linear combinations $s \in S$ of reference examples:

$$
\mathcal{P}\left[\Phi^{*} \mathbf{s}\right] \propto \exp \left\{-\frac{1}{2}\left\|\mathbf{P}^{\prime} \mathbf{s}\right\|_{S}^{2}\right\} .
$$

Notably, the parameter of the probability density around the linear combination $\Phi$ * $s$ is not the length of $s$ itself, but of its projection to the eigenspace of the ensemble. ${ }^{21}$

With the construction of $\mathbf{P}^{\prime}$ (2.33), there is an explicit expression of the length of the projection:

$$
\left\|\mathbf{P}^{\prime} \mathbf{s}\right\|_{S}^{2}=\left\langle\mathbf{P}^{\prime} \mathbf{s}, \mathbf{P}^{\prime} \mathbf{s}\right\rangle=\sum_{\sigma>0}\left(\mathbf{s}_{\sigma}, \mathbf{s}\right)^{2} .
$$

[^7]With this, the, somewhat arbitrary, reference, through $\{\hat{t}\}$, to the way the sampling experiment is conducted, which is evident in (2.9), is circumvented. Also, the dimensionality of the factorial representation for the probability (2.35) is equal to the dimensionality of the eigenspace of the ensemble $\Phi$, which is bounded from above by the volume of the system $V$.

It is useful to study the projection of an example $\Phi^{*} \hat{t} \in U$ to its "best" place $\mathbf{P}^{\prime} \hat{t} \in S^{22}$

$$
\mathbf{P}^{\prime} \hat{t}=\sum_{\sigma>0} \mathbf{s}_{\sigma}\left\langle\mathbf{s}_{\sigma}, \hat{t}\right\rangle \equiv \sum_{\sigma>0} a_{\sigma}^{i} \mathbf{s}_{\sigma}
$$

and its length

$$
\left\|\mathbf{P}^{\prime} \hat{t}\right\|_{S}^{2}=\left\langle\mathbf{P}^{\prime} \hat{t}, \mathbf{P}^{\prime} \hat{t}\right\rangle=\sum_{\sigma>0}\left\langle\mathbf{s}_{\sigma}, \hat{t}\right\rangle^{2}=\sum_{\sigma>0} u_{\sigma}^{t^{2}} .
$$

We see that the PCA coefficients $a_{\sigma}^{t}$ are directly related to the probability of observing a given receptor activation pattern, and that this probability factorizes to a product of the probabilities of observing individual PCA coefficients.

The PCA coefficients $a_{\sigma}^{t}$ also figure in the representation of the example in the physical space-for any $\hat{t}, \phi^{t}=\Phi^{*} \hat{t}=\Phi^{*} \mathbf{P}^{\prime} \hat{t}=\sum_{\sigma>0} a_{\sigma}^{t} \Phi^{*} \mathbf{s}_{\sigma}=\sum_{\sigma>0} \sigma a_{\sigma}^{t} \psi_{\sigma}$, and finally,

$$
\phi^{t}=\sum_{\sigma>0} \sigma a_{\sigma}^{t} \psi_{\sigma} .
$$

Also, they participate in the expression for the length of $\phi^{t}$, which is sometimes called the signal power, and is given (2.8) by:

$$
\left(\phi^{t}, \phi^{t}\right)=\sum_{\sigma>0} \sigma^{2} a_{\sigma}^{t^{2}} .
$$

Using the identity $1 s(2.5)$, we can study the evolution in "sampling time" of the measurements in the physical space $\psi_{\sigma}$ : $\Phi \psi_{\sigma}=\sigma \mathrm{s}_{\sigma}=\sigma \mathbf{1}_{S} \mathbf{s}_{\sigma}=\frac{1}{T} \sum_{t} \hat{t}\left\langle\hat{t}, \sigma \mathrm{~s}_{\sigma}\right\rangle=$ $\frac{1}{T} \sum_{t} \sigma a_{v}^{t} \hat{t}$. Hence, $\left\{\sigma \mathrm{s}_{\sigma}\right\}$ are the evolutions of the measurements $\left\{\psi_{\sigma}\right\}$. For their correlations, on one hand

$$
\left(\psi_{\sigma}, \mathbf{R} \psi_{\sigma^{\prime}}\right)=\left\langle\Phi \psi_{\sigma}, \Phi \psi_{\sigma^{\prime}}\right\rangle=\sigma \sigma^{\prime} \frac{1}{T} \sum_{t} a_{\sigma}^{t} a_{\sigma^{\prime}}^{t}
$$

and, on the other hand, $\left(\psi_{\sigma}, \mathbf{R} \psi_{a^{\prime}}\right)=\sigma^{2} \delta_{\sigma, \sigma^{\prime}}$ (2.24), so finally, for the correlation of the PCA coefficients,

$$
\left\langle\Phi \psi_{\sigma}, \Phi \psi_{\sigma^{\prime}}\right\rangle=\sigma \sigma^{\prime} \frac{1}{T} \sum_{t} a_{\sigma}^{t} a_{\sigma^{\prime}}^{t}=\sigma^{2} \delta_{\sigma_{1} \sigma^{\prime}}
$$

${ }^{22}$ The coefficients $a_{\sigma}^{t} \equiv\left(\mathbf{s}_{\sigma}, \hat{t}\right)$ can be viewed either as the projections of the examples to the eigenbasis, or as the expression of the eigenvectors as linear combinations of the reference examples: $\mathbf{s}_{\sigma}=\mathbf{1}_{S} \mathbf{s}_{\sigma}=\frac{1}{T} \sum_{t} \hat{t}\left\{\hat{t}, \mathbf{s}_{\sigma}\right\rangle=\frac{1}{T} \sum_{t} a_{\sigma}^{t} \hat{t}$, from which $\psi_{\sigma}=\sigma^{-1} \Phi^{\prime \prime} \mathbf{s}_{\sigma}=$ $\frac{1}{T} \sum_{t} a_{\sigma}^{i} \Phi^{*} \hat{i}=\frac{1}{T} \sum_{t} a_{\sigma}^{t} \phi^{t}$. This fact is very useful when $T<V$, and the eigen analysis is carried out more easily in $S$, by the snapshot method (Sirovich 1987).

This is one of the useful properties of PCA-instead of working directly with the receptor readouts $\Phi \dot{\mathrm{x}}$, which are correlated (2.14), PCA follows $\Phi \psi_{\sigma}$, whose coefficients $a_{\sigma}^{t}$ are decorrelated. Also, from (2.35) and (2.38), the probability of $\phi^{t}$ factorizes into individual probabilities

$$
\mathcal{P}\left[\phi^{t}\right]=\mathcal{P}\left[\mathbf{P}^{\prime} \hat{t}\right]=\prod_{\sigma>0} \mathcal{P}\left[a_{\sigma}^{t}\right] .
$$

So far, we have shown that the eigenbasis of $\Phi$ (2.24) is directly related to the factorization properties of PCA. We have also shown that the dimensionality of the PCA representation is bounded from above by both $T$ and $V$. We proceed to show how PCA can be used to further reduce the dimensionality. For this, let us arrange the spectrum $\{\sigma\}$ in non-increasing order $\left\{\sigma_{r}\right\},^{23}$ such that $r>r^{\prime} \Rightarrow \sigma_{r} \leq \sigma_{r^{\prime}}$, and let us use $r$ to label the bases $\psi_{r} \equiv \psi_{\sigma_{r}}$ and $z_{r} \equiv \mathbf{s}_{\sigma \rho}$. Then, for the ensemble $\Phi$, its correlation matrix $\mathbf{R} \equiv \Phi^{*} \Phi_{1}$, and the average signal power $\operatorname{trR}$ (footnote 13 on page 14), we have

$$
\begin{aligned}
\Phi & =\sum_{r} \sigma_{r} \mathbf{s}_{r}\left(\psi_{r},\right) \\
\Phi^{*} \Phi=\mathbf{R} & =\sum_{r}^{r} \sigma_{r}^{2}\left(\psi_{r},\right) \\
\operatorname{tr} \mathbf{R} & =\sum_{r}^{r} \sigma_{r}^{2} .
\end{aligned}
$$

PCA reduces the dimensionality of the original ensemble $\Phi$ by truncation of these expansions to only a small number of terms $N$, thereby defining a modified ensemble $\Phi_{N}$

$$
\begin{aligned}
\Phi_{N} & =\sum_{r=1}^{N} \sigma_{r} \mathbf{s}_{r}\left(\psi_{r},\right) \\
\left(\Phi_{N}\right)^{*} \Phi_{N}=\mathbf{R}_{N} & =\sum_{r=1}^{N} \sigma_{r}{ }^{2}\left(\psi_{r},\right) \\
\operatorname{tr} \mathbf{R}_{N} & =\sum_{r=1}^{N} \sigma_{r}{ }^{2} .
\end{aligned}
$$

The motivation here is that when the "important" quantity is the fidelity of the representation $\frac{\operatorname{tr} \mathrm{R}_{N}}{\operatorname{tr} \mathrm{R}} \in[0,1]$, it can be shown that the truncation (2.45) is optimal with respect to fidelity among the restrictions of R on all possible $N$-dimensional subspaces of $U$.

We defined $\Phi$ in terms of the random drawing of examples from an underlying ensemble with a probability density $\mathcal{P}[\phi(\mathbf{x})]$. Necessarily, the exact outcomes of the random drawings figure prominently in the constitution of $\Phi$. The projection to the eigen subspace, or to the first $N$ dimensions of it, somewhat mitigates the effect of this randomness. PCA becomes accurate for a long

[^8] enough sampling experiment (for a "high enough" ratio of $T / N$ ) the modified ensemble $\Phi_{N}$ (2.45) adequately describes the probability density via
$$
\left(\Phi_{N}\right)^{*+}=\sum_{r=1}^{N} \sigma_{r}^{-1} \mathbf{s}_{r}\left(\psi_{r},\right)
$$

For any receptor activation pattern $\phi$, PCA defines the set of coefficients

$$
a_{r}(\phi) \equiv \sigma_{r}^{-1}\left(\psi_{r}, \phi\right)
$$

such that

$$
\left(\Phi_{N}\right)^{*+} \phi=\sum_{r=1}^{N} \sigma_{r}^{-1} \mathbf{s}_{r}\left(\psi_{r}, \phi\right)=\sum_{r=1}^{N} a_{r} \mathbf{s}_{r} .
$$

Then its PCA probability (2.20) is

$$
\mathcal{P}[\phi] \propto \exp \left\{-\frac{1}{2} \sum_{r=1}^{N} a_{r}^{2}\right\} \propto \prod_{r=1}^{N} \exp \left\{-\frac{1}{2} a_{r}^{2}\right\}
$$

its PCA reconstruction is

$$
\phi_{N}^{\mathrm{rec}}=\left(\Phi_{N}\right)^{*}\left(\Phi_{N}\right)^{*+} \phi=\mathbf{P}_{N} \phi=\sum_{r=1}^{N} a_{r} \sigma_{r} \psi_{r}
$$

the residual error is

$$
\phi^{e r \tau} \equiv \phi-\phi^{r e c}=\left(1-\mathbf{P}_{N}\right) \phi
$$

the reconstructed signal power is

$$
\left\|\phi_{N}^{r e c}\right\|_{U}^{2}=\left(\phi_{N}^{r e c}, \phi_{N}^{r e c}\right)=\sum_{r=1}^{N} \sigma^{2} a_{r}^{2}
$$

and the Signal to Noise Ratio (SNR) of the reconstruction in octaves, is $-\log _{2} \frac{\left\|\phi^{\text {err }}\right\|^{2}}{\|\phi\|^{2}} .{ }^{24}$
To summarize, when the assumptions of PCA are met, it is a factorial representation of dimensionality $N$, that optimally preserves the signal power fidelity of the reconstruction.
${ }^{24}$ To get the value in Bells, one multiplies by $\log _{10} 2 \approx 0.301$, and by another 10-to get it in [dB].

## Chapter 3

Principal Component Analysis for Face Recognition

PCA has received much attention and usage as a general method for describing, storing, and analyzing statistical data (for a list of applications see Jolliffe 1986).

The application of PCA to human faces was pioneered by Sirovich and Kirby (1987) who applied it to a region including the eyes and the nose of 115 subjects. It was later revisited (Kirby and Sirovich 1990) by applying it to whole-face pictures of about 100 subjects.

On the basis of all these experiments, it has been hypothesized that the (properly defined) ensemble of pictures of human faces spans some low-dimensional subspace of the receptor activation space.

The application of PCA to surfaces of human heads in 3 dimensions was pioneered by Atick et al. (1996b) who applied it to the problem of extracting 3D shape information about human heads from the shading of photographic images of them shape-from-shading (Atick et al. 1996a).

It has been shown in (Sirovich and Kirby 1987; Atick et al. 1996b) and confirmed later (Penev and Atick 1996) that the PCA representations (2.47-2.52) of human faces and heads generalize well: given a certain fidelity tolerance, only a small number of modes $N<T \ll V$ is needed to represent out-ofsample examples. It has also been shown (Penev and Atick 1996) that PCA has the property of object constancy in the sense that it suppresses input noise (see Fig. A.11).

On the basis of the original hypothesis of low-dimensionality of the ensemble of human faces, Turk and Pentland (1991) proposed that PCA be utilized to find low-dimensional measures that are useful for the recognition of the identity of human subjects; the number of dimensions in the determination of the eigenbasis, $N$, was set as low as 16.

More systematic studies of the application of PCA to face recognition have been carried out lately, along with other linear holistic methods such as Lin-
ear Discriminant Analysis and Fisher Discriminant Analysis (Belhumeur 1996; Etemad et al. 1997; Belhumeur et al. 1997).

Nevertheless, a general, robust method for practical face recognition utilizing linear holistic methods has proven to be elusive. Indeed, the best method for human face recognition so far (Phillips et al. 1996; Rauss et al. 1996b; Rauss et al. 1996a) does not use an entirely holistic approach (Griffin 1996).

In this Chapter we will conduct a deeper study of this problem, which will reveal one of the main shortcomings of the PCA method. This will serve as a motivation in Chapter 4 to propose a new method-Local Feature Analysis (LFA) that has all the desirable properties of PCA, and at the same time explicitly reveals some symmetries not captured previously.

In Section 3.1, we will illustrate the theoretical ideas developed in Chapter 2, will introduce some new ones, and will try to develop some intuition of PCA. Along the way, we will probe the structure of the "face space" more deeply than before.

In Section 3.2.2, we will apply the Fisher Discriminant Method in an attempt to estimate the utility of the PCA representation for face recognition.

At the end, we will argue that a new method is needed to find representations suitable for face recognition.

### 3.1 PCA of Face Ensembles

In this Section we will illustrate the theoretical ideas outlined in Chapter 2 by studying the results of their application to various ensembles of images of human faces. We will start with small ensembles and will introduce bigger ones when circumstances warrant. Along the way, we will try to introduce new ideas and develop some intuition.

### 3.1.1 $T=15$

The first database we will use is a small, publicly available database the Yale Database (see Appendix A. 1 for definition)-developed for the purposes of face classification (Belhumeur 1996). ${ }^{1}$

Initially, we will analyze an ensemble which contains one image of every different person-their noglasses pose (Fig. A.1). ${ }^{2}$ Although this ensemble is very small $(T=15)$, one can gain a lot of insight by using it. Moreover, an ensemble of size $T=16$ (Appendix A.2) was used in the pioneering study of

[^9]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-09.jpg?height=708&width=870&top_left_y=196&top_left_x=1037)
Figure 3.1: PCA Analysis of the noglasses Ensemble $(T=15)$

The examples in the ensemble $\left\{\phi^{t}(\mathbf{x})\right\}_{t=1}^{15}$ (top) and its eigenmodes $\left\{\Psi_{r}(\mathbf{x}) \equiv\left(\hat{\mathbf{x}}, \psi_{r}\right)\right\}_{r=1}^{15}$ (bottom).
The arrangement is such that atop each eigenmode (apart from $\Psi_{1}$ ) is sitting the example which contributes most in the "snapshot method" of its construction $\left(\psi_{r}=\frac{1}{T} \sum_{t} a_{r}^{t} \phi^{t}\right)$. For some examples there were two eigenmodes to which they contributed most (for example, $\phi^{11}$ for $\Psi_{4}$ and $\Psi_{2}$ ). The second-most contributing example was chosen in those cases.
Also, the sign of the $r$-th eigenmode was chosen so that the coefficient $a_{r}^{t}$ for the $t$-th example atop it is positive. This is not a problem, since any multiple of an eigenvector is an eigenvector, and all "observables" in the $U$ space multiply by that factor twice.

23
the application of PCA to face recognition (Turk and Pentland 1991), so the noglasses ensemble can serve as a good reference point.

The noglasses Ensemble and its PCA analysis are shown on Fig. 3.1. By looking at the eigenmodes $\Psi_{r}(\mathbf{x})$, one can immediately see that this ensemble does not reveal too much about the structure of "face space." Namely, four observations can be made.

First, the mean face $\left(\Psi_{1}\right)$ is a relatively robust feature. Indeed, from a very small ensemble, a "face-like" picture emerges, that does not have any perceived identity. This can explain its utility for algorithms of finding the location of faces in unstructured scenes.

The second observation is that faces come with very different ratios of "head size" to inter-eye distance $\left(\Psi_{2}\right) .{ }^{3}$ This is not very surprising, but is nevertheless noteworthy. It has been a matter of debate what constitutes a properly normalized" face image. The locations of the eyes are used in this Thesis for two reasons. On one hand, they are firmly attached to the skull and are close to the nose, cheeks, and eyebrows, which cannot change very much within a single identity and, therefore, have been hypothesized to be useful for recognition. On the other hand, fast algorithms exist to find the eye locations robustly (Phillips et al. 1996; Griffin 1996). ${ }^{4}$

Third, the hair $\left(\Psi_{3}\right)$ is a strongly varying feature of faces. This is also intuitively correct and one can be satisfied that it shows up in the PCA calculation of such a small ensemble.

We note that only global features have been deduced by the application of PCA to this ensemble.

The fourth observation is an illustration of the in-sample effect that was discussed several times in Chapter 2. It can be seen that most of the eigenmodes have very strongly expressed individualities that can be easily traced down to the largest coefficient in their "snapshot expansion." Therefore, we are forced to conclude that, by far, most of the PCA results in this case have to do with the outcome of the random drawing from the probability density $\mathcal{P}[\phi(\mathbf{x})]$, rather than with $\mathcal{P}[\phi(\mathbf{x})]$ itself. In other words, the major part of the results are just a random fluctuation, i.e., an artifact.

The idea of the in-sample effect is illustrated in another way that we will use increasingly as we progress on Fig. 3.2. The top row shows the successive reconstructions $\phi_{N}^{\text {rec }}$ of an in-sample example with increasing dimensionality of

[^10]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-09.jpg?height=692&width=873&top_left_y=1435&top_left_x=1046)
Figure 3.2: Reconstruction with the noglasses Ensemble ( $T=15$ )

The successive reconstructions $\left\{\phi_{N}^{\text {rec }}\right\}_{N=1}^{T}$ for $\phi^{12}$ (see Fig. 3.1) are shown at the top. They are labeled with the Signal to Noise Ratio (SNR) of the reconstruction in octaves, i.e. $-\log _{2} \frac{\left\|\phi^{e v} \mathrm{r}\right\|^{2}}{\|\phi\|^{2}}$, where $\phi_{N}^{\text {err }} \equiv \phi-\phi_{N}^{\text {rec }}=\left(\mathbf{1}-\mathbf{P}_{N}\right) \phi$.
The successive reconstructions for an out-of-sample example (original) are shown at the bottom. The last digit of the SNR did not improve with $N>12$, so no reconstructions are shown past it.
The reconstruction with all PCA coefficients $\left(\phi^{\text {rec }}\right)$ is shown on rec. and the error ( $\phi^{\text {err }}$ ) is shown on error. Its contrast has been doubled to utilize better the grayscale dynamic range of the printed page. Note that a tripling of contrast would have been too much.
the ensemble $N$ according to (2.50). It is evident that after the first 3-4 modes, which contribute most, further increase in fidelity is slow.

Even at the relatively high SNR $\approx 6$ (this means that only $2^{-6} \approx 1.5 \%$ of the signal power is missing), there are still large perceptual differences-the "head size" is different, the "chin location" and the "expression" are different, and the "complexion" is different. Indeed, one can easily imagine, that a different person would correspond better to the perceptual appearance of the
$\mathrm{SNR}=6.14$ reconstruction. If the situation is so drastic with an in-sample example of an ensemble with controlled lighting and clear background, one can imagine that remarks about general ensembles and out-of-sample examples should be made very cautiously.

Notable also, the unmistakable identity of $\phi^{12}$ develops at $\mathrm{SNR} \approx 8$ and, incidentally, this is right after the contribution of its "personal" mode $\Psi_{13}$ (Fig. 3.1), so in this case one is tempted to attribute the perceptual development to the in-sample effect.

This simple exercise serves to illustrate the point, that "signal power" is not the perceptually relevant measure; the brain is concerned with something else. Indeed, the signals that impinge on the sensory periphery are a product not only of the conceptual description of the world in front of a sensory system, but are influenced by the physical means of the signal formation, transmission, and detection. Therefore, much of the signal power is due simply and invariably to the laws of Physics; it is redundant.

Notably, the individual modes' contribution to the signal power, the squared length in $U$, is determined by the spectrum $\left\{\sigma_{r}\right\}_{r=1}^{N}(2.52)$. A byproduct of the spectrum hierarchy the fidelity was guiding the dimensionality reduction of the ensemble (2.45).

Interestingly, the spectrum does not influence the squared length in $S$ (2.49), which we interpreted as $-\log \mathcal{P}[\phi]$, the information content of the sensory signal $\phi$. This is exactly the quantity Barlow (1961b) suggested should be proportional to the length of the optimal redundancy-reducing code. ${ }^{5}$

The out-of-sample reconstruction, shown on the bottom row of Fig. 3.2, further illustrates the ideas just discussed-after the first 3-4 terms in (2.50), only very small improvements in the SNR are achieved. This time, since there is no "personal" eigenmode, the SNR quickly asymptotes to its final value of $\sim 3.8$. There are two things to note. One is that the final SNR. for this out-ofsample example does not even reach the quality of the two-term reconstruction for $\phi^{12}$. This is again a manifestation of the in-sample effect.

Second, it is not surprising that the perceptual quality of the reconstruction with SNR $\approx 4$ of the identity of the person is not great-we had to go to $\mathrm{SNR} \approx 8$ to get good perceptual quality, and then, it could still be attributed to the in-sample effect. What is notable is that the reconstruction (Fig. 3.2rec.) contains virtually no identity information. Indeed, the face's identity is contained in full in the error (Fig. 3.2-error).

In the light of arguments outlined so far, one is tempted to generalize a bit and hypothesize that the overly optimistic application of PCA (or of any
${ }^{5}$ This is somewhat puzzling; if it is indeed the case that the length in $S$ is the perceptually relevant quantity, we should be looking for a hierarchy in $S$ on the basis of which to reduce dimensionality. Notably, all Principal Components in $S$ are equally "important" (2.49), and, suddenly, we no longer know how to reduce dimensionality. We will address this question later in the Thesis.

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-10.jpg?height=361&width=873&top_left_y=1439&top_left_x=112)
Figure 3.3: PCA Analysis of the full Yale Ensemble ( $T=87$ )

The first 16 eigenmodes $\left\{\Psi_{r}(\mathbf{x})\right\}_{r=1}^{16}$ of the full Yale ensemble.
For all 12 no-glasses subjects (shown on Fig. A.1) the following pose indices were excluded: glasses, sad, surprised, wink; the noglasses pose was included for all 15 subjects.
The name full refers to the physical volume $V=96 \times 120=11,520$, which is the dimensionality of the $U$ space.
other method, for that matter), may lead to pitfalls. In general, it is not clear that any insight into the structure of $\mathcal{P}[\phi(\mathbf{x})]$ is gained by a PCA experiment on "small" ensembles. A further illustration of this point can be found in Appendix A.2.

### 3.1.2 $T=87$

Having extracted more than initially expected from the analysis of the $T=15$ ensemble, we move to a bigger one-comprised of the images with no glasses and relatively "normal" expressions (Fig. 3.3).

It is evident that the eigenmodes are "smoother" and "less-personal," but still, the identity of the people in the ensemble is apparent in the eigenmodes.

Also notable is the development of $\Psi_{3}$, which is a "lighting" mode, coupled with some "head size" information. It was not observed before because all pictures in the earlier ensemble were with frontal lighting. This suggests that with larger ensembles symmetries will play a role in the analysis, and we will return to this point later.

One can ask the question how the quality of the out-of-sample reconstruction is influenced by the improved statistics of the ensemble. Fig. 3.4 compares the result from the noglasses ensemble with the current one. Indeed, the bigger ensemble has generalized better-the SNR of the reconstruction has improved; arguably, the perceptual quality of the reconstruction has improved, and the magnitude of the error has decreased. Nevertheless, it is evident, that

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-10.jpg?height=247&width=875&top_left_y=85&top_left_x=1033)
Figure 3.4: Reconstruction with the full Yale Ensemble ( $T=87$ )

The reconstructions with all PCA coefficients $\phi^{\text {rec }}$ and the residual errors $\phi^{\text {err }}$ of the example Fig. 3.2-original, shown also here on original in the context of the noglasses Ensemble (Fig. 3.1) and the current ensemble (Fig. 3.3) are shown on the left and right, respectively.
The reconstructions are labeled with theit respective SNRs, and the errors are shown at the same magnification of two.
most of the identity is still outside the eigenspace.
Motivated on one hand by the understanding that we need to increase the ratio $T / V$, and on the other hand remembering that the poor segmentation of the object from the background is a strong generator of artifacts (cf. Appendix A.2), we are lead to the idea of cropping the images closer around the face. ${ }^{6}$ In order to study this effect, we have chosen two closer croppings: one, which we will index with h3q below, is constructed by just chopping off the top of the hair, which is supposedly a source of intra-identity variability; the other, which we will index with third below, is a much closer cropping of the clothing around the neck and of some of the background on both sides.

The results are shown on Fig. 3.5. It can be seen that the "lighting" mode is now liberated from the coupling with the "head size" and, being purer, is stronger and has moved to $\Psi_{2}$ in both ensembles. Also, it is almost freed from any "personality" traces in the third ensemble.

The latter is also true for other modes we start to see the influence of individual reference examples being washed away, and general global face features emerging.

The reconstruction quality in the context of those two ensembles is shown
${ }^{8}$ Indeed, Sirovich and Kirby (1987) had obviously had this idea in mind in their pioneering study where they decrease $V$ by using only the eye and the nose region. In a later study (Kirby and Sirovich 1990) the area of the image has been increased, but also the size of the ensemble has been increased. Moreover, they have maintained control over the segmentation by asking subjects to mechanically adjust their heads in a fixed oval opening against a smooth background, and also they have controlled for facial hair and race. Using those techniques, SNR $\approx 9.5$ averaged over 10 out-of-sample examples has been reported, with $N=100$ and $T \approx 200$.

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-10.jpg?height=610&width=870&top_left_y=1430&top_left_x=1049)
Figure 3.5: PCA Analysis of the h3q and third Yale Ensembles ( $T=87$ ) The first 16 eigenmodes $\left\{\Psi_{r}(\mathbf{x})\right\}_{r=1}^{16}$ of the h3q (top) and third croppings of the Yale ensemble. See Fig. 3.3 for description of the images in the selection. The notation h3q refers to "height-3-quarters," i.e., $V=96 \times 90=8,640$, and third refers to "third" volume $V=64 \times 60=3,840$ the $U$ dimensionality of our favorite ensemble.

on Fig. 3.6. In comparison with the full cropping (Fig. $3.3 B$ ), the SNR for the h3q reconstruction is slightly smaller. This is mainly due to the exclusion of a relatively large area of uniformity background and hair which contribute a lot in the SNR measure. Arguably, the perceptual quality is slightly better, this time the shape of the ears is a bit better defined.

The most improvement is seen in the third cropping; SNR has gone up, the error magnitude has gone down, and the perceptual quality of identity reconstruction is markedly better. Still, there is a lot of identity information in $\phi^{e r r}$ which is not a big surprise, judging by the $\mathrm{SNR} \approx 5.7$.

While for smaller ensembles it was feasible to show the whole succession of the reconstruction $\phi_{N}^{\text {rec }}$ (Fig. 3.2), it is more convenient to trace the evolution of just SNR with $N$ for bigger ensembles. This is shown on Fig. 3.7.

It is evident that the out-of-sample and in-sample reconstructions have markedly different properties-the in-sample fidelity reaches much higher levels

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-11.jpg?height=388&width=530&top_left_y=96&top_left_x=272)
Figure 3.6: Reconstruction with the h3q and third Yale Ensembles ( $T=87$ ) The reconstructions with all PCA coefficients $\phi^{\text {rec }}$ and the residual errors $\phi^{\text {err }}$ in the context of the h3q (top) and third (bottom) Yale Ensembles (Fig. 3.5). The reconstructions are labeled with theit respective SNRs, and the errors are shown at the same magnification of two.

and, after a few beginning terms ${ }^{7}$ grows much faster than the out-of-sample. This is a manifestation of the in-sample effect.

It can also be seen that, for the out-of-sample case, after the first several terms in the reconstruction (2.50), relatively little SNR is gained for each additional term. Also, the discrepancy between the out-of-sample and in-sample SNR gains in this regime hints that most probably the eigenmodes at that point are somewhat arbitrary and tied to the particular way the random drawing from $\mathcal{P}[\phi(\mathbf{x})]$ was done, so it might be unwise to waste our "resources" on additional terms in (2.50).

Trying to understand better what is a "wise" allocation of "resources," we remember that SNR is not the perceptually relevant quantity. So far, we have only concerned ourselves with squares of projection lengths in $U$, namely, the signal power at the pixel level. In the context of PCA, we have another measure as our disposal-the square of the projection length in $S$ (2.49). It is the negative logarithm of the probability ( $-\log \mathcal{P}[\phi]$ ) of a given sensory stimulus $\phi$ its information content. This is the quantity that Barlow (1961b) proposed as the optimal length of the code for the sensory stimulus $\phi$ in the context of redundancy reduction.
${ }^{7}$ Interestingly, the contributions from $\Psi_{1}, \Psi_{3}$, and $\Psi_{4}$ are unexpectedly large for the outof-sample case. We would say that this example, Fig. 3.1-original, is described relatively well by those modes. Actually, in an ensemble with better statistics, Ensemble 1 (Fig. 3.9), the whole effect is concentrated in $\boldsymbol{\Psi}_{\mathbf{1}}$; we would say that $\boldsymbol{\Psi}_{1}$ of Ensemble 1 is a good description of this example.

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-11.jpg?height=599&width=813&top_left_y=1439&top_left_x=139)
Figure 3.7: SNR with the $T=87$ Yale Ensembles The SNR of the reconstruction for the out-of-sample examples (Fig. 3.4-A, B; Fig. 3.6) in the context of the $T=87$ Yale Ensembles as a function of the number of terms $N$ in (2.50) is shown with points. The average in-sample SNR, $\log _{2}(1-$ fidelity $)=\log _{2}\left(\frac{\text { trfl-trfu }}{\text { trf }}\right)$, is shown with lines.

We may, now, ask the question of how probable our reconstruction is in the context of a given ensemble, that is, in an "optimal" system, a sensory message of what length should code for it? An $S-U$ diagram depicting the dependence between the squared lengths of the projections in $S$ and $U$, respectively, as terms are added in (2.50)-is shown on Fig. 3.8 for the reconstruction in the out-of-sample case. ${ }^{8}$

The $S-U$ diagram has an interesting interpretation. On one axis is the squared length in $U$, the signal power (actually, the reconstruction error in the signal power). We have already developed some intuition of why we need good reconstruction of the signal power, and roughly how much we need for "perceptually good" reconstruction.

On the other axis is the squared length in $S$. On Fig. 3.8 we interpreted it as the "entropic cost" of the representation. In the context of Information Theory (Shannon and Weaver 1949), this is the information content of the

[^11]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-11.jpg?height=578&width=802&top_left_y=185&top_left_x=1067)
Figure 3.8: $S-U$ diagrams of reconstructions with the $T=87$ Yale Ensembles The SNR from Fig. 3.7 is plotted on the horizontal axis.
The average component length squared of the projection in $S$, $\langle S\rangle=\frac{1}{N}\left\|\left(\Phi_{N}\right)^{* \dagger} \phi\right\|_{S}^{2}$ (2.47 2.49) is plotted on the vertical axis. (The average squared length per component is shown instead of the total squared length for easy comparison with a horizontal line. When we deal with translation-invariant ensembles, this average will have a well-defined meaning.)
To illustrate the dependence on $N$, the first, and every tenth, reconstruction are marked with points.
The average length for the in-sample reconstruction is exactly one (2.42) and is shown with a line. Note that it extends to much higher SNRs than shown. Since the exponential of $\langle S\rangle$ is proportional to the probability of the reconstruction $\mathcal{P}[\phi] \propto \exp \left\{-\frac{1}{2}\langle S\rangle\right\},\langle S\rangle$ itself can be broadly labeled as the entropy of the reconstruction. Also, in the context of Information Theory, $-\log \mathcal{P}[\phi]$ is the information content in a given message, and is proportional to the length of the optimal code for that message.

33
sensory stimulus $\phi$. After proper normalization, ${ }^{9},\langle S\rangle$ is the optimal length of the sensory message in bits-the minimal "cost" to represent the sensory stimulus $\phi$.

It can be seen that in the context of the third ensemble, much of the SNR can be gotten relatively "cheaply"-20-40 terms with an average entropy of $\approx 0.3$. Thereafter, the differential gain in SNR with respect to both entropy per component and total entropy of the representation is much lower, i.e., the reconstruction is very improbable in the context of the given ensemble.

The $S-U$ diagram of a given reconstruction is a quantitative measure telling a sensory system when to stop adding more terms to (2.50) because the example is no longer consistent with its a priori expectation for the ensemble. This can happen for a variety of reasons. In the case shown on Fig. 3.8, this is most probably due to poor ensemble statistics, or the in-sample effect. Another reason could be that the example to be represented with (2.50) is noisy. In this case truncating the sum has the effect of noise suppression. ${ }^{10}$

### 3.1.3 $T=1038$

Having introduced and illustrated several theoretical ideas by the examination of small ensembles, we will proceed with the analysis of Ensemble $1(T=1038)$ (see Appendix A. 1 for definition). In light of its better $T / V$ ratio, we will consider only the third cropping $(V=3840)$ (Fig. 3.5).

The PCA analysis of Ensemble 1 is shown on Fig. 3.9. It is evident that there is no longer perceptual identity information in the strongest eigenmodes. ${ }^{11}$ Also, it is easy to identify some symmetries that PCA has explicitly captured $\Psi_{2}$ can be understood as a "background mode," i.e., adjusting $a_{2}$ would correspond to adjusting the differences in luminosity between the background and

[^12]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-12.jpg?height=439&width=873&top_left_y=98&top_left_x=103)
Figure 3.9: PCA Analysis of Ensemble $1(T=1038, V=3840)$

The first 16 eigenmodes $\left\{\Psi_{r}(\mathbf{x})\right\}_{\tau=1}^{16}$ of Ensemble 1 (top and middle) and several of the rest (bottom) (see Appendix A. 1 for definition).
This figure is reproduced on Plate 1A.
the face; $\Psi_{3}$ is a "lighting" mode; $\Psi_{4}$ and $\Psi_{5}$ correspond to variations in the background on both sides of the head.

More interesting are the "facial" modes that follow-various perceptually relevant regions are highlighted in different eigenmodes, some particularly strongly $\left(\Psi_{12}, \Psi_{19}, \Psi_{22}\right)$. There are several modes that "describe" eyebrows, and it could be argued that they are needed to span the variability of human eyebrows.

Interestingly, this cannot be said about the "mouth" modes. What happens on $\Psi_{50}$ is the subtraction of a mouth from one place of the face and the addition of a mouth to another, i.e., the location of the mouth is a relevant parameter. This is not surprising, because what stays fixed in Ensemble 1 is the location of the eyes it is easily understandable that eyebrows will have a hard time relocating very much, but mouths will have much more freedom, mainly driven by the small errors in the localization of the eyes, the natural skull size variability, as well as the limited expression variability in Ensemble 1. This is also well illustrated by $\Psi_{1}$-the region around the nose is very well defined and features gradually wash away as distance (and "facial flexibility") increases. ${ }^{12}$

[^13]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-12.jpg?height=196&width=870&top_left_y=94&top_left_x=1035)
Figure 3.10: Reconstruction with Ensemble $1(T=1038, V=3840)$

The reconstructions with all PCA coefficients $\phi^{\text {rec }}$ and the residual errors $\phi^{\text {err }}$ of the example shown on original in the context of the Yale ensemble (Fig. 3.3) and Ensemble 1 (Fig. 3.9) are shown on the left and right, respectively. The reconstructions are labeled with theit respective SNRs, and the errors are shown at the same magnification of two.
of faces is, indeed, lower than 1000.
By looking at the eigenmodes on Fig. 3.9, one is tempted to suggest that the crossover regime between true information about $\mathcal{P}[\phi(\mathbf{x})]$ and the in-sample effect happens somewhere between $N=100$ and $N=300$, and the cross-over between the in-sample effect and true receptor noise between $N=500$ and $N=1000 .{ }^{15}$

Having gotten insight from the eigen-pictures themselves, we briefly note that the reconstruction in the context of Ensemble 1 (Fig. 3.10) is good although the right eyebrow lacks some definition, and the teeth are not as sharp as on the original, overall, one can easily deduce the identity and the expression of the subject-for most practical purposes, there is enough identity and expression information in the eigen subspace.

Although the final recoustruction with $\mathrm{SNR} \approx 8.5$ is most probably satisfactory for many practical purposes, it would be interesting to study at what "cost" it is achieved by constructing the corresponding $S-U$ diagram (Fig. 3.11).

Four regimes are evident: there is rapid SNR gain up to $N \sim 70$ when $\mathrm{SNR} \approx 6$ is achieved at very low entropic cost; there is a gradual increase of the cost per component until $\mathrm{SNR} \approx 7, N \sim 170$; later, there is a plateau to $\mathrm{SNR} \approx 7.5, N \sim 350$, followed by a rapid, "exponential" growth in entropic cost at the end.

The $S-U$ diagram (Fig. 3.11) too supports the conclusion we reached from the eigenmodes (Fig. 3.9) there is somewhat of a distinct regime in the $N=$ 200 to $N=350$ range.

Obviously, it is unwise to keep terms in (2.50) much more than $N=300$ in the context of this ensemble. Although "unwise," we do not know yet whether

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-12.jpg?height=594&width=795&top_left_y=1435&top_left_x=1078)
Figure 3.11: $S-U$ diagram of a reconstruction with Ensemble 1 ( $T=1038$, $V=3840$ )
The SNR of the reconstrution of the example Fig. 3.10 -original is plotted on the horizontal axis, and the average entropy per component (cf. Fig. 3.8) is plotted on the vertical axis.
To illustrate the dependence on $N$, the curves are marked with points at regular intervals.
The first, and every 10-th reconstruction for $T=87$ (Fig. 3.8-third) are shown with crosses.
The first and every 50-th reconstruction for ( $T=1038, V=3840$ ) are shown with pluses and every 200 -th reconstruction is shown with squares.

it is "necessary" $\mathrm{SNR} \approx 8.5$ seems good, but is $\mathrm{SNR} \approx 7.5$ so? One way to try to answer this question, is to look again at the successive reconstructions $\phi_{N}^{r a x}$ and errors $\phi_{N}^{e r r}$ (Fig. 3.12).

Evidently, $\mathrm{SNR} \approx 6.5$ is perceptually inadequate; there is noticeable improvement between $\mathrm{SNR} \approx 7$ and $\mathrm{SNR} \approx 7.8$; and only the tiniest details develop all the way to $\mathrm{SNR} \approx 8.5$, notably the teeth and the right eyebrow. One can assume that for most purposes, $N \in[300,400]$ would be a reasonable reconstruction of this example.

It is interesting to note that, although weird-looking, the eigenmodes in the crossover regime are actually necessary for even moderate perceptual quality

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-13.jpg?height=283&width=873&top_left_y=101&top_left_x=101)
Figure 3.12: Successive reconstruction in the cross-over regime of Ensemble 1

The successive reconstructions $\phi_{N}^{\text {rec }}$ labeled with their SNR (top) and their respective residual errors $\phi_{N}^{\text {err }}$ (bottom) for Example 1 (Fig. 3.10-original). The first four errors are magnified $5 \times$ and the last $-20 \times$.
This figure is reproduced on Plate $1 B$.
of the reconstruction. The fact that the error in the regime of the "personal" modes $(N=500)$ contains some identity information is not surprising the in-sample effect is not valid for out-of-sample examples. Interestingly, there is still some identity information well into the pixel noise regime $(N=1000)$, which suggests that there is still interesting structure in $\mathcal{P}[\phi(\mathbf{x})]$ that is not captured by the Ensemble $1(T=1038, V=3840)$.

It would be useful to know whether there is some more straight-forward way of finding the generalization properties of an ensemble than looking at eigenmodes, $S-U$ diagrams and reconstructions, and judging them by eye. ${ }^{16}$

We hypothesize that this information is contained in the spectrum of an ensemble, shown on Fig. 3.13. Three regimes are evident an initial fast decrease of the signal power, a very long, almost linear regime in the middle, and a sharp drop at the end. ${ }^{17}$

Since the spectrum is showil on a logarithmic scale, the linear regime corresponds to an exponential decay in the signal power per mode. Also shown is the average residual power of the error, which is the sum of the signal power of all modes after the truncation point of (2.50). If the dependence of the spectrum on the mode number is exponential with a coefficient $-\alpha$, so would be its integral and they will be two parallel lines on this plot, which in this case is almost true. Also, the ratio of the signal power and its integral would be a constant, and we can see only modest deviations from this behavior.

It is interesting to understand what is happening in the beginning of the
${ }^{16} \mathrm{By}$ "generalization properties" we mean how much of the actual structure of $\mathcal{P}[\phi(\mathbf{x})]$ is captured by a given sampling experiment $\Phi$.
${ }^{17}$ We have to emphasize again (footnote 14 on page 36), that this is indeed due to the true spectrum of the ensemble and not to accumulation of computational errors.

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-13.jpg?height=599&width=804&top_left_y=1441&top_left_x=139)
Figure 3.13: $\log$ Spectrum of Ensemble $1(T=1038, V=3840)$

The ratio of the signal power in a given mode $\Psi_{N}$ to the total signal power $\log _{2} \frac{\sigma_{r}{ }^{2}}{\mathrm{tr} \mathrm{R}}$ is shown with a solid line. The ratio of the resudial signal power after truncation of (2.50) to the total signal power $\log _{2} \frac{\operatorname{tr} \mathrm{R}-\mathrm{tr} \mathrm{R}_{\mathrm{N}}}{\operatorname{trR}}=\log _{2}(1-$ fidelity) is shown with a dashed line, and the ratio of the mode signal power to residual signal power is shown with a dotted line.
spectrum and, therefore, it is shown on Fig. 3.14 with $N$ on a logarithmic scale.
Notably, the first regime in the spectrum is very close to a power law regime. This is interesting, since in the translation-invariant case, where arguably there are sufficient statistics, and lack of an in-sample effect, many groups have measured power law spectra. If this is the case, its integral would also be a power law with a different power, which seems to be close to the case. Also reinforcing this hypothesis is the ratio of the spectrum and its integral, which is expected also to behave as a power law and it does.

Is there any connection between the ability of the PCA analysis of a sampling experiment $\Phi$ to capture the underlying $\mathcal{P}[\phi(\mathbf{x})]$ of the ensemble and the spectrum of $\Phi \Phi^{*}$ ? We hypothesize that there is; namely, we propose that "genuine" information is captured in the power law regime, the in-sample effect is evident in the exponential regime, and there is a cross-over regime between them.

Indeed, by looking at Fig. 3.14 it is evident that $N=100$ definitely belongs

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-13.jpg?height=578&width=818&top_left_y=94&top_left_x=1065)
Figure 3.14: $\log -\log$ Spectrum of Ensemble $1(T=1038, V=3840)$
The same dependencies as in Fig. 3.13 are shown on a logarithmic scale for $N$.

to the power-law regime, and by looking at Fig. 3.13 it is evident that $N=400$ is definitely in the exponential regime.

Therefore, we propose an objective measure of the amount of information captured by a PCA experiment no genuine $\mathcal{P}[\phi(\mathbf{x})]$ information is contained after the exponential regime of the spectrum. Therefore, it is "unwise" to keep many more terms in (2.50), but at least the terms in the power law regime must be kept.

This suggestion may be a step towards an automatic Information-Theorydriven way to reduce the dimensionality of a given ensemble of sensory signals (see discussion in footnote 5 on page 27).

### 3.2 Face Recognition by PCA

Ever since Sirovich and Kirby (1987) constructed a low-dimensional representation of images of human faces, its use for the solution of pattern-recognition problems has been an attractive idea. In this Section, we will search for a facediscriminability measure that operates at the level of the PCA coefficients.

41

### 3.2.1 The Initial Hypothesis

Turk and Pentland (1991) were first to propose an application of PCA for face recognition by the following procedure. For a suitably defined ensemble of faces, perform the PCA analysis as outlined in Section 2.3 and choose a truncation point $N(2.45)$. Then, define $K$ classes of examples, each with a representative $\left\{\phi^{k}\right\}_{k \in K}$, whereby each class contains images of a single person, and calculate and store the respective projections to the PCA subspace $\left\{\mathbf{P}_{N} \phi^{k}\right\}_{k \in K}$. Subsequently, when a unknown out-of-sample face $\phi$ needs to be classified, calculate its projection to the PCA subspace $\mathbf{P}_{N} \phi$ and subtract it from each of the $K$ stored projections. For a forced-choice experiment, classify the new face to the class $k$, so that the reference projection $\mathbf{P}_{N} \phi^{k}$ that has the smallest distance

$$
\epsilon=\left\|\mathbf{P}_{N} \phi^{k}-\mathbf{P}_{N} \phi\right\|_{U}
$$

to the new projection $\mathbf{P}_{N} \phi(2.8)$, which is usually calculated using (2.52).
Unfortunately, this early study suffered from two drawbacks. One is that the sub-optimal definition of the input ensemble has resulted in the classification of the background, rather that the faces, which had been the initial goal (Appendix A.2).

More importantly, the proposed measure (3.1) is the (square root of the) signal power (2.8) of the projection (2.50) to the PCA subspace of $\phi^{k}-\phi$, the pixel-by-pixel difference between the example to be classified $\phi$ and a suitably chosen reference example $\phi^{k}$. The idea to measure the signal power of such differences, albeit without projecting them to a subspace, had been around for quite some time before that, and had been verified as not suitable for face recognition (Baron 1981). We will argue that even after projecting the difference to the PCA subspace, the signal power is equally unsuitable for classification.

In Chapter 2 we showed that relatively high SNR values are needed for perceptually adequate reconstruction $\mathbf{P}_{N} \phi$, necessarily achieved with relatively large numbers of terms $N$ in (2.50). Moreover, good perceptual quality was achieved typically with $\mathrm{SNR} \approx 7.5$ (see Fig. 3.12), which means that only $\sim 0.5 \%$ of the signal power could be safely discarded; by the time the identity information is contained in the PCA subspace, SNR is typically high, and $\mathbf{P}_{N} \phi$ already contains almost all of the signal power in $\phi$. Therefore, $\epsilon$ from (3.1) is virtually unchanged by the proposed projection. ${ }^{18}$

In general, while it is true that PCA reduces dimensionality-from $V \approx$ 4000 to $N \approx 400$ (Fig. 3.12), the pixel-level signal power does not change very much because PCA was designed with the goal to preserve precisely that. Obviously, other ways for utilizing the low dimensionality are needed. Before

[^14]we discuss some possibilities later, it is useful to define the experimental setup and develop some insight into the "identity" information contained in pictures of human faces.

### 3.2.2 In Search of a Discriminability Measure

For the study in this Section, we have used Ensemble 5 (see Appendix A. 1 for definition) which has the same cropping third as Ensemble 1, but is about three times larger $(T=3279, V=3840)$.

All examples in the ensemble have been marked as either with known identity, or with unknown. In the PCA analysis we have used all examples to improve the quality of our information about $\mathcal{P}[\phi(\mathbf{x})]$, but in the discrimination experiments only a restricted ensemble has been considered-of examples labeled with a known subject.

Every ordered pair of pictures in the restricted ensemble $(p, q) \in T \times T$ falls in one of three classes: one, if $q=p$, the pictures are identical; two, $q \neq p$ but the pictures are of the same subject; three, $q \neq p$ and the pictures are of different subjects. Finally,

$$
T \times T=\{(p, p)\}_{p \in T} \cup C_{\text {same }} \cup C_{\text {diff }} .
$$

The statistics of the ensemble is shown in Table 3.1.
With this definition, the face classification problem is, Find a procedure that, given a pair $(p, q)$, will produce markedly different results for the pairs in $C_{\text {same }}$ as opposed to those in $C_{\text {diff }}$.

If for every pair $(p, q)$ we take difference of the PCA representations of the examples ${ }^{19}$

$$
\mathrm{d}^{(p, q)}=\left(\Phi_{N}\right)^{*+} \phi^{p} \quad\left(\Phi_{N}\right)^{*+} \phi^{q} \in S
$$

then the solutions to the face classification problem can be parameterized with the measures $\mu\left(\mathrm{d}^{(p, q)}\right)$, from which we want to pick one that is somehow the "best."

One possibility is to search for a linear operator $\mathrm{W}: S \mapsto S$ which corresponds to the measure $\mu(\mathbf{d})=(\mathbf{W d}, \mathbf{W d})$. If such a W is found, then the ransformation Wd would send $\mathrm{d}^{(\mathrm{p}, \mathrm{g})}$ to the "eigen-identity" representation. Since here we want to explore the utility of the PCA representation itself, we will constrain our considerations to diagonal $\mathrm{W}^{*} \mathrm{~W}$ and parameterize the possible measures with its diagonal elements $\left\{w_{r}\right\}_{r=1}^{N}$ :

$$
\mu\left(\mathrm{d}^{(p, q)}\right)=\sum_{r=1}^{N} w_{r}\left(a_{r}^{p}-a_{r}^{q}\right)^{2}=\sum_{r=1}^{N} w_{r} D_{r}^{(p, q)} \equiv D^{(p, q)}
$$

with

$$
D_{r}^{(p, q)} \equiv\left(a_{r}^{p}-a_{r}^{q}\right)^{2} .
$$

${ }^{19}$ In this notation $\Phi^{*} \mathrm{~d}^{(p, q)} \in U$ and the measure (3.1) is $\varepsilon=\left\|\Phi^{*} \mathbf{d}^{(p, q)}\right\|_{U}$.

| 43 |  |  |  |
| :--- | :--- | :--- | :--- |
| $n$ | $s(n)$ | $\frac{n(n-1)}{2}$ | $s(n) \times \frac{n(n-1)}{2}$ |
| 1 | 26 | 0 | 0 |
| 2 | 769 | 1 | 769 |
| 3 | 145 | 3 | 435 |
| 4 | 143 | 6 | 858 |
| 5 | 12 | 10 | 120 |
| 6 | 17 | 15 | 255 |
| 7 | 8 | 21 | 168 |
| 8 | 3 | 28 | 84 |
| 9 | 2 | 36 | 72 |
| 10 | 3 | 45 | 135 |
| 11 | 16 | 55 | 880 |
| 12 | 1 | 67 | 67 |
|  |  |  | $N_{s}=3842$ |

Table 3.1: Statistics for the Face Classification Study ( $T_{\text {restricted }}=3049$ ) In the set of subjects $\{\alpha\}=A$, any subject $\alpha \in A$ is represented with a set of pictures in the ensemble $\alpha \subset T$; also all identities are known, $T=\bigcup_{A} \alpha$. The number of pictures for a given subject is the size of the set $\alpha, \mid \alpha$, and is also known.
The number of pairs $(p, q) \in C_{\text {same }}$ for a given subject $\alpha$ is $\frac{|\alpha| \times(\alpha \mid-1)}{2}$. The number of subjects that are represented with a given number of pictures $n$ is $s(n)=\left|\left\{\left.\alpha\right|_{|\alpha|=n}\right\}\right|$. Then, for the pairs $\left\{(p, q) \in C_{\text {same }}\right\}, N_{s}=\frac{1}{2}\left|C_{\text {same }}\right|=$ $\sum_{n} s(n) \times \frac{n(n-1)}{2}$ is the number of unordered pairs in $C_{\text {same }}$. Analogously, $N_{d}=$ 4,642,834 is the number of unordered pairs in $C_{\text {diff }}$.
It is worth noting that the statistics of $C_{s a m e}$ are not very satisfactory. In further studies, this parameter needs to be incorporated better in the design of the databases.

In this notation, the original proposal (3.1) is $w_{r}=\sigma_{\mathrm{r}}{ }^{2}$. In Section 3.2.1 we argued that it is not expected to work very well.

Another obvious candidate is $w_{r}=1$. There is no a priori reason for or against it, so we will keep it in mind as we proceed.

Another idea is to run some optimization procedure for $w_{r}$; the attractiveness of (3.4) lies in the fact that there are only a small number of coefficients to optimize for $N$.

Before we do this, it is interesting to look into the distributions of the differences of the individual PCA coefficients $D_{r}^{(p, q)}$ (3.5)

$$
\begin{aligned}
F_{r}^{\text {same }}(u) & =\mathcal{P}\left[D_{r}^{(p, q)} \leq u\right]_{(p, q) \in C_{\text {aame }}} \\
F_{r}^{\text {diff }}(u) & =\mathcal{P}\left[D_{r}^{(p, q)} \leq u\right]_{(p, q) \in C_{\text {diff }}}
\end{aligned}
$$

whose means ( $m_{r}^{\text {aame }}$ and $m_{r}^{\text {diff }}$ ) and standard deviations ( $\sigma_{r}^{\text {an e }}$ and $\sigma_{r}^{\text {diff }}$ ) are

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-14.jpg?height=580&width=742&top_left_y=91&top_left_x=1117)
Figure 3.15: Discriminability of Ensemble $5(T=3279, V=3840)$, linear $r$ The mean $m_{r}^{s a m e}$ of the distribution $F_{r}^{s a m e}(3.6)$ is plotted with diamonds; the mean $m_{r}^{\text {diff }}$ of $F_{r}^{\text {diff }}$, with the top solid line as a function of $r$. The ratios with their respective standard deviations are plotted with the bottom solid line $\left(m_{r}^{\text {diff }} / \sigma_{r}^{\text {dif }}\right)$ and the dashed line $\left(m_{r}^{\text {same }} / \sigma_{r}^{\text {same }}\right)$ (cf. Fig. 3.16). The dotted lines are at 2 and $\sqrt{2} / 2 \approx 0.707$.

shown on Fig. 3.15 with $r$ on a linear scale and on Fig. 3.16, with $r$ on a logarithmic scale.

When $(p, q) \in C_{\text {diff }}$ ( $\phi^{p}$ and $\phi^{q}$ are images of two different people), there is an expectation that the PCA coefficients of $\phi^{p}$ and $\phi^{q}$ will be uncorrelated, and the distribution of their differences could be calculated on the basis of the individual distributions (A.1). Indeed, if they were normal- $\mathcal{N}(0,1)$ (A.2), then the distribution of their difference would be $\mathcal{N}(0,2)$ (Papoulis 1991). Since $D_{r}^{(p, q)}$ is the square of the difference (3.5), ${ }^{20}$ then its mean $m_{r}^{\text {diff }}=m_{1}$ would be equal to the second moment of $\mathcal{N}(0,2), m_{1}=2$, independent of $r$. Its second moment $m_{2}$ would be equal to the fourth moment $\mu_{4}$ of $\mathcal{N}(0,2), m_{2}=$ $3 \times 2^{2}=12$ (A.4). The variance would be $\sigma_{r}^{\text {diff }}=\sqrt{m_{2}-m_{1}{ }^{2}}=2 \sqrt{2}$, and finally, $m_{r}^{d i f} / \sigma_{r}^{d i f}$ would be $\sqrt{2} / 2$, independent on $r$.

[^15]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-14.jpg?height=599&width=742&top_left_y=1432&top_left_x=1126)
Figure 3.16: Discriminability of Ensemble $5(T=3279, V=3840), \log r$ The dependencies from Fig. 3.15 are plotted on a logarithmic scale for $r$.

Those two expectations are plotted with horizontal lines on Fig. 3.15 and Fig. 3.16. It is evident that the measured moments differ from the expectations. The deviation of the variance is easier to account for-in Appendix A. 3 we show that the actual distributions of the PCA coefficients are not normal; Fig. A. 8 illustrates that their first few moments are larger that expected, i.e, the distributions are wider. This is evident for $m_{r}^{\text {diff }} / \sigma_{r}^{\text {diff }}$ on Fig. 3.15 and Fig. 3.16 -its behavior correlates nicely with the observation of the individual moments on Fig. A.8.

The deviation of $m_{r}^{\text {diff }}$ from 2 is somewhat more puzzling. Indeed, it is the second central moment of a distribution of the differences of two random variables, drawn arguably independently from the same distribution. Then

$$
\mu_{2}=\left\langle(\mathbf{u}-\mathbf{v})^{2}\right\rangle=\left\langle\mathbf{u}^{2}\right\rangle+\left\langle\mathbf{v}^{2}\right\rangle-2\langle\mathbf{u} \mathbf{v}\rangle
$$

independently of the assumed shape of the distribution. The first two terms in (3.7) are equal to 1 by construction (2.42). By the same argument, if they were drawn from distributions with different $r$, the last term would vanish. Since they are drawn from the same distribution, there is nothing to guarantee this-it could happen that the distribution is not zero-centered. In such a case, with independent drawings, $\langle\mathbf{u v}\rangle=\langle\mathbf{u}\rangle\langle\mathbf{v}\rangle=\langle\mathbf{u}\rangle^{2} \neq 0$ and we would be
able to explain the deviations $\mu_{2} \neq 2$. Unfortunately, the distributions are zero-centered (Fig. A.7) and we need another explanation. ${ }^{21}$

Having devoted much ink to the small, but most probably understandable, deviation of $F_{r}^{\text {diff }}$ from the our expectations, we now move to the much more interesting $r$-dependence of $F_{r}^{s a m e}$ (Fig. 3.15). Three regimes are evident: initial rapid growth, up to $N \approx 400$; mildly asymptotic behavior, up to $N \approx 1800$; and strong growth thereafter. One is tempted to hypothesize that the first one is the logarithmic regime of the spectrum, and last two are the exponential-the regime of personal eigenmodes, and pixel-level noise, respectively (see discussion on page 36).

The initial regime looks more interesting on a logarithmic scale for $r$ (Fig. 3.16); there it is roughly linear. We have encountered this situation previously; when we studied the logarithm of the average signal power (Fig. 3.14) we identified a power-law regime. In this case, the vertical axis is not on a logarithmic scale. Nevertheless, the variables whose averages are plotted $D_{r}^{(p, q)}(3.5)$ are squares of lengths in $S$, and, since the exponentials of such objects define probabilities (2.49), we can identify a power-law regime for those probabilities.

Notably, the power law coupling between the probability density $\mathcal{P}[\phi(\mathbf{x})]$ of faces and the concept of "identity" is not self-evident-we know of no a priori reason to expect one, so we treat this coupling as an experimental fact, rather than an illustration of something that we knew in advance. ${ }^{22}$

Having found this intriguing dependency, one is curious to know whether it could be used for classification; How does the observation of a "small" $D_{r}^{(p, q)}$ influence our confidence that $\phi^{\mathrm{p}}$ and $\phi^{q}$ are images of the same person?

Evident from $m_{\mathrm{r}}^{\text {ane }} / \sigma_{\mathrm{r}}^{\text {anme }}$ and $m_{\mathrm{r}}^{\text {diff }} / \sigma_{\mathrm{r}}^{\text {diff }}$ (the bottom two lines of Fig. 3.16), the distributions of the intra-identity differences are wider-the differences have a very high probability of being small, but also, relatively high probability of being large. Qualitatively, their tails extend well into the range of values which are normally associated with different identities, thereby preventing a clear-cut distinction.

To quantify the separation properties of the pairs of distributions $F_{r}^{\text {same }}$ and $F_{r}^{\text {diff }}$, we look at their Receiver Operating Curve (ROC) for various $r$ (Fig. 3.17). ${ }^{23}$
${ }^{21}$ There are two possible reasons that a zero-centered distribution might have $\langle\mathbf{u v}\rangle \neq 0$. One is that the averaging is not over independent drawings; the other, that it is due somehow to either the distribution itself, or to the limited statistics. We would favor the later hypothesis. Indeed, the averaging (3.6) is done over $C_{\text {diff }}$, instead of over $T \times T$ nevertheless, $\frac{1}{2}\left|C_{\text {diff }}\right|=N_{d}=4,642,834$, and $\frac{T \times T}{2}=\frac{3049 \times 3048}{2}=4,646,676$ (Table 3.1)-too small a difference to account for the 5-20\% effect that is evident on Fig. 3.16.
${ }^{22}$ Naturally, it would be interesting to understand the reason for this nontrivial coupling, but this is beyond the scope of this Thesis.
${ }^{23}$ The distribution of the random variable $u$ is the function $F: \mathcal{R} \mapsto[0,1]$ with certain properties (Papoulis 1991), where $F(u)$ is the probability $P\{\mathbf{u}<u\}$. For any two distributions $F_{1}$ and $F_{2}$, their ROO is $F_{2} \circ F_{1}^{-1}:[0,1] \mapsto[0,1]$, i.e., the ROO is the parametric plot

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-15.jpg?height=599&width=802&top_left_y=1439&top_left_x=139)
Figure 3.17: ROC for individual eigenmodes of Ensemble 5

It is evident that for any value of $r$, the two respective distributions are not very well separated. Indeed, the most discriminating one is $r=2$; if we observe, for a given pair of images $(p, q)$, a $D_{2}^{(p, q)}$ value such that $30 \%$ of the differences in $F_{2}^{\text {same }}$ are below it, then only 2-3\% of the ones in $F_{2}^{\text {dif }}$ would be. Unfortunately, if we want to raise the intra-identity cutoff to 40\%, the error rate will go to 5\%; even worse, a 60\% confidence comes with a 10\% error rate; $80 \%$, with $30 \%$. Although unacceptable for any practical purposes, this is not troubling per se; there is still the hope that, by somehow combining the information from many weak separations, good discrimination can be achieved.

We proceed to search for such combinations (3.4). Although one possibility is to use $w_{\tau}^{\text {equal }}=1$, it is evident from both Fig. 3.17 and Fig. 3.16 that weighing every $D_{r}$ equally may not be the best idea-some are more informative than others.

Another possibility is to use the Fisher Discriminant Method (Watanabe 1985). It treats $\mathrm{d}^{(\mathrm{p}, q)}$ as points in an $N$ dimensional space and tries to find the hyperplane which best separates them. The normal of this plane is given by

$$
w_{t}^{F i s h e r} \propto \sum_{r=1}^{N}\left(m_{r}^{s q a m \varepsilon}-m_{r}^{d i f f}\right)\left(H^{i n t m g}\right)_{r t}^{-1}
$$

$x=F_{1}(u), y=F_{2}(u)$.

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-15.jpg?height=573&width=800&top_left_y=94&top_left_x=1065)
Figure 3.18: ROC for the Fisher discriminability measure Receiver Operating Curves for the Fisher coefficients $w_{r}^{\text {Fieher }}(3.8)$.

where $H^{\text {intra }}$ is a suitably defined intra-class scatter matrix.
Alternatively, if no dependency across $r$ is assumed, $H^{\text {intra }}$ can be considered diagonal with elements $H_{r r}^{\text {intra }}=\left(\sigma_{r}^{\text {same }}\right)^{2}+\left(\sigma_{r}^{\text {diff }}\right)^{2}$ and the weighing is according to the individual separations of the means and the variances of the distributions for each $r$

$$
w_{r}^{\text {naive }} \propto\left(m_{r}^{\text {same }}-m_{r}^{\text {diff }}\right)\left(H^{\text {intra }}\right)_{r r}^{-1} .
$$

The ROCs for these three strategies $w_{r}^{\text {Fisher }}, w_{r}^{\text {nnive }}$, and $w_{r}^{\text {equal }}$ are shown on Fig. 3.18, Fig. 3.19, and Fig. 3.20, respectively, wherein the dimensionality of the PCA subspace $N$ has been varied.

It is evident that $w_{r}^{\text {Fisher }}$ provides the best strategy of all three in the small $N$ regime. For example, for $N=20$, an operational cutoff $\epsilon$ can be chosen such that $D^{\text {same }}$ will fall below $\epsilon$ for $80 \%$ of the cases, whereas $D^{\text {diff }}$ will fall below $\varepsilon$ for only $20 \%$ of the cases. While this is an improvement over the single-coefficient separation (Fig. 3.17), it is not usable for building practical systems.

The failure to classify well with $N=20$ is not a surprise-we know that about $N=300$ is needed to preserve the identity information in the PCA subspace (Fig. 3.12). Unfortunately, for bigger values of $N$, all three proposed methods actually decrease their performance, indicating that identity infor-

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-15.jpg?height=599&width=800&top_left_y=1430&top_left_x=1074)
Figure 3.19: ROC for the "naïve" discriminability measure Receiver Operating Curves for $w_{r}^{\text {naive }}(3.9)$.

mation is distributed non-trivially across all dimensions. Therefore, only the limited task of classification according to broadly defined classes can be carried out naturally in the PCA representation.

### 3.3 The Shortcomings of PCA

In Section 3.2.2 we found a non-trivial power law coupling between the eigenspace for human faces and the concept of "identity" (Fig. 3.16). We showed that it is weak enough so that it cannot be exploited in a straight-forward manner for building practical systems.

Although many other (relatively complex) algorithms are known, can be, and most probably have been, attempted on the low-dimensional PCA representation, the goal of this Thesis is to find representations, in which the complexity of the classification problem is more manageable.

By now, we have developed some intuition for where the problem lies. In Section 3.1.3 we argued that the information about localization of features is distributed in a sub-optimal and non-explicit manner across the PCA modes (Fig. 3.9). In general, we know intuitively that there are limited local symmetries in the physical space scale and translational that are present in even

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-16.jpg?height=580&width=802&top_left_y=98&top_left_x=132)
Figure 3.20: ROC for the component probability discriminability measure Several Receiver Operating Curves for $w_{r}=1$.

the best controlled ensembles. PCA as a method has no way of dealing with them naturally-they will invariably lead to spread of features across many PCA modes.

And finally, before we proceed to propose a representation in which the localization information is explicit, we will give one last illustration of this feature localization effect.

The PCA analysis of Ensemble 4 (see Appendix A. 1 for definition) is shown on Fig. 3.21. It is comprised of the same pictures as Ensemble 1 with a more liberal cropping-including the hair, some clothing and more background. Since there is much more translation symmetry in those areas, it would be expected that more "localization" modes are present. Indeed, apart from the in-sample effect, almost all of the genuine ${ }^{24}$ modes are purely localization and background modes there is not a single strong "facial feature" mode present. ${ }^{25}$

[^16]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-16.jpg?height=516&width=886&top_left_y=1503&top_left_x=98)
Figure 3.21: PCA Analysis of Ensemble $4(T=1038, V=11520)$

The first 16 eigenmodes $\left\{\Psi_{r}(x)\right\}_{r=1}^{16}$ of Ensemble 4 (top and middle) and several of the rest (bottom). See Appendix A. 1 for description of the images in it.

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-16.jpg?height=334&width=848&top_left_y=2239&top_left_x=130)
Figure 3.22: $\log$ Spectrum of Ensemble $4(T=1038, V=11520)$ The spectrum of Ensemble $4(T=1038, V=11520)$ compared with Ensemble 1 $(T=1038, V=3840)$. See Fig. 3.13 for definition of the dependencies being ploted.

even worse with this ensemble.
53

## Chapter 4

## Local Feature Analysis

This Chapter presents the main result of the Thesis. After a brief summary of the reasoning that led to it, we will lay out its organization.

### 4.1 Introduction

Driven by the principle of redundancy reduction (Section 2.1), we realized that the problem is one of finding an economical, yet relatively accurate parameterization of the probability density $\mathcal{P}[\phi(\mathbf{x})]$ of ensembles of natural stimuli, $\left\{\phi^{t}(\mathbf{x}), t=1, \cdots, T\right\}$.

We found that PCA is a redundancy-reducing factorial code (Section 2.2) that produces a natural hierarchical parameterization of $\mathcal{P}[\phi(\mathbf{x})]$ (2.49). On the basis of an argument about signal power fidelity, we showed how PCA can be utilized for dimensionality reduction of the representation (2.50).

We studied various ensembles of images of human heads taken under natural conditions and showed that, for suitably defined alignment and cropping, PCA is an adequate and economical representation with dimensionality $N$ as low as 300-400 (Fig. 3.12). We also developed some insight into the dependence of the quality of the results on the ensemble size and preparation protocol.

Motivated by this low dimensionality, we attempted to build a straightforward practical system for face classification (Section 3.2.2). Failing, we argued that there are naturally occurring symmetries that are not captured transparently by PCA (Section 3.3).

In this Chapter, we propose a novel, statistically-driven representation of objects in terms of their local features. The two-stage procedure, which we call Local Feature Analysis (LFA), initially derives a dense set of local receptive fields, defined at each point of the receptor grid and different from each other, that are optimally matched to the input ensemble, and whose outputs are as decorrelated as possible.

Since the objects from the input ensemble span only a very-low-dimensional subspace, the dense outputs are necessarily linearly dependent and, also, con-
tain residual correlations; this temporarily obscures the low dimensionality of the ensemble.

The second, dynamic, stage of LFA finds a sparse set of outputs that form a distributed code of the objects in terms of their local features. The number of active units for a given example is typically much less than the already low underlying PCA dimensionality of the ensemble, therefore not only making the it explicit, but also reducing it further.

The organization of this Chapter is as follows. In Section 4.2 we motivate the need for topographic representations with the requirement for local computations; we develop the LFA formalism for symmetric ensembles, with full dimensionality, and discuss their properties in the context of LFA.

In Section 4.3 we generalize the LFA formalism to include object ensembles, with reduced dimensionality. We illustrate it by deriving local features in three different object ensembles, similar to ensembles for which global representations have been derived in the past (Sirovich and Kirby 1987; Atick et al. 1996b).

In Section 4.4 we show how a local sparse-distributed representation can be derived from the representation of Section 4.3. Initially, we show how to find maximum-likelihood estimates, consistent with the measurements of a single simple feature (Section 4.4.2), and then, of many complex features (Section 4.4.3). In Section 4.4.4 we propose an efficient serial sparsification algorithm. On the basis of its output, in Section 4.4.5 we interpret the sparsedistributed representation as a set of weakly interacting clusters, each representing a complex local feature. In Section 4.4.6 we propose a neural-network architecture and dynamics, in which the residual correlations form the basis of lateral inhibition, which inherently parallel and biologically plausible.

### 4.2 Linear Factorial Codes for Symmetric Ensembles

In Chapter 2 we motivated our interest in factorial codes from the point of view of redundancy reduction-a design principle formulated to address, among other things, the problem of high data rates of natural signals (see discussion on page 9).

In Chapter 3 we showed how PCA, a factorial code, can be used to reduce the dimensionality of suitably prepared ensembles of objects.

The preparation of such ensembles, however, is a non-trivial task, related to segmentation and categorization, and arguably happens during the late stages of the neural processing of visual stimuli. ${ }^{1}$ Also, in the discussion of ensembles of objects, we did not mention the high-data-rate problem; it, arguably, has to be addressed at an earlier stage of processing.
${ }^{1}$ There is good evidence that the processing specific to faces happens only after the primary visual cortex processing (Nachson 1995 and references therein).

## 55

Let us take, for example, the human retina: on one side of it are the outputs of the photo receptors, driven by the ensemble of natural stimuli, with an estimated the data rate ~ 5 Gbytes/sec; on the other side is the optic nerve, comprised of about 1,000,000 axons, each with a maximum capacity of ~1000 bits/sec, totaling ~ 1 Gbits/sec. ${ }^{2}$ One of the tasks of the retina is to perform, in real time, a computation that reduces the redundancy of the input ~40 times.

We already identified a reason why this daunting task might turn out to be possible-the natural signals are not random; they are redundant (see discussion in footnote 5 on page 10). PCA (Chapter 2) is arguably the most natural, theoretically well understood, and computationally feasible method for redundancy reduction; an obvious idea is to apply it to the ensemble of natural images.

The first step in the application of PCA is to measure the correlation matrix (2.1) and diagonalize it (2.25). Here we face a problem immediately with the number of photo receptors $V \approx 6 \times 10^{6}, R(\mathbf{x}, \mathbf{y})$ has $\frac{1}{2} V^{2} \approx 18,000$ Giga elements; storing so many values is a problem, ${ }^{3}$ measuring them statistically significantly is an even bigger problem, but diagonalizing such a matrix is the biggest one.

Luckily, there are certain symmetries that are present, or can safely be assumed to be present, in natural signals; the translation symmetry is the most prominent. Indeed, animals have the freedom to move their heads and eyes at will, and it can be assumed that any natural scene has an equal chance of being observed at any translation in the field of view. Mathematically, this means that ${ }^{4}$

$$
R(\mathbf{x}, \mathbf{y})=r(\mathbf{x}-\mathbf{y}) .
$$

All the elements along a given diagonal of $R(\mathbf{x}, \mathbf{y})$ are equal- $R(\mathbf{x}, \mathbf{y})$ is a Toeplitz matrix. This reduces the storage and measurement requirements to $\sim 6,000,000$-a manageable level, but still, the diagonalization of such systems is a problem (Chan et al. 1996). Another symmetry that is usually taken into account is the rotational symmetry-animals can tilt their heads, therefore

[^17]natural scenes have equal chances of being encountered at any angle, ${ }^{5}$ and the autocorrelation function can only depend on the distance $\ell=\|\mathbf{x}-\mathbf{y}\|$, but not on the direction of $\mathbf{x}-\mathbf{y}$; hence
$$
R(\mathbf{x}, \mathbf{y})=r(\mathbf{x}-\mathbf{y})=\rho(\ell) .
$$
The assumption of rotational symmetry reduces the dimensionality of the problem to $\sim \sqrt{6,000,000} \approx 3,000$-quite a manageable size. ${ }^{6}$

The assumption of translation symmetry makes the diagonalization task even simpler-in the translationally-invariant case, PCA is equivalent to Fourier Analysis; ${ }^{7}$ the eigenvectors of $R(\mathbf{x}, \mathbf{y})$ are indexed with the spatial frequency $\mathbf{f}$ and are given, up to a normalization constant, by

$$
\Psi_{\mathbf{f}}(\mathbf{x})=e^{\mathbf{i f} \cdot \mathbf{x}} .
$$

The eigenvalue associated with the eigenmode $\Psi_{\mathbf{f}}(\mathbf{x})$ is the Fourier transform of $r(\mathbf{x})$ evaluated at $\mathbf{f}, \tilde{r}(\mathbf{f})$. In the rotationally-symmetric case it only depends on the norm of the frequency $|f|$.

That leaves us with the task of measuring $\rho(\ell)$ (4.2) and doing a Fourier transform on it to get the spatial power spectrum, of static natural scenes. This is what has been measured, with moderate to great care, by many groups many times over the years (Burton and Moorhead 1987; Field 1987; Tolhurst et al. 1992; Hancock et al. 1992; Ruderman and Bialek 1994; Ruderman 1994b). Invariably, those studies show a power-law spectrum (cf. Fig. 3.21)

$$
\sigma_{\mathbf{f}}^{2} \equiv \tilde{r}(\mathbf{f}) \propto \frac{1}{|\mathbf{f}|^{\alpha}}
$$

with $\alpha \approx 2$, slightly less, ${ }^{8}$ depending on the degree of care taken in the measurements.
${ }^{5}$ This may be a questionable proposition for the inhabitants of Manhattan, New York (Fig. A.12), but it is, most probably, very close to true for the inhabitants of the rain forest, Brazil (or Princeton, New Jersey, for that matter; Ruderman and Bialek 1994).

In all cases, the assumption of rotational symmetry greatly simplifies the solution to the problem and, moreover, is experimentally supported by the observation of circularly symmetric receptive fields in the retina (Stone 1983; Dowling 1987; Wässle and Boycott 1991).
${ }^{6}$ This is an oversimplification; because of the irregular placement of photo receptors on the retina, as well as of the retina not being square, $\ell$ assumes more values than stated. Nevertheless, this still leaves a problem whose dimensionality is thousands, instead of millions.
${ }^{7}$ Strictly speaking, the system has to be infinite for this analysis to hold. In that case, $U$ is no longer finite-dimensional and proper care should be taken in saying what is meant by inner products (2.4) and sums (2.5). For the time being, we will assume that (4.3) is a good approximation to the exact solution and let the intuition developed in the previous chapters take control. We will return to the problem of finite-size effects and more rigorous definitions in Appendix A.6.
${ }^{8}$ If the world were truly scale-invariant, $\alpha=2$ would hold exactly (Atick and Redlich 1992).

## 57

Finally, the parameterization for the correlation function $R(\mathbf{x}, \mathbf{y})$, and, therefore, of the probability density $\mathcal{P}[\phi(\mathbf{x})]$, of the translationally and rotationally symmetric ensemble of static natural scenes is $(2.25)^{9}$

$$
\Phi^{*} \Phi=\mathrm{R}=\sum_{\mathbf{f}} \Psi_{\mathbf{f}} \sigma_{\mathbf{f}}^{2}\left(\Psi_{\mathbf{f}},\right)
$$

with $\Psi_{\mathbf{f}}$ from (4.3) and $\sigma_{\mathbf{f}}$ from (4.4). Since the spectrum is entirely in the power-law regime (see discussion on page 40), no dimensionality reduction is possible by truncation of (2.45), and $N=V \approx 6,000,000$.

With the spectral decomposition of the retinal ensemble (4.5), we can proceed with the application of PCA. For any example $\phi(x)$ at the output of the photo receptors, we need to calculate its $N \approx 6,000,000$ PCA coefficients from (2.48), and ship them over the optic nerve. ${ }^{10}$

We see several immediate problems. First, although (4.5) is an extremely frugal parameterization at the abstract level, ${ }^{11}$ any actual calculation, such as (2.48), needs all the $N \times V$ coefficients of the $N$ eigenmodes explicitly. Since there is no dimensionality reduction, $N=V$, and we necessarily hit the storage problem again, ${ }^{12}$ this time, for the coefficients (4.3) of the eigenmodes.

[^18]A possible solution would be, the modes to have only a small number of significantly non-zero coefficients (to have small supports), so that the storage requirements are much less than the theoretical maximum. Unfortunately, the Fourier eigenmodes (4.3) are periodic (they are sines and cosines) and have non-zero coefficients everywhere.

Also, it is not entirely clear how the computational noise in the sum (2.47), with $N=6,000,000$ elements, can be controlled via chemical means in the cells and synapses of the retina. We will refer to this set of problems as the large support problem.

Second, in the calculation of any given PCA coefficient (2.48), the values of $\phi(\mathbf{x})$ from all over the receptor grid have to be brought together at the same place to be summed. This would require the retina to be densely wired with afferents, which connect every point to every other point. We will refer to this problem as the global support problem.

Are these problems unsurmountable? Is it time to abandon second-order statistics and search for other methods?

In trying to answer these questions, we turn to the architecture of the retina. It is known that the retinal processing is local (Wässle and Boycott 1991). The ganglion cells have receptive fields that cover only a limited part of the visual field. Also, the processing is topographic-the receptive fields of neighboring ganglion cells overlap each other-and retinotopic-the receptive fields of ganglion cells in the center of the retina are in the center of the visual field, and so for the periphery.

Locality receptive fields with small supports, which are confined to spa- tially localized regions-and topography-output variables that are labeled with the same index as the input variables, spatial, in this case-are related concepts, but are somewhat different. On one hand, it is difficult to imagine local nontopographic processing that does not change dimensionality. On the other hand, the processing may well be topographic, but still be global.

The value of locality is clear it solves both the global support problem and the large support problem. We speculate that the value of topography is twofold: on one hand, to allow the existence of local receptive fields; on the other, to preserve for subsequent steps of processing spatial information that is not explicitly taken care of during the current step.

Although it is not exactly clear mathematically how to impose locality, topography is a very simple property all it says is that the output of an operator should be in the same space as its input. ${ }^{13}$

Guided by the architecture of the retina, Atick and Redlich (1992) decided to look for a topographic linear operator

$$
\mathrm{K}: U \rightarrow U
$$

${ }^{13}$ Note that this is not the case for PCA (2.47).

## 59

that reduces redundancy in the context of the ensemble of natural scenes-with $\mathcal{P}[\phi(\mathbf{x})]$, parameterized by (4.3-4.5). Acting on any input activation pattern $\phi^{\hat{t}}=\Phi^{*} \hat{t}$ in the ensemble, $\mathbf{K}$ results in

$$
\mathrm{K} \phi^{t}=\mathrm{K} \Phi^{*} \hat{t} \equiv \mathrm{O}^{*} \hat{t} \equiv O^{t} .
$$

Thus, given the ensemble of sensory inputs $\Phi, \mathbf{K}$ produces the ensemble of outputs O by

$$
K \Phi^{*}=O^{*}
$$

such that (cf. 2.12)

$$
\langle\hat{t}, \mathbf{O} \hat{\mathbf{x}}\rangle=\left(\mathbf{O}^{*} \hat{t}, \hat{\mathbf{x}}\right) \equiv O^{t}(\mathbf{x}) .
$$

Atick and Redlich (1992) imposed the requirement of redundancy reduction in the form of ensemble-average decorrelation of the output variables (cf. 2.42):

$$
\langle O(\mathbf{x}) O(\mathbf{y})\rangle_{T}=\frac{1}{T} \sum_{t} O^{t}(\mathbf{x}) O^{t}(\mathbf{y}) \propto \delta_{\mathbf{x}, \mathbf{y}}
$$

with a proportionality constant dependent on the choice of units for $O(\mathbf{x})$. It is determined by the choice of the inner products (2.4) and, with the definition (4.9), is equal to $V$.

With this choice, from (2.4), (4.10), and (2.14)

$$
(\hat{\mathbf{x}}, \hat{\mathbf{y}})=V \delta_{\mathbf{x}, \mathbf{y}}=\frac{1}{T} \sum_{t} O^{t}(\mathbf{x}) O^{t}(\mathbf{y})=\langle\mathrm{O} \hat{\mathbf{x}}, \mathrm{O} \hat{\mathbf{y}}\rangle=\left(\hat{\mathbf{x}}, \mathrm{O}^{*} \mathrm{O} \hat{\mathbf{y}}\right)
$$

hence

$$
\mathbf{O}^{+} \mathbf{O}=\mathbf{1}_{U} .
$$

Therefore, the decorrelation of the topographic outputs (4.9) requires that $\mathrm{O}^{*} \mathrm{O}$ be the identity operator (2.5) on $U$. The identity has the nice property that it looks identically in any complete orthonormal basis. In the retinal case, the PCA basis (4.5) is complete- $\sigma_{\mathrm{f}}>0$ for all f (4.4), hence (2.34)

$$
O^{*} O=\sum_{f} \Psi_{f}\left(\Psi_{f},\right)
$$

The spectral decomposition of $\mathrm{O}^{*} \mathrm{O}$ (4.13) is encouraging, since it utilizes the PCA $U$-basis of $\Phi$. We are now interested what O is; this is fully determined by its action on the basis vectors $\Psi_{\mathbf{F}}$ :

$$
\mathbf{O} \Psi_{\mathbf{f}}=\mathbf{o}_{\mathbf{f}} \in S .
$$

In order to satisfy (4.13), $\left\{\mathrm{o}_{\mathrm{f}}\right\}$ have to satisfy

$$
O^{*} o_{\mathbf{f}}=\Psi_{f} .
$$

This, actually, leaves quite some freedom in the choice for $\mathrm{of}_{\mathrm{f}} .^{14}$ We will have this degree of freedom in mind, and will, for now, follow Atick and Redlich (1992) and use the PCA $S$-basis of $\Phi$ to fix it:

$$
o_{f}=s_{f} .
$$

With this choice,

$$
\begin{aligned}
\mathrm{O} & =\sum_{f} \mathrm{~s}_{\mathbf{f}}\left(\Psi_{f},\right) \\
\mathrm{O}^{*} & =\sum_{f} \Psi_{f}\left\langle\mathrm{~s}_{f},\right\rangle .
\end{aligned}
$$

Notably, $\mathrm{O}=\mathrm{O}^{*+}$, which comes from the fact that the eigenvalues of O*O (4.13) are all equal to $1 .{ }^{15}$

From (4.17), (cf. 2.33)

$$
O O^{*}=\sum_{f} s_{f}\left(s_{f},\right)=P^{\prime} .
$$

Note that even though $\mathrm{O}^{*} \mathrm{O}$ is the identity on $U(4.12), \mathrm{OO}^{*}$ is still only a projector to a subspace in $S$. This follows from the fact that $N=V$, but $T \gg V .{ }^{16}$

We are now prepared to state what K is: from (4.8), (2.31), and (4.17)

$$
\mathrm{K}=\sum_{\mathbf{f}} \Psi_{\mathbf{f}} \frac{1}{\sigma_{\mathrm{f}}}\left(\Psi_{\mathbf{f}},\right)=0^{*} \Phi^{*+}
$$

This is a remarkable fact-the redundancy-reducing topographic operator K acts by first, calculating the PCA representation with $\Phi^{*+}$ (2.48) and, then, sending it back to $U$ with O* to regain topography.
${ }^{14}$ It can be shown that (4.12) can be satisfied if the transformation matrix $U$ between $\left\{\mathbf{o}_{\mathbf{f}}\right\}$ and $\left\{\mathbf{s}_{\mathbf{f}}\right\}$ obeys $\mathbf{U}^{*} \mathbf{U}=\mathbf{P}^{\prime}$. In this notation, the choice (4.16) is $\mathbf{U}=\mathbf{P}^{\prime}$.

The $U$-symmetry was exploited previously to produce representations that, without destroying decorrelation, possess other desirable properties for example scale invariance, which leads to a multi-scale representation (Li and Atick 1994).
The current fixing of the unitary symmetry was derived in previous work on the retina (Atick and Redlich 1992) by the criterion of minimal distortion from input to output, where it was shown to generate local receptive fields.
${ }^{15}$ Mathematicians would say that O is an orthogonal operator.
${ }^{16}$ Indeed, by enforcing translation invariance, we are effectively including in the ensemble all translated versions of a single example $\phi$. With $V$ receptors, there are $V$ possible translations, thus, a single original example, when translated, can result in $V=T$. Of course, this does not mean that these statistics are enough, because the examples are not independent in the statistical sense, although they are linearly independent and span $U$.

## 61

The factor $1 / \sigma_{\mathrm{f}}$ in (4.17) is also notable. One way to think about it is that it normalizes the PCA output variance (2.42) to unity. ${ }^{17}$

More importantly, its appearance in the formula for the PCA coefficients (2.48) guaranteed that the square of the length of the vector $\Phi^{*+} \phi \in S$ is proportional to the length of the optimal code for $\phi,-\log \mathcal{P}[\phi]$ (2.49). It is interesting to see whether such a useful relationship exists for the topographic representation $O=\mathrm{K} \phi$ (4.7).

For that, we need to consider $\left\|\Phi^{*+} \phi\right\|_{S}^{2}$ (2.20). We act on both sides of (4.19) with O and, noting (4.18) and (2.33), we get

$$
\mathrm{OK}=\mathrm{OO}^{*} \Phi^{*+}=\mathrm{P}^{\prime} \Phi^{*+}=\Phi^{*+}
$$

hence

$$
\begin{aligned}
\left\|\Phi^{*+} \phi\right\|_{S}^{2}= & \left\langle\Phi^{*+} \phi, \Phi^{*+} \phi\right\rangle=\langle\mathbf{O K} \phi, \mathbf{O K} \phi\rangle= \\
=\left(\mathbf{K} \phi, \mathbf{O}^{*} \mathbf{O K} \phi\right)= & (\mathbf{K} \phi, \mathbf{K} \phi)=\|\mathbf{K} \phi\|_{U}^{2} .
\end{aligned}
$$

This is another remarkable fact the probability $\mathcal{P}[\phi(\mathbf{x})]$ factorizes and is determined by the square of the length of the representation (cf. 2.49):

$$
\mathcal{P}[\phi] \propto \exp \left\{-\frac{1}{2} \sum_{x} O(\mathbf{x})^{2}\right\} \propto \prod_{\mathbf{x}} \exp \left\{-\frac{1}{2} O(\mathbf{x})^{2}\right\} .
$$

The variables $\{O(\mathbf{x})\}_{x \in V}$ do, indeed, code directly for the probability of observation a given sensory stimulus $\phi$ a design goal postulated by Barlow et al. (1989). We proceed to show how they code for $\phi$ itself. For that, we need an inverse of $\mathrm{K}(4.19) .^{18}$ With $O=\mathrm{K} \phi, \mathrm{O}^{*+}=\mathrm{O}$ (4.17), and (4.20),

$$
\mathrm{O}^{*+} O=\mathrm{O} O=\mathrm{OK} \phi=\Phi^{*+} \phi .
$$

Notably, the ensembles $\Phi$ and O share the same PCA representation. Finally we act with $\Phi^{*}$, noting (2.34): $\Phi^{*} \mathrm{O}^{*+} O=\Phi^{*} \Phi^{*+} \phi=\phi$. Hence, from (4.17)

[^19]and (2.31) (cf. 4.19)
$$
\mathbf{K}^{-1}=\Phi^{*} \mathbf{O}^{*+}=\sum_{\mathbf{f}} \Psi_{\mathbf{f}} \sigma_{\mathbf{f}}\left(\Psi_{\mathbf{f}},\right) .
$$

Now we are ready to ask the question how much we have achieved. Following Atick and Redlich (1992), we enforced topography in the hope that we can get locality. Indeed, nothing guarantees this-we hypothesized that topography will allow locality, but acknowledged that there might be nonlocal topographic representations. Nevertheless, the requirement (4.12) is weak enough, so we may hope to use the freedom in it to find local representations among the many possible topographic ones.

Indeed, Atick and Redlich (1992) fixed the degree of freedom (4.16) by requiring "minimum distortion from input to output," which at least sounds "local." Interestingly, with this fixing, from (4.19), in the context of the ensemble of natural scenes-with the PCA eigenvectors ${ }^{19} \Psi_{\mathrm{f}}$ (4.3) and eigenvalues ${ }^{20}$ $\sigma_{\mathrm{f}}$ (4.4) the receptive field at the grid point x

$$
K_{x}(y) \equiv K \hat{x}=\sum_{f} \Psi_{f} \frac{1}{\sigma_{f}}\left(\Psi_{f}, \hat{x}\right)=\sum_{f}|f| e^{i f(y-x)}
$$

does look like the center-surround receptive fields measured in numerous neurophysiological experiments if the retinas of primates (Wässle and Boycott 1991).

A very interesting property of the topographic representation (4.17) is obvious from (4.25) translation invariance. Indeed, although the sensory ensemble is translationally invariant (4.1), the global PCA modes (4.3) are not-for any given mode $\Psi_{\mathbf{f}}$, the coefficient $\Psi_{\mathbf{f}}(\mathbf{x})=\left(\Psi_{\mathbf{f}}, \hat{\mathbf{x}}\right)$, associated with a given grid point x, changes with x and, also, depends on the existence of a hypothetical origin $\mathbf{x}_{0}=\mathbf{0}$. This is unsatisfactory, because the choice of $\mathbf{x}_{0}$ has to be made somehow, propagated reliably during the development of the retina and maintained with precision subsequently. On the other hand, the shape of the topographic receptive field centered at a given grid point, $\mathrm{K}_{\mathrm{x}}$ (4.25), depends only on the distance $\mathbf{x}-\mathbf{y}$ of the coefficient for $\mathbf{y}, \mathbf{K}_{\mathbf{x}}(\mathbf{y})=\left(\hat{\mathbf{y}}, \mathbf{K}_{\mathbf{x}}\right)$, from the center x; it is easy to imagine feasible developmental algorithms that rely on distance to guide the retinal wiring even without visual input (Shatz 1996), as well as such that are visual-input driven (Atick and Redlich 1993).

Very importantly, the topographic receptive fields (4.25) make apparent a symmetry of the ensemble (4.3-4.4) that was temporarily obscured in the PCA
${ }^{19}$ In dealing with an infinite-dimensional $U$, we need to specify what sums and inner products mean (footnote 7 on page 57). Part of the specification in this case is that the exponent is complex and the inner product conjugates the first operand hence the minus sign for x.
${ }^{20}$ We have assumed $\alpha=2$, sloppily. Although this changes the shape of the receptive fields slightly, it does not change the qualitative picture and makes it is a bit easier to manipulate (4.25) theoretically.

63
representation (2.47-2.52). This property is shared by all the members of the family of topographic operators

$$
\begin{aligned}
\mathrm{K}=\mathrm{O}^{*} \Phi^{*+} & =\sum_{\mathrm{f}} \Psi_{\mathrm{f}}\left(\frac{1}{\sigma_{\mathrm{f}}}\right)^{1}\left(\Psi_{\mathrm{f}},\right) \\
1=\mathrm{O}^{*} \mathrm{O} & =\sum_{\mathrm{f}} \Psi_{\mathrm{f}}\left(\frac{1}{\sigma_{\mathrm{f}}}\right)^{0}\left(\Psi_{\mathrm{f}},\right) \\
\mathrm{K}^{-1}=\Phi^{*} \mathrm{O}^{*+} & =\sum_{\mathrm{f}} \Psi_{\mathrm{f}}\left(\frac{1}{\sigma_{\mathrm{f}}}\right)^{-1}\left(\Psi_{\mathrm{f}},\right) \\
\mathrm{R}=\Phi^{*} \Phi & =\sum_{\mathrm{f}} \Psi_{\mathrm{f}}\left(\frac{1}{\sigma_{\mathrm{f}}}\right)^{-2}\left(\Psi_{\mathrm{f}},\right)
\end{aligned}
$$

for which the general member $i 8^{21}$

$$
\mathrm{K}^{n}=\sum_{\mathrm{f}} \Psi_{\mathrm{f}}\left(\frac{1}{\sigma_{\mathrm{f}}}\right)^{n}\left(\Psi_{\mathrm{f}},\right) .
$$

All members of the family are constructed by acting once, and expanding once, with $\Psi_{\mathbf{f}}$ and, by virtue of the argument for $\mathbf{K}_{\mathbf{x}}$ (4.25), depend only on $\mathbf{x}-\mathbf{y}$.

The fact that the description of the family (4.26) makes apparent the original symmetry in the ensemble has nothing to do with locality it could happen that no $\mathrm{K}^{n}$ (with the exception of $\mathrm{K}^{0}$, of course) is local; it comes entirely from topography. This makes topography valuable by itself, independently of locality.

So far, the inquiry into how much has been achieved was focused on topography; now we ask the question, How much locality has been achieved?

For the ensemble of natural scenes, the correlation matrix, $\mathbf{R}=\mathbf{K}^{-2}=$ $r(\mathbf{x}-\mathbf{y})$ (4.1), is equal to 1 at $\mathbf{x}-\mathbf{y}=0$ (every scene is perfectly correlated with itself) and decays with distance, being always positive. Unfortunately, because of the power-law spectrum (4.4), it can extend to relatively large distances. On the other hand, $\mathbf{K}^{0}=\mathbf{1}$ is extremely well localized its support collapses to the point in the center. We believe that the reconstruction operator $\mathrm{K}^{1}$ is somewhere in between $\mathbf{K}^{-2}$ and $\mathbf{K}^{0}$ spread somewhat, but not very much, and mostly positive. The coding operator $\mathbf{K}^{1}$ "overshoots" the absolute localization $K^{0}$ and is again spread somewhat-local, but, this time, with a center-surround structure.

In practice, the least local object, R, is never needed. The only needs that arise are, given an example $\phi$, to calculate its representation $O$, by use of K , and, given a representation $O$, to reconstruct the example $\phi$, by use

[^20]of $\mathrm{K}^{-1}$; both kernels used in practice are local. Also, since their values outside a local region are very small, they can be truncated to zero. This truncation will generate an error, which can be made arbitrary small by expanding the support. In practice, since the example $\phi$ itself contains some noise, the size of the support can be chosen so that the computational error is on the order of the measurement error, or less.

So far, we saw that the topographic representation, besides its desirable theoretical properties, can account qualitatively for the properties and the shape of the retinal receptive fields. Even more importantly, Atick and Redlich (1992) showed that, taking photon-counting noise into account (see discussion in footnote 17 on page 62), the factor $1 / \sigma_{\mathrm{f}}$ is in perfect quantitative agreement, up to the experimental error, with the contrast-sensitivity curves of human subjects under conditions of varying spatial frequency and background luminosity (noise level).

This is a remarkable finding. It shows that the human visual system, as a whole, is concerned with the probability of a given sensory stimulus, rather than its signal power-large changes of signal power in the modes with big variance go unnoticed, as long as they fall within the expectations, while relatively small changes, in the modes with small variance are very apparent, since they are unexpected. ${ }^{22}$

### 4.3 Local Features from Global Modes

The application of the topographic extension of PCA (4.26) to the ensemble of static natural scenes was so successful, that it was immediately applied to the color coding of the retina (Atick et al. 1992) and the cortex (Atick et al. 1993).

The success there motivated the measurement of the spatio-temporal power spectrum of natural scenes (Dong and Atick 1995a), and the application of topographic PCA to the ensembles of moving natural scenes resulted in the theory of LGN spatio-temporal decorrelation (Dong and Atick 1995b).

These exhausted all apparent second-order statistics of natural visual stimuli and left open questions about the possible role of the cortex. Arguably, there was no more value left in second-order correlations, and various attempts to turn to higher-order correlation were advanced. ${ }^{23}$

Shortly thereafter, Atick, Griffin, and Redlich (1996b) applied PCA to the ensemble of 3D surfaces of human heads and found rich structure in its second order statistics. This raised the possibility that, even after the retinal and
${ }^{22}$ This is in agreement with the observation of the relation between fidelity (SNR) and "perceptual quality," made several times throughout Chapter 3.
${ }^{23}$ Some of the most prominent redundancy-reducing approaches are enumerated in Chapter 1.

65
LGN processing, restricted ensembles of objects may still posses interesting second-order statistics.

This was also observed in Chapter 3-the (carefully prepared) ensemble of images of human faces has Principal Components that are markedly different from the sines and cosines of the translation-invariant retinal ensemble. Thus, even after possible retinal processing, if one has the ability to categorize, second-order statistics are still of interest.

In Chapter 3 we argued that, although PCA is a factorial code with the ability to reduce dimensionality whenever possible, it is still not a very suitable representation for higher-level tasks, such as classification and recognition. Interestingly, we hypothesized that the reason for this are the partial symmetries of the ensemble, which cannot be captured naturally by PCA.

In Section 4.2 we motivated the topographic representation (4.26) by the desire for local topographic processing. When we enforced topography, the translation symmetry of the ensemble, temporarily obscured in the global modes, became apparent.

It would be interesting to know whether there is a local topographic representation, analogous to (4.26), for ensembles of objects, what it looks like, and what its properties are.

With object ensembles, we are confronted with a problem. We derived the topographic representation (Section 4.2) from the requirement that the output variables $O(\mathbf{x})$ be decorrelated (4.11), which lead to the requirement $\mathbf{O}^{*} \mathbf{O}=\mathbf{1}_{U}$ (4.12) and the subsequent representation of $\mathrm{O}^{*} \mathrm{O}$ in the PCA basis of $U$ (4.13). Since typical object ensembles are with reduced dimensionality the modified ensemble $\Phi_{N}$ (2.45) is degenerate-the PCA basis does not span the whole $U$, and it cannot represent $\mathbf{1}_{U}$ fully.

The solution to this problem was suggested by Penev and Atick (1996) since full decorrelation (4.12) cannot be achieved in the context of (degenerate) object ensembles, the best possible decorrelation that can be achieved is

$$
\mathbf{O}^{*} \mathbf{O}=\mathbf{P}
$$

with $\mathbf{P}$, the projector to the PCA subspace (2.34). Then, the degenerate topographic family (cf. 4.26) is ${ }^{24}$

$$
\begin{aligned}
K^{(1)}=\mathrm{K} & =\sum_{r=1}^{N} \psi_{r}\left(\frac{1}{\sigma_{r}}\right)^{1}\left(\psi_{r},\right) \\
K^{(0)}=P & =\sum_{r=1}^{N} \psi_{r}\left(\frac{1}{\sigma_{r}}\right)^{0}\left(\psi_{r},\right) \\
K^{(-1)}=K^{(-1)} & =\sum_{r=1}^{N} \psi_{r}\left(\frac{1}{\sigma_{r}}\right)^{-1}\left(\psi_{r},\right)
\end{aligned}
$$

[^21]$$
\mathbf{K}^{(-2)}=\mathbf{R}=\sum_{r=1}^{N} \psi_{r}\left(\frac{1}{\sigma_{r}}\right)^{-2}\left(\psi_{r},\right)
$$
with a general member
$$
\mathbf{K}^{(n)}=\sum_{r=1}^{N} \psi_{r}\left(\frac{1}{\sigma_{r}}\right)^{n}\left(\psi_{r},\right) .
$$

With (4.29), given an example $\phi$, its topographic representation is (cf. 4.26)

$$
O=\mathbf{K} \phi=\mathrm{O}^{*} \Phi^{*+} \phi=\sum_{r=1}^{N} a_{r} \psi_{r}
$$

hence

$$
O(\mathbf{x})=(\hat{\mathbf{x}}, O)=\sum_{r=1}^{N} a_{r} \Psi_{r}(\mathbf{x})
$$

The output array $\{O(\mathbf{x})\}$ preserves all the information in the PCA coefficients $a_{r}$ (4.23)

$$
O^{*+} O=\Phi^{*+} \phi
$$

hence (cf. 2.47)

$$
a_{r}(O)=\left(\psi_{r}, O\right) .
$$

In practice, we rarely need $\left\{a_{r}\right\}$ explicitly; we reconstruct with $\mathbf{K}^{(-1)}$ (cf. 4.26). From (2.50)

$$
\phi=\mathbf{P}_{N} \phi=\Phi^{*} \Phi^{*+} \phi=\Phi^{*} \mathbf{O}^{*+} O=\mathbf{K}^{(-\mathbf{1})} O=\sum_{r=1}^{N} a_{r} \sigma_{r} \psi_{r}
$$

Since the truncated ensemble is degenerate, we are forced to accept a reconstruction error $\left\|\phi-\phi^{\text {rec }}\right\|^{2}$, as in the PCA case; it is exactly equal to that for the PCA representation and is given by $\left\|\phi_{\perp}(\mathbf{x})\right\|^{2}$, where $\phi_{\perp}(\mathbf{x})$ is the part of $\phi(\mathbf{x})$ that is orthogomal to the subspace spanned by the PCA basis. Hence, both representations share the same best reconstruction, generalization, and object constancy properties.

Having generalized the topographic representation (4.26) for degenerate ensembles of objects (4.29), and having discussed its properties in relation with the PCA representation, we proceed to study what it looks like for some object ensembles.

The results on Fig. 4.1 show K and P derived for Ensemble 1 2D images of hmman faces. Analogous results for Finsemble 2-3D surfaces of human heads are shown on Fig. 4.2. Since the results exhibit the same properties, we will discuss them together.

As we can see, the receptive fields develop compact support and are local. They are also strongly matched to the local features of the face. For example,

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-20.jpg?height=551&width=877&top_left_y=98&top_left_x=1037)
Figure 4.2: Receptive fields $\mathbf{K}$ and residual correlations $\mathbf{P}$ for surfaces of heads, Ensemble 2
positions: $\Psi_{1}$, the "average" of the examples, of Ensemble 2 (Appendix A.1), is marked with the respective positions $\mathrm{x}_{0}$ for $a e$.
$a-e$ : Five receptive fields $K\left(\mathbf{x}_{0}, \mathbf{y}\right)=\mathbf{K}_{\mathbf{x}_{\mathbf{0}}}(\mathbf{y})=\left(\mathbf{K}, \hat{\mathbf{x}}_{\mathbf{0}}\right)$ (cf. 4.25) (top row) and correlators $\mathbf{P}_{\mathbf{x}_{0}}(\mathbf{y})$ (bottom row) at the five choices for $\mathbf{x}_{0}$. The parameters are $V=8192, T=N=348$, and $n=0$ (see Fig. 4.1).
Note the weak bilateral symmetry on (c) and (e) (cf. 4.1c,e). Since Ensemble 2 was not symmetrized about $\theta=0$, the even-odd symmetry that was observed in (Kirby and Sirovich 1990) has not developed here.
Part of this figure is reproduced on Plate $1 D$.

a receptive field matched to a mouth develops at position 4.1a, a nose receptive field-at position 4.1b, and eyebrow, jaw-line, and cheek-bone receptive fieldsat positions $4.1 c, 4.1 d$ and $4.1 e$, respectively. The same results local feature receptive fields (for nose, forehead, eye, jaw-line, and cheekbone in $4.2 a, 4.2 b$, $4.2 c, 4.2 d$, and $4.2 e$, respectively)-are observed for input Ensemble 2. We should note that these are two very different input receptor spaces; the first is intensity samplings of photographic images ${ }^{25}$ of naturally rendered heads, the second is the radii (in millimeters) of surfaces of heads, before rendering, and with no albedo information. ${ }^{26}$ The fact that they develop conceptually similar

[^22]
## 69

receptive fields supports the theoretical understanding that the topographic extension to PCA captures the underlying structure of the input ensemble probability density, as PCA does, regardless of what the receptor space happens to be.

![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-20.jpg?height=688&width=879&top_left_y=1574&top_left_x=91)
Figure 4.1: Receptive Fields $\mathbf{K}$ and Residual Correlations $\mathbf{P}$ for Images of Faces, Ensemble 1
positions: $\Psi_{1}$, the "average" of the examples, of Ensemble 1 (Appendix A.1), is marked with the respective positions $\mathbf{x}_{\mathbf{0}}$ for $a \quad e$.
$a$-e: Five receptive flelds $K\left(\mathbf{x}_{0}, \mathbf{y}\right)=\mathbf{K}_{\mathbf{x}_{0}}(\mathbf{y})=\left(\mathbf{K}, \hat{\mathbf{x}}_{0}\right)$ (cf. 4.25) (top row) and correlators $\mathbf{P}_{\mathbf{x}_{0}}(\mathbf{y})$ (bottom row) at the five choices for $\mathbf{x}_{0}$. Low-pass noise filtering is performed with $F_{\mathrm{r}}=\frac{\sigma_{\mathrm{r}}^{2}}{\left(\sigma_{\mathrm{r}}^{2}+n^{2}\right)}$ so that $\mathrm{K}=\sum_{\mathrm{r}=1}^{N} \psi_{\mathrm{r}} \frac{F_{\mathrm{r}}}{\sigma_{\mathrm{r}}}\left(\psi_{\mathrm{r}},\right)$ (cf. 4.29). The parameters are $(T=1038, V=3840), N=400$, and $n=\sigma_{400}$. This results in the peak of the bandpass filter at $r=400$. The choice of $n$ was guided by our intuition about the amount of noise in the ensemble.
Part of this figure is reproduced on Plate $1 C$.

Note that the receptive fields that develop are not edge detectors in general; they are feature detectors, different from each other, and matched to the feature that is expected near their respective centers. Note also that the receptive fields have captured a correct symmetry-strong at the eyes, eyebrows and cheeks-which reflects the bilateral symmetry of human faces, and nonexistent at the outlines, which reflects the pose variability in the input ensembles. The symmetry is greater, and the receptive fields are more sharply defined, in Figure 4.2; the input ensemble there is better aligned and has less extrinsic variability.

The receptive fields for the examined ensembles happen to be mostly local, although locality was not imposed; the only imposed condition was topography, which, along with the simplistic fixing of the U symmetry (4.16), allowed the correlation function to manifest its local structure in the locality of the kernels. Indeed, wherever the correlations are not local as in the places of partial bilateral symmetry-the receptive fields turn out to be nonlocal as well.

Because the topographic representation (4.29) captures the local features of the investigated ensembles so well, we have decided to call it, by analogy with Principal Component Analysis, Local Feature Analysis (LFA).

The reconstruction power of the LFA outputs $O(\mathbf{x})$ for a given cutoff $N$ in (4.32) is exactly equal to that of the PCA representation (2.50) with the same cutoff. In order go gain some insight into the properties of $O(\mathbf{x})$, we have constructed the successive LFA outputs $O_{N}$ for the out-of-sample Example 1 (see Appendix A. 1 for definition), shown on Fig. 4.3. The test image was captured with a camcorder (linear gain control) as opposed to the photographic images ${ }^{27}$ of the ensemble used in deriving the representation. Also, the lighting conditions and the backgrounds are very different.

We note that the LFA outputs $O(\mathbf{x})$ (Fig. 4.3, top row) are very different from those given by edge detectors (Camy 1986). They are active at all places where the image deviates from the expectation of faces, not only at the edges, thus revealing the face-specific features of the example. This is in agreement with the representation of the probability of the example (4.22)-O(x) is large when the example deviates from the a priori expectation and is, therefore, improbable.

[^23]![](https://cdn.mathpix.com/cropped/4543005f-bb5d-4491-a9d4-2522beda47f5-21.jpg?height=281&width=870&top_left_y=91&top_left_x=107)
Figure 4.3: Successive LFA outputs in the cross-over regime of Ensemble 1

For Example 1 (Fig. 3.10-original), the successive LFA outputs (top) $O_{N}=\sum_{r=1}^{N} a_{r} F_{r, N} \psi_{r}$ (cf. 4.31) low-pass filtered (cf. Fig. 4.1) with $F_{\mathrm{r}, N}=\frac{\sigma_{\mathrm{r}}{ }^{2}}{\alpha_{\mathrm{r}}{ }^{2}+n_{\mathrm{N}^{2}}}, n_{N}=\sigma_{N}$, are labeled with the SNR of their respective reconstructions $\phi_{N}^{\text {rec }}$; the respective residual errors are $\phi_{N}^{\text {err }}$ (bottom) (cf. Fig. 3.12, Fig. 3.11).
$O_{N}$ is scaled adaptively at each $N$ as to fill the available dynamic range. The first two errors are magnified $5 x$ and the rest- $20 x$ (cf. Fig. 3.12). This figure is reproduced on Plate $1 E$.

Notably, the behavior of $O_{N}$ on Fig. 4.3 correlates well with the regimes of Ensemble 1, evident from the eigenmodes (Fig. 3.9), the successive reconstructions (Fig. 3.12), the $S-U$ diagram (Fig. 3.11), and the spectrum (Fig. 3.14): there is a rapid gain of identity information from $N \sim 60$ up to $N \sim 200$, gradual refinement up to $N \sim 500$, and incorporation of noise, thereafter. Evidently, up to $N \sim 300, O(\mathrm{x})$ is smooth, reflecting the identity of the person; more identity information is picked up to $N \sim 500$ at the expense of some noise, and noise is taking over identity thereafter.

### 4.4 Sparse-distributed from Topographic Representations

In Section 4.3 we showed how to generalize the topographic representation (4.26) to degenerate sensory ensembles. Applied to ensembles of objects, this generalization (4.29) discovered their local features, so we called it Local Feature Analysis (LFA).

The LFA outputs (4.32) have all the desirable representational properties of PCA (2.47-2.52), and are also local and topographic, making the receptive fields $\mathbf{K}_{\mathbf{x}}$ (Fig. 4.1) feasible candidates for biological implementation.

Unfortunately, there is one problem with the representational variables $\{O(\mathbf{x})\}_{\mathbf{x} \in V}$, namely there are too many of them $V$. This was not a problem

## 71

in the retinal case (Section 4.2); because of the translational symmetry, there were as many topographic variables, $V$, as there were PCA coefficients, $N$ (see discussion in footnote 16 on page 61). For degenerate ensembles, such as ensembles of objects, however, $N \ll V$, and one attractiveness of the global PCA representation-its low-dimensional parameterization (2.45), is lost. Moreover, the resulting variables are no longer decorrelated (4.12), but only "as decorrelated as possible" (4.28).

A solution to this problem was proposed by Penev and Atick (1996), which is based on the observation that the $V$ variables $\{O(\mathbf{x})\}_{\mathbf{x} \in V}$ are linearly dependent and can be described exactly with only $N$ free parameters.

One possible choice are the $N$ PCA coefficients $\left\{a_{r}\right\}_{r \in N}$ (4.32). Of course, calculating $\left\{a_{r}\right\}$ explicitly would require global operations, so we need a more suitable representation of the same information.

An alternative choice would be $N$ of the values of the LFA outputs $O(\mathbf{x})$ - restricted over a limited set of $N$ grid points $\left\{\mathbf{x}_{m}\right\} \equiv \mathcal{M},\left\{O_{m} \equiv O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$. Indeed, from (4.32) $O_{m}=\sum_{r=1}^{N} \boldsymbol{\Psi}_{r m} a_{r}$, with $\boldsymbol{\Psi}_{r m} \equiv \Psi_{r}\left(\mathbf{x}_{m}\right)$ an $N \times|\mathcal{M}|$ matrix. In the case $|\mathcal{M}|=N, \Psi$ is square and is, in general, invertible. Then, $a_{r}=\sum_{m} O_{m} \Psi^{-1}{ }_{m r}$; and (4.32)

$$
O(\mathbf{x})=\sum_{m=1}^{|M|} O_{m} a_{m}(\mathbf{x})
$$

with $a_{m}(\mathbf{x})=\sum_{r=1}^{N} \Psi_{m r}^{-1} \Psi_{r}(\mathbf{x})$. The low dimensionality of the LFA outputs is now explicit, and the PCA coefficients are not needed. Of course, there are the reconstructors $\left\{a_{m}(\mathbf{x})\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$ to worry about; they might turn out to be global. Nevertheless, there is considerable freedom in choosing $\mathcal{M}$, so one can hope to be able make a good choice.

Since the process of choosing a small number, $|\mathcal{M}|$, of values from the dense LFA outputs $O(\mathbf{x})$ effectively sparsifies the output, we will call it sparsification.

### 4.4.1 Static vs. Dynamic Sparsification

Even though, in principle, almost any $N$ points will be sufficient to recover $O(\mathbf{x})$, there are practical considerations in favor of their judicious choice. For example, if some points that are too close to each other in the sense that some are within the support of the correlators, $\mathbf{P}_{\mathbf{x}}$ (Fig. 4.1 4.2), of others the values $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{x_{m} \in \mathcal{M}}$ will be correlated, and the representation will be redundant. Moreover, the non-redundant information in $O_{m}$ will be carried by the least-significant digits, which would require extremely high precision of calculations and storage. This is wasteful in principle, and impractical in biology, where the available signal-to-noise ratio of the noisy neurous cannot be pushed very far.

One may be tempted to ask the question, If we are using only $N$ of the values of the LFA outputs, why at all calculate the rest $V-N \gg N$ ? Why not decide in advance which $N$ points we will be using and calculate only those outputs?

Such a strategy is possible; it will be called static sparsification, because it requires the choice of the grid points to be made once, for all examples that will be represented. In contrast, a strategy in which $O(x)$ is calculated densely, and the choice of $\mathcal{M}$ is made on an example-by-example basis, will be called dynamic sparsification.

With static sparsification, the judicious choice of $\mathcal{M}$ to avoid correlations is no longer needed; there are exactly $N$ outputs, and one can impose and satisfy their full decorrelation, instead of trying to satisfy (4.28). This is, indeed, possible and is equivalent to suitably fixing the U-symmetry (4.16) (see discussion in footnote 30 on page 75).

There is at least one objection to the pre-selection of $N$ points and the calculation of the LFA outputs only there, which is evident on Fig. 4.1-4.2. The receptive fields $\mathbf{K}_{\mathbf{x}}$ in the area of the chin, for example, are all "chin detectors" (4.2d). Since human heads have only one chin, for any given head $\phi$, the chin can be at only one location, $\mathbf{x}_{m}$, and only one chin detector, $\mathbf{K}_{\mathbf{x}_{m}}$, will detect a chin. The rest of them will be weakly activated, on the average, according to $\mathbf{P}_{x_{m}}$. For different examples, the location of the respective feature, chin, in this case, will vary, and the Iocation of the strongest activation of $O(\mathbf{x})$ will also vary. If all outputs $O(\mathbf{x})$ are calculated for an example $\phi$, then the choice of $O\left(\mathbf{x}_{m}\right)$, with $\mathbf{x}_{m}$, the exact location of the feature, is potentially very informative for subsequent processing steps. If, on the other hand, $\mathcal{M}$ has been pre-fixed, the chance is that the feature will be signaled with one of the peripheral values, in the weak activation regime.

From a numerical perspective, this will mean that the large value of $O\left(\mathbf{x}_{m}\right)$ at the peak will have to be estimated from a small value in the periphery, which will result in noise amplification. The flexibility in the choice of $\mathcal{M}$ on an example-per-example basis will allow the large value at the peak to be measured directly and the small values in the periphery to be estimated from it, which will result in noise attenuation.

Even more importantly, we speculated that in most object ensembles there are partial symmetries that camnot be captured by PCA. ${ }^{28}$ In the chin example above, this was the partial local translation symmetry of the chin. In general, most of the features can be slightly translated, mostly independently of each other, and the resulting object will still be in the eusemble. In Chapter 3 we referred to the inability of PCA to cope with this symmetry as the feature localization problem (see discussion on page 36); it was part of the motivation to develop LFA in the first place.
${ }^{28}$ Indeed, the assumption that the probability distribution $\mathcal{P}[\phi(\mathbf{x})]$ is joint-normal (2.2) is only a model; its validity has to be verified on a case-by-case basis. In Appendix A. 3 we show that the marginal distributions of the PCA coefficients for the ensemble of human faces deviate from normality.

## 73

We argued that the strategy to pre-fix the set of grid points $\mathcal{M}$ and restrict the evaluation of the LFA outputs only to them would preclude potentially valuable information about the locations of the features from being made apparent. Now, we return to the original proposal: for each example $\phi$, evaluate $O(\mathbf{x})$ everywhere; then, based on the results, choose a set of outputs $\left\{O\left(\mathrm{x}_{\mathrm{m}}\right)\right\}_{\mathrm{x}_{\mathrm{m}} \in \mathcal{M}}$; and, at last, reconstruct $O(\mathbf{x})$ using them.

Since, in different situations, there might be different criteria for the dynamic choice of $\mathcal{M}$, we will consider the reconstruction first, independently of the way $\mathcal{M}$ was chosen. Later in this section, we will propose one algorithm for choosing $\mathcal{M}$ that is suitable for serial calculation. Further, we will suggest how a similar algorithm may be implemented by a recurrent neural network, plausible for biological implementation. In Section 5.6 we will suggest another such algorithm, based on other design goals.

### 4.4.2 Reconstruction of One Simple Local Feature

In order to gain some insight into the reconstruction based on $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$, let us first consider a simpler problem. Given an example $\phi=\Phi^{*} \mathrm{~s}$ with, therefore, LFA outputs $O=\mathrm{O}^{*}$ s, we will try to reconstruct one simple local feature of the face, for example the chin (see discussion on page 73).

We will assume that we have already decided which grid point $\mathbf{x}_{m}$ to use, for example by looking around in the chin area and finding, at the grid point $\mathbf{x}_{m}$, the largest output of the "chin detectors" $O_{m}=O\left(\mathrm{x}_{m}\right)$; we will also assume that this feature is simple its location $\mathbf{x}_{m}$ and strength $O_{m}$ are all we need to reconstruct it.

We ask the question, What is the maximum likelihood estimate $O^{\text {rec }}(\mathbf{x})$ of $O(\mathbf{x})$ in the context of the probability distribution $\mathcal{P}[\phi(\mathbf{x})](2.2)$, which is consistent with the knowledge that the value of $O(\mathbf{x})$ at the location $\mathbf{x}_{m}$ is $O_{m} ?^{29}$

We note that $O_{m}=O\left(\mathbf{x}_{m}\right)=\left(\hat{\mathbf{x}}_{m}, O\right)=\left(\hat{\mathbf{x}}_{m}, \mathbf{O} * \mathrm{~s}\right)=\left\langle\mathbf{O} \hat{\mathbf{x}}_{m}, s\right)$; hence

$$
O_{m}=\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}\right\rangle
$$

with

$$
\mathbf{q}_{\mathbf{x}_{m}} \equiv \mathbf{O} \hat{\mathbf{x}}_{m} .
$$

This is an interesting observation-for every grid point $\mathbf{x}$, there is an associated vector $\mathrm{q}_{\mathrm{x}} \in S$, such that the calculation of $O(\mathrm{x})$ is equivalent to calculation of

[^24]the projection of $s$ on $\mathrm{q}_{x}{ }^{30}$
It is useful to decompose s into a sum of two parts-along $\mathbf{q}_{\mathbf{x}_{m}}$, and orthogonal to it: $\mathbf{s}=\mathbf{s}_{\|}+\mathbf{s}_{\perp}$. The projector to the direction of $\mathbf{q}_{\mathbf{x}_{m}}$ is
$$
\mathbf{Q}_{\mathbf{x}_{m}}=\frac{\mathbf{q}_{\mathbf{x}_{m}}\left\langle\mathbf{q}_{\mathbf{x}_{m}},\right\rangle}{\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{q}_{\mathbf{x}_{m}}\right\rangle}=\mathbf{p}_{\mathbf{x}_{m}}\left\langle\mathbf{q}_{\mathbf{x}_{m}},\right\rangle
$$
with
$$
\mathbf{p}_{x_{m}}=\frac{\mathbf{q}_{x_{m}}}{\left\langle\mathbf{q}_{x_{m}}, \mathbf{q}_{x_{m}}\right\rangle} .
$$
Note that
$$
\left\langle q_{x_{m}}, p_{x_{m}}\right\rangle=1
$$
and $\mathbf{Q}_{\mathbf{x}_{m}}{ }^{2}=\mathbf{p}_{\mathbf{x}_{m}}\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{p}_{\mathbf{x}_{m}}\right\rangle\left\langle\mathbf{q}_{\mathbf{x}_{m}},\right\rangle=\mathbf{p}_{\mathbf{x}_{m}}\left\langle\mathbf{q}_{\mathbf{x}_{m}},\right\rangle=\mathbf{Q}_{\mathbf{x}_{m}} ; \mathbf{Q}_{\mathbf{x}_{m}}$ is a projector indeed. With (4.39),
$$
\mathbf{s}_{\|}=\mathbf{Q}_{\mathbf{x}_{m}} \mathbf{s}=\mathbf{p}_{\mathbf{x}_{m}}\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}\right\rangle=O_{m} \mathbf{p}_{\mathbf{x}_{m}}
$$
hence $\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}_{\|}\right\rangle=O_{m}$. Then,
$$
\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}_{\perp}\right\rangle=\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}-\mathbf{s}_{\|}\right\rangle=\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}\right\rangle-\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{s}_{\|}\right\rangle=O_{m}-O_{m}=0 .
$$
From (4.42) and (4.40), $\mathbf{s}_{\|}=\alpha \mathbf{q}_{x_{m}}$ with $\alpha=\frac{O_{m}}{\left\langle\mathbf{q}_{x_{m}}, \mathbf{q}_{x_{m}}\right\rangle}$, hence $\left\langle\mathbf{s}_{\|}, \mathbf{s}_{\perp}\right\rangle=0$. Then
$$
\|\mathbf{s}\|^{2}=\left\|\mathbf{s}_{\|}\right\|^{2}+\left\|\mathbf{s}_{\perp}\right\|^{2}
$$
and $\mathcal{P}[\phi] \propto \exp \left\{-\frac{1}{2}\|\mathbf{s}\|^{2}\right\}(2.16)$ is largest when $\left\|\mathrm{s}_{\perp}\right\|^{2}=0\left(\mathrm{~s}_{\perp}=0\right)$. Hence, among all possible s , consistent with $O_{m}, \mathrm{~s}^{\text {rec }}=\mathrm{s}_{\|}$(4.42) has the largest probability and is, therefore, the maximum likelihood estimation.

Let us look back and understand what happened. To choose a point $\mathbf{x}_{m}$ means to choose a vector $\mathbf{q}_{\mathbf{x}_{\boldsymbol{m}}} \in S$, which spans a one-dimensional subspace $U_{\mathbf{x}_{m}} \subset S$, with a projector $\mathbf{Q}_{\mathbf{x}_{m}}$ (4.39). Then, the example $\mathbf{s}$ is a sum of two orthogonal parts: $\mathbf{s}_{\|} \in U_{\mathbf{x}_{m}}$ and $\mathbf{s}_{\perp} \in U_{\mathbf{x}_{m}}^{1}$, which can be determined independently of one another. To know the value of the measurement $O_{m}$ means to determine $\mathrm{s}_{\|}$(4.42). The contribution to $\mathrm{s}_{\|}$due to the measurement $O_{m}$ is a multiple of a vector $\mathbf{p}_{\mathbf{x}_{m}}$ (4.40) with a very special property (4.41). The knowledge of $O_{m}$ brings no information about $\mathrm{s}_{\perp} \in U_{x_{m}}^{\perp}$. To get the maximum likelihood estimation, we use the shortest possible vector $\mathrm{s}^{\mathrm{rec}} \in S$, which is achieved when $\mathrm{s}_{\perp}=0$.

Now, it is easy calculate the reconstructions of the LFA outputs

$$
O^{r e c}(\mathbf{x})=\left(\hat{\mathbf{x}}, \mathrm{O}^{*} \mathbf{s}^{r e c}\right) .
$$

${ }^{30}$ There are $V$ such projections, but, in general, only $N$ are needed to determine s. Prefixing $N$ of them is equivalent to pre-fixing $\mathcal{M}$. In general, those $N$ vectors, $\left\{\mathbf{q}_{\mathbf{x}_{m}}\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$, will not be orthogonal; one may orthogonalize them to get $\left\{\mathbf{o}_{\mathbf{r}}\right\}_{r \in N}$ (cf. 4.15). This treatment is equivalent to a particular fixing of the U-symmetry (4.16).

From (4.42) and (4.40),

$$
O^{r e c}(\mathbf{x})=O_{m}\left(\hat{\mathbf{x}}, \mathbf{O}^{*} \mathbf{p}_{\mathbf{x}_{m}}\right)=\frac{O_{m}}{\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{q}_{\mathbf{x}_{m}}\right\rangle}\left(\hat{\mathbf{x}}, \mathbf{O}^{*} \mathbf{q}_{\mathbf{x}_{m}}\right)
$$

From (4.38) and (4.28),

$$
\left(\hat{\mathbf{x}}, \mathbf{O}^{*} \mathbf{q}_{\mathbf{x}_{m}}\right)=\left(\hat{\mathbf{x}}, \mathbf{O}^{*} \mathbf{O} \hat{\mathbf{x}}_{m}\right)=\left(\hat{\mathbf{x}}, \mathbf{P} \hat{\mathbf{x}}_{m}\right) \equiv\left(\hat{\mathbf{x}}, \mathbf{P}_{\mathbf{x}_{m}}\right) \equiv P_{\mathbf{x}_{m}}(\mathbf{x}) .
$$

Notably, $P_{\mathbf{x}_{m}}(\mathbf{x})$ is the correlation between the output $O\left(\mathbf{x}_{m}\right)$ of the receptive field centered at $\mathrm{x}_{m}$ and the rest of the LFA outputs $O(\mathrm{x})$.

With (4.47) $\left\langle\mathbf{q}_{\mathbf{x}_{m}}, \mathbf{q}_{\mathbf{x}_{m}}\right\rangle=\left\langle\mathbf{O} \hat{\mathbf{x}}_{m}, \mathbf{q}_{\mathbf{x}_{m}}\right\rangle=\left(\hat{\mathbf{x}}_{m}, \mathbf{O}^{*} \mathbf{q}_{\mathbf{x}_{m}}\right)=P_{\mathbf{x}_{m}}\left(\mathbf{x}_{m}\right) ;$ hence

$$
O^{r e c}(\mathbf{x})=O_{m} a_{\mathbf{x}_{\mathrm{wa}}}(\mathbf{x})
$$

with $a_{\mathrm{x}_{m}}(\mathrm{x})$, the reconstructor based on the grid point $\mathrm{x}_{m}$,

$$
a_{\mathbf{x}_{m}}(\mathbf{x})=\frac{P_{\mathbf{x}_{m}}(\mathbf{x})}{P_{\mathbf{x}_{m}}\left(\mathbf{x}_{m}\right)} .
$$

This is a very reasonable result-the magnitude of the reconstruction $O^{\text {rec }}(\mathbf{x})$ on the basis of the magnitude $O_{m}$ measured at the grid point $\mathrm{x}_{m}$ is proportional to $O_{m}$, which depends on the example $\phi$. The $\mathbf{x}$ dependence $a_{m}(\mathbf{x})$ of the reconstruction, however, is the decaying correlation $P_{\mathbf{x}_{\boldsymbol{m}}}(\mathbf{x})$ (cf. Fig. 4.1- 4.2), normalized so that its peak value is one, and is dependent only of the choice of $\mathbf{x}_{\boldsymbol{m}}$. Note the perfect reconstruction at $\mathbf{x}_{m}, O^{r e c}\left(\mathbf{x}_{m}\right)=O_{m}$, which was guaranteed by the requirement $\left\langle\mathrm{q}_{\mathrm{x}_{\mathrm{m}}}, \mathrm{s}^{\text {rec }}\right\rangle=O_{m}$ (4.42).

For the reconstruction of the example itself he have (cf. 4.45),

$$
\phi^{r e c}(\mathbf{x})=\left(\hat{\mathbf{x}}, \Phi^{*} \mathbf{s}^{r e c}\right)
$$

hence, analogously (cf. 4.48),

$$
\phi^{r e c}(\mathbf{x})=O_{m} \frac{K^{(-1)} \mathbf{x}_{m}(\mathbf{x})}{P_{\mathbf{x}_{m}}\left(\mathbf{x}_{m}\right)}
$$

with $K^{(-1)}{ }_{x_{m}}(x)=\left(\hat{x}, K^{(-1)} x_{m}\right)$, the $\phi$-reconstructor (4.29) (cf. 4.47).
We have come to an interesting result the LFA representations of the maximum-likelihood estimates $O^{\text {rec }}(\mathbf{x})$ (4.48) and $\phi^{\text {rec }}(\mathbf{x})$ (4.51) use only the topographic operators (4.29), which, we argued, are local.

Indeed, the LFA kernels for the ensembles we have studied-human faces (Fig. 4.1) and heads (Fig. 4.2)-are local. Therefore, the reconstruction (4.48-4.49) on the basis of the location and the strength of one simple feature will be non-vanishing only in its neighborhood and will not contribute to the re-construction of distant regions, as is evident from $\mathbf{P}_{\boldsymbol{x}}$ (bottom row of Fig. 4.1-4.2). ${ }^{\text {al }}$

[^25]
### 4.4.3 Full LFA Reconstruction

From the discussion so far, we have learned how to reconstruct a localized portion of an example $\phi$. We now ask the question, How to reconstruct the whole example?

One possible idea is to look for the reference locations of all simple features by, say, looking for the local peaks in $O(\mathbf{x})$, reconstruct each of them using (4.48-4.49), and add the results together.

This approach has a potential problem-the reconstructor based on $\mathrm{x}_{m}$, $a_{\mathbf{x}_{m}}(\mathbf{x})$ (4.49), will have nonvanishing contributions to the reconstructions at all other reference locations that fall in its support. This will result in $O^{\text {rec }}\left(\mathbf{x}_{m}\right) \neq$ $O_{m}$-a reconstruction that, at the reference locations $O^{r e s}\left(\mathrm{x}_{m}\right)$, is inconsistent with the measurements $O_{m}$.

One possible approach is to choose each new reference location outside the support of all the others. Unfortunately, the individual reconstructors $a_{\mathrm{x}_{\mathrm{m}}}(\mathrm{x})$ are too wide for that. Indeed, $a_{\mathbf{x}_{m}}(\mathbf{x})$ provides the expectation of the value of $O(\mathbf{x})$, based on the knowledge of $O\left(\mathbf{x}_{m}\right) ; O(\mathbf{x})$ itself will be sometimes smaller, sometimes larger. The square of the standard deviation of $O^{\text {rec }}(\mathbf{x})-O(\mathbf{x})$ at the grid point $\mathbf{x}$ is provided by $P(\mathbf{x}, \mathbf{x})-P\left(\mathbf{x}_{m}, \mathbf{x}\right) .{ }^{32}$ Hence, when $a_{\mathbf{x}_{m}}(\mathbf{x})=50 \%$ - well within the support-the error in the estimate of $O(\mathbf{x})$ will be of the order of the estimate itself. Two options are available: either tolerate such large errors, or add a new reference point and produce an error on the order of 50\% in $O\left(\mathbf{x}_{m}\right)$; both are unacceptable.

By now, we have developed some intuition into what is at stake: the reconstructor $a_{\mathbf{x}_{\mathrm{m}}}(\mathbf{x})$ (4.49) had the nice property, that its value was 1 at the reference point $\mathbf{x}_{\boldsymbol{m}}$; the problem is that its value will be, in general, nonvanishing at all other reference points. This is natural; when deriving it, we did not know what other reference point there were, and we did not impose any additional conditions besides (4.41).

We will proceed to impose such conditions and derive more clever reconstructors that not only have a value of 1 at their respective reference points, but also have a value of 0 at all the other reference points; we will interpolate $O(\mathbf{x})$ with the values in $\left\{O\left(\mathrm{x}_{m}\right)\right\}_{\mathrm{x}_{m} \in \mathcal{M}}$.

It is obvious that the new reconstructors will have to depend on all points in $\mathcal{M}$ together. Indeed, suppose we want to add a new reference point, $\mathrm{x}_{\mathrm{m}}$, to $\mathcal{M}$. On the basis of the old $\mathcal{M}$, we knew the expectation and the variance at $\mathbf{x}_{m}$. When we add $O\left(\mathrm{x}_{m}\right)$, this changes both of them, hence the old estimates are no longer valid.

We will consider solving the recoustruction problem for a given $\mathcal{M}$ as a
${ }^{32}$ Indeed, having fixed $\mathbf{s}_{\|}$(4.42), we still know nothing about $\mathbf{s}_{\perp}$. The projector to $U_{\mathbf{x}_{m}}^{\perp}$ is $\mathbf{P}_{\perp}=\mathbf{O}^{\boldsymbol{N}} \mathbf{O}-\mathbf{Q}_{\mathbf{x}_{\boldsymbol{m}}}$, hence the conditional ensemble defined by it generates a variance at the grid point $\mathbf{x}$, whose square is $\left\langle\mathbf{O} \hat{\mathbf{x}}, \mathbf{P}_{\perp} \mathbf{O} \hat{\mathbf{x}}\right\rangle=P(\mathbf{x}, \mathbf{x})-P\left(\mathbf{x}_{m}, \mathbf{x}\right)$.

77
whole. Analogously to the treatment in Section 4.4.2, we define (cf. 4.38)

$$
\mathbf{q}_{m} \equiv \mathbf{q}_{\mathbf{x}_{m}}=\mathbf{O} \hat{\mathbf{x}}_{m} .
$$

For each example $\phi$, we interpret the set of measurements $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$ as the $|\mathcal{M}|$ projections of $\Phi^{*+} \phi$ to the vectors (4.52) $\left\{\mathbf{q}_{m}\right\}_{x_{m} \in \mathcal{M}}$ (4.37); those vectors span a subspace $U_{\mathcal{M}} \in S$. Again, we want to decompose $\mathbf{s}$ as a sum of $\mathrm{s}_{\|} \in U_{\mathcal{M}}$ and $s_{\perp} \in U_{\mathcal{M}}^{\perp}$.

For $\mathbf{s}_{\|}$, we need a basis of $U_{\mathcal{M}},\left\{\mathbf{p}_{i}\right\}_{i=1}^{|\mathcal{M}|}$, which is some linear combination of $\left\{\mathrm{q}_{m}\right\}_{x_{m} \in \mathcal{M}}$ :

$$
\mathbf{p}_{l}=\sum_{n=1}^{|M|} \mathbf{B}_{l n} \mathbf{q}_{n} .
$$

There might be many possible criteria for choosing a basis for $U_{\mathcal{M} i}$ an orthogonal basis is one such possibility. ${ }^{39}$ Analogously to (4.41), we choose, uniquely, the reciprocal, or dual, basis with the condition

$$
\left\langle\mathbf{q}_{m}, \mathbf{p}_{i}\right\rangle=\delta_{m, i} .
$$

This is a reasonable condition, since, we will see, it guarantees interpolating reconstructors. ${ }^{34}$ With (cf. 4.42) we define

$$
\mathbf{s}_{| |}=\sum_{m=1}^{M \mid} O_{m} \mathbf{p}_{m}
$$

and calculate its projections to $\left\{\mathbf{q}_{m}\right\}_{\mathbf{x}_{m} \in \mathcal{M}}$

$$
\left\langle\mathbf{q}_{m}, \mathbf{s}_{\|}\right\rangle=\sum_{l=1}^{|\mathcal{M}|} O_{l}\left\langle\mathbf{q}_{m}, \mathbf{p}_{l}\right\rangle=\sum_{l=1}^{\mathcal{M} \mid} O_{l} \delta_{m l}=O_{m}=\left\langle\mathbf{q}_{m}, \mathbf{s}\right\rangle
$$

hence, for $\mathrm{s}_{\perp}=\mathrm{s}-\mathrm{s}_{\|}$(cf. 4.43),

$$
\left\langle\mathbf{q}_{m}, \mathbf{s}_{\perp}\right\rangle=\left\langle\mathbf{q}_{m}, \mathbf{s}-\mathbf{s}_{\|}\right\rangle=\left\langle\mathbf{q}_{m}, \mathbf{s}\right\rangle-\left\langle\mathbf{q}_{m}, \mathbf{s}_{\|}\right\rangle=O_{m}-O_{m}=0 .
$$

Since $\mathrm{s}_{\|}$is a linear combination of $\left\{\mathrm{p}_{\mathrm{m}}\right\}_{\mathrm{x}_{\mathrm{m}} \in \mathcal{M}}$, which are themselves linear combinations of $\left\{q_{m}\right\}_{x_{m} \in \mathcal{M}}, s_{\|}$is a linear combination of $\left\{q_{m}\right\}_{x_{m} \in \mathcal{M}}$, and,

[^26]
[^0]:    ${ }^{3}$ For a recent review of all these techniques see (Deco and Obradovic 1996).
    ${ }^{4}$ PCA has also been utilized, albeit implicitly, in the redundancy-reducing factorial codes described in Section 4.2, where it can be identified as their first step.

[^1]:    ${ }^{2}$ We have to note here, that although redundancy reduction at the retinal and LGN stages does produce a decorrelated representation, it does not reduce the dimensionality, the mathematical reason being that the correlation matrix of the translationally symmetric ensemble of natural images is non-degenerate-a point that we will return to several times during this Thesis.

[^2]:    ${ }^{5}$ The term "symmetry breaking" has a firmly established meaning when used in the con text of Statistical Mechanics: it denotes a situation, whereby although the laws of Physics described by the the Hamiltonian $H$ obey some symmetry, nevertheless the state of the system $\phi(x)$ is not symmetric. We will resist the temptation to offer an analogy with certain aspects of LFA until Section 5.4.

[^3]:    ${ }^{1}$ These 100 distinct levels refer to the output voltage of the photo receptors, whose gain control continuously adapts to the overall light level in a non-trivial manner. The interior of the photo receptor cell has information about the light intensity, in the form of the number of isomerized retinoic acid molecules per unit time, which is quantized to a number of levels, at least a couple orders of magnitudes bigger. One can argue that even the 5 Gbytes/sec data rate is not of the input signal itself, but of its representation after its first stage of processing.
    ${ }^{2}$ In the most restrictive treatment, $\{x\}$ is considered a discrete set with a finite number of $V=|\{x\}|$ elements. Whenever in doubt about the exact mathematical definition, the reader

[^4]:    should have this in mind.
    Nevertbeless, many of the facts of Linear Algebra of finite-dimensional vector spaces that we rely on are meaningfully expendable to infinite-dimensional spaces, to a varying degree to ones with countable and uncountable bases. Most of the observable results of this Thesis do not depend explicitly on $|\{x\}|$ and, in general, the reader can relax the rigor and develop an intuition about $V$ being the volume of the system.
    ${ }^{3}$ By "topography" we mean that some grid points in $\{\mathbf{x}\}$ are somehow "close" to each other, either spatially, temporally, both, or in any other way. For the moment, we shy away from the mathematically loaded term topology, keeping our options open on saying what "topography" means. Nevertheless, "topography" will play a central role in understanding the limitations of PCA.
    ${ }^{4}$ In the restrictive trestment (footnote 2 on page 10), $\{x\}$ is a discrete finite sampling of the time axis.
    ${ }^{5}$ This is easily illustrated by turning on an older TV set and tuning it to a channel with no broadcast program. The resulting randomly dancing dots in space and time are a very valid example $\phi^{\text {random }}(\mathbf{x})$ in the sense that the light intensity and color values fall within an acceptable range at all places of the receptor grid $\{\mathrm{x}\}$. Navertheless, it is not a "natural" stimulus: the probability $\mathcal{P}\left[\phi^{\text {random }}(x)\right]$ of it occurring "naturally" in a broadcast program-is very low.
    ${ }^{6}$ Consider the following example. For a the problem of face representation and recognition we have used the smallest possible number of points of the receptor grid that still gives us reasonable subjective discrimination of identities- $V=60 \times 64 \approx 4000$. If any of the 4000

[^5]:    ${ }^{9}$ We wish to thank Prof. M. J. Feigenbaum for the suggestion of this clarifying language that makes the presentation somewhat transparent. The treatment in this and the next Sections are based on (Feigenbaum 1997), which we chose to include because we have not seen a similar treatment in the literature.
    ${ }^{10}$ Here $\mathcal{R}$ is the range of possible receptor readouts, which we assume can be any real number. In practice, the values of the readouts are bounded from both above and below, and, because of the presence of noise in their measurement, only values separated by some finite difference are meaningful; hence, $\mathcal{R}$ can be the set of some finite number of discrete states. For our favorite ensemble the luminosity values were discretized to 256 grayscale levels.

    Nevertheless, it is convenient to consider that the "true" receptor values are in the field of the real numbers, but are tainted by discretization noise-this way all the machinery of linear algebra of vector spaces can be applied to $\mathcal{R}^{V}$.

[^6]:    ${ }^{11}$ The object $\cos ^{2}\left(\phi, \phi^{\prime}\right)=\frac{\left|\left(\phi, \phi^{\prime}\right)\right|^{2}}{(\phi, \phi)\left(\phi^{\prime}, \phi^{\prime}\right)}=\frac{\left|\left(\phi, \phi^{\prime}\right)\right|^{2}}{\|\phi\|^{\prime}\left\|\phi^{\prime}\right\| v} \in[0,1]$ is the normalized comelator of $\phi$ and $\phi$. It has found extensive use in pattern recognition algorithms.
    ${ }^{12}$ We note that the adjoint of $\Phi^{*}$ is $\Phi$ itself, $\left(\Phi^{*}\right)^{*}=\Phi$. Indeed, $\left\langle\mathbf{s},\left(\Phi^{*}\right)^{*} \mathbf{u}\right\rangle=\left(\Phi^{*} \mathbf{s}, \mathbf{u}\right)$ by the definition of what adjoint means and from (2.11) we see that this value is also equal to $\langle\mathbf{s}, \Phi \mathbf{u}\rangle$, so $\langle\mathbf{s}, \Phi \mathbf{u}\rangle=\left\langle\mathbf{s},\left(\Phi^{*}\right)^{*} \mathbf{u}\right\rangle$ for all $\mathbf{s}$ and $\mathbf{u}$, therefore $\left(\Phi^{*}\right)^{*}=\Phi$.

    13
    The action of $\Phi$ on the unit vector $\hat{\mathbf{x}}$ associated with the grid point $\mathbf{x}$ is the sequence in "sampling time" of the values of the receptor activation at that grid point; that gives a tangible meaning to (2.7)-the expansion in the $\{t\}$ basis of a vector $\mathrm{s} \in S$ is the evolution in "sampling time" of the value of some (suitably defined) measurement in the physical space. Now, suppose that we are following two such evolutions-of the receptor readouts at the two grid points $\mathbf{x}$ and $\mathbf{y}$, given by $\Phi \hat{\mathbf{x}} \in S$ and $\Phi \hat{\mathbf{y}} \in S$, respectively. The inner product on $S$

    $$
    \langle\Phi \hat{\mathbf{x}}, \Phi \hat{\mathbf{y}}\rangle=\frac{1}{T} \sum_{t} \phi^{t}(\mathbf{x}) \phi^{t}(\mathbf{y})
    $$

    can be understood as the correlation between those two measurements. ${ }^{13}$
    We can understand $\Phi^{*} \hat{t}$ as the sampling operator

    $$
    \Phi^{*} \hat{t} \equiv \mathbf{1}_{U} \Phi^{*} \hat{t}=\frac{1}{V} \sum_{\mathbf{x}} \hat{\mathbf{x}} \phi^{t}(\mathbf{x})=\phi^{t} .
    $$

    This is remarkable, and will be used extensively throughout this Thesis-the basis vectors $\hat{t} \in S$ correspond to the respective examples drawn from the input ensemble.

    Now, any vector $s \in S$ is a linear combination of the basis in $S$, with $\Phi^{*} \mathrm{~s} \in U$, the corresponding linear combination of examples (receptor activation patterns). Therefore, the action of $\Phi^{*}$, defined by the sampling $\Phi$, can generate all activation patterns that are linear combinations of the reference examples.

    The motivation behind PCA is that, since the examples $\left\{\phi^{t} \equiv \Phi^{*} \hat{t}\right\}_{t=1}^{T}$ are drawn at random from the probability density $\mathcal{P}[\phi(\mathbf{x})]$, then, lacking any other considerations, their probabilities $\left\{\mathcal{P}\left[\Phi^{*} \hat{t}\right]\right\}$ should be considered equal. ${ }^{14}$ PCA

[^7]:    ${ }^{21}$ In this notation, the earlier remark about the in-sample effect is transparent-as long as there aren't enough reference examples, the basis vectors $\{t\}$ are inside the eigenspace $\left(\mathbf{P}^{\prime} \hat{t}=\hat{t}\right)$, and PCA erroneously assigns them the same probability (density); once the statistics in $\Phi$ grow sufficiently ( $T$ grows), $\{t\}$ are, in general, outside the eigenspace, whose them closer to their "best" places $\mathbf{P}^{\prime} \hat{t} \in S$.

[^8]:    ${ }^{23}$ For discrete finite $V$ or $T$, as well as in some other cases, this is possible.

[^9]:    ${ }^{1}$ We chose it for several reasons: it is publicly available; there are no limitations on showing its subjects in publications; and, finally, it is small enough to be reproduced in full in a publication like this (Fig. A.1).
    ${ }^{2}$ Glasses are a very strong feature that can wash away much of the intrinsic variability of the ensemble accoss most of the interesting part of the face, therefore we will try to avoid them as much as we can. Interestingly, they are also perceptually very strong.

[^10]:    ${ }^{3}$ In all ensembles in this Thesis, unless explicitly noted otherwise, we have broken the translation, scale, and rotation symmetry by manually pinpointing the locations of the two eyes. An affine transformation of the plane has then been applied to place the eyes symmetrically with respect to the vertical axis and 28 pixels apart. We note that one pixel variation in the eye location, therefore, is responsible for variations of two to three pixels on the periphery borizontally, and up to four pixels vertically for ensembles like full (see Appendix A. 1 for definition). This is a "natural" variation of the ensemble we cannot expect to break the symmetry any better than this way.
    ${ }^{4}$ Also, inter-eye distance has been considered by Sirovich and Kirby (1987).

[^11]:    ${ }^{8}$ We will find good use for such S-U diagrams in Section 5.2.

[^12]:    ${ }^{9}$ Indeed, we defined $\mathcal{P}[\phi(\mathbf{x})]$ as the probability density around $\phi$. To get to probabilities, and, from there, to information in bits, we need to decide how finely we want to chop the receptor activation space.

    The situation is very similar to the decision where to truncate the decimal representations of real numbers-a single number can contain a lot of information if we decide to keep for it a lot of decimal digits (currently, one can fill pages, even whole books with the decimal representation of numbers such as e and $\pi$ ).
    ${ }^{10}$ Another interesting possibility is that the receptor activation pattern is due to more than one underlying reason, for example, a face with a tattoo on the cheek. In such a case, the tattoo will not be explained very well in the context of faces, and truncating the face representation sarly will leave the tattoo in the error signal, therefore opening the possibility for it to be represented efficiently in the context of an ensemble of tattoos. The idea of the error signal of one representation serving as the input signal for another takes us to the discussion of active blackboards (Mumford 1991; Mumford 1992) and we will return to it in Section 5.3.
    ${ }^{11}$ Although $\mathbf{\Psi}_{14}$ can be recognized as the "Richard Nixon" mode, none of the examples in Ensemble 1 is an image of Richard Nixon; $\Psi_{14}$ does not capture the identity of an example, but rather, a global feature, from which identities are built.

[^13]:    ${ }^{12}$ An obvious idea would be to create a new ensemble by re-centering by, say, the "tip of the nose," re-do the PCA analysis on it to get a sharper picture in that region, and somehow "glue" both of them together.
    This idea was circulated for a while in our work on 3D surfaces of heads, which came with about 20 markings each of anatomically very well defined characteristic skull points which were determined by a doctor after manual examination of the skulls of the subjects. With the current technology though, it would not be very easy to extract their location automatically

[^14]:    ${ }^{18}$ Of course, one can always truncate (2.50) early and leave substantial amount of pixel power out (Turk and Pentland 1991), but then the results have to be interpreted carefully in light of the discussion in Appendix A.2.

[^15]:    ${ }^{20}$ Note that $F_{r}^{s a m e}$ and $F_{r}^{d i f f}$ are not symmetric their variables are squares of variables with symmetric distributions peaked at 0, so they are also peaked at 0, and the means do not have maximum probabilities.

[^16]:    ${ }^{24}$ We defined "genuine" as the modes in the power-law regime of the spectrum (see discussion on page 40)). Arguably, almost all of the spectrum for Ensemble 4, shown on Fig. 3.22, is in the power-law regime. Therefore, almost all information is "genuine" for this ensemble it has a much higher underlying dimensionality. This is expected, since we argued that even one localization parameter can generate many eigenmodes via the feature-localization problem (Fig. 3.9, also Fig. 5.1).
    ${ }^{25}$ One is tempted to hypothesize that the performance PCA for classification of faces is

[^17]:    ${ }^{2}$ Rieke, Warland, de Ruyter van Steveninck, and Bialek (1997) review the information transmission in the sensory systems of several lower organisms and find the information capacity of the respective axons in the 1001000 bits/sec range. The axons in the optic nerve spike with a frequency of ~ 150 Hz, which, for 1000 bits/sec, is ~ 6 bits/spike-about the maximum Rieke et al. (1997) describe. Even if the 1 Gbytes/sec estimate misses the correct value somewhat, we feel that it would be no more than a factor of 2 in either direction.
    ${ }^{3}$ In terms of the earlier analogy (see discussion in footnote 6 on page 10), if one wants to measure 64 bits (8 bytes) for each value-something that we routinely did for the ensembles discussed in Chapter 3, one needs 8,00018 GB diaks, worth about USD 10,000,000- definitely within the reach of certain agencies of the USA Federal and other Governments, but still implausible for single organisms.
    ${ }^{4}$ The function $r(\Delta \mathbf{x})$ is usually called the autocorrelation function of the ensemble.

[^18]:    ${ }^{9}$ See footnote 7 on page 57.
    ${ }^{10}$ One question that comes to mind is, How can we ship to the LGN, over the $1,000,000$ axons of the optic nerve, 6 times as many values? This is somewhat akin to the question, How can we ship to London, over only one telegraphic sub-Atlantic cable, as many values as the different prices on the New York Mercantile Exchange? The answer was given by Samuel F. B. Morse and is called channel coding (Shannon and Weaver 1949). It says that, whatever the nature of the transmitted variables, they have to be encoded into channel symbols that are optimally matched to the properties of the transmission medium.
    Then, What is the channel code of the retina? Meister (1996) has recorded simultaneously from multiple ganglion cells in a salamander retina preparation. Surprisingly, he finds that action potentials traveling over different axons are not at all independent for any given action potential on a given axon, there are a few action potentials generated almost exactly at the same time in neighboring axons, lending support to the idea that they are coming from some other "activity" After careful analysis of which action potential belongs to which "activity," he finds that there are about five times as many "activities" as ganglion cells, which he speculates to be coming from amacrine cells. When he analyzes the receptive fields of the "activities," he finds them much sharper, well-defined and selective (spatially, temporally, and chromatically) than those of the ganglion cells; obviously.

    This comes to illustrate that, in the salamander's retina at least, there is an attempt to utilize the optic nerve efficiently. Also, it comes to say that there is danger in interpreting the results of single-unit recordings in cells that generate long-distance action potentials.

    Now, If the ganglion cells are just channel coders for the "amacrines," what is the nature of the "amacrine" coding? We will suggest a possibility in Section 5.6.
    ${ }^{11}$ Indeed, the only coefficients that need to be measured and stored are $\sigma_{\mathrm{f}}$, of which there are relative few (see discussion in footnote 6 on page 57). Moreover, since the $\sigma_{\mathbf{f}}$ dependence on $|f|$ (4.4) is so regular, the only "experimental" parameter is $\alpha$, and it is feasible that it can be determined through the species' evolution and stored in their genetic material. Indeed, in primates, the retina develops almost fully in uterm (Shatz 1996), without the need for visual stimulation.
    ${ }^{12}$ See footnote 3 ori page 56.

[^19]:    ${ }^{17}$ In practice, one should also include noise filtering, since the process of whitening by multiplying by $1 / \sigma_{r}$ (2.47) amplifies both signal and noise. Whereas the power of the signal decreases with $r$, the power of the noise remains constant. The whitening factor is most significant in the regime of small values of $\sigma$-precisely where the signal to noise ratio is small. In order to fight noise amplification, one should multiply additionally by a low-pass noise filter; then the resulting factor will be effectively a band-pass filter in the eigenmode number $\tau$; it will attenuate the power for small $r$ (high $\sigma$ ) as well as high $r$ (small $\sigma$ ) and amplify it for intermediate values of $r$ very much like the contrast sensitivity curves encountered in (Atick and Redlich 1992).

    The exact form of the optimal bandpass filter can be derived only after a specific model of the noise is adopted.
    ${ }^{18}$ We argued that, in the general context of PCA, inverses are not guaranteed to exist; this forced us to relax the requirements to (2.18-2.19). In fully-symmetric ensembles, such as the retinal, the PCA $U$-subspace necessarily spans the whole $U$ (see discussion in footnote 16 on page 61), and an exact inverse can be achieved.

[^20]:    ${ }^{21} \mathbf{K}^{2} \equiv \mathbf{R}^{-1}$ is conspicuously missing. In the Engineering literature it is called Differential Pulse Code Modulation (DPCM) (Gonzalez and Woods 1992). We speculate that it is suboptimal; its construction would require $\Phi^{+}=\sum_{\mathbf{f}} \mathbf{\Psi}_{\mathbf{f}} \frac{1}{\sigma_{\mathbf{f}}}\left(\mathbf{日}_{\mathbf{f}},\right)$, for which we haven't found any meaning so far. We speculate that, in general, $\mathbf{K}^{1}$ should be used instead of $\mathbf{K}^{2}$. We discuss the relation between DPCM and LFA in Section 5.6.1.

[^21]:    ${ }^{24}$ In the context of object ensembles, with reduced dimensionality, there is no genuine inverse, and the operators are not real powers of $\mathbf{K}$; they are just labeled with the respective index.

[^22]:    ${ }^{25}$ The photographic film has a logarithmic response to light intensity.
    ${ }^{26}$ The transformations back and forth those two spaces are highly non-linear. The trans-

[^23]:    formation from surfaces to images is called rendering; the addition of the albedo information, texture mapping. This is a problem of computer graphics and has been solved adequately only recently. The transformation from images to surfaces is the shape-from-shading problem; it is a long-standing problem of Artificial Intelligence and has not been solved satisfactory so far (Atick et al. 1996a).
    ${ }^{27}$ See footnote 25 on page 69.

[^24]:    ${ }^{29}$ Notably, no useumptions have been made about a particular criterion for the selection of $\mathcal{M}$ so far; hence, in the discussion that follows, no information aside from $\mathbf{x}_{m}$ and $O_{m}$ will be used.

    Such information will be available for any specific selection criterion and should, in general, be utilized to improve the naïve reconstructions. For example, if $\mathrm{x}_{\mathrm{m}}$ is at a local maximum of $O(\mathbf{x})$, the information that the neighboring values of $O(\mathbf{x})$ are less than $O_{m}$ is valuable. Such a possibility is explored in Section 5.6.

[^25]:    ${ }^{31}$ The LFA kernels on Fig. 4.1-4.2 have nonvanishing values everywhere. This can be attributed to the small statistics of the respective ensembles; indeed, for ensembles with better statistics, the supports of the LFA kernels are much more confined (Fig. 5.4).

[^26]:    ${ }^{33}$ There are many possible orthogonal bases; advancing a criterion for choosing one of them goes into the direction of fixing the U-symmetry (see discussion in footnote 30 on page 75). Also, it is always possible to treat $\left\{\mathbf{q}_{\mathbf{x}}\right\}_{\mathbf{x}_{\mathbf{m}} \in \mathcal{M}}$ as examples in some ensemble and find the respective PCA basis, which will be uniquely determined. One possible objection would be that the set $\left\{\mathbf{q}_{\mathbf{x}}\right\}_{\mathbf{x}_{\boldsymbol{\ldots}} \in \boldsymbol{\mathcal { M }}}$ comes from a single example $\phi$ and changes on an example-byexample basis-a meaningful ensemble interpretation would be difficult,
    ${ }^{34}$ Why interpolating? one might ask, Why not approximating? This is a valid question-in practice, we never know $\left\{O\left(\mathbf{x}_{m}\right)\right\}_{\mathbf{x}_{m} \in M}$ exactly, so approximation might not be such a bad idea. We will entertain it for a while in Section 5.6.


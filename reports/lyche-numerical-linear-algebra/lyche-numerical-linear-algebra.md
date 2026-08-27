![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-001.jpg?height=500&width=1166&top_left_y=59&top_left_x=176)

Tom Lyche

# Numerical Linear Algebra and Matrix Factorizations 

Editorial Board

T. J. Barth<br>M. Griebel<br>D. E. Keyes<br>R. M. Nieminen<br>D. Roose<br>T. Schlick

# Texts in Computational Science and Engineering 

22

Editors

Timothy J. Barth<br>Michael Griebel<br>David E. Keyes<br>Risto M. Nieminen<br>Dirk Roose<br>Tamar Schlick

More information about this series at http://www.springer.com/series/5151

Tom Lyche

# Numerical Linear Algebra and Matrix Factorizations 

Tom Lyche
Blindern
University of Oslo
Oslo, Norway

ISSN 1611-0994 ISSN 2197-179X (electronic)
Texts in Computational Science and Engineering
ISBN 978-3-030-36467-0 ISBN 978-3-030-36468-7 (eBook)
https://doi.org/10.1007/978-3-030-36468-7
Mathematics Subject Classification (2010): 15-XX, 65-XX
© Springer Nature Switzerland AG 2020
This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.
The publisher, the authors, and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer Nature Switzerland AG.
The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland

## Foreword

It is a pleasure to write this foreword to the book "Numerical Linear Algebra and Matrix Factorizations" by Tom Lyche. I see this book project from three perspectives, corresponding to my three different roles: first, as a friend and close colleague of Tom for a number of years, secondly as the present department head, and, finally, as a researcher within the international linear algebra and matrix theory community. The book actually has a long history and started out as lecture notes that Tom wrote for a course in numerical linear algebra. For almost forty years this course has been an important and popular course for our students in mathematics, both in theoretical and more applied directions, as well as students in statistics, physics, mechanics and computer science. These notes have been revised multiple times during the years, and new topics have been added. I have had the pleasure to lecture the course myself, using Tom's lecture notes, and I believe that both the selection of topics and the combined approach of theory and algorithms is very appealing. This is also what our students point out when they have taken this course. As we know, the area presented in this book play a highly central role in many applications of mathematics and in scientific computing in general. Sometimes, in the international linear algebra and matrix theory community, one divides the area into numerical linear algebra, applied linear algebra and core (theoretical) linear algebra. This may serve some purpose, but often it is fruitful to have a more unified view on this, in order to see the interplay between theory, applications and algorithms. I think this view dominates this book, and that this makes the book interesting to a wide range of readers. Finally, I would like to thank Tom for his work with this book and the mentioned course, and for being a good colleague from whom I have learned a lot. I know that his international research community in spline theory also share this view. Most importantly, I hope that you, the reader, will enjoy the book!

Oslo, Norway
Geir Dahl
June 2019

## Preface

This book, which has grown out of a one semester course at the University of Oslo, targets upper undergraduate and beginning graduate students in mathematics, statistics, computational physics and engineering who need a mathematical background in numerical linear algebra and related matrix factorizations.

Mastering the material in this book should enable a student to analyze computational problems and develop his or her own algorithms for solving problems of the following kind,

- System of linear equations. Given a (square) matrix $\boldsymbol{A}$ and a vector $\boldsymbol{b}$. Find a vector $\boldsymbol{x}$ such that $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$.
- Least squares. Given a (rectangular) matrix $\boldsymbol{A}$ and a vector $\boldsymbol{b}$. Find a vector $\boldsymbol{x}$ such that the sum of squares of the components of $\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}$ is as small as possible.
- Eigenvalues and eigenvectors. Given a (square) matrix $\boldsymbol{A}$. Find a number $\lambda$ and/or a nonzero vector $\boldsymbol{x}$ such that $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$.

Such problems can be large and difficult to handle, so much can be gained by understanding and taking advantage of special structures. For this we need a good understanding of basic numerical linear algebra and matrix factorizations. Factoring a matrix into a product of simpler matrices is a crucial tool in numerical linear algebra for it allows one to tackle large problems through solving a sequence of easier ones.

The main characteristics of this book are as follows:

1. It is self-contained, only assuming first year calculus, an introductory course in linear algebra, and some experience in solving mathematical problems on a computer. A special feature of this book is the detailed proofs of practically all results. Parts of the book can be studied independently making it suitable for self study.
2. There are numerous exercises which can be found at the end of each chapter. In a separate book we offer solutions to all problems. Solutions of many exam problems given for this course at the University of Oslo are included in this separate volume.

3. The book, consisting of an introductory first chapter and 15 more chapters, naturally disaggregating into six thematically related parts. The chapters are designed to be suitable for a one week per chapter one semester course. Toward the goal of being self-contained, the first chapter contains a review of linear algebra, and is provided to the reader for convenient occasional reference.
4. Many of the chapters contain material beyond what might normally be covered in one week of lectures. A typical 15 week semester's curriculum could consist of the following curated material

| LU and QR factorizations | 2.4, 2.5, 3.2, 3.3, 3.5, 4.1, 4.2, 5.1-5.4, 5.6 |
| :--- | :--- |
| SVD, norms and LSQ | 6.1, 6.3, 7.1-7.4, 8.1-8.3, 9.1-9.3, 9.4.1 |
| Kronecker products | 10.1, 10.2, 10.3, 11.1, 11.2, 11.3 |
| Iterative methods | 12.1-12.4, 13.1-13.3, 13.5 |
| Eigenpairs | 14.1-14.5, 15.1-15.3 |

Chapters 2-4 give a rather complete treatment of various LU factorizations.
Chapters 5-9 cover QR and singular value factorizations, matrix norms, least squares methods and perturbation theory for linear equations and least squares problems.

Chapter 10 gives an introduction to Kronecker products. We illustrate their use by giving simple proofs of properties of the matrix arising from a discretization of the 2 dimensional Poison Equation. Also, we study fast methods based on eigenvector expansions and the Fast Fourier Transform in Chap. 11. Some background from Chaps. 2, 3 and 4 may be needed for Chaps. 10 and 11.

Iterative methods are studied in Chaps. 12 and 13. This includes the classical methods of Jacobi, Gauss Seidel Richardson and Successive Over Relaxation (SOR), as well as a derivation and convergence analysis of the methods of steepest descent and conjugate gradients. The preconditioned conjugate gradient method is introduced and applied to the Poisson problem with variable coefficients.

In Chap. 14 we consider perturbation theory for eigenvalues, the power method and its variants, and use the Inertia Theorem to find a single eigenvalue of a symmetric matrix. Chapter 15 gives a brief informal introduction to one of the most celebrated algorithms of the twentieth century, the QR method for finding all eigenvalues and eigenvectors of a matrix.

5. In this book we give many detailed numerical algorithms for solving linear algebra problems. We have written these algorithms as functions in MATLAB. A list of these functions and the page number where they can be found is included after the table of contents. Moreover, their listings can be found online at http:// folk.uio.no/tom/numlinalg/code. Complexity is discussed briefly in Sect. 3.3.2. As for programming issues, we often vectorize the algorithms leading to shorter and more efficient programs. Stability is important both for the mathematical problems and for the numerical algorithms. Stability can be studied in terms of perturbation theory that leads to condition numbers, see Chaps. 8, 9 and 14. We

will often use phrases like "the algorithm is numerically stable" or "the algorithm is not numerically stable" without saying precisely what we mean by this. Loosely speaking, an algorithm is numerically stable if the solution, computed in floating point arithmetic, is the exact solution of a slightly perturbed problem. To determine upper bounds for these perturbations is the topic of backward error analysis. We refer to [7] and [17, 18] for an in-depths treatment.

A list of freely available software tools for solving linear algebra problems can be found at www.netlib.org/utk/people/JackDongarra/la-sw.html

To supplement this volume the reader might consult Björck [2], Meyer [15] and Stewart [17, 18]. For matrix analysis the two volumes by Horn and Johnson [9, 10] contain considerable additional material.

## Acknowledgments

I would like to thank my colleagues Elaine Cohen, Geir Dahl, Michael Floater, Knut Mørken, Richard Riesenfeld, Nils Henrik Risebro, Øyvind Ryan and Ragnar Winther for all the inspiring discussions we have had over the years. Earlier versions of this book were converted to LaTeX by Are Magnus Bruaset and Njål Foldnes with help for the final version from Øyvind Ryan. I thank Christian Schulz, Georg Muntingh and Øyvind Ryan who helped me with the exercise sessions and we have, in a separate volume, provided solutions to practically all problems in this book. I also thank an anonymous referee for useful suggestions. Finally, I would like to give a special thanks to Larry Schumaker for his enduring friendship and encouragement over the years.

Oslo, Norway
Tom Lyche
June 2019

## Contents

1 A Short Review of Linear Algebra ..... 1
1.1 Notation ..... 1
1.2 Vector Spaces and Subspaces ..... 5
1.2.1 Linear Independence and Bases ..... 6
1.2.2 Subspaces ..... 8
1.2.3 The Vector Spaces $\mathbb{R}^{n}$ and $\mathbb{C}^{n}$ ..... 10
1.3 Linear Systems ..... 11
1.3.1 Basic Properties ..... 12
1.3.2 The Inverse Matrix ..... 13
1.4 Determinants ..... 15
1.5 Eigenvalues, Eigenvectors and Eigenpairs ..... 18
1.6 Exercises Chap. 1 ..... 20
1.6.1 Exercises Sect. 1.1 ..... 20
1.6.2 Exercises Sect. 1.3 ..... 21
1.6.3 Exercises Sect. 1.4 ..... 22
Part I LU and QR Factorizations
2 Diagonally Dominant Tridiagonal Matrices; Three Examples ..... 27
2.1 Cubic Spline Interpolation ..... 27
2.1.1 Polynomial Interpolation ..... 28
2.1.2 Piecewise Linear and Cubic Spline Interpolation ..... 28
2.1.3 Give Me a Moment ..... 31
2.1.4 LU Factorization of a Tridiagonal System ..... 34
2.2 A Two Point Boundary Value Problem ..... 37
2.2.1 Diagonal Dominance ..... 38
2.3 An Eigenvalue Problem ..... 40
2.3.1 The Buckling of a Beam ..... 40
2.4 The Eigenpairs of the 1D Test Matrix ..... 41
2.5 Block Multiplication and Triangular Matrices ..... 43
2.5.1 Block Multiplication ..... 43
2.5.2 Triangular Matrices ..... 46
2.6 Exercises Chap. 2 ..... 48
2.6.1 Exercises Sect. 2.1 ..... 48
2.6.2 Exercises Sect. 2.2 ..... 52
2.6.3 Exercises Sect. 2.3 ..... 53
2.6.4 Exercises Sect. 2.4 ..... 53
2.6.5 Exercises Sect. 2.5 ..... 54
2.7 Review Questions ..... 55
3 Gaussian Elimination and LU Factorizations ..... 57
3.13 by 3 Example ..... 57
3.2 Gauss and LU ..... 59
3.3 Banded Triangular Systems ..... 62
3.3.1 Algorithms for Triangular Systems ..... 62
3.3.2 Counting Operations ..... 64
3.4 The PLU Factorization ..... 66
3.4.1 Pivoting ..... 66
3.4.2 Permutation Matrices ..... 66
3.4.3 Pivot Strategies ..... 69
3.5 The LU and LDU Factorizations ..... 70
3.5.1 Existence and Uniqueness ..... 71
3.6 Block LU Factorization ..... 74
3.7 Exercises Chap. 3 ..... 75
3.7.1 Exercises Sect. 3.3 ..... 75
3.7.2 Exercises Sect. 3.4 ..... 76
3.7.3 Exercises Sect. 3.5 ..... 78
3.7.4 Exercises Sect. 3.6 ..... 81
3.8 Review Questions ..... 81
4 LDL* Factorization and Positive Definite Matrices ..... 83
4.1 The LDL* Factorization ..... 83
4.2 Positive Definite and Semidefinite Matrices ..... 85
4.2.1 The Cholesky Factorization ..... 87
4.2.2 Positive Definite and Positive Semidefinite Criteria ..... 89
4.3 Semi-Cholesky Factorization of a Banded Matrix ..... 91
4.4 The Non-symmetric Real Case ..... 95
4.5 Exercises Chap. 4 ..... 96
4.5.1 Exercises Sect. 4.2 ..... 96
4.6 Review Questions ..... 97
5 Orthonormal and Unitary Transformations ..... 99
5.1 Inner Products, Orthogonality and Unitary Matrices ..... 99
5.1.1 Real and Complex Inner Products ..... 100
5.1.2 Orthogonality ..... 102
5.1.3 Sum of Subspaces and Orthogonal Projections ..... 104
5.1.4 Unitary and Orthogonal Matrices ..... 106
5.2 The Householder Transformation ..... 107
5.3 Householder Triangulation ..... 111
5.3.1 The Algorithm ..... 111
5.3.2 The Number of Arithmetic Operations ..... 113
5.3.3 Solving Linear Systems Using Unitary Transformations ..... 113
5.4 The QR Decomposition and QR Factorization ..... 114
5.4.1 Existence ..... 114
5.5 QR and Gram-Schmidt ..... 116
5.6 Givens Rotations ..... 117
5.7 Exercises Chap. 5 ..... 119
5.7.1 Exercises Sect. 5.1 ..... 119
5.7.2 Exercises Sect. 5.2 ..... 119
5.7.3 Exercises Sect. 5.4 ..... 120
5.7.4 Exercises Sect. 5.5 ..... 123
5.7.5 Exercises Sect. 5.6 ..... 123
5.8 Review Questions ..... 125
Part II Eigenpairs and Singular Values
6 Eigenpairs and Similarity Transformations ..... 129
6.1 Defective and Nondefective Matrices ..... 129
6.1.1 Similarity Transformations ..... 131
6.1.2 Algebraic and Geometric Multiplicity of Eigenvalues ..... 132
6.2 The Jordan Factorization ..... 133
6.3 The Schur Factorization and Normal Matrices ..... 135
6.3.1 The Schur Factorization ..... 135
6.3.2 Unitary and Orthogonal Matrices ..... 135
6.3.3 Normal Matrices ..... 137
6.3.4 The Rayleigh Quotient ..... 139
6.3.5 The Quasi-Triangular Form ..... 139
6.3.6 Hermitian Matrices ..... 140
6.4 Minmax Theorems ..... 141
6.4.1 The Hoffman-Wielandt Theorem ..... 143
6.5 Left Eigenvectors ..... 143
6.5.1 Biorthogonality ..... 144
6.6 Exercises Chap. 6 ..... 145
6.6.1 Exercises Sect. 6.1 ..... 145
6.6.2 Exercises Sect. 6.2 ..... 147
6.6.3 Exercises Sect. 6.3 ..... 149
6.6.4 Exercises Sect. 6.4 ..... 150
6.7 Review Questions ..... 150
7 The Singular Value Decomposition ..... 153
7.1 The SVD Always Exists ..... 154
7.1.1 The Matrices $\boldsymbol{A}^{*} \boldsymbol{A}, \boldsymbol{A} \boldsymbol{A}^{*}$ ..... 154
7.2 Further Properties of SVD ..... 156
7.2.1 The Singular Value Factorization ..... 156
7.2.2 SVD and the Four Fundamental Subspaces ..... 159
7.3 A Geometric Interpretation ..... 159
7.4 Determining the Rank of a Matrix Numerically ..... 161
7.4.1 The Frobenius Norm ..... 161
7.4.2 Low Rank Approximation ..... 162
7.5 Exercises Chap. 7 ..... 163
7.5.1 Exercises Sect. 7.1 ..... 163
7.5.2 Exercises Sect. 7.2 ..... 164
7.5.3 Exercises Sect. 7.4 ..... 167
7.6 Review Questions ..... 168
Part III Matrix Norms and Least Squares
8 Matrix Norms and Perturbation Theory for Linear Systems ..... 171
8.1 Vector Norms ..... 171
8.2 Matrix Norms ..... 174
8.2.1 Consistent and Subordinate Matrix Norms ..... 174
8.2.2 Operator Norms ..... 175
8.2.3 The Operator $p$-Norms ..... 177
8.2.4 Unitary Invariant Matrix Norms ..... 179
8.2.5 Absolute and Monotone Norms ..... 180
8.3 The Condition Number with Respect to Inversion ..... 180
8.3.1 Perturbation of the Right Hand Side in a Linear Systems ..... 181
8.3.2 Perturbation of a Square Matrix ..... 183
8.4 Proof That the $p$-Norms Are Norms ..... 185
8.4.1 p-Norms and Inner Product Norms ..... 188
8.5 Exercises Chap. 8 ..... 190
8.5.1 Exercises Sect. 8.1 ..... 190
8.5.2 Exercises Sect. 8.2 ..... 191
8.5.3 Exercises Sect. 8.3 ..... 194
8.5.4 Exercises Sect. 8.4 ..... 197
8.6 Review Questions ..... 198
9 Least Squares ..... 199
9.1 Examples ..... 200
9.1.1 Curve Fitting ..... 202
9.2 Geometric Least Squares Theory ..... 204
9.3 Numerical Solution ..... 205
9.3.1 Normal Equations ..... 205
9.3.2 QR Factorization ..... 206
9.3.3 Singular Value Decomposition, Generalized Inverses and Least Squares ..... 207
9.4 Perturbation Theory for Least Squares ..... 210
9.4.1 Perturbing the Right Hand Side ..... 211
9.4.2 Perturbing the Matrix ..... 212
9.5 Perturbation Theory for Singular Values ..... 213
9.5.1 The Minmax Theorem for Singular Values and the Hoffman-Wielandt Theorem ..... 213
9.6 Exercises Chap. 9 ..... 216
9.6.1 Exercises Sect. 9.1 ..... 216
9.6.2 Exercises Sect. 9.2 ..... 217
9.6.3 Exercises Sect. 9.3 ..... 218
9.6.4 Exercises Sect. 9.4 ..... 221
9.6.5 Exercises Sect. 9.5 ..... 221
9.7 Review Questions ..... 222
Part IV Kronecker Products and Fourier Transforms
10 The Kronecker Product ..... 225
10.1 The 2D Poisson Problem ..... 225
10.1.1 The Test Matrices ..... 228
10.2 The Kronecker Product ..... 229
10.3 Properties of the 2D Test Matrices ..... 232
10.4 Exercises Chap. 10 ..... 234
10.4.1 Exercises Sects. 10.1, 10.2 ..... 234
10.4.2 Exercises Sect. 10.3 ..... 234
10.5 Review Questions ..... 236
11 Fast Direct Solution of a Large Linear System ..... 237
11.1 Algorithms for a Banded Positive Definite System ..... 237
11.1.1 Cholesky Factorization ..... 238
11.1.2 Block LU Factorization of a Block Tridiagonal Matrix ..... 238
11.1.3 Other Methods ..... 239
11.2 A Fast Poisson Solver Based on Diagonalization ..... 239
11.3 A Fast Poisson Solver Based on the Discrete Sine and Fourier Transforms ..... 242
11.3.1 The Discrete Sine Transform (DST) ..... 242
11.3.2 The Discrete Fourier Transform (DFT) ..... 242
11.3.3 The Fast Fourier Transform (FFT) ..... 244
11.3.4 A Poisson Solver Based on the FFT ..... 247
11.4 Exercises Chap. 11 ..... 247
11.4.1 Exercises Sect. 11.3 ..... 247
11.5 Review Questions ..... 250
Part V Iterative Methods for Large Linear Systems
12 The Classical Iterative Methods ..... 253
12.1 Classical Iterative Methods; Component Form ..... 253
12.1.1 The Discrete Poisson System ..... 255
12.2 Classical Iterative Methods; Matrix Form ..... 257
12.2.1 Fixed-Point Form ..... 258
12.2.2 The Splitting Matrices for the Classical Methods ..... 258
12.3 Convergence ..... 260
12.3.1 Richardson's Method ..... 261
12.3.2 Convergence of SOR ..... 263
12.3.3 Convergence of the Classical Methods for the Discrete Poisson Matrix ..... 264
12.3.4 Number of Iterations ..... 266
12.3.5 Stopping the Iteration ..... 267
12.4 Powers of a Matrix ..... 268
12.4.1 The Spectral Radius ..... 268
12.4.2 Neumann Series ..... 270
12.5 The Optimal SOR Parameter $\omega$ ..... 271
12.6 Exercises Chap. 12 ..... 274
12.6.1 Exercises Sect. 12.3 ..... 274
12.6.2 Exercises Sect. 12.4 ..... 276
12.7 Review Questions ..... 277
13 The Conjugate Gradient Method ..... 279
13.1 Quadratic Minimization and Steepest Descent ..... 280
13.2 The Conjugate Gradient Method ..... 283
13.2.1 Derivation of the Method ..... 283
13.2.2 The Conjugate Gradient Algorithm ..... 285
13.2.3 Numerical Example ..... 286
13.2.4 Implementation Issues ..... 286
13.3 Convergence ..... 288
13.3.1 The Main Theorem ..... 288
13.3.2 The Number of Iterations for the Model Problems ..... 289
13.3.3 Krylov Spaces and the Best Approximation Property ..... 289
13.4 Proof of the Convergence Estimates ..... 293
13.4.1 Chebyshev Polynomials ..... 293
13.4.2 Convergence Proof for Steepest Descent ..... 296
13.4.3 Monotonicity of the Error ..... 298
13.5 Preconditioning ..... 299
13.6 Preconditioning Example ..... 302
13.6.1 A Variable Coefficient Problem ..... 302
13.6.2 Applying Preconditioning ..... 305
13.7 Exercises Chap. 13 ..... 306
13.7.1 Exercises Sect. 13.1 ..... 306
13.7.2 Exercises Sect. 13.2 ..... 307
13.7.3 Exercises Sect. 13.3 ..... 309
13.7.4 Exercises Sect. 13.4 ..... 312
13.7.5 Exercises Sect. 13.5 ..... 313
13.8 Review Questions ..... 313
Part VI Eigenvalues and Eigenvectors
14 Numerical Eigenvalue Problems ..... 317
14.1 Eigenpairs ..... 317
14.2 Gershgorin's Theorem ..... 318
14.3 Perturbation of Eigenvalues ..... 320
14.3.1 Nondefective Matrices ..... 322
14.4 Unitary Similarity Transformation of a Matrix into Upper Hessenberg Form ..... 324
14.4.1 Assembling Householder Transformations ..... 326
14.5 Computing a Selected Eigenvalue of a Symmetric Matrix ..... 326
14.5.1 The Inertia Theorem ..... 328
14.5.2 Approximating $\lambda_{m}$ ..... 329
14.6 Exercises Chap. 14 ..... 330
14.6.1 Exercises Sect. 14.1 ..... 330
14.6.2 Exercises Sect. 14.2 ..... 331
14.6.3 Exercises Sect. 14.3 ..... 331
14.6.4 Exercises Sect. 14.4 ..... 332
14.6.5 Exercises Sect. 14.5 ..... 332
14.7 Review Questions ..... 334
15 The QR Algorithm ..... 335
15.1 The Power Method and Its Variants ..... 335
15.1.1 The Power Method ..... 335
15.1.2 The Inverse Power Method ..... 339
15.1.3 Rayleigh Quotient Iteration ..... 340
15.2 The Basic QR Algorithm ..... 342
15.2.1 Relation to the Power Method ..... 343
15.2.2 Invariance of the Hessenberg Form ..... 344
15.2.3 Deflation ..... 345
15.3 The Shifted QR Algorithms ..... 345
15.4 Exercises Chap. 15 ..... 346
15.4.1 Exercises Sect. 15.1 ..... 346
15.5 Review Questions ..... 347
Part VII Appendix
16 Differentiation of Vector Functions ..... 351
References ..... 355
Index ..... 357

## List of Figures

Fig. 1.1 The triangle $T$ defined by the three points $P_{1}, P_{2}$ and $P_{3}$ ..... 23
Fig. 2.1 The polynomial of degree 13 interpolating $f(x)=\arctan (10 x)+\pi / 2$ on $[-1,1]$. See text ..... 29
Fig. 2.2 The piecewise linear polynomial interpolating $f(x)=\arctan (10 x)+\pi / 2$ at $n=14$ uniform points on [-1, 1] ..... 29
Fig. 2.3 A cubic spline with one knot interpolating $f(x)=x^{4}$ on [0, 2] ..... 31
Fig. 2.4 A cubic B-spline ..... 34
Fig. 2.5 The cubic spline interpolating $f(x)=\arctan (10 x)+\pi / 2$ at 14 equidistant sites on $[-1,1]$. The exact function is also shown ..... 51
Fig. 3.1 Gaussian elimination ..... 59
Fig. 3.2 Lower triangular $5 \times 5$ band matrices: $d=1$ (left) and $d=2$ right ..... 62
Fig. 5.1 The construction of $\boldsymbol{v}_{1}$ and $\boldsymbol{v}_{2}$ in Gram-Schmidt. The constant $c$ is given by $c:=\left\langle\boldsymbol{s}_{2}, \boldsymbol{v}_{1}\right\rangle /\left\langle\boldsymbol{v}_{1}, \boldsymbol{v}_{1}\right\rangle$ ..... 103
Fig. 5.2 The orthogonal projections of $\boldsymbol{s}+\boldsymbol{t}$ into $\mathcal{S}$ and $\mathcal{T}$ ..... 105
Fig. 5.3 The Householder transformation in Example 5.1 ..... 108
Fig. 5.4 A plane rotation ..... 117
Fig. 7.1 The ellipse $y_{1}^{2} / 9+y_{2}^{2}=1$ (left) and the rotated ellipse $\boldsymbol{A} \boldsymbol{\mathcal { S }}$ (right) ..... 160
Fig. 8.1 A convex function ..... 185
Fig. 9.1 A least squares fit to data ..... 201
Fig. 9.2 Graphical interpretation of the bounds in Theorem 9.8 ..... 211
Fig. 10.1 Numbering of grid points ..... 227
Fig. 10.2 The 5-point stencil ..... 227
Fig. 10.3 Band structure of the 2D test matrix ..... 228
Fig. 11.1 Fill-inn in the Cholesky factor of the Poisson matrix ( $n=100$ ) ..... 238
Fig. 12.1 The functions $\alpha \rightarrow\left|1-\alpha \lambda_{1}\right|$ and $\alpha \rightarrow\left|1-\alpha \lambda_{n}\right|$ ..... 262
Fig. $12.2 \rho\left(\boldsymbol{G}_{\omega}\right)$ with $\omega \in[0,2]$ for $n=100$, (lower curve) and $n=2500$ (upper curve) ..... 266
Fig. 13.1 Level curves for $Q(x, y)$ given by (13.4). Also shown is a steepest descent iteration (left) and a conjugate gradient iteration (right) to find the minimum of $Q$ (cf Examples 13.1,13.2) ..... 281
Fig. 13.2 The orthogonal projection of $\boldsymbol{x}-\boldsymbol{x}_{0}$ into $\mathbb{W}_{k}$ ..... 291
Fig. 13.3 This is an illustration of the proof of Theorem 13.6 for $k=3 . f \equiv Q-Q^{*}$ has a double zero at $\mu_{1}$ and one zero between $\mu_{2}$ and $\mu_{3}$ ..... 295
Fig. 14.1 The Gershgorin disk $R_{i}$ ..... 319
Fig. 15.1 Post multiplication in a QR step ..... 344

## List of Tables

Table 12.1 The number of iterations $k_{n}$ to solve the discrete Poisson problem with $n$ unknowns using the methods of Jacobi, Gauss-Seidel, and SOR (see text) with a tolerance $10^{-8}$ ..... 256
Table 12.2 Spectral radial for $\boldsymbol{G}_{J}, \boldsymbol{G}_{1}, \boldsymbol{G}_{\omega^{*}}$ and the smallest integer $k_{n}$ such that $\rho(\boldsymbol{G})^{k_{n}} \leq 10^{-8}$ ..... 266
Table 13.1 The number of iterations $K$ for the averaging problem on a $\sqrt{n} \times \sqrt{n}$ grid for various $n$ ..... 287
Table 13.2 The number of iterations $K$ for the Poisson problem on a $\sqrt{n} \times \sqrt{n}$ grid for various $n$ ..... 287
Table 13.3 The number of iterations $K$ (no preconditioning) and $K_{p r e}$ (with preconditioning) for the problem (13.52) using the discrete Poisson problem as a preconditioner ..... 305
Table 15.1 Quadratic convergence of Rayleigh quotient iteration ..... 341

## Listings

2.1 trifactor ..... 36
2.2 trisolve ..... 36
2.3 splineint ..... 50
2.4 findsubintervals ..... 50
2.5 splineval ..... 51
3.1 rforwardsolve ..... 63
3.2 rbacksolve ..... 63
3.3 cforwardsolve ..... 64
3.4 L1U ..... 73
3.5 cbacksolve ..... 75
4.1 LDLs ..... 85
4.2 bandcholesky ..... 89
4.3 bandsemicholeskyL ..... 94
5.1 housegen ..... 110
5.2 housetriang ..... 112
5.3 rothesstri ..... 123
11.1 fastpoisson ..... 241
11.2 fftrec ..... 246
12.1 jdp ..... 256
12.2 sordp ..... 257
13.1 cg ..... 286
13.2 cgtest ..... 287
13.3 pcg ..... 301
14.1 hesshousegen ..... 325
14.2 accumulateQ ..... 326
15.1 powerit ..... 338
15.2 rayleighit ..... 341

## Chapter 1 <br> A Short Review of Linear Algebra

In this introductory chapter we give a compact introduction to linear algebra with emphasis on $\mathbb{R}^{n}$ and $\mathbb{C}^{n}$. For a more elementary introduction, see for example the book [13].

### 1.1 Notation

The following sets and notations will be used in this book.

1. The sets of natural numbers, integers, rational numbers, real numbers, and complex numbers are denoted by $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$, respectively.
2. We use the "colon equal" symbol $v:=e$ to indicate that the symbol $v$ is defined by the expression $e$.
3. $\mathbb{R}^{n}$ is the set of $n$-tuples of real numbers which we will represent as bold face column vectors. Thus $\boldsymbol{x} \in \mathbb{R}^{n}$ means
$$
\boldsymbol{x}=\left[\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right],
$$
where $x_{i} \in \mathbb{R}$ for $i=1, \ldots, n$. Row vectors are normally identified using the transpose operation. Thus if $\boldsymbol{x} \in \mathbb{R}^{n}$ then $\boldsymbol{x}$ is a column vector and $\boldsymbol{x}^{T}$ is a row vector.

4. Addition and scalar multiplication are denoted and defined by
$$
\boldsymbol{x}+\boldsymbol{y}:=\left[\begin{array}{c}
x_{1}+y_{1} \\
\vdots \\
x_{n}+y_{n}
\end{array}\right], \quad a \boldsymbol{x}:=\left[\begin{array}{c}
a x_{1} \\
\vdots \\
a x_{n}
\end{array}\right], \quad \boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}, \quad a \in \mathbb{R} .
$$
5. $\mathbb{R}^{m \times n}$ is the set of matrices $\boldsymbol{A}$ with real elements. The integers $m$ and $n$ are the number of rows and columns in the tableau
$$
\boldsymbol{A}=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right] .
$$
The element in the $i$ th row and $j$ th column of $\boldsymbol{A}$ will be denoted by $a_{i, j}, a_{i j}$, $\boldsymbol{A}(i, j)$ or $(\boldsymbol{A})_{i, j}$. We use the notations
$$
\boldsymbol{a}_{: j}:=\left[\begin{array}{c}
a_{1 j} \\
a_{2 j} \\
\vdots \\
a_{m j}
\end{array}\right], \quad \boldsymbol{a}_{i:}^{T}:=\left[a_{i 1}, a_{i 2}, \ldots, a_{i n}\right], \quad \boldsymbol{A}=\left[\boldsymbol{a}_{: 1}, \boldsymbol{a}_{: 2}, \ldots \boldsymbol{a}_{: n}\right]=\left[\begin{array}{c}
\boldsymbol{a}_{1:}^{T} \\
\boldsymbol{a}_{2:}^{T} \\
\vdots \\
\boldsymbol{a}_{m:}^{T}
\end{array}\right]
$$
for the columns $\boldsymbol{a}_{: j}$ and rows $\boldsymbol{a}_{i:}^{T}$ of $\boldsymbol{A}$. We often drop the colon and write $\boldsymbol{a}_{j}$ and $\boldsymbol{a}_{i}^{T}$ with the risk of some confusion. If $m=1$ then $\boldsymbol{A}$ is a row vector, if $n=1$ then $\boldsymbol{A}$ is a column vector, while if $m=n$ then $\boldsymbol{A}$ is a square matrix. In this text we will denote matrices by boldface capital letters $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}, \cdots$ and vectors most often by boldface lower case letters $\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z}, \cdots$.
6. A complex number is a number written in the form $x=a+i b$, where $a, b$ are real numbers and $i$, the imaginary unit, satisfies $i^{2}=-1$. The set of all such numbers is denoted by $\mathbb{C}$. The numbers $a=\operatorname{Re} x$ and $b=\operatorname{Im} x$ are the real and imaginary part of $x$. The number $\bar{x}:=a-i b$ is called the complex conjugate of $x=a+i b$, and $|x|:=\sqrt{\bar{x} x}=\sqrt{a^{2}+b^{2}}$ the absolute value or modulus of $x$. The complex exponential function can be defined by
$$
e^{x}=e^{a+i b}:=e^{a}(\cos b+i \sin b) .
$$
In particular,
$$
e^{i \pi / 2}=i, \quad e^{i \pi}=-1, \quad e^{2 i \pi}=1 .
$$

We have $e^{x+y}=e^{x} e^{y}$ for all $x, y \in \mathbb{C}$. The polar form of a complex number is
$$
x=a+i b=r e^{i \theta}, \quad r=|x|=\sqrt{a^{2}+b^{2}}, \quad \cos \theta=\frac{a}{r}, \quad \sin \theta=\frac{b}{r} .
$$
7. For matrices and vectors with complex elements we use the notation $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ and $\boldsymbol{x} \in \mathbb{C}^{n}$. We define complex row vectors using either the transpose $\boldsymbol{x}^{T}$ or the conjugate transpose operation $\boldsymbol{x}^{*}:=\overline{\boldsymbol{x}}^{T}=\left[\bar{x}_{1}, \ldots, \bar{x}_{n}\right]$. If $\boldsymbol{x} \in \mathbb{R}^{n}$ then $x^{*}=x^{T}$.
8. For $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ and $a \in \mathbb{C}$ the operations of vector addition and scalar multiplication is defined by component operations as in the real case (cf. 4.).
9. The arithmetic operations on rectangular matrices are
    - matrix addition $\boldsymbol{C}:=\boldsymbol{A}+\boldsymbol{B}$ if $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}$ are matrices of the same size, i.e., with the same number of rows and columns, and $c_{i j}:=a_{i j}+b_{i j}$ for all $i, j$.
    - multiplication by a scalar $\boldsymbol{C}:=\alpha \boldsymbol{A}$, where $c_{i j}:=\alpha a_{i j}$ for all $i, j$.
    - matrix multiplication $\boldsymbol{C}:=\boldsymbol{A} \boldsymbol{B}, \boldsymbol{C}=\boldsymbol{A} \cdot \boldsymbol{B}$ or $\boldsymbol{C}=\boldsymbol{A} * \boldsymbol{B}$, where $\boldsymbol{A} \in$ $\mathbb{C}^{m \times p}, \boldsymbol{B} \in \mathbb{C}^{p \times n}, \boldsymbol{C} \in \mathbb{C}^{m \times n}$, and $c_{i j}:=\sum_{k=1}^{p} a_{i k} b_{k j}$ for $i=1, \ldots, m$, $j=1, \ldots, n$.
    - element-by-element matrix operations $\boldsymbol{C}:=\boldsymbol{A} \times \boldsymbol{B}, \boldsymbol{D}:=\boldsymbol{A} / \boldsymbol{B}$, and $\boldsymbol{E}:=$ $\boldsymbol{A} \wedge r$ where all matrices are of the same size and $c_{i j}:=a_{i j} b_{i j}, d_{i j}:=a_{i j} / b_{i j}$ and $e_{i j}:=a_{i j}^{r}$ for all $i, j$ and suitable $r$. For the division $\boldsymbol{A} / \boldsymbol{B}$ we assume that all elements of $\boldsymbol{B}$ are nonzero. The element-by-element product $\boldsymbol{C}=\boldsymbol{A} \times \boldsymbol{B}$ is known as the Schur product and also the Hadamard product.
10. Let $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ or $\boldsymbol{A} \in \mathbb{C}^{m \times n}$. The transpose $\boldsymbol{A}^{T}$ and conjugate transpose $\boldsymbol{A}^{*}$ are $n \times m$ matrices with elements $a_{i j}^{T}:=a_{j i}$ and $a_{i j}^{*}:=\bar{a}_{j i}$, respectively. If $\boldsymbol{B}$ is an $n, p$ matrix then $(\boldsymbol{A} \boldsymbol{B})^{T}=\boldsymbol{B}^{T} \boldsymbol{A}^{T}$ and $(\boldsymbol{A} \boldsymbol{B})^{*}=\boldsymbol{B}^{*} \boldsymbol{A}^{*}$. A matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is symmetric if $\boldsymbol{A}^{T}=\boldsymbol{A}$ and Hermitian if $\boldsymbol{A}^{*}=\boldsymbol{A}$.
11. The unit vectors in $\mathbb{R}^{n}$ and $\mathbb{C}^{n}$ are denoted by
$$
\boldsymbol{e}_{1}:=\left[\begin{array}{c}
1 \\
0 \\
0 \\
\vdots \\
0
\end{array}\right], \quad \boldsymbol{e}_{2}:=\left[\begin{array}{c}
0 \\
1 \\
0 \\
\vdots \\
0
\end{array}\right], \quad \boldsymbol{e}_{3}:=\left[\begin{array}{c}
0 \\
0 \\
1 \\
\vdots \\
0
\end{array}\right], \quad \ldots, \quad \boldsymbol{e}_{n}:=\left[\begin{array}{c}
0 \\
0 \\
0 \\
\vdots \\
1
\end{array}\right],
$$
while $\boldsymbol{I}_{n}=\boldsymbol{I}:=\left[\delta_{i j}\right]_{i, j=1}^{n}$, where
$$
\delta_{i j}:= \begin{cases}1 & \text { if } i=j \\ 0 & \text { otherwise }\end{cases}
$$
is the identity matrix of order $n$. Both the columns and the transpose of the rows of $\boldsymbol{I}$ are the unit vectors $\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \ldots, \boldsymbol{e}_{n}$.

12. Some matrices with many zeros have names indicating their "shape". Suppose $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ or $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Then $\boldsymbol{A}$ is
    - diagonal if $a_{i j}=0$ for $i \neq j$.
    - upper triangular or right triangular if $a_{i j}=0$ for $i>j$.
    - lower triangular or left triangular if $a_{i j}=0$ for $i<j$.
    - upper Hessenberg if $a_{i j}=0$ for $i>j+1$.
    - lower Hessenberg if $a_{i j}=0$ for $i<j+1$.
    - tridiagonal if $a_{i j}=0$ for $|i-j|>1$.
    - $d$-banded if $a_{i j}=0$ for $|i-j|>d$.
13. We use the following notations for diagonal- and tridiagonal $n \times n$ matrices
$$
\begin{gathered}
\operatorname{diag}\left(d_{i}\right)=\operatorname{diag}\left(d_{1}, \ldots, d_{n}\right):=\left[\begin{array}{cccc}
d_{1} & 0 & \cdots & 0 \\
0 & d_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_{n}
\end{array}\right]=\left[\begin{array}{lll}
d_{1} & & \\
& \ddots & \\
& & d_{n}
\end{array}\right], \\
\boldsymbol{B}=\operatorname{tridiag}\left(a_{i}, d_{i}, c_{i}\right)=\operatorname{tridiag}(\boldsymbol{a}, \boldsymbol{d}, \boldsymbol{c}):=\left[\begin{array}{cccc}
d_{1} & c_{1} & & \\
a_{1} & d_{2} & c_{2} & \\
& \ddots & \ddots & \ddots \\
& & a_{n-2} & d_{n-1} \\
& & & a_{n-1} \\
& & d_{n}
\end{array}\right] .
\end{gathered}
$$
Here $b_{i i}:=d_{i}$ for $i=1, \ldots, n, b_{i+1, i}:=a_{i}, b_{i, i+1}:=c_{i}$ for $i=1, \ldots, n-1$, and $b_{i j}:=0$ otherwise.
14. Suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ and $1 \leq i_{1}<i_{2}<\cdots<i_{r} \leq m, 1 \leq j_{1}<j_{2}<\cdots<$ $j_{c} \leq n$. The matrix $\boldsymbol{A}(\boldsymbol{i}, \boldsymbol{j}) \in \mathbb{C}^{r \times c}$ is the submatrix of $\boldsymbol{A}$ consisting of rows $\boldsymbol{i}:=\left[i_{1}, \ldots, i_{r}\right]$ and columns $\boldsymbol{j}:=\left[j_{1}, \ldots, j_{c}\right]$
$$
\boldsymbol{A}(\boldsymbol{i}, \boldsymbol{j}):=\boldsymbol{A}\left(\begin{array}{cccc}
i_{1} & i_{2} & \cdots & i_{r} \\
j_{1} & j_{2} & \cdots & j_{c}
\end{array}\right)=\left[\begin{array}{cccc}
a_{i_{1}, j_{1}} & a_{i_{1}, j_{2}} & \cdots & a_{i_{1}, j_{c}} \\
a_{i_{2}, j_{1}} & a_{i_{2}, j_{2}} & \cdots & a_{i_{2}, j_{c}} \\
\vdots & \vdots & \ddots & \vdots \\
a_{i_{r}, j_{1}} & a_{i_{r}, j_{2}} & \cdots & a_{i_{r}, j_{c}}
\end{array}\right] .
$$
For the special case of consecutive rows and columns we also use the notation
$$
\boldsymbol{A}\left(r_{1}: r_{2}, c_{1}: c_{2}\right):=\left[\begin{array}{rrrr}
a_{r_{1}, c_{1}} & a_{r_{1}, c_{1}+1} & \cdots & a_{r_{1}, c_{2}} \\
a_{r_{1}+1, c_{1}} & a_{r_{1}+1, c_{1}+1} & \cdots & a_{r_{1}+1, c_{2}} \\
\vdots & \vdots & \ddots & \vdots \\
a_{r_{2}, c_{1}} & a_{r_{2}, c_{1}+1} & \cdots & a_{r_{2}, c_{2}}
\end{array}\right] .
$$

### 1.2 Vector Spaces and Subspaces

Many mathematical systems have analogous properties to vectors in $\mathbb{R}^{2}$ or $\mathbb{R}^{3}$.
Definition 1.1 (Real Vector Space) A real vector space is a nonempty set $\mathcal{V}$, whose objects are called vectors, together with two operations $+: \mathcal{V} \times \mathcal{V} \longrightarrow \mathcal{V}$ and $\cdot: \mathbb{R} \times \mathcal{V} \longrightarrow \mathcal{V}$, called addition and scalar multiplication, satisfying the following axioms for all vectors $\boldsymbol{u}, \boldsymbol{v}, \boldsymbol{w}$ in $\mathcal{V}$ and scalars $c, d$ in $\mathbb{R}$.

(V1) The sum $\boldsymbol{u}+\boldsymbol{v}$ is in $\mathcal{V}$,
(V2) $\boldsymbol{u}+\boldsymbol{v}=\boldsymbol{v}+\boldsymbol{u}$,
(V3) $\boldsymbol{u}+(\boldsymbol{v}+\boldsymbol{w})=(\boldsymbol{u}+\boldsymbol{v})+\boldsymbol{w}$,
(V4) There is a zero vector $\mathbf{0}$ such that $\boldsymbol{u}+\mathbf{0}=\boldsymbol{u}$,
(V5) For each $\boldsymbol{u}$ in $\mathcal{V}$ there is a vector $-\boldsymbol{u}$ in $\mathcal{V}$ such that $\boldsymbol{u}+(-\boldsymbol{u})=\mathbf{0}$,
(S1) The scalar multiple $c \cdot \boldsymbol{u}$ is in $\mathcal{V}$,
(S2) $c \cdot(\boldsymbol{u}+\boldsymbol{v})=c \cdot \boldsymbol{u}+c \cdot \boldsymbol{v}$,
(S3) $(c+d) \cdot \boldsymbol{u}=c \cdot \boldsymbol{u}+d \cdot \boldsymbol{u}$,
(S4) $c \cdot(d \cdot \boldsymbol{u})=(c d) \cdot \boldsymbol{u}$,
(S5) $1 \cdot \boldsymbol{u}=\boldsymbol{u}$.

The scalar multiplication symbol ⋅ is often omitted, writing $c \boldsymbol{v}$ instead of $c \cdot \boldsymbol{v}$. We define $\boldsymbol{u}-\boldsymbol{v}:=\boldsymbol{u}+(-\boldsymbol{v})$. We call $\mathcal{V}$ a complex vector space if the scalars consist of all complex numbers $\mathbb{C}$. In this book a vector space is either real or complex.

From the axioms it follows that

1. The zero vector is unique.
2. For each $\boldsymbol{u} \in \mathcal{V}$ the negative $-\boldsymbol{u}$ of $\boldsymbol{u}$ is unique.
3. $0 \boldsymbol{u}=\mathbf{0}, c \mathbf{0}=\mathbf{0}$, and $-\boldsymbol{u}=(-1) \boldsymbol{u}$.

Here are some examples

1. The spaces $\mathbb{R}^{n}$ and $\mathbb{C}^{n}$, where $n \in \mathbb{N}$, are real and complex vector spaces, respectively.
2. Let $\mathcal{D}$ be a subset of $\mathbb{R}$ and $d \in \mathbb{N}$. The set $\mathcal{V}$ of all functions $\boldsymbol{f}, \boldsymbol{g}: \mathcal{D} \rightarrow \mathbb{R}^{d}$ is a real vector space with
$$
(\boldsymbol{f}+\boldsymbol{g})(t):=\boldsymbol{f}(t)+\boldsymbol{g}(t), \quad(c \boldsymbol{f})(t):=c \boldsymbol{f}(t), \quad t \in \mathcal{D}, \quad c \in \mathbb{R} .
$$
Two functions $\boldsymbol{f}, \boldsymbol{g}$ in $\mathcal{V}$ are equal if $\boldsymbol{f}(t)=\boldsymbol{g}(t)$ for all $t \in \mathcal{D}$. The zero element is the zero function given by $\boldsymbol{f}(t)=\mathbf{0}$ for all $t \in \mathcal{D}$ and the negative of $\boldsymbol{f}$ is given by $-\boldsymbol{f}=(-1) \boldsymbol{f}$. In the following we will use boldface letters for functions only if $d>1$.
3. For $n \geq 0$ the space $\Pi_{n}$ of polynomials of degree at most $n$ consists of all polynomials $p: \mathbb{R} \rightarrow \mathbb{R}, p: \mathbb{R} \rightarrow \mathbb{C}$, or $p: \mathbb{C} \rightarrow \mathbb{C}$ of the form
$$
p(t):=a_{0}+a_{1} t+a_{2} t^{2}+\cdots+a_{n} t^{n},
$$

where the coefficients $a_{0}, \ldots, a_{n}$ are real or complex numbers. $p$ is called the zero polynomial if all coefficients are zero. All other polynomials are said to be nontrivial. The degree of a nontrivial polynomial $p$ given by (1.2) is the smallest integer $0 \leq k \leq n$ such that $p(t)=a_{0}+\cdots+a_{k} t^{k}$ with $a_{k} \neq 0$. The degree of the zero polynomial is not defined. $\Pi_{n}$ is a vector space if we define addition and scalar multiplication as for functions.

Definition 1.2 (Linear Combination) For $n \geq 1$ let $\mathcal{X}:=\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ be a set of vectors in a vector space $\mathcal{V}$ and let $c_{1}, \ldots, c_{n}$ be scalars.

1. The sum $c_{1} \boldsymbol{x}_{1}+\cdots+c_{n} \boldsymbol{x}_{n}$ is called a linear combination of $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}$.
2. The linear combination is nontrivial if $c_{j} \boldsymbol{x}_{j} \neq \mathbf{0}$ for at least one $j$.
3. The set of all linear combinations of elements in $\mathcal{X}$ is denoted $\operatorname{span}(\mathcal{X})$.
4. A vector space is finite dimensional if it has a finite spanning set; i.e., there exists $n \in \mathbb{N}$ and $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ in $\mathcal{V}$ such that $\mathcal{V}=\operatorname{span}\left(\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}\right)$.

Example 1.1 (Linear Combinations)

1. Any $\boldsymbol{x}=\left[x_{1}, \ldots, x_{m}\right]^{T}$ in $\mathbb{C}^{m}$ can be written as a linear combination of the unit vectors as $\boldsymbol{x}=x_{1} \boldsymbol{e}_{1}+x_{2} \boldsymbol{e}_{2}+\cdots+x_{m} \boldsymbol{e}_{m}$. Thus, $\mathbb{C}^{m}=\operatorname{span}\left(\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{m}\right\}\right)$ and $\mathbb{C}^{m}$ is finite dimensional. Similarly $\mathbb{R}^{m}$ is finite dimensional.
2. Let $\Pi=\cup_{n} \Pi_{n}$ be the space of all polynomials. $\Pi$ is a vector space that is not finite dimensional. For suppose $\Pi$ is finite dimensional. Then $\Pi=$ $\operatorname{span}\left(\left\{p_{1}, \ldots, p_{m}\right\}\right)$ for some polynomials $p_{1}, \ldots, p_{m}$. Let $d$ be an integer such that the degree of $p_{j}$ is less than $d$ for $j=1, \ldots, m$. A polynomial of degree $d$ cannot be written as a linear combination of $p_{1}, \ldots, p_{m}$, a contradiction.

### 1.2.1 Linear Independence and Bases

Definition 1.3 (Linear Independence) A set $\mathcal{X}=\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ of nonzero vectors in a vector space is linearly dependent if 0 can be written as a nontrivial linear combination of $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$. Otherwise $\mathcal{X}$ is linearly independent.

A set of vectors $\mathcal{X}=\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ is linearly independent if and only if

$$
c_{1} \boldsymbol{x}_{1}+\cdots+c_{n} \boldsymbol{x}_{n}=\mathbf{0} \quad \Longrightarrow \quad c_{1}=\cdots=c_{n}=0 .
$$

Suppose $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ is linearly independent. Then

1. If $\boldsymbol{x} \in \operatorname{span}(\mathcal{X})$ then the scalars $c_{1}, \ldots, c_{n}$ in the representation $\boldsymbol{x}=c_{1} \boldsymbol{x}_{1}+\cdots+$ $c_{n} \boldsymbol{x}_{n}$ are unique.
2. Any nontrivial linear combination of $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}$ is nonzero,

Lemma 1.1 (Linear Independence and Span) Suppose $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}$ span a vector space $\mathcal{V}$ and that $\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{k}$ are linearly independent vectors in $\mathcal{V}$. Then $k \leq n$.

Proof Suppose $k>n$. Write $\boldsymbol{w}_{1}$ as a linear combination of elements from the set $\mathcal{X}_{0}:=\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$, say $\boldsymbol{w}_{1}=c_{1} \boldsymbol{v}_{1}+\cdots+c_{n} \boldsymbol{v}_{n}$. Since $\boldsymbol{w}_{1} \neq \mathbf{0}$ not all the $c$ 's are equal to zero. Pick a nonzero $c$, say $c_{i_{1}}$. Then $\boldsymbol{v}_{i_{1}}$ can be expressed as a linear combination of $\boldsymbol{w}_{1}$ and the remaining $\boldsymbol{v}$ 's. So the set $\mathcal{X}_{1}:=$ $\left\{\boldsymbol{w}_{1}, \boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{i_{1}-1}, \boldsymbol{v}_{i_{1}+1}, \ldots, \boldsymbol{v}_{n}\right\}$ must also be a spanning set for $\mathcal{V}$. We repeat this for $\boldsymbol{w}_{2}$ and $\mathcal{X}_{1}$. In the linear combination $\boldsymbol{w}_{2}=d_{i_{1}} \boldsymbol{w}_{1}+\sum_{j \neq i_{1}} d_{j} \boldsymbol{v}_{j}$, we must have $d_{i_{2}} \neq 0$ for some $i_{2}$ with $i_{2} \neq i_{1}$. For otherwise $\boldsymbol{w}_{2}=d_{1} \boldsymbol{w}_{1}$ contradicting the linear independence of the $\boldsymbol{w}$ 's. So the set $\mathcal{X}_{2}$ consisting of the $\boldsymbol{v}$ 's with $\boldsymbol{v}_{i_{1}}$ replaced by $\boldsymbol{w}_{1}$ and $\boldsymbol{v}_{i_{2}}$ replaced by $\boldsymbol{w}_{2}$ is again a spanning set for $\mathcal{V}$. Repeating this process $n-2$ more times we obtain a spanning set $\mathcal{X}_{n}$ where $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}$ have been replaced by $\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{n}$. Since $k>n$ we can then write $\boldsymbol{w}_{k}$ as a linear combination of $\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{n}$ contradicting the linear independence of the $\boldsymbol{w}$ 's. We conclude that $k \leq n$. $\square$

Definition 1.4 (Basis) A finite set of vectors $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ in a vector space $\mathcal{V}$ is a basis for $\mathcal{V}$ if

1. $\operatorname{span}\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}=\mathcal{V}$.
2. $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ is linearly independent.

Theorem 1.1 (Basis Subset of a Spanning Set) Suppose $\mathcal{V}$ is a vector space and that $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ is a spanning set for $\mathcal{V}$. Then we can find a subset $\left\{\boldsymbol{v}_{i_{1}}, \ldots, \boldsymbol{v}_{i_{k}}\right\}$ that forms a basis for $\mathcal{V}$.

Proof If $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ is linearly dependent we can express one of the $\boldsymbol{v}$ 's as a nontrivial linear combination of the remaining $\boldsymbol{v}$ 's and drop that $\boldsymbol{v}$ from the spanning set. Continue this process until the remaining $\boldsymbol{v}$ 's are linearly independent. They still span the vector space and therefore form a basis. $\square$

Corollary 1.1 (Existence of a Basis) A vector space is finite dimensional (cf. Definition 1.2) if and only if it has a basis.

Proof Let $\mathcal{V}=\operatorname{span}\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ be a finite dimensional vector space. By Theorem 1.1, $\mathcal{V}$ has a basis. Conversely, if $\mathcal{V}=\operatorname{span}\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ and $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ is a basis then it is by definition a finite spanning set. $\square$

Theorem 1.2 (Dimension of a Vector Space) Every basis for a vector space $\mathcal{V}$ has the same number of elements. This number is called the dimension of the vector space and denoted $\operatorname{dim} \mathcal{V}$.

Proof Suppose $\mathcal{X}=\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right\}$ and $\mathcal{Y}=\left\{\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{k}\right\}$ are two bases for $\mathcal{V}$. By Lemma 1.1 we have $k \leq n$. Using the same Lemma with $\mathcal{X}$ and $\mathcal{Y}$ switched we obtain $n \leq k$. We conclude that $n=k$. $\square$

The set of unit vectors $\left\{\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{n}\right\}$ form a basis for both $\mathbb{R}^{n}$ and $\mathbb{C}^{n}$.
Theorem 1.3 (Enlarging Vectors to a Basis) Every linearly independent set of vectors $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$ in a finite dimensional vector space $\mathcal{V}$ can be enlarged to a basis for $\mathcal{V}$.

Proof If $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$ does not span $\mathcal{V}$ we can enlarge the set by one vector $\boldsymbol{v}_{k+1}$ which cannot be expressed as a linear combination of $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$. The enlarged set is also linearly independent. Continue this process. Since the space is finite dimensional it must stop after a finite number of steps. $\square$

### 1.2.2 Subspaces

Definition 1.5 (Subspace) A nonempty subset $\mathcal{S}$ of a real or complex vector space $\mathcal{V}$ is called a subspace of $\mathcal{V}$ if

(V1) The sum $\boldsymbol{u}+\boldsymbol{v}$ is in $\mathcal{S}$ for any $\boldsymbol{u}, \boldsymbol{v} \in \mathcal{S}$.
(S1) The scalar multiple $c \boldsymbol{u}$ is in $\mathcal{S}$ for any scalar $c$ and any $\boldsymbol{u} \in \mathcal{S}$.

Using the operations in $\mathcal{V}$, any subspace $\mathcal{S}$ of $\mathcal{V}$ is a vector space, i.e., all 10 axioms $V 1-V 5$ and $S 1-S 5$ are satisfied for $\mathcal{S}$. In particular, $\mathcal{S}$ must contain the zero element in $\mathcal{V}$. This follows since the operations of vector addition and scalar multiplication are inherited from $\mathcal{V}$.

Example 1.2 (Examples of Subspaces)

1. $\{\mathbf{0}\}$, where $\mathbf{0}$ is the zero vector is a subspace, the trivial subspace. The dimension of the trivial subspace is defined to be zero. All other subspaces are nontrivial.
2. $\mathcal{V}$ is a subspace of itself.
3. $\operatorname{span}(\mathcal{X})$ is a subspace of $\mathcal{V}$ for any $\mathcal{X}=\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\} \subseteq \mathcal{V}$. Indeed, it is easy to see that (V1) and (S1) hold.
4. The sum of two subspaces $\mathcal{S}$ and $\mathcal{T}$ of a vector space $\mathcal{V}$ is defined by
$$
\mathcal{S}+\mathcal{T}:=\{\boldsymbol{s}+\boldsymbol{t}: \boldsymbol{s} \in \mathcal{S} \text { and } \boldsymbol{t} \in \mathcal{T}\} .
$$
Clearly (V1) and (S1) hold and it is a subspace of $\mathcal{V}$.
5. The intersection of two subspaces $\mathcal{S}$ and $\mathcal{T}$ of a vector space $\mathcal{V}$ is defined by
$$
\mathcal{S} \cap \mathcal{T}:=\{\boldsymbol{x}: \boldsymbol{x} \in \mathcal{S} \text { and } \boldsymbol{x} \in \mathcal{T}\} .
$$
It is a subspace of $\mathcal{V}$.
6. The union of two subspaces $\mathcal{S}$ and $\mathcal{T}$ of a vector space $\mathcal{V}$ is defined by
$$
\mathcal{S} \cup \mathcal{T}:=\{\boldsymbol{x}: \boldsymbol{x} \in \mathcal{S} \text { or } \boldsymbol{x} \in \mathcal{T}\} .
$$
In general it is not a subspace of $\mathcal{V}$.
7. A sum of two subspaces $\mathcal{S}$ and $\mathcal{T}$ of a vector space $\mathcal{V}$ is called a direct sum and denoted $\mathcal{S} \oplus \mathcal{T}$ if $\mathcal{S} \cap \mathcal{T}=\{\mathbf{0}\}$.

Theorem 1.4 (Dimension Formula for Sums of Subspaces) Let $\mathcal{S}$ and $\mathcal{T}$ be two finite subspaces of a vector space $\mathcal{V}$. Then

$$
\operatorname{dim}(\mathcal{S}+\mathcal{T})=\operatorname{dim}(\mathcal{S})+\operatorname{dim}(\mathcal{T})-\operatorname{dim}(\mathcal{S} \cap \mathcal{T}) .
$$

In particular, for a direct sum

$$
\operatorname{dim}(\mathcal{S} \oplus \mathcal{T})=\operatorname{dim}(\mathcal{S})+\operatorname{dim}(\mathcal{T}) .
$$

Proof Let $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}\right\}$ be a basis for $\mathcal{S} \cap \mathcal{T}$, where $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}\right\}=\emptyset$, the empty set, in the case $\mathcal{S} \cap \mathcal{T}=\{\mathbf{0}\}$. We use Theorem 1.3 to extend $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}\right\}$ to a basis $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}, \boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{q}\right\}$ for $\mathcal{S}$ and a basis $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}, \boldsymbol{t}_{1}, \ldots, \boldsymbol{t}_{r}\right\}$ for $\mathcal{T}$. Every $\boldsymbol{x} \in \mathcal{S}+\mathcal{T}$ can be written as a linear combination of

$$
\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}, \boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{q}, \boldsymbol{t}_{1}, \ldots, \boldsymbol{t}_{r}\right\}
$$

so these vectors span $\mathcal{S}+\mathcal{T}$. We show that they are linearly independent and hence a basis. Suppose $\boldsymbol{u}+\boldsymbol{s}+\boldsymbol{t}=\mathbf{0}$, where $\boldsymbol{u}:=\sum_{j=1}^{p} \alpha_{j} \boldsymbol{u}_{j}, \boldsymbol{s}:=\sum_{j=1}^{q} \rho_{j} \boldsymbol{s}_{j}$, and $\boldsymbol{t}:=\sum_{j=1}^{r} \sigma_{j} \boldsymbol{t}_{j}$. Now $\boldsymbol{s}=-(\boldsymbol{u}+\boldsymbol{t})$ belongs to both $\mathcal{S}$ and to $\mathcal{T}$ and hence $\boldsymbol{s} \in$ $\mathcal{S} \cap \mathcal{T}$. Therefore $\boldsymbol{s}$ can be written as a linear combination of $\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}$ say $\boldsymbol{s}:=$ $\sum_{j=1}^{p} \beta_{j} \boldsymbol{u}_{j}$. But then $\mathbf{0}=\sum_{j=1}^{p} \beta_{j} \boldsymbol{u}_{j}-\sum_{j=1}^{q} \rho_{j} \boldsymbol{s}_{j}$ and since

$$
\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}, \boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{q}\right\}
$$

is linearly independent we must have $\beta_{1}=\cdots=\beta_{p}=\rho_{1}=\cdots=\rho_{q}=0$ and hence $\boldsymbol{s}=\mathbf{0}$. We then have $\boldsymbol{u}+\boldsymbol{t}=\mathbf{0}$ and by linear independence of $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}, \boldsymbol{t}_{1}, \ldots, \boldsymbol{t}_{r}\right\}$ we obtain $\alpha_{1}=\cdots=\alpha_{p}=\sigma_{1}=\cdots=\sigma_{r}=0$. We have shown that the vectors $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{p}, \boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{q}, \boldsymbol{t}_{1}, \ldots, \boldsymbol{t}_{r}\right\}$ constitute a basis for $\mathcal{S}+\mathcal{T}$. But then

$$
\operatorname{dim}(\mathcal{S}+\mathcal{T})=p+q+r=(p+q)+(p+r)-p=\operatorname{dim}(\mathcal{S})+\operatorname{dim}(\mathcal{T})-\operatorname{dim}(\mathcal{S} \cap \mathcal{T})
$$

and (1.7) follows. Equation (1.7) implies (1.8) since $\operatorname{dim}\{\mathbf{0}\}=0$. $\square$

It is convenient to introduce a matrix transforming a basis in a subspace into a basis for the space itself.

Lemma 1.2 (Change of Basis Matrix) Suppose $\mathcal{S}$ is a subspace of a finite dimensional vector space $\mathcal{V}$ and let $\left\{\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{n}\right\}$ be a basis for $\mathcal{S}$ and $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{m}\right\}$ a basis for $\mathcal{V}$. Then each $\boldsymbol{s}_{j}$ can be expressed as a linear combination of $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{m}$, say

$$
\boldsymbol{s}_{j}=\sum_{i=1}^{m} a_{i j} \boldsymbol{v}_{i} \text { for } j=1, \ldots, n .
$$

If $\boldsymbol{x} \in \mathcal{S}$ then $\boldsymbol{x}=\sum_{j=1}^{n} c_{j} \boldsymbol{s}_{j}=\sum_{i=1}^{m} b_{i} \boldsymbol{v}_{i}$ for some coefficients $\boldsymbol{b}:=$ $\left[b_{1}, \ldots, \boldsymbol{b}_{m}\right]^{T}, \boldsymbol{c}:=\left[c_{1}, \ldots, c_{n}\right]^{T}$. Moreover $\boldsymbol{b}=\boldsymbol{A} \boldsymbol{c}$, where $\boldsymbol{A}=\left[a_{i j}\right] \in \mathbb{C}^{m \times n}$ is given by (1.9). The matrix $\boldsymbol{A}$ has linearly independent columns.

Proof Equation (1.9) holds for some $a_{i j}$ since $\boldsymbol{s}_{j} \in \mathcal{V}$ and $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{m}\right\}$ spans $\mathcal{V}$. Since $\left\{\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{n}\right\}$ is a basis for $\mathcal{S}$ and $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{m}\right\}$ a basis for $\mathcal{V}$, every $\boldsymbol{x} \in \mathcal{S}$ can be written $\boldsymbol{x}=\sum_{j=1}^{n} c_{j} \boldsymbol{s}_{j}=\sum_{i=1}^{m} b_{i} \boldsymbol{v}_{i}$ for some scalars $\left(c_{j}\right)$ and $\left(b_{i}\right)$. But then

$$
\sum_{i=1}^{m} b_{i} \boldsymbol{v}_{i}=\boldsymbol{x}=\sum_{j=1}^{n} c_{j} \boldsymbol{s}_{j} \stackrel{(1.9)}{=} \sum_{j=1}^{n} c_{j}\left(\sum_{i=1}^{m} a_{i j} \boldsymbol{v}_{i}\right)=\sum_{i=1}^{m}\left(\sum_{j=1}^{n} a_{i j} c_{j}\right) \boldsymbol{v}_{i} .
$$

Since $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{m}\right\}$ is linearly independent it follows that $b_{i}=\sum_{j=1}^{n} a_{i j} c_{j}$ for $i=$ $1, \ldots, m$ or $\boldsymbol{b}=\boldsymbol{A} \boldsymbol{c}$. Finally, to show that $\boldsymbol{A}$ has linearly independent columns suppose $\boldsymbol{b}:=\boldsymbol{A} \boldsymbol{c}=\mathbf{0}$ for some $\boldsymbol{c}=\left[c_{1}, \ldots, c_{n}\right]^{T}$. Define $\boldsymbol{x}:=\sum_{j=1}^{n} c_{j} \boldsymbol{s}_{j}$. Then $\boldsymbol{x}=\sum_{i=1}^{m} b_{i} \boldsymbol{v}_{i}$ and since $\boldsymbol{b}=\mathbf{0}$ we have $\boldsymbol{x}=\mathbf{0}$. But since $\left\{\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{n}\right\}$ is linearly independent it follows that $\boldsymbol{c}=\mathbf{0}$. $\square$

The matrix $\boldsymbol{A}$ in Lemma 1.2 is called a change of basis matrix.

### 1.2.3 The Vector Spaces $\mathbb{R}^{n}$ and $\mathbb{C}^{n}$

When $\mathcal{V}=\mathbb{R}^{m}$ or $\mathbb{C}^{m}$ we can think of $n$ vectors in $\mathcal{V}$, say $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}$, as a set $\mathcal{X}:=\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ or as the columns of an $m \times n$ matrix $\boldsymbol{X}=\left[\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right]$. A linear combination can then be written as a matrix times vector $\boldsymbol{X} \boldsymbol{c}$, where $\boldsymbol{c}=$ $\left[c_{1}, \ldots, c_{n}\right]^{T}$ is the vector of scalars. Thus

$$
\mathcal{R}(\boldsymbol{X}):=\left\{\boldsymbol{X} \boldsymbol{c}: \boldsymbol{c} \in \mathbb{R}^{n}\right\}=\operatorname{span}(\mathcal{X}) .
$$

Definition 1.6 (Column Space, Null Space, Inner Product and Norm) Associated with an $m \times n$ matrix $\boldsymbol{X}=\left[\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right]$, where $\boldsymbol{x}_{j} \in \mathcal{V}, j=1, \ldots, n$ are the following subspaces of $\mathcal{V}$.

1. The subspace $\mathcal{R}(\boldsymbol{X})$ is called the column space of $\boldsymbol{X}$. It is the smallest subspace containing $\mathcal{X}=\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$. The dimension of $\mathcal{R}(\boldsymbol{X})$ is called the rank of $\boldsymbol{X}$. The matrix $\boldsymbol{X}$ has rank $n$ if and only if it has linearly independent columns.
2. $\mathcal{R}\left(\boldsymbol{X}^{T}\right)$ is called the row space of $\boldsymbol{X}$. It is generated by the rows of $\boldsymbol{X}$ written as column vectors.
3. The subspace $\mathcal{N}(\boldsymbol{X}):=\left\{\boldsymbol{y} \in \mathbb{R}^{n}: \boldsymbol{X} \boldsymbol{y}=\mathbf{0}\right\}$ is called the null space or kernel space of $\boldsymbol{X}$. The dimension of $\mathcal{N}(\boldsymbol{X})$ is called the nullity of $\boldsymbol{X}$ and denoted $\operatorname{null}(\boldsymbol{X})$.
4. The standard inner product is

$$
\langle\boldsymbol{x}, \boldsymbol{y}\rangle:=\boldsymbol{y}^{*} \boldsymbol{x}=\boldsymbol{x}^{T} \overline{\boldsymbol{y}}=\sum_{j=1}^{n} x_{j} \overline{y_{j}} .
$$

5. The Euclidian norm is defined by

$$
\|x\|_{2}:=\left(\sum_{j=1}^{n}\left|x_{j}\right|^{2}\right)^{1 / 2}=\sqrt{x^{*} x} .
$$

Clearly $\mathcal{N}(\boldsymbol{X})$ is nontrivial if and only if $\boldsymbol{X}$ has linearly dependent columns. Inner products and norms are treated in more generality in Chaps. 5 and 8.

The following Theorem is shown in any basic course in linear algebra. See Exercise 7.10 for a simple proof using the singular value decomposition.

Theorem 1.5 (Counting Dimensions of Fundamental Subspaces) Suppose $\boldsymbol{X} \in$ $\mathbb{C}^{m \times n}$. Then

1. $\operatorname{rank}(\boldsymbol{X})=\operatorname{rank}\left(\boldsymbol{X}^{*}\right)$.
2. $\operatorname{rank}(\boldsymbol{X})+\operatorname{null}(\boldsymbol{X})=n$,
3. $\operatorname{rank}(\boldsymbol{X})+\operatorname{null}\left(\boldsymbol{X}^{*}\right)=m$,

### 1.3 Linear Systems

Consider a linear system

$$
\begin{array}{ccc}
a_{11} x_{1}+a_{12} x_{2}+\cdots+ & a_{1 n} x_{n}=b_{1} \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+ & a_{2 n} x_{n}= & b_{2} \\
\vdots & \vdots & \vdots \\
a_{m 1} x_{1}+a_{m 2} x_{2}+\cdots+ & \vdots \\
a_{m n} x_{n} & =b_{m}
\end{array}
$$

of $m$ equations in $n$ unknowns. Here for all $i, j$, the coefficients $a_{i j}$, the unknowns $x_{j}$, and the components $b_{i}$ of the right hand side are real or complex numbers. The system can be written as a vector equation

$$
x_{1} \boldsymbol{a}_{1}+x_{2} \boldsymbol{a}_{2}+\cdots+x_{n} \boldsymbol{a}_{n}=\boldsymbol{b},
$$

where $\boldsymbol{a}_{j}=\left[a_{1 j}, \ldots, \boldsymbol{a}_{m j}\right]^{T} \in \mathbb{C}^{m}$ for $j=1, \ldots, n$ and $\boldsymbol{b}=\left[b_{1}, \ldots, b_{m}\right]^{T} \in \mathbb{C}^{m}$. It can also be written as a matrix equation

$$
\boldsymbol{A} \boldsymbol{x}=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]\left[\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right]=\left[\begin{array}{c}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{array}\right]=\boldsymbol{b} .
$$

The system is homogeneous if $\boldsymbol{b}=\mathbf{0}$ and it is said to be underdetermined, square, or overdetermined if $m<n, m=n$, or $m>n$, respectively.

### 1.3.1 Basic Properties

A linear system has a unique solution, infinitely many solutions, or no solution. To discuss this we first consider the real case, and a homogeneous underdetermined system.

Lemma 1.3 (Underdetermined System) Suppose $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ with $m<n$. Then there is a nonzero $\boldsymbol{x} \in \mathbb{R}^{n}$ such that $\boldsymbol{A x}=\mathbf{0}$.

Proof Suppose $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ with $m<n$. The $n$ columns of $\boldsymbol{A}$ span a subspace of $\mathbb{R}^{m}$. Since $\mathbb{R}^{m}$ has dimension $m$ the dimension of this subspace is at most $m$. By Lemma 1.1 the columns of $\boldsymbol{A}$ must be linearly dependent. It follows that there is a nonzero $\boldsymbol{x} \in \mathbb{R}^{n}$ such that $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$. $\square$

A square matrix is either nonsingular or singular.
Definition 1.7 (Real Nonsingular or Singular Matrix) A square matrix $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$ is said to be nonsingular if the only real solution of the homogeneous system $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$ is $\boldsymbol{x}=\mathbf{0}$. The matrix is singular if there is a nonzero $\boldsymbol{x} \in \mathbb{R}^{n}$ such that $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$.

Theorem 1.6 (Linear Systems; Existence and Uniqueness) Suppose $\boldsymbol{A} \in \mathbb{R}^{n \times n}$. The linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ has a unique solution $\boldsymbol{x} \in \mathbb{R}^{n}$ for any $\boldsymbol{b} \in \mathbb{R}^{n}$ if and only if the matrix $\boldsymbol{A}$ is nonsingular.

Proof Suppose $\boldsymbol{A}$ is nonsingular. We define $\boldsymbol{B}=[\boldsymbol{A} \boldsymbol{b}] \in \mathbb{R}^{n \times(n+1)}$ by adding a column to $\boldsymbol{A}$. By Lemma 1.3 there is a nonzero $\boldsymbol{z} \in \mathbb{R}^{n+1}$ such that $\boldsymbol{B} \boldsymbol{z}=\mathbf{0}$. If we write $\boldsymbol{z}=\left[\begin{array}{c}\tilde{\boldsymbol{z}} \\ z_{n+1}\end{array}\right]$ where $\tilde{\boldsymbol{z}}=\left[z_{1}, \ldots, z_{n}\right]^{T} \in \mathbb{R}^{n}$ and $z_{n+1} \in \mathbb{R}$, then

$$
\boldsymbol{B} z=\left[\begin{array}{ll}
\boldsymbol{A} & \boldsymbol{b}
\end{array}\right]\left[\begin{array}{c}
\tilde{\boldsymbol{z}} \\
z_{n+1}
\end{array}\right]=\boldsymbol{A} \tilde{\boldsymbol{z}}+z_{n+1} \boldsymbol{b}=\mathbf{0} .
$$

We cannot have $z_{n+1}=0$ for then $\boldsymbol{A} \tilde{\boldsymbol{z}}=\mathbf{0}$ for a nonzero $\tilde{\boldsymbol{z}}$, contradicting the nonsingularity of $\boldsymbol{A}$. Define $\boldsymbol{x}:=-\tilde{\boldsymbol{z}} / z_{n+1}$. Then

$$
\boldsymbol{A} \boldsymbol{x}=-\boldsymbol{A}\left(\frac{\tilde{\boldsymbol{z}}}{z_{n+1}}\right)=-\frac{1}{z_{n+1}} \boldsymbol{A} \tilde{\boldsymbol{z}}=-\frac{1}{z_{n+1}}\left(-z_{n+1} \boldsymbol{b}\right)=\boldsymbol{b},
$$

so $\boldsymbol{x}$ is a solution.
Suppose $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ and $\boldsymbol{A} \boldsymbol{y}=\boldsymbol{b}$ for $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$. Then $\boldsymbol{A}(\boldsymbol{x}-\boldsymbol{y})=\mathbf{0}$ and since $\boldsymbol{A}$ is nonsingular we conclude that $\boldsymbol{x}-\boldsymbol{y}=\mathbf{0}$ or $\boldsymbol{x}=\boldsymbol{y}$. Thus the solution is unique.

Conversely, if $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ has a unique solution for any $\boldsymbol{b} \in \mathbb{R}^{n}$ then $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$ has a unique solution which must be $\boldsymbol{x}=\mathbf{0}$. Thus $\boldsymbol{A}$ is nonsingular. $\square$

For the complex case we have
Lemma 1.4 (Complex Underdetermined System) Suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ with $m<$ $n$. Then there is a nonzero $\boldsymbol{x} \in \mathbb{C}^{n}$ such that $\boldsymbol{A x}=\mathbf{0}$.

Definition 1.8 (Complex Nonsingular Matrix) A square matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is said to be nonsingular if the only complex solution of the homogeneous system $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$ is $\boldsymbol{x}=\mathbf{0}$. The matrix is singular if it is not nonsingular.

Theorem 1.7 (Complex Linear System; Existence and Uniqueness) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. The linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ has a unique solution $\boldsymbol{x} \in \mathbb{C}^{n}$ for any $\boldsymbol{b} \in \mathbb{C}^{n}$ if and only if the matrix $\boldsymbol{A}$ is nonsingular.

### 1.3.2 The Inverse Matrix

Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is a square matrix. A matrix $\boldsymbol{B} \in \mathbb{C}^{n \times n}$ is called a right inverse of $\boldsymbol{A}$ if $\boldsymbol{A} \boldsymbol{B}=\boldsymbol{I}$. A matrix $\boldsymbol{C} \in \mathbb{C}^{n \times n}$ is said to be a left inverse of $\boldsymbol{A}$ if $\boldsymbol{C} \boldsymbol{A}=\boldsymbol{I}$. We say that $\boldsymbol{A}$ is invertible if it has both a left- and a right inverse. If $\boldsymbol{A}$ has a right inverse $\boldsymbol{B}$ and a left inverse $\boldsymbol{C}$ then

$$
C=C I=C(A B)=(C A) B=I B=B
$$

and this common inverse is called the inverse of $\boldsymbol{A}$ and denoted by $\boldsymbol{A}^{-1}$. Thus the inverse satisfies $\boldsymbol{A}^{-1} \boldsymbol{A}=\boldsymbol{A} \boldsymbol{A}^{-1}=\boldsymbol{I}$.

We want to characterize the class of invertible matrices and start with a lemma.
Theorem 1.8 (Product of Nonsingular Matrices) If $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C} \in \mathbb{C}^{n \times n}$ with $\boldsymbol{A} \boldsymbol{B}=$ $\boldsymbol{C}$ then $\boldsymbol{C}$ is nonsingular if and only if both $\boldsymbol{A}$ and $\boldsymbol{B}$ are nonsingular. In particular, if either $\boldsymbol{A} \boldsymbol{B}=\boldsymbol{I}$ or $\boldsymbol{B} \boldsymbol{A}=\boldsymbol{I}$ then $\boldsymbol{A}$ is nonsingular and $\boldsymbol{A}^{-1}=\boldsymbol{B}$.

Proof Suppose both $\boldsymbol{A}$ and $\boldsymbol{B}$ are nonsingular and let $\boldsymbol{C} \boldsymbol{x}=\mathbf{0}$. Then $\boldsymbol{A} \boldsymbol{B} \boldsymbol{x}=\mathbf{0}$ and since $\boldsymbol{A}$ is nonsingular we see that $\boldsymbol{B} \boldsymbol{x}=\mathbf{0}$. Since $\boldsymbol{B}$ is nonsingular we have $\boldsymbol{x}=\mathbf{0}$. We conclude that $\boldsymbol{C}$ is nonsingular.

For the converse suppose first that $\boldsymbol{B}$ is singular and let $\boldsymbol{x} \in \mathbb{C}^{n}$ be a nonzero vector so that $\boldsymbol{B} \boldsymbol{x}=\mathbf{0}$. But then $\boldsymbol{C} \boldsymbol{x}=(\boldsymbol{A} \boldsymbol{B}) \boldsymbol{x}=\boldsymbol{A}(\boldsymbol{B} \boldsymbol{x})=\boldsymbol{A} \mathbf{0}=\mathbf{0}$ so $\boldsymbol{C}$ is singular. Finally suppose $\boldsymbol{B}$ is nonsingular, but $\boldsymbol{A}$ is singular. Let $\tilde{\boldsymbol{x}}$ be a nonzero vector such that $\boldsymbol{A} \tilde{\boldsymbol{x}}=\mathbf{0}$. By Theorem 1.7 there is a vector $\boldsymbol{x}$ such that $\boldsymbol{B} \boldsymbol{x}=\tilde{\boldsymbol{x}}$ and $\boldsymbol{x}$ is nonzero since $\tilde{\boldsymbol{x}}$ is nonzero. But then $\boldsymbol{C} \boldsymbol{x}=(\boldsymbol{A} \boldsymbol{B}) \boldsymbol{x}=\boldsymbol{A}(\boldsymbol{B} \boldsymbol{x})=\boldsymbol{A} \tilde{\boldsymbol{x}}=\mathbf{0}$ for a nonzero vector $\boldsymbol{x}$ and $\boldsymbol{C}$ is singular. $\square$

Theorem 1.9 (When Is a Square Matrix Invertible?) A square matrix is invertible if and only if it is nonsingular.

Proof Suppose first $\boldsymbol{A}$ is a nonsingular matrix. By Theorem 1.7 each of the linear systems $\boldsymbol{A} \boldsymbol{b}_{i}=\boldsymbol{e}_{i}$ has a unique solution $\boldsymbol{b}_{i}$ for $i=1, \ldots, n$. Let $\boldsymbol{B}=\left[\boldsymbol{b}_{1}, \ldots, \boldsymbol{b}_{n}\right]$. Then $\boldsymbol{A} \boldsymbol{B}=\left[\boldsymbol{A} \boldsymbol{b}_{1}, \ldots, \boldsymbol{A} \boldsymbol{b}_{n}\right]=\left[\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{n}\right]=\boldsymbol{I}$ so that $\boldsymbol{A}$ has a right inverse $\boldsymbol{B}$. By Theorem $1.8 \boldsymbol{B}$ is nonsingular since $\boldsymbol{I}$ is nonsingular and $\boldsymbol{A} \boldsymbol{B}=\boldsymbol{I}$. Since $\boldsymbol{B}$ is nonsingular we can use what we have shown for $\boldsymbol{A}$ to conclude that $\boldsymbol{B}$ has a right inverse $\boldsymbol{C}$, i.e. $\boldsymbol{B} \boldsymbol{C}=\boldsymbol{I}$. But then $\boldsymbol{A} \boldsymbol{B}=\boldsymbol{B} \boldsymbol{C}=\boldsymbol{I}$ so $\boldsymbol{B}$ has both a right inverse and a left inverse which must be equal so $\boldsymbol{A}=\boldsymbol{C}$. Since $\boldsymbol{B} \boldsymbol{C}=\boldsymbol{I}$ we have $\boldsymbol{B} \boldsymbol{A}=\boldsymbol{I}$, so $\boldsymbol{B}$ is also a left inverse of $\boldsymbol{A}$ and $\boldsymbol{A}$ is invertible.

Conversely, if $\boldsymbol{A}$ is invertible then it has a right inverse $\boldsymbol{B}$. Since $\boldsymbol{A} \boldsymbol{B}=\boldsymbol{I}$ and $\boldsymbol{I}$ is nonsingular, we again use Theorem 1.8 to conclude that $\boldsymbol{A}$ is nonsingular. $\square$

To verify that some matrix $\boldsymbol{B}$ is an inverse of another matrix $\boldsymbol{A}$ it is enough to show that $\boldsymbol{B}$ is either a left inverse or a right inverse of $\boldsymbol{A}$. This calculation also proves that $\boldsymbol{A}$ is nonsingular. We use this observation to give simple proofs of the following results.

Corollary 1.2 (Basic Properties of the Inverse Matrix) Suppose $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$ are nonsingular and $c$ is a nonzero constant.

1. $\boldsymbol{A}^{-1}$ is nonsingular and $\left(\boldsymbol{A}^{-1}\right)^{-1}=\boldsymbol{A}$.
2. $\boldsymbol{C}=\boldsymbol{A} \boldsymbol{B}$ is nonsingular and $\boldsymbol{C}^{-1}=\boldsymbol{B}^{-1} \boldsymbol{A}^{-1}$.
3. $\boldsymbol{A}^{T}$ is nonsingular and $\left(\boldsymbol{A}^{T}\right)^{-1}=\left(\boldsymbol{A}^{-1}\right)^{T}=: \boldsymbol{A}^{-T}$.
4. $\boldsymbol{A}^{*}$ is nonsingular and $\left(\boldsymbol{A}^{*}\right)^{-1}=\left(\boldsymbol{A}^{-1}\right)^{*}=: \boldsymbol{A}^{-*}$.
5. $c \boldsymbol{A}$ is nonsingular and $(c \boldsymbol{A})^{-1}=\frac{1}{c} \boldsymbol{A}^{-1}$.

Proof

1. Since $\boldsymbol{A}^{-1} \boldsymbol{A}=\boldsymbol{I}$ the matrix $\boldsymbol{A}$ is a right inverse of $\boldsymbol{A}^{-1}$. Thus $\boldsymbol{A}^{-1}$ is nonsingular and $\left(\boldsymbol{A}^{-1}\right)^{-1}=\boldsymbol{A}$.
2. We note that $\left(\boldsymbol{B}^{-1} \boldsymbol{A}^{-1}\right)(\boldsymbol{A} \boldsymbol{B})=\boldsymbol{B}^{-1}\left(\boldsymbol{A}^{-1} \boldsymbol{A}\right) \boldsymbol{B}=\boldsymbol{B}^{-1} \boldsymbol{B}=\boldsymbol{I}$. Thus $\boldsymbol{A} \boldsymbol{B}$ is invertible with the indicated inverse since it has a left inverse.
3. Now $\boldsymbol{I}=\boldsymbol{I}^{T}=\left(\boldsymbol{A}^{-1} \boldsymbol{A}\right)^{T}=\boldsymbol{A}^{T}\left(\boldsymbol{A}^{-1}\right)^{T}$ showing that $\left(\boldsymbol{A}^{-1}\right)^{T}$ is a right inverse of $\boldsymbol{A}^{T}$. The proof of part 4 is similar.
4. The matrix $\frac{1}{c} \boldsymbol{A}^{-1}$ is a one sided inverse of $c \boldsymbol{A}$.

### 1.4 Determinants

The first systematic treatment of determinants was given by Cauchy in 1812. He adopted the word "determinant". The first use of determinants was made by Leibniz in 1693 in a letter to De L'Hôspital. By the beginning of the twentieth century the theory of determinants filled four volumes of almost 2000 pages (Muir, 1906-1923. Historic references can be found in this work). The main use of determinants in this text will be to study the characteristic polynomial of a matrix and to show that a matrix is nonsingular.

For any $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ the determinant of $\boldsymbol{A}$ is defined by the number

$$
\operatorname{det}(\boldsymbol{A})=\sum_{\sigma \in S_{n}} \operatorname{sign}(\sigma) a_{\sigma(1), 1} a_{\sigma(2), 2} \cdots a_{\sigma(n), n}
$$

This sum ranges of all $n!$ permutations of $\{1,2, \ldots, n\}$. Moreover, $\operatorname{sign}(\sigma)$ equals the number of times a bigger integer precedes a smaller one in $\sigma$. We also denote the determinant by (Cayley, 1841)

$$
\left|\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right| .
$$

From the definition we have

$$
\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|=a_{11} a_{22}-a_{21} a_{12} .
$$

The first term on the right corresponds to the identity permutation $\epsilon$ given by $\epsilon(i)=$ $i, i=1,2$. The second term comes from the permutation $\sigma=\{2,1\}$. For $n=3$ there are six permutations of $\{1,2,3\}$. Then

$$
\begin{aligned}
&\left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|=a_{11} a_{22} a_{33}-a_{11} a_{32} a_{23}-a_{21} a_{12} a_{33} \\
&+a_{21} a_{32} a_{13}+a_{31} a_{12} a_{23}-a_{31} a_{22} a_{13}
\end{aligned}
$$

This follows since $\operatorname{sign}(\{1,2,3\})=\operatorname{sign}(\{2,3,1\})=\operatorname{sign}(\{3,1,2\})=1$, and noting that interchanging two numbers in a permutation reverses it sign we find $\operatorname{sign}(\{2,1,3\})=\operatorname{sign}(\{3,2,1\})=\operatorname{sign}(\{1,3,2\})=-1$.

To compute the value of a determinant from the definition can be a trying experience. It is often better to use elementary operations on rows or columns to reduce it to a simpler form. For example, if $\boldsymbol{A}$ is triangular then $\operatorname{det}(\boldsymbol{A})=$
$a_{11} a_{22} \cdots a_{n n}$, the product of the diagonal elements. In particular, for the identity matrix $\operatorname{det}(\boldsymbol{I})=1$. The elementary operations using either rows or columns are

1. Interchanging two rows(columns): $\operatorname{det}(\boldsymbol{B})=-\operatorname{det}(\boldsymbol{A})$,
2. Multiply a row(column) by a scalar: $\alpha, \operatorname{det}(\boldsymbol{B})=\alpha \operatorname{det}(\boldsymbol{A})$,
3. Add a constant multiple of one row(column) to another row(column):
$$
\operatorname{det}(\boldsymbol{B})=\operatorname{det}(\boldsymbol{A}) .
$$

where $\boldsymbol{B}$ is the result of performing the indicated operation on $\boldsymbol{A}$.
If only a few elements in a row or column are nonzero then a cofactor expansion can be used. These expansions take the form

$$
\begin{aligned}
\operatorname{det}(\boldsymbol{A}) & =\sum_{j=1}^{n}(-1)^{i+j} a_{i j} \operatorname{det}\left(\boldsymbol{A}_{i j}\right) \text { for } i=1, \ldots, n, \text { row } \\
\operatorname{det}(\boldsymbol{A}) & =\sum_{i=1}^{n}(-1)^{i+j} a_{i j} \operatorname{det}\left(\boldsymbol{A}_{i j}\right) \text { for } j=1, \ldots, n, \text { column. }
\end{aligned}
$$

Here $\boldsymbol{A}_{i, j}$ denotes the submatrix of $\boldsymbol{A}$ obtained by deleting the $i$ th row and $j$ th column of $\boldsymbol{A}$. For $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ and $1 \leq i, j \leq n$ the determinant $\operatorname{det}\left(\boldsymbol{A}_{i j}\right)$ is called the cofactor of $a_{i j}$.

Example 1.3 (Determinant Equation for a Straight Line) The equation for a straight line through two points $\left(x_{1}, y_{1}\right)$ and $\left(x_{2}, y_{2}\right)$ in the plane can be written as the equation

$$
\operatorname{det}(\boldsymbol{A}):=\left|\begin{array}{ccc}
1 & x & y \\
1 & x_{1} & y_{1} \\
1 & x_{2} & y_{2}
\end{array}\right|=0
$$

involving a determinant of order 3. We can compute this determinant using row operations of type 3. Subtracting row 2 from row 3 and then row 1 from row 2, and then using a cofactor expansion on the first column we obtain

$$
\begin{aligned}
\left|\begin{array}{ccc}
1 & x & y \\
1 & x_{1} & y_{1} \\
1 & x_{2} & y_{2}
\end{array}\right| & =\left|\begin{array}{ccc}
1 & x & y \\
0 & x_{1}-x & y_{1}-y \\
0 & x_{2}-x_{1} & y_{2}-y_{1}
\end{array}\right| \\
& =\left|\begin{array}{cc}
x_{1}-x & y_{1}-y \\
x_{2}-x_{1} & y_{2}-y_{1}
\end{array}\right|=\left(x_{1}-x\right)\left(y_{2}-y_{1}\right)-\left(y_{1}-y\right)\left(x_{2}-x_{1}\right)
\end{aligned}
$$

Rearranging the equation $\operatorname{det}(\boldsymbol{A})=0$ we obtain

$$
y-y_{1}=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}\left(x-x_{1}\right)
$$

which is the slope form of the equation of a straight line.
We will freely use, without proofs, the following properties of determinants. If $\boldsymbol{A}, \boldsymbol{B}$ are square matrices of order $n$ with real or complex elements, then

1. $\operatorname{det}(\boldsymbol{A B})=\operatorname{det}(\boldsymbol{A}) \operatorname{det}(\boldsymbol{B})$.
2. $\operatorname{det}\left(\boldsymbol{A}^{T}\right)=\operatorname{det}(\boldsymbol{A})$, and $\operatorname{det}\left(\boldsymbol{A}^{*}\right)=\overline{\operatorname{det}(\boldsymbol{A})}$, (complex conjugate).
3. $\operatorname{det}(a \boldsymbol{A})=a^{n} \operatorname{det}(\boldsymbol{A})$, for $a \in \mathbb{C}$.
4. $\boldsymbol{A}$ is singular if and only if $\operatorname{det}(\boldsymbol{A})=0$.
5. If $\boldsymbol{A}=\left[\begin{array}{ll}\boldsymbol{C} & \boldsymbol{D} \\ \mathbf{0} & \boldsymbol{E}\end{array}\right]$ for some square matrices $\boldsymbol{C}, \boldsymbol{E}$ then $\operatorname{det}(\boldsymbol{A})=\operatorname{det}(\boldsymbol{C}) \operatorname{det}(\boldsymbol{E})$.
6. Cramer's rule Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular and $\boldsymbol{b} \in \mathbb{C}^{n}$. Let $\boldsymbol{x}=$ $\left[x_{1}, x_{2}, \ldots, x_{n}\right]^{T}$ be the unique solution of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Then
$$
x_{j}=\frac{\operatorname{det}\left(\boldsymbol{A}_{j}(\boldsymbol{b})\right)}{\operatorname{det}(\boldsymbol{A})}, \quad j=1,2, \ldots, n,
$$
where $\boldsymbol{A}_{j}(\boldsymbol{b})$ denote the matrix obtained from $\boldsymbol{A}$ by replacing the $j$ th column of $\boldsymbol{A}$ by $\boldsymbol{b}$.
7. Adjoint formula for the inverse. If $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular then
$$
\boldsymbol{A}^{-1}=\frac{1}{\operatorname{det}(\boldsymbol{A})} \operatorname{adj}(\boldsymbol{A}),
$$
where the matrix $\operatorname{adj}(\boldsymbol{A}) \in \mathbb{C}^{n \times n}$ with elements $\operatorname{adj}(\boldsymbol{A})_{i, j}=(-1)^{i+j} \operatorname{det}\left(\boldsymbol{A}_{j, i}\right)$ is called the adjoint of $\boldsymbol{A}$. Moreover, $\boldsymbol{A}_{j, i}$ denotes the submatrix of $\boldsymbol{A}$ obtained by deleting the $j$ th row and $i$ th column of $\boldsymbol{A}$.
8. Cauchy-Binet formula: Let $\boldsymbol{A} \in \mathbb{C}^{m \times p}, \boldsymbol{B} \in \mathbb{C}^{p \times n}$ and $\boldsymbol{C}=\boldsymbol{A} \boldsymbol{B}$. Suppose $1 \leq r \leq \min \{m, n, p\}$ and let $\boldsymbol{i}=\left\{i_{1}, \ldots, i_{r}\right\}$ and $\boldsymbol{j}=\left\{j_{1}, \ldots, j_{r}\right\}$ be integers with $1 \leq i_{1}<i_{2}<\cdots<i_{r} \leq m$ and $1 \leq j_{1}<j_{2}<\cdots<j_{r} \leq n$. Then
$$
\left[\begin{array}{ccc}
c_{i_{1}, j_{1}} & \cdots & c_{i_{1}, j_{r}} \\
\vdots & & \vdots \\
c_{i_{r}, j_{1}} & \cdots & c_{i_{r}, j_{r}}
\end{array}\right]=\sum_{\boldsymbol{k}}\left[\begin{array}{ccc}
a_{i_{1}, k_{1}} & \cdots & a_{i_{1}, k_{r}} \\
\vdots & & \vdots \\
a_{i_{r} k_{1}} & \cdots & a_{i_{r}, k_{r}}
\end{array}\right]\left[\begin{array}{ccc}
b_{k_{1}, j_{1}} & \cdots & b_{k_{1}, j_{r}} \\
\vdots & & \vdots \\
b_{k_{r}, j_{1}} & \cdots & b_{k_{r}, j_{r}}
\end{array}\right],
$$
where we sum over all $\boldsymbol{k}=\left\{k_{1}, \ldots, k_{r}\right\}$ with $1 \leq k_{1}<k_{2}<\cdots<k_{r} \leq p$. More compactly,
$$
\operatorname{det}(\boldsymbol{C}(\boldsymbol{i}, \boldsymbol{j}))=\sum_{\boldsymbol{k}} \operatorname{det}(\boldsymbol{A}(\boldsymbol{i}, \boldsymbol{k})) \operatorname{det}(\boldsymbol{B}(\boldsymbol{k}, \boldsymbol{j})),
$$
Note the resemblance to the formula for matrix multiplication.

### 1.5 Eigenvalues, Eigenvectors and Eigenpairs

Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is a square matrix, $\lambda \in \mathbb{C}$ and $\boldsymbol{x} \in \mathbb{C}^{n}$. We say that ( $\lambda, \boldsymbol{x}$ ) is an eigenpair for $\boldsymbol{A}$ if $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ and $\boldsymbol{x}$ is nonzero. The scalar $\lambda$ is called an eigenvalue and $\boldsymbol{x}$ is said to be an eigenvector. ${ }^{1}$ The set of eigenvalues is called the spectrum of $\boldsymbol{A}$ and is denoted by $\sigma(\boldsymbol{A})$. For example, $\sigma(\boldsymbol{I})=\{1, \ldots, 1\}=\{1\}$.

Eigenvalues are the roots of the characteristic polynomial.
Lemma 1.5 (Characteristic Equation) For any $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ we have $\lambda \in$ $\sigma(\boldsymbol{A}) \Longleftrightarrow \operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=0$.

Proof Suppose $(\lambda, \boldsymbol{x})$ is an eigenpair for $\boldsymbol{A}$. The equation $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ can be written $(\boldsymbol{A}-\lambda \boldsymbol{I}) \boldsymbol{x}=\mathbf{0}$. Since $\boldsymbol{x}$ is nonzero the matrix $\boldsymbol{A}-\lambda \boldsymbol{I}$ must be singular with a zero determinant. Conversely, if $\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=0$ then $\boldsymbol{A}-\lambda \boldsymbol{I}$ is singular and $(\boldsymbol{A}-\lambda \boldsymbol{I}) \boldsymbol{x}=\mathbf{0}$ for some nonzero $\boldsymbol{x} \in \mathbb{C}^{n}$. Thus $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ and $(\lambda, \boldsymbol{x})$ is an eigenpair for $\boldsymbol{A}$. $\square$

The expression $\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})$ is a polynomial of exact degree $n$ in $\lambda$. For $n=3$ we have

$$
\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=\left|\begin{array}{ccc}
a_{11}-\lambda & a_{12} & a_{13} \\
a_{21} & a_{22}-\lambda & a_{23} \\
a_{31} & a_{32} & a_{33}-\lambda
\end{array}\right| .
$$

Expanding this determinant by the first column we find

$$
\begin{aligned}
\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I}) & =\left(a_{11}-\lambda\right)\left|\begin{array}{cc}
a_{22}-\lambda & a_{23} \\
a_{32} & a_{33}-\lambda
\end{array}\right|-a_{21}\left|\begin{array}{cc}
a_{12} & a_{13} \\
a_{32} & a_{33}-\lambda
\end{array}\right| \\
& +a_{31}\left|\begin{array}{cc}
a_{12} & a_{13} \\
a_{22}-\lambda & a_{23}
\end{array}\right|=\left(a_{11}-\lambda\right)\left(a_{22}-\lambda\right)\left(a_{33}-\lambda\right)+r(\lambda)
\end{aligned}
$$

for some polynomial $r$ of degree at most one. In general

$$
\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=\left(a_{11}-\lambda\right)\left(a_{22}-\lambda\right) \cdots\left(a_{n n}-\lambda\right)+r(\lambda),
$$

where each term in $r(\lambda)$ has at most $n-2$ factors containing $\lambda$. It follows that $r$ is a polynomial of degree at most $n-2, \operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})$ is a polynomial of exact degree $n$ in $\lambda$ and the eigenvalues are the roots of this polynomial.

We observe that $\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=(-1)^{n} \operatorname{det}(\lambda \boldsymbol{I}-\boldsymbol{A})$ so $\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=0$ if and only if $\operatorname{det}(\lambda \boldsymbol{I}-\boldsymbol{A})=0$.

[^0]Definition 1.9 (Characteristic Polynomial of a Matrix) The function $\pi_{\boldsymbol{A}}: \mathbb{C} \rightarrow$ $\mathbb{C}$ given by $\pi_{\boldsymbol{A}}(\lambda)=\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})$ is called the characteristic polynomial of $\boldsymbol{A}$. The equation $\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=0$ is called the characteristic equation of $\boldsymbol{A}$.

By the fundamental theorem of algebra an $n \times n$ matrix has, counting multiplicities, precisely $n$ eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$ some of which might be complex even if $\boldsymbol{A}$ is real. The complex eigenpairs of a real matrix occur in complex conjugate pairs. Indeed, taking the complex conjugate on both sides of the equation $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ with $\boldsymbol{A}$ real gives $\boldsymbol{A} \overline{\boldsymbol{x}}=\bar{\lambda} \overline{\boldsymbol{x}}$.

Theorem 1.10 (Sums and Products of Eigenvalues; Trace) For any $\boldsymbol{A} \in \mathbb{C}^{n \times n}$

$$
\operatorname{trace}(\boldsymbol{A})=\lambda_{1}+\lambda_{2}+\cdots+\lambda_{n}, \quad \operatorname{det}(\boldsymbol{A})=\lambda_{1} \lambda_{2} \cdots \lambda_{n},
$$

where the trace of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is the sum of its diagonal elements

$$
\operatorname{trace}(\boldsymbol{A}):=a_{11}+a_{22}+\cdots+a_{n n} .
$$

Proof We compare two different expansions of $\pi_{\boldsymbol{A}}$. On the one hand from (1.16) we find

$$
\pi_{A}(\lambda)=(-1)^{n} \lambda^{n}+c_{n-1} \lambda^{n-1}+\cdots+c_{0},
$$

where $c_{n-1}=(-1)^{n-1} \operatorname{trace}(\boldsymbol{A})$ and $c_{0}=\pi_{\boldsymbol{A}}(0)=\operatorname{det}(\boldsymbol{A})$. On the other hand

$$
\pi_{A}(\lambda)=\left(\lambda_{1}-\lambda\right) \cdots\left(\lambda_{n}-\lambda\right)=(-1)^{n} \lambda^{n}+d_{n-1} \lambda^{n-1}+\cdots+d_{0},
$$

where $d_{n-1}=(-1)^{n-1}\left(\lambda_{1}+\cdots+\lambda_{n}\right)$ and $d_{0}=\lambda_{1} \cdots \lambda_{n}$. Since $c_{j}=d_{j}$ for all $j$ we obtain (1.17). $\square$

For a 2 × 2 matrix the characteristic equation takes the convenient form

$$
\lambda^{2}-\operatorname{trace}(\boldsymbol{A}) \lambda+\operatorname{det}(\boldsymbol{A})=0 .
$$

Thus, if $\boldsymbol{A}=\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$ then $\operatorname{trace}(\boldsymbol{A})=4, \operatorname{det}(\boldsymbol{A})=3$ so that $\pi_{\boldsymbol{A}}(\lambda)=\lambda^{2}-4 \lambda+3$.
Since $\boldsymbol{A}$ is singular $\Longleftrightarrow \boldsymbol{A} \boldsymbol{x}=\mathbf{0}$, some $\boldsymbol{x} \neq 0 \Longleftrightarrow \boldsymbol{A} \boldsymbol{x}=\mathbf{0} \boldsymbol{x}$, some $\boldsymbol{x} \neq$ $0 \Longleftrightarrow$ zero is an eigenvalue of $\boldsymbol{A}$, we obtain

Theorem 1.11 (Zero Eigenvalue) The matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is singular if and only if zero is an eigenvalue.

Since the determinant of a triangular matrix is equal to the product of the diagonal elements the eigenvalues of a triangular matrix are found on the diagonal. In general it is not easy to find all eigenvalues of a matrix. However, sometimes the dimension of the problem can be reduced. Since the determinant of a block triangular matrix is equal to the product of the determinants of the diagonal blocks we obtain

Theorem 1.12 (Eigenvalues of a Block Triangular Matrix) If $\boldsymbol{A}=\left[\begin{array}{cc}\boldsymbol{B} & \boldsymbol{D} \\ 0 & \boldsymbol{C}\end{array}\right]$ is block triangular then $\pi_{\boldsymbol{A}}=\pi_{\boldsymbol{B}} \cdot \pi_{\boldsymbol{C}}$.

### 1.6 Exercises Chap. 1

### 1.6.1 Exercises Sect. 1.1

Exercise 1.1 (Strassen Multiplication (Exam Exercise 2017-1)) (By arithmetic operations we mean additions, subtractions, multiplications and divisions.) Let $\boldsymbol{A}$ and $\boldsymbol{B}$ be $n \times n$ real matrices.

a) With $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{R}^{n \times n}$, how many arithmetic operations are required to form the product $\boldsymbol{A} \boldsymbol{B}$ ?
b) Consider the $2 n \times 2 n$ block matrix
$$
\left[\begin{array}{ll}
W & X \\
Y & Z
\end{array}\right]=\left[\begin{array}{ll}
A & B \\
C & D
\end{array}\right]\left[\begin{array}{ll}
E & F \\
G & H
\end{array}\right],
$$
where all matrices $\boldsymbol{A}, \ldots, \boldsymbol{Z}$ are in $\mathbb{R}^{n \times n}$. How many operations does it take to compute $\boldsymbol{W}, \boldsymbol{X}, \boldsymbol{Y}$ and $\boldsymbol{Z}$ by the obvious algorithm?
c) An alternative method to compute $\boldsymbol{W}, \boldsymbol{X}, \boldsymbol{Y}$ and $\boldsymbol{Z}$ is to use Strassen's formulas:
$$
\begin{array}{ll}
\mathbf{P}_{1}=(\boldsymbol{A}+\boldsymbol{D})(\boldsymbol{E}+\boldsymbol{H}), & \\
\mathbf{P}_{2}=(\boldsymbol{C}+\boldsymbol{D}) \boldsymbol{E}, & \mathbf{P}_{5}=(\boldsymbol{A}+\boldsymbol{B}) \boldsymbol{H}, \\
\mathbf{P}_{3}=\boldsymbol{A}(\boldsymbol{F}-\boldsymbol{H}), & \mathbf{P}_{6}=(\boldsymbol{C}-\boldsymbol{A})(\boldsymbol{E}+\boldsymbol{F}), \\
\mathbf{P}_{4}=\boldsymbol{D}(\boldsymbol{G}-\boldsymbol{E}), & \mathbf{P}_{7}=(\boldsymbol{B}-\boldsymbol{D})(\boldsymbol{G}+\boldsymbol{H}), \\
\boldsymbol{W}=\mathbf{P}_{1}+\mathbf{P}_{4}-\mathbf{P}_{5}+\mathbf{P}_{7}, & \boldsymbol{X}=\mathbf{P}_{3}+\mathbf{P}_{5}, \\
\boldsymbol{Y}=\mathbf{P}_{2}+\mathbf{P}_{4}, & \boldsymbol{Z}=\mathbf{P}_{1}+\mathbf{P}_{3}-\mathbf{P}_{2}+\mathbf{P}_{6} .
\end{array}
$$
You do not have to verify these formulas. What is the operation count for this method?
d) Describe a recursive algorithm, based on Strassen's formulas, which given two matrices $\boldsymbol{A}$ and $\boldsymbol{B}$ of size $m \times m$, with $m=2^{k}$ for some $k \geq 0$, calculates the product $\boldsymbol{A} \boldsymbol{B}$.
e) Show that the operation count of the recursive algorithm is $\mathcal{O}\left(m^{\log _{2}(7)}\right)$. Note that $\log _{2}(7) \approx 2.8<3$, so this is less costly than straightforward matrix multiplication.

### 1.6.2 Exercises Sect. 1.3

Exercise 1.2 (The Inverse of a General $2 \times 2$ Matrix) Show that

$$
\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]^{-1}=\alpha\left[\begin{array}{cc}
d & -b \\
-c & a
\end{array}\right], \quad \alpha=\frac{1}{a d-b c}
$$

for any $a, b, c, d$ such that $a d-b c \neq 0$.
Exercise 1.3 (The Inverse of a Special $2 \times 2$ Matrix) Find the inverse of

$$
A=\left[\begin{array}{cc}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{array}\right] .
$$

Exercise 1.4 (Sherman-Morrison Formula) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$, and $\boldsymbol{B}, \boldsymbol{C} \in$ $\mathbb{R}^{n \times m}$ for some $n, m \in \mathbb{N}$. If $\left(\boldsymbol{I}+\boldsymbol{C}^{T} \boldsymbol{A}^{-1} \boldsymbol{B}\right)^{-1}$ exists then

$$
\left(\boldsymbol{A}+\boldsymbol{B} \boldsymbol{C}^{T}\right)^{-1}=\boldsymbol{A}^{-1}-\boldsymbol{A}^{-1} \boldsymbol{B}\left(\boldsymbol{I}+\boldsymbol{C}^{T} \boldsymbol{A}^{-1} \boldsymbol{B}\right)^{-1} \boldsymbol{C}^{T} \boldsymbol{A}^{-1} .
$$

Exercise 1.5 (Inverse Update (Exam Exercise 1977-1))

a) Let $\boldsymbol{u}, \boldsymbol{v} \in \mathbb{R}^{n}$ and suppose $\boldsymbol{v}^{T} \boldsymbol{u} \neq 1$. Show that $\boldsymbol{I}-\boldsymbol{u} \boldsymbol{v}^{T}$ has an inverse given by $\boldsymbol{I}-\tau \boldsymbol{u} \boldsymbol{v}^{T}$, where $\tau=1 /\left(\boldsymbol{v}^{T} \boldsymbol{u}-1\right)$.
b) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be nonsingular with inverse $\boldsymbol{C}:=\boldsymbol{A}^{-1}$, and let $\boldsymbol{a} \in \mathbb{R}^{n}$. Let $\overline{\boldsymbol{A}}$ be the matrix which differs from $\boldsymbol{A}$ by exchanging the $i$ th row of $\boldsymbol{A}$ with $\boldsymbol{a}^{T}$, i.e., $\overline{\boldsymbol{A}}=\boldsymbol{A}-\boldsymbol{e}_{i}\left(\boldsymbol{e}_{i}^{T} \boldsymbol{A}-\boldsymbol{a}^{T}\right)$, where $\boldsymbol{e}_{i}$ is the $i$ th column in the identity matrix $\boldsymbol{I}$. Show that if
$$
\lambda:=\boldsymbol{a}^{T} \boldsymbol{C} \boldsymbol{e}_{i} \neq 0,
$$
then $\overline{\boldsymbol{A}}$ has an inverse $\overline{\boldsymbol{C}}=\overline{\boldsymbol{A}}^{-1}$ given by
$$
\overline{\boldsymbol{C}}=\boldsymbol{C}\left(\boldsymbol{I}+\frac{1}{\lambda} \boldsymbol{e}_{i}\left(\boldsymbol{e}_{i}^{T}-\boldsymbol{a}^{T} \boldsymbol{C}\right)\right)
$$
c) Write an algorithm which to given $\boldsymbol{C}$ and $\boldsymbol{a}$ checks if (1.20) holds and computes $\overline{\boldsymbol{C}}$ provided $\lambda \neq 0$. (hint: Use (1.21) to find formulas for computing each column in $\overline{\boldsymbol{C}}$. )

Exercise 1.6 (Matrix Products (Exam Exercise 2009-1)) Let $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}, \boldsymbol{E} \in$ $\mathbb{R}^{n \times n}$ be matrices where $\boldsymbol{A}^{T}=\boldsymbol{A}$. In this problem an (arithmetic) operation is an addition or a multiplication. We ask about exact numbers of operations.

a) How many operations are required to compute the matrix product $\boldsymbol{B} \boldsymbol{C}$ ? How many operations are required if $\boldsymbol{B}$ is lower triangular?
b) Show that there exists a lower triangular matrix $\boldsymbol{L} \in \mathbb{R}^{n \times n}$ such that $\boldsymbol{A}=\boldsymbol{L}+\boldsymbol{L}^{T}$.

c) We have $\boldsymbol{E}^{T} \boldsymbol{A} \boldsymbol{E}=\boldsymbol{S}+\boldsymbol{S}^{T}$ where $\boldsymbol{S}=\boldsymbol{E}^{T} \boldsymbol{L} \boldsymbol{E}$. How many operations are required to compute $\boldsymbol{E}^{T} \boldsymbol{A} \boldsymbol{E}$ in this way?

### 1.6.3 Exercises Sect. 1.4

Exercise 1.7 (Cramer's Rule; Special Case) Solve the following system by Cramer's rule:

$$
\left[\begin{array}{ll}
1 & 2 \\
2 & 1
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{l}
3 \\
6
\end{array}\right]
$$

Exercise 1.8 (Adjoint Matrix; Special Case) Show that if

$$
\boldsymbol{A}=\left[\begin{array}{ccc}
2 & -6 & 3 \\
3 & -2 & -6 \\
6 & 3 & 2
\end{array}\right],
$$

then

$$
\operatorname{adj}(\boldsymbol{A})=\left[\begin{array}{ccc}
14 & 21 & 42 \\
-42 & -14 & 21 \\
21 & -42 & 14
\end{array}\right] .
$$

Moreover,

$$
\operatorname{adj}(\boldsymbol{A}) \boldsymbol{A}=\left[\begin{array}{ccc}
343 & 0 & 0 \\
0 & 343 & 0 \\
0 & 0 & 343
\end{array}\right]=\operatorname{det}(\boldsymbol{A}) \boldsymbol{I} .
$$

Exercise 1.9 (Determinant Equation for a Plane) Show that

$$
\left|\begin{array}{llll}
x & y & z & 1 \\
x_{1} & y_{1} & z_{1} & 1 \\
x_{2} & y_{2} & z_{2} & 1 \\
x_{3} & y_{3} & z_{3} & 1
\end{array}\right|=0
$$

is the equation for a plane through three points $\left(x_{1}, y_{1}, z_{1}\right),\left(x_{2}, y_{2}, z_{2}\right),\left(x_{3}, y_{3}, z_{3}\right)$ in space.

Fig. 1.1 The triangle $T$ defined by the three points $P_{1}, P_{2}$ and $P_{3}$
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-043.jpg?height=441&width=635&top_left_y=213&top_left_x=705)

Exercise 1.10 (Signed Area of a Triangle) Let $P_{i}=\left(x_{i}, y_{i}\right), i=1,2,3$, be three points in the plane defining a triangle $T$. Show that the area of $T \mathrm{is}^{2}$

$$
A(T)=\frac{1}{2}\left|\begin{array}{ccc}
1 & 1 & 1 \\
x_{1} & x_{2} & x_{3} \\
y_{1} & y_{2} & y_{3}
\end{array}\right| .
$$

The area is positive if we traverse the vertices in counterclockwise order.
Exercise 1.11 (Vandermonde Matrix) Show that

$$
\left|\begin{array}{ccccc}
1 & x_{1} & x_{1}^{2} & \cdots & x_{1}^{n-1} \\
1 & x_{2} & x_{2}^{2} & \cdots & x_{2}^{n-1} \\
\vdots & \vdots & \vdots & & \vdots \\
1 & x_{n} & x_{n}^{2} & \cdots & x_{n}^{n-1}
\end{array}\right|=\prod_{i>j}\left(x_{i}-x_{j}\right),
$$

where $\prod_{i>j}\left(x_{i}-x_{j}\right)=\prod_{i=2}^{n}\left(x_{i}-x_{1}\right)\left(x_{i}-x_{2}\right) \cdots\left(x_{i}-x_{i-1}\right)$. This determinant is called the Vandermonde determinant. ${ }^{3}$

Exercise 1.12 (Cauchy Determinant (1842)) Let $\boldsymbol{\alpha}=\left[\alpha_{1}, \ldots, \alpha_{n}\right]^{T}, \boldsymbol{\beta}=$ $\left[\beta_{1}, \ldots, \beta_{n}\right]^{T}$ be in $\mathbb{R}^{n}$.

a) Consider the matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ with elements $a_{i, j}=1 /\left(\alpha_{i}+\beta_{j}\right), i, j=$ $1,2, \ldots, n$. Show that
$$
\operatorname{det}(\boldsymbol{A})=P g(\boldsymbol{\alpha}) g(\boldsymbol{\beta})
$$

[^1]

where $P=\prod_{i=1}^{n} \prod_{j=1}^{n} a_{i j}$, and for $\boldsymbol{\gamma}=\left[\gamma_{1}, \ldots, \gamma_{n}\right]^{T}$
$$
g(\boldsymbol{\gamma})=\prod_{i=2}^{n}\left(\gamma_{i}-\gamma_{1}\right)\left(\gamma_{i}-\gamma_{2}\right) \cdots\left(\gamma_{i}-\gamma_{i-1}\right)
$$
Hint: Multiply the $i$ th row of $\boldsymbol{A}$ by $\prod_{j=1}^{n}\left(\alpha_{i}+\beta_{j}\right)$ for $i=1,2, \ldots, n$. Call the resulting matrix $\boldsymbol{C}$. Each element of $\boldsymbol{C}$ is a product of $n-1$ factors $\alpha_{r}+\beta_{s}$. Hence $\operatorname{det}(\boldsymbol{C})$ is a sum of terms where each term contain precisely $n(n-1)$ factors $\alpha_{r}+\beta_{s}$. Thus $\operatorname{det}(\boldsymbol{C})=q(\alpha, \beta)$ where $q$ is a polynomial of degree at most $n(n-1)$ in $\alpha_{i}$ and $\beta_{j}$. Since $\operatorname{det}(\boldsymbol{A})$ and therefore $\operatorname{det}(\boldsymbol{C})$ vanishes if $\alpha_{i}=\alpha_{j}$ for some $i \neq j$ or $\beta_{r}=\beta_{s}$ for some $r \neq s$, we have that $q(\boldsymbol{\alpha}, \boldsymbol{\beta})$ must be divisible by each factor in $g(\boldsymbol{\alpha})$ and $g(\boldsymbol{\beta})$. Since $g(\boldsymbol{\alpha})$ and $g(\boldsymbol{\beta})$ is a polynomial of degree $n(n-1)$, we have
$$
q(\boldsymbol{\alpha}, \boldsymbol{\beta})=k g(\boldsymbol{\alpha}) g(\boldsymbol{\beta})
$$
for some constant $k$ independent of $\boldsymbol{\alpha}$ and $\boldsymbol{\beta}$. Show that $k=1$ by choosing $\beta_{i}+\alpha_{i}=0, i=1,2, \ldots, n$.
b)Notice that the cofactor of any element in the above matrix $\boldsymbol{A}$ is the determinant of a matrix of similar form. Use the cofactor and determinant of $\boldsymbol{A}$ to represent the elements of $\boldsymbol{A}^{-1}=\left(b_{j, k}\right)$. Answer:
$$
b_{j, k}=\left(\alpha_{k}+\beta_{j}\right) A_{k}\left(-\beta_{j}\right) B_{j}\left(-\alpha_{k}\right),
$$
where
$$
A_{k}(x)=\prod_{s \neq k}\left(\frac{\alpha_{s}-x}{\alpha_{s}-\alpha_{k}}\right), \quad B_{k}(x)=\prod_{s \neq k}\left(\frac{\beta_{s}-x}{\beta_{s}-\beta_{k}}\right) .
$$


Exercise 1.13 (Inverse of the Hilbert Matrix) Let $\boldsymbol{H}_{n}=\left(h_{i, j}\right)$ be the $n \times n$ matrix with elements $h_{i, j}=1 /(i+j-1)$. Use Exercise 1.12 to show that the elements $t_{i, j}^{n}$ in $\boldsymbol{T}_{n}=\boldsymbol{H}_{n}^{-1}$ are given by

$$
t_{i, j}^{n}=\frac{f(i) f(j)}{i+j-1},
$$

where

$$
f(i+1)=\left(\frac{i^{2}-n^{2}}{i^{2}}\right) f(i), \quad i=1,2, \ldots, \quad f(1)=-n .
$$

## Part I LU and QR Factorizations

The first three chapters in this part consider ways of factoring a matrix $\boldsymbol{A}$ into a lower triangular matrix $\boldsymbol{L}$ and an upper triangular matrix $\boldsymbol{U}$ resulting in the product $\boldsymbol{A}=$ $\boldsymbol{L} \boldsymbol{U}$. We also consider the factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{D} \boldsymbol{U}$, where $\boldsymbol{L}$ is lower triangular, $\boldsymbol{D}$ is diagonal and $\boldsymbol{U}$ is upper triangular. Moreover, $\boldsymbol{L}$ and $\boldsymbol{U}$ have ones on their respective diagonals.

Three simple introductory problems and related LU factorizations are considered in Chap. 2. We also consider some basic properties of triangular matrices and the powerful tool of block multiplication. We consider Gaussian elimination, it's relation to LU factorization, and the general theory of LU factorizations in Chap. 3. Symmetric positive definite matrices, where LU factorizations play an important role, are considered in Chap. 4.

There exists problems where Gaussian elimination leads to inaccurate results. Such problems can to a large extent be avoided by using an alternative method based on QR factorization. Here $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$, where $\boldsymbol{Q}$ is unitary, i.e., $\boldsymbol{Q}^{*} \boldsymbol{Q}=\boldsymbol{I}$, and $\boldsymbol{R}$ is upper triangular. QR factorization is related to Gram-Schmidt orthogonalization of a basis in a vector space. The QR factorization plays an important role in computational least squares and eigenvalue problems.

## Chapter 2 <br> Diagonally Dominant Tridiagonal Matrices; Three Examples

In this chapter we consider three problems originating from:

- cubic spline interpolation,
- a two point boundary value problem,
- an eigenvalue problem for a two point boundary value problem.

Each of these problems leads to a linear algebra problem with a matrix which is diagonally dominant and tridiagonal. Taking advantage of structure we can show existence, uniqueness and characterization of a solution, and derive efficient and stable algorithms based on LU factorization to compute a numerical solution.

For a particular tridiagonal test matrix we determine all its eigenvectors and eigenvalues. We will need these later when studying more complex problems.

We end the chapter with an introduction to block multiplication, a powerful tool in matrix analysis and numerical linear algebra. Block multiplication is applied to derive some basic facts about triangular matrices.

### 2.1 Cubic Spline Interpolation

We consider the following interpolation problem.
Given an interval $[a, b], n+1 \geq 2$ equidistant sites in $[a, b]$

$$
x_{i}=a+\frac{i-1}{n}(b-a), \quad i=1,2, \ldots, n+1
$$

and $y$ values $\boldsymbol{y}:=\left[y_{1}, \ldots, y_{n+1}\right]^{T} \in \mathbb{R}^{n+1}$. We seek a function $g:[a, b] \rightarrow \mathbb{R}$ such that

$$
g\left(x_{i}\right)=y_{i}, \text { for } i=1, \ldots, n+1 .
$$

For simplicity we only consider equidistant sites. More generally they could be any $a \leq x_{1}<x_{2}<\cdots<x_{n+1} \leq b$.

### 2.1.1 Polynomial Interpolation

Since there are $n+1$ interpolation conditions in (2.2) a natural choice for a function $g$ is a polynomial of degree $n$. As shown in most books on numerical methods such a $g$ is uniquely defined and there are good algorithms for computing it. Evidently, when $n=1, g$ is the straight line

$$
g(x)=y_{1}+\frac{y_{2}-y_{1}}{x_{2}-x_{1}}\left(x-x_{1}\right),
$$

known as the linear interpolation polynomial.
Polynomial interpolation is an important technique which often gives good results, but the interpolant $g$ can have undesirable oscillations when $n$ is large. As an example, consider the function given by

$$
f(x)=\arctan (10 x)+\pi / 2, \quad x \in[-1,1] .
$$

The function $f$ and the polynomial $g$ of degree at most 13 satisfying (2.2) with $[a, b]=[-1,1]$ and $y_{i}=f\left(x_{i}\right), i=1, \ldots, 14$ is shown in Fig. 2.1. The interpolant has large oscillations near the end of the range. This is an example of the Runge phenomenon. Using larger $n$ will only make the oscillations bigger. ${ }^{1}$

### 2.1.2 Piecewise Linear and Cubic Spline Interpolation

To avoid oscillations like the one in Fig. 2.1 piecewise linear interpolation can be used. An example is shown in Fig. 2.2. The interpolant $g$ approximates the original function quite well, and for some applications, like plotting, the linear interpolant using many points is what is used. Note that $g$ is a piecewise polynomial of the form

$$
g(x):= \begin{cases}p_{1}(x), & \text { if } x_{1} \leq x<x_{2}, \\ p_{2}(x), & \text { if } x_{2} \leq x<x_{3}, \\ \vdots & \\ p_{n-1}(x), & \text { if } x_{n-1} \leq x<x_{n}, \\ p_{n}(x), & \text { if } x_{n} \leq x \leq x_{n+1},\end{cases}
$$

[^2]![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-048.jpg?height=598&width=971&top_left_y=213&top_left_x=276)
Fig. 2.1 The polynomial of degree 13 interpolating $f(x)=\arctan (10 x)+\pi / 2$ on $[-1,1]$. See text

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-048.jpg?height=615&width=969&top_left_y=946&top_left_x=278)
Fig. 2.2 The piecewise linear polynomial interpolating $f(x)=\arctan (10 x)+\pi / 2$ at $n=14$ uniform points on [-1, 1]

where each $p_{i}$ is a polynomial of degree $\leq 1$. In particular, $p_{1}$ is given in (2.3) and the other polynomials $p_{i}$ are given by similar expressions.

The piecewise linear interpolant is continuous, but the first derivative will usually have jumps at the interior sites. We can obtain a smoother approximation by letting $g$ be a piecewise polynomial of higher degree. With degree 3 (cubic) we obtain continuous derivatives of order $\leq 2$ ( $C^{2}$ ). We consider here the following functions giving examples of $C^{2}$ cubic spline interpolants.

Definition 2.1 (The $D_{2}$-Spline Problem) Given $n \in \mathbb{N}$, an interval $[a, b]$, $\boldsymbol{y} \in$ $\mathbb{R}^{n+1}$, knots (sites) $x_{1}, \ldots, x_{n+1}$ given by (2.1) and numbers $\mu_{1}, \mu_{n+1}$. The problem is to find a function $g:[a, b] \rightarrow \mathbb{R}$ such that

- piecewise cubic polynomial: $g$ is of the form (2.4) with each $p_{i}$ a cubic polynomial, ,
- smoothness: $g \in C^{2}[a, b]$, i.e., derivatives of order $\leq 2$ are continuous on $\mathbb{R}$,
- interpolation: $g\left(x_{i}\right)=y_{i}, \quad i=1,2, \ldots, n+1$,
- $\boldsymbol{D}_{\mathbf{2}}$ boundary conditions: $g^{\prime \prime}(a)=\mu_{1}, \quad g^{\prime \prime}(b)=\mu_{n+1}$.

We call $g$ a $D_{2}$-spline. It is called an $N$-spline or natural spline if $\mu_{1}=\mu_{n+1}=0$.
Example 2.1 (A $D_{2}$-Spline) Suppose we choose $n=2$ and sample data from the function $f:[0,2] \rightarrow \mathbb{R}$ given by $f(x)=x^{4}$. Thus we consider the $D_{2}$-spline problem with $[a, b]=[0,2], \boldsymbol{y}:=[0,1,16]^{T}$ and $\mu_{1}=g^{\prime \prime}(0)=0, \mu_{3}=g^{\prime \prime}(2)=$ 48. The knots are $x_{1}=0, x_{2}=1$ and $x_{3}=2$. The function $g$ given by

$$
g(x):= \begin{cases}p_{1}(x)=-\frac{1}{2} x+\frac{3}{2} x^{3}, & \text { if } 0 \leq x<1, \\ p_{2}(x)=1+4(x-1)+\frac{9}{2}(x-1)^{2}+\frac{13}{2}(x-1)^{3}, & \text { if } 1 \leq x \leq 2,\end{cases}
$$

is a $D_{2}$-spline solving this problem. Indeed, $p_{1}$ and $p_{2}$ are cubic polynomials. For smoothness we find $p_{1}(1)=p_{2}(1)=1, p_{1}^{\prime}(1)=p_{2}^{\prime}(1)=4, p_{1}^{\prime \prime}(1)=p_{2}^{\prime \prime}(1)=$ 9 which implies that $g \in C^{2}[0,2]$. Finally we check that the interpolation and boundary conditions hold. Indeed, $g(0)=p_{1}(0)=0, g(1)=p_{2}(1)=1, g(2)=$ $p_{2}(2)=16, g^{\prime \prime}(0)=p_{1}^{\prime \prime}(0)=0$ and $g^{\prime \prime}(2)=p_{2}^{\prime \prime}(2)=48$. Note that $p_{1}^{\prime \prime \prime}(x)=9 \neq$ $39=p_{2}^{\prime \prime \prime}(x)$ showing that the third derivative of $g$ is piecewise constant with a jump discontinuity at the interior knot. A plot of $f$ and $g$ is shown in Fig. 2.3. It is hard to distinguish one from the other.

We note that

- The $C^{2}$ condition is equivalent to
$$
p_{i-1}^{(j)}\left(x_{i}\right)=p_{i}^{(j)}\left(x_{i}\right), \quad j=0,1,2, \quad i=2, \ldots, n .
$$
- The extra boundary conditions $D_{2}$ or $N$ are introduced to obtain a unique interpolant. Indeed counting requirements we have $3(n-1) C^{2}$ conditions, $n+1$ conditions (2.2), and two boundary conditions, adding to $4 n$. Since a cubic polynomial has four coefficients, this number is equal to the number of coefficients of the $n$ polynomials $p_{1}, \ldots, p_{n}$ and give hope for uniqueness of the interpolant.

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-050.jpg?height=769&width=958&top_left_y=213&top_left_x=284)
Fig. 2.3 A cubic spline with one knot interpolating $f(x)=x^{4}$ on $[0,2]$

### 2.1.3 Give Me a Moment

Existence and uniqueness of a solution of the $D_{2}$-spline problem hinges on the nonsingularity of a linear system of equations that we now derive. The unknowns are derivatives at the knots. Here we use second derivatives which are sometimes called moments. We start with the following lemma.

Lemma 2.1 (Representing Each $p_{i}$ Using $(0,2)$ Interpolation) Given $a<b$, $h=(b-a) / n$ with $n \geq 2, x_{i}=a+(i-1) h$, and numbers $y_{i}, \mu_{i}$ for $i=1, \ldots, n+1$. For $i=1, \ldots, n$ there are unique cubic polynomials $p_{i}$ such that

$$
p_{i}\left(x_{i}\right)=y_{i}, \quad p_{i}\left(x_{i+1}\right)=y_{i+1}, \quad p_{i}^{\prime \prime}\left(x_{i}\right)=\mu_{i}, \quad p_{i}^{\prime \prime}\left(x_{i+1}\right)=\mu_{i+1} .
$$

Moreover,

$$
p_{i}(x)=c_{i, 1}+c_{i, 2}\left(x-x_{i}\right)+c_{i, 3}\left(x-x_{i}\right)^{2}+c_{i, 4}\left(x-x_{i}\right)^{3} \quad i=1, \ldots, n,
$$

where

$$
c_{i 1}=y_{i}, c_{i 2}=\frac{y_{i+1}-y_{i}}{h}-\frac{h}{3} \mu_{i}-\frac{h}{6} \mu_{i+1}, c_{i, 3}=\frac{\mu_{i}}{2}, c_{i, 4}=\frac{\mu_{i+1}-\mu_{i}}{6 h} .
$$

Proof Consider $p_{i}$ in the form (2.7) for some $1 \leq i \leq n$. Evoking (2.6) we find $p_{i}\left(x_{i}\right)=c_{i, 1}=y_{i}$. Since $p_{i}^{\prime \prime}(x)=2 c_{i, 3}+6 c_{i, 4}\left(x-x_{i}\right)$ we obtain $c_{i, 3}$ from $p_{i}^{\prime \prime}\left(x_{i}\right)=$ $2 c_{i, 3}=\mu_{i}$ (a moment), and then $c_{i, 4}$ from $p_{i}^{\prime \prime}\left(x_{i+1}\right)=\mu_{i}+6 h c_{i, 4}=\mu_{i+1}$. Finally we find $c_{i, 2}$ by solving $p_{i}\left(x_{i+1}\right)=y_{i}+c_{i, 2} h+\frac{\mu_{i}}{2} h^{2}+\frac{\mu_{i+1}-\mu_{i}}{6 h} h^{3}=y_{i+1}$. For $j=0,1,2,3$ the shifted powers $\left(x-x_{i}\right)^{j}$ constitute a basis for cubic polynomials and the formulas (2.8) are unique by construction. It follows that $p_{i}$ is unique. $\square$

Theorem 2.1 (Constructing a $D_{2}$-Spline) Suppose for some moments $\mu_{1}, \ldots$, $\mu_{n+1}$ that each $p_{i}$ is given as in Lemma 2.1 for $i=1, \ldots, n$. If in addition

$$
\mu_{i-1}+4 \mu_{i}+\mu_{i+1}=\frac{6}{h^{2}}\left(y_{i+1}-2 y_{i}+y_{i-1}\right), \quad i=2, \ldots, n,
$$

then the function $g$ given by (2.4) solves a $D_{2}$-spline problem.
Proof Suppose for $1 \leq i \leq n$ that $p_{i}$ is given as in Lemma 2.1 for some $\mu_{1}, \ldots, \mu_{n+1}$. Consider the $C^{2}$ requirement. Since $p_{i-1}\left(x_{i}\right)=p_{i}\left(x_{i}\right)=y_{i}$ and $p_{i-1}^{\prime \prime}\left(x_{i}\right)=p_{i}^{\prime \prime}\left(x_{i}\right)=\mu_{i}$ for $i=2, \ldots, n$ it follows that $g \in C^{2}$ if and only if $p_{i-1}^{\prime}\left(x_{i}\right)=p_{i}^{\prime}\left(x_{i}\right)$ for $i=2, \ldots, n$. By (2.7)

$$
\begin{aligned}
p_{i-1}^{\prime}\left(x_{i}\right) & =c_{i-1,2}+2 h c_{i-1,3}+3 h^{2} c_{i-1,4} \\
& =\frac{y_{i}-y_{i-1}}{h}-\frac{h}{3} \mu_{i-1}-\frac{h}{6} \mu_{i}+2 h \frac{\mu_{i-1}}{2}+3 h^{2} \frac{\mu_{i}-\mu_{i-1}}{6 h} \\
& =\frac{y_{i}-y_{i-1}}{h}+\frac{h}{6} \mu_{i-1}+\frac{h}{3} \mu_{i} \\
p_{i}^{\prime}\left(x_{i}\right) & =c_{i 2}=\frac{y_{i+1}-y_{i}}{h}-\frac{h}{3} \mu_{i}-\frac{h}{6} \mu_{i+1} .
\end{aligned}
$$

A simple calculation shows that $p_{i-1}^{\prime}\left(x_{i}\right)=p_{i}^{\prime}\left(x_{i}\right)$ if and only if (2.9) holds.
Finally consider the function $g$ given by (2.4). If (2.9) holds then $g \in C^{2}[a, b]$. By construction $g\left(x_{i}\right)=y_{i}, i=1, \ldots, n+1, g^{\prime \prime}(a)=p_{1}^{\prime \prime}\left(x_{1}\right)=\mu_{1}$ and $g^{\prime \prime}(b)=$ $p_{n}^{\prime \prime}\left(x_{n+1}\right)=\mu_{n+1}$. It follows that $g$ solves the $D_{2}$-spline problem. $\square$

In order for the $D_{2}$-spline to exist we need to show that $\mu_{2}, \ldots, \mu_{n}$ always can be determined from (2.9). For $n \geq 3$ and with $\mu_{1}$ and $\mu_{n+1}$ given (2.9) can be written in the form

$$
\left[\begin{array}{ccccc}
4 & 1 & & & \\
1 & 4 & 1 & & \\
& \ddots & \ddots & \ddots & \\
& & 1 & 4 & 1 \\
& & & 1 & 4
\end{array}\right]\left[\begin{array}{c}
\mu_{2} \\
\mu_{3} \\
\vdots \\
\mu_{n-1} \\
\mu_{n}
\end{array}\right]=\frac{6}{h^{2}}\left[\begin{array}{c}
\delta^{2} y_{2}-\mu_{1} \\
\delta^{2} y_{3} \\
\vdots \\
\delta^{2} y_{n-1} \\
\delta^{2} y_{n}-\mu_{n+1}
\end{array}\right], \delta^{2} y_{i}:=y_{i+1}-2 y_{i}+y_{i-1} .
$$

This is a square linear system of equations. We recall (see Theorem 1.6) that a square system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ has a solution for all right hand sides $\boldsymbol{b}$ if and only if the coefficient matrix $\boldsymbol{A}$ is nonsingular, i.e., the homogeneous system $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$ only has the solution $\boldsymbol{x}=\mathbf{0}$. Moreover, the solution is unique. We need to show that the coefficient matrix in (2.11) is nonsingular.

We observe that the matrix in (2.11) is strictly diagonally dominant in accordance with the following definition.

Definition 2.2 (Strict Diagonal Dominance) The matrix $\boldsymbol{A}=\left[a_{i j}\right] \in \mathbb{C}^{n \times n}$ is strictly diagonally dominant if

$$
\left|a_{i i}\right|>\sum_{j \neq i}\left|a_{i j}\right|, i=1, \ldots, n .
$$

Theorem 2.2 (Strict Diagonal Dominance) A strictly diagonally dominant matrix is nonsingular. Moreover, if $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is strictly diagonally dominant then the solution $\boldsymbol{x}$ of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ is bounded as follows:

$$
\max _{1 \leq i \leq n}\left|x_{i}\right| \leq \max _{1 \leq i \leq n}\left(\frac{\left|b_{i}\right|}{\sigma_{i}}\right), \text { where } \sigma_{i}:=\left|a_{i i}\right|-\sum_{j \neq i}\left|a_{i j}\right| .
$$

Proof We first show that the bound (2.13) holds for any solution $\boldsymbol{x}$. Choose $k$ so that $\left|x_{k}\right|=\max _{i}\left|x_{i}\right|$. Then

$$
\left|b_{k}\right|=\left|a_{k k} x_{k}+\sum_{j \neq k} a_{k j} x_{j}\right| \geq\left|a_{k k}\right|\left|x_{k}\right|-\sum_{j \neq k}\left|a_{k j}\right|\left|x_{j}\right| \geq\left|x_{k}\right|\left(\left|a_{k k}\right|-\sum_{j \neq k}\left|a_{k j}\right|\right),
$$

and this implies $\max _{1 \leq i \leq n}\left|x_{i}\right|=\left|x_{k}\right| \leq \frac{\left|b_{k}\right|}{\sigma_{k}} \leq \max _{1 \leq i \leq n}\left(\frac{\left|b_{i}\right|}{\sigma_{i}}\right)$. For the nonsingularity, if $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$, then $\max _{1 \leq i \leq n}\left|x_{i}\right| \leq 0$ by (2.13), and so $\boldsymbol{x}=\mathbf{0}$. $\square$

For an alternative simple proof of the nonsingularity based on Gershgorin circle theorem see Exercise 14.3.

Theorem 2.2 implies that the system (2.11) has a unique solution giving rise to a function $g$ detailed in Lemma 2.1 and solving the $D_{2}$-spline problem. For uniqueness suppose $g_{1}$ and $g_{2}$ are two $D_{2}$-splines interpolating the same data. Then $g:=g_{1}-g_{2}$ is an $N$-spline satisfying (2.2) with $\boldsymbol{y}=\mathbf{0}$. The solution $\left[\mu_{2}, \ldots, \mu_{n}\right]^{T}$ of (2.11) and also $\mu_{1}=\mu_{n+1}$ are zero. It follows from (2.8) that all coefficients $c_{i, j}$ are zero. We conclude that $g=0$ and $g_{1}=g_{2}$.

Example 2.2 (Cubic $B$-Spline) For the $N$-spline with $[a, b]=[0,4]$ and $\boldsymbol{y}=$ $\left[0, \frac{1}{6}, \frac{2}{3}, \frac{1}{6}, 0\right]$ the linear system (2.9) takes the form

$$
\left[\begin{array}{lll}
4 & 1 & 0 \\
1 & 4 & 1 \\
0 & 1 & 4
\end{array}\right]\left[\begin{array}{l}
\mu_{2} \\
\mu_{3} \\
\mu_{4}
\end{array}\right]=\left[\begin{array}{c}
2 \\
-6 \\
2
\end{array}\right] .
$$

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-053.jpg?height=910&width=948&top_left_y=217&top_left_x=289)
Fig. 2.4 A cubic B-spline

The solution is $\mu_{2}=\mu_{4}=1, \mu_{3}=-2$. The knotset is $\{0,1,2,3,4\}$. Using (2.8) (cf. Exercise 2.6) we find

$$
g(x):= \begin{cases}p_{1}(x)=\frac{1}{6} x^{3}, & \text { if } 0 \leq x<1, \\ p_{2}(x)=\frac{1}{6}+\frac{1}{2}(x-1)+\frac{1}{2}(x-1)^{2}-\frac{1}{2}(x-1)^{3}, & \text { if } 1 \leq x<2, \\ p_{3}(x)=\frac{2}{3}-(x-2)^{2}+\frac{1}{2}(x-2)^{3}, & \text { if } 2 \leq x<3, \\ p_{4}(x)=\frac{1}{6}-\frac{1}{2}(x-3)+\frac{1}{2}(x-3)^{2}-\frac{1}{6}(x-3)^{3}, & \text { if } 3 \leq x \leq 4,\end{cases}
$$

A plot of this spline is shown in Fig. 2.4. On $(0,4)$ the function $g$ equals the nonzero part of a function known as a $C^{2}$ cubic B-spline.

### 2.1.4 LU Factorization of a Tridiagonal System

To find the $D^{2}$-spline $g$ we have to solve the triangular system (2.11). Consider solving a general tridiagonal linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ where $\boldsymbol{A}=\operatorname{tridiag}\left(a_{i}, d_{i}, c_{i}\right) \in$
$\mathbb{C}^{n \times n}$. Instead of using Gaussian elimination directly, we can construct two matrices $\boldsymbol{L}$ and $\boldsymbol{U}$ such that $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$. Since $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{L} \boldsymbol{U} \boldsymbol{x}=\boldsymbol{b}$ we can find $\boldsymbol{x}$ by solving two systems $\boldsymbol{L} \boldsymbol{z}=\boldsymbol{b}$ and $\boldsymbol{U} \boldsymbol{x}=\boldsymbol{z}$. Moreover $\boldsymbol{L}$ and $\boldsymbol{U}$ are both triangular and bidiagonal, and if in addition they are nonsingular the two systems can be solved easily without using elimination.

In our case we write the product $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$ in the form

$$
\left[\begin{array}{ccccc}
d_{1} & c_{1} & & & \\
a_{1} & d_{2} & c_{2} & & \\
& \ddots & \ddots & \ddots & \\
& & a_{n-2} & d_{n-1} & c_{n-1} \\
& & & a_{n-1} & d_{n}
\end{array}\right]=\left[\begin{array}{cccc}
1 & & & \\
l_{1} & 1 & & \\
& \ddots & \ddots & \\
& & l_{n-1} & 1
\end{array}\right]\left[\begin{array}{cccc}
u_{1} & c_{1} & & \\
& \ddots & \ddots & \\
& & u_{n-1} & c_{n-1} \\
& & & u_{n}
\end{array}\right]
$$

To find $\boldsymbol{L}$ and $\boldsymbol{U}$ we first consider the case $n=3$. Equation (2.15) takes the form

$$
\left[\begin{array}{lll}
d_{1} & c_{1} & 0 \\
a_{1} & d_{2} & c_{2} \\
0 & a_{2} & d_{3}
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
l_{1} & 1 & 0 \\
0 & l_{2} & 1
\end{array}\right]\left[\begin{array}{ccc}
u_{1} & c_{1} & 0 \\
0 & u_{2} & c_{2} \\
0 & 0 & u_{3}
\end{array}\right]=\left[\begin{array}{ccc}
u_{1} & c_{1} & 0 \\
l_{1} u_{1} & l_{1} c_{1}+u_{2} & c_{2} \\
0 & l_{2} u_{2} & l_{2} c_{2}+u_{3}
\end{array}\right],
$$

and the systems $\boldsymbol{L} \boldsymbol{z}=\boldsymbol{b}$ and $\boldsymbol{U} \boldsymbol{x}=\boldsymbol{z}$ can be written

$$
\left[\begin{array}{lll}
1 & 0 & 0 \\
l_{1} & 1 & 0 \\
0 & l_{2} & 1
\end{array}\right]\left[\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right]=\left[\begin{array}{l}
b_{1} \\
b_{2} \\
b_{3}
\end{array}\right], \quad\left[\begin{array}{ccc}
u_{1} & c_{1} & 0 \\
0 & u_{2} & c_{2} \\
0 & 0 & u_{3}
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right]=\left[\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right] .
$$

Comparing elements we find

$$
\begin{aligned}
& u_{1}=d_{1}, \quad l_{1}=a_{1} / u_{1}, \quad u_{2}=d_{2}-l_{1} c_{1}, \quad l_{2}=a_{2} / u_{2}, \quad u_{3}=d_{3}-l_{2} c_{2} \\
& z_{1}=b_{1}, \quad z_{2}=b_{2}-l_{1} z_{1}, \quad z_{3}=b_{3}-l_{2} z_{2} \\
& x_{3}=z_{3} / u_{3}, \quad x_{2}=\left(z_{2}-c_{2} x_{3}\right) / u_{2}, \quad x_{1}=\left(z_{1}-c_{1} x_{2}\right) / u_{1}
\end{aligned}
$$

In general, if

$$
u_{1}=d_{1}, \quad l_{k}=a_{k} / u_{k}, \quad u_{k+1}=d_{k+1}-l_{k} c_{k}, \quad k=1,2, \ldots, n-1,
$$

then $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$. If $u_{1}, u_{2}, \ldots, u_{n-1}$ are nonzero then (2.16) is well defined. If in addition $u_{n} \neq 0$ then we can solve $\boldsymbol{L} \boldsymbol{z}=\boldsymbol{b}$ and $\boldsymbol{U} \boldsymbol{x}=\boldsymbol{z}$ for $\boldsymbol{z}$ and $\boldsymbol{x}$. We formulate this as two algorithms. In trifactor, vectors $\boldsymbol{l} \in \mathbb{C}^{n-1}, \boldsymbol{u} \in \mathbb{C}^{n}$ are computed from $\boldsymbol{a}, \boldsymbol{c} \in \mathbb{C}^{n-1}, \boldsymbol{d} \in \mathbb{C}^{n}$. This implements the LU factorization of a tridiagonal matrix:

```
function [l,u]=trifactor(a,d,c)
% [l,u]=trifactor(a,d,c)
u=d; l=a;
for k =1:length(a)
    l(k)=a(k)/u(k);
    u (k+1) = d(k+1) -l (k) *c(k) ;
end
```

Listing 2.1 trifactor

In trisolve, the solution $\boldsymbol{x}$ of a tridiagonal system with $r$ right hand sides is computed from a previous call to trifactor. Here $\boldsymbol{l}, \in \mathbb{C}^{n-1}$ and $\boldsymbol{u} \in \mathbb{C}^{n}$ are output from trifactor and $\boldsymbol{b} \in \mathbb{C}^{n, r}$ for some $r \in \mathbb{N}$ :

```
function x = trisolve (l,u,c,b)
% x = trisolve (l,u,c,b)
x=b;
n= size(b,1);
for k =2:n
    x(k, :)=b(k, :) -l (k-1) *x(k-1, :) ;
end
x(n,:)=x(n,:)/u(n);
for k=(n-1) :-1 :1
    x(k, :) = (x(k, :) -c (k) *x(k+1, :) ) /u(k) ;
end
```

Listing 2.2 trisolve

Since division by zero can occur, the algorithms will not work in general, but for tridiagonal strictly diagonally dominant systems we have

Theorem 2.3 (LU of a Tridiagonal Strictly Dominant System) A strictly diagonally dominant tridiagonal matrix has a unique LU factorization of the form (2.15).

Proof We show that the $u_{k}$ 's in (2.16) are nonzero for $k=1, \ldots, n$. For this it is sufficient to show by induction that

$$
\left|u_{k}\right| \geq \sigma_{k}+\left|c_{k}\right|, \quad \text { where, } \sigma_{k}:=\left|d_{k}\right|-\left|a_{k-1}\right|-\left|c_{k}\right|>0, k=1, \ldots, n,
$$

and where $a_{0}:=c_{n}:=0$. By assumption $\left|u_{1}\right|=\left|d_{1}\right|=\sigma_{1}+\left|c_{1}\right|$. Suppose $\left|u_{k}\right| \geq$ $\sigma_{k}+\left|c_{k}\right|$ for some $1 \leq k \leq n-1$. Then $\left|c_{k}\right| /\left|u_{k}\right|<1$ and by (2.16) and strict diagonal dominance

$$
\begin{aligned}
\left|u_{k+1}\right| & =\left|d_{k+1}-l_{k} c_{k}\right|=\left|d_{k+1}-\frac{a_{k} c_{k}}{u_{k}}\right| \geq\left|d_{k+1}\right|-\frac{\left|a_{k}\right|\left|c_{k}\right|}{\left|u_{k}\right|} \\
& \geq\left|d_{k+1}\right|-\left|a_{k}\right|=\sigma_{k+1}+\left|c_{k+1}\right|
\end{aligned}
$$ $\square$

Corollary 2.1 (Stability of the LU Factorization) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is tridiagonal and strictly diagonally dominant with computed elements in the LU factorization given by (2.16). Then (2.17) holds, $u_{1}=d_{1}$ and

$$
\left|l_{k}\right|=\frac{\left|a_{k}\right|}{\left|u_{k}\right|} \leq \frac{\left|a_{k}\right|}{\left|d_{k}\right|-\left|a_{k-1}\right|},\left|u_{k+1}\right| \leq\left|d_{k+1}\right|+\frac{\left|a_{k}\right|\left|c_{k}\right|}{\left|d_{k}\right|-\left|a_{k-1}\right|}, k=1, \ldots, n-1 .
$$

Proof Using (2.16) and (2.17) for $1 \leq k \leq n-1$ we find

$$
\left|l_{k}\right|=\frac{\left|a_{k}\right|}{\left|u_{k}\right|} \leq \frac{\left|a_{k}\right|}{\left|d_{k}\right|-\left|a_{k-1}\right|},\left|u_{k+1}\right| \leq\left|d_{k+1}\right|+\left|l_{k}\right|\left|c_{k}\right| \leq\left|d_{k+1}\right|+\frac{\left|a_{k}\right|\left|c_{k}\right|}{\left|d_{k}\right|-\left|a_{k-1}\right|} .
$$ $\square$

- For a strictly diagonally dominant tridiagonal matrix it follows from Corollary 2.1 that the LU factorization algorithm trifactor is stable meaning that we cannot have severe growth in the computed elements $u_{k}$ and $l_{k}$.
- The number of arithmetic operations to compute the LU factorization of a tridiagonal matrix of order $n$ using (2.16) is $3 n-3$, while the number of arithmetic operations for Algorithm trisolve is $r(5 n-4)$, where $r$ is the number of right-hand sides. This means that the complexity to solve a tridiagonal system is $O(n)$, or more precisely $8 n-7$ when $r=1$, and this number only grows linearly ${ }^{2}$ with $n$.

### 2.2 A Two Point Boundary Value Problem

Consider the simple two point boundary value problem

$$
-u^{\prime \prime}(x)=f(x), \quad x \in[0,1], \quad u(0)=0, u(1)=0,
$$

where $f$ is a given continuous function on $[0,1]$ and $u$ is an unknown function. This problem is also known as the one-dimensional (1D) Poisson problem. In principle it is easy to solve (2.20) exactly. We just integrate $f$ twice and determine the two integration constants so that the homogeneous boundary conditions $u(0)=u(1)=$ 0 are satisfied. For example, if $f(x)=1$ then $u(x)=x(x-1) / 2$ is the solution.

Suppose $f$ cannot be integrated exactly. Problem (2.20) can then be solved approximately using the finite difference method. We need a difference approximation to the second derivative. If $g$ is a function differentiable at $x$ then

$$
g^{\prime}(x)=\lim _{h \rightarrow 0} \frac{g\left(x+\frac{h}{2}\right)-g\left(x-\frac{h}{2}\right)}{h}
$$

[^3]and applying this to a function $u$ that is twice differentiable at $x$
$$
\begin{aligned}
u^{\prime \prime}(x) & =\lim _{h \rightarrow 0} \frac{u^{\prime}\left(x+\frac{h}{2}\right)-u^{\prime}\left(x-\frac{h}{2}\right)}{h}=\lim _{h \rightarrow 0} \frac{\frac{u(x+h)-u(x)}{h}-\frac{u(x)-u(x-h)}{h}}{h} \\
& =\lim _{h \rightarrow 0} \frac{u(x+h)-2 u(x)+u(x-h)}{h^{2}} .
\end{aligned}
$$
To define the points where this difference approximation is used we choose a positive integer $m$, let $h:=1 /(m+1)$ be the discretization parameter, and replace the interval [0, 1] by grid points $x_{j}:=j h$ for $j=0,1, \ldots, m+1$. We then obtain approximations $v_{j}$ to the exact solution $u\left(x_{j}\right)$ for $j=1, \ldots, m$ by replacing the differential equation by the difference equation
$$
\frac{-v_{j-1}+2 v_{j}-v_{j+1}}{h^{2}}=f(j h), \quad j=1, \ldots, m, \quad v_{0}=v_{m+1}=0 .
$$
Moving the $h^{2}$ factor to the right hand side this can be written as an $m \times m$ linear system
$$
\boldsymbol{T} \boldsymbol{v}=\left[\begin{array}{rrrrr}
2 & -1 & 0 & & \\
-1 & 2 & -1 & & \\
0 & \ddots & \ddots & \ddots & \\
& & & & 0 \\
& & & -1 & 2-1 \\
& & & 0-1 & 2
\end{array}\right]\left[\begin{array}{c}
v_{1} \\
v_{2} \\
\vdots \\
v_{m-1} \\
v_{m}
\end{array}\right]=h^{2}\left[\begin{array}{c}
f(h) \\
f(2 h) \\
\vdots \\
f((m-1) h) \\
f(m h)
\end{array}\right]=: \boldsymbol{b} .
$$
The matrix $\boldsymbol{T}$ is called the second derivative matrix and will occur frequently in this book. It is our second example of a tridiagonal matrix, $\boldsymbol{T}=\operatorname{tridiag}\left(a_{i}, d_{i}, c_{i}\right) \in$ $\mathbb{R}^{m \times m}$, where in this case $a_{i}=c_{i}=-1$ and $d_{i}=2$ for all $i$.

### 2.2.1 Diagonal Dominance

We want to show that (2.21) has a unique solution. Note that $\boldsymbol{T}$ is not strictly diagonally dominant. However, $\boldsymbol{T}$ is weakly diagonally dominant in accordance with the following definition.

Definition 2.3 (Diagonal Dominance) The matrix $\boldsymbol{A}=\left[a_{i j}\right] \in \mathbb{C}^{n \times n}$ is weakly diagonally dominant if

$$
\left|a_{i i}\right| \geq \sum_{j \neq i}\left|a_{i j}\right|, i=1, \ldots, n .
$$

We showed in Theorem 2.2 that a strictly diagonally dominant matrix is nonsingular. This is in general not true in the weakly diagonally dominant case. Consider the 3 matrices

$$
\boldsymbol{A}_{1}=\left[\begin{array}{lll}
1 & 1 & 0 \\
1 & 2 & 1 \\
0 & 1 & 1
\end{array}\right], \quad \boldsymbol{A}_{2}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 1
\end{array}\right], \quad \boldsymbol{A}_{3}=\left[\begin{array}{rrr}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 2
\end{array}\right] .
$$

They are all weakly diagonally dominant, but $\boldsymbol{A}_{1}$ and $\boldsymbol{A}_{2}$ are singular, while $\boldsymbol{A}_{3}$ is nonsingular. Indeed, for $\boldsymbol{A}_{1}$ column two is the sum of columns one and three, $\boldsymbol{A}_{2}$ has a zero row, and $\operatorname{det}\left(\boldsymbol{A}_{3}\right)=4 \neq 0$. It follows that for the nonsingularity and existence of an LU factorization of a weakly diagonally dominant matrix we need some additional conditions. Here are some sufficient conditions.

Theorem 2.4 (Weak Diagonal Dominance) Suppose $\boldsymbol{A}=\operatorname{tridiag}\left(a_{i}, d_{i}, c_{i}\right) \in$ $\mathbb{C}^{n \times n}$ is tridiagonal and weakly diagonally dominant. If in addition $\left|d_{1}\right|>\left|c_{1}\right|$ and $a_{i} \neq 0$ for $i=1, \ldots, n-2$, then $\boldsymbol{A}$ has a unique $L U$ factorization (2.15). If in addition $d_{n} \neq 0$, then $\boldsymbol{A}$ is nonsingular.

Proof The proof is similar to the proof of Theorem 2.2. The matrix $\boldsymbol{A}$ has an LU factorization if the $u_{k}$ 's in (2.16) are nonzero for $k=1, \ldots, n-1$. For this it is sufficient to show by induction that $\left|u_{k}\right|>\left|c_{k}\right|$ for $k=1, \ldots, n-1$. By assumption $\left|u_{1}\right|=\left|d_{1}\right|>\left|c_{1}\right|$. Suppose $\left|u_{k}\right|>\left|c_{k}\right|$ for some $1 \leq k \leq n-2$. Then $\left|c_{k}\right| /\left|u_{k}\right|<1$ and by (2.16) and since $a_{k} \neq 0$

$$
\left|u_{k+1}\right|=\left|d_{k+1}-l_{k} c_{k}\right|=\left|d_{k+1}-\frac{a_{k} c_{k}}{u_{k}}\right| \geq\left|d_{k+1}\right|-\frac{\left|a_{k}\right|\left|c_{k}\right|}{\left|u_{k}\right|}>\left|d_{k+1}\right|-\left|a_{k}\right| .
$$

This also holds for $k=n-1$ if $a_{n-1} \neq 0$. By (2.23) and weak diagonal dominance $\left|u_{k+1}\right|>\left|d_{k+1}\right|-\left|a_{k}\right| \geq\left|c_{k+1}\right|$ and it follows by induction that an LU factorization exists. It is unique since any LU factorization must satisfy (2.16). For the nonsingularity we need to show that $u_{n} \neq 0$. For then by Lemma 2.5, both $\boldsymbol{L}$ and $\boldsymbol{U}$ are nonsingular, and this is equivalent to $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$ being nonsingular. If $a_{n-1} \neq 0$ then by (2.16) $\left|u_{n}\right|>\left|d_{n}\right|-\left|a_{n-1}\right| \geq 0$ by weak diagonal dominance, while if $a_{n-1}=0$ then again by (2.23) $\left|u_{n}\right| \geq\left|d_{n}\right|>0$. $\square$

Consider now the special system $\boldsymbol{T} \boldsymbol{v}=\boldsymbol{b}$ given by (2.21). The matrix $\boldsymbol{T}$ is weakly diagonally dominant and satisfies the additional conditions in Theorem 2.4. Thus it is nonsingular and we can solve the system in $O(n)$ arithmetic operations using the algorithms trifactor and trisolve.

We could use the explicit inverse of $\boldsymbol{T}$, given in Exercise 2.15, to compute the solution of $\boldsymbol{T} \boldsymbol{v}=\boldsymbol{b}$ as $\boldsymbol{v}=\boldsymbol{T}^{-1} \boldsymbol{b}$. However, this is not a good idea. In fact, all elements in $\boldsymbol{T}^{-1}$ are nonzero and the calculation of $\boldsymbol{T}^{-1} \boldsymbol{b}$ requires $O\left(n^{2}\right)$ operations.

### 2.3 An Eigenvalue Problem

Recall that if $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is a square matrix and $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ for some nonzero $\boldsymbol{x} \in$ $\mathbb{C}^{n}$, then $\lambda \in \mathbb{C}$ is called an eigenvalue and $\boldsymbol{x}$ an eigenvector. We call ( $\lambda, \boldsymbol{x}$ ) an eigenpair of $\boldsymbol{A}$.

### 2.3.1 The Buckling of a Beam

Consider a horizontal beam of length $L$ located between 0 and $L$ on the $x$-axis of the plane. We assume that the beam is fixed at $x=0$ and $x=L$ and that a force $F$ is applied at $(L, 0)$ in the direction towards the origin. This situation can be modeled by the boundary value problem

$$
R y^{\prime \prime}(x)=-F y(x), \quad y(0)=y(L)=0,
$$

where $y(x)$ is the vertical displacement of the beam at $x$, and $R$ is a constant defined by the rigidity of the beam. We can transform the problem to the unit interval [0, 1] by considering the function $u:[0,1] \rightarrow \mathbb{R}$ given by $u(t):=y(t L)$. Since $u^{\prime \prime}(t)=$ $L^{2} y^{\prime \prime}(t L)$, the problem (2.24) then becomes

$$
u^{\prime \prime}(t)=-K u(t), \quad u(0)=u(1)=0, \quad K:=\frac{F L^{2}}{R} .
$$

Clearly $u=0$ is a solution, but we can have nonzero solutions corresponding to certain values of the K known as eigenvalues. The corresponding function $u$ is called an eigenfunction. If $F=0$ then $K=0$ and $u=0$ is the only solution, but if the force is increased it will reach a critical value where the beam will buckle and maybe break. This critical value corresponds to the smallest eigenvalue of (2.25). With $u(t)=\sin (\pi t)$ we find $u^{\prime \prime}(t)=-\pi^{2} u(t)$ and this $u$ is a solution if $K=\pi^{2}$. It can be shown that this is the smallest eigenvalue of (2.25) and solving for $F$ we find $F=\frac{\pi^{2} R}{L^{2}}$.

We can approximate this eigenvalue numerically. Choosing $m \in \mathbb{N}, h:=1 /(m+$ 1) and using for the second derivative the approximation

$$
u^{\prime \prime}(j h) \approx \frac{u((j+1) h)-2 u(j h)+u((j-1) h)}{h^{2}}, \quad j=1, \ldots, m,
$$

(this is the same finite difference approximation as in Sect. 2.2) we obtain

$$
\frac{-v_{j-1}+2 v_{j}-v_{j+1}}{h^{2}}=K v_{j}, \quad j=1, \ldots, m, h=\frac{1}{m+1}, \quad v_{0}=v_{m+1}=0,
$$

where $v_{j} \approx u(j h)$ for $j=0, \ldots, m+1$. If we define $\lambda:=h^{2} K$ then we obtain the equation

$$
\boldsymbol{T} \boldsymbol{v}=\lambda \boldsymbol{v}, \text { with } \boldsymbol{v}=\left[v_{1}, \ldots, v_{m}\right]^{T},
$$

and

$$
\boldsymbol{T}=\boldsymbol{T}_{m}:=\operatorname{tridiag}_{m}(-1,2,-1)-=\left[\begin{array}{rrrrr}
2 & -1 & 0 & & \\
-1 & 2 & -1 & & \\
0 & \ddots & \ddots & \ddots & \\
& & & 0 \\
& & & -1 & 2-1 \\
& & & 0-1 & 2
\end{array}\right] \in \mathbb{R}^{m \times m} .
$$

The problem now is to determine the eigenvalues of $\boldsymbol{T}$. Normally we would need a numerical method to determine the eigenvalues of a matrix, but for this simple problem the eigenvalues can be determined exactly. We show in the next subsection that the smallest eigenvalue of (2.26) is given by $\lambda=4 \sin ^{2}(\pi h / 2)$. Since $\lambda=$ $h^{2} K=\frac{h^{2} F L^{2}}{R}$ we can solve for $F$ to obtain

$$
F=\frac{4 \sin ^{2}(\pi h / 2) R}{h^{2} L^{2}} .
$$

For small $h$ this is a good approximation to the value $\frac{\pi^{2} R}{L^{2}}$ we computed above.

### 2.4 The Eigenpairs of the 1D Test Matrix

The second derivative matrix $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1)$ is a special case of the tridiagonal matrix

$$
\boldsymbol{T}_{1}:=\operatorname{tridiag}(a, d, a)
$$

where $a, d \in \mathbb{R}$. We call this the $\mathbf{1 D}$ test matrix. It is symmetric and strictly diagonally dominant if $|d|>2|a|$.

We show that the eigenvectors are the columns of the sine matrix defined by

$$
\boldsymbol{S}=\left[\sin \frac{j k \pi}{m+1}\right]_{j, k=1}^{m} \in \mathbb{R}^{m \times m} .
$$

For $m=3$,

$$
\boldsymbol{S}=\left[\boldsymbol{s}_{1}, \boldsymbol{s}_{2}, \boldsymbol{s}_{3}\right]=\left[\begin{array}{c}
\sin \frac{\pi}{4} \sin \frac{2 \pi}{4} \sin \frac{3 \pi}{4} \\
\sin \frac{2 \pi}{4} \sin \frac{4 \pi}{4} \sin \frac{6 \pi}{4} \\
\sin \frac{3 \pi}{4} \sin \frac{6 \pi}{4} \sin \frac{9 \pi}{4}
\end{array}\right]=\left[\begin{array}{ccc}
t & 1 & t \\
1 & 0 & -1 \\
t & -1 & t
\end{array}\right], \quad t:=\frac{1}{\sqrt{2}} .
$$

Lemma 2.2 (Eigenpairs of 1D Test Matrix) Suppose $\boldsymbol{T}_{1}=\left(t_{k j}\right)_{k, j}=$ $\operatorname{tridiag}(a, d, a) \in \mathbb{R}^{m \times m}$ with $m \geq 2, a, d \in \mathbb{R}$, and let $h=1 /(m+1)$.

1. We have $\boldsymbol{T}_{1} \boldsymbol{s}_{j}=\lambda_{j} \boldsymbol{s}_{j}$ for $j=1, \ldots, m$, where
$$
\begin{aligned}
& \boldsymbol{s}_{j}=[\sin (j \pi h), \sin (2 j \pi h), \ldots, \sin (m j \pi h)]^{T}, \\
& \lambda_{j}=d+2 a \cos (j \pi h) .
\end{aligned}
$$
2. The eigenvalues are distinct and the eigenvectors are orthogonal
$$
\boldsymbol{s}_{j}^{T} \boldsymbol{s}_{k}=\frac{m+1}{2} \delta_{j, k}=\frac{1}{2 h} \delta_{j, k}, \quad j, k=1, \ldots, m .
$$

Proof We find for $1<k<m$

$$
\begin{aligned}
\left(\boldsymbol{T}_{1} \boldsymbol{s}_{j}\right)_{k} & =\sum_{l=1}^{m} t_{k, l} \sin (l j \pi h) \\
& =a[\sin ((k-1) j \pi h)+\sin ((k+1) j \pi h)]+d \sin (k j \pi h) \\
& =2 a \cos (j \pi h) \sin (k j \pi h)+d \sin (k j \pi h)=\lambda_{j} s_{k, j} .
\end{aligned}
$$

This also holds for $k=1, m$, and part 1 follows. Since $j \pi h=j \pi /(m+1) \in(0, \pi)$ for $j=1, \ldots, m$ and the cosine function is strictly monotone decreasing on $(0, \pi)$ the eigenvalues are distinct, and since $\boldsymbol{T}_{1}$ is symmetric it follows from Lemma 2.3 below that the eigenvectors $\boldsymbol{s}_{j}$ are orthogonal. To finish the proof of (2.32) we compute

$$
\begin{aligned}
\boldsymbol{s}_{j}^{T} \boldsymbol{s}_{j} & =\sum_{k=1}^{m} \sin ^{2}(k j \pi h)=\sum_{k=0}^{m} \sin ^{2}(k j \pi h)=\frac{1}{2} \sum_{k=0}^{m}(1-\cos (2 k j \pi h)) \\
& =\frac{m+1}{2}-\frac{1}{2} \sum_{k=0}^{m} \cos (2 k j \pi h)=\frac{m+1}{2},
\end{aligned}
$$

since the last cosine sum is zero. We show this by summing a geometric series of complex exponentials. With $i=\sqrt{-1}$ we find

$$
\sum_{k=0}^{m} \cos (2 k j \pi h)+i \sum_{k=0}^{m} \sin (2 k j \pi h)=\sum_{k=0}^{m} e^{2 i k j \pi h}=\frac{e^{2 i(m+1) j \pi h}-1}{e^{2 i j \pi h}-1}=0,
$$

and (2.32) follows. $\square$

Recall that the conjugate transpose of a matrix is defined by $\boldsymbol{A}^{*}:=\overline{\boldsymbol{A}}^{T}$, where $\overline{\boldsymbol{A}}$ is obtained from $\boldsymbol{A}$ by taking the complex conjugate of all elements. A matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is Hermitian if $\boldsymbol{A}^{*}=\boldsymbol{A}$. A real symmetric matrix is Hermitian.

Lemma 2.3 (Eigenpairs of a Hermitian Matrix) The eigenvalues of a Hermitian matrix are real. Moreover, eigenvectors corresponding to distinct eigenvalues are orthogonal.

Proof Suppose $\boldsymbol{A}^{*}=\boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ with $\boldsymbol{x} \neq 0$. We multiply both sides of $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ from the left by $\boldsymbol{x}^{*}$ and divide by $\boldsymbol{x}^{*} \boldsymbol{x}$ to obtain $\lambda=\frac{\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}}{\boldsymbol{x}^{*} \boldsymbol{x}}$. Taking complex conjugates we find $\bar{\lambda}=\lambda^{*}=\frac{\left(\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}\right)^{*}}{\left(\boldsymbol{x}^{*} \boldsymbol{x}\right)^{*}}=\frac{\boldsymbol{x}^{*} \boldsymbol{A}^{*} \boldsymbol{x}}{\boldsymbol{x}^{*} \boldsymbol{x}}=\frac{\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}}{\boldsymbol{x}^{*} \boldsymbol{x}}=\lambda$, and $\lambda$ is real. Suppose that $(\lambda, \boldsymbol{x})$ and $(\mu, \boldsymbol{y})$ are two eigenpairs for $\boldsymbol{A}$ with $\mu \neq \lambda$. Multiplying $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ by $\boldsymbol{y}^{*}$ gives

$$
\lambda \boldsymbol{y}^{*} \boldsymbol{x}=\boldsymbol{y}^{*} \boldsymbol{A} \boldsymbol{x}=\left(\boldsymbol{x}^{*} \boldsymbol{A}^{*} \boldsymbol{y}\right)^{*}=\left(\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{y}\right)^{*}=\left(\mu \boldsymbol{x}^{*} \boldsymbol{y}\right)^{*}=\mu \boldsymbol{y}^{*} \boldsymbol{x},
$$

using that $\mu$ is real. Since $\lambda \neq \mu$ it follows that $\boldsymbol{y}^{*} \boldsymbol{x}=0$, which means that $\boldsymbol{x}$ and $\boldsymbol{y}$ are orthogonal. $\square$

### 2.5 Block Multiplication and Triangular Matrices

Block multiplication is a powerful and essential tool for dealing with matrices. It will be used extensively in this book. We will also need some basic facts about triangular matrices.

### 2.5.1 Block Multiplication

A rectangular matrix $\boldsymbol{A}$ can be partitioned into submatrices by drawing horizontal lines between selected rows and vertical lines between selected columns. For example, the matrix

$$
\boldsymbol{A}=\left[\begin{array}{lll}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{array}\right]
$$

can be partitioned as
(i) $\left[\begin{array}{ll}\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\ \boldsymbol{A}_{21} & \boldsymbol{A}_{22}\end{array}\right]=\left[\begin{array}{l|ll}1 & 2 & 3 \\ \hline 4 & 5 & 6 \\ 7 & 8 & 9\end{array}\right]$,
(ii) $\left[\boldsymbol{a}_{: 1}, \boldsymbol{a}_{: 2}, \boldsymbol{a}_{: 3}\right]=\left[\begin{array}{c|c|c}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{array}\right]$,
(iii) $\left[\begin{array}{c}\boldsymbol{a}_{1}^{T} \\ \boldsymbol{a}_{2:}^{T} \\ \boldsymbol{a}_{3:}^{T}\end{array}\right]=\left[\begin{array}{l}\frac{123}{45} 6 \\ \hline \frac{789}{788}\end{array}\right]$,
(iv) $\left[\boldsymbol{A}_{11}, \boldsymbol{A}_{12}\right]=\left[\begin{array}{c|cc}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{array}\right]$.

In (i) the matrix $\boldsymbol{A}$ is divided into four submatrices

$$
\boldsymbol{A}_{11}=[1], \quad \boldsymbol{A}_{12}=[2,3], \quad \boldsymbol{A}_{21}=\left[\begin{array}{l}
4 \\
7
\end{array}\right], \quad \text { and } \boldsymbol{A}_{22}=\left[\begin{array}{ll}
5 & 6 \\
8 & 9
\end{array}\right],
$$

while in $(i i)$ and $(i i i) \boldsymbol{A}$ has been partitioned into columns and rows, respectively. The submatrices in a partition are often referred to as blocks and a partitioned matrix is sometimes called a block matrix.

In the following we assume that $\boldsymbol{A} \in \mathbb{C}^{m \times p}$ and $\boldsymbol{B} \in \mathbb{C}^{p \times n}$. Here are some rules and observations for block multiplication.

1. If $\boldsymbol{B}=\left[\boldsymbol{b}_{: 1}, \ldots, \boldsymbol{b}_{: n}\right]$ is partitioned into columns then the partition of the product $\boldsymbol{A} \boldsymbol{B}$ into columns is
$$
\boldsymbol{A} \boldsymbol{B}=\left[\boldsymbol{A} \boldsymbol{b}_{: 1}, \boldsymbol{A} \boldsymbol{b}_{: 2}, \ldots, \boldsymbol{A} \boldsymbol{b}_{: n}\right] .
$$
In particular, if $\boldsymbol{I}$ is the identity matrix of order $p$ then
$$
\boldsymbol{A}=\boldsymbol{A} \boldsymbol{I}=\boldsymbol{A}\left[\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \ldots, \boldsymbol{e}_{p}\right]=\left[\boldsymbol{A} \boldsymbol{e}_{1}, \boldsymbol{A} \boldsymbol{e}_{2}, \ldots, \boldsymbol{A} \boldsymbol{e}_{p}\right]
$$
and we see that column $j$ of $\boldsymbol{A}$ can be written $\boldsymbol{A} \boldsymbol{e}_{j}$ for $j=1, \ldots, p$.
2. Similarly, if $\boldsymbol{A}$ is partitioned into rows then
$$
\boldsymbol{A} \boldsymbol{B}=\left[\begin{array}{c}
a_{1:}^{T} \\
a_{2:}^{T} \\
\vdots \\
a_{m:}^{T}
\end{array}\right] \boldsymbol{B}=\left[\begin{array}{c}
a_{1:}^{T} \boldsymbol{B} \\
a_{2:}^{T} \boldsymbol{B} \\
\vdots \\
a_{m:}^{T} \boldsymbol{B}
\end{array}\right],
$$
and taking $\boldsymbol{A}=\boldsymbol{I}$ it follows that row $i$ of $\boldsymbol{B}$ can be written $\boldsymbol{e}_{i}^{T} \boldsymbol{B}$ for $i=1, \ldots, m$.
3. It is often useful to write the matrix-vector product $\boldsymbol{A} \boldsymbol{x}$ as a linear combination of the columns of $\boldsymbol{A}$
$$
\boldsymbol{A} \boldsymbol{x}=x_{1} \boldsymbol{a}_{: 1}+x_{2} \boldsymbol{a}_{: 2}+\cdots+x_{p} \boldsymbol{a}_{: p} .
$$

4. If $\boldsymbol{B}=\left[\boldsymbol{B}_{1}, \boldsymbol{B}_{2}\right]$, where $\boldsymbol{B}_{1} \in \mathbb{C}^{p \times r}$ and $\boldsymbol{B}_{2} \in \mathbb{C}^{p \times(n-r)}$ then
$$
\boldsymbol{A}\left[\boldsymbol{B}_{1}, \boldsymbol{B}_{2}\right]=\left[\boldsymbol{A} \boldsymbol{B}_{1}, \boldsymbol{A} \boldsymbol{B}_{2}\right] .
$$
This follows from Rule 1. by an appropriate grouping of columns.
5. If $\boldsymbol{A}=\left[\begin{array}{l}\boldsymbol{A}_{1} \\ \boldsymbol{A}_{2}\end{array}\right]$, where $\boldsymbol{A}_{1} \in \mathbb{C}^{k \times p}$ and $\boldsymbol{A}_{2} \in \mathbb{C}^{(m-k) \times p}$ then
$$
\left[\begin{array}{l}
A_{1} \\
A_{2}
\end{array}\right] B=\left[\begin{array}{l}
A_{1} B \\
A_{2} B
\end{array}\right] .
$$
This follows from Rule 2. by a grouping of rows.
6. If $\boldsymbol{A}=\left[\boldsymbol{A}_{1}, \boldsymbol{A}_{2}\right]$ and $\boldsymbol{B}=\left[\begin{array}{l}\boldsymbol{B}_{1} \\ \boldsymbol{B}_{2}\end{array}\right]$, where $\boldsymbol{A}_{1} \in \mathbb{C}^{m \times s}, \boldsymbol{A}_{2} \in \mathbb{C}^{m \times(p-s)}, \boldsymbol{B}_{1} \in$ $\mathbb{C}^{s \times n}$ and $\boldsymbol{B}_{2} \in \mathbb{C}^{(p-s) \times n}$ then
$$
\left[\boldsymbol{A}_{1}, \boldsymbol{A}_{2}\right]\left[\begin{array}{l}
\boldsymbol{B}_{1} \\
\boldsymbol{B}_{2}
\end{array}\right]=\left[\boldsymbol{A}_{1} \boldsymbol{B}_{1}+\boldsymbol{A}_{2} \boldsymbol{B}_{2}\right] .
$$
Indeed,
$$
\begin{aligned}
(\boldsymbol{A} \boldsymbol{B})_{i j} & =\sum_{k=1}^{p} a_{i k} b_{k j}=\sum_{k=1}^{s} a_{i k} b_{k j}+\sum_{k=s+1}^{p} a_{i k} b_{k j} \\
& =\left(\boldsymbol{A}_{1} \boldsymbol{B}_{1}\right)_{i j}+\left(\boldsymbol{A}_{2} \boldsymbol{B}_{2}\right)_{i j}=\left(\boldsymbol{A}_{1} \boldsymbol{B}_{1}+\boldsymbol{A}_{2} \boldsymbol{B}_{2}\right)_{i j} .
\end{aligned}
$$
7. If $\boldsymbol{A}=\left[\begin{array}{ll}\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\ \boldsymbol{A}_{21} & \boldsymbol{A}_{22}\end{array}\right]$ and $\boldsymbol{B}=\left[\begin{array}{ll}\boldsymbol{B}_{11} & \boldsymbol{B}_{12} \\ \boldsymbol{B}_{21} & \boldsymbol{B}_{22}\end{array}\right]$ then
$$
\left[\begin{array}{ll}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{array}\right]\left[\begin{array}{ll}
B_{11} & B_{12} \\
B_{21} & B_{22}
\end{array}\right]=\left[\begin{array}{ll}
A_{11} B_{11}+A_{12} B_{21} & A_{11} B_{12}+A_{12} B_{22} \\
A_{21} B_{11}+A_{22} B_{21} & A_{21} B_{12}+A_{22} B_{22}
\end{array}\right],
$$
provided the vertical partition in $\boldsymbol{A}$ matches the horizontal one in $\boldsymbol{B}$, i.e. the number of columns in $\boldsymbol{A}_{11}$ and $\boldsymbol{A}_{21}$ equals the number of rows in $\boldsymbol{B}_{11}$ and $\boldsymbol{B}_{12}$ and the number of columns in $\boldsymbol{A}$ equals the number of rows in $\boldsymbol{B}$. To show this we use Rule 4. to obtain
$$
\boldsymbol{A} \boldsymbol{B}=\left[\left[\begin{array}{ll}
\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\
\boldsymbol{A}_{21} & \boldsymbol{A}_{22}
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{B}_{11} \\
\boldsymbol{B}_{21}
\end{array}\right],\left[\begin{array}{ll}
\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\
\boldsymbol{A}_{21} & \boldsymbol{A}_{22}
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{B}_{12} \\
\boldsymbol{B}_{22}
\end{array}\right]\right] .
$$
We complete the proof using Rules 5. and 6.

8. Consider finally the general case. If all the matrix products $\boldsymbol{A}_{i k} \boldsymbol{B}_{k j}$ in
$$
\boldsymbol{C}_{i j}=\sum_{k=1}^{s} \boldsymbol{A}_{i k} \boldsymbol{B}_{k j}, \quad i=1, \ldots, p, j=1, \ldots, q
$$
are well defined then
$$
\left[\begin{array}{ccc}
\boldsymbol{A}_{11} & \cdots & \boldsymbol{A}_{1 s} \\
\vdots & & \vdots \\
\boldsymbol{A}_{p 1} & \cdots & \boldsymbol{A}_{p s}
\end{array}\right]\left[\begin{array}{ccc}
\boldsymbol{B}_{11} & \cdots & \boldsymbol{B}_{1 q} \\
\vdots & & \vdots \\
\boldsymbol{B}_{s 1} & \cdots & \boldsymbol{B}_{s q}
\end{array}\right]=\left[\begin{array}{ccc}
\boldsymbol{C}_{11} & \cdots & \boldsymbol{C}_{1 q} \\
\vdots & & \vdots \\
\boldsymbol{C}_{p 1} & \cdots & \boldsymbol{C}_{p q}
\end{array}\right] .
$$
The requirements are that
    - the number of columns in $\boldsymbol{A}$ is equal to the number of rows in $\boldsymbol{B}$.
    - the position of the vertical partition lines in $\boldsymbol{A}$ has to mach the position of the horizontal partition lines in $\boldsymbol{B}$. The horizontal lines in $\boldsymbol{A}$ and the vertical lines in $\boldsymbol{B}$ can be anywhere.

### 2.5.2 Triangular Matrices

We need some basic facts about triangular matrices and we start with
Lemma 2.4 (Inverse of a Block Triangular Matrix) Suppose

$$
\boldsymbol{A}=\left[\begin{array}{cc}
\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\
\mathbf{0} & \boldsymbol{A}_{22}
\end{array}\right]
$$

where $\boldsymbol{A}, \boldsymbol{A}_{11}$ and $\boldsymbol{A}_{22}$ are square matrices. Then $\boldsymbol{A}$ is nonsingular if and only if both $\boldsymbol{A}_{11}$ and $\boldsymbol{A}_{22}$ are nonsingular. In that case

$$
\boldsymbol{A}^{-1}=\left[\begin{array}{cc}
\boldsymbol{A}_{11}^{-1} & \boldsymbol{C} \\
\mathbf{0} & \boldsymbol{A}_{22}^{-1}
\end{array}\right],
$$

for some matrix $\boldsymbol{C}$.
Proof Suppose $\boldsymbol{A}$ is nonsingular. We partition $\boldsymbol{B}:=\boldsymbol{A}^{-1}$ conformally with $\boldsymbol{A}$ and have

$$
\boldsymbol{B} \boldsymbol{A}=\left[\begin{array}{ll}
\boldsymbol{B}_{11} & \boldsymbol{B}_{12} \\
\boldsymbol{B}_{21} & \boldsymbol{B}_{22}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\
\mathbf{0} & \boldsymbol{A}_{22}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{I} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{I}
\end{array}\right]=\boldsymbol{I}
$$

Using block-multiplication we find

$$
\boldsymbol{B}_{11} \boldsymbol{A}_{11}=\boldsymbol{I}, \boldsymbol{B}_{21} \boldsymbol{A}_{11}=\mathbf{0}, \boldsymbol{B}_{21} \boldsymbol{A}_{12}+\boldsymbol{B}_{22} \boldsymbol{A}_{22}=\boldsymbol{I}, \boldsymbol{B}_{11} \boldsymbol{A}_{12}+\boldsymbol{B}_{12} \boldsymbol{A}_{22}=\mathbf{0} .
$$

The first equation implies that $\boldsymbol{A}_{11}$ is nonsingular, this in turn implies that $\boldsymbol{B}_{21}=$ $\mathbf{0 A}_{11}^{-1}=\mathbf{0}$ in the second equation, and then the third equation simplifies to $\boldsymbol{B}_{22} \boldsymbol{A}_{22}=\boldsymbol{I}$. We conclude that also $\boldsymbol{A}_{22}$ is nonsingular. From the fourth equation we find

$$
\boldsymbol{B}_{12}=\boldsymbol{C}=-\boldsymbol{A}_{11}^{-1} \boldsymbol{A}_{12} \boldsymbol{A}_{22}^{-1} .
$$

Conversely, if $\boldsymbol{A}_{11}$ and $\boldsymbol{A}_{22}$ are nonsingular then

$$
\left[\begin{array}{cc}
\boldsymbol{A}_{11}^{-1} & -\boldsymbol{A}_{11}^{-1} \boldsymbol{A}_{12} \boldsymbol{A}_{22}^{-1} \\
\mathbf{0} & \boldsymbol{A}_{22}^{-1}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\
\mathbf{0} & \boldsymbol{A}_{22}
\end{array}\right]=\left[\begin{array}{ll}
\boldsymbol{I} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{I}
\end{array}\right]=\boldsymbol{I}
$$

and $\boldsymbol{A}$ is nonsingular with the indicated inverse. $\square$

Consider now a triangular matrix.
Lemma 2.5 (Inverse of a Triangular Matrix) An upper (lower) triangular matrix $\boldsymbol{A}=\left[a_{i j}\right] \in \mathbb{C}^{n \times n}$ is nonsingular if and only if the diagonal elements $a_{i i}$, $i=1, \ldots, n$ are nonzero. In that case the inverse is upper (lower) triangular with diagonal elements $a_{i i}^{-1}, i=1, \ldots, n$.

Proof We use induction on $n$. The result holds for $n=1$. The 1-by-1 matrix $\boldsymbol{A}=$ [ $a_{11}$ ] is nonsingular if and only if $a_{11} \neq \mathbf{0}$ and in that case $\boldsymbol{A}^{-1}=\left[a_{11}^{-1}\right]$. Suppose the result holds for $n=k$ and let $\boldsymbol{A} \in \mathbb{C}^{(k+1) \times(k+1)}$ be upper triangular. We partition $\boldsymbol{A}$ in the form

$$
\boldsymbol{A}=\left[\begin{array}{cc}
\boldsymbol{A}_{k} & \boldsymbol{a}_{k} \\
\mathbf{0} & a_{k+1, k+1}
\end{array}\right]
$$

and note that $\boldsymbol{A}_{k} \in \mathbb{C}^{k \times k}$ is upper triangular. By Lemma $2.4 \boldsymbol{A}$ is nonsingular if and only if $\boldsymbol{A}_{k}$ and $\left(a_{k+1, k+1}\right)$ are nonsingular and in that case

$$
\boldsymbol{A}^{-1}=\left[\begin{array}{cc}
\boldsymbol{A}_{k}^{-1} & \boldsymbol{c} \\
\mathbf{0} & a_{k+1, k+1}^{-1}
\end{array}\right],
$$

for some $\boldsymbol{c} \in \mathbb{C}^{n}$. By the induction hypothesis $\boldsymbol{A}_{k}$ is nonsingular if and only if the diagonal elements $a_{11}, \ldots, a_{k k}$ of $\boldsymbol{A}_{k}$ are nonzero and in that case $\boldsymbol{A}_{k}^{-1}$ is upper triangular with diagonal elements $a_{i i}^{-1}, i=1, \ldots, k$. The result for $\boldsymbol{A}$ follows. $\square$

Lemma 2.6 (Product of Triangular Matrices) The product $\boldsymbol{C}=\boldsymbol{A B}=\left(c_{i j}\right)$ of two upper (lower) triangular matrices $\boldsymbol{A}=\left(a_{i j}\right)$ and $\boldsymbol{B}=\left(b_{i j}\right)$ is upper (lower) triangular with diagonal elements $c_{i i}=a_{i i} b_{i i}$ for all $i$.

Proof Exercise. $\square$

A matrix is called unit triangular if it is triangular with 1's on the diagonal.

Lemma 2.7 (Unit Triangular Matrices) For a unit upper (lower) triangular matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ :

1. $\boldsymbol{A}$ is nonsingular and the inverse is unit upper(lower) triangular.
2. The product of two unit upper (lower) triangular matrices is unit upper (lower) triangular.

Proof 1. follows from Lemma 2.5, while Lemma 2.6 implies 2. $\square$

### 2.6 Exercises Chap. 2

### 2.6.1 Exercises Sect. 2.1

Exercise 2.1 (The Shifted Power Basis Is a Basis) Show that the polynomials $\left\{\left(x-x_{i}\right)^{j}\right\}_{0 \leq j \leq n}$ is a basis for polynomials of degree $n .^{3}$

Exercise 2.2 (The Natural Spline, $n=1$ ) How can one define an $N$-spline when $n=1$ ?

Exercise 2.3 (Bounding the Moments) Show that for the $N$-spline the solution of the linear system (2.11) is bounded as follows ${ }^{4}$ :

$$
\max _{2 \leq j \leq n}\left|\mu_{j}\right| \leq \frac{3}{h^{2}} \max _{2 \leq i \leq n}\left|y_{i+1}-2 y_{i}+y_{i-1}\right| .
$$

Exercise 2.4 (Moment Equations for 1. Derivative Boundary Conditions) Suppose instead of the $D_{2}$ boundary conditions we use $D_{1}$ conditions given by $g^{\prime}(a)=$ $s_{1}$ and $g^{\prime}(b)=s_{n+1}$ for some given numbers $s_{1}$ and $s_{n+1}$. Show that the linear system for the moments of a $D_{1}$-spline can be written

$$
\left[\begin{array}{ccccc}
2 & 1 & & & \\
1 & 4 & 1 & & \\
& \ddots & \ddots & \ddots & \\
& & 1 & 4 & 1 \\
& & & 1 & 2
\end{array}\right]\left[\begin{array}{c}
\mu_{1} \\
\mu_{2} \\
\vdots \\
\mu_{n} \\
\mu_{n+1}
\end{array}\right]=\frac{6}{h^{2}}\left[\begin{array}{c}
y_{2}-y_{1}-h s_{1} \\
\delta^{2} y_{2} \\
\delta^{2} y_{3} \\
\vdots \\
\delta^{2} y_{n-1} \\
\delta^{2} y_{n} \\
h s_{n+1}-y_{n+1}+y_{n}
\end{array}\right],
$$

where $\delta^{2} y_{i}:=y_{i+1}-2 y_{i}+y_{i-1}, i=2, \ldots, n$. Hint: Use (2.10) to compute $g^{\prime}\left(x_{1}\right)$ and $g^{\prime}\left(x_{n+1}\right)$, Is $g$ unique?

[^4]Exercise 2.5 (Minimal Norm Property of the Natural Spline) Study proof of the following theorem. ${ }^{5}$

Theorem 2.5 (Minimal Norm Property of a Cubic Spline) Suppose $g$ is an $N$ -spline. Then

$$
\int_{a}^{b}\left(g^{\prime \prime}(x)\right)^{2} d x \leq \int_{a}^{b}\left(h^{\prime \prime}(x)\right)^{2} d x
$$

for all $h \in C^{2}[a, b]$ such that $h\left(x_{i}\right)=g\left(x_{i}\right), i=1, \ldots, n+1$.
Proof Let $h$ be any interpolant as in the theorem. We first show the orthogonality condition

$$
\int_{a}^{b} g^{\prime \prime} e^{\prime \prime}=0, \quad e:=h-g .
$$

Integration by parts gives $\int_{a}^{b} g^{\prime \prime} e^{\prime \prime}=\left[g^{\prime \prime} e^{\prime}\right]_{a}^{b}-\int_{a}^{b} g^{\prime \prime \prime} e^{\prime}$. The first term is zero since $g^{\prime \prime}$ is continuous and $g^{\prime \prime}(b)=g^{\prime \prime}(a)=0$. For the second term, since $g^{\prime \prime \prime}$ is equal to a constant $v_{i}$ on each subinterval ( $x_{i}, x_{i+1}$ ) and $e\left(x_{i}\right)=0$, for $i=1, \ldots, n+1$

$$
\int_{a}^{b} g^{\prime \prime \prime} e^{\prime}=\sum_{i=1}^{n} \int_{x_{i}}^{x_{i+1}} g^{\prime \prime \prime} e^{\prime}=\sum_{i=1}^{n} v_{i} \int_{x_{i}}^{x_{i+1}} e^{\prime}=\sum_{i=1}^{n} v_{i}\left(e\left(x_{i+1}\right)-e\left(x_{i}\right)\right)=0 .
$$

Writing $h=g+e$ and using (2.35)

$$
\begin{aligned}
\int_{a}^{b}\left(h^{\prime \prime}\right)^{2} & =\int_{a}^{b}\left(g^{\prime \prime}+e^{\prime \prime}\right)^{2} \\
& =\int_{a}^{b}\left(g^{\prime \prime}\right)^{2}+\int_{a}^{b}\left(e^{\prime \prime}\right)^{2}+2 \int_{a}^{b} g^{\prime \prime} e^{\prime \prime} \\
& =\int_{a}^{b}\left(g^{\prime \prime}\right)^{2}+\int_{a}^{b}\left(e^{\prime \prime}\right)^{2} \geq \int_{a}^{b}\left(g^{\prime \prime}\right)^{2}
\end{aligned}
$$

and the proof is complete. $\square$

Exercise 2.6 (Computing the $D_{2}$-Spline) Let $g$ be the $D_{2}$-spline corresponding to an interval $[a, b]$, a vector $\boldsymbol{y} \in \mathbb{R}^{n+1}$ and $\mu_{1}, \mu_{n+1}$. The vector $\boldsymbol{x}=\left[x_{1}, \ldots, x_{n}\right]$ and

[^5]the coefficient matrix $\boldsymbol{C} \in \mathbb{R}^{n \times 4}$ in (2.7) are returned in the following algorithm. It uses Algorithms 2.1 and 2.2 to solve the tridiagonal linear system.

```
function [x,C]=splineint(a,b,y,mu1,munp1)
% [x,C]=splineint(a,b,y,mul,munp1)
y=y(:); n=length(y)-1;
h=(b-a)/n; x=a:h:b-h; c=ones(n-2,1);
[l,u]= trifactor(c,4*ones(n-1,1),c);
b1=6/h^2*(y(3:n+1)-2*y(2:n)+y(1:n-1));
b1(1)=b1(1)-mu1; b1(n-1)=b1(n-1)-munp1;
mu= [mu1;trisolve(l,u,c,b1);munp1];
C=zeros(4*n,1);
C(1:4:4*n-3)=y(1:n);
C(2:4:4*n-2)=(y(2:n+1)-y(1:n))/h...
    -h*mu(1:n)/3-h*mu(2:n+1)/6;
C(3:4:4*n-1)=mu(1:n)/2;
C(4:4:4*n)=(mu(2:n+1)-mu(1:n))/(6*h);
C=reshape (C,4,n) ';
end
```

Listing 2.3 splineint

Use the algorithm to compute the $c_{i, j}$ in Example 2.2.
Exercise 2.7 (Spline Evaluation) To plot a piecewise polynomial $g$ in the form (2.4) we need to compute values $g\left(r_{j}\right)$ at a number of sites $\boldsymbol{r}=\left[r_{1}, \ldots, r_{m}\right] \in$ $\mathbb{R}^{m}$ for some reasonably large integer $m$. To determine $g\left(r_{j}\right)$ for some $j$ we need to find an integer $i_{j}$ so that $g\left(r_{j}\right)=p_{i_{j}}\left(r_{j}\right)$.

Given $k \in \mathbb{N}, \boldsymbol{t}=\left[t_{1}, \ldots, t_{k}\right]$ and a real number $x$. We consider the problem of computing an integer $i$ so that $i=1$ if $x<t_{2}, i=k$ if $x \geq t_{k}$, and $t_{i} \leq$ $x<t_{i+1}$ otherwise. If $\boldsymbol{x} \in \mathbb{R}^{m}$ is a vector then an $m$-vector $\boldsymbol{i}$ should be computed, such that the $j$ th component of $\boldsymbol{i}$ gives the location of the $j$ th component of $\boldsymbol{x}$. The following MATLAB function determines $\boldsymbol{i}=\left[i_{1}, \ldots, i_{m}\right]$. It uses the built in MATLAB functions length, min, sort, find.

```
function i = findsubintervals(t,x)
%i = findsubintervals(t,x)
k=length(t); m=length(x);
    if k<2
        i=ones (m,1) ;
    else
        t (1) = min (x (1) , t (1) ) - 1;
        [~,j]=sort([t(:)',x(:)']);
        i=(find(j>k)-(1:m))';
    end
```

Listing 2.4 findsubintervals

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-070.jpg?height=704&width=963&top_left_y=213&top_left_x=282)
Fig. 2.5 The cubic spline interpolating $f(x)=\arctan (10 x)+\pi / 2$ at 14 equidistant sites on $[-1,1]$. The exact function is also shown

Use findsubintervals and the algorithm splineval below to make the plots in Fig. 2.5.

```
function [X,G]=splineval(x,C,X)
% [X,G]=splineval(x,C,X)
m=length(X);
i=findsubintervals(x,X);
G=zeros(m,1);
for j=1:m
        k=i(j);
        t=X(j)-x(k);
    G(j)=[1,t,t^2,t^3]*C(k,:)';
end
```

Listing 2.5 splineval

Given output $\boldsymbol{x}, \boldsymbol{C}$ of splineint, defining a cubic spline $g$, and a vector $\boldsymbol{X}$, splinevalăcomputes the vector $\boldsymbol{G}=g(\boldsymbol{X})$.

### 2.6.2 Exercises Sect. 2.2

Exercise 2.8 (Central Difference Approximation of 2. Derivative) Consider

$$
\delta^{2} f(x):=\frac{f(x+h)-2 f(x)+f(x-h)}{h^{2}}, \quad h>0, \quad f:[x-h, x+h] \rightarrow \mathbb{R} .
$$

a) Show using Taylor expansion that if $f \in C^{2}[x-h, x+h]$ then for some $\eta_{2}$
$$
\delta^{2} f(x)=f^{\prime \prime}\left(\eta_{2}\right), \quad x-h<\eta_{2}<x+h .
$$
b) Show that if $f \in C^{4}[x-h, x+h]$ then for some $\eta_{4}$
$$
\delta^{2} f(x)=f^{\prime \prime}(x)+\frac{h^{2}}{12} f^{(4)}\left(\eta_{4}\right), \quad x-h<\eta_{4}<x+h .
$$
$\delta^{2} f(x)$ is known as the central difference approximation to the second derivative at $x$.

Exercise 2.9 (Two Point Boundary Value Problem) We consider a finite difference method for the two point boundary value problem

$$
\begin{aligned}
-u^{\prime \prime}(x)+r(x) u^{\prime}(x)+q(x) u(x) & =f(x), \text { for } x \in[a, b], \\
u(a) & =g_{0}, \quad u(b)=g_{1} .
\end{aligned}
$$

We assume that the given functions $f, q$ and $r$ are continuous on $[a, b]$ and that $q(x) \geq 0$ for $x \in[a, b]$. It can then be shown that (2.36) has a unique solution $u$.

To solve (2.36) numerically we choose $m \in \mathbb{N}, h=(b-a) /(m+1), x_{j}=a+j h$ for $j=0,1, \ldots, m+1$ and solve the difference equation

$$
\frac{-v_{j-1}+2 v_{j}-v_{j+1}}{h^{2}}+r\left(x_{j}\right) \frac{v_{j+1}-v_{j-1}}{2 h}+q\left(x_{j}\right) v_{j}=f\left(x_{j}\right), \quad j=1, \ldots, m,
$$

with $v_{0}=g_{0}$ and $v_{m+1}=g_{1}$.

a) Show that (2.37) leads to a tridiagonal linear system $\boldsymbol{A} \boldsymbol{v}=\boldsymbol{b}$, where $\boldsymbol{A}=$ $\operatorname{tridiag}\left(a_{j}, d_{j} . c_{j}\right) \in \mathbb{R}^{m \times m}$ has elements
$$
a_{j}=-1-\frac{h}{2} r\left(x_{j}\right), c_{j}=-1+\frac{h}{2} r\left(x_{j}\right), d_{j}=2+h^{2} q\left(x_{j}\right) \text {, }
$$

and

$$
b_{j}= \begin{cases}h^{2} f\left(x_{1}\right)-a_{1} g_{0}, & \text { if } j=1, \\ h^{2} f\left(x_{j}\right), & \text { if } 2 \leq j \leq m-1, \\ h^{2} f\left(x_{m}\right)-c_{m} g_{1}, & \text { if } j=m .\end{cases}
$$

b) Show that the linear system satisfies the conditions in Theorem 2.4 if the spacing $h$ is so small that $\frac{h}{2}|r(x)|<1$ for all $x \in[a, b]$.
(c) Propose a method to find $v_{1}, \ldots, v_{m}$.

Exercise 2.10 (Two Point Boundary Value Problem; Computation)

a) Consider the problem (2.36) with $r=0, f=q=1$ and boundary conditions $u(0)=1, u(1)=0$. The exact solution is $u(x)=1-\sinh x / \sinh 1$. Write a computer program to solve (2.37) for $h=0.1,0.05,0.025,0.0125$, and compute the "error" $\max _{1 \leq j \leq m}\left|u\left(x_{j}\right)-v_{j}\right|$ for each $h$.
b) Make a combined plot of the solution $u$ and the computed points $v_{j}, j=$ $0, \ldots, m+1$ for $h=0.1$.
c) One can show that the error is proportional to $h^{p}$ for some integer $p$. Estimate $p$ based on the error for $h=0.1,0.05,0.025,0.0125$.

### 2.6.3 Exercises Sect. 2.3

Exercise 2.11 (Approximate Force) Show that

$$
F=\frac{4 \sin ^{2}(\pi h / 2) R}{h^{2} L^{2}}=\frac{\pi^{2} R}{L^{2}}+O\left(h^{2}\right) .
$$

Exercise 2.12 (Symmetrize Matrix (Exam Exercise 1977-3)) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be tridiagonal and suppose $a_{i, i+1} a_{i+1, i}>0$ for $i=1, \ldots, n-1$. Show that there exists a diagonal matrix $\boldsymbol{D}=\operatorname{diag}\left(d_{1}, \ldots, d_{n}\right)$ with $d_{i}>0$ for all $i$ such that $\boldsymbol{B}:=\boldsymbol{D} \boldsymbol{A} \boldsymbol{D}^{-1}$ is symmetric.

### 2.6.4 Exercises Sect. 2.4

Exercise 2.13 (Eigenpairs $\boldsymbol{T}$ of Order 2) Compute directly the eigenvalues and eigenvectors for $\boldsymbol{T}$ when $n=2$ and thus verify Lemma 2.2 in this case.

Exercise 2.14 (LU Factorization of 2. Derivative Matrix) Show that $\boldsymbol{T}=\boldsymbol{L} \boldsymbol{U}$, where

$$
\boldsymbol{L}=\left[\begin{array}{ccccc}
1 & 0 & \cdots & \cdots & 0 \\
-\frac{1}{2} & 1 & \ddots & & \vdots \\
0 & -\frac{2}{3} & 1 & \ddots & \vdots \\
\vdots & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & 0 & -\frac{m-1}{m} & 1
\end{array}\right], \boldsymbol{U}=\left[\begin{array}{ccccc}
2 & -1 & 0 & \cdots & 0 \\
0 & \frac{3}{2} & -1 & \ddots & \vdots \\
\vdots & \ddots & \ddots & \ddots & 0 \\
\vdots & \ddots & \frac{m}{m-1} & -1 \\
0 & \cdots & \cdots & 0 & \frac{m+1}{m}
\end{array}\right] .
$$

This is the LU factorization of $\boldsymbol{T}$.
Exercise 2.15 (Inverse of the 2. Derivative Matrix) Let $\boldsymbol{S} \in \mathbb{R}^{m \times m}$ have elements $s_{i j}$ given by

$$
s_{i, j}=s_{j, i}=\frac{1}{m+1} j(m+1-i), \quad 1 \leq j \leq i \leq m .
$$

Show that $\boldsymbol{S} \boldsymbol{T}=\boldsymbol{I}$ and conclude that $\boldsymbol{T}^{-1}=\boldsymbol{S}$.

### 2.6.5 Exercises Sect. 2.5

Exercise 2.16 (Matrix Element as a Quadratic Form) For any matrix $\boldsymbol{A}$ show that $a_{i j}=\boldsymbol{e}_{i}^{T} \boldsymbol{A} \boldsymbol{e}_{j}$ for all $i, j$.

Exercise 2.17 (Outer Product Expansion of a Matrix) For any matrix $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ show that $\boldsymbol{A}=\sum_{i=1}^{m} \sum_{j=1}^{n} a_{i j} \boldsymbol{e}_{i} \boldsymbol{e}_{j}^{T}$.

Exercise 2.18 (The Product $\boldsymbol{A}^{T} \boldsymbol{A}$ ) Let $\boldsymbol{B}=\boldsymbol{A}^{T} \boldsymbol{A}$. Explain why this product is defined for any matrix $\boldsymbol{A}$. Show that $b_{i j}=\boldsymbol{a}_{: i}^{T} \boldsymbol{a}_{: j}$ for all $i, j$.

Exercise 2.19 (Outer Product Expansion) For $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ and $\boldsymbol{B} \in \mathbb{R}^{p \times n}$ show that

$$
\boldsymbol{A} \boldsymbol{B}^{T}=\boldsymbol{a}_{: 1} \boldsymbol{b}_{: 1}^{T}+\boldsymbol{a}_{: 2} \boldsymbol{b}_{: 2}^{T}+\cdots+\boldsymbol{a}_{: n} \boldsymbol{b}_{: n}^{T} .
$$

This is called the outer product expansion of the columns of $\boldsymbol{A}$ and $\boldsymbol{B}$.
Exercise 2.20 (System with Many Right Hand Sides; Compact Form) Suppose $\boldsymbol{A} \in \mathbb{R}^{m \times n}, \boldsymbol{B} \in \mathbb{R}^{m \times p}$, and $\boldsymbol{X} \in \mathbb{R}^{n \times p}$. Show that

$$
\boldsymbol{A} \boldsymbol{X}=\boldsymbol{B} \quad \Longleftrightarrow \quad \boldsymbol{A} \boldsymbol{x}_{: j}=\boldsymbol{b}_{: j}, j=1, \ldots, p .
$$

Exercise 2.21 (Block Multiplication Example) Suppose $\boldsymbol{A}=\left[\boldsymbol{A}_{1}, \boldsymbol{A}_{2}\right]$ and $\boldsymbol{B}=$ $\left[\begin{array}{c}\boldsymbol{B}_{1} \\ \mathbf{0}\end{array}\right]$. When is $\boldsymbol{A} \boldsymbol{B}=\boldsymbol{A}_{1} \boldsymbol{B}_{1}$ ?

Exercise 2.22 (Another Block Multiplication Example) Suppose $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C} \in$ $\mathbb{R}^{n \times n}$ are given in block form by

$$
\boldsymbol{A}:=\left[\begin{array}{ll}
\lambda & \boldsymbol{a}^{T} \\
\mathbf{0} & \boldsymbol{A}_{1}
\end{array}\right], \quad \boldsymbol{B}:=\left[\begin{array}{ll}
1 & \mathbf{0}^{T} \\
\mathbf{0} & \boldsymbol{B}_{1}
\end{array}\right], \quad \boldsymbol{C}:=\left[\begin{array}{ll}
1 & \mathbf{0}^{T} \\
\mathbf{0} & \boldsymbol{C}_{1}
\end{array}\right],
$$

where $\boldsymbol{A}_{1}, \boldsymbol{B}_{1}, \boldsymbol{C}_{1} \in \mathbb{R}^{(n-1) \times(n-1)}$. Show that

$$
\boldsymbol{C} \boldsymbol{A} \boldsymbol{B}=\left[\begin{array}{cc}
\lambda & \boldsymbol{a}^{T} \boldsymbol{B}_{1} \\
\mathbf{0} & \boldsymbol{C}_{1} \boldsymbol{A}_{1} \boldsymbol{B}_{1}
\end{array}\right] .
$$

### 2.7 Review Questions

2.7.1 How do we define nonsingularity of a matrix?
2.7.2 Define the second derivative matrix $\boldsymbol{T}$. How did we show that it is nonsingular?
2.7.3 Why do we not use the explicit inverse of $\boldsymbol{T}$ to solve the linear system $\boldsymbol{T} \boldsymbol{x}=\boldsymbol{b} ?$
2.7.4 What are the eigenpairs of the matrix $\boldsymbol{T}$ ?
2.7.5 Why are the diagonal elements of a Hermitian matrix real?
2.7.6 Is the matrix $\left[\begin{array}{cc}1 & 1+i \\ 1+i & 2\end{array}\right]$ Hermitian? Symmetric?
2.7.7 Is a weakly diagonally dominant matrix nonsingular?
2.7.8 Is a strictly diagonally dominant matrix always nonsingular?
2.7.9 Does a tridiagonal matrix always have an LU factorization?

## Chapter 3 <br> Gaussian Elimination and LU Factorizations

In this chapter we first review Gaussian elimination. Gaussian elimination leads to an LU factorization of the coefficient matrix or more generally to a PLU factorization, if row interchanges are introduced. Here $\boldsymbol{P}$ is a permutation matrix, $\boldsymbol{L}$ is lower triangular and $\boldsymbol{U}$ is upper triangular.

We also consider in great detail the general theory of LU factorizations.

### 3.13 by 3 Example

Gaussian elimination with row interchanges is the classical method for solving $n$ linear equations in $n$ unknowns. ${ }^{1}$ We first recall how it works on a $3 \times 3$ system.

Example 3.1 (Gaussian Elimination on a 3 × 3 System) Consider a nonsingular system of three equations in three unknowns:

$$
\begin{array}{ll}
a_{11}^{(1)} x_{1}+a_{12}^{(1)} x_{2}+a_{13}^{(1)} x_{3}=b_{1}^{(1)}, & \mathrm{I} \\
a_{21}^{(1)} x_{1}+a_{22}^{(1)} x_{2}+a_{23}^{(1)} x_{3}=b_{2}^{(1)}, & \mathrm{II} \\
a_{31}^{(1)} x_{1}+a_{32}^{(1)} x_{2}+a_{33}^{(1)} x_{3}=b_{3}^{(1)} . & \mathrm{III} .
\end{array}
$$

[^6]To solve this system by Gaussian elimination suppose $a_{11}^{(1)} \neq 0$. We subtract $l_{21}^{(1)}:=$ $a_{21}^{(1)} / a_{11}^{(1)}$ times equation I from equation II and $l_{31}^{(1)}:=a_{31}^{(1)} / a_{11}^{(1)}$ times equation I from equation III. The result is

$$
\begin{aligned}
a_{11}^{(1)} x_{1}+a_{12}^{(1)} x_{2}+a_{13}^{(1)} x_{3}=b_{1}^{(1)}, & \mathrm{I} \\
a_{22}^{(2)} x_{2}+a_{23}^{(2)} x_{3}=b_{2}^{(2)}, & \mathrm{II}^{\prime} \\
a_{32}^{(2)} x_{2}+a_{33}^{(2)} x_{3}=b_{3}^{(2)}, & \mathrm{III}^{\prime},
\end{aligned}
$$

where $b_{i}^{(2)}=b_{i}^{(1)}-l_{i 1}^{(1)} b_{i}^{(1)}$ for $i=2,3$ and $a_{i j}^{(2)}=a_{i j}^{(1)}-l_{i, 1}^{(1)} a_{1 j}^{(1)}$ for $i, j=2,3$. If $a_{11}^{(1)}=0$ and $a_{21}^{(1)} \neq 0$ we first interchange equation I and equation II. If $a_{11}^{(1)}=$ $a_{21}^{(1)}=0$ we interchange equation I and III. Since the system is nonsingular the first column cannot be zero and an interchange is always possible.

If $a_{22}^{(2)} \neq 0$ we subtract $l_{32}^{(2)}:=a_{32}^{(2)} / a_{22}^{(2)}$ times equation II ${ }^{\prime}$ from equation III ${ }^{\prime}$ to obtain

$$
\begin{aligned}
a_{11}^{(1)} x_{1}+a_{12}^{(1)} x_{2}+a_{13}^{(1)} x_{3}=b_{1}^{(1)}, & \mathrm{I} \\
a_{22}^{(2)} x_{2}+a_{23}^{(2)} x_{3}=b_{2}^{(2)}, & \mathrm{II}^{\prime} \\
a_{33}^{(3)} x_{3}=b_{3}^{(3)}, & \mathrm{III}^{\prime \prime},
\end{aligned}
$$

where $a_{33}^{(3)}=a_{33}^{(2)}-l_{32}^{(2)} a_{23}^{(2)}$ and $b_{3}^{(3)}=b_{3}^{(2)}-l_{32}^{(2)} b_{2}^{(2)}$. If $a_{22}^{(2)}=0$ then $a_{32}^{(2)} \neq 0$ (cf. Sect. 3.4) and we first interchange equation II ${ }^{\prime}$ and equation III ${ }^{\prime}$. The reduced system is easy to solve since it is upper triangular. Starting from the bottom and moving upwards we find

$$
\begin{aligned}
& x_{3}=b_{3}^{(3)} / a_{33}^{(3)} \\
& x_{2}=\left(b_{2}^{(2)}-a_{23}^{(2)} x_{3}\right) / a_{22}^{(2)} \\
& x_{1}=\left(b_{1}^{(1)}-a_{12}^{(1)} x_{2}-a_{13}^{(1)} x_{3}\right) / a_{11}^{(1)} .
\end{aligned}
$$

This is known as back substitution. Gauss elimination leads to an LU factorization. Indeed, if $a_{k k}^{(k)} \neq 0, k=1,2$ then

$$
\begin{aligned}
\boldsymbol{L} \boldsymbol{U} & :=\left[\begin{array}{ccc}
1 & 0 & 0 \\
l_{21}^{(1)} & 1 & 0 \\
l_{31}^{(1)} & l_{32}^{(2)} & 1
\end{array}\right]\left[\begin{array}{ccc}
a_{11}^{(1)} & a_{12}^{(1)} & a_{13}^{(1)} \\
0 & a_{22}^{(2)} & a_{23}^{(2)} \\
0 & 0 & a_{33}^{(3)}
\end{array}\right] \\
= & {\left[\begin{array}{ccc}
a_{11}^{(1)} & a_{12}^{(1)} & a_{13}^{(1)} \\
l_{21}^{(1)} a_{11}^{(1)} & l_{21}^{(1)} a_{12}^{(1)}+a_{22}^{(2)} & l_{21}^{(1)} a_{13}^{(1)}+a_{23}^{(2)} \\
l_{31}^{(1)} a_{11}^{(1)} & l_{31}^{(1)} a_{12}^{(1)}+l_{32}^{(2)} a_{22}^{(2)} & l_{31}^{(1)} a_{13}^{(1)}+l_{32}^{(2)} a_{23}^{(2)}+a_{33}^{(3)}
\end{array}\right]=\left[\begin{array}{lll}
a_{11}^{(1)} & a_{12}^{(1)} & a_{13}^{(1)} \\
a_{21}^{(1)} & a_{22}^{(1)} & a_{23}^{(1)} \\
a_{31}^{(1)} & a_{32}^{(1)} & a_{33}^{(1)}
\end{array}\right]=\boldsymbol{A} . }
\end{aligned}
$$

Thus Gaussian elimination leads to an LU factorization of the coefficient matrix $\boldsymbol{A}^{(1)}$ (cf. the proof of Theorem 3.2).

### 3.2 Gauss and LU

In Gaussian elimination without row interchanges we start with a linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ and generate a sequence of equivalent systems $\boldsymbol{A}^{(k)} \boldsymbol{x}=\boldsymbol{b}^{(k)}$ for $k=$ $1, \ldots, n$, where $\boldsymbol{A}^{(1)}=\boldsymbol{A}, \boldsymbol{b}^{(1)}=\boldsymbol{b}$, and $\boldsymbol{A}^{(k)}$ has zeros under the diagonal in its first $k-1$ columns. Thus $\boldsymbol{A}^{(n)}$ is upper triangular and the system $\boldsymbol{A}^{(n)} \boldsymbol{x}=\boldsymbol{b}^{(n)}$ is easy to solve. The process is illustrated in Fig. 3.1.

The matrix $\boldsymbol{A}^{(k)}$ takes the form

$$
\boldsymbol{A}^{(k)}=\left[\begin{array}{ccc|ccccc}
a_{1,1}^{(1)} & \cdots & a_{1, k-1}^{(1)} & a_{1, k}^{(1)} & \cdots & a_{1, j}^{(1)} & \cdots & a_{1, n}^{(1)} \\
& \ddots & \vdots & \vdots & & \vdots & & \vdots \\
& & a_{k-1, k-1}^{(k-1)} & a_{k-1, k}^{(k-1)} & \cdots & a_{k-1, j}^{(k-1)} & \cdots & a_{k-1, n}^{(k-1)} \\
\hline & & & a_{k, k}^{(k)} & \cdots & a_{k, j}^{(k)} & \cdots & a_{k, n}^{(k)} \\
& & & \vdots & & \vdots & & \vdots \\
& & & a_{i, k}^{(k)} & \cdots & a_{i, j}^{(k)} & \cdots & a_{i, n}^{(k)} \\
& & & \vdots & & \vdots & & \vdots \\
& & & a_{n, k}^{(k)} & \cdots & a_{n, j}^{(k)} & \cdots & a_{n, n}^{(k)}
\end{array}\right] .
$$

The process transforming $\boldsymbol{A}^{(k)}$ into $\boldsymbol{A}^{(k+1)}$ for $k=1, \ldots, n-1$ can be described as follows.

$$
\text { for } \begin{aligned}
i & =k+1: n \\
l_{i k}^{(k)} & =a_{i k}^{(k)} / a_{k k}^{(k)}
\end{aligned}
$$

$$
\text { for } j=k: n
$$

$$
a_{i j}^{(k+1)}=a_{i j}^{(k)}-l_{i k}^{(k)} a_{k j}^{(k)}
$$

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-077.jpg?height=274&width=965&top_left_y=1748&top_left_x=280)
Fig. 3.1 Gaussian elimination

For $j=k$ it follows from (3.2) that $a_{i k}^{(k+1)}=a_{i k}^{(k)}-\frac{a_{i k}^{(k)}}{a_{k k}^{(k)}} a_{k k}^{(k)}=0$ for $i=$ $k+1, \ldots, n$. Thus $\boldsymbol{A}^{(k+1)}$ will have zeros under the diagonal in its first $k$ columns and the elimination is carried one step further. The numbers $l_{i k}^{(k)}$ in (3.2) are called multipliers.

Gaussian elimination with no row interchanges is valid if and only if the pivots $a_{k k}^{(k)}$ are nonzero for $k=1, \ldots, n-1$. This depends on certain submatrices of $\boldsymbol{A}$ known as principal submatrices.
Definition 3.1 (Principal Submatrix) For $k=1, \ldots, n$ the matrices $\boldsymbol{A}_{[k]} \in \mathbb{C}^{k \times k}$ given by

$$
\boldsymbol{A}_{[k]}:=\boldsymbol{A}(1: k, 1: k)=\left[\begin{array}{ccc}
a_{11} & \cdots & a_{k 1} \\
\vdots & & \vdots \\
a_{k 1} & \cdots & a_{k k}
\end{array}\right]
$$

are called the leading principal submatrices of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. More generally, a matrix $\boldsymbol{B} \in \mathbb{C}^{k \times k}$ is called a principal submatrix of $\boldsymbol{A}$ if $\boldsymbol{B}=\boldsymbol{A}(\boldsymbol{r}, \boldsymbol{r})$, where $\boldsymbol{r}=\left[r_{1}, \ldots, r_{k}\right]$ for some $1 \leq r_{1}<\cdots<r_{k} \leq n$. Thus,

$$
b_{i, j}=a_{r_{i}, r_{j}}, \quad i, j=1, \ldots, k .
$$

The determinant of a (leading) principal submatrix is called a (leading) principal minor.

A principal submatrix is leading if $r_{j}=j$ for $j=1, \ldots, k$. Also a principal submatrix is special in that it uses the same rows and columns of $\boldsymbol{A}$. For $k=1$ The only principal submatrices of order $k=1$ are the diagonal elements of $\boldsymbol{A}$.

Example 3.2 (Principal Submatrices) The principal submatrices of $\boldsymbol{A}=\left[\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{array}\right]$ are

$$
[1],[5],[9],\left[\begin{array}{ll}
1 & 2 \\
4 & 5
\end{array}\right],\left[\begin{array}{ll}
1 & 3 \\
7 & 9
\end{array}\right],\left[\begin{array}{ll}
5 & 6 \\
8 & 9
\end{array}\right], \boldsymbol{A} .
$$

The leading principal submatrices are

$$
[1],\left[\begin{array}{ll}
1 & 2 \\
4 & 5
\end{array}\right], \boldsymbol{A} .
$$

Theorem 3.1 We have $a_{k, k}^{(k)} \neq 0$ for $k=1, \ldots, n-1$ if and only if the leading principal submatrices $\boldsymbol{A}_{[k]}$ of $\boldsymbol{A}$ are nonsingular for $k=1, \ldots, n-1$. Moreover

$$
\operatorname{det}\left(\boldsymbol{A}_{[k]}\right)=a_{11}^{(1)} a_{22}^{(2)} \cdots a_{k k}^{(k)}, \quad k=1, \ldots, n .
$$

Proof Let $\boldsymbol{B}_{k}=\boldsymbol{A}_{k-1}^{(k)}$ be the upper left $k-1$ corner of $\boldsymbol{A}^{(k)}$ given by (3.1). Observe that the elements of $\boldsymbol{B}_{k}$ are computed from $\boldsymbol{A}$ by using only elements from $\boldsymbol{A}_{[k-1]}$. Since the determinant of a matrix does not change under the operation of subtracting a multiple of one row from another row the determinant of $\boldsymbol{A}_{[k]}$ equals the product of diagonal elements of $\boldsymbol{B}_{k+1}$ and (3.3) follows. But then $a_{11}^{(1)} \cdots a_{k k}^{(k)} \neq 0$ for $k=$ $1, \ldots, n-1$ if and only if $\operatorname{det}\left(\boldsymbol{A}_{[k]}\right) \neq 0$ for $k=1, \ldots, n-1$, or equivalently $\boldsymbol{A}_{[k]}$ is nonsingular for $k=1, \ldots, n-1$. $\square$

Gaussian elimination is a way to compute the LU factorization of the coefficient matrix.

Theorem 3.2 Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ and that the leading principal submatrices $\boldsymbol{A}_{[k]}$ are nonsingular for $k=1, \ldots, n-1$. Then Gaussian elimination with no row interchanges results in an LU factorization of $\boldsymbol{A}$. In particular $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$, where

$$
\boldsymbol{L}=\left[\begin{array}{cccc}
1 & & & \\
l_{21}^{(1)} & 1 & & \\
\vdots & & \ddots & \\
l_{n 1}^{(1)} & l_{n 2}^{(2)} & \cdots & 1
\end{array}\right], \quad \boldsymbol{U}=\left[\begin{array}{ccc}
a_{11}^{(1)} & \cdots & a_{1 n}^{(1)} \\
& \ddots & \vdots \\
& & a_{n n}^{(n)}
\end{array}\right],
$$

where the $l_{i j}^{(j)}$ and $a_{i j}^{(i)}$ are given by (3.2).
Proof From (3.2) we have for all $i, j$

$$
l_{i k}^{(k)} a_{k j}^{(k)}=a_{i j}^{(k)}-a_{i j}^{(k+1)} \text { for } k<\min (i, j) \text {, and } l_{i j}^{(k)} a_{j j}^{(j)}=a_{i j}^{(j)} \text { for } i>j .
$$

Thus for $i \leq j$ we find

$$
(\boldsymbol{L} \boldsymbol{U})_{i j}=\sum_{k=1}^{i-1} l_{i k}^{(k)} a_{k j}^{(k)}+a_{i j}^{(i)}=\sum_{k=1}^{i-1}\left(a_{i j}^{(k)}-a_{i j}^{(k+1)}\right)+a_{i j}^{(i)}=a_{i j}^{(1)}=a_{i j},
$$

while for $i>j$

$$
(\boldsymbol{L} \boldsymbol{U})_{i j}=\sum_{k=1}^{j-1} l_{i k}^{(k)} a_{k j}^{(k)}+l_{i j} a_{j j}^{(j)}=\sum_{k=1}^{j-1}\left(a_{i j}^{(k)}-a_{i j}^{(k+1)}\right)+a_{i j}^{(j)}=a_{i j} .
$$ $\square$

Note that this Theorem holds even if $\boldsymbol{A}$ is singular. Since $\boldsymbol{L}$ is nonsingular the matrix $\boldsymbol{U}$ is then singular, and we must have $a_{n n}^{(n)}=0$ when $\boldsymbol{A}$ is singular.

### 3.3 Banded Triangular Systems

Once we know an LU factorization of $\boldsymbol{A}$ the system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ is solved in two steps. Since $\boldsymbol{L} \boldsymbol{U} \boldsymbol{x}=\boldsymbol{b}$ we have $\boldsymbol{L} \boldsymbol{y}=\boldsymbol{b}$, where $\boldsymbol{y}:=\boldsymbol{U} \boldsymbol{x}$. We first solve $\boldsymbol{L} \boldsymbol{y}=\boldsymbol{b}$, for $\boldsymbol{y}$ and then $\boldsymbol{U} \boldsymbol{x}=\boldsymbol{y}$ for $\boldsymbol{x}$.

### 3.3.1 Algorithms for Triangular Systems

A nonsingular triangular linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ is easy to solve. By Lemma $2.5 \boldsymbol{A}$ has nonzero diagonal elements. Consider first the lower triangular case. For $n=3$ the system is

$$
\left[\begin{array}{ccc}
a_{11} & 0 & 0 \\
a_{21} & a_{22} & 0 \\
a_{31} & a_{32} & a_{33}
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right]=\left[\begin{array}{l}
b_{1} \\
b_{2} \\
b_{3}
\end{array}\right] .
$$

From the first equation we find $x_{1}=b_{1} / a_{11}$. Solving the second equation for $x_{2}$ we obtain $x_{2}=\left(b_{2}-a_{21} x_{1}\right) / a_{22}$. Finally the third equation gives $x_{3}=\left(b_{3}-a_{31} x_{1}-\right.$ $\left.a_{32} x_{2}\right) / a_{33}$. This process is known as forward substitution. In general

$$
x_{k}=\left(b_{k}-\sum_{j=1}^{k-1} a_{k, j} x_{j}\right) / a_{k k}, \quad k=1,2, \ldots, n .
$$

When $\boldsymbol{A}$ is a lower triangular band matrix the number of arithmetic operations necessary to find $\boldsymbol{x}$ can be reduced. Suppose $\boldsymbol{A}$ is a lower triangular $d$-banded, so that $a_{k, j}=0$ for $j \notin\left\{l_{k}, l_{k}+1, \ldots, k\right.$ for $k=1,2, \ldots, n$, and where $l_{k}:=\max (1, k-d)$, see Fig. 3.2. For a lower triangular $d$-band matrix the calculation in (3.7) can be simplified as follows

$$
x_{k}=\left(b_{k}-\sum_{j=l_{k}}^{k-1} a_{k, j} x_{j}\right) / a_{k k}, \quad k=1,2, \ldots, n .
$$

Note that (3.8) reduces to (3.7) if $d=n$. Letting $A\left(k, l_{k}:(k-1)\right) * x\left(l_{k}:(k-1)\right)$ denote the sum $\sum_{j=l_{k}}^{k-1} a_{k j} x_{j}$ we arrive at the following algorithm, where the initial

Fig. 3.2 Lower triangular $5 \times 5$ band matrices: $d=1$ (left) and $d=2$ right

$$
\left[\begin{array}{ccccc}
a_{11} & 0 & 0 & 0 & 0 \\
a_{21} & a_{22} & 0 & 0 & 0 \\
0 & a_{32} & a_{33} & 0 & 0 \\
0 & 0 & a_{43} & a_{44} & 0 \\
0 & 0 & 0 & a_{54} & a_{55}
\end{array}\right], \quad\left[\begin{array}{ccccc}
a_{11} & 0 & 0 & 0 & 0 \\
a_{21} & a_{22} & 0 & 0 & 0 \\
a_{31} & a_{32} & a_{33} & 0 & 0 \\
0 & a_{42} & a_{43} & a_{44} & 0 \\
0 & 0 & a_{53} & a_{54} & a_{55}
\end{array}\right]
$$

"r" in the name signals that this algorithm is row oriented. The algorithm takes a nonsingular lower triangular $d$-banded matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$, and $\boldsymbol{b} \in \mathbb{C}^{n}$, as input, and returns an $\boldsymbol{x} \in \mathbb{C}^{n}$ so that $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. For each $k$ we take the inner product of a part of a row with the already computed unknowns.

```
function x=rforwardsolve (A,b,d)
% x=rforwardsolve(A,b,d)
n=length(b); x=b;
x (1) =b(1) /A(1,1);
for k=2:n
    lk=max(1,k-d);
    x(k)=(b(k)-A(k,lk:(k-1))*x(lk:(k-1)))/A(k,k);
end
```

Listing 3.1 rforwardsolve

A system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A}$ is upper triangular must be solved by back substitution or 'bottom-up'. We first find $x_{n}$ from the last equation and then move upwards for the remaining unknowns. For an upper triangular $d$-banded matrix this leads to the following algorithm, which takes a nonsingular upper triangular $d$ banded matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}, \boldsymbol{b} \in \mathbb{C}^{n}$ and $d$, as input, and returns an $\boldsymbol{x} \in \mathbb{C}^{n}$ so that $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$.

```
function x=rbacksolve (A,b,d)
% x=rbacksolve(A,b,d)
n=length(b); x=b;
x (n) =b(n) /A(n,n) ;
for k=n-1:-1:1
    uk=min(n,k+d);
    x (k) = (b(k) -A(k, (k+1) :uk) *x((k+1) :uk)) /A(k,k);
end
```

Listing 3.2 rbacksolve

Example 3.3 (Column Oriented Forwardsolve) In this example we develop a column oriented vectorized version of forward substitution. For a backward substitution see Exercise 3.1. Consider the system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is lower triangular. Suppose after $k-1$ steps of the algorithm we have a reduced system in the form

$$
\left[\begin{array}{cccc}
a_{k, k} & 0 & \cdots & 0 \\
a_{k+1, k} & a_{k+1, k+1} & \cdots & 0 \\
\vdots & & \ddots & \vdots \\
a_{n, k} & & \cdots & a_{n \times n}
\end{array}\right]\left[\begin{array}{c}
x_{k} \\
x_{k+1} \\
\vdots \\
x_{n}
\end{array}\right]=\left[\begin{array}{c}
b_{k} \\
b_{k+1} \\
\vdots \\
b_{n}
\end{array}\right] .
$$

This system is of order $n-k+1$. The unknowns are $x_{k}, \ldots, x_{n}$.

We see that $x_{k}=b_{k} / a_{k, k}$ and eliminating $x_{k}$ from the remaining equations we obtain a system of order $n-k$ with unknowns $x_{k+1}, \ldots, x_{n}$

$$
\left[\begin{array}{cccc}
a_{k+1, k+1} & 0 & \cdots & 0 \\
a_{k+2, k+1} & a_{k+2, k+2} & \cdots & 0 \\
\vdots & & \ddots & \vdots \\
a_{n, k+1} & & \cdots & a_{n, n}
\end{array}\right]\left[\begin{array}{c}
x_{k+1} \\
\vdots \\
x_{n}
\end{array}\right]=\left[\begin{array}{c}
b_{k+1} \\
\vdots \\
b_{n}
\end{array}\right]-x_{k}\left[\begin{array}{c}
a_{k+1, k} \\
\vdots \\
a_{n, k}
\end{array}\right] .
$$

Thus at the $k$ th step, $k=1,2, \ldots n$ we set $x_{k}=b_{k} / A(k, k)$ and update $b$ as follows:

$$
b((k+1): n)=b((k+1): n)-x(k) * A((k+1): n, k) .
$$

This leads to the following algorithm for column oriented forward solve, which takes a nonsingular lower triangular $d$-banded matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}, \boldsymbol{b} \in \mathbb{C}^{n}$, and $d$ as input, and returns an $\boldsymbol{x} \in \mathbb{C}^{n}$ so that $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$.

```
function x=cforwardsolve(A,b,d)
%x=cforwardsolve(A,b,d)
x=b; n=length(b);
for k=1:n-1
    x (k) = b (k) /A (k,k) ; uk=min (n,k+d) ;
    b((k+1):uk)=b((k+1):uk)-A((k+1):uk,k)*x(k);
end
x (n) = b (n) /A(n,n) ;
end
```


### 3.3.2 Counting Operations

It is useful to have a number which indicates the amount of work an algorithm requires. In this book we measure this by estimating the total number of (complex) arithmetic operations. We count both additions, subtractions, multiplications and divisions, but not work on indices. As an example we show that the LU factorization of a full matrix of order $n$ using Gaussian elimination requires exactly

$$
N_{L U}:=\frac{2}{3} n^{3}-\frac{1}{2} n^{2}-\frac{1}{6} n
$$
Listing 3.3 cforwardsolve

operations. Let $M, D, A, S$ be the number of (complex) multiplications, divisions, additions, and subtractions. In (3.2) the multiplications and subtractions occur in the calculation of $a_{i j}^{k+1}=a_{i j}^{(k)}-l_{i k}^{(k)} a_{k j}^{(k)}$ which is carried out $(n-k)^{2}$ times. Moreover,
each calculation involves one subtraction and one multiplication. Thus we find $M+$ $S=2 \sum_{k=1}^{n-1}(n-k)^{2}=2 \sum_{m=1}^{n-1} m^{2}=\frac{2}{3} n(n-1)\left(n-\frac{1}{2}\right)$. For each $k$ there are $n-k$ divisions giving a sum of $\sum_{k=1}^{n-1}(n-k)=\frac{1}{2} n(n-1)$. Since there are no additions we obtain the total

$$
M+D+A+S=\frac{2}{3} n(n-1)\left(n-\frac{1}{2}\right)+\frac{1}{2} n(n-1)=N_{L U}
$$

given by (3.9).
We are only interested in $N_{L U}$ when $n$ is large and for such $n$ the term $\frac{2}{3} n^{3}$ dominates. We therefore regularly ignore lower order terms and use number of operations both for the exact count and for the highest order term. We also say more loosely that the number of operations is $O\left(n^{3}\right)$. We will use the number of operations counted in one of these ways as a measure of the complexity of an algorithm and say that the complexity of LU factorization of a full matrix is $O\left(n^{3}\right)$ or more precisely $\frac{2}{3} n^{3}$.

We will compare the number of arithmetic operations of many algorithms with the number of arithmetic operations of Gaussian elimination and define for $n \in \mathbb{N}$ the number $G_{n}$ as follows:
Definition $3.2\left(G_{n}:=\frac{2}{3} n^{3}\right)$ We define $G_{n}:=\frac{2}{3} n^{3}$.
There is a quick way to arrive at the leading term $2 n^{3} / 3$. We only consider the operations contributing to this term. In (3.2) the leading term comes from the inner loop contributing to $M+S$. Then we replace sums by integrals letting the summation indices be continuous variables and adjust limits of integration in an insightful way to simplify the calculation. Thus,

$$
M+S=2 \sum_{k=1}^{n-1}(n-k)^{2} \approx 2 \int_{1}^{n-1}(n-k)^{2} d k \approx 2 \int_{0}^{n}(n-k)^{2} d k=\frac{2}{3} n^{3}
$$

and this is the correct leading term.
Consider next $N_{S}$, the number of forward plus backward substitutions. By (3.7) we obtain

$$
N_{S}=2 \sum_{k=1}^{n}(2 k-1) \approx 2 \int_{1}^{n}(2 k-1) d k \approx 4 \int_{0}^{n} k d k=2 n^{2}
$$

The last integral actually give the exact value for the sum in this case (cf. (3.26)).
We see that LU factorization is an $O\left(n^{3}\right)$ process while solving a triangular system requires $O\left(n^{2}\right)$ arithmetic operations. Thus, if $n=10^{6}$ and one arithmetic operation requires $c=10^{-14}$ seconds of computing time then $c n^{3}=$ $10^{4}$ seconds $\approx 3$ hours and $c n^{2}=0.01$ second, giving dramatic differences in computing time.

### 3.4 The PLU Factorization

Theorem 3.1 shows that Gaussian elimination without row interchanges can fail on a nonsingular system. A simple example is $\left[\begin{array}{ll}0 & 1 \\ 1 & 1\end{array}\right]\left[\begin{array}{l}x_{1} \\ x_{2}\end{array}\right]=\left[\begin{array}{l}1 \\ 1\end{array}\right]$. We show here that any nonsingular linear system can be solved by Gaussian elimination if we incorporate row interchanges.

### 3.4.1 Pivoting

Interchanging two rows (and/or two columns) during Gaussian elimination is known as pivoting. The element which is moved to the diagonal position $(k, k)$ is called the pivot element or pivot for short, and the row containing the pivot is called the pivot row. Gaussian elimination with row pivoting can be described as follows.

1. Choose $r_{k} \geq k$ so that $a_{r_{k}, k}^{(k)} \neq 0$.
2. Interchange rows $r_{k}$ and $k$ of $\boldsymbol{A}^{(k)}$.
3. Eliminate by computing $l_{i k}^{(k)}$ and $a_{i j}^{(k+1)}$ using (3.2).

To show that Gaussian elimination can always be carried to completion by using suitable row interchanges suppose by induction on $k$ that $\boldsymbol{A}^{(k)}$ is nonsingular. Since $\boldsymbol{A}^{(1)}=\boldsymbol{A}$ this holds for $k=1$. By Lemma 2.4 the lower right diagonal block in $\boldsymbol{A}^{(k)}$ is nonsingular. But then at least one element in the first column of that block must be nonzero and it follows that $r_{k}$ exists so that $a_{r_{k}, k}^{(k)} \neq 0$. But then $\boldsymbol{A}^{(k+1)}$ is nonsingular since it is computed from $\boldsymbol{A}^{(k)}$ using row operations preserving the nonsingularity. We conclude that $\boldsymbol{A}^{(k)}$ is nonsingular for $k=1, \ldots, n$.

### 3.4.2 Permutation Matrices

Row interchanges can be described in terms of permutation matrices.
Definition 3.3 A permutation matrix is a matrix of the form

$$
\boldsymbol{P}=\boldsymbol{I}(:, \boldsymbol{p})=\left[\boldsymbol{e}_{i_{1}}, \boldsymbol{e}_{i_{2}}, \ldots, \boldsymbol{e}_{i_{n}}\right] \in \mathbb{R}^{n \times n},
$$

where $\boldsymbol{e}_{i_{1}}, \ldots, \boldsymbol{e}_{i_{n}}$ is a permutation of the unit vectors $\boldsymbol{e}_{1}, \ldots, \boldsymbol{e}_{n} \in \mathbb{R}^{n}$.
Every permutation $\boldsymbol{p}=\left[i_{1}, \ldots, i_{n}\right]^{T}$ of the integers $1,2, \ldots, n$ gives rise to a permutation matrix and vice versa. Post-multiplying a matrix $\boldsymbol{A}$ by a permutation matrix results in a permutation of the columns, while pre-multiplying by a permutation matrix gives a permutation of the rows. In symbols

$$
\boldsymbol{A} \boldsymbol{P}=\boldsymbol{A}(:, \boldsymbol{p}), \quad \boldsymbol{P}^{T} \boldsymbol{A}=\boldsymbol{A}(\boldsymbol{p},:) .
$$

Indeed, $\boldsymbol{A} \boldsymbol{P}=\left(\boldsymbol{A} \boldsymbol{e}_{i_{1}}, \ldots, \boldsymbol{A} \boldsymbol{e}_{i_{n}}\right)=\boldsymbol{A}(:, \boldsymbol{p})$ and $\boldsymbol{P}^{T} \boldsymbol{A}=\left(\boldsymbol{A}^{T} \boldsymbol{P}\right)^{T}=\left(\boldsymbol{A}^{T}(\right.$ : $, \boldsymbol{p}))^{T}=\boldsymbol{A}(\boldsymbol{p},:)$.

Since $\boldsymbol{P}^{T} \boldsymbol{P}=\boldsymbol{I}$ the inverse of $\boldsymbol{P}$ is equal to its transpose, $\boldsymbol{P}^{-1}=\boldsymbol{P}^{T}$ and $\boldsymbol{P} \boldsymbol{P}^{T}=\boldsymbol{I}$ as well. We will use a particularly simple permutation matrix.

Definition 3.4 We define a $(j, k)$-Interchange matrix $\boldsymbol{I}_{j k}$ by interchanging column $j$ and $k$ of the identity matrix.

Since $\boldsymbol{I}_{j k}=\boldsymbol{I}_{k j}$, and we obtain the identity by applying $\boldsymbol{I}_{j k}$ twice, we see that $\boldsymbol{I}_{j k}^{2}=\boldsymbol{I}$ and an interchange matrix is symmetric and equal to its own inverse. Premultiplying a matrix by an interchange matrix interchanges two rows of the matrix, while post-multiplication interchanges two columns.

We can keep track of the row interchanges using pivot vectors $\boldsymbol{p}_{k}$. We define

$$
\boldsymbol{p}:=\boldsymbol{p}_{n}, \text { where } \boldsymbol{p}_{1}:=[1,2, \ldots, n]^{T}, \text { and } \boldsymbol{p}_{k+1}:=\boldsymbol{I}_{r_{k}, k} \boldsymbol{p}_{k} \text { for } k=1, \ldots, n-1 .
$$

We obtain $\boldsymbol{p}_{k+1}$ from $\boldsymbol{p}_{k}$ by interchanging the entries $r_{k}$ and $k$ in $\boldsymbol{p}_{k}$. In particular, since $r_{k} \geq k$, the first $k-1$ components in $\boldsymbol{p}_{k}$ and $\boldsymbol{p}_{k+1}$ are the same.

There is a close relation between the pivot vectors $\boldsymbol{p}_{k}$ and the corresponding interchange matrices $\boldsymbol{P}_{k}:=\boldsymbol{I}_{r_{k}, k}$. Since $\boldsymbol{P}_{k} \boldsymbol{I}\left(\boldsymbol{p}_{k},:\right)=\boldsymbol{I}\left(\boldsymbol{P}_{k} \boldsymbol{p}_{k},:\right)=\boldsymbol{I}\left(\boldsymbol{p}_{k+1},:\right)$ we obtain

$$
\boldsymbol{P}^{T}=\boldsymbol{P}_{n-1} \cdots \boldsymbol{P}_{1}=\boldsymbol{I}(\boldsymbol{p},:), \quad \boldsymbol{P}=\boldsymbol{P}_{1} \boldsymbol{P}_{2} \cdots \boldsymbol{P}_{n-1}=\boldsymbol{I}(:, \boldsymbol{p}) .
$$

Instead of interchanging the rows of $\boldsymbol{A}$ during elimination we can keep track of the ordering of the rows using the pivot vectors $\boldsymbol{p}_{k}$. Gaussian elimination with row pivoting starting with $a_{i j}^{(1)}=a_{i j}$ can be described as follows:

$$
\begin{aligned}
& \boldsymbol{p}=[1, \ldots, n]^{T} ; \\
& \text { for } k=1: n-1 \\
& \text { choose } r_{k} \geq k \text { so that } a_{p_{r_{k}}, k}^{(k)} \neq 0 \text {. } \\
& \qquad \boldsymbol{p}=I_{r_{k}, k} \boldsymbol{p}
\end{aligned}
$$

$$
\begin{aligned}
& \text { for } i=k+1: n \\
& \qquad \begin{array}{l}
a_{p_{i}, k}^{(k)}=a_{p_{i}, k}^{(k)} / a_{p_{k}, k}^{(k)} \\
\text { for } j=k: n \\
\qquad a_{p_{i}, j}^{(k+1)}=a_{p_{i}, j}^{(k)}-a_{p_{i}, k}^{(k)} a_{p_{k}, j}^{(k)}
\end{array}
\end{aligned}
$$

This leads to the following factorization:
Theorem 3.3 Gaussian elimination with row pivoting on a nonsingular matrix $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$ leads to the factorization $\boldsymbol{A}=\boldsymbol{P} \boldsymbol{L} \boldsymbol{U}$, where $\boldsymbol{P}$ is a permutation matrix, $\boldsymbol{L}$ is lower triangular with ones on the diagonal, and $\boldsymbol{U}$ is upper triangular. More explicitly, $\boldsymbol{P}=\boldsymbol{I}(:, \boldsymbol{p})$, where $\boldsymbol{p}=\boldsymbol{I}_{r_{n-1}, n-1} \cdots \boldsymbol{I}_{r_{1}, 1}[1, \ldots, n]^{T}$, and

$$
\boldsymbol{L}=\left[\begin{array}{ccc}
1 & & \\
a_{p_{2}, 1}^{(1)} & 1 & \\
\vdots & & \ddots \\
a_{p_{n}, 1}^{(1)} & a_{p_{n}, 2}^{(2)} & \cdots 1
\end{array}\right], \quad \boldsymbol{U}=\left[\begin{array}{ccc}
a_{p_{1}, 1}^{(1)} & \cdots & a_{p_{1}, n}^{(1)} \\
& \ddots & \vdots \\
& & a_{p_{n}, n}^{(n)}
\end{array}\right] .
$$

Proof The proof is analogous to the proof for LU factorization without pivoting. From (3.13) we have for all $i, j$

$$
a_{p_{i}, k}^{(k)} a_{p_{k}, j}^{(k)}=a_{p_{i}, j}^{(k)}-a_{p_{i}, j}^{(k+1)} \text { for } k<\min (i, j), \text { and } a_{p_{i}, j}^{(k)} a_{p_{j}, j}^{(j)}=a_{p_{i}, j}^{(j)} \text { for } i>j .
$$

Thus for $i \leq j$ we find

$$
\begin{aligned}
(\boldsymbol{L} \boldsymbol{U})_{i j} & =\sum_{k=1}^{n} l_{i, k} u_{k j}=\sum_{k=1}^{i-1} a_{p_{i}, k}^{(k)} a_{p_{k}, j}^{(k)}+a_{p_{i}, j}^{(i)} \\
& =\sum_{k=1}^{i-1}\left(a_{p_{i}, j}^{(k)}-a_{p_{i}, j}^{(k+1)}\right)+a_{p_{i}, j}^{(i)}=a_{p_{i}, j}^{(1)}=a_{p_{i}, j}=\left(\boldsymbol{P}^{T} \boldsymbol{A}\right)_{i j},
\end{aligned}
$$

while for $i>j$

$$
\begin{aligned}
(\boldsymbol{L} \boldsymbol{U})_{i j} & =\sum_{k=1}^{n} l_{i k}^{(k)} u_{k j}=\sum_{k=1}^{j-1} a_{p_{i}, k}^{(k)} a_{p_{k}, j}^{(k)}+a_{p_{i}, j}^{(k)} a_{p_{j}, j}^{(j)} \\
& =\sum_{k=1}^{j-1}\left(a_{p_{i}, j}^{(k)}-a_{p_{i}, j}^{(k+1)}\right)+a_{p_{i}, j}^{(j)}=a_{p_{i}, j}^{(1)}=a_{p_{i}, j}=\left(\boldsymbol{P}^{T} \boldsymbol{A}\right)_{i j} .
\end{aligned}
$$ $\square$

The PLU factorization can also be written $\boldsymbol{P}^{T} \boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$. This shows that for a nonsingular matrix there is a permutation of the rows of $\boldsymbol{A}$ so that the permuted matrix has an LU factorization.

### 3.4.3 Pivot Strategies

The choice of pivot element in (3.13) is not unique. In partial pivoting we select the largest element

$$
\left|a_{r_{k}, k}^{(k)}\right|:=\max \left\{\left|a_{i, k}^{(k)}\right|: k \leq i \leq n\right\}
$$

with $r_{k}$ the smallest such index in case of a tie. The following example illustrating that small pivots should be avoided.

Example 3.4 Applying Gaussian elimination without row interchanges to the linear system

$$
\begin{array}{r}
10^{-4} x_{1}+2 x_{2}=4 \\
x_{1}+x_{2}=3
\end{array}
$$

we obtain the upper triangular system

$$
\begin{aligned}
10^{-4} x_{1}+2 x_{2} & =4 \\
\left(1-2 \times 10^{4}\right) x_{2} & =3-4 \times 10^{4}
\end{aligned}
$$

The exact solution is

$$
x_{2}=\frac{-39997}{-19999} \approx 2, \quad x_{1}=\frac{4-2 x_{2}}{10^{-4}}=\frac{20000}{19999} \approx 1 .
$$

Suppose we round the result of each arithmetic operation to three digits. The solutions $\mathrm{fl}\left(x_{1}\right)$ and $\mathrm{fl}\left(x_{2}\right)$ computed in this way is

$$
\mathrm{fl}\left(x_{2}\right)=2, \quad \mathrm{fl}\left(x_{1}\right)=0 .
$$

The computed value 0 of $x_{1}$ is completely wrong. Suppose instead we apply Gaussian elimination to the same system, but where we have interchanged the equations. The system is

$$
\begin{aligned}
x_{1}+x_{2} & =3 \\
10^{-4} x_{1}+2 x_{2} & =4
\end{aligned}
$$

and we obtain the upper triangular system

$$
\begin{aligned}
x_{1}+x_{2} & =3 \\
\left(2-10^{-4}\right) x_{2} & =4-3 \times 10^{-4}
\end{aligned}
$$

Now the solution is computed as follows

$$
x_{2}=\frac{3.9997}{1.9999} \approx 2, \quad x_{1}=3-x_{2} \approx 1 .
$$

In this case rounding each calculation to three digits produces $\mathrm{fl}\left(x_{1}\right)=1$ and $\mathrm{fl}\left(x_{2}\right)=2$ which is quite satisfactory since it is the exact solution rounded to three digits.

Related to partial pivoting is scaled partial pivoting. Here $r_{k}$ is the smallest index such that

$$
\frac{\left|a_{r_{k}, k}^{(k)}\right|}{s_{k}}:=\max \left\{\frac{\left|a_{i, k}^{(k)}\right|}{s_{k}}: k \leq i \leq n\right\}, \quad s_{k}:=\max _{1 \leq j \leq n}\left|a_{k j}\right| .
$$

This can sometimes give more accurate results if the coefficient matrix have coefficients of wildly different sizes. Note that the scaling factors $s_{k}$ are computed using the initial matrix.

It also is possible to interchange both rows and columns. The choice

$$
a_{r_{k}, s_{k}}^{(k)}:=\max \left\{\left|a_{i, j}^{(k)}\right|: k \leq i, j \leq n\right\}
$$

with $r_{k}, s_{k}$ the smallest such indices in case of a tie, is known as complete pivoting. Complete pivoting is known to be more numerically stable than partial pivoting, but requires a lot of search and is seldom used in practice.

### 3.5 The LU and LDU Factorizations

Gaussian elimination without row interchanges is one way of computing an LU factorization of a matrix. There are other ways that can be advantageous for certain kind of problems. Here we consider the general theory of LU factorizations. Recall that $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$ is an $\mathbf{L U}$ factorization of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ if $\boldsymbol{L} \in \mathbb{C}^{n \times n}$ is lower triangular and $\boldsymbol{U} \in \mathbb{C}^{n \times n}$ is upper triangular , i.e.,

$$
\boldsymbol{L}=\left[\begin{array}{ccc}
l_{1,1} & \cdots & 0 \\
\vdots & \ddots & \vdots \\
l_{n, 1} & \cdots & l_{n, n}
\end{array}\right], \quad \boldsymbol{U}=\left[\begin{array}{ccc}
u_{1,1} & \cdots & u_{1, n} \\
\vdots & \ddots & \vdots \\
0 & \cdots & u_{n, n}
\end{array}\right] .
$$

To find an LU factorization there is one equation for each of the $n^{2}$ elements in $\boldsymbol{A}$, and $\boldsymbol{L}$ and $\boldsymbol{U}$ contain a total of $n^{2}+n$ unknown elements. There are several ways to restrict the number of unknowns to $n^{2}$.

L1U: $\quad l_{i i}=1$ all $i$,
LU1: $\quad u_{i i}=1$ all $i$,
LDU: $\quad \boldsymbol{A}=\boldsymbol{L} \boldsymbol{D} \boldsymbol{U}, l_{i i}=u_{i i}=1$ all $i, \boldsymbol{D}=\operatorname{diag}\left(d_{11}, \ldots, d_{n n}\right)$.

### 3.5.1 Existence and Uniqueness

Consider the L1U factorization. Three things can happen. An L1U factorization exists and is unique, it exists, but it is not unique, or it does not exist. The $2 \times 2$ case illustrates this.

Example 3.5 (L1U of $2 \times 2$ Matrix) Let $a, b, c, d \in \mathbb{C}$. An L1U factorization of $\boldsymbol{A}=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$ must satisfy the equations

$$
\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
l_{1} & 1
\end{array}\right]\left[\begin{array}{ll}
u_{1} & u_{2} \\
0 & u_{3}
\end{array}\right]=\left[\begin{array}{cc}
u_{1} & u_{2} \\
u_{1} l_{1} & u_{2} l_{1}+u_{3}
\end{array}\right]
$$

for the unknowns $l_{1}$ in $\boldsymbol{L}$ and $u_{1}, u_{2}, u_{3}$ in $\boldsymbol{U}$. The equations are

$$
u_{1}=a, \quad u_{2}=b, \quad a l_{1}=c, \quad b l_{1}+u_{3}=d .
$$

These equations do not always have a solution. Indeed, the main problem is the equation $a l_{1}=c$. There are essentially three cases

1. $a \neq 0$ : The matrix has a unique L1U factorization.
2. $a=c=0$ : The L1U factorization exists, but it is not unique. Any value for $l_{1}$ can be used.
3. $a=0, c \neq 0$ : No L1U factorization exists.

Consider the four matrices

$$
\boldsymbol{A}_{1}:=\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right], \quad \boldsymbol{A}_{2}:=\left[\begin{array}{ll}
0 & 1 \\
1 & 1
\end{array}\right], \quad \boldsymbol{A}_{3}:=\left[\begin{array}{ll}
0 & 1 \\
0 & 2
\end{array}\right], \quad \boldsymbol{A}_{4}:=\left[\begin{array}{ll}
1 & 1 \\
1 & 1
\end{array}\right] .
$$

From the previous discussion it follows that $\boldsymbol{A}_{1}$ has a unique L1U factorization, $\boldsymbol{A}_{2}$ has no L1U factorization, $\boldsymbol{A}_{3}$ has an L1U factorization but it is not unique, and $\boldsymbol{A}_{4}$ has a unique L1U factorization even if it is singular.

In preparation for the main theorem about LU factorization we prove a simple lemma. Recall that

$$
\boldsymbol{A}_{[k]}:=\left[\begin{array}{ccc}
a_{11} & \cdots & a_{k 1} \\
\vdots & & \vdots \\
a_{k 1} & \cdots & a_{k k}
\end{array}\right]
$$

is called a leading principal submatrix of $\boldsymbol{A}$.

Lemma 3.1 (L1U of Leading Principal Submatrices) Suppose $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$ is an L1U factorization of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. For $k=1, \ldots, n$ let $\boldsymbol{A}_{[k]}, \boldsymbol{L}_{[k]}, \boldsymbol{U}_{[k]}$ be the leading principal submatrices of $\boldsymbol{A}, \boldsymbol{L}, \boldsymbol{U}$, respectively. Then $\boldsymbol{A}_{[k]}=\boldsymbol{L}_{[k]} \boldsymbol{U}_{[k]}$ is an L1U factorization of $\boldsymbol{A}_{[k]}$ for $k=1, \ldots, n$.

Proof For $k=1, \ldots, n-1$ we partition $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$ as follows:

$$
\left[\begin{array}{cc}
\boldsymbol{A}_{[k]} & \boldsymbol{B}_{k} \\
\boldsymbol{C}_{k} & \boldsymbol{F}_{k}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{L}_{[k]} & \mathbf{0} \\
\boldsymbol{M}_{k} & \boldsymbol{N}_{k}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{U}_{[k]} & \boldsymbol{S}_{k} \\
\mathbf{0} & \boldsymbol{T}_{k}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{L}_{[k]} \boldsymbol{U}_{[k]} & \boldsymbol{L}_{[k]} \boldsymbol{S}_{k} \\
\boldsymbol{M}_{k} \boldsymbol{U}_{[k]} & \boldsymbol{M}_{k} \boldsymbol{S}_{k}+\boldsymbol{N}_{k} \boldsymbol{T}_{k}
\end{array}\right],
$$

where $\boldsymbol{F}_{k}, \boldsymbol{N}_{k}, \boldsymbol{T}_{k} \in \mathbb{C}^{n-k, n-k}$. Comparing blocks we find $\boldsymbol{A}_{[k]}=\boldsymbol{L}_{[k]} \boldsymbol{U}_{[k]}$. Since $\boldsymbol{L}_{[k]}$ is unit lower triangular and $\boldsymbol{U}_{[k]}$ is upper triangular this is an L1U factorization of $\boldsymbol{A}_{[k]}$. $\square$

The following theorem gives a necessary and sufficient condition for existence of a unique LU factorization. The conditions are the same for the three factorizations L1U, LU1 and LDU.

Theorem 3.4 (LU Theorem) A square matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has a unique L1U (LU1, LDU) factorization if and only if the leading principal submatrices $\boldsymbol{A}_{[k]}$ of $\boldsymbol{A}$ are nonsingular for $k=1, \ldots, n-1$.

Proof Suppose $\boldsymbol{A}_{[k]}$ is nonsingular for $k=1, \ldots, n-1$. Under these conditions Gaussian elimination gives an L1U factorization (cf. Theorem 3.2). We give another proof here that in addition to showing uniqueness also gives alternative ways to compute the L1U factorization. The proofs for the LU1 and LDU factorizations are similar and left as exercises.

We use induction on $n$ to show that $\boldsymbol{A}$ has a unique L1U factorization. The result is clearly true for $n=1$, since the unique L1U factorization of a $1 \times 1$ matrix is $\left[a_{11}\right]=[1]\left[a_{11}\right]$. Suppose that $\boldsymbol{A}_{[n-1]}$ has a unique L1U factorization $\boldsymbol{A}_{[n-1]}=$ $\boldsymbol{L}_{n-1} \boldsymbol{U}_{n-1}$, and that $\boldsymbol{A}_{[1]}, \ldots, \boldsymbol{A}_{[n-1]}$ are nonsingular. By block multiplication

$$
\boldsymbol{A}=\left[\begin{array}{cc}
\boldsymbol{A}_{[n-1]} & \boldsymbol{c}_{n} \\
\boldsymbol{r}_{n}^{T} & a_{n n}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{L}_{n-1} & \mathbf{0} \\
\boldsymbol{l}_{n}^{T} & 1
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{U}_{n-1} & \boldsymbol{u}_{n} \\
0 & u_{n n}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{L}_{n-1} \boldsymbol{U}_{n-1} & \boldsymbol{L}_{n-1} \boldsymbol{u}_{n} \\
\boldsymbol{l}_{n}^{T} \boldsymbol{U}_{n-1} & \boldsymbol{l}_{n}^{T} \boldsymbol{u}_{n}+u_{n n}
\end{array}\right],
$$

if and only if $\boldsymbol{A}_{[n-1]}=\boldsymbol{L}_{n-1} \boldsymbol{U}_{n-1}$ and $\boldsymbol{l}_{n}, \boldsymbol{u}_{n} \in \mathbb{C}^{n-1}$ and $u_{n n} \in \mathbb{C}$ are determined from

$$
\boldsymbol{U}_{n-1}^{T} \boldsymbol{l}_{n}=\boldsymbol{r}_{n}, \quad \boldsymbol{L}_{n-1} \boldsymbol{u}_{n}=\boldsymbol{c}_{n}, \quad u_{n n}=a_{n n}-\boldsymbol{l}_{n}^{T} \boldsymbol{u}_{n} .
$$

Since $\boldsymbol{A}_{[n-1]}$ is nonsingular it follows that $\boldsymbol{L}_{n-1}$ and $\boldsymbol{U}_{n-1}$ are nonsingular and therefore $\boldsymbol{l}_{n}, \boldsymbol{u}_{n}$, and $u_{n n}$ are uniquely given. Thus (3.17) gives a unique L1U factorization of $\boldsymbol{A}$.

Conversely, suppose $\boldsymbol{A}$ has a unique L1U factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$. By Lemma 3.1 $\boldsymbol{A}_{[k]}=\boldsymbol{L}_{[k]} \boldsymbol{U}_{[k]}$ is an L1U factorization of $\boldsymbol{A}_{[k]}$ for $k=1, \ldots, n-1$. Suppose
$\boldsymbol{A}_{[k]}$ is singular for some $k \leq n-1$. We will show that this leads to a contradiction. Let $k$ be the smallest integer so that $\boldsymbol{A}_{[k]}$ is singular. Since $\boldsymbol{A}_{[j]}$ is nonsingular for $\boldsymbol{j} \leq k-1$ it follows from what we have already shown that $\boldsymbol{A}_{[k]}=\boldsymbol{L}_{[k]} \boldsymbol{U}_{[k]}$ is the unique L1U factorization of $\boldsymbol{A}_{[k]}$. The matrix $\boldsymbol{U}_{[k]}$ is singular since $\boldsymbol{A}_{[k]}$ is singular and $\boldsymbol{L}_{[k]}$ is nonsingular. By (3.16) we have $\boldsymbol{U}_{[k]}^{T} \boldsymbol{M}_{k}^{T}=\boldsymbol{C}_{k}^{T}$. This can be written as $n-k$ linear systems for the columns of $\boldsymbol{M}_{k}^{T}$. By assumption $\boldsymbol{M}_{k}^{T}$ exists, but since $\boldsymbol{U}_{[k]}^{T}$ is singular $\boldsymbol{M}_{k}$ is not unique, a contradiction. $\square$

By combining the last two equations in (3.18) we obtain with $k=n$

$$
\boldsymbol{U}_{k-1}^{T} \boldsymbol{l}_{k}=\boldsymbol{r}_{k}, \quad\left[\begin{array}{cc}
\boldsymbol{L}_{k-1} & \mathbf{0} \\
\boldsymbol{l}_{k}^{T} & 1
\end{array}\right]\left[\begin{array}{c}
\boldsymbol{u}_{k} \\
u_{k k}
\end{array}\right]=\left[\begin{array}{c}
\boldsymbol{c}_{k} \\
a_{k k}
\end{array}\right] .
$$

This can be used in an algorithm to compute the L1U factorization. Moreover, if $\boldsymbol{A}$ is $d$-banded then the first $k-d$ components in $\boldsymbol{r}_{k}$ and $\boldsymbol{c}_{k}$ are zero so both $\boldsymbol{L}$ and $\boldsymbol{U}$ will be $d$-banded. Thus we can use the banded rforwardsolve Algorithm 3.1 to solve the lower triangular system $\boldsymbol{U}_{k-1}^{T} \boldsymbol{l}_{k}=\boldsymbol{r}_{k}$ for the $k$ th row $\boldsymbol{l}_{k}^{T}$ in $\boldsymbol{L}$ and the $k$ th column $\left[\begin{array}{c}\boldsymbol{u}_{k} \\ u_{k}\end{array}\right]$ in $\boldsymbol{U}$ for $k=2, \ldots, n$. This leads to the following algorithm to compute the L1U factorization of a $d$-banded matrix $\boldsymbol{A}$ with $d \geq 1$. The algorithm will fail if the conditions in the LU theorem are not satisfied.

```
function [L,U]=L1U(A,d)
% [L,U]=L1U(A,d)
n=length(A);
L=eye(n,n); U=zeros(n,n);U(1,1)=A(1,1);
for k=2:n
    km=max(1,k-d);
    L (k,km:(k-1) )=rforwardsolve(U(km:(k-1) ...
    ,km:(k-1))',A(k,km:(k-1))',d)';
    U(km:k,k)=rforwardsolve(L(km:k,km:k),A(km:k,k),d);
end
```

Listing 3.4 L1U

For each $k$ we essentially solve a lower triangular linear system of order $d$. Thus the number of arithmetic operation for this algorithm is $O\left(d^{2} n\right)$.

Remark 3.1 (LU of Upper Triangular Matrix) A matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ can have an LU factorization even if $\boldsymbol{A}_{[k]}$ is singular for some $k<n$. By Theorem 4.1 such an LU factorization cannot be unique. An L1U factorization of an upper triangular matrix $\boldsymbol{A}$ is $\boldsymbol{A}=\boldsymbol{I} \boldsymbol{A}$ so it always exists even if $\boldsymbol{A}$ has zeros somewhere on the diagonal. By Lemma 2.5, if some $a_{k k}$ is zero then $\boldsymbol{A}_{[k]}$ is singular and the L1U factorization is not unique. In particular, for the zero matrix any unit lower triangular matrix can be used as $\boldsymbol{L}$ in an L1U factorization.

### 3.6 Block LU Factorization

Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is a block matrix of the form

$$
\boldsymbol{A}:=\left[\begin{array}{ccc}
\boldsymbol{A}_{11} & \cdots & \boldsymbol{A}_{1 m} \\
\vdots & & \vdots \\
\boldsymbol{A}_{m 1} & \cdots & \boldsymbol{A}_{m m}
\end{array}\right],
$$

where each diagonal block $\boldsymbol{A}_{i i}$ is square. We call the factorization

$$
\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}=\left[\begin{array}{cccc}
\boldsymbol{I} & & & \\
\boldsymbol{L}_{21} & \boldsymbol{I} & & \\
\vdots & & \ddots & \\
\boldsymbol{L}_{m 1} & \cdots & \boldsymbol{L}_{m, m-1} & \boldsymbol{I}
\end{array}\right]\left[\begin{array}{cccc}
\boldsymbol{U}_{11} & & \cdots & \boldsymbol{U}_{1 m} \\
& \boldsymbol{U}_{22} & \cdots & \boldsymbol{U}_{2 m} \\
& & \ddots & \vdots \\
& & & \boldsymbol{U}_{m m}
\end{array}\right]
$$

a block $\mathbf{L}$ 1U factorization of $\boldsymbol{A}$. Here the $i$ th diagonal blocks $\boldsymbol{I}$ and $\boldsymbol{U}_{i i}$ in $\boldsymbol{L}$ and $\boldsymbol{U}$ have the same size as $\boldsymbol{A}_{i i}$, the $i$ th diagonal block in $\boldsymbol{A}$. Moreover, the $\boldsymbol{U}_{i i}$ are not necessarily upper triangular. Block LU1 and block LDU factorizations are defined similarly.

The results for element-wise LU factorization carry over to block LU factorization as follows.

Theorem 3.5 (Block LU Theorem) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is a block matrix of the form (3.19). Then $\boldsymbol{A}$ has a unique block $L U$ factorization (3.20) if and only if the leading principal block submatrices

$$
\boldsymbol{A}_{\{k\}}:=\left[\begin{array}{ccc}
\boldsymbol{A}_{11} & \cdots & \boldsymbol{A}_{1 k} \\
\vdots & & \vdots \\
\boldsymbol{A}_{k 1} & \cdots & \boldsymbol{A}_{k k}
\end{array}\right]
$$

are nonsingular for $k=1, \ldots, m-1$.
Proof Suppose $\boldsymbol{A}_{\{k\}}$ is nonsingular for $k=1, \ldots, m-1$. Following the proof in Theorem 3.4 suppose $\boldsymbol{A}_{\{m-1\}}$ has a unique block LU factorization $\boldsymbol{A}_{\{m-1\}}=$ $\boldsymbol{L}_{\{m-1\}} \boldsymbol{U}_{\{m-1\}}$, and that $\boldsymbol{A}_{\{1\}}, \ldots, \boldsymbol{A}_{\{m-1\}}$ are nonsingular. Then $\boldsymbol{L}_{\{m-1\}}$ and $\boldsymbol{U}_{\{m-1\}}$ are nonsingular and

$$
\begin{aligned}
\boldsymbol{A} & =\left[\begin{array}{cc}
\boldsymbol{A}_{\{m-1\}} & \boldsymbol{B} \\
\boldsymbol{C}^{T} & \boldsymbol{A}_{m m}
\end{array}\right] \\
& =\left[\begin{array}{cc}
\boldsymbol{L}_{\{m-1\}} & \mathbf{0} \\
\boldsymbol{C}^{T} \boldsymbol{U}_{\{m-1\}}^{-1} & \boldsymbol{I}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{U}_{\{m-1\}} & \boldsymbol{L}_{\{m-1\}}^{-1} \boldsymbol{B} \\
0 & \boldsymbol{A}_{m m}-\boldsymbol{C}^{T} \boldsymbol{U}_{\{m-1\}}^{-1} \boldsymbol{L}_{\{m-1\}}^{-1} \boldsymbol{B}
\end{array}\right],
\end{aligned}
$$

is a block LU factorization of $\boldsymbol{A}$. It is unique by derivation. Conversely, suppose $\boldsymbol{A}$ has a unique block LU factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$. Then as in Lemma 3.1 it is easily seen that $\boldsymbol{A}_{\{k\}}=\boldsymbol{L}_{\{k\}} \boldsymbol{U}_{\{k\}}$ is the unique block LU factorization of $\boldsymbol{A}_{[k]}$ for $k=1, \ldots, m$. The rest of the proof is similar to the proof of Theorem 3.4. $\square$

Remark 3.2 (Comparing LU and Block LU) The number of arithmetic operations for the block LU factorization is the same as for the ordinary LU factorization. An advantage of the block method is that it combines many of the operations into matrix operations.

Remark 3.3 (A Block $L U$ Is Not an $L U$ ) Note that (3.20) is not an LU factorization of $\boldsymbol{A}$ since the $\boldsymbol{U}_{i i}$ 's are not upper triangular in general. To relate the block LU factorization to the usual LU factorization we assume that each $\boldsymbol{U}_{i i}$ has an LU factorization $\boldsymbol{U}_{i i}=\tilde{\boldsymbol{L}}_{i i} \tilde{\boldsymbol{U}}_{i i}$. Then $\boldsymbol{A}=\hat{\boldsymbol{L}} \hat{\boldsymbol{U}}$, where $\hat{\boldsymbol{L}}:=\boldsymbol{L} \operatorname{diag}\left(\tilde{\boldsymbol{L}}_{i i}\right)$ and $\hat{\boldsymbol{U}}:=\operatorname{diag}\left(\tilde{\boldsymbol{L}}_{i i}^{-1}\right) \boldsymbol{U}$, and this is an ordinary LU factorization of $\boldsymbol{A}$.

### 3.7 Exercises Chap. 3

### 3.7.1 Exercises Sect. 3.3

Exercise 3.1 (Column Oriented Backsolve) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular, upper triangular, $d$-banded, and $\boldsymbol{b} \in \mathbb{C}^{n}$. Justify the following column oriented vectorized algorithm for solving $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$.

```
function x=cbacksolve (A,b,d)
% x=cbacksolve(A,b,d)
x=b; n=length(b);
for k=n:-1:2
    x (k) =b(k) /A(k,k); lk=max(1,k-d) ;
    b(lk:(k-1))=b(lk:(k-1))-A(lk:(k-1),k)*x(k);
end
x(1)=b(1)/A(1,1);
end
```

Exercise 3.2 (Computing the Inverse of a Triangular Matrix) Suppose $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$ is a nonsingular lower triangular matrix. By Lemma 2.5 the inverse $\boldsymbol{B}=$ $\left[\boldsymbol{b}_{1}, \ldots, \boldsymbol{b}_{n}\right]$ is also lower triangular. The $k$ th column $\boldsymbol{b}_{k}$ of $\boldsymbol{B}$ is the solution of the linear systems $\boldsymbol{A} \boldsymbol{b}_{k}=\boldsymbol{e}_{k}$. Show that $b_{k}(k)=1 / a(k, k)$ for $k=1, \ldots, n$, and explain why we can find $\boldsymbol{b}_{k}$ by solving the linear systems

$$
\boldsymbol{A}((k+1): n,(k+1): n) \boldsymbol{b}_{k}((k+1): n)=-\boldsymbol{A}((k+1): n, k) b_{k}(k), \quad k=1, \ldots, n-1 .
$$
Listing 3.5 cbacksolve

Is it possible to store the interesting part of $\boldsymbol{b}_{k}$ in $\boldsymbol{A}$ as soon as it is computed?
When $\boldsymbol{A}$ instead is upper triangular, show also that we can find $\boldsymbol{b}_{k}$ by solving the linear systems

$$
\boldsymbol{A}(1: k, 1: k) \boldsymbol{b}_{k}(1: k)=\boldsymbol{I}(1: k, k), \quad k=n, n-1, \ldots, 1,
$$

for $k=n, n-1, \ldots, 1$.
Exercise 3.3 (Finite Sums of Integers) Use induction on $m$, or some other method, to show that

$$
\begin{aligned}
1+2+\cdots+m & =\frac{1}{2} m(m+1), \\
1^{2}+2^{2}+\cdots+m^{2} & =\frac{1}{3} m\left(m+\frac{1}{2}\right)(m+1), \\
1+3+5+\cdots+2 m-1 & =m^{2}, \\
1 * 2+2 * 3+3 * 4+\cdots+(m-1) m & =\frac{1}{3}(m-1) m(m+1) .
\end{aligned}
$$

Exercise 3.4 (Multiplying Triangular Matrices) Show that the matrix multiplication $\boldsymbol{A} \boldsymbol{B}$ can be done in $\frac{1}{3} n\left(2 n^{2}+1\right) \approx G_{n}$ arithmetic operations when $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is lower triangular and $\boldsymbol{B} \in \mathbb{R}^{n \times n}$ is upper triangular. What about $\boldsymbol{B} \boldsymbol{A}$ ?

### 3.7.2 Exercises Sect. 3.4

Exercise 3.5 (Using PLU for $\boldsymbol{A}^{*}$ ) Suppose we know the PLU factors $\boldsymbol{P}, \boldsymbol{L}, \boldsymbol{U}$ in a PLU factorization $\boldsymbol{A}=\boldsymbol{P} \boldsymbol{L} \boldsymbol{U}$ of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Explain how we can solve the system $\boldsymbol{A}^{*} \boldsymbol{x}=\boldsymbol{b}$ economically.

Exercise 3.6 (Using PLU for Determinant) Suppose we know the PLU factors $\boldsymbol{P}, \boldsymbol{L}, \boldsymbol{U}$ in a PLU factorization $\boldsymbol{A}=\boldsymbol{P} \boldsymbol{L} \boldsymbol{U}$ of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Explain how we can use this to compute the determinant of $\boldsymbol{A}$.

Exercise 3.7 (Using PLU for $\boldsymbol{A}^{-1}$ ) Suppose the factors $\boldsymbol{P}, \boldsymbol{L}, \boldsymbol{U}$ in a PLU factorization of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ are known. Use Exercise 3.4 to show that it takes approximately $2 G_{n}$ arithmetic operations to compute $\boldsymbol{A}^{-1}=\boldsymbol{U}^{-1} \boldsymbol{L}^{-1} \boldsymbol{P}^{T}$. Here we have not counted the final multiplication with $\boldsymbol{P}^{T}$ which amounts to $n$ row interchanges.

Exercise 3.8 (Upper Hessenberg System (Exam Exercise (1994-2)) Gaussian elimination with row pivoting can be written in the following form if for each $k$ we exchange rows $k$ and $k+1$

## Algorithm 1

1. for $k=1,2, \ldots, n-1$
    (a) exchange $a_{k, j}$ and $a_{k+1, j}$ for $j=k, k+1, \ldots, n$
    (b) for $i=k+1, k+2, \ldots, n$
        i. $a_{i, k}=m_{i, k}=a_{i, k} / a_{k, k}$
        ii. $a_{i, j}=a_{i, j}-m_{i, k} a_{k, j}$ for $j=k+1, k+2, \ldots, n$

To solve the set of equations $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ we have the following algorithm:

## Algorithm 2

1. for $k=1,2, \ldots, n-1$
    (a) exchange $b_{k}$ and $b_{k+1}$
    (b) $b_{i}=b_{i}-a_{i, k} b_{k}$ for $i=k+1, k+2, \ldots, n$
2. $x_{n}=b_{n} / a_{n, n}$
3. for $k=n-1, n-2, \ldots, 1$
    (a) sum $=0$
    (b) sum = sum $+a_{k, j} x_{j}$ for $j=k+1, k+2, \ldots, n$
    (c) $x_{k}=\left(b_{k}-\right.$ sum $) / a_{k, k}$

We say that $\boldsymbol{H} \in \mathbb{R}^{n \times n}$ is unreduced upper Hessenberg if it is upper Hessenberg and the subdiagonal elements $h_{i, i-1} \neq 0$ for $i=2, \ldots, n$.

a) Let $\boldsymbol{H} \in \mathbb{R}^{n \times n}$ be unreduced upper Hessenberg. Give an $O\left(n^{2}\right)$ algorithm for solving the linear system $\boldsymbol{H} \boldsymbol{x}=\boldsymbol{b}$ using suitable specializations of Algorithms 1 and 2.
b) Find the number of multiplications/divisions in the algorithm you developed in exercise a). Is division by zero possible?
c) Let $\boldsymbol{U} \in \mathbb{R}^{n \times n}$ be upper triangular and nonsingular. We define
$$
\boldsymbol{C}:=\boldsymbol{U}+\boldsymbol{v} \boldsymbol{e}_{1}^{T},
$$
where $\boldsymbol{v} \in \mathbb{R}^{n}$ and $\boldsymbol{e}_{1}$ is the first unit vector in $\mathbb{R}^{n}$. We also let
$$
\boldsymbol{P}:=\boldsymbol{I}_{1,2} \boldsymbol{I}_{2,3} \cdots \boldsymbol{I}_{n-1, n},
$$
where the $\boldsymbol{I}_{i, j}$ are obtained from the identity matrix by interchanging rows $i$ and $j$. Explain why the matrix $\boldsymbol{E}:=\boldsymbol{C} \boldsymbol{P}$ is unreduced upper Hessenberg.

d) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be nonsingular. We assume that $\boldsymbol{A}$ has a unique L1U factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$. To a given $\boldsymbol{W} \in \mathbb{R}^{n}$ we define a rank one modification of $\boldsymbol{A}$ by
$$
\boldsymbol{B}:=\boldsymbol{A}+\boldsymbol{w} \boldsymbol{e}_{1}^{T} .
$$
Show that $\boldsymbol{B}$ has the factorization $\boldsymbol{B}=\boldsymbol{L} \boldsymbol{H} \boldsymbol{P}^{T}$, where $\boldsymbol{L}$ is unit lower triangular, $\boldsymbol{P}$ is given by (3.29) and $\boldsymbol{H}$ is unreduced upper Hessenberg.
e) Use the results above to sketch an $O\left(n^{2}\right)$ algorithm for solving the linear system $\boldsymbol{B} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{B}$ is given by (3.30). We assume that the matrices $\boldsymbol{L}$ and $\boldsymbol{U}$ in the L1U factorization of $\boldsymbol{A}$ have already been computed.

### 3.7.3 Exercises Sect. 3.5

Exercise 3.9 (\# Operations for Banded Triangular Systems) Show that for $1 \leq$ $d \leq n$ Algorithm 3.4, with $A(k, k)=1$ for $k=1, \ldots, n$ in Algorithm 3.1, requires exactly $N_{L U}(n, d):=\left(2 d^{2}+d\right) n-\left(d^{2}+d\right)(8 d+1) / 6=O\left(d^{2} n\right)$ operations. ${ }^{2}$ In particular, for a full matrix $d=n-1$ and we find $N_{L U}(n, n)=\frac{2}{3} n^{3}-\frac{1}{2} n^{2}-\frac{1}{6} n \approx$ $G_{n}$ in agreement with the exact count (3.9) for Gaussian elimination, while for a tridiagonal matrix $N_{L U}(n, 1)=3 n-3=O(n)$.

Exercise 3.10 (L1U and LU1) Show that the matrix $\boldsymbol{A}_{3}$ in Example 3.5 has no LU1 or LDU factorization. Give an example of a matrix that has an LU1 factorization, but no LDU or L1U factorization.

Exercise 3.11 (LU of Nonsingular Matrix) Show that the following are equivalent for a nonsingular matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$.

1. $\boldsymbol{A}$ has an LDU factorization.
2. $\boldsymbol{A}$ has an L1U factorization.
3. $\boldsymbol{A}$ has an LU1 factorization.

Exercise 3.12 (Row Interchange) Show that $\boldsymbol{A}=\left[\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right]\right.$ has a unique L1U factorization. Note that we have only interchanged rows in Example 3.5.

Exercise 3.13 (LU and Determinant) Suppose $\boldsymbol{A}$ has an L1U factorization $\boldsymbol{A}=$ $\boldsymbol{L} \boldsymbol{U}$. Show that

$$
\operatorname{det}\left(\boldsymbol{A}_{[k]}\right)=u_{11} u_{22} \cdots u_{k k} \text { for } k=1, \ldots, n .
$$

[^7]Exercise 3.14 (Diagonal Elements in U) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ and $\boldsymbol{A}_{[k]}$ is nonsingular for $k=1, \ldots, n-1$. Use Exercise 3.13 to show that the diagonal elements $u_{k k}$ in the L1U factorization are

$$
u_{11}=a_{11}, \quad u_{k k}=\frac{\operatorname{det}\left(\boldsymbol{A}_{[k]}\right)}{\operatorname{det}\left(\boldsymbol{A}_{[k-1]}\right)}, \text { for } k=2, \ldots, n .
$$

Exercise 3.15 (Proof of LDU Theorem) Give a proof of the LU theorem for the LDU case.

Exercise 3.16 (Proof of LU1 Theorem) Give a proof of the LU theorem for the LU1 case.

Exercise 3.17 (Computing the Inverse (Exam Exercise 1978-1)) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be nonsingular and with a unique L1U factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$. We partition $\boldsymbol{L}$ and $\boldsymbol{U}$ as follows

$$
\boldsymbol{L}=\left[\begin{array}{cc}
1 & 0 \\
\boldsymbol{\ell}_{1} & \boldsymbol{L}_{2,2}
\end{array}\right], \quad \boldsymbol{U}=\left[\begin{array}{cc}
u_{1,1} & \boldsymbol{u}_{1}^{T} \\
0 & \boldsymbol{U}_{2,2}
\end{array}\right],
$$

where $\boldsymbol{L}_{2,2}, \boldsymbol{U}_{2,2} \in \mathbb{R}^{(n-1) \times(n-1)}$. Define $\boldsymbol{A}_{2,2}:=\boldsymbol{L}_{2,2} \boldsymbol{U}_{2,2}$ and $\boldsymbol{B}_{2,2}:=\boldsymbol{A}_{2,2}^{-1}$.

a) Show that $\boldsymbol{A}^{-1}=\boldsymbol{B}$, where
$$
\boldsymbol{B}:=\left[\begin{array}{cc}
\left(1+\boldsymbol{u}_{1}^{T}\right. & \left.\boldsymbol{B}_{2,2} \boldsymbol{\ell}_{1}\right) / u_{1,1} \\
-\boldsymbol{u}_{2,2}^{T} & \boldsymbol{B}_{2,2} / u_{1,1} \\
& \boldsymbol{B}_{2,2}
\end{array}\right] .
$$
b) Suppose that the elements $l_{i, j}, i>j$ in $\boldsymbol{L}$ and $u_{i, j}, j \geq i$ in $\boldsymbol{U}$ are stored in $\boldsymbol{A}$ with elements $a_{i, j}$. Write an algorithm that overwrites the elements in $\boldsymbol{A}$ with ones in $\boldsymbol{A}^{-1}$. Only one extra vector $\boldsymbol{s} \in \mathbb{R}^{n}$ should be used.

Exercise 3.18 (Solving $\boldsymbol{T} \boldsymbol{H} \boldsymbol{x}=\boldsymbol{b}$ (Exam Exercise 1981-3)) In this exercise we consider nonsingular matrices $\boldsymbol{T}, \boldsymbol{H}, \boldsymbol{S} \in \mathbb{R}^{n \times n}$ with $\boldsymbol{T}=\left(t_{i j}\right)$ upper triangular, $\boldsymbol{H}=\left(h_{i j}\right)$ upper Hessenberg and $\boldsymbol{S}:=\boldsymbol{T} \boldsymbol{H}$. We assume that $\boldsymbol{H}$ has a unique LU1 factorization $\boldsymbol{H}=\boldsymbol{L} \boldsymbol{U}$ with $\|\boldsymbol{L}\|_{\infty}\|\boldsymbol{U}\|_{\infty} \leq K\|\boldsymbol{H}\|_{\infty}$ for a constant $K$ not too large. In this exercise the number of operations is the highest order term in the number of multiplications and divisions.

a) Give an algorithm which computes $\boldsymbol{S}$ from $\boldsymbol{T}$ and $\boldsymbol{H}$ without using the lower parts $\left(t_{i j}, i>j\right)$ of $\boldsymbol{T}$ and $\left(h_{i j}, i>j+1\right)$ of $\boldsymbol{H}$. In what order should the elements in $\boldsymbol{S}$ be computed if $\boldsymbol{S}$ overwrites the elements in $\boldsymbol{H}$ ? What is the number of operations of the algorithm?
b) Show that $\boldsymbol{L}$ is upper Hessenberg.
c) Give a detailed algorithm for finding the LU1-factorization of $\boldsymbol{H}$ stored in $\boldsymbol{H}$. Determine the number of operations in the algorithm.

d) Given $\boldsymbol{b} \in \mathbb{R}^{n}$ and $\boldsymbol{T}, \boldsymbol{H}$ as before. Suppose $\boldsymbol{S}$ and the LU1-factorization are not computed. We want to find $\boldsymbol{x} \in \mathbb{R}^{n}$ such that $\boldsymbol{S} \boldsymbol{x}=\boldsymbol{b}$. We have the 2 following methods
Method 1:
1. $\boldsymbol{S}=\boldsymbol{T} \boldsymbol{H}$
2. Solve $\boldsymbol{S} \boldsymbol{x}=\boldsymbol{b}$

Method 2:

1. Solve $\boldsymbol{T} \boldsymbol{z}=\boldsymbol{b}$
2. Solve $\boldsymbol{H} \boldsymbol{x}=\boldsymbol{z}$

What method would you prefer? Give reasons for your answer.
Exercise 3.19 (L1U Factorization Update (Exam Exercise 1983-1)) Let $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$ be nonsingular with columns $\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \ldots, \boldsymbol{a}_{n}$. We assume that $\boldsymbol{A}$ has a unique L1U factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$.
For a positive integer $p \leq n$ and $\boldsymbol{b} \in \mathbb{R}^{n}$ we define

$$
\boldsymbol{B}:=\left[\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{p-1}, \boldsymbol{a}_{p+1}, \ldots, \boldsymbol{a}_{n}, \boldsymbol{b}\right] \in \mathbb{R}^{n \times n} .
$$

a) Show that $\boldsymbol{H}:=\boldsymbol{L}^{-1} \boldsymbol{B}$ is upper Hessenberg. We assume that $\boldsymbol{H}$ has a unique L1U factorization. $\boldsymbol{H}=\boldsymbol{L}_{H} \boldsymbol{U}_{H}$.
b) Describe briefly how many multiplications/divisions are required to find the L1U factorization of $\boldsymbol{H}$ ?
c) Suppose we have found the L1U factorization $\boldsymbol{H}:=\boldsymbol{L}_{H} \boldsymbol{U}_{H}$ of $\boldsymbol{H}$. Explain how we can find the L1U factorization of $\boldsymbol{B}$ from $\boldsymbol{L}_{H}$ and $\boldsymbol{U}_{H}$.

Exercise 3.20 (U1L Factorization (Exam Exercise 1990-1)) We say that $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$ has a U1L factorization if $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{L}$ for an upper triangular matrix $\boldsymbol{U} \in \mathbb{R}^{n \times n}$ with ones on the diagonal and a lower triangular $\boldsymbol{L} \in \mathbb{R}^{n \times n}$. A UL and the more common LU factorization are analogous, but normally not the same.

a) Find a U1L factorization of the matrix
$$
A:=\left[\begin{array}{rr}
-3 & -2 \\
4 & 2
\end{array}\right] .
$$
b) Let the columns of $\boldsymbol{P} \in \mathbb{R}^{n \times n}$ be the unit vectors in reverse order, i.e.,
$$
\boldsymbol{P}:=\left[\boldsymbol{e}_{n}, \boldsymbol{e}_{n-1}, \ldots, \boldsymbol{e}_{1}\right] .
$$

Show that $\boldsymbol{P}^{T}=\boldsymbol{P}$ and $\boldsymbol{P}^{2}=\boldsymbol{I}$. What is the connection between the elements in $\boldsymbol{A}$ and $\boldsymbol{P} \boldsymbol{A}$ ?
c) Let $\boldsymbol{B}:=\boldsymbol{P} \boldsymbol{A} \boldsymbol{P}$. Find integers $r, s$, depending on $i, j, n$, such that $b_{i, j}=a_{r, s}$.
d) Make a detailed algorithm which to given $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ determines $\boldsymbol{B}:=\boldsymbol{P} \boldsymbol{A} \boldsymbol{P}$. The elements $b_{i, j}$ in $\boldsymbol{B}$ should be stored in position $i, j$ in $\boldsymbol{A}$. You should not use other matrices than $\boldsymbol{A}$ and a scalar $w \in \mathbb{R}$.
e) Let $\boldsymbol{P} \boldsymbol{A} \boldsymbol{P}=\boldsymbol{M} \boldsymbol{R}$ be an L1U factorization of $\boldsymbol{P} \boldsymbol{A} \boldsymbol{P}$, i.e., $\boldsymbol{M}$ is lower triangular with ones on the diagonal and $\boldsymbol{R}$ is upper triangular. Express the matrices $\boldsymbol{U}$ and $\boldsymbol{L}$ in a U1L factorization of $\boldsymbol{A}$ in terms of $\boldsymbol{M}, \boldsymbol{R}$ and $\boldsymbol{P}$.
f) Give necessary and sufficient conditions for a matrix to have a unique U1L factorization.

### 3.7.4 Exercises Sect. 3.6

Exercise 3.21 (Making Block $\mathbf{L U}$ into $\mathbf{L U}$ ) Show that $\hat{\boldsymbol{L}}$ is unit lower triangular and $\hat{\boldsymbol{U}}$ is upper triangular.

### 3.8 Review Questions

3.8.1 When is a triangular matrix nonsingular?
3.8.2 What is the general condition for Gaussian elimination without row interchanges to be well defined?
3.8.3 What is the content of the LU theorem?
3.8.4 Approximately how many arithmetic operations are needed for
    - the multiplication of two square matrices?
    - The LU factorization of a matrix?
    - the solution of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, when $\boldsymbol{A}$ is triangular?
3.8.5 What is a PLU factorization? When does it exist?
3.8.6 What is complete pivoting?

## Chapter 4 <br> LDL* Factorization and Positive Definite Matrices

In this chapter we consider LU factorizations of Hermitian and positive definite matrices. Recall that a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is Hermitian if $\boldsymbol{A}^{*}=\boldsymbol{A}$, i.e., $a_{j i}=\bar{a}_{i j}$ for all $i, j$. A real Hermitian matrix is symmetric. Since $a_{i i}=\bar{a}_{i i}$ the diagonal elements of a Hermitian matrix must be real.

### 4.1 The LDL* Factorization

There are special versions of the LU factorization for Hermitian and positive definite matrices which takes advantage of the special properties of such matrices. The most important ones are

1. the LDL* factorization which is an LDU factorization with $\boldsymbol{U}=\boldsymbol{L}^{*}$ and $\boldsymbol{D}$ a diagonal matrix with real diagonal elements
2. the LL* factorization which is an LU factorization with $\boldsymbol{U}=\boldsymbol{L}^{*}$ and $l_{i i}>0$ all $i$.

A matrix $\boldsymbol{A}$ having an LDL* factorization must be Hermitian since $\boldsymbol{D}$ is real so that $\boldsymbol{A}^{*}=\left(\boldsymbol{L} \boldsymbol{D} \boldsymbol{L}^{*}\right)^{*}=\boldsymbol{L} \boldsymbol{D}^{*} \boldsymbol{L}^{*}=\boldsymbol{A}$. The LL* factorization is called a Cholesky factorization .

Example 4.1 (LDL* of $2 \times 2$ Hermitian Matrix) Let $a, d \in \mathbb{R}$ and $b \in \mathbb{C}$. An LDL* factorization of a 2 × 2 Hermitian matrix must satisfy the equations

$$
\left[\begin{array}{ll}
a & \bar{b} \\
b & d
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
l_{1} & 1
\end{array}\right]\left[\begin{array}{cc}
d_{1} & 0 \\
0 & d_{2}
\end{array}\right]\left[\begin{array}{cc}
1 & \overline{l_{1}} \\
0 & 1
\end{array}\right]=\left[\begin{array}{cc}
d_{1} & d_{1} \overline{l_{1}} \\
d_{1} l_{1} & d_{1}\left|l_{1}\right|^{2}+d_{2}
\end{array}\right]
$$

for the unknowns $l_{1}$ in $\boldsymbol{L}$ and $d_{1}, d_{2}$ in $\boldsymbol{D}$. They are determined from

$$
d_{1}=a . \quad a l_{1}=b, \quad d_{2}=d-a\left|l_{1}\right|^{2} .
$$

There are essentially three cases

1. $a \neq 0$ : The matrix has a unique LDL* factorization. Note that $d_{1}$ and $d_{2}$ are real.
2. $a=b=0$ : The LDL* factorization exists, but it is not unique. Any value for $l_{1}$ can be used.
3. $a=0, b \neq 0$ : No LDL* factorization exists.

Lemma 3.1 carries over to the Hermitian case.
Lemma 4.1 (LDL* of Leading Principal Sub Matrices) Suppose $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{D L}^{*}$ is an $L D L^{*}$ factorization of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. For $k=1, \ldots, n$ let $\boldsymbol{A}_{[k]}, \boldsymbol{L}_{[k]}$ and $\boldsymbol{D}_{[k]}$ be the leading principal submatrices of $\boldsymbol{A}, \boldsymbol{L}$ and $\boldsymbol{D}$, respectively. Then $\boldsymbol{A}_{[k]}=$ $\boldsymbol{L}_{[k]} \boldsymbol{D}_{[k]} \boldsymbol{L}_{[k]}^{*}$ is an $L D L^{*}$ factorization of $\boldsymbol{A}_{[k]}$ for $k=1, \ldots, n$.

Proof For $k=1, \ldots, n-1$ we partition $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{D} \boldsymbol{L}^{*}$ as follows:

$$
\boldsymbol{A}=\left[\begin{array}{cc}
\boldsymbol{A}_{[k]} & \boldsymbol{B}_{k}^{*} \\
\boldsymbol{B}_{k} & \boldsymbol{F}_{k}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{L}_{[k]} & \mathbf{0} \\
\boldsymbol{M}_{k} & \boldsymbol{N}_{k}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{D}_{[k]} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{E}_{k}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{L}_{[k]}^{*} & \boldsymbol{M}_{k}^{*} \\
\mathbf{0} & \boldsymbol{N}_{k}^{*}
\end{array}\right]=\boldsymbol{L} \boldsymbol{D} \boldsymbol{U},
$$

where $\boldsymbol{F}_{k}, \boldsymbol{N}_{k}, \boldsymbol{E}_{k} \in \mathbb{C}^{n-k, n-k}$. Block multiplication gives $\boldsymbol{A}_{[k]}=\boldsymbol{L}_{[k]} \boldsymbol{D}_{[k]} \boldsymbol{L}_{[k]}^{*}$. Since $\boldsymbol{L}_{[k]}$ is unit lower triangular and $\boldsymbol{D}_{[k]}$ is real and diagonal this is an LDL* factorization of $\boldsymbol{A}_{[k]}$. $\square$

Theorem 4.1 (LDL* Theorem) The matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has a unique LDL* factorization if and only if $\boldsymbol{A}=\boldsymbol{A}^{*}$ and $\boldsymbol{A}_{[k]}$ is nonsingular for $k=1, \ldots, n-1$.

Proof We essentially repeat the proof of Theorem 3.4 incorporating the necessary changes. Suppose $\boldsymbol{A}^{*}=\boldsymbol{A}$ and that $\boldsymbol{A}_{[k]}$ is nonsingular for $k=1, \ldots, n-1$. Note that $\boldsymbol{A}_{[k]}^{*}=\boldsymbol{A}_{[k]}$ for $k=1, \ldots, n$. We use induction on $n$ to show that $\boldsymbol{A}$ has a unique LDL* factorization. The result is clearly true for $n=1$, since the unique LDL* factorization of a 1-by-1 matrix is $\left[a_{11}\right]=[1]\left[a_{11}\right][1]$ and $a_{11}$ is real since $\boldsymbol{A}^{*}=\boldsymbol{A}$. Suppose that $\boldsymbol{A}_{[n-1]}$ has a unique LDL* factorization $\boldsymbol{A}_{[n-1]}=$ $\boldsymbol{L}_{n-1} \boldsymbol{D}_{n-1} \boldsymbol{L}_{n-1}^{*}$, and that $\boldsymbol{A}_{[1]}, \ldots, \boldsymbol{A}_{[n-1]}$ are nonsingular. By definition $\boldsymbol{D}_{n-1}$ is real. Using block multiplication

$$
\begin{aligned}
\boldsymbol{A}=\left[\begin{array}{cc}
\boldsymbol{A}_{[n-1]} & \boldsymbol{a}_{n} \\
\boldsymbol{a}_{n}^{*} & a_{n n}
\end{array}\right] & =\left[\begin{array}{cc}
\boldsymbol{L}_{n-1} & \mathbf{0} \\
\boldsymbol{l}_{n}^{*} & 1
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{D}_{n-1} & \mathbf{0} \\
0 & d_{n n}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{L}_{n-1}^{*} & \boldsymbol{l}_{n} \\
\mathbf{0}^{*} & 1
\end{array}\right] \\
& =\left[\begin{array}{cc}
\boldsymbol{L}_{n-1} \boldsymbol{D}_{n-1} \boldsymbol{L}_{n-1}^{*} & \boldsymbol{L}_{n-1} \boldsymbol{D}_{n-1} \boldsymbol{l}_{n} \\
\boldsymbol{l}_{n}^{*} \boldsymbol{D}_{n-1} \boldsymbol{L}_{n-1}^{*} & \boldsymbol{l}_{n}^{*} \boldsymbol{D}_{n-1} \boldsymbol{l}_{n}+d_{n n}
\end{array}\right]
\end{aligned}
$$

if and only if $\boldsymbol{A}_{[n-1]}=\boldsymbol{L}_{n-1} \boldsymbol{D}_{n-1} \boldsymbol{L}_{n-1}^{*}$, and

$$
\boldsymbol{a}_{n}=\boldsymbol{L}_{n-1} \boldsymbol{D}_{n-1} \boldsymbol{l}_{n}, \quad a_{n n}=\boldsymbol{l}_{n}^{*} \boldsymbol{D}_{n-1} \boldsymbol{l}_{n}+d_{n n} .
$$

Thus we obtain an LDL* factorization of $\boldsymbol{A}$ that is unique since $\boldsymbol{L}_{n-1}$ and $\boldsymbol{D}_{n-1}$ are nonsingular. Also $d_{n n}$ is real since $a_{n n}$ and $\boldsymbol{D}_{n-1}$ are real.

For the converse we use Lemma 4.1 in the same way as Lemma 3.1 was used to prove Theorem 3.4. $\square$

Here is an analog of Algorithm 3.4 that tries to compute the LDL* factorization of a $d$-banded matrix $\boldsymbol{A}$ with $d \geq 1$. It uses the upper part of the matrix.

```
function [L,dg]=LDLs(A,d)
% [L,dg]=LDLs(A,d)
n=length(A);
L=eye(n,n); dg=zeros(n,1);dg(1)=A(1,1);
for k=2:n
    m=rforwardsolve(L(1:k-1,1:k-1),A(1:k-1,k),d);
    L (k,1:k-1)=m./dg(1:k-1);
    dg(k)=A(k,k)-L(k,1:k-1)*m;
end
```

Listing 4.1 LDLs

The number of arithmetic operations for the LDL* factorization is approximately $\frac{1}{2} G_{n}$, half the number of operations needed for the LU factorization. Indeed, in the L1U factorization we needed to solve two triangular systems to find the vectors $\boldsymbol{s}$ and $\boldsymbol{m}$, while only one such system is needed to find $\boldsymbol{m}$ in the Hermitian case (4.3). The work to find $d_{n n}$ is $O(n)$ and does not contribute to the highest order term.

Example 4.2 (A Factorization) Is the factorization

$$
\left[\begin{array}{ll}
3 & 1 \\
1 & 3
\end{array}\right]=\left[\begin{array}{cc}
1 & 0 \\
1 / 3 & 1
\end{array}\right]\left[\begin{array}{cc}
3 & 0 \\
0 & 8 / 3
\end{array}\right]\left[\begin{array}{cc}
1 & 1 / 3 \\
0 & 1
\end{array}\right]
$$

an LDL* factorization?

### 4.2 Positive Definite and Semidefinite Matrices

Given $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. The function $f: \mathbb{C}^{n} \rightarrow \mathbb{R}$ given by

$$
f(\boldsymbol{x})=\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j} \bar{x}_{i} x_{j}
$$

is called a quadratic form. Note that $f$ is real valued if $\boldsymbol{A}$ is Hermitian. Indeed, $\overline{f(\boldsymbol{x})}=\overline{\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}}=\left(\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}\right)^{*}=\boldsymbol{x}^{*} \boldsymbol{A}^{*} \boldsymbol{x}=f(\boldsymbol{x})$.

Definition 4.1 (Positive Definite Matrix) We say that a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is

(i) positive definite if $\boldsymbol{A}^{*}=\boldsymbol{A}$ and $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}>0$ for all nonzero $\boldsymbol{x} \in \mathbb{C}^{n}$;
(ii) positive semidefinite if $\boldsymbol{A}^{*}=\boldsymbol{A}$ and $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x} \geq 0$ for all $\boldsymbol{x} \in \mathbb{C}^{n}$;
(iii) negative (semi)definite if $-\boldsymbol{A}$ is positive (semi)definite.

We observe that

1. The zero-matrix is positive semidefinite, while the unit matrix is positive definite.
2. The matrix $\boldsymbol{A}$ is positive definite if and only if it is positive semidefinite and $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=0 \Longrightarrow \boldsymbol{x}=\mathbf{0}$.
3. A positive definite matrix $\boldsymbol{A}$ is nonsingular. For if $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$ then $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=0$ and this implies that $\boldsymbol{x}=\mathbf{0}$.
4. It follows from Lemma 4.6 that a nonsingular positive semidefinite matrix is positive definite.
5. If $\boldsymbol{A}$ is real then it is enough to show definiteness for real vectors only. Indeed, if $\boldsymbol{A} \in \mathbb{R}^{n \times n}, \boldsymbol{A}^{T}=\boldsymbol{A}$ and $\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x}>0$ for all nonzero $\boldsymbol{x} \in \mathbb{R}^{n}$ then $\boldsymbol{z}^{*} \boldsymbol{A} \boldsymbol{z}>0$ for all nonzero $\boldsymbol{z} \in \mathbb{C}^{n}$. For if $\boldsymbol{z}=\boldsymbol{x}+i \boldsymbol{y} \neq \mathbf{0}$ with $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$ then
$$
\begin{aligned}
z^{*} A z & =(x-i y)^{T} A(x+i y)=x^{T} A x-i y^{T} A x+i x^{T} A y-i^{2} y^{T} A y \\
& =x^{T} A x+y^{T} A y,
\end{aligned}
$$
and this is positive since at least one of the real vectors $\boldsymbol{x}, \boldsymbol{y}$ is nonzero.

Example 4.3 (Gradient and Hessian) Symmetric positive definite matrices is important in nonlinear optimization. Consider (cf. (16.1)) the gradient $\nabla f$ and hessian $H f$ of a function $f: \Omega \subset \mathbb{R}^{n} \rightarrow \mathbb{R}$

$$
\nabla f(\boldsymbol{x})=\left[\begin{array}{c}
\frac{\partial f(\boldsymbol{x})}{\partial x_{1}} \\
\vdots \\
\frac{\partial f(\boldsymbol{x})}{\partial x_{n}}
\end{array}\right] \in \mathbb{R}^{n}, \quad H f(\boldsymbol{x})=\left[\begin{array}{ccc}
\frac{\partial^{2} f(\boldsymbol{x})}{\partial x_{1} \partial x_{1}} & \ldots & \frac{\partial^{2} f(\boldsymbol{x})}{\partial x_{1} \partial x_{n}} \\
\vdots & & \vdots \\
\frac{\partial^{2} f(\boldsymbol{x})}{\partial x_{n} \partial x_{1}} & \ldots & \frac{\partial^{2} f(\boldsymbol{x})}{\partial x_{n} \partial x_{n}}
\end{array}\right] \in \mathbb{R}^{n \times n} .
$$

We assume that $f$ has continuous first and second order partial derivatives on $\Omega$.
Under suitable conditions on the domain $\Omega$ it is shown in advanced calculus texts that if $\nabla f(\boldsymbol{x})=\mathbf{0}$ and $H f(\boldsymbol{x})$ is positive definite then $\boldsymbol{x}$ is a local minimum for $f$. This can be shown using the second-order Taylor expansion (16.2). Moreover, $\boldsymbol{x}$ is a local maximum if $\nabla f(\boldsymbol{x})=\mathbf{0}$ and $H f(\boldsymbol{x})$ is negative definite.

Lemma 4.2 (The Matrix $\boldsymbol{A}^{*} \boldsymbol{A}$ ) The matrix $\boldsymbol{A}^{*} \boldsymbol{A}$ is positive semidefinite for any $m, n \in \mathbb{N}$ and $\boldsymbol{A} \in \mathbb{C}^{m \times n}$. It is positive definite if and only if $\boldsymbol{A}$ has linearly independent columns or equivalently rank $n$.

Proof Clearly $\boldsymbol{A}^{*} \boldsymbol{A}$ is Hermitian. Let $\boldsymbol{x} \in \mathbb{C}^{n}$ and set $\boldsymbol{z}:=\boldsymbol{A} \boldsymbol{x}$. By the definition (1.11) of the Euclidean norm we have $\boldsymbol{x}^{*} \boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{z}^{*} \boldsymbol{z}=\|\boldsymbol{z}\|_{2}^{2}=\|\boldsymbol{A} \boldsymbol{x}\|_{2}^{2} \geq 0$ with equality if and only if $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$. It follows that $\boldsymbol{A}^{*} \boldsymbol{A}$ is positive semidefinite and positive definite if and only if $\boldsymbol{A}$ has linearly independent columns. But this is equivalent to $\boldsymbol{A}$ having rank $n$ (cf. Definition 1.6). $\square$

Lemma 4.3 (T Is Positive Definite) The second derivative matrix $\boldsymbol{T}=$ $\operatorname{tridiag}(-1,2,-1) \in \mathbb{R}^{n \times n}$ is positive definite.

Proof Clearly $\boldsymbol{T}$ is symmetric. For any $\boldsymbol{x} \in \mathbb{R}^{n}$

$$
\begin{aligned}
\boldsymbol{x}^{T} \boldsymbol{T} \boldsymbol{x} & =2 \sum_{i=1}^{n} x_{i}^{2}-\sum_{i=1}^{n-1} x_{i} x_{i+1}-\sum_{i=2}^{n} x_{i-1} x_{i} \\
& =\sum_{i=1}^{n-1} x_{i}^{2}-2 \sum_{i=1}^{n-1} x_{i} x_{i+1}+\sum_{i=1}^{n-1} x_{i+1}^{2}+x_{1}^{2}+x_{n}^{2} \\
& =x_{1}^{2}+x_{n}^{2}+\sum_{i=1}^{n-1}\left(x_{i+1}-x_{i}\right)^{2} .
\end{aligned}
$$

Thus $\boldsymbol{x}^{T} \boldsymbol{T} \boldsymbol{x} \geq 0$ and if $\boldsymbol{x}^{T} \boldsymbol{T} \boldsymbol{x}=0$ then $x_{1}=x_{n}=0$ and $x_{i}=x_{i+1}$ for $i=$ $1, \ldots, n-1$ which implies that $\boldsymbol{x}=0$. Hence $\boldsymbol{T}$ is positive definite. $\square$

### 4.2.1 The Cholesky Factorization

Recall that a principal submatrix $\boldsymbol{B}=\boldsymbol{A}(\boldsymbol{r}, \boldsymbol{r}) \in \mathbb{C}^{k \times k}$ of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has elements $b_{i, j}=a_{r_{i}, r_{j}}$ for $i, j=1, \ldots, k$, where $1 \leq r_{1}<\cdots<r_{k} \leq n$. It is a leading principal submatrix, denoted $\boldsymbol{A}_{[k]}$ if $\boldsymbol{r}=[1,2, \ldots, k]^{T}$. We have

$$
\boldsymbol{A}(\boldsymbol{r}, \boldsymbol{r})=\boldsymbol{X}^{*} \boldsymbol{A} \boldsymbol{X}, \quad \boldsymbol{X}:=\left[\boldsymbol{e}_{r_{1}}, \ldots, \boldsymbol{e}_{r_{k}}\right] \in \mathbb{C}^{n \times k} .
$$

Lemma 4.4 (Submatrices) Any principal submatrix of a positive (semi)definite matrix is positive (semi)definite.

Proof Let $\boldsymbol{X}$ and $\boldsymbol{B}:=\boldsymbol{A}(\boldsymbol{r}, \boldsymbol{r})$ be given by (4.5). If $\boldsymbol{A}$ is positive semidefinite then $\boldsymbol{B}$ is positive semidefinite since

$$
\boldsymbol{y}^{*} \boldsymbol{B} \boldsymbol{y}=\boldsymbol{y}^{*} \boldsymbol{X}^{*} \boldsymbol{A} \boldsymbol{X} \boldsymbol{y}=\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x} \geq 0, \quad \boldsymbol{y} \in \mathbb{C}^{k}, \quad \boldsymbol{x}:=\boldsymbol{X} \boldsymbol{y} .
$$

Suppose $\boldsymbol{A}$ is positive definite and $\boldsymbol{y}^{*} \boldsymbol{B} \boldsymbol{y}=0$. By (4.6) we have $\boldsymbol{x}=\mathbf{0}$ and since $\boldsymbol{X}$ has linearly independent columns it follows that $\boldsymbol{y}=\mathbf{0}$. We conclude that $\boldsymbol{B}$ is positive definite. $\square$

Theorem 4.2 (LDL* and LL*) The following is equivalent for a matrix $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$.

1. $\boldsymbol{A}$ is positive definite,
2. $\boldsymbol{A}$ has an LDL* factorization with positive diagonal elements in $\boldsymbol{D}$,
3. A has a Cholesky factorization.

If the Cholesky factorization exists it is unique.
Proof Recall that $\boldsymbol{A}^{-*}:=\left(\boldsymbol{A}^{-1}\right)^{*}=\left(\boldsymbol{A}^{*}\right)^{-1}$.
We show that $1 \Longrightarrow 2 \Longrightarrow 3 \Longrightarrow 1$.

$1 \Longrightarrow$ 2: Suppose $\boldsymbol{A}$ is positive definite. By Lemma 4.4 the leading principal submatrices $\boldsymbol{A}_{[k]} \in \mathbb{C}^{k \times k}$ are positive definite and therefore nonsingular for $k=1, \ldots, n-1$. Since $\boldsymbol{A}$ is Hermitian it has by Theorem 4.1 a unique LDL* factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{D} \boldsymbol{L}^{*}$. To show that the $i$ th diagonal element in $\boldsymbol{D}$ is positive we note that $\boldsymbol{x}_{i}:=\boldsymbol{L}^{-*} \boldsymbol{e}_{i}$ is nonzero since $\boldsymbol{L}^{-*}$ is nonsingular. But then $d_{i i}=\boldsymbol{e}_{i}^{*} \boldsymbol{D} \boldsymbol{e}_{i}=\boldsymbol{e}_{i}^{*} \boldsymbol{L}^{-1} \boldsymbol{A} \boldsymbol{L}^{-*} \boldsymbol{e}_{i}=\boldsymbol{x}_{i}^{*} \boldsymbol{A} \boldsymbol{x}_{i}>0$ since $\boldsymbol{A}$ is positive definite.
$2 \Longrightarrow$ 3: Suppose $\boldsymbol{A}$ has an $\mathrm{LDL}^{*}$ factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{D} \boldsymbol{L}^{*}$ with positive diagonal elements $d_{i i}$ in $\boldsymbol{D}$. Then $\boldsymbol{A}=\boldsymbol{S} \boldsymbol{S}^{*}$, where $\boldsymbol{S}:=\boldsymbol{L} \boldsymbol{D}^{1 / 2}$ and $\boldsymbol{D}^{1 / 2}:=$ $\operatorname{diag}\left(\sqrt{d_{11}}, \ldots, \sqrt{d_{n n}}\right)$, and this is a Cholesky factorization of $\boldsymbol{A}$.
$3 \Longrightarrow$ 1: Suppose $\boldsymbol{A}$ has a Cholesky factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{*}$. Clearly $\boldsymbol{A}^{*}=\boldsymbol{A}$. Since $\boldsymbol{L}$ has positive diagonal elements it is nonsingular and $\boldsymbol{A}$ is positive definite by Lemma 4.2.

For uniqueness suppose $\boldsymbol{L} \boldsymbol{L}^{*}=\boldsymbol{S} \boldsymbol{S}^{*}$ are two Cholesky factorizations of the positive definite matrix $\boldsymbol{A}$. Since $\boldsymbol{A}$ is nonsingular both $\boldsymbol{L}$ and $\boldsymbol{S}$ are nonsingular. Then $\boldsymbol{S}^{-1} \boldsymbol{L}=\boldsymbol{S}^{*} \boldsymbol{L}^{-*}$, where by Lemma $2.5 \boldsymbol{S}^{-1} \boldsymbol{L}$ is lower triangular and $\boldsymbol{S}^{*} \boldsymbol{L}^{-*}$ is upper triangular, with diagonal elements $\ell_{i i} / s_{i i}$ and $s_{i i} / \ell_{i i}$, respectively. But then both matrices must be equal to the same diagonal matrix and $\ell_{i i}^{2}=s_{i i}^{2}$. By positivity $\ell_{i i}=s_{i i}$ and we conclude that $\boldsymbol{S}^{-1} \boldsymbol{L}=\boldsymbol{I}=\boldsymbol{S}^{*} \boldsymbol{L}^{-*}$ which means that $\boldsymbol{L}=\boldsymbol{S}$. $\square$

A Cholesky factorization can also be written in the equivalent form $\boldsymbol{A}=\boldsymbol{R}^{*} \boldsymbol{R}$, where $\boldsymbol{R}=\boldsymbol{L}^{*}$ is upper triangular with positive diagonal elements.

Example $4.4(2 \times 2)$ The matrix $\boldsymbol{A}=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$ has an LDL* and a Choleskyfactorization given by

$$
\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right]=\left[\begin{array}{cc}
1 & 0 \\
-\frac{1}{2} & 1
\end{array}\right]\left[\begin{array}{ll}
2 & 0 \\
0 & \frac{3}{2}
\end{array}\right]\left[\begin{array}{cc}
1 & -\frac{1}{2} \\
0 & 1
\end{array}\right]=\left[\begin{array}{cc}
\sqrt{2} & 0 \\
-1 / \sqrt{2} & \sqrt{3 / 2}
\end{array}\right]\left[\begin{array}{cc}
\sqrt{2} & -1 / \sqrt{2} \\
0 & \sqrt{3 / 2}
\end{array}\right] .
$$

There are many good algorithms for finding the Cholesky factorization of a matrix, see [3]. The following version for finding the factorization of a matrix $\boldsymbol{A}$ with bandwidth $d \geq 1$ uses the LDL* factorization Algorithm 4.1. Only the upper part of $\boldsymbol{A}$ is used. The algorithm uses the MATLAB command diag.

```
function L=bandcholesky (A,d)
%L=bandcholesky (A, d)
[L,dg]=LDL(A,d);
L=L*diag(sqrt(dg));
end
```

As for the LDL* factorization the leading term in an operation count for a band matrix is $O\left(d^{2} n\right)$. When $d$ is small this is a considerable saving compared to the count $\frac{1}{2} G_{n}=n^{3} / 3$ for a full matrix.

### 4.2.2 Positive Definite and Positive Semidefinite Criteria

Not all Hermitian matrices are positive definite, and sometimes we can tell just by glancing at the matrix that it cannot be positive definite. Here are some necessary conditions.

Theorem 4.3 (Necessary Conditions for Positive (Semi)Definiteness) If $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$ is positive (semi)definite then for all $i, j$ with $i \neq j$

1. $a_{i i}>0,\left(a_{i i} \geq 0\right)$,
2. $\left|\operatorname{Re}\left(a_{i j}\right)\right|<\left(a_{i i}+a_{j j}\right) / 2,\left(\left|\operatorname{Re}\left(a_{i j}\right)\right| \leq\left(a_{i i}+a_{j j}\right) / 2\right)$,
3. $\left|a_{i j}\right|<\sqrt{a_{i i} a_{j j}},\left(\left|a_{i j}\right| \leq \sqrt{a_{i i} a_{j j}}\right)$,
4. If $\boldsymbol{A}$ is positive semidefinite and $a_{i i}=0$ for some $i$ then $a_{i j}=a_{j i}=0$ for $j=1, \ldots, n$.

Proof Clearly $a_{i i}=\boldsymbol{e}_{i}^{T} \boldsymbol{A} \boldsymbol{e}_{i}>(\geq) 0$ and Part 1 follows. If $\alpha, \beta \in \mathbb{C}$ and $\alpha \boldsymbol{e}_{i}+\beta \boldsymbol{e}_{j} \neq$ 0 then

$$
0<(\leq)\left(\alpha \boldsymbol{e}_{i}+\beta \boldsymbol{e}_{j}\right)^{*} \boldsymbol{A}\left(\alpha \boldsymbol{e}_{i}+\beta \boldsymbol{e}_{j}\right)=|\alpha|^{2} a_{i i}+|\beta|^{2} a_{j j}+2 \operatorname{Re}\left(\bar{\alpha} \beta a_{i j}\right) .
$$
Listing 4.2 bandcholesky

Taking $\alpha=1, \beta= \pm 1$ we obtain $a_{i i}+a_{j j} \pm 2 \operatorname{Re} a_{i j}>0$ and this implies Part 2. We first show 3 . when $\boldsymbol{A}$ is positive definite. Taking $\alpha=-a_{i j}, \beta=a_{i i}$ in (4.7) we find

$$
0<\left|a_{i j}\right|^{2} a_{i i}+a_{i i}^{2} a_{j j}-2\left|a_{i j}\right|^{2} a_{i i}=a_{i i}\left(a_{i i} a_{j j}-\left|a_{i j}\right|^{2}\right) .
$$

Since $a_{i i}>0$ Part 3 follows in the positive definite case.
Suppose now $\boldsymbol{A}$ is positive semidefinite. For $\varepsilon>0$ we define $\boldsymbol{B}:=\boldsymbol{A}+\varepsilon \boldsymbol{I}$. The matrix $\boldsymbol{B}$ is positive definite since it is Hermitian and $\boldsymbol{x}^{*} \boldsymbol{B} \boldsymbol{x} \geq \varepsilon\|\boldsymbol{x}\|_{2}^{2}>0$ for any nonzero $\boldsymbol{x} \in \mathbb{C}^{n}$. From what we have shown

$$
\left|a_{i j}\right|=\left|b_{i j}\right|<\sqrt{b_{i i} b_{j j}}=\sqrt{\left(a_{i i}+\varepsilon\right)\left(a_{j j}+\varepsilon\right)}, \quad i \neq j .
$$

Since $\varepsilon>0$ is arbitrary Part 3 follows in the semidefinite case. Since $\boldsymbol{A}$ is Hermitian Part 3 implies Part 4. $\square$

Example 4.5 (Not Positive Definite) Consider the matrices

$$
\boldsymbol{A}_{1}=\left[\begin{array}{ll}
0 & 1 \\
1 & 1
\end{array}\right], \quad \boldsymbol{A}_{2}=\left[\begin{array}{ll}
1 & 2 \\
2 & 2
\end{array}\right], \quad \boldsymbol{A}_{3}=\left[\begin{array}{rr}
-2 & 1 \\
1 & 2
\end{array}\right] .
$$

Here $\boldsymbol{A}_{1}$ and $\boldsymbol{A}_{3}$ are not positive definite, since a diagonal element is not positive. $\boldsymbol{A}_{2}$ is not positive definite since neither Part 2 nor Part 3 in Theorem 4.3 are satisfied.

The matrix $\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$ enjoys all the necessary conditions in Theorem 4.3. But to decide if it is positive definite it is nice to have sufficient conditions as well.

We start by considering eigenvalues of a positive (semi)definite matrix.
Lemma 4.5 (Positive Eigenvalues) A matrix is positive (semi)definite if and only if it is Hermitian and all its eigenvalues are positive (nonnegative).

Proof Suppose $\boldsymbol{A}$ is positive (semi)definite. Then $\boldsymbol{A}$ is Hermitian by definition, and if $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ and $\boldsymbol{x}$ is nonzero, then $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}^{*} \boldsymbol{x}$. This implies that $\lambda>0(\geq 0)$ since $\boldsymbol{A}$ is positive (semi)definite and $\boldsymbol{x}^{*} \boldsymbol{x}=\|\boldsymbol{x}\|_{2}^{2}>0$. Conversely, suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is Hermitian with positive (nonnegative) eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$. By Theorem 6.9 (the spectral theorem) there is a matrix $\boldsymbol{U} \in \mathbb{C}^{n \times n}$ with $\boldsymbol{U}^{*} \boldsymbol{U}=$ $\boldsymbol{U} \boldsymbol{U}^{*}=\boldsymbol{I}$ such that $\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)$. Let $\boldsymbol{x} \in \mathbb{C}^{n}$ and define $\boldsymbol{z}:=$ $\boldsymbol{U}^{*} \boldsymbol{x}=\left[z_{1}, \ldots, z_{n}\right]^{T} \in \mathbb{C}^{n}$. Then $\boldsymbol{x}=\boldsymbol{U} \boldsymbol{U}^{*} \boldsymbol{x}=\boldsymbol{U} \boldsymbol{z}$ and by the spectral theorem

$$
\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=z^{*} \boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U} \boldsymbol{z}=z^{*} \operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right) \boldsymbol{z}=\sum_{j=1}^{n} \lambda_{j}\left|z_{j}\right|^{2} \geq 0 .
$$

It follows that $\boldsymbol{A}$ is positive semidefinite. Since $\boldsymbol{U}^{*}$ is nonsingular we see that $\boldsymbol{z}=$ $\boldsymbol{U}^{*} \boldsymbol{x}$ is nonzero if $\boldsymbol{x}$ is nonzero, and therefore $\boldsymbol{A}$ is positive definite. $\square$

Lemma 4.6 (Positive Semidefinite and Nonsingular) A matrix is positive definite if and only if it is positive semidefinite and nonsingular.

Proof If $\boldsymbol{A}$ is positive definite then it is positive semidefinite and if $\boldsymbol{A} \boldsymbol{x}=\mathbf{0}$ then $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=0$ which implies that $\boldsymbol{x}=\mathbf{0}$. Conversely, if $\boldsymbol{A}$ is positive semidefinite then it is Hermitian with nonnegative eigenvalues (cf. Lemma 4.5). If it is nonsingular all eigenvalues are positive (cf. Theorem 1.11), and it follows from Lemma 4.5 that $\boldsymbol{A}$ is positive definite. $\square$

The following necessary and sufficient conditions can be used to decide if a matrix is positive definite.

Theorem 4.4 (Positive Definite Characterization) The following statements are equivalent for a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$.

1. $\boldsymbol{A}$ is positive definite.
2. $\boldsymbol{A}$ is Hermitian with only positive eigenvalues.
3. $\boldsymbol{A}$ is Hermitian and all leading principal submatrices have a positive determinant.
4. $\boldsymbol{A}=\boldsymbol{B} \boldsymbol{B}^{*}$ for a nonsingular $\boldsymbol{B} \in \mathbb{C}^{n \times n}$.

Proof

1 ⟺ 2: This follows from Lemma 4.5.
1 ⟹ 3: A positive definite matrix has positive eigenvalues, and since the determinant of a matrix equals the product of its eigenvalues (cf. Theorem 1.10) the determinant is positive. Every leading principal submatrix of a positive definite matrix is positive definite (cf. Lemma 4.4) and therefore has a positive determinant.
3 ⟹ 4: Since a leading principal submatrix has a positive determinant it is nonsingular and Theorem 4.1 implies that $\boldsymbol{A}$ has a unique LDL* factorization and by Theorem 4.2 a unique Cholesky factorization $\boldsymbol{A}=\boldsymbol{B} \boldsymbol{B}^{*}$ with $\boldsymbol{B}=\boldsymbol{L}$.
$4 \Longrightarrow$ 1: This follows from Lemma 4.2.

Example 4.6 (Positive Definite Characterization) Consider the symmetric matrix $\boldsymbol{A}:=\left[\begin{array}{ll}3 & 1 \\ 1 & 3\end{array}\right]$.

1. We have $\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x}=2 x_{1}^{2}+2 x_{2}^{2}+\left(x_{1}+x_{2}\right)^{2}>0$ for all nonzero $\boldsymbol{x}$ showing that $\boldsymbol{A}$ is positive definite.
2. The eigenvalues of $\boldsymbol{A}$ are $\lambda_{1}=2$ and $\lambda_{2}=4$. They are positive showing that $\boldsymbol{A}$ is positive definite since it is symmetric.
3. We find $\operatorname{det}\left(\boldsymbol{A}_{[1]}\right)=3$ and $\operatorname{det}\left(\boldsymbol{A}_{[2]}\right)=8$ showing again that $\boldsymbol{A}$ is positive definite since it is also symmetric.
4. Finally $\boldsymbol{A}$ is positive definite since by Example 4.2 we have
$$
\boldsymbol{A}=\boldsymbol{B B}^{*}, \quad \boldsymbol{B}=\left[\begin{array}{cc}
1 & 0 \\
1 / 3 & 1
\end{array}\right]\left[\begin{array}{cc}
\sqrt{3} & 0 \\
0 & \sqrt{8 / 3}
\end{array}\right] .
$$

### 4.3 Semi-Cholesky Factorization of a Banded Matrix

A positive semidefinite matrix has a factorization that is similar to the Cholesky factorization.

Definition 4.2 (Semi-Cholesky Factorization) A factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{*}$ of $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$, where $\boldsymbol{L}$ is lower triangular with nonnegative diagonal elements is called a semi-Cholesky factorization.

Note that a semi-Cholesky factorization of a positive definite matrix is necessarily a Cholesky factorization. For if $\boldsymbol{A}$ is positive definite then it is nonsingular and then $\boldsymbol{L}$ must be nonsingular. Thus the diagonal elements of $\boldsymbol{L}$ cannot be zero.

Theorem 4.5 (Characterization, Semi-Cholesky Factorization) A matrix $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$ has a semi-Cholesky factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{*}$ if and only if it is positive semidefinite.

Proof If $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{*}$ is a semi-Cholesky factorization then $\boldsymbol{A}$ is Hermitian. Moreover, $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=\left\|\boldsymbol{L}^{*} \boldsymbol{x}\right\|_{2}^{2} \geq 0$ and $\boldsymbol{A}$ is positive semidefinite. For the converse we use induction on $n$. A positive semidefinite matrix of order one has a semi-Cholesky factorization since the only element in $\boldsymbol{A}$ is nonnegative. Suppose any positive semidefinite matrix of order $n-1$ has a semi-Cholesky factorization and suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is positive semidefinite. We partition $\boldsymbol{A}$ as follows

$$
\boldsymbol{A}=\left[\begin{array}{ll}
\alpha & \boldsymbol{v}^{*} \\
\boldsymbol{v} & \boldsymbol{B}
\end{array}\right], \quad \alpha \in \mathbb{C}, \quad \boldsymbol{v} \in \mathbb{C}^{n-1}, \quad \boldsymbol{B} \in \mathbb{C}^{(n-1) \times(n-1)} .
$$

There are two cases. Suppose first $\alpha=\boldsymbol{e}_{1}^{*} \boldsymbol{A} \boldsymbol{e}_{1}>0$. We claim that $\boldsymbol{C}:=\boldsymbol{B}-$ $\boldsymbol{v} \boldsymbol{v}^{*} / \alpha$ is positive semidefinite. $\boldsymbol{C}$ is Hermitian since $\boldsymbol{B}$ is. To show that $\boldsymbol{C}$ is positive semidefinite we consider any $\boldsymbol{y} \in \mathbb{C}^{n-1}$ and define $\boldsymbol{x}^{*}:=\left[-\boldsymbol{y}^{*} \boldsymbol{v} / \alpha, \boldsymbol{y}^{*}\right] \in \mathbb{C}^{n}$. Then

$$
\begin{aligned}
0 \leq \boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x} & =\left[-\boldsymbol{y}^{*} \boldsymbol{v} / \alpha, \boldsymbol{y}^{*}\right]\left[\begin{array}{ll}
\alpha & \boldsymbol{v}^{*} \\
\boldsymbol{v} & \boldsymbol{B}
\end{array}\right]\left[\begin{array}{c}
-\boldsymbol{v}^{*} \boldsymbol{y} / \alpha \\
\boldsymbol{y}
\end{array}\right] \\
& =\left[0,-\left(\boldsymbol{y}^{*} \boldsymbol{v}\right) \boldsymbol{v}^{*} / \alpha+\boldsymbol{y}^{*} \boldsymbol{B}\right]\left[\begin{array}{c}
-\boldsymbol{v}^{*} \boldsymbol{y} / \alpha \\
\boldsymbol{y}
\end{array}\right] \\
& =-\boldsymbol{y}^{*} \boldsymbol{v} \boldsymbol{v}^{*} \boldsymbol{y} / \alpha+\boldsymbol{y}^{*} \boldsymbol{B} \boldsymbol{y}=\boldsymbol{y}^{*} \boldsymbol{C} \boldsymbol{y} .
\end{aligned}
$$

So $\boldsymbol{C} \in \mathbb{C}^{(n-1) \times(n-1)}$ is positive semidefinite and by the induction hypothesis it has a semi-Cholesky factorization $\boldsymbol{C}=\boldsymbol{L}_{1} \boldsymbol{L}_{1}^{*}$. The matrix

$$
\boldsymbol{L}^{*}:=\left[\begin{array}{cc}
\beta & \boldsymbol{v}^{*} / \beta \\
\mathbf{0} & \boldsymbol{L}_{1}^{*}
\end{array}\right], \quad \beta:=\sqrt{\alpha},
$$

is upper triangular with nonnegative diagonal elements and

$$
\boldsymbol{L} \boldsymbol{L}^{*}=\left[\begin{array}{cc}
\beta & \mathbf{0} \\
\boldsymbol{v} / \beta & \boldsymbol{L}_{1}
\end{array}\right]\left[\begin{array}{cc}
\beta & \boldsymbol{v}^{*} / \beta \\
\mathbf{0} & \boldsymbol{L}_{1}^{*}
\end{array}\right]=\left[\begin{array}{ll}
\alpha & \boldsymbol{v}^{*} \\
\boldsymbol{v} & \boldsymbol{B}
\end{array}\right]=\boldsymbol{A}
$$

is a semi-Cholesky factorization of $\boldsymbol{A}$.
If $\alpha=0$ then part 4 of Theorem 4.3 implies that $\boldsymbol{v}=\mathbf{0}$. Moreover, $\boldsymbol{B} \in$ $\mathbb{C}^{(n-1) \times(n-1)}$ in (4.8) is positive semidefinite and therefore has a semi-Cholesky
factorization $\boldsymbol{B}=\boldsymbol{L}_{1} \boldsymbol{L}_{1}^{*}$. But then $\boldsymbol{L}^{*}$, where $\boldsymbol{L}=\left[\begin{array}{cc}0 & \mathbf{0}^{*} \\ \mathbf{0} & \boldsymbol{L}_{1}\end{array}\right]$ is a semi-Cholesky factorization of $\boldsymbol{A}$. Indeed, $\boldsymbol{L}$ is lower triangular and

$$
\boldsymbol{L} \boldsymbol{L}^{*}=\left[\begin{array}{ll}
0 & \mathbf{0}^{*} \\
\mathbf{0} & \boldsymbol{L}_{1}
\end{array}\right]\left[\begin{array}{ll}
0 & \mathbf{0}^{*} \\
\mathbf{0} & \boldsymbol{L}_{1}^{*}
\end{array}\right]=\left[\begin{array}{ll}
0 & \mathbf{0}^{*} \\
\mathbf{0} & \boldsymbol{B}
\end{array}\right]=\boldsymbol{A} .
$$ $\square$

Recall that a matrix $\boldsymbol{A}$ is $d$-banded if $a_{i j}=0$ for $|i-j|>d$. A (semi-) Cholesky factorization preserves bandwidth.

Theorem 4.6 (Bandwidth Semi-Cholesky Factor) The semi-Cholesky factor $\boldsymbol{L}$ given by (4.10) has the same bandwidth as $\boldsymbol{A}$.

Proof Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is $d$-banded. Then $\boldsymbol{v}^{*}=\left[\boldsymbol{u}^{*}, \mathbf{0}^{*}\right]$ in (4.8), where $\boldsymbol{u} \in \mathbb{C}^{d}$, and therefore $\boldsymbol{C}:=\boldsymbol{B}-\boldsymbol{v} \boldsymbol{v}^{*} / \alpha$ differs from $\boldsymbol{B}$ only in the upper left $d \times d$ corner. It follows that $\boldsymbol{C}$ has the same bandwidth as $\boldsymbol{B}$ and $\boldsymbol{A}$. By induction on $n, \boldsymbol{C}=\boldsymbol{L}_{1} \boldsymbol{L}_{1}^{*}$, where $\boldsymbol{L}_{1}^{*}$ has the same bandwidth as $\boldsymbol{C}$. But then $\boldsymbol{L}$ in (4.10) has the same bandwidth as $\boldsymbol{A}$. $\square$

Consider now implementing an algorithm based on the previous discussion. Since $\boldsymbol{A}$ is Hermitian we only need to use the lower part of $\boldsymbol{A}$. The first column of $\boldsymbol{L}$ is $\left[\beta, \boldsymbol{v}^{*} / \beta\right]^{*}$ if $\alpha>0$. If $\alpha=0$ then by 4 in Theorem 4.3 the first column of $\boldsymbol{A}$ is zero and this is also the first column of $\boldsymbol{L}$. We obtain

$$
\begin{aligned}
& \text { if } A(1,1)>0 \\
& A(1,1)=\sqrt{A(1,1)} \\
& A(2: n, 1)=A(2: n, 1) / A(1,1) \\
& \text { for } j=2: n \\
& \quad A(j: n, j)=A(j: n, j)-A(j, 1) * A(j: n, 1)
\end{aligned}
$$

Here we store the first column of $\boldsymbol{L}$ in the first column of $\boldsymbol{A}$ and the lower part of $\boldsymbol{C}=\boldsymbol{B}-\boldsymbol{v} \boldsymbol{v}^{*} / \alpha$ in the lower part of $A(2: n, 2: n)$.

The code can be made more efficient when $\boldsymbol{A}$ is a $d$-banded matrix. We simply replace all occurrences of $n$ by $\min (i+d, n)$. Continuing the reduction we arrive at the following algorithm, which take a $d$-banded positive semidefinite $\boldsymbol{A}$ and $d \geq 1$ as input, and returns a lower triangular matrix $\boldsymbol{L}$ so that $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{*}$. This is the Cholesky factorization of $\boldsymbol{A}$ if $\boldsymbol{A}$ is positive definite and a semi-Cholesky factorization of $\boldsymbol{A}$ otherwise. The algorithm uses the MATLAB command tril:

```
function L=bandsemicholeskyL(A,d)
%L=bandsemicholeskyL (A,d)
n=length(A);
for k=1:n
    kp=min(n,k+d);
    if A(k,k) >0
        A(k,k)=sqrt(A(k,k));
        A((k+1):kp,k)=A((k+1):kp,k)/A(k,k);
            for j=k+1:kp
                A(j:kp,j)=A(j:kp,j)-A(j,k)*A(j:kp,k);
            end
    else
            A(k:kp,k)=zeros(kp-k+1,1);
    end
end
L=tril(A);
end
```

Listing 4.3 bandsemicholeskyL

In the algorithm we overwrite the lower triangle of $\boldsymbol{A}$ with the elements of $\boldsymbol{L}$. Column $k$ of $\boldsymbol{L}$ is zero for those $k$ where $\ell_{k k}=0$. We reduce round-off noise by forcing those rows to be zero. In the semidefinite case no update is necessary and we "do nothing".

Deciding when a diagonal element is zero can be a problem in floating point arithmetic.

We end the section with some necessary and sufficient conditions for a matrix to be positive semidefinite.

Theorem 4.7 (Positive Semidefinite Characterization) The following is equivalent for a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$.

1. $\boldsymbol{A}$ is positive semidefinite.
2. $\boldsymbol{A}$ is Hermitian with only nonnegative eigenvalues.
3. $\boldsymbol{A}$ is Hermitian and all principal submatrices have a nonnegative determinant.
4. $\boldsymbol{A}=\boldsymbol{B} \boldsymbol{B}^{*}$ for some $\boldsymbol{B} \in \mathbb{C}^{n \times n}$.

Proof

$1 \Longleftrightarrow 2$ : This follows from Lemma 4.5.
$1 \Longleftrightarrow$ 4: This follows from Theorem 4.5
$1 \Longleftrightarrow 3$ : We refer to page 567 of [15], where it is shown that $4 \Longrightarrow 3$ (and therefore $1 \Longrightarrow 3$ since $1 \Longleftrightarrow 4$ ) and $3 \Longrightarrow 1$. $\square$

Example 4.7 (Positive Semidefinite Characterization) Consider the symmetric matrix $\boldsymbol{A}:=\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$.

1. We have $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=x_{1}^{2}+x_{2}^{2}+x_{1} x_{2}+x_{2} x_{1}=\left(x_{1}+x_{2}\right)^{2} \geq 0$ for all $\boldsymbol{x} \in \mathbb{R}^{2}$ showing that $\boldsymbol{A}$ is positive semidefinite.
2. The eigenvalues of $\boldsymbol{A}$ are $\lambda_{1}=2$ and $\lambda_{2}=0$ and they are nonnegative showing that $\boldsymbol{A}$ is positive semidefinite since it is symmetric.
3. There are three principal sub matrices, and they have determinants $\operatorname{det}\left(\left[a_{11}\right]\right)=$ 1, $\operatorname{det}\left(\left[a_{22}\right]\right)=1$ and $\operatorname{det}(\boldsymbol{A})=0$ and showing again that $\boldsymbol{A}$ is positive semidefinite.
4. Finally $\boldsymbol{A}$ is positive semidefinite since $\boldsymbol{A}=\boldsymbol{B B}^{*}$, where $\boldsymbol{B}=\left[\begin{array}{ll}1 & 0 \\ 1 & 0\end{array}\right]$.

In part 4 of Theorem 4.7 we require nonnegativity of all principal minors, while only positivity of leading principal minors was required for positive definite matrices (cf. Theorem 4.4). To see that nonnegativity of the leading principal minors is not enough consider the matrix $\boldsymbol{A}:=\left[\begin{array}{rr}0 & 0 \\ 0 & -1\end{array}\right]$. The leading principal minors are nonnegative, but $\boldsymbol{A}$ is not positive semidefinite.

### 4.4 The Non-symmetric Real Case

In this section we say that a matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is positive semidefinite if $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x} \geq 0$ for all $\boldsymbol{x} \in \mathbb{R}^{n}$ and positive definite if $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}>0$ for all nonzero $\boldsymbol{x} \in \mathbb{R}^{n}$. Thus we do not require $\boldsymbol{A}$ to be symmetric. This means that some of the eigenvalues can be complex (cf. Example 4.8). Note that a non-symmetric positive definite matrix is nonsingular, but in Exercise 4.3 you can show that a converse is not true.

We have the following theorem.
Theorem 4.8 (The Non-symmetric Case) Suppose $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is positive definite. Then the following holds true.

1. Every principal submatrix of $\boldsymbol{A}$ is positive definite,
2. A has a unique LU factorization,
3. the real eigenvalues of $\boldsymbol{A}$ are positive,
4. $\operatorname{det}(\boldsymbol{A})>0$,
5. $a_{i i} a_{j j}>a_{i j} a_{j i}$, for $i \neq j$.

Proof

1. The proof is the same as for Lemma 4.4.
2. Since all leading submatrices are positive definite they are nonsingular and the result follows from the LU Theorem 3.4.

3. Suppose $(\lambda, \boldsymbol{x})$ is an eigenpair of $\boldsymbol{A}$ and that $\lambda$ is real. Since $\boldsymbol{A}$ is real we can choose $\boldsymbol{x}$ to be real. Multiplying $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ by $\boldsymbol{x}^{T}$ and solving for $\lambda$ we find $\lambda=\frac{\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x}}{\boldsymbol{x}^{T} \boldsymbol{x}}>0$.
4. The determinant of $\boldsymbol{A}$ equals the product of its eigenvalues. The eigenvalues are either real and positive or occur in complex conjugate pairs. The product of two nonzero complex conjugate numbers is positive.
5. The principal submatrix $\left[\begin{array}{cc}a_{i i} & a_{i j} \\ a_{j i} & a_{j j}\end{array}\right]$ has a positive determinant.

Example 4.8 ( $2 \times 2$ Positive Definite) A non-symmetric positive definite matrix can have complex eigenvalues. The family of matrices

$$
\boldsymbol{A}[a]:=\left[\begin{array}{cc}
2 & 2-a \\
a & 1
\end{array}\right], \quad a \in \mathbb{R}
$$

is positive definite for any $a \in \mathbb{R}$. Indeed, for any nonzero $\boldsymbol{x} \in \mathbb{R}^{2}$

$$
\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x}=2 x_{1}^{2}+(2-a) x_{1} x_{2}+a x_{2} x_{1}+x_{2}^{2}=x_{1}^{2}+\left(x_{1}+x_{2}\right)^{2}>0 .
$$

The eigenvalues of $\boldsymbol{A}[a]$ are positive for $a \in\left[1-\frac{\sqrt{5}}{2}, 1+\frac{\sqrt{5}}{2}\right]$ and complex for other values of $a$.

### 4.5 Exercises Chap. 4

### 4.5.1 Exercises Sect. 4.2

Exercise 4.1 (Positive Definite Characterizations) Show directly that all 4 characterizations in Theorem 4.4 hold for the matrix $\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$.

Exercise 4.2 (L1U factorization (Exam 1982-1)) ]Find the L1U factorization of the following matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$

$$
A=\left(\begin{array}{ccccc}
1 & -1 & 0 & \cdots & 0 \\
-1 & 2 & -1 & \ddots & \vdots \\
0 & \ddots & \ddots & \ddots & 0 \\
\vdots & \ddots & -1 & 2 & -1 \\
0 & \cdots & 0 & -1 & 2
\end{array}\right) .
$$

Is $\boldsymbol{A}$ positive definite?

Exercise 4.3 (A Counterexample) In the non-symmetric case a nonsingular positive semidefinite matrix is not necessarily positive definite. Show this by considering the matrix $\boldsymbol{A}:=\left[\begin{array}{cc}1 & 0 \\ -2 & 1\end{array}\right]$.

Exercise 4.4 (Cholesky Update (Exam Exercise 2015-2))

a) Let $\boldsymbol{E} \in \mathbb{R}^{n \times n}$ be of the form $\boldsymbol{E}=\boldsymbol{I}+\boldsymbol{u} \boldsymbol{u}^{T}$, where $\boldsymbol{u} \in \mathbb{R}^{n}$. Show that $\boldsymbol{E}$ is symmetric and positive definite, and find an expression for $\boldsymbol{E}^{-1} .1$
b) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be of the form $\boldsymbol{A}=\boldsymbol{B}+\boldsymbol{u} \boldsymbol{u}^{T}$, where $\boldsymbol{B} \in \mathbb{R}^{n \times n}$ is symmetric and positive definite, and $\boldsymbol{u} \in \mathbb{R}^{n}$. Show that $\boldsymbol{A}$ can be decomposed as
$$
\boldsymbol{A}=\boldsymbol{L}\left(\boldsymbol{I}+\boldsymbol{v} \boldsymbol{v}^{T}\right) \boldsymbol{L}^{T},
$$
where $\boldsymbol{L}$ is nonsingular and lower triangular, and $\boldsymbol{v} \in \mathbb{R}^{n}$.
c) Assume that the Cholesky decomposition of $\boldsymbol{B}$ is already computed. Outline a procedure to solve the system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A}$ is of the form above.

Exercise 4.5 (Cholesky Update (Exam Exercise 2016-2)) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be a symmetric positive definite matrix with a known Cholesky factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{T}$. Furthermore, let $\boldsymbol{A}_{+}$be a corresponding $(n+1) \times(n+1)$ matrix of the form

$$
\boldsymbol{A}_{+}=\left[\begin{array}{cc}
\boldsymbol{A} & \boldsymbol{a} \\
\boldsymbol{a}^{T} & \alpha
\end{array}\right],
$$

where $\boldsymbol{a}$ is a vector in $\mathbb{R}^{n}$, and $\alpha$ is a real number. We assume that the matrix $\boldsymbol{A}_{+}$is symmetric positive definite.

a) Show that if $\boldsymbol{A}_{+}=\boldsymbol{L}_{+} \boldsymbol{L}_{+}^{T}$ is the Cholesky factorization of $\boldsymbol{A}_{+}$, then $\boldsymbol{L}_{+}$is of the form
$$
\boldsymbol{L}_{+}=\left[\begin{array}{cc}
\boldsymbol{L} & 0 \\
\boldsymbol{y}^{T} & \lambda
\end{array}\right],
$$
i.e., that the leading principal $n \times n$ submatrix of $\boldsymbol{L}_{+}$is $\boldsymbol{L}$.
b) Explain why $\alpha>\left\|\boldsymbol{L}^{-1} \boldsymbol{a}\right\|_{2}^{2}$.
c) Explain how you can compute $\boldsymbol{L}_{+}$when $\boldsymbol{L}$ is known.

### 4.6 Review Questions

4.6.1 What is the content of the LDL* theorem?
4.6.2 Is $\boldsymbol{A}^{*} \boldsymbol{A}$ always positive definite?

[^8]

4.6.3Is the matrix $\left[\begin{array}{lll}10 & 4 & 3 \\ 4 & 0 & 2 \\ 3 & 2 & 5\end{array}\right]$ positive definite?
4.6.4What class of matrices has a Cholesky factorization?
4.6.5What is the bandwidth of the Cholesky factor of a band matrix?
4.6.6For a symmetric matrix give 3 conditions that are equivalent to positive definiteness.
4.6.7What class of matrices has a semi-Cholesky factorization?


## Chapter 5 <br> Orthonormal and Unitary Transformations

In Gaussian elimination and LU factorization we solve a linear system by transforming it to triangular form. These are not the only kind of transformations that can be used for such a task. Matrices with orthonormal columns, called unitary matrices can be used to reduce a square matrix to upper triangular form and more generally a rectangular matrix to upper triangular (also called upper trapezoidal) form. This lead to a decomposition of a rectangular matrix known as a QR decomposition and a reduced form which we refer to as a QR factorization. The QR decomposition and factorization will be used in later chapters to solve least squares- and eigenvalue problems.

Unitary transformations have the advantage that they preserve the Euclidian norm of a vector. This means that when a unitary transformation is applied to an inaccurate vector then the error will not grow. Thus a unitary transformation is said to be numerically stable. We consider two classes of unitary transformations known as Householder- and Givens transformations, respectively.

### 5.1 Inner Products, Orthogonality and Unitary Matrices

An inner product or scalar product in a vector space is a function mapping pairs of vectors into a scalar.

### 5.1.1 Real and Complex Inner Products

Definition 5.1 (Inner Product) An inner product in a complex vector space $\mathcal{V}$ is a function $\mathcal{V} \times \mathcal{V} \rightarrow \mathbb{C}$ satisfying for all $\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z} \in \mathcal{V}$ and all $a, b \in \mathbb{C}$ the following conditions:

1. $\langle\boldsymbol{x}, \boldsymbol{x}\rangle \geq 0$ with equality if and only if $\boldsymbol{x}=\mathbf{0}$. (positivity)
2. $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\overline{\langle\boldsymbol{y}, \boldsymbol{x}\rangle}$ (skew symmetry)
3. $\langle a \boldsymbol{x}+b \boldsymbol{y}, \boldsymbol{z}\rangle=a\langle\boldsymbol{x}, \boldsymbol{z}\rangle+b\langle\boldsymbol{y}, \boldsymbol{z}\rangle$. (linearity)

The pair $(\mathcal{V},\langle\cdot, \cdot\rangle)$ is called an inner product space.
Note the complex conjugate in 2 . Since

$$
\langle\boldsymbol{x}, a \boldsymbol{y}+b \boldsymbol{z}\rangle=\overline{\langle a \boldsymbol{y}+b \boldsymbol{z}, \boldsymbol{x}\rangle}=\overline{a\langle\boldsymbol{y}, \boldsymbol{x}\rangle+b\langle\boldsymbol{z}, \boldsymbol{x}\rangle}=\bar{a} \overline{\langle\boldsymbol{y}, \boldsymbol{x}\rangle}+\overline{b\langle\boldsymbol{z}, \boldsymbol{x}\rangle}
$$

we find

$$
\langle\boldsymbol{x}, a \boldsymbol{y}+b \boldsymbol{z}\rangle=\bar{a}\langle\boldsymbol{x}, \boldsymbol{y}\rangle+\bar{b}\langle\boldsymbol{x}, \boldsymbol{z}\rangle, \quad\langle a \boldsymbol{x}, a \boldsymbol{y}\rangle=|a|^{2}\langle\boldsymbol{x}, \boldsymbol{y}\rangle .
$$

An inner product in a real vector space $\mathcal{V}$ is real valued function satisfying Properties 1,2,3 in Definition 5.1, where we can replace skew symmetry by symmetry

$$
\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\langle\boldsymbol{y}, \boldsymbol{x}\rangle \quad \text { (symmetry). }
$$

In the real case we have linearity in both variables since we can remove the complex conjugates in (5.1).

Recall that (cf. (1.10)) the standard inner product in $\mathbb{C}^{n}$ is given by

$$
\langle\boldsymbol{x}, \boldsymbol{y}\rangle:=\boldsymbol{y}^{*} \boldsymbol{x}=\boldsymbol{x}^{T} \overline{\boldsymbol{y}}=\sum_{j=1}^{n} x_{j} \overline{y_{j}} .
$$

Note the complex conjugate on $\boldsymbol{y}$. It is clearly an inner product in $\mathbb{C}^{n}$.
The function

$$
\|\cdot\|: \mathcal{V} \rightarrow \mathbb{R}, \quad \boldsymbol{x} \longmapsto\|\boldsymbol{x}\|:=\sqrt{\langle\boldsymbol{x}, \boldsymbol{x}\rangle}
$$

is called the inner product norm.
The inner product norm for the standard inner product is the Euclidian norm $\|\boldsymbol{x}\|=\|\boldsymbol{x}\|_{2}=\sqrt{\boldsymbol{x}^{*} \boldsymbol{x}}$.

The following inequality holds for any inner product.
Theorem 5.1 (Cauchy-Schwarz Inequality) For any $\boldsymbol{x}$, $\boldsymbol{y}$ in a real or complex inner product space

$$
|\langle\boldsymbol{x}, \boldsymbol{y}\rangle| \leq\|\boldsymbol{x}\|\|\boldsymbol{y}\|,
$$

with equality if and only if $\boldsymbol{x}$ and $\boldsymbol{y}$ are linearly dependent.
Proof If $\boldsymbol{y}=\mathbf{0}$ then $0 \boldsymbol{x}+\boldsymbol{y}=\mathbf{0}$ and $\boldsymbol{x}$ and $\boldsymbol{y}$ are linearly dependent. Moreover the inequality holds with equality since $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\langle\boldsymbol{x}, 0 \boldsymbol{y}\rangle=0\langle\boldsymbol{x}, \boldsymbol{y}\rangle=0$ and $\|\boldsymbol{y}\|=0$. So assume $\boldsymbol{y} \neq \mathbf{0}$. Define

$$
\boldsymbol{z}:=\boldsymbol{x}-a \boldsymbol{y}, \quad a:=\frac{\langle\boldsymbol{x}, \boldsymbol{y}\rangle}{\langle\boldsymbol{y}, \boldsymbol{y}\rangle} .
$$

By linearity $\langle\boldsymbol{z}, \boldsymbol{y}\rangle=\langle\boldsymbol{x}, \boldsymbol{y}\rangle-a\langle\boldsymbol{y}, \boldsymbol{y}\rangle=0$ so that by 2. and (5.1)

$$
\langle a \boldsymbol{y}, \boldsymbol{z}\rangle+\langle\boldsymbol{z}, a \boldsymbol{y}\rangle=a \overline{\langle\boldsymbol{z}, \boldsymbol{y}\rangle}+\bar{a}\langle\boldsymbol{z}, \boldsymbol{y}\rangle=0 .
$$

But then

$$
\begin{aligned}
\|\boldsymbol{x}\|^{2} & =\langle\boldsymbol{x}, \boldsymbol{x}\rangle=\langle\boldsymbol{z}+a \boldsymbol{y}, \boldsymbol{z}+a \boldsymbol{y}\rangle \\
& \stackrel{(5.4)}{=}\langle\boldsymbol{z}, \boldsymbol{z}\rangle+\langle a \boldsymbol{y}, a \boldsymbol{y}\rangle \stackrel{(5.1)}{=}\|\boldsymbol{z}\|^{2}+|a|^{2}\|\boldsymbol{y}\|^{2} \\
& \geq|a|^{2}\|\boldsymbol{y}\|^{2}=\frac{|\langle\boldsymbol{x}, \boldsymbol{y}\rangle|^{2}}{\|\boldsymbol{y}\|^{2}} .
\end{aligned}
$$

Multiplying by $\|\boldsymbol{y}\|^{2}$ gives (5.3). We have equality if and only if $\boldsymbol{z}=\mathbf{0}$, which means that $\boldsymbol{x}$ and $\boldsymbol{y}$ are linearly dependent. $\square$

Theorem 5.2 (Inner Product Norm) For all $\boldsymbol{x}, \boldsymbol{y}$ in an inner product space and all a in $\mathbb{C}$ we have

1. $\|\boldsymbol{x}\| \geq 0$ with equality if and only if $\boldsymbol{x}=\mathbf{0}$.

(positivity)

2. $\|a \boldsymbol{x}\|=|a|\|\boldsymbol{x}\|$.
(homogeneity)
3. $\|\boldsymbol{x}+\boldsymbol{y}\| \leq\|\boldsymbol{x}\|+\|\boldsymbol{y}\|$,
(subadditivity)

where $\|\boldsymbol{x}\|:=\sqrt{\langle\boldsymbol{x}, \boldsymbol{x}\rangle}$.
In general a function $\left\|\|: \mathbb{C}^{n} \rightarrow \mathbb{R}\right.$ that satisfies these three properties is called a vector norm. A class of vector norms called $p$-norms will be studied in Chap. 8.

Proof The first statement is an immediate consequence of positivity, while the second one follows from (5.1). Expanding $\|\boldsymbol{x}+a \boldsymbol{y}\|^{2}=\langle\boldsymbol{x}+a \boldsymbol{y}, \boldsymbol{x}+a \boldsymbol{y}\rangle$ using (5.1) we obtain

$$
\|\boldsymbol{x}+a \boldsymbol{y}\|^{2}=\|\boldsymbol{x}\|^{2}+a\langle\boldsymbol{y}, \boldsymbol{x}\rangle+\bar{a}\langle\boldsymbol{x}, \boldsymbol{y}\rangle+|a|^{2}\|\boldsymbol{y}\|^{2}, \quad a \in \mathbb{C}, \quad \boldsymbol{x}, \boldsymbol{y} \in \mathcal{V} .
$$

Now (5.5) with $a=1$ and the Cauchy-Schwarz inequality implies

$$
\|\boldsymbol{x}+\boldsymbol{y}\|^{2} \leq\|\boldsymbol{x}\|^{2}+2\|\boldsymbol{x}\|\|\boldsymbol{y}\|+\|\boldsymbol{y}\|^{2}=(\|\boldsymbol{x}\|+\|\boldsymbol{y}\|)^{2} .
$$

Taking square roots completes the proof. $\square$

In the real case the Cauchy-Schwarz inequality implies that $-1 \leq \frac{\langle\boldsymbol{x}, \boldsymbol{y}\rangle}{\|\boldsymbol{x}\|\|\boldsymbol{y}\|} \leq 1$ for nonzero $\boldsymbol{x}$ and $\boldsymbol{y}$, so there is a unique angle $\theta$ in $[0, \pi]$ such that

$$
\cos \theta=\frac{\langle\boldsymbol{x}, \boldsymbol{y}\rangle}{\|\boldsymbol{x}\|\|\boldsymbol{y}\|} .
$$

This defines the angle between vectors in a real inner product space.

### 5.1.2 Orthogonality

Definition 5.2 (Orthogonality) Two vectors $\boldsymbol{x}, \boldsymbol{y}$ in a real or complex inner product space are orthogonal or perpendicular, denoted as $\boldsymbol{x} \perp \boldsymbol{y}$, if $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=0$. The vectors are orthonormal if in addition $\|\boldsymbol{x}\|=\|\boldsymbol{y}\|=1$.

From the definitions (5.6), (5.20) of angle $\theta$ between two nonzero vectors in $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$ it follows that $\boldsymbol{x} \perp \boldsymbol{y}$ if and only if $\theta=\pi / 2$.

Theorem 5.3 (Pythagoras) For a real or complex inner product space

$$
\|\boldsymbol{x}+\boldsymbol{y}\|^{2}=\|\boldsymbol{x}\|^{2}+\|\boldsymbol{y}\|^{2}, \quad \text { if } \quad \boldsymbol{x} \perp \boldsymbol{y} .
$$

Proof We set $a=1$ in (5.5) and use the orthogonality. $\square$

Definition 5.3 (Orthogonal- and Orthonormal Bases) A set of nonzero vectors $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$ in a subspace $\mathcal{S}$ of a real or complex inner product space is an orthogonal basis for $\mathcal{S}$ if it is a basis for $\mathcal{S}$ and $\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{j}\right\rangle=0$ for $i \neq j$. It is an orthonormal basis for $\mathcal{S}$ if it is a basis for $\mathcal{S}$ and $\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{j}\right\rangle=\delta_{i j}$ for all $i, j$.

A basis for a subspace of an inner product space can be turned into an orthogonalor orthonormal basis for the subspace by the following construction (Fig. 5.1).

Fig. 5.1 The construction of $\boldsymbol{v}_{1}$ and $\boldsymbol{v}_{2}$ in Gram-Schmidt. The constant $c$ is given by $c:=\left\langle\boldsymbol{s}_{2}, \boldsymbol{v}_{1}\right\rangle /\left\langle\boldsymbol{v}_{1}, \boldsymbol{v}_{1}\right\rangle$
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-120.jpg?height=360&width=708&top_left_y=227&top_left_x=632)

Theorem 5.4 (Gram-Schmidt) Let $\left\{\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{k}\right\}$ be a basis for a real or complex inner product space $(\mathcal{S},\langle\cdot, \cdot\rangle)$. Define

$$
\boldsymbol{v}_{1}:=\boldsymbol{s}_{1}, \quad \boldsymbol{v}_{j}:=\boldsymbol{s}_{j}-\sum_{i=1}^{j-1} \frac{\left\langle\boldsymbol{s}_{j}, \boldsymbol{v}_{i}\right\rangle}{\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{i}\right\rangle} \boldsymbol{v}_{i}, \quad j=2, \ldots, k .
$$

Then $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$ is an orthogonal basis for $\mathcal{S}$ and the normalized vectors

$$
\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{k}\right\}:=\left\{\frac{\boldsymbol{v}_{1}}{\left\|\boldsymbol{v}_{1}\right\|}, \ldots, \frac{\boldsymbol{v}_{k}}{\left\|\boldsymbol{v}_{k}\right\|}\right\}
$$

form an orthonormal basis for $\mathcal{S}$.
Proof To show that $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$ is an orthogonal basis for $\mathcal{S}$ we use induction on $k$. Define subspaces $S_{j}:=\operatorname{span}\left\{\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{j}\right\}$ for $j=1, \ldots, k$. Clearly $\boldsymbol{v}_{1}=\boldsymbol{s}_{1}$ is an orthogonal basis for $S_{1}$. Suppose for some $j \geq 2$ that $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{j-1}$ is an orthogonal basis for $S_{j-1}$ and let $\boldsymbol{v}_{j}$ be given by (5.8) as a linear combination of $\boldsymbol{s}_{j}$ and $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{j-1}$. Now each of these $\boldsymbol{v}_{i}$ is a linear combination of $\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{i}$, and we obtain $\boldsymbol{v}_{j}=\sum_{i=1}^{j} a_{i} \boldsymbol{s}_{i}$ for some $a_{0}, \ldots, a_{j}$ with $a_{j}=1$. Since $\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{j}$ are linearly independent and $a_{j} \neq 0$ we deduce that $\boldsymbol{v}_{j} \neq 0$. By the induction hypothesis

$$
\left\langle\boldsymbol{v}_{j}, \boldsymbol{v}_{l}\right\rangle=\left\langle\boldsymbol{s}_{j}, \boldsymbol{v}_{l}\right\rangle-\sum_{i=1}^{j-1} \frac{\left\langle\boldsymbol{s}_{j}, \boldsymbol{v}_{i}\right\rangle}{\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{i}\right\rangle}\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{l}\right\rangle=\left\langle\boldsymbol{s}_{j}, \boldsymbol{v}_{l}\right\rangle-\frac{\left\langle\boldsymbol{s}_{j}, \boldsymbol{v}_{l}\right\rangle}{\left\langle\boldsymbol{v}_{l}, \boldsymbol{v}_{l}\right\rangle}\left\langle\boldsymbol{v}_{l}, \boldsymbol{v}_{l}\right\rangle=0
$$

for $l=1, \ldots, j-1$. Thus $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{j}$ is an orthogonal basis for $S_{j}$.
If $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$ is an orthogonal basis for $\mathcal{S}$ then clearly $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{k}\right\}$ is an orthonormal basis for $\mathcal{S}$. $\square$

Sometimes we want to extend an orthogonal basis for a subspace to an orthogonal basis for a larger space.

Theorem 5.5 (Orthogonal Extension of Basis) Suppose $\mathcal{S} \subset \mathcal{T}$ are finite dimensional subspaces of a vector space $\mathcal{V}$. An orthogonal basis for $\mathcal{S}$ can always be extended to an orthogonal basis for $\mathcal{T}$.

Proof Suppose $\operatorname{dim} \mathcal{S}:=k<\operatorname{dim} \mathcal{T}=n$. Using Theorem 1.3 we first extend an orthogonal basis $\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{k}$ for $\mathcal{S}$ to a basis $\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{k}, \boldsymbol{s}_{k+1}, \ldots, \boldsymbol{s}_{n}$ for $\mathcal{T}$, and then apply the Gram-Schmidt process to this basis obtaining an orthogonal basis $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}$ for $\mathcal{T}$. This is an extension of the basis for $\mathcal{S}$ since $\boldsymbol{v}_{i}=\boldsymbol{s}_{i}$ for $i=$ $1, \ldots, k$. We show this by induction. Clearly $\boldsymbol{v}_{1}=\boldsymbol{s}_{1}$. Suppose for some $2 \leq r<k$ that $\boldsymbol{v}_{j}=\boldsymbol{s}_{j}$ for $j=1, \ldots, r-1$. Consider (5.8) for $j=r$. Since $\left\langle\boldsymbol{s}_{r}, \boldsymbol{v}_{i}\right\rangle=$ $\left\langle\boldsymbol{s}_{r}, \boldsymbol{s}_{i}\right\rangle=0$ for $i<r$ we obtain $\boldsymbol{v}_{r}=\boldsymbol{s}_{r}$. $\square$

Letting $\mathcal{S}=\operatorname{span}\left(\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{k}\right)$ and $\mathcal{T}$ be $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$ we obtain
Corollary 5.1 (Extending Orthogonal Vectors to a Basis) For $1 \leq k<n$ a set $\left\{\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{k}\right\}$ of nonzero orthogonal vectors in $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$ can be extended to an orthogonal basis for the whole space.

### 5.1.3 Sum of Subspaces and Orthogonal Projections

Suppose $\mathcal{S}$ and $\mathcal{T}$ are subspaces of a real or complex vector space $\mathcal{V}$ endowed with an inner product $\langle\boldsymbol{x}, \boldsymbol{y}\rangle$. We define

- Sum: $\mathcal{S}+\mathcal{T}:=\{\boldsymbol{s}+\boldsymbol{t}: \boldsymbol{s} \in \mathcal{S}$ and $\boldsymbol{t} \in \mathcal{T}\}$,
- direct $\boldsymbol{\operatorname { s u m }} \mathcal{S} \oplus \mathcal{T}$ : a sum where $\mathcal{S} \cap \mathcal{T}=\{\mathbf{0}\}$,
- orthogonal sum $\mathcal{S} \stackrel{\perp}{\oplus} \mathcal{T}$ : a sum where $\langle\boldsymbol{s}, \boldsymbol{t}\rangle=0$ for all $\boldsymbol{s} \in \mathcal{S}$ and $\boldsymbol{t} \in \mathcal{T}$.

We note that

- $\mathcal{S}+\mathcal{T}$ is a vector space, a subspace of $\mathcal{V}$ which in this book will be $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$ (cf. Example 1.2).
- Every $\boldsymbol{v} \in \mathcal{S} \oplus \mathcal{T}$ can be decomposed uniquely in the form $\boldsymbol{v}=\boldsymbol{s}+\boldsymbol{t}$, where $\boldsymbol{s} \in \mathcal{S}$ and $\boldsymbol{t} \in \mathcal{T}$. For if $\boldsymbol{v}=\boldsymbol{s}_{1}+\boldsymbol{t}_{1}=\boldsymbol{s}_{2}+\boldsymbol{t}_{2}$ for $\boldsymbol{s}_{1}, \boldsymbol{s}_{2} \in \mathcal{S}$ and $\boldsymbol{t}_{1}, \boldsymbol{t}_{2} \in \mathcal{T}$, then $\mathbf{0}=\boldsymbol{s}_{1}-\boldsymbol{s}_{2}+\boldsymbol{t}_{1}-\boldsymbol{t}_{2}$ or $\boldsymbol{s}_{1}-\boldsymbol{s}_{2}=\boldsymbol{t}_{2}-\boldsymbol{t}_{1}$. It follows that $\boldsymbol{s}_{1}-\boldsymbol{s}_{2}$ and $\boldsymbol{t}_{2}-\boldsymbol{t}_{1}$ belong to both $\mathcal{S}$ and $\mathcal{T}$ and hence to $\mathcal{S} \cap \mathcal{T}$. But then $\boldsymbol{s}_{1}-\boldsymbol{s}_{2}=\boldsymbol{t}_{2}-\boldsymbol{t}_{1}=\mathbf{0}$ so $\boldsymbol{s}_{1}=\boldsymbol{s}_{2}$ and $\boldsymbol{t}_{2}=\boldsymbol{t}_{1}$.
By (1.8) in the introduction chapter we have
$$
\operatorname{dim}(\mathcal{S} \oplus \mathcal{T})=\operatorname{dim}(\mathcal{S})+\operatorname{dim}(\mathcal{T}) .
$$
The subspaces $\mathcal{S}$ and $\mathcal{T}$ in a direct sum are called complementary subspaces.
- An orthogonal sum is a direct sum. For if $\boldsymbol{v} \in \mathcal{S} \cap \mathcal{T}$ then $\boldsymbol{v}$ is orthogonal to itself, $\langle\boldsymbol{v}, \boldsymbol{v}\rangle=0$, which implies that $\boldsymbol{v}=0$. We often write $\mathcal{T}:=\mathcal{S}^{\perp}$.
- Suppose $\boldsymbol{v}=\boldsymbol{s}_{0}+\boldsymbol{t}_{0} \in \mathcal{S} \oplus \mathcal{T}$, where $\boldsymbol{s}_{0} \in \mathcal{S}$ and $\boldsymbol{t}_{0} \in \mathcal{T}$. The vector $\boldsymbol{s}_{0}$ is called the oblique projection of $\boldsymbol{v}$ into $\mathcal{S}$ along $\mathcal{T}$. Similarly, The vector $\boldsymbol{t}_{0}$ is

Fig. 5.2 The orthogonal projections of $\boldsymbol{s}+\boldsymbol{t}$ into $\mathcal{S}$ and $\mathcal{T}$
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-122.jpg?height=438&width=638&top_left_y=213&top_left_x=704)

called the oblique projection of $\boldsymbol{v}$ into $\mathcal{T}$ along $\mathcal{S}$. If $\mathcal{S} \stackrel{\perp}{\oplus} \mathcal{T}$ is an orthogonal sum then $\boldsymbol{s}_{0}$ is called the orthogonal projection of $\boldsymbol{v}$ into $\mathcal{S}$. Similarly, $\boldsymbol{t}_{0}$ is called the orthogonal projection of $\boldsymbol{v}$ in $\mathcal{T}=\mathcal{S}^{\perp}$. The orthogonal projections are illustrated in Fig. 5.2.

Theorem 5.6 (Orthogonal Projection) Let $\mathcal{S}$ and $\mathcal{T}$ be subspaces of a finite dimensional real or complex vector space $\mathcal{V}$ with an inner product $\langle\cdot, \cdot\rangle$. The orthogonal projections $\boldsymbol{s}_{0}$ of $\boldsymbol{v} \in \mathcal{S} \stackrel{\perp}{\oplus} \mathcal{T}$ into $\mathcal{S}$ and $\boldsymbol{t}_{0}$ of $\boldsymbol{v} \in \mathcal{S} \stackrel{\perp}{\oplus} \mathcal{T}$ into $\mathcal{T}$ satisfy $\boldsymbol{v}=\boldsymbol{s}_{0}+\boldsymbol{t}_{0}$, and

$$
\left\langle\boldsymbol{s}_{0}, \boldsymbol{s}\right\rangle=\langle\boldsymbol{v}, \boldsymbol{s}\rangle, \quad \text { for all } \boldsymbol{s} \in \mathcal{S}, \quad\left\langle\boldsymbol{t}_{0}, \boldsymbol{t}\right\rangle=\langle\boldsymbol{v}, \boldsymbol{t}\rangle, \quad \text { for all } \boldsymbol{t} \in \mathcal{T} .
$$

Moreover, if $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}\right\}$ is an orthogonal basis for $\boldsymbol{S}$ then

$$
\boldsymbol{s}_{0}=\sum_{i=1}^{k} \frac{\left\langle\boldsymbol{v}, \boldsymbol{v}_{i}\right\rangle}{\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{i}\right\rangle} \boldsymbol{v}_{i} .
$$

Proof We have $\left\langle\boldsymbol{s}_{0}, \boldsymbol{s}\right\rangle=\left\langle\boldsymbol{v}-\boldsymbol{t}_{0}, \boldsymbol{s}\right\rangle=\langle\boldsymbol{v}, \boldsymbol{s}\rangle$, since $\left\langle\boldsymbol{t}_{0}, \boldsymbol{s}\right\rangle=0$ for all $\boldsymbol{s} \in \mathcal{S}$ and (5.9) follows. If $\boldsymbol{s}_{0}$ is given by (5.10) then for $j=1, \ldots, k$

$$
\left\langle\boldsymbol{s}_{0}, \boldsymbol{v}_{j}\right\rangle=\left\langle\sum_{i=1}^{k} \frac{\left\langle\boldsymbol{v}, \boldsymbol{v}_{i}\right\rangle}{\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{i}\right\rangle} \boldsymbol{v}_{i}, \boldsymbol{v}_{j}\right\rangle=\sum_{i=1}^{k} \frac{\left\langle\boldsymbol{v}, \boldsymbol{v}_{i}\right\rangle}{\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{i}\right\rangle}\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{j}\right\rangle=\left\langle\boldsymbol{v}, \boldsymbol{v}_{j}\right\rangle .
$$

By linearity (5.9) holds for all $\boldsymbol{s} \in \mathcal{S}$. By uniqueness it must be the orthogonal projections of $\boldsymbol{v} \in \mathcal{S} \stackrel{\perp}{\oplus} \mathcal{T}$ into $\mathcal{S}$. The proof for $\boldsymbol{t}_{0}$ is similar. $\square$

Corollary 5.2 (Best Approximation) Let $\mathcal{S}$ be a subspaces of a finite dimensional real or complex vector space $\mathcal{V}$ with an inner product $\langle\cdot, \cdot\rangle$ and corresponding norm $\|\boldsymbol{v}\|:=\sqrt{\langle\boldsymbol{v}, \boldsymbol{v}\rangle}$. If $\boldsymbol{s}_{0} \in \mathcal{S}$ is the orthogonal projection of $\boldsymbol{v} \in \mathcal{V}$ then

$$
\left\|\boldsymbol{v}-\boldsymbol{s}_{0}\right\|<\|\boldsymbol{v}-\boldsymbol{s}\|, \text { for all } \boldsymbol{s} \in \mathcal{S}, \boldsymbol{s} \neq \boldsymbol{s}_{0} .
$$

Proof Let $s_{0} \neq s \in \mathcal{S}$ and $0 \neq \boldsymbol{u}:=s_{0}-s \in \mathcal{S}$. It follows from (5.9) that $\left\langle\boldsymbol{v}-\boldsymbol{s}_{0}, \boldsymbol{u}\right\rangle=0$. By (5.7) (Pythagoras) we obtain

$$
\|\boldsymbol{v}-\boldsymbol{s}\|^{2}=\left\|\boldsymbol{v}-\boldsymbol{s}_{0}+\boldsymbol{u}\right\|^{2}=\left\|\boldsymbol{v}-\boldsymbol{s}_{0}\right\|^{2}+\|\boldsymbol{u}\|^{2}>\left\|\boldsymbol{v}-\boldsymbol{s}_{0}\right\|^{2} .
$$ $\square$

### 5.1.4 Unitary and Orthogonal Matrices

In the rest of this chapter orthogonality is in terms of the standard inner product in $\mathbb{C}^{n}$ given by $\langle\boldsymbol{x}, \boldsymbol{y}\rangle:=\boldsymbol{y}^{*} \boldsymbol{x}=\sum_{j=1}^{n} x_{j} \overline{y_{j}}$. For symmetric and Hermitian matrices we have the following characterization.

Lemma 5.1 Let $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ and $\langle\boldsymbol{x}, \boldsymbol{y}\rangle$ be the standard inner product in $\mathbb{C}^{n}$. Then

1. $\boldsymbol{A}^{T}=\boldsymbol{A} \Longleftrightarrow\langle\boldsymbol{A} \boldsymbol{x}, \boldsymbol{y}\rangle=\langle\boldsymbol{x}, \overline{\boldsymbol{A}} \boldsymbol{y}\rangle$ for all $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$.
2. $\boldsymbol{A}^{*}=\boldsymbol{A} \Longleftrightarrow\langle\boldsymbol{A} \boldsymbol{x}, \boldsymbol{y}\rangle=\langle\boldsymbol{x}, \boldsymbol{A} \boldsymbol{y}\rangle$ for all $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$.

Proof Suppose $\boldsymbol{A}^{T}=\boldsymbol{A}$ and $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$. Then

$$
\langle\boldsymbol{x}, \overline{\boldsymbol{A}} \boldsymbol{y}\rangle=(\overline{\boldsymbol{A}} \boldsymbol{y})^{*} \boldsymbol{x}=\boldsymbol{y}^{*} \overline{\boldsymbol{A}}^{*} \boldsymbol{x}=\boldsymbol{y}^{*} \boldsymbol{A}^{T} \boldsymbol{x}=\boldsymbol{y}^{*} \boldsymbol{A} \boldsymbol{x}=\langle\boldsymbol{A} \boldsymbol{x}, \boldsymbol{y}\rangle .
$$

For the converse we take $\boldsymbol{x}=\boldsymbol{e}_{j}$ and $\boldsymbol{y}=\boldsymbol{e}_{i}$ for some $i, j$ and obtain

$$
\boldsymbol{e}_{i}^{T} \boldsymbol{A} \boldsymbol{e}_{j}=\left\langle\boldsymbol{A} \boldsymbol{e}_{j}, \boldsymbol{e}_{i}\right\rangle=\left\langle\boldsymbol{e}_{j}, \overline{\boldsymbol{A}} \boldsymbol{e}_{i}\right\rangle=\boldsymbol{e}_{i}^{T} \boldsymbol{A}^{T} \boldsymbol{e}_{j} .
$$

Thus, $\boldsymbol{A}=\boldsymbol{A}^{T}$ since they have the same $i, j$ element for all $i, j$. The proof of 2. is similar. $\square$

A square matrix $\boldsymbol{U} \in \mathbb{C}^{n \times n}$ is unitary if $\boldsymbol{U}^{*} \boldsymbol{U}=\boldsymbol{I}$. If $\boldsymbol{U}$ is real then $\boldsymbol{U}^{T} \boldsymbol{U}=$ $\boldsymbol{I}$ and $\boldsymbol{U}$ is called an orthogonal matrix. Unitary and orthogonal matrices have orthonormal columns.

If $\boldsymbol{U}^{*} \boldsymbol{U}=\boldsymbol{I}$ the matrix $\boldsymbol{U}$ is nonsingular, $\boldsymbol{U}^{-1}=\boldsymbol{U}^{*}$ and therefore $\boldsymbol{U} \boldsymbol{U}^{*}=$ $\boldsymbol{U} \boldsymbol{U}^{-1}=\boldsymbol{I}$ as well. Moreover, both the columns and rows of a unitary matrix of order $n$ form orthonormal bases for $\mathbb{C}^{n}$. We also note that the product of two unitary matrices is unitary. Indeed, if $\boldsymbol{U}_{1}^{*} \boldsymbol{U}_{1}=\boldsymbol{I}$ and $\boldsymbol{U}_{2}^{*} \boldsymbol{U}_{2}=\boldsymbol{I}$ then $\left(\boldsymbol{U}_{1} \boldsymbol{U}_{2}\right)^{*}\left(\boldsymbol{U}_{1} \boldsymbol{U}_{2}\right)=$ $\boldsymbol{U}_{2}^{*} \boldsymbol{U}_{1}^{*} \boldsymbol{U}_{1} \boldsymbol{U}_{2}=\boldsymbol{I}$.

Theorem 5.7 (Unitary Matrix) The matrix $\boldsymbol{U} \in \mathbb{C}^{n \times n}$ is unitary if and only if $\langle\boldsymbol{U} \boldsymbol{x}, \boldsymbol{U} \boldsymbol{y}\rangle=\langle\boldsymbol{x}, \boldsymbol{y}\rangle$ for all $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$. In particular, if $\boldsymbol{U}$ is unitary then $\|\boldsymbol{U} \boldsymbol{x}\|_{2}=$ $\|\boldsymbol{x}\|_{2}$ for all $\boldsymbol{x} \in \mathbb{C}^{n}$.

Proof If $\boldsymbol{U}^{*} \boldsymbol{U}=\boldsymbol{I}$ and $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ then

$$
\langle U x, U y\rangle=(U y)^{*}(U x)=y^{*} U^{*} U x=y^{*} x=\langle x, y\rangle .
$$

Conversely, if $\langle\boldsymbol{U} \boldsymbol{x}, \boldsymbol{U} \boldsymbol{y}\rangle=\langle\boldsymbol{x}, \boldsymbol{y}\rangle$ for all $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ then $\boldsymbol{U}^{*} \boldsymbol{U}=\boldsymbol{I}$ since for $i, j=1, \ldots, n$

$$
\left(\boldsymbol{U}^{*} \boldsymbol{U}\right)_{i, j}=\boldsymbol{e}_{i}^{*} \boldsymbol{U}^{*} \boldsymbol{U} \boldsymbol{e}_{j}=\left(\boldsymbol{U} \boldsymbol{e}_{i}\right)^{*}\left(\boldsymbol{U} \boldsymbol{e}_{j}\right)=\left\langle\boldsymbol{U} \boldsymbol{e}_{j}, \boldsymbol{U} \boldsymbol{e}_{i}\right\rangle=\left\langle\boldsymbol{e}_{j}, \boldsymbol{e}_{i}\right\rangle=\boldsymbol{e}_{i}^{*} \boldsymbol{e}_{j},
$$

so that $\left(\boldsymbol{U}^{*} \boldsymbol{U}\right)_{i, j}=\delta_{i, j}$ for all $i, j$. The last part of the theorem follows immediately by taking $\boldsymbol{y}=\boldsymbol{x}$ : $\square$

### 5.2 The Householder Transformation

We consider a unitary matrix with many useful properties.
Definition 5.4 (Householder Transformation) A matrix $\boldsymbol{H} \in \mathbb{C}^{n \times n}$ of the form

$$
\boldsymbol{H}:=\boldsymbol{I}-\boldsymbol{u} \boldsymbol{u}^{*}, \text { where } \boldsymbol{u} \in \mathbb{C}^{n} \text { and } \boldsymbol{u}^{*} \boldsymbol{u}=2
$$

is called a Householder transformation. The name elementary reflector is also used.

In the real case and for $n=2$ we find

$$
\boldsymbol{H}=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]-\left[\begin{array}{l}
u_{1} \\
u_{2}
\end{array}\right]\left[\begin{array}{ll}
u_{1} & u_{2}
\end{array}\right]=\left[\begin{array}{cc}
1-u_{1}^{2} & -u_{1} u_{2} \\
-u_{2} u_{1} & 1-u_{2}^{2}
\end{array}\right] .
$$

A Householder transformation is Hermitian and unitary. Indeed, $\boldsymbol{H}^{*}=(\boldsymbol{I}-$ $\left.\boldsymbol{u} \boldsymbol{u}^{*}\right)^{*}=\boldsymbol{H}$ and

$$
\boldsymbol{H}^{*} \boldsymbol{H}=\boldsymbol{H}^{2}=\left(\boldsymbol{I}-\boldsymbol{u} \boldsymbol{u}^{*}\right)\left(\boldsymbol{I}-\boldsymbol{u} \boldsymbol{u}^{*}\right)=\boldsymbol{I}-2 \boldsymbol{u} \boldsymbol{u}^{*}+\boldsymbol{u}\left(\boldsymbol{u}^{*} \boldsymbol{u}\right) \boldsymbol{u}^{*}=\boldsymbol{I} .
$$

In the real case $\boldsymbol{H}$ is symmetric and orthogonal.
There are several ways to represent a Householder transformation. Householder used $\boldsymbol{I}-2 \boldsymbol{u} \boldsymbol{u}^{*}$, where $\boldsymbol{u}^{*} \boldsymbol{u}=1$. For any nonzero $\boldsymbol{v} \in \mathbb{C}^{n}$ the matrix

$$
\boldsymbol{H}:=\boldsymbol{I}-2 \frac{\boldsymbol{v} \boldsymbol{v}^{*}}{\boldsymbol{v}^{*} \boldsymbol{v}}
$$

is a Householder transformation. Indeed, $\boldsymbol{H}=\boldsymbol{I}-\boldsymbol{u} \boldsymbol{u}^{*}$, where $\boldsymbol{u}:=\sqrt{2} \frac{\boldsymbol{v}}{\|\boldsymbol{v}\|_{2}}$ has length $\sqrt{2}$.

Two vectors can, under certain conditions, be mapped into each other by a Householder transformation.

Lemma 5.2 Suppose $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ are two vectors such that $\|\boldsymbol{x}\|_{2}=\|\boldsymbol{y}\|_{2}, \boldsymbol{y}^{*} \boldsymbol{x}$ is real and $\boldsymbol{v}:=\boldsymbol{x}-\boldsymbol{y} \neq \mathbf{0}$. Then $\left(\boldsymbol{I}-2 \frac{\boldsymbol{v} \boldsymbol{v}^{*}}{\boldsymbol{v}^{*} \boldsymbol{v}}\right) \boldsymbol{x}=\boldsymbol{y}$.

Proof Since $\boldsymbol{x}^{*} \boldsymbol{x}=\boldsymbol{y}^{*} \boldsymbol{y}$ and $\operatorname{Re}\left(\boldsymbol{y}^{*} \boldsymbol{x}\right)=\boldsymbol{y}^{*} \boldsymbol{x}$ we have

$$
\boldsymbol{v}^{*} \boldsymbol{v}=(\boldsymbol{x}-\boldsymbol{y})^{*}(\boldsymbol{x}-\boldsymbol{y})=2 \boldsymbol{x}^{*} \boldsymbol{x}-2 \operatorname{Re}\left(\boldsymbol{y}^{*} \boldsymbol{x}\right)=2 \boldsymbol{v}^{*} \boldsymbol{x} .
$$

But then $\left(\boldsymbol{I}-2 \frac{\boldsymbol{v} \boldsymbol{v}^{*}}{\boldsymbol{v}^{*} \boldsymbol{v}}\right) \boldsymbol{x}=\boldsymbol{x}-\frac{2 \boldsymbol{v}^{*} \boldsymbol{x}}{\boldsymbol{v}^{*} \boldsymbol{v}} \boldsymbol{v}=\boldsymbol{x}-\boldsymbol{v}=\boldsymbol{y}$. $\square$

There is a nice geometric interpretation of this Lemma. We have

$$
\boldsymbol{H}=\boldsymbol{I}-\frac{2 \boldsymbol{v} \boldsymbol{v}^{*}}{\boldsymbol{v}^{*} \boldsymbol{v}}=\boldsymbol{P}-\frac{\boldsymbol{v} \boldsymbol{v}^{*}}{\boldsymbol{v}^{*} \boldsymbol{v}}, \text { where } \boldsymbol{P}:=\boldsymbol{I}-\frac{\boldsymbol{v} \boldsymbol{v}^{*}}{\boldsymbol{v}^{*} \boldsymbol{v}},
$$

and

$$
\boldsymbol{P} \boldsymbol{x}=\boldsymbol{x}-\frac{\boldsymbol{v}^{*} \boldsymbol{x}}{\boldsymbol{v}^{*} \boldsymbol{v}} \boldsymbol{v} \stackrel{(5.13)}{=} \boldsymbol{x}-\frac{1}{2} \boldsymbol{v}=\frac{1}{2}(\boldsymbol{x}+\boldsymbol{y}) .
$$

If $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$ it follows that $\boldsymbol{H} \boldsymbol{x}$ is the reflected image of $\boldsymbol{x}$. The "mirror" $\mathcal{M}:=$ $\left\{\boldsymbol{w} \in \mathbb{R}^{n}: \boldsymbol{w}^{*} \boldsymbol{v}=0\right\}$ contains the vector $(\boldsymbol{x}+\boldsymbol{y}) / 2$ and has normal $\boldsymbol{x}-\boldsymbol{y}$. This is illustrated for the real case in Fig. 5.3.

Fig. 5.3 The Householder transformation in Example 5.1
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-125.jpg?height=586&width=680&top_left_y=1348&top_left_x=664)

Example 5.1 (Reflector) Suppose $\boldsymbol{x}:=[1,0,1]^{T}$ and $\boldsymbol{y}:=[-1,0,1]^{T}$. Then $\boldsymbol{v}=$ $\boldsymbol{x}-\boldsymbol{y}=[2,0,0]^{T}$ and

$$
\begin{gathered}
\boldsymbol{H}:=\boldsymbol{I}-\frac{2 \boldsymbol{v} \boldsymbol{v}^{T}}{\boldsymbol{v}^{T} \boldsymbol{v}}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]-\frac{2}{4}\left[\begin{array}{l}
2 \\
0 \\
0
\end{array}\right]\left[\begin{array}{lll}
2 & 0 & 0
\end{array}\right]=\left[\begin{array}{ccc}
-1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right], \\
\boldsymbol{P}:=\boldsymbol{I}-\frac{\boldsymbol{v} \boldsymbol{v}^{T}}{\boldsymbol{v}^{T} \boldsymbol{v}}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]-\frac{1}{4}\left[\begin{array}{l}
2 \\
0 \\
0
\end{array}\right]\left[\begin{array}{lll}
2 & 0 & 0
\end{array}\right]=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] .
\end{gathered}
$$

The set

$$
\mathcal{M}:=\left\{\boldsymbol{w} \in \mathbb{R}^{3}: \boldsymbol{w}^{T} \boldsymbol{v}=0\right\}=\left\{\left[\begin{array}{l}
w_{1} \\
w_{2} \\
w_{3}
\end{array}\right]: 2 w_{1}=0\right\}
$$

is the $y z$ plane (cf. Fig. 5.3), $\boldsymbol{H} \boldsymbol{x}=[-1,0,1]^{T}=\boldsymbol{y}$, and $\boldsymbol{P} \boldsymbol{x}=[0,0,1]^{T}=$ $(\boldsymbol{x}+\boldsymbol{y}) / 2 \in \mathcal{M}$.

Householder transformations can be used to produce zeros in vectors. In the following Theorem we map any vector in $\mathbb{C}^{n}$ into a multiple of the first unit vector.

Theorem 5.8 (Zeros in Vectors) For any $\boldsymbol{x} \in \mathbb{C}^{n}$ there is a Householder transformation $\boldsymbol{H} \in \mathbb{C}^{n \times n}$ such that

$$
\boldsymbol{H} \boldsymbol{x}=a \boldsymbol{e}_{1}, \quad a=-\rho\|\boldsymbol{x}\|_{2}, \quad \rho:= \begin{cases}x_{1} /\left|x_{1}\right|, & \text { if } x_{1} \neq 0, \\ 1, & \text { otherwise } .\end{cases}
$$

Proof If $\boldsymbol{x}=0$ then $\boldsymbol{H} \boldsymbol{x}=\mathbf{0}$ and $a=0$. Any $\boldsymbol{u}$ with $\|\boldsymbol{u}\|_{2}=\sqrt{2}$ will work, and we choose $\boldsymbol{u}:=\sqrt{2} \boldsymbol{e}_{1}$ in this case. For $\boldsymbol{x} \neq \mathbf{0}$ we define

$$
\boldsymbol{u}:=\frac{\boldsymbol{z}+\boldsymbol{e}_{1}}{\sqrt{1+z_{1}}}, \text { where } \boldsymbol{z}:=\bar{\rho} \boldsymbol{x} /\|\boldsymbol{x}\|_{2} .
$$

Since $|\rho|=1$ we have $\rho\|\boldsymbol{x}\|_{2} \boldsymbol{z}=|\rho|^{2} \boldsymbol{x}=\boldsymbol{x}$. Moreover, $\|\boldsymbol{z}\|_{2}=1$ and $z_{1}=$ $\left|x_{1}\right| /\|\boldsymbol{x}\|_{2}$ is real so that $\boldsymbol{u}^{*} \boldsymbol{u}=\frac{\left(z+\boldsymbol{e}_{1}\right)^{*}\left(z+\boldsymbol{e}_{1}\right)}{1+z_{1}}=\frac{2+2 z_{1}}{1+z_{1}}=2$. Finally,

$$
\begin{aligned}
\boldsymbol{H} \boldsymbol{x} & =\boldsymbol{x}-\left(\boldsymbol{u}^{*} \boldsymbol{x}\right) \boldsymbol{u}=\rho\|\boldsymbol{x}\|_{2}\left(\boldsymbol{z}-\left(\boldsymbol{u}^{*} \boldsymbol{z}\right) \boldsymbol{u}\right)=\rho\|\boldsymbol{x}\|_{2}\left(z-\frac{\left(z^{*}+\boldsymbol{e}_{1}^{*}\right) \boldsymbol{z}}{1+z_{1}}\left(z+\boldsymbol{e}_{1}\right)\right) \\
& =\rho\|\boldsymbol{x}\|_{2}\left(z-\left(z+\boldsymbol{e}_{1}\right)\right)=-\rho\|\boldsymbol{x}\|_{2} \boldsymbol{e}_{1}=a \boldsymbol{e}_{1}
\end{aligned}
$$ $\square$

The formulas in Theorem 5.8 are implemented in the following algorithm adapted from [17]. To any given $\boldsymbol{x} \in \mathbb{C}^{n}$, a number $a$ and a vector $\boldsymbol{u}$ with $\boldsymbol{u}^{*} \boldsymbol{u}=2$ is computed so that $\left(\boldsymbol{I}-\boldsymbol{u u}^{*}\right) \boldsymbol{x}=a \boldsymbol{e}_{1}$ :

```
function [u,a]=housegen(x)
% [u,a]=housegen (x)
a=norm(x);
if a==0
    u=x; u(1)=sqrt(2); return;
end
if x(1)== 0
    r=1;
else
    r=x(1)/abs(x(1));
end
u=conj (r) *x/a;
u(1) =u(1) +1;
u=u/sqrt(u(1));
a=-r*a;
end
```

Listing 5.1 housegen

Note that

- In Theorem 5.8 the first component of $\boldsymbol{z}$ is $z_{1}=\left|x_{1}\right| /\|\boldsymbol{x}\|_{2} \geq 0$. Since $\|\boldsymbol{z}\|_{2}=$ 1 we have $1 \leq 1+z_{1} \leq 2$. It follows that we avoid cancelation error when computing $1+z_{1}$ and $\boldsymbol{u}$ and $a$ are computed in a numerically stable way.
- In order to compute $\boldsymbol{H} \boldsymbol{x}$ for a vector $\boldsymbol{x}$ we do not need to form the matrix $\boldsymbol{H}$. Indeed, $\boldsymbol{H} \boldsymbol{x}=\left(\boldsymbol{I}-\boldsymbol{u} \boldsymbol{u}^{*}\right) \boldsymbol{x}=\boldsymbol{x}-\left(\boldsymbol{u}^{*} \boldsymbol{x}\right) \boldsymbol{u}$. If $\boldsymbol{u}, \boldsymbol{x} \in \mathbb{R}^{m}$ this requires $2 m$ operations to find $\boldsymbol{u}^{T} \boldsymbol{x}, m$ operations for $\left(\boldsymbol{u}^{T} \boldsymbol{x}\right) \boldsymbol{u}$ and $m$ operations for the final subtraction of the two vectors, a total of $4 m$ arithmetic operations. If $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ then $4 m n$ operations are required for $\boldsymbol{H} \boldsymbol{A}=\boldsymbol{A}-\left(\boldsymbol{u}^{T} \boldsymbol{A}\right) \boldsymbol{u}$, i.e., $4 m$ operations for each of the $n$ columns of $\boldsymbol{A}$.
- Householder transformations can also be used to zero out only the lower part of a vector. Suppose $\boldsymbol{x}^{T}:=[\boldsymbol{y}, \boldsymbol{z}]^{T}$, where $\boldsymbol{y} \in \mathbb{C}^{k}, \boldsymbol{z} \in \mathbb{C}^{n-k}$ for some $1 \leq k<$ $n$. The command $[\hat{\boldsymbol{u}}, a]:=\operatorname{housegen}(\boldsymbol{z})$ defines a Householder transformation $\hat{\boldsymbol{H}}=\boldsymbol{I}-\hat{\boldsymbol{u}} \hat{\boldsymbol{u}}^{*}$ so that $\hat{\boldsymbol{H}} z=a \boldsymbol{e}_{1} \in \mathbb{C}^{n-k}$. With $\boldsymbol{u}:=\left[\begin{array}{c}\mathbf{0} \\ \hat{\boldsymbol{u}}\end{array}\right] \in \mathbb{C}^{n}$ we see that $\boldsymbol{u}^{*} \boldsymbol{u}=\hat{\boldsymbol{u}}^{*} \hat{\boldsymbol{u}}=2$, and
$$
\boldsymbol{H} \boldsymbol{x}=\left[\begin{array}{c}
\boldsymbol{y} \\
a \boldsymbol{e}_{1}
\end{array}\right], \text { where } \boldsymbol{H}:=\boldsymbol{I}-\boldsymbol{u} \boldsymbol{u}^{*}=\left[\begin{array}{cc}
\boldsymbol{I} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{I}
\end{array}\right]-\left[\begin{array}{c}
\mathbf{0} \\
\hat{\boldsymbol{u}}
\end{array}\right]\left[\begin{array}{ll}
\mathbf{0} & \hat{\boldsymbol{u}}^{*}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{I} & \mathbf{0} \\
\mathbf{0} & \hat{\boldsymbol{H}}
\end{array}\right],
$$
defines a Householder transformation that produces zeros in the lower part of $\boldsymbol{x}$.

### 5.3 Householder Triangulation

We say that a matrix $\boldsymbol{R} \in \mathbb{C}^{m \times n}$ is upper trapezoidal, if $r_{i, j}=0$ for $j<i$ and $i=2,3 \ldots, m$. Upper trapezoidal matrices corresponding to $m<n, m=n$, and $m>n$ look as follows:

$$
\left[\begin{array}{cccc}
x & x & x & x \\
0 & x & x & x \\
0 & 0 & x & x
\end{array}\right], \quad\left[\begin{array}{cccc}
x & x & x & x \\
0 & x & x & x \\
0 & 0 & x & x \\
0 & 0 & 0 & x
\end{array}\right], \quad\left[\begin{array}{ccc}
x & x & x \\
0 & x & x \\
0 & 0 & x \\
0 & 0 & 0
\end{array}\right] .
$$

In this section we consider a method for bringing a matrix to upper trapezoidal form using Householder transformations.

### 5.3.1 The Algorithm

We treat the cases $m>n$ and $m \leq n$ separately and consider first $m>n$. We describe how to find a sequence $\boldsymbol{H}_{1}, \ldots, \boldsymbol{H}_{n}$ of Householder transformations such that

$$
\boldsymbol{A}_{n+1}:=\boldsymbol{H}_{n} \boldsymbol{H}_{n-1} \cdots \boldsymbol{H}_{1} \boldsymbol{A}=\left[\begin{array}{c}
\boldsymbol{R}_{1} \\
\mathbf{0}
\end{array}\right]=\boldsymbol{R},
$$

and where $\boldsymbol{R}_{1}$ is square and upper triangular. We define

$$
\boldsymbol{A}_{1}:=\boldsymbol{A}, \quad \boldsymbol{A}_{k+1}=\boldsymbol{H}_{k} \boldsymbol{A}_{k}, \quad k=1,2, \ldots, n .
$$

Suppose $\boldsymbol{A}_{k}$ has the following form

$$
\begin{aligned}
\boldsymbol{A}_{k} & =\left[\begin{array}{ccc|ccccc}
a_{1,1}^{(1)} & \cdots & a_{1, k-1}^{(1)} & a_{1, k}^{(1)} & \cdots & a_{1, j}^{(1)} & \cdots & a_{1, n}^{(1)} \\
& \ddots & \vdots & \vdots & & \vdots & & \vdots \\
& & a_{k-1, k-1}^{(k-1)} & a_{k-1, k}^{(k-1)} & \cdots & a_{k-1, j}^{(k-1)} & \cdots & a_{k-1, n}^{(k-1)} \\
\hline & & & a_{k, k}^{(k)} & \cdots & a_{k, j}^{(k)} & \cdots & a_{k, n}^{(k)} \\
& & & \vdots & & \vdots & & \vdots \\
& & & a_{i, k}^{(k)} & \cdots & a_{i, j}^{(k)} & \cdots & a_{i, n}^{(k)} \\
& & & \vdots & & \vdots & & \vdots \\
& & & a_{m, k}^{(k)} & \cdots & a_{m, j}^{(k)} & \cdots & a_{m, n}^{(k)}
\end{array}\right] \\
& =\left[\begin{array}{cc}
\boldsymbol{B}_{k} & \boldsymbol{C}_{k} \\
\mathbf{0} & \boldsymbol{D}_{k}
\end{array}\right] .
\end{aligned}
$$

Thus $\boldsymbol{A}_{k}$ is upper trapezoidal in its first $k-1$ columns (which is true for $k=1$ ).

Let $\hat{\boldsymbol{H}}_{k}:=\boldsymbol{I}-\hat{\boldsymbol{u}}_{k} \hat{\boldsymbol{u}}_{k}^{*}$ be a Householder transformation that maps the first column $\left[a_{k, k}^{(k)}, \ldots, a_{m, k}^{(k)}\right]^{T}$ of $\boldsymbol{D}_{k}$ to a multiple of $\boldsymbol{e}_{1}, \hat{\boldsymbol{H}}_{k}\left(\boldsymbol{D}_{k} \boldsymbol{e}_{1}\right)=a_{k} \boldsymbol{e}_{1}$. Using Algorithm 5.1 we have $\left[\hat{\boldsymbol{u}}_{k}, a_{k}\right]=\operatorname{housegen}\left(\boldsymbol{D}_{k} \boldsymbol{e}_{1}\right)$. Then $\boldsymbol{H}_{k}:=\left[\begin{array}{cc}\boldsymbol{I}_{k-1} & \mathbf{0} \\ \mathbf{0} & \hat{\boldsymbol{H}}_{k}\end{array}\right]$ is a Householder transformation and

$$
\boldsymbol{A}_{k+1}:=\boldsymbol{H}_{k} \boldsymbol{A}_{k}=\left[\begin{array}{cc}
\boldsymbol{B}_{k} & \boldsymbol{C}_{k} \\
\mathbf{0} & \hat{\boldsymbol{H}}_{k} \boldsymbol{D}_{k}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{B}_{k+1} & \boldsymbol{C}_{k+1} \\
\mathbf{0} & \boldsymbol{D}_{k+1}
\end{array}\right],
$$

where $\boldsymbol{B}_{k+1} \in \mathbb{C}^{k \times k}$ is upper triangular and $\boldsymbol{D}_{k+1} \in \mathbb{C}^{(m-k) \times(n-k)}$. Thus $\boldsymbol{A}_{k+1}$ is upper trapezoidal in its first $k$ columns and the reduction has been carried one step further. At the end $\boldsymbol{R}:=\boldsymbol{A}_{n+1}=\left[\begin{array}{c}\boldsymbol{R}_{1} \\ \mathbf{0}\end{array}\right]$, where $\boldsymbol{R}_{1}$ is upper triangular.

The process can also be applied to $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ if $m \leq n$. If $m=1$ then $\boldsymbol{A}$ is already in upper trapezoidal form. Suppose $m>1$. In this case $m-1$ Householder transformations will suffice and $\boldsymbol{H}_{m-1} \cdots \boldsymbol{H}_{1} \boldsymbol{A}$ is upper trapezoidal.

In an algorithm we can store most of the vector $\hat{\boldsymbol{u}}_{k}=\left[u_{k k}, \ldots, u_{m k}\right]^{T}$ and the matrix and $\boldsymbol{A}_{k}$ in $\boldsymbol{A}$. However, the elements $u_{k, k}$ and $a_{k}=r_{k, k}$ have to compete for the diagonal in $\boldsymbol{A}$. For $m=4$ and $n=3$ the two possibilities look as follows:

$$
\boldsymbol{A}=\left[\begin{array}{lll}
u_{11} & r_{12} & r_{13} \\
u_{21} & u_{22} & r_{23} \\
u_{31} & u_{32} & u_{33} \\
u_{41} & u_{42} & u_{43}
\end{array}\right] \text { or } \boldsymbol{A}=\left[\begin{array}{lll}
r_{11} & r_{12} & r_{13} \\
u_{21} & r_{22} & r_{23} \\
u_{31} & u_{32} & r_{33} \\
u_{41} & u_{42} & u_{43}
\end{array}\right] .
$$

The following algorithm for Householder triangulation takes $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ and $\boldsymbol{B} \in \mathbb{C}^{m \times r}$ as input, and uses housegen to compute Householder transformations $\boldsymbol{H}_{1}, \ldots, \boldsymbol{H}_{s}$ so that $\boldsymbol{R}=\boldsymbol{H}_{s} \cdots \boldsymbol{H}_{1} \boldsymbol{A}$ is upper trapezoidal, and $\boldsymbol{C}=\boldsymbol{H}_{s} \cdots \boldsymbol{H}_{1} \boldsymbol{B}$. The matrices $\boldsymbol{R}$ and $\boldsymbol{C}$ are returned. If $\boldsymbol{B}$ is the empty matrix then $\boldsymbol{C}$ is the empty matrix with $m$ rows and 0 columns. $r_{k, k}$ is stored in $\boldsymbol{A}$, and $u_{k, k}$ is stored in a separate vector. We will see that the algorithm can be used to solve linear systems and least squares problems with right hand $\operatorname{side}(\mathrm{s}) \boldsymbol{B}$, and to compute the product of the Householder transformations by choosing $\boldsymbol{B}=\boldsymbol{I}$.

```
function [R, C] = housetriang(A,B)
% [R,C] = housetriang(A,B)
[m,n]=size(A); r=size(B,2); A=[A,B];
for k=1:min(n,m-1)
    [v,A(k,k)]=housegen(A(k:m,k));
    C=A(k:m,k+1:n+r); A(k:m,k+1:n+r)=C-v*(v'*C);
end
R=triu(A(:,1:n)); C=A(:,n+1:n+r);
end
```

Listing 5.2 housetriang

Here $v=\hat{\boldsymbol{u}}_{k}$ and the update is computed as $\hat{\boldsymbol{H}}_{k} \boldsymbol{C}=\left(\boldsymbol{I}-\boldsymbol{v} \boldsymbol{v}^{*}\right) \boldsymbol{C}=\boldsymbol{C}-\boldsymbol{v}\left(\boldsymbol{v}^{*} \boldsymbol{C}\right)$. The MATLAB command triu extracts the upper triangular part of $\boldsymbol{A}$ introducing zeros in rows $n+1, \ldots, m$.

### 5.3.2 The Number of Arithmetic Operations

The bulk of the work in Algorithm 5.2 is the computation of $\boldsymbol{C}-\boldsymbol{v} *\left(\boldsymbol{v}^{*} * \boldsymbol{C}\right)$ for each $k$. Since in Algorithm 5.2, $\boldsymbol{C} \in \mathbb{C}^{(m-k+1) \times(n+r-k)}$ and $m \geq n$ the cost of computing the update $\boldsymbol{C}-\boldsymbol{v} *\left(\boldsymbol{v}^{T} * \boldsymbol{C}\right)$ in the real case is $4(m-k+1)(n+r-k)$ arithmetic operations. This implies that the work in Algorithm 5.2 can be estimated as

$$
\int_{0}^{n} 4(m-k)(n+r-k) d k=2 m(n+r)^{2}-\frac{2}{3}(n+r)^{3} .
$$

For $m=n$ and $r=0$ this gives $4 n^{3} / 3=2 G_{n}$ for the number of arithmetic operations to bring a matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ to upper triangular form using Householder transformations.

### 5.3.3 Solving Linear Systems Using Unitary Transformations

Consider now the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A}$ is square. Using Algorithm 5.2 we obtain an upper triangular system $\boldsymbol{R} \boldsymbol{x}=\boldsymbol{c}$ that is upper triangular and nonsingular if $\boldsymbol{A}$ is nonsingular. Thus, it can be solved by back substitution and we have a method for solving linear systems that is an alternative to Gaussian elimination. The two methods are similar since they both reduce $\boldsymbol{A}$ to upper triangular form using certain transformations and they both work for nonsingular systems.

Which method is better? Here is a very brief discussion.

- Advantages with Householder:
    - Row interchanges are not necessary, but see [3].
    - Numerically stable.
- Advantages with Gauss
    - Half the number of arithmetic operations compared to Householder.
    - Row interchanges are often not necessary.
    - Usually stable (but no guarantee).

Linear systems can be constructed where Gaussian elimination will fail numerically even if row interchanges are used, see [21]. On the other hand the transformations used in Householder triangulation are unitary so the method is quite stable. So why is Gaussian elimination more popular than Householder triangulation? One
reason is that the number of arithmetic operations in (5.16) when $m=n$ is $4 n^{3} / 3=$ $2 G_{n}$, which is twice the number for Gaussian elimination. Numerical stability can be a problem with Gaussian elimination, but years and years of experience shows that it works well for most practical problems and pivoting is often not necessary. Also Gaussian elimination often wins for banded and sparse problems.

### 5.4 The QR Decomposition and QR Factorization

Gaussian elimination without row interchanges results in an LU factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{U}$ of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Consider Householder triangulation of $\boldsymbol{A}$. Applying Algorithm 5.2 gives $\boldsymbol{R}=\boldsymbol{H}_{n-1} \cdots \boldsymbol{H}_{1} \boldsymbol{A}$ implying the factorization $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$, where $\boldsymbol{Q}=\boldsymbol{H}_{1} \cdots \boldsymbol{H}_{n-1}$ is unitary and $\boldsymbol{R}$ is upper triangular. This is known as a QR factorization of $\boldsymbol{A}$.

### 5.4.1 Existence

For a rectangular matrix we define the following.
Definition 5.5 (QR Decomposition) Let $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ with $m, n \in \mathbb{N}$. We say that $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ is a $\mathbf{Q R}$ decomposition of $\boldsymbol{A}$ if $\boldsymbol{Q} \in \mathbb{C}^{m, m}$ is square and unitary and $\boldsymbol{R} \in \mathbb{C}^{m \times n}$ is upper trapezoidal. If $m \geq n$ then $\boldsymbol{R}$ takes the form

$$
\boldsymbol{R}=\left[\begin{array}{c}
\boldsymbol{R}_{1} \\
\mathbf{0}_{m-n, n}
\end{array}\right]
$$

where $\boldsymbol{R}_{1} \in \mathbb{C}^{n \times n}$ is upper triangular and $\mathbf{0}_{m-n, n}$ is the zero matrix with $m-n$ rows and $n$ columns. For $m \geq n$ we call $\boldsymbol{A}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$ a $\mathbf{Q R}$ factorization of $\boldsymbol{A}$ if $\boldsymbol{Q}_{1} \in \mathbb{C}^{m \times n}$ has orthonormal columns and $\boldsymbol{R}_{1} \in \mathbb{C}^{n \times n}$ is upper triangular.

Suppose $m \geq n$. A QR factorization is obtained from a QR decomposition $\boldsymbol{A}=$ $\boldsymbol{Q} \boldsymbol{R}$ by simply using the first $n$ columns of $\boldsymbol{Q}$ and the first $n$ rows of $\boldsymbol{R}$. Indeed, if we partition $\boldsymbol{Q}$ as $\left[\boldsymbol{Q}_{1}, \boldsymbol{Q}_{2}\right]$ and $\boldsymbol{R}=\left[\begin{array}{c}\boldsymbol{R}_{1} \\ \mathbf{0}\end{array}\right]$, where $\boldsymbol{Q}_{1} \in \mathbb{R}^{m \times n}$ and $\boldsymbol{R}_{1} \in \mathbb{R}^{n \times n}$ then $\boldsymbol{A}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$ is a QR factorization of $\boldsymbol{A}$. On the other hand a QR factorization $\boldsymbol{A}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$ of $\boldsymbol{A}$ can be turned into a QR decomposition by extending the set of columns $\left\{\boldsymbol{q}_{1}, \ldots, \boldsymbol{q}_{n}\right\}$ of $\boldsymbol{Q}_{1}$ into an orthonormal basis $\left\{\boldsymbol{q}_{1}, \ldots, \boldsymbol{q}_{n}, \boldsymbol{q}_{n+1}, \ldots, \boldsymbol{q}_{m}\right\}$ for $\mathbb{R}^{m}$ and adding $m-n$ rows of zeros to $\boldsymbol{R}_{1}$. We then obtain a QR decomposition $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$, where $\boldsymbol{Q}=\left[\boldsymbol{q}_{1}, \ldots, \boldsymbol{q}_{m}\right]$ and $\boldsymbol{R}=\left[\begin{array}{c}\boldsymbol{R}_{1} \\ \mathbf{0}\end{array}\right]$.

Example 5.2 (QR Decomposition and Factorization) Consider the factorization

$$
\boldsymbol{A}=\left[\begin{array}{rrr}
1 & 3 & 1 \\
1 & 3 & 7 \\
1 & -1 & -4 \\
1 & -1 & 2
\end{array}\right]=\frac{1}{2}\left[\begin{array}{rrrr}
1 & 1 & -1 & -1 \\
1 & 1 & 1 & 1 \\
1 & -1 & -1 & 1 \\
1 & -1 & 1 & -1
\end{array}\right] \times\left[\begin{array}{lll}
2 & 2 & 3 \\
0 & 4 & 5 \\
0 & 0 & 6 \\
0 & 0 & 0
\end{array}\right]=\boldsymbol{Q} \boldsymbol{R} .
$$

Since $\boldsymbol{Q}^{T} \boldsymbol{Q}=\boldsymbol{I}$ and $\boldsymbol{R}$ is upper trapezoidal, this is a QR decomposition of $\boldsymbol{A}$. A QR factorization $\boldsymbol{A}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$ is obtained by dropping the last column of $\boldsymbol{Q}$ and the last row of $\boldsymbol{R}$, so that

$$
\boldsymbol{A}=\frac{1}{2}\left[\begin{array}{ccc}
1 & 1 & -1 \\
1 & 1 & 1 \\
1 & -1 & -1 \\
1 & -1 & 1
\end{array}\right] \times\left[\begin{array}{lll}
2 & 2 & 3 \\
0 & 4 & 5 \\
0 & 0 & 6
\end{array}\right]=\boldsymbol{Q}_{1} \boldsymbol{R}_{1} .
$$

Consider existence and uniqueness.
Theorem 5.9 (Existence of QR Decomposition) Any matrix $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ with $m, n \in \mathbb{N}$ has a $Q R$ decomposition.

Proof If $m=1$ then $\boldsymbol{A}$ is already in upper trapezoidal form and $\boldsymbol{A}=[1] \boldsymbol{A}$ is a QR decomposition of $\boldsymbol{A}$. Suppose $m>1$ and set $s:=\min (m-1, n)$. Note that the function housegen (x) returns the vector $\boldsymbol{u}$ in a Householder transformation for any vector $\boldsymbol{x}$. With $\boldsymbol{B}=\boldsymbol{I}$ in Algorithm 5.2 we obtain $\boldsymbol{R}=\boldsymbol{C} \boldsymbol{A}$ and $\boldsymbol{C}=$ $\boldsymbol{H}_{s} \cdots \boldsymbol{H}_{2} \boldsymbol{H}_{1}$. Thus $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ is a QR decomposition of $\boldsymbol{A}$ since $\boldsymbol{Q}:=\boldsymbol{C}^{*}=$ $\boldsymbol{H}_{1} \cdots \boldsymbol{H}_{s}$ is a product of unitary matrices and therefore unitary. $\square$

Theorem 5.10 (Uniqueness of QR Factorization) If $m \geq n$ then the QR factorization is unique if $\boldsymbol{A}$ has linearly independent columns and $\boldsymbol{R}$ has positive diagonal elements.

Proof Let $\boldsymbol{A}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$ be a QR factorization of $\boldsymbol{A} \in \mathbb{C}^{m \times n}$. Now $\boldsymbol{A}^{*} \boldsymbol{A}=$ $\boldsymbol{R}_{1}^{*} \boldsymbol{Q}_{1}^{*} \boldsymbol{Q}_{1} \boldsymbol{R}_{1}=\boldsymbol{R}_{1}^{*} \boldsymbol{R}_{1}$. By Lemma 4.2 the matrix $\boldsymbol{A}^{*} \boldsymbol{A}$ is positive definite, the matrix $\boldsymbol{R}_{1}$ is nonsingular, and if its diagonal elements are positive then $\boldsymbol{R}_{1}^{*} \boldsymbol{R}_{1}$ is the Cholesky factorization of $\boldsymbol{A}^{*} \boldsymbol{A}$. Since the Cholesky factorization is unique it follows that $\boldsymbol{R}_{1}$ is unique and since necessarily $\boldsymbol{Q}_{1}=\boldsymbol{A} \boldsymbol{R}_{1}^{-1}$, it must also be unique. $\square$

Example 5.3 (QR Decomposition and Factorization) Consider finding the QR decomposition and factorization of the matrix $\boldsymbol{A}=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$ using the method of the uniqueness proof of Theorem 5.10. We find $\boldsymbol{B}:=\boldsymbol{A}^{T} \boldsymbol{A}=\left[\begin{array}{cc}5 & -4 \\ -4 & 5\end{array}\right]$. The Cholesky factorization of $\boldsymbol{B}=\boldsymbol{R}^{T} \boldsymbol{R}$ is given by $\boldsymbol{R}=\frac{1}{\sqrt{5}}\left[\begin{array}{cc}5 & -4 \\ 0 & 3\end{array}\right]$. Now $\boldsymbol{R}^{-1}=\frac{1}{3 \sqrt{5}}\left[\begin{array}{ll}3 & 4 \\ 0 & 5\end{array}\right]$ so $\boldsymbol{Q}=\boldsymbol{A} \boldsymbol{R}^{-1}=\frac{1}{\sqrt{5}}\left[\begin{array}{cc}2 & 1 \\ -1 & 2\end{array}\right]$. Since $\boldsymbol{A}$ is square $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ is both the QR decomposition and QR factorization of $\boldsymbol{A}$.

### 5.5 QR and Gram-Schmidt

The Gram-Schmidt orthogonalization of the columns of $\boldsymbol{A}$ can be used to find the QR factorization of $\boldsymbol{A}$.

Theorem 5.11 (QR and Gram-Schmidt) Suppose $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ has rank $n$ and let $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}$ be the result of applying Gram Schmidt to the columns $\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{n}$ of $\boldsymbol{A}$, i.e.,

$$
\boldsymbol{v}_{1}=\boldsymbol{a}_{1}, \quad \boldsymbol{v}_{j}=\boldsymbol{a}_{j}-\sum_{i=1}^{j-1} \frac{\boldsymbol{a}_{j}^{T} \boldsymbol{v}_{i}}{\boldsymbol{v}_{i}^{T} \boldsymbol{v}_{i}} \boldsymbol{v}_{i}, \quad \text { for } j=2, \ldots, n .
$$

Let

$$
\begin{aligned}
& \boldsymbol{Q}_{1}:=\left[\begin{array}{llll}
\boldsymbol{q}_{1}, \ldots, \boldsymbol{q}_{n}
\end{array}\right], \\
& \boldsymbol{R}_{1}:= \\
& \boldsymbol{q}_{j}:=\frac{\boldsymbol{v}_{j}}{\left\|\boldsymbol{v}_{j}\right\|_{2}}, \quad j=1, \ldots, n \text { and } \\
& {\left[\begin{array}{ccccc}
\left\|\boldsymbol{v}_{1}\right\|_{2} & \boldsymbol{a}_{2}^{T} \boldsymbol{q}_{1} & \boldsymbol{a}_{3}^{T} \boldsymbol{q}_{1} & \cdots & \boldsymbol{a}_{n-1}^{T} \boldsymbol{q}_{1} \\
0 & \left\|\boldsymbol{v}_{2}\right\|_{2} & \boldsymbol{a}_{3}^{T} \boldsymbol{q}_{2} & \cdots & \boldsymbol{a}_{n-1}^{T} \boldsymbol{q}_{2} \\
& 0 & \left\|\boldsymbol{v}_{3}\right\|_{2} & \cdots & \boldsymbol{a}_{n-1}^{T} \boldsymbol{q}_{2} \\
& & \ddots & \ddots & \boldsymbol{a}_{n}^{T} \boldsymbol{q}_{3} \\
& & & \ddots & \vdots \\
& & & \left\|\boldsymbol{v}_{n-1}\right\|_{2} & \boldsymbol{a}_{n}^{T} \boldsymbol{q}_{n-1} \\
& & & 0 & \left\|\boldsymbol{v}_{n}\right\|_{2}
\end{array}\right] .}
\end{aligned}
$$

Then $\boldsymbol{A}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$ is the unique $Q R$ factorization of $\boldsymbol{A}$.
Proof Let $\boldsymbol{Q}_{1}$ and $\boldsymbol{R}_{1}$ be given by (5.18). The matrix $\boldsymbol{Q}_{1}$ is well defined and has orthonormal columns, since $\left\{\boldsymbol{q}_{1}, \ldots, \boldsymbol{q}_{n}\right\}$ is an orthonormal basis for $\mathcal{R}(\boldsymbol{A})$ by Theorem 5.4. By (5.17)

$$
\boldsymbol{a}_{j}=\boldsymbol{v}_{j}+\sum_{i=1}^{j-1} \frac{\boldsymbol{a}_{j}^{T} \boldsymbol{v}_{i}}{\boldsymbol{v}_{i}^{T} \boldsymbol{v}_{i}} \boldsymbol{v}_{i}=r_{j j} \boldsymbol{q}_{j}+\sum_{i=1}^{j-1} \boldsymbol{q}_{i} r_{i j}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1} \boldsymbol{e}_{j}, j=1, \ldots, n .
$$

Clearly $\boldsymbol{R}_{1}$ has positive diagonal elements and the factorization is unique. $\square$

Example 5.4 (QR Using Gram-Schmidt) Consider finding the QR decomposition and factorization of the matrix $\boldsymbol{A}=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]=\left[\boldsymbol{a}_{1}, \boldsymbol{a}_{2}\right]$ using Gram-Schmidt. Using (5.17) we find $\boldsymbol{v}_{1}=\boldsymbol{a}_{1}$ and $\boldsymbol{v}_{2}=\boldsymbol{a}_{2}-\frac{\boldsymbol{a}_{2}^{T} \boldsymbol{v}_{1}}{\boldsymbol{v}_{1}^{T} \boldsymbol{v}_{1}} \boldsymbol{v}_{1}=\frac{3}{5}\left[\begin{array}{l}1 \\ 2\end{array}\right]$. Thus $\boldsymbol{Q}=\left[\boldsymbol{q}_{1}, \boldsymbol{q}_{2}\right]$, where $\boldsymbol{q}_{1}=\frac{1}{\sqrt{5}}\left[\begin{array}{c}2 \\ -1\end{array}\right]$ and $\boldsymbol{q}_{2}=\frac{1}{\sqrt{5}}\left[\begin{array}{l}1 \\ 2\end{array}\right]$. By (5.18) we find

$$
\boldsymbol{R}_{1}=\boldsymbol{R}=\left[\begin{array}{cc}
\left\|\boldsymbol{v}_{1}\right\|_{2} & \boldsymbol{a}_{2}^{T} \boldsymbol{q}_{1} \\
0 & \left\|\boldsymbol{v}_{2}\right\|_{2}
\end{array}\right]=\frac{1}{\sqrt{5}}\left[\begin{array}{cc}
5 & -4 \\
0 & 3
\end{array}\right]
$$

and this agrees with what we found in Example 5.3.

Warning The Gram-Schmidt orthogonalization process should not be used to compute the QR factorization numerically. The columns of $\boldsymbol{Q}_{1}$ computed in floating point arithmetic using Gram-Schmidt orthogonalization will often be far from orthogonal. There is a modified version of Gram-Schmidt which behaves better numerically, see [2]. Here we only considered Householder transformations (cf. Algorithm 5.2).

### 5.6 Givens Rotations

In some applications, the matrix we want to triangulate has a special structure. Suppose for example that $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is square and upper Hessenberg as illustrated by a Wilkinson diagram for $n=4$

$$
\boldsymbol{A}=\left[\begin{array}{llll}
x & x & x & x \\
x & x & x & x \\
0 & x & x & x \\
0 & 0 & x & x
\end{array}\right] .
$$

Only one element in each column needs to be annihilated and a full Householder transformation will be inefficient. In this case we can use a simpler transformation.

Definition 5.6 (Givens Rotation, Plane Rotation) A plane rotation (also called a Given's rotation) is a matrix $\boldsymbol{P} \in \mathbb{R}^{2,2}$ of the form

$$
\boldsymbol{P}:=\left[\begin{array}{cc}
c & s \\
-s & c
\end{array}\right], \text { where } c^{2}+s^{2}=1 .
$$

A plane rotation is an orthogonal matrix and there is a unique angle $\theta \in[0,2 \pi)$ such that $c=\cos \theta$ and $s=\sin \theta$. Moreover, the identity matrix is a plane rotation corresponding to $\theta=0$. A vector $\boldsymbol{x}$ in the plane is rotated an angle $\theta$ clockwise by $\boldsymbol{P}=\boldsymbol{R}$. See Exercise 5.16 and Fig. 5.4.

Fig. 5.4 A plane rotation
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-134.jpg?height=291&width=343&top_left_y=1660&top_left_x=1001)

A Givens rotation can be used to introduce one zero in a vector. Consider first the case of a 2-vector. Suppose

$$
\boldsymbol{x}=\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right] \neq \mathbf{0}, \quad c:=\frac{x_{1}}{r}, \quad s:=\frac{x_{2}}{r}, \quad r:=\|\boldsymbol{x}\|_{2} .
$$

If $\boldsymbol{x} \in \mathbb{R}^{2}$ then

$$
\boldsymbol{P} \boldsymbol{x}=\frac{1}{r}\left[\begin{array}{rr}
x_{1} & x_{2} \\
-x_{2} & x_{1}
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\frac{1}{r}\left[\begin{array}{c}
x_{1}^{2}+x_{2}^{2} \\
0
\end{array}\right]=\left[\begin{array}{l}
r \\
0
\end{array}\right],
$$

and we have introduced a zero in $\boldsymbol{x}$. We can take $\boldsymbol{P}=\boldsymbol{I}$ when $\boldsymbol{x}=\mathbf{0}$.
For an $n$-vector $\boldsymbol{x} \in \mathbb{R}^{n}$ and $1 \leq i<j \leq n$ we define a rotation in the $i, j$-plane as a matrix $\boldsymbol{P}_{i j}=\left(p_{k l}\right) \in \mathbb{R}^{n \times n}$ by $p_{k l}=\delta_{k l}$ except for positions $i i, j j, i j, j i$, which are given by

$$
\left[\begin{array}{cc}
p_{i i} & p_{i j} \\
p_{j i} & p_{j j}
\end{array}\right]=\left[\begin{array}{cc}
c & s \\
-s & c
\end{array}\right], \text { where } c^{2}+s^{2}=1 .
$$

Thus, for $n=4$,

$$
\boldsymbol{P}_{12}=\left[\begin{array}{cccc}
c & s & 0 & 0 \\
-s & c & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{array}\right], \quad \boldsymbol{P}_{13}=\left[\begin{array}{cccc}
c & 0 & s & 0 \\
0 & 1 & 0 & 0 \\
-s & 0 & c & 0 \\
0 & 0 & 0 & 1
\end{array}\right], \quad \boldsymbol{P}_{23}=\left[\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & s & c & 0 \\
0 & -s & c & 0 \\
0 & 0 & 0 & 1
\end{array}\right] .
$$

Premultiplying a matrix by a rotation in the $i, j$-plane changes only rows $i$ and $j$ of the matrix, while post multiplying the matrix by such a rotation only changes column $i$ and $j$. In particular, if $\boldsymbol{B}=\boldsymbol{P}_{i j} \boldsymbol{A}$ and $\boldsymbol{C}=\boldsymbol{A} \boldsymbol{P}_{i j}$ then $\boldsymbol{B}(k,:)=\boldsymbol{A}(k,:)$, $\boldsymbol{C}(:, k)=\boldsymbol{A}(:, k)$ for all $k \neq i, j$ and

$$
\left[\begin{array}{l}
\boldsymbol{B}(i,:) \\
\boldsymbol{B}(j,:)
\end{array}\right]=\left[\begin{array}{rc}
c & s \\
-s c &
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{A}(i,:) \\
\boldsymbol{A}(j,:)
\end{array}\right],[\boldsymbol{C}(:, i) \boldsymbol{C}(:, j)]=[\boldsymbol{A}(:, i) \boldsymbol{A}(:, j)]\left[\begin{array}{rc}
c & s \\
-s & c
\end{array}\right] .
$$

Givens rotations can be used as an alternative to Householder transformations for solving linear systems. It can be shown that for a dense system of order $n$ the number of arithmetic operations is asymptotically $2 n^{3}$, corresponding to the work of 3 Gaussian eliminations, while, the work using Householder transformations corresponds to 2 Gaussian eliminations. However, for matrices with a special structure Givens rotations can be used to advantage. As an example consider an upper Hessenberg matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$. It can be transformed to upper triangular form using rotations $\boldsymbol{P}_{i, i+1}$ for $i=1, \ldots, n-1$. For $n=4$ the process can be illustrated as follows.

$$
\boldsymbol{A}=\left[\begin{array}{llll}
x & x & x & x \\
x & x & x & x \\
0 & x & x & x \\
0 & 0 & x & x
\end{array}\right] \xrightarrow{\boldsymbol{P}_{12}}\left[\begin{array}{cccc}
r_{11} & r_{12} & r_{13} & r_{14} \\
\mathbf{0} & x & x & x \\
0 & x & x & x \\
0 & 0 & x & x
\end{array}\right] \xrightarrow{\boldsymbol{P}_{23}}\left[\begin{array}{cccc}
r_{11} & r_{12} & r_{13} & r_{14} \\
0 & r_{22} & r_{23} & r_{24} \\
0 & \mathbf{0} & x & x \\
0 & 0 & x & x
\end{array}\right] \xrightarrow{\boldsymbol{P}_{34}}\left[\begin{array}{cccc}
r_{11} & r_{12} & r_{13} & r_{14} \\
0 & r_{22} & r_{23} & r_{24} \\
0 & 0 & r_{33} & r_{34} \\
0 & 0 & \mathbf{0} & r_{44}
\end{array}\right] .
$$

For an algorithm see Exercise 5.18. This reduction is used in the QR method discussed in Chap. 15.

### 5.7 Exercises Chap. 5

### 5.7.1 Exercises Sect. 5.1

Exercise 5.1 (The $\boldsymbol{A}^{*} \boldsymbol{A}$ Inner Product) Suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has linearly independent columns. Show that $\langle\boldsymbol{x}, \boldsymbol{y}\rangle:=\boldsymbol{y}^{*} \boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}$ defines an inner product on $\mathbb{C}^{n}$.

Exercise 5.2 (Angle Between Vectors in Complex Case) Show that in the complex case there is a unique angle $\theta$ in $[0, \pi / 2]$ such that

$$
\cos \theta=\frac{|\langle\boldsymbol{x}, \boldsymbol{y}\rangle|}{\|\boldsymbol{x}\|\|\boldsymbol{y}\|} .
$$

Exercise 5.3 ( $\boldsymbol{x}^{T}$ Ay Inequality (Exam Exercise 1979-3)) Suppose $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is symmetric positive definite. Show that

$$
\left|\boldsymbol{x}^{T} \boldsymbol{A y}\right|^{2} \leq \boldsymbol{x}^{T} \boldsymbol{A x} \boldsymbol{y}^{T} \boldsymbol{A y}
$$

for all $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$, with equality if and only if $\boldsymbol{x}$ and $\boldsymbol{y}$ are linearly dependent.

### 5.7.2 Exercises Sect. 5.2

Exercise 5.4 (What Does Algorithm Housegen Do When $\boldsymbol{x}=\boldsymbol{e}_{1}$ ?) Determine $\boldsymbol{H}$ in Algorithm 5.1 when $\boldsymbol{x}=\boldsymbol{e}_{1}$.

Exercise 5.5 (Examples of Householder Transformations) If $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$ with $\|\boldsymbol{x}\|_{2}=\|\boldsymbol{y}\|_{2}$ and $\boldsymbol{v}:=\boldsymbol{x}-\boldsymbol{y} \neq \mathbf{0}$ then it follows from Example 5.1 that $\left(\boldsymbol{I}-2 \frac{\boldsymbol{v} \boldsymbol{v}^{T}}{\boldsymbol{v}^{T} \boldsymbol{v}}\right) \boldsymbol{x}=\boldsymbol{y}$. Use this to construct a Householder transformation $\boldsymbol{H}$ such that $\boldsymbol{H} \boldsymbol{x}=\boldsymbol{y}$ in the following cases.

a) $\boldsymbol{x}=\left[\begin{array}{l}3 \\ 4\end{array}\right], \quad \boldsymbol{y}=\left[\begin{array}{l}5 \\ 0\end{array}\right]$.
b) $\boldsymbol{x}=\left[\begin{array}{l}2 \\ 2 \\ 1\end{array}\right], \quad \boldsymbol{y}=\left[\begin{array}{l}0 \\ 3 \\ 0\end{array}\right]$.

Exercise 5.6 (2 × 2 Householder Transformation) Show that a real 2 × 2 Householder transformation can be written in the form

$$
\boldsymbol{H}=\left[\begin{array}{cc}
-\cos \phi & \sin \phi \\
\sin \phi & \cos \phi
\end{array}\right] .
$$

Find $\boldsymbol{H} \boldsymbol{x}$ if $\boldsymbol{x}=[\cos \phi, \sin \phi]^{T}$.
Exercise 5.7 (Householder Transformation (Exam Exercise 2010-1))

a) Suppose $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$ with $\|\boldsymbol{x}\|_{2}=\|\boldsymbol{y}\|_{2}$ and $\boldsymbol{v}:=\boldsymbol{x}-\boldsymbol{y} \neq 0$. Show that
$$
\boldsymbol{H} \boldsymbol{x}=\boldsymbol{y}, \quad \text { where } \quad \boldsymbol{H}:=\boldsymbol{I}-2 \frac{\boldsymbol{v} \boldsymbol{v}^{T}}{\boldsymbol{v}^{T} \boldsymbol{v}} .
$$
b) Let $\boldsymbol{B} \in \mathbb{R}^{4,4}$ be given by
$$
\boldsymbol{B}:=\left[\begin{array}{llll}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\epsilon & 0 & 0 & 0
\end{array}\right],
$$
where $0<\epsilon<1$. Compute a Householder transformation $\boldsymbol{H}$ and a matrix $\boldsymbol{B}_{1}$ such that the first column of $\boldsymbol{B}_{1}:=\boldsymbol{H} \boldsymbol{B} \boldsymbol{H}$ has a zero in the last two positions.

### 5.7.3 Exercises Sect. 5.4

Exercise 5.8 (QR Decomposition)

$$
\boldsymbol{A}=\left[\begin{array}{ll}
1 & 2 \\
1 & 2 \\
1 & 0 \\
1 & 0
\end{array}\right], \quad \boldsymbol{Q}=\frac{1}{2}\left[\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1 \\
1 & -1 & 1 & -1
\end{array}\right], \quad \boldsymbol{R}=\left[\begin{array}{ll}
2 & 2 \\
0 & 2 \\
0 & 0 \\
0 & 0
\end{array}\right] .
$$

Show that $\boldsymbol{Q}$ is orthonormal and that $\boldsymbol{Q} \boldsymbol{R}$ is a QR decomposition of $\boldsymbol{A}$. Find a QR factorization of $\boldsymbol{A}$.

Exercise 5.9 (Householder Triangulation)

a) Let
$$
A:=\left[\begin{array}{ccc}
1 & 0 & 1 \\
-2 & -1 & 0 \\
2 & 2 & 1
\end{array}\right] .
$$

Find Householder transformations $\boldsymbol{H}_{1}, \boldsymbol{H}_{2} \in \mathbb{R}^{3 \times 3}$ such that $\boldsymbol{H}_{2} \boldsymbol{H}_{1} \boldsymbol{A}$ is upper triangular.

b) Find the QR factorization of $\boldsymbol{A}$, when $\boldsymbol{R}$ has positive diagonal elements.

Exercise 5.10 (Hadamard's Inequality) In this exercise we use the QR factorization to prove a classical determinant inequality. For any $\boldsymbol{A}=\left[\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{n}\right] \in \mathbb{C}^{n \times n}$ we have

$$
|\operatorname{det}(\boldsymbol{A})| \leq \prod_{j=1}^{n}\left\|\boldsymbol{a}_{j}\right\|_{2} .
$$

Equality holds if and only if $\boldsymbol{A}$ has a zero column or the columns of $\boldsymbol{A}$ are orthogonal.

a) Show that if $\boldsymbol{Q}$ is unitary then $|\operatorname{det}(\boldsymbol{Q})|=1$.
b) Let $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ be a QR factorization of $\boldsymbol{A}$ and let $\boldsymbol{R}=\left[\boldsymbol{r}_{1}, \ldots, \boldsymbol{r}_{n}\right]$. Show that $\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)_{j j}=\left\|\boldsymbol{a}_{j}\right\|_{2}^{2}=\left(\boldsymbol{R}^{*} \boldsymbol{R}\right)_{j j}=\left\|\boldsymbol{r}_{j}\right\|_{2}^{2}$.
c) Show that $|\operatorname{det}(\boldsymbol{A})|=\prod_{j=1}^{n}\left|r_{j j}\right| \leq \prod_{j=1}^{n}\left\|\boldsymbol{a}_{j}\right\|_{2}$.
d) Show that we have equality if $\boldsymbol{A}$ has a zero column,
e) Suppose the columns of $\boldsymbol{A}$ are nonzero. Show that we have equality if and only if the columns of $\boldsymbol{A}$ are orthogonal. ${ }^{1}$

Exercise 5.11 (QL Factorization (Exam Exercise 1982-2)) Suppose $\boldsymbol{B} \in \mathbb{R}^{n \times n}$ is symmetric and positive definite. It can be shown that $\boldsymbol{B}$ has a factorization of the form $\boldsymbol{B}=\boldsymbol{L}^{T} \boldsymbol{L}$, where $\boldsymbol{L}$ is lower triangular with positive diagonal elements (you should not show this). Note that this is different from the Cholesky factorization $\boldsymbol{B}=\boldsymbol{L} \boldsymbol{L}^{T}$.

a) Suppose $\boldsymbol{B}=\boldsymbol{L}^{T} \boldsymbol{L}$. Write down the equations to determine the elements $l_{i, j}$ of $\boldsymbol{L}$, in the order $i=n, n-1, \ldots, 1$ and $j=i, 1,2 \ldots, i-1$.
b) Explain (without making a detailed algorithm) how the $\boldsymbol{L}^{T} \boldsymbol{L}$ factorization can be used to solve the linear system $\boldsymbol{B} \boldsymbol{x}=\boldsymbol{c}$. Compute $\|\boldsymbol{L}\|_{F}$. Is the algorithm stable?
c) Show that every nonsingular matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ can be factored in the form $\boldsymbol{A}=$ $\boldsymbol{Q} \boldsymbol{L}$, where $\boldsymbol{Q} \in \mathbb{R}^{n \times n}$ is orthogonal and $\boldsymbol{L} \in \mathbb{R}^{n \times n}$ is lower triangular with positive diagonal elements.
d) Show that the $\boldsymbol{Q} \boldsymbol{L}$ factorization in c) is unique.

Exercise 5.12 (QL-Factorization (Exam Exercise 1982-3)) In this exercise we will develop an algorithm to find a QL-factorization of $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ (cf. Exam exercise 1982-2) using Householder transformations.

a) Given vectors $\boldsymbol{a}:=\left[a_{1}, \ldots, a_{n}\right]^{T} \in \mathbb{R}^{n}$ and $\boldsymbol{e}_{n}:=[0, \ldots, 0,1]^{T}$. Find $\boldsymbol{v} \in \mathbb{R}^{n}$ such that the Householder transformation $\boldsymbol{H}:=\boldsymbol{I}-2 \frac{\boldsymbol{v} \boldsymbol{v}^{*}}{\boldsymbol{v}^{*} \boldsymbol{v}}$ satisfies $\boldsymbol{H} \boldsymbol{a}=-s \boldsymbol{e}_{n}$, where $|s|=\|\boldsymbol{a}\|_{2}$. How should we choose the sign of $s$ ?

[^9]

b)Let $1 \leq r \leq n, \boldsymbol{v}_{r} \in \mathbb{R}^{r}, \boldsymbol{v}_{r} \neq \mathbf{0}$, and
$$
\boldsymbol{V}_{r}:=\boldsymbol{I}_{r}-2 \frac{\boldsymbol{v}_{r} \boldsymbol{v}_{r}^{*}}{\boldsymbol{v}_{r}^{*} \boldsymbol{v}_{r}}=\boldsymbol{I}_{r}-\boldsymbol{u}_{r} \boldsymbol{u}_{r}^{*}, \text { with } \boldsymbol{u}_{r}:=\sqrt{2} \frac{\boldsymbol{v}_{r}}{\left\|\boldsymbol{v}_{r}\right\|_{2}} .
$$
Show that $\boldsymbol{H}:=\left[\begin{array}{cc}\boldsymbol{V}_{r} & \mathbf{0} \\ \mathbf{0} & \boldsymbol{I}_{n-r}\end{array}\right]$ is a Householder transformation. Show also that if $a_{i, j}=0$ for $i=1, \ldots, r$ and $j=r+1, \ldots, n$ then the last $r$ columns of $\boldsymbol{A}$ and $\boldsymbol{H} \boldsymbol{A}$ are the same.
c)Explain, without making a detailed algorithm, how we to a given matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ can find Householder transformations $\boldsymbol{H}_{1}, \ldots, \boldsymbol{H}_{n-1}$ such that $\boldsymbol{H}_{n-1}, \ldots, \boldsymbol{H}_{1} \boldsymbol{A}$ is lower triangular. Give a $\boldsymbol{Q} \boldsymbol{L}$ factorization of $\boldsymbol{A}$.


Exercise 5.13 (QR Fact. of Band Matrices (Exam Exercise 2006-2)) Let $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$ be a nonsingular symmetric band matrix with bandwidth $d \leq n-1$, so that $a_{i j}=0$ for all $i, j$ with $|i-j|>d$. We define $\boldsymbol{B}:=\boldsymbol{A}^{T} \boldsymbol{A}$ and let $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ be the QR factorization of $\boldsymbol{A}$ where $\boldsymbol{R}$ has positive diagonal entries.

a) Show that $\boldsymbol{B}$ is symmetric.
b) Show that $\boldsymbol{B}$ has bandwidth $\leq 2 d$.
c) Write a MATLAB function $\mathrm{B}=$ ata $(\mathrm{A}, \mathrm{d})$ which computes $\boldsymbol{B}$. You shall exploit the symmetry and the function should only use $\mathcal{O}\left(c n^{2}\right)$ flops, where $c$ only depends on $d$.
d) Estimate the number of arithmetic operations in your algorithm.
e) Show that $\boldsymbol{A}^{T} \boldsymbol{A}=\boldsymbol{R}^{T} \boldsymbol{R}$.
f) Explain why $\boldsymbol{R}$ has upper bandwidth $2 d$.
g) We consider 3 methods for finding the QR factorization of the band matrix $\boldsymbol{A}$, where we assume that $n$ is much bigger than $d$. The methods are based on
    1. Gram-Schmidt orthogonalization,
    2. Householder transformations,
    3. Givens rotations.

Which method would you recommend for a computer program using floating point arithmetic? Give reasons for your answer.

Exercise 5.14 (Find QR Factorization (Exam Exercise 2008-2)) Let

$$
A:=\left[\begin{array}{rr}
2 & 1 \\
2 & -3 \\
-2 & -1 \\
-2 & 3
\end{array}\right]
$$

a) Find the Cholesky factorization of $\boldsymbol{A}^{T} \boldsymbol{A}$.
b) Find the QR factorization of $\boldsymbol{A}$.

### 5.7.4 Exercises Sect. 5.5

Exercise 5.15 (QR Using Gram-Schmidt, II) Construct $\boldsymbol{Q}_{1}$ and $\boldsymbol{R}_{1}$ in Example 5.2 using Gram-Schmidt orthogonalization.

### 5.7.5 Exercises Sect. 5.6

Exercise 5.16 (Plane Rotation) Show that if $\boldsymbol{x}=\left[\begin{array}{c}r \cos \alpha \\ r \sin \alpha\end{array}\right]$ then $\boldsymbol{P} \boldsymbol{x}=$ $\left[\begin{array}{l}r \cos (\alpha-\theta) \\ r \sin (\alpha-\theta)\end{array}\right]$.

Exercise 5.17 (Updating the QR Decomposition) Let $\boldsymbol{H} \in \mathbb{R}^{4,4}$ be upper Hessenberg. Find Givens rotation matrices $\boldsymbol{G}_{1}, \boldsymbol{G}_{2}, \boldsymbol{G}_{3}$ such that

$$
\boldsymbol{G}_{3} \boldsymbol{G}_{2} \boldsymbol{G}_{1} \boldsymbol{H}=\boldsymbol{R}
$$

is upper triangular. (Here each $\boldsymbol{G}_{k}=\boldsymbol{P}_{i, j}$ for suitable $i, j, c$ og $s$, and for each $k$ you are meant to find suitable $i$ and $j$.)

Exercise 5.18 (Solving Upper Hessenberg System Using Rotations) Let $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$ be upper Hessenberg and nonsingular, and let $\boldsymbol{b} \in \mathbb{R}^{n}$. The following algorithm solves the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ using rotations $\boldsymbol{P}_{k, k+1}$ for $k=1, \ldots, n-1$. It uses the back solve Algorithm 3.2. Determine the number of arithmetic operations of this algorithm.

```
function x=rothesstri(A,b)
% x=rothesstri(A,b)
n=length(A);A=[A b];
for k=1:n-1
    r=norm([A(k,k),A(k+1,k)]);
    if r>0
        c=A(k,k)/r; s=A(k+1,k)/r;
        A([k k+1],k+1:n+1) ...
            =[c s;-s c]*A([k k+1],k+1:n+1);
    end
    A(k,k)=r; A(k+1,k)=0;
end
x=rbacksolve(A(:,1:n),A(:,n+1),n);
end
```

Listing 5.3 rothesstri

Exercise 5.19 (A Givens Transformation (Exam Exercise 2013-2)) A Givens rotation of order 2 has the form $\boldsymbol{G}:=\left[\begin{array}{rc}c & s \\ -s & c\end{array}\right] \in \mathbb{R}^{2 \times 2}$, where $s^{2}+c^{2}=1$.

a) Is $\boldsymbol{G}$ symmetric and unitary?
b) Given $x_{1}, x_{2} \in \mathbb{R}$ and set $r:=\sqrt{x_{1}^{2}+x_{2}^{2}}$. Find $\boldsymbol{G}$ and $y_{1}, y_{2}$ so that $y_{1}=y_{2}$, where $\left[\begin{array}{l}y_{1} \\ y_{2}\end{array}\right]=\boldsymbol{G}\left[\begin{array}{l}x_{1} \\ x_{2}\end{array}\right]$.

Exercise 5.20 (Givens Transformations (Exam Exercise 2016-3)) Recall that a rotation in the $i j$-plane is an $m \times m$-matrix, denoted $\boldsymbol{P}_{i, j}$, which differs from the identity matrix only in the entries $i i, i j, j i, j j$, which equal

$$
\left[\begin{array}{ll}
p_{i i} & p_{i j} \\
p_{j i} & p_{j j}
\end{array}\right]=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right],
$$

i.e., these four entries are those of a Givens rotation.

a) For $\theta \in \mathbb{R}$, let $\boldsymbol{P}$ be a Givens rotation of the form
$$
\boldsymbol{P}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right]
$$
and let $\boldsymbol{x}$ be a fixed vector in $\mathbb{R}^{2}$. Show that there exists a unique $\theta \in(-\pi / 2, \pi / 2]$ so that $\boldsymbol{P} \boldsymbol{x}= \pm\|\boldsymbol{x}\|_{2} \boldsymbol{e}_{1}$, where $\boldsymbol{e}_{1}=(1,0)^{T}$.
b) Show that, for any vector $\boldsymbol{w} \in \mathbb{R}^{m}$, one can find rotations in the 12-plane, 23-plane, . . ., $(m-1) m$-plane, so that
$$
\boldsymbol{P}_{1,2} \boldsymbol{P}_{2,3} \cdots \boldsymbol{P}_{m-2, m-1} \boldsymbol{P}_{m-1, m} \boldsymbol{w}=\left[\begin{array}{c}
\alpha \\
0 \\
\vdots \\
0
\end{array}\right],
$$
where $\alpha= \pm\|\boldsymbol{w}\|_{2}$.
c) Assume that $m \geq n$. Recall that an $m \times n$-matrix $\boldsymbol{A}$ with entries $a_{i, j}$ is called upper trapezoidal if there are no nonzero entries below the main diagonal
$$
\left(a_{1,1}, a_{2,2}, \ldots, a_{n, n}\right)
$$
(for $m=n$, upper trapezoidal is the same as upper triangular). Recall also that an $m \times n$-matrix is said to be in upper Hessenberg form if there are no nonzero entries below the subdiagonal
$$
\left(a_{2,1}, a_{3,2}, \ldots, a_{n, n-1}\right) .
$$

Explain that, if an $m \times n$-matrix $\boldsymbol{H}$ is in upper Hessenberg form, one can find plane rotations so that
$$
\boldsymbol{P}_{m-1, m} \boldsymbol{P}_{m-2, m-1} \cdots \boldsymbol{P}_{2,3} \boldsymbol{P}_{1,2} \boldsymbol{H}
$$
is upper trapezoidal.
d) Let again $\boldsymbol{A}$ be an $m \times n$-matrix with $m \geq n$, and let $\boldsymbol{A}_{-}$be the matrix obtained by removing column $k$ in $\boldsymbol{A}$. Explain how you can find a QR Decomposition of $\boldsymbol{A}_{-}$, when we already have a QR decomposition $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ of $\boldsymbol{A} .{ }^{2}$

Exercise 5.21 (Cholesky and Givens (Exam Exercise 2018-2)) Assume that $\boldsymbol{A}$ is $n \times n$ symmetric positive definite, and with Cholesky factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{*}$. Assume also that $z$ is a given column vector of length $n$.

a) Explain why $\boldsymbol{A}+\boldsymbol{z} \boldsymbol{z}^{*}$ has a unique Cholesky factorization.
b) Assume that we are given a QR decomposition
$$
\left[\begin{array}{c}
\boldsymbol{L}^{*} \\
\boldsymbol{z}^{*}
\end{array}\right]=\boldsymbol{Q}\left[\begin{array}{c}
\boldsymbol{R} \\
0
\end{array}\right],
$$
with $\boldsymbol{R}$ square and upper triangular. Explain why $\boldsymbol{R}$ is nonsingular. Explain also that, if $\boldsymbol{R}$ also has nonnegative diagonal entries, then $\boldsymbol{A}+\boldsymbol{z} \boldsymbol{z}^{*}$ has the Cholesky factorization $\boldsymbol{R}^{*} \boldsymbol{R}$.
c) Explain how one can find plane rotations $P_{i_{1}, n+1}, P_{i_{2}, n+1}, \ldots, P_{i_{n}, n+1}$ so that
$$
P_{i_{1}, n+1} P_{i_{2}, n+1} \cdots P_{i_{n}, n+1}\left[\begin{array}{c}
\boldsymbol{L}^{*} \\
\boldsymbol{z}^{*}
\end{array}\right]=\left[\begin{array}{c}
\boldsymbol{R}^{\prime} \\
0
\end{array}\right],
$$
with $\boldsymbol{R}^{\prime}$ upper triangular, and explain how to obtain a QR decomposition of $\left[\begin{array}{c}\boldsymbol{L}^{*} \\ \boldsymbol{z}^{*}\end{array}\right]$ from this. In particular you should write down the numbers $i_{1}, \ldots, i_{n}$. Is it possible to choose the plane rotations so that $\boldsymbol{R}^{\prime}$ in (5.22) also has positive diagonal entries?

### 5.8 Review Questions

5.8.1 What is a Householder transformation?
5.8.2 Why are they good for numerical work?
5.8.3 What are the main differences between solving a linear system by Gaussian elimination and Householder transformations?

[^10]

5.8.4What are the differences between a QR decomposition and a QR factorization?
5.8.5Does any matrix have a QR decomposition?
5.8.6What is a Givens transformation?
5.8.7Is a unitary matrix always well conditioned?


## Part II Eigenpairs and Singular Values

We turn now to eigenpairs of matrices, i.e., eigenvalues and corresponding eigenvectors. The eigenpairs of a matrix are easily determined if it is diagonal. Indeed, the eigenvalues are the diagonal elements and the eigenvectors are unit vectors. We will see that not all matrices can be reduced to diagonal form using eigenvalue preserving transformations known as similarity transformations. This raises the question: how close to a diagonal matrix can we reduce a general matrix using similarity transformations? We give one answer to this question, the Jordan factorization or the Jordan canonical form. We also characterize matrices which can be diagonalized using unitary similarity transformations, and study the subclass of Hermitian matrices. Numerical methods for determining eigenvalues and eigenvectors will be considered in Chaps. 14 and 15.

In the second chapter in this part we consider the important singular value decomposition of a rectangular matrix. This decomposition will play a central role in several of the remaining chapters in this book.

## Chapter 6 <br> Eigenpairs and Similarity Transformations

We have seen that a Hermitian matrix is positive definite if and only if it has positive eigenvalues. Eigenvalues and some related quantities called singular values occur in many branches of applied mathematics and are also needed for a deeper study of linear systems and least squares problems. In this and the next chapter we study eigenvalues and singular values. Recall that if $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is a square matrix, $\lambda \in \mathbb{C}$ and $\boldsymbol{x} \in \mathbb{C}^{n}$ then $(\lambda, \boldsymbol{x})$ is an eigenpair for $\boldsymbol{A}$ if $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ and $\boldsymbol{x}$ is nonzero. The scalar $\lambda$ is called an eigenvalue and $\boldsymbol{x}$ is said to be an eigenvector. The set of eigenvalues is called the spectrum of $\boldsymbol{A}$ and is denoted by $\sigma(\boldsymbol{A})$. For example, $\sigma(\boldsymbol{I})=\{1, \ldots, 1\}=\{1\}$. The eigenvalues are the roots of the characteristic polynomial of $\boldsymbol{A}$ given for $\lambda \in \mathbb{C}$ by

$$
\pi_{\boldsymbol{A}}(\lambda)=\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I}) .
$$

The equation $\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=0$ is called the characteristic equation of $\boldsymbol{A}$. Equivalently the characteristic equation can be written $\operatorname{det}(\lambda \boldsymbol{I}-\boldsymbol{A})=0$.

### 6.1 Defective and Nondefective Matrices

For the eigenvectors we will see that it is important to know if the eigenvectors of a matrix of order $n$ form a basis for $\mathbb{C}^{n}$. We say that $\boldsymbol{A}$ is defective if the eigenvectors do not form a basis for $\mathbb{C}^{n}$ and nondefective otherwise.

We have the following sufficient condition for a matrix to be nondefective.
Theorem 6.1 (Distinct Eigenvalues) A matrix with distinct eigenvalues is nondefective, i.e., its eigenvectors are linearly independent.

Proof The proof is by contradiction. Suppose $\boldsymbol{A}$ has eigenpairs $\left(\lambda_{k}, \boldsymbol{x}_{k}\right), k=$ $1, \ldots, n$, with linearly dependent eigenvectors. Let $m$ be the smallest integer such that $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{m}\right\}$ is linearly dependent. Thus $\sum_{j=1}^{m} c_{j} \boldsymbol{x}_{j}=\mathbf{0}$, where at least one $c_{j}$ is nonzero. We must have $m \geq 2$ since eigenvectors are nonzero. We find

$$
\sum_{j=1}^{m} c_{j} \boldsymbol{x}_{j}=\mathbf{0} \Rightarrow \sum_{j=1}^{m} c_{j} \boldsymbol{A} \boldsymbol{x}_{j}=\sum_{j=1}^{m} c_{j} \lambda_{j} \boldsymbol{x}_{j}=\mathbf{0} .
$$

From the last relation we subtract $\sum_{j=1}^{m} c_{j} \lambda_{m} \boldsymbol{x}_{j}=\mathbf{0}$ and find $\sum_{j=1}^{m-1} c_{j}\left(\lambda_{j}-\right.$ $\left.\lambda_{m}\right) \boldsymbol{x}_{j}=\mathbf{0}$. But since $\lambda_{j}-\lambda_{m} \neq 0$ for $j=1, \ldots, m-1$ and at least one $c_{j} \neq 0$ for $j<m$ we see that $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{m-1}\right\}$ is linearly dependent, contradicting the minimality of $m$. $\square$

If some of the eigenvalues occur with multiplicity higher than one then the matrix can be either defective or nondefective.

Example 6.1 (Defective and Nondefective Matrices) Consider the matrices

$$
\boldsymbol{I}:=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right], \quad \boldsymbol{J}:=\left[\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right] .
$$

Since $\boldsymbol{I} \boldsymbol{x}=\boldsymbol{x}$ and $\lambda_{1}=\lambda_{2}=1$ any vector $\boldsymbol{x} \in \mathbb{C}^{2}$ is an eigenvector for $\boldsymbol{I}$. In particular the two unit vectors $\boldsymbol{e}_{1}$ and $\boldsymbol{e}_{2}$ are eigenvectors and form an orthonormal basis for $\mathbb{C}^{2}$. We conclude that the identity matrix is nondefective. The matrix $\boldsymbol{J}$ also has the eigenvalue one with multiplicity two, but since $\boldsymbol{J} \boldsymbol{x}=\boldsymbol{x}$ if and only if $x_{2}=0$, any eigenvector must be a multiple of $\boldsymbol{e}_{1}$. Thus $\boldsymbol{J}$ is defective.

If the eigenvectors $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}$ form a basis for $\mathbb{C}^{n}$ then any $\boldsymbol{x} \in \mathbb{C}^{n}$ can be written

$$
\boldsymbol{x}=\sum_{j=1}^{n} c_{j} \boldsymbol{x}_{j} \text { for some scalars } c_{1}, \ldots, c_{n}
$$

We call this an eigenvector expansion of $\boldsymbol{x}$. Thus to any nondefective matrix there corresponds an eigenvector expansion.

Example 6.2 (Eigenvector Expansion Example) Eigenpairs of $\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$ are $\left(1,[1,1]^{T}\right)$ and $\left(3,[1,-1]^{T}\right)$. Any $\boldsymbol{x}=\left[x_{1}, x_{2}\right]^{T} \in \mathbb{C}^{2}$ has the eigenvector expansion

$$
\boldsymbol{x}=\frac{x_{1}+x_{2}}{2}\left[\begin{array}{l}
1 \\
1
\end{array}\right]+\frac{x_{1}-x_{2}}{2}\left[\begin{array}{c}
1 \\
-1
\end{array}\right] .
$$

### 6.1.1 Similarity Transformations

We need a transformation that can be used to simplify a matrix without changing the eigenvalues.

Definition 6.1 (Similar Matrices) Two matrices $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$ are said to be similar if there is a nonsingular matrix $\boldsymbol{S} \in \mathbb{C}^{n \times n}$ such that $\boldsymbol{B}=\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}$. The transformation $\boldsymbol{A} \rightarrow \boldsymbol{B}$ is called a similarity transformation. The columns of $\boldsymbol{S}$ are denoted by $\boldsymbol{s}_{1}, \boldsymbol{s}_{2}, \ldots, \boldsymbol{s}_{n}$.

We note that

1. Similar matrices have the same eigenvalues, they even have the same characteristic polynomial. Indeed, by the product rule for determinants $\operatorname{det}(\boldsymbol{A} \boldsymbol{C})=$ $\operatorname{det}(\boldsymbol{A}) \operatorname{det}(\boldsymbol{C})$ so that
$$
\begin{aligned}
\pi_{\boldsymbol{B}}(\lambda) & =\operatorname{det}\left(\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}-\lambda \boldsymbol{I}\right)=\operatorname{det}\left(\boldsymbol{S}^{-1}(\boldsymbol{A}-\lambda \boldsymbol{I}) \boldsymbol{S}\right) \\
& =\operatorname{det}\left(\boldsymbol{S}^{-1}\right) \operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I}) \operatorname{det}(\boldsymbol{S})=\operatorname{det}\left(\boldsymbol{S}^{-1} \boldsymbol{S}\right) \operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=\pi_{\boldsymbol{A}}(\lambda),
\end{aligned}
$$
since $\operatorname{det}(\boldsymbol{I})=1$.
2. ( $\lambda, \boldsymbol{x}$ ) is an eigenpair for $\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}$ if and only if ( $\lambda, \boldsymbol{S} \boldsymbol{x}$ ) is an eigenpair for $\boldsymbol{A}$. In fact $\left(\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}\right) \boldsymbol{x}=\lambda \boldsymbol{x}$ if and only if $\boldsymbol{A}(\boldsymbol{S} \boldsymbol{x})=\lambda(\boldsymbol{S} \boldsymbol{x})$.
3. If $\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}=\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ we can partition $\boldsymbol{A} \boldsymbol{S}=\boldsymbol{S} \boldsymbol{D}$ by columns to obtain $\left[\boldsymbol{A} \boldsymbol{s}_{1}, \ldots, \boldsymbol{A} \boldsymbol{s}_{n}\right]=\left[\lambda_{1} \boldsymbol{s}_{1}, \ldots, \lambda_{n} \boldsymbol{s}_{n}\right]$. Thus the columns of $\boldsymbol{S}$ are eigenvectors of $\boldsymbol{A}$. Moreover, $\boldsymbol{A}$ is nondefective since $\boldsymbol{S}$ is nonsingular. Conversely, if $\boldsymbol{A}$ is nondefective then it can be diagonalized by a similarity transformation $\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}$, where the columns of $\boldsymbol{S}$ are eigenvectors of $\boldsymbol{A}$.
4. For any square matrices $\boldsymbol{A}, \boldsymbol{C} \in \mathbb{C}^{n \times n}$ the two products $\boldsymbol{A} \boldsymbol{C}$ and $\boldsymbol{C} \boldsymbol{A}$ have the same characteristic polynomial. More generally, for rectangular matrices $\boldsymbol{A} \in$ $\mathbb{C}^{m \times n}$ and $\boldsymbol{C} \in \mathbb{C}^{n \times m}$, with say $m>n$, the bigger matrix has $m-n$ extra zero eigenvalues
$$
\pi_{A C}(\lambda)=\lambda^{m-n} \pi_{C A}(\lambda), \quad \lambda \in \mathbb{C} .
$$
To show this define for any $m, n \in \mathbb{N}$ block triangular matrices of order $n+m$ by
$$
E:=\left[\begin{array}{cc}
A C & 0 \\
C & 0
\end{array}\right], \quad F:=\left[\begin{array}{cc}
0 & 0 \\
C & C A
\end{array}\right], \quad S=\left[\begin{array}{cc}
I & A \\
0 & I
\end{array}\right] .
$$
The matrix $\boldsymbol{S}$ is nonsingular with $\boldsymbol{S}^{-1}=\left[\begin{array}{cc}\boldsymbol{I} & -\boldsymbol{A} \\ \mathbf{0} & \boldsymbol{I}\end{array}\right]$. Moreover, $\boldsymbol{E} \boldsymbol{S}=\boldsymbol{S} \boldsymbol{F}$ so $\boldsymbol{E}$ and $\boldsymbol{F}$ are similar and therefore have the same characteristic polynomials. Moreover, this polynomial is the product of the characteristic polynomial of the diagonal blocks. But then $\pi_{\boldsymbol{E}}(\lambda)=\lambda^{n} \pi_{\boldsymbol{A} \boldsymbol{C}}(\lambda)=\pi_{\boldsymbol{F}}(\lambda)=\lambda^{m} \pi_{\boldsymbol{C} \boldsymbol{A}}(\lambda)$. This implies the statements for $m \geq n$.

### 6.1.2 Algebraic and Geometric Multiplicity of Eigenvalues

Linear independence of eigenvectors depends on the multiplicity of the eigenvalues in a nontrivial way. For multiple eigenvalues we need to distinguish between two kinds of multiplicities.

Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has $k$ distinct eigenvalues $\lambda_{1}, \ldots, \lambda_{k}$ with multiplicities $a_{1}, \ldots, a_{k}$ so that

$$
\pi_{\boldsymbol{A}}(\lambda):=\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=\left(\lambda_{1}-\lambda\right)^{a_{1}} \cdots\left(\lambda_{k}-\lambda\right)^{a_{k}}, \quad \lambda_{i} \neq \lambda_{j}, i \neq j, \sum_{i=1}^{k} a_{i}=n .
$$

The positive integer $a_{i}=a\left(\lambda_{i}\right)=a_{\boldsymbol{A}}\left(\lambda_{i}\right)$ is called the multiplicity, or more precisely the algebraic multiplicity of the eigenvalue $\lambda_{i}$. The multiplicity of an eigenvalue is simple (double, triple) if $a_{i}$ is equal to one (two, three).

To define a second kind of multiplicity we consider for each $\lambda \in \sigma(\boldsymbol{A})$ the nullspace

$$
\mathcal{N}(\boldsymbol{A}-\lambda \boldsymbol{I}):=\left\{\boldsymbol{x} \in \mathbb{C}^{n}:(\boldsymbol{A}-\lambda \boldsymbol{I}) \boldsymbol{x}=\mathbf{0}\right\}
$$

of $\boldsymbol{A}-\lambda \boldsymbol{I}$. The nullspace is a subspace of $\mathbb{C}^{n}$ consisting of all eigenvectors of $\boldsymbol{A}$ corresponding to the eigenvalue $\lambda$. The dimension of the subspace must be at least one since $\boldsymbol{A}-\lambda \boldsymbol{I}$ is singular.

Definition 6.2 (Geometric Multiplicity) The geometric multiplicity $g=g(\lambda)=$ $g_{\boldsymbol{A}}(\lambda)$ of an eigenvalue $\lambda$ of $\boldsymbol{A}$ is the dimension of the nullspace $\mathcal{N}(\boldsymbol{A}-\lambda \boldsymbol{I})$.

Example 6.3 (Geometric Multiplicity) The $n \times n$ identity matrix $\boldsymbol{I}$ has the eigenvalue $\lambda=1$ with $\pi_{\boldsymbol{I}}(\lambda)=(1-\lambda)^{n}$. Since $\boldsymbol{I}-\lambda \boldsymbol{I}$ is the zero matrix when $\lambda=1$, the nullspace of $\boldsymbol{I}-\lambda \boldsymbol{I}$ is all of $n$-space and it follows that $a=g=n$. On the other hand we saw in Example 6.1 that the matrix $\boldsymbol{J}:=\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right]$ has the eigenvalue $\lambda=1$ with $a=2$ and any eigenvector is a multiple of $\boldsymbol{e}_{1}$. Thus $g=1$.

Theorem 6.2 (Geometric Multiplicity of Similar Matrices) Similar matrices have the same eigenvalues with the same algebraic and geometric multiplicities.

Proof Similar matrices have the same characteristic polynomials and only the invariance of geometric multiplicity needs to be shown. Suppose $\lambda \in \sigma(\boldsymbol{A})$, $\operatorname{dim} \mathcal{N}\left(\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}-\lambda \boldsymbol{I}\right)=k$, and $\operatorname{dim} \mathcal{N}(\boldsymbol{A}-\lambda \boldsymbol{I})=\ell$. We need to show that $k=\ell$. Suppose $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{k}$ is a basis for $\mathcal{N}\left(\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}-\lambda \boldsymbol{I}\right)$. Then $\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S} \boldsymbol{v}_{i}=\lambda \boldsymbol{v}_{i}$ or $\boldsymbol{A} \boldsymbol{S} \boldsymbol{v}_{i}=\lambda \boldsymbol{S} \boldsymbol{v}_{i}, i=1, \ldots, k$. But then $\left\{\boldsymbol{S} \boldsymbol{v}_{1}, \ldots, \boldsymbol{S} \boldsymbol{v}_{k}\right\} \subset \mathcal{N}(\boldsymbol{A}-\lambda \boldsymbol{I})$, which implies that $k \leq \ell$. Similarly, if $\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{\ell}$ is a basis for $\mathcal{N}(\boldsymbol{A}-\lambda \boldsymbol{I})$ then $\left\{\boldsymbol{S}^{-1} \boldsymbol{w}_{1}, \ldots, \boldsymbol{S}^{-1} \boldsymbol{w}_{\ell}\right\} \subset \mathcal{N}\left(\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}-\lambda \boldsymbol{I}\right)$. which implies that $k \geq \ell$. We conclude that $k=\ell$. $\square$

For a proof of the following theorem see the next section. ${ }^{1}$
Theorem 6.3 (Geometric Multiplicity) We have

1. The geometric multiplicity of an eigenvalue is always bounded above by the algebraic multiplicity of the eigenvalue.
2. The number of linearly independent eigenvectors of a matrix equals the sum of the geometric multiplicities of the eigenvalues.
3. A matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has $n$ linearly independent eigenvectors if and only if the algebraic and geometric multiplicity of all eigenvalues are the same.

### 6.2 The Jordan Factorization

We have seen that a nondefective matrix can be diagonalized by its eigenvectors, while a defective matrix does not enjoy this property. The following question arises. How close to a diagonal matrix can we reduce a general matrix by a similarity transformation? We give one answer to this question, called the Jordan factorization, or the Jordan canonical form, in Theorem 6.4. For a proof, see for example [10]. The Jordan factorization is an important tool in matrix analysis and it has applications to systems of differential equations, see [8].

The Jordan factorization involves bidiagonal matrices called Jordan blocks.
Definition 6.3 (Jordan Block)
A Jordan block of order $m$, denoted $\boldsymbol{J}_{m}(\lambda)$ is an $m \times m$ matrix of the form

$$
\boldsymbol{J}_{m}(\lambda):=\left[\begin{array}{cccccc}
\lambda & 1 & 0 & \cdots & 0 & 0 \\
0 & \lambda & 1 & \cdots & 0 & 0 \\
0 & 0 & \lambda & \cdots & 0 & 0 \\
\vdots & & & & & \vdots \\
0 & 0 & 0 & \cdots & \lambda & \lambda \\
0 & 0 & 0 & \cdots & 0 & \lambda
\end{array}\right]=\lambda \boldsymbol{I}_{m}+\boldsymbol{E}_{m}, \quad \boldsymbol{E}_{m}:=\left[\begin{array}{cccccc}
0 & 1 & 0 & \cdots & 0 & 0 \\
0 & 0 & 1 & \cdots & 0 & 0 \\
0 & 0 & 0 & \cdots & 0 & 0 \\
\vdots & & & & \vdots \\
0 & 0 & 0 & \cdots & 0 & 1 \\
0 & 0 & 0 & \cdots & 0 & 0
\end{array}\right] .
$$

A $3 \times 3$ Jordan block has the form $\boldsymbol{J}_{3}(\lambda)=\left[\begin{array}{ccc}\lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda\end{array}\right]$. Since a Jordan block is upper triangular $\lambda$ is an eigenvalue of $\boldsymbol{J}_{m}(\lambda)$ and any eigenvector must be a multiple of $\boldsymbol{e}_{1}$. Indeed, if $\boldsymbol{J}_{m}(\lambda) \boldsymbol{v}=\lambda \boldsymbol{v}$ for some $\boldsymbol{v}=\left[v_{1}, \ldots, v_{m}\right]$ then $\lambda v_{i-1}+v_{i}=\lambda v_{i-1}$, $i=2, \ldots, m$ which shows that $v_{2}=\cdots=v_{m}=0$. Thus, the eigenvalue $\lambda$ of $\boldsymbol{J}_{m}(\lambda)$ has algebraic multiplicity $a=m$ and geometric multiplicity $g=1$.

The Jordan factorization is a factorization of a matrix into Jordan blocks.
Theorem 6.4 (The Jordan Factorization of a Matrix)
Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has $k$ distinct eigenvalues $\lambda_{1}, \ldots, \lambda_{k}$ of algebraic multiplicities $a_{1}, \ldots, a_{k}$ and geometric multiplicities $g_{1}, \ldots, g_{k}$. There is a nonsingular matrix

[^11]$\boldsymbol{S} \in \mathbb{C}^{n \times n}$ such that
$$
\boldsymbol{J}:=\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}=\operatorname{diag}\left(\boldsymbol{U}_{1}, \ldots, \boldsymbol{U}_{k}\right), \text { with } \boldsymbol{U}_{i} \in \mathbb{C}^{a_{i} \times a_{i}},
$$
where each $\boldsymbol{U}_{i}$ is block diagonal having $g_{i}$ Jordan blocks along the diagonal
$$
\boldsymbol{U}_{i}=\operatorname{diag}\left(\boldsymbol{J}_{m_{i, 1}}\left(\lambda_{i}\right), \ldots, \boldsymbol{J}_{m_{i, g_{i}}}\left(\lambda_{i}\right)\right) .
$$
Here $m_{i, 1}, \ldots, m_{i, g_{i}}$ are positive integers and they are unique if they are ordered so that $m_{i, 1} \geq m_{i, 2} \geq \cdots \geq m_{i, g_{i}}$. Moreover, $a_{i}=\sum_{j=1}^{g_{i}} m_{i, j}$ for all $i$.

We note that

1. The matrices $\boldsymbol{S}$ and $\boldsymbol{J}$ in (6.5) are called Jordan factors. We also call $\boldsymbol{J}$ the Jordan factorization of $\boldsymbol{A}$.
2. The columns of $\boldsymbol{S}$ are called principal vectors or generalized eigenvectors. They satisfy the matrix equation $\boldsymbol{A} \boldsymbol{S}=\boldsymbol{S} \boldsymbol{J}$.
3. Each $\boldsymbol{U}_{i}$ is upper triangular with the eigenvalue $\lambda_{i}$ on the diagonal and consists of $g_{i}$ Jordan blocks. These Jordan blocks can be taken in any order and it is customary to refer to any such block diagonal matrix as the Jordan factorization of $\boldsymbol{A}$.

Example 6.4 (Jordan Factorization) As an example consider the Jordan factorization

$$
\boldsymbol{J}:=\operatorname{diag}\left(\boldsymbol{U}_{1}, \boldsymbol{U}_{2}\right)=\left[\begin{array}{ccccccc}
2 & 1 & 0 & & & & \\
0 & 2 & 1 & & & & \\
0 & 0 & 2 & & 1 & & \\
& & 0 & 1 & & \\
& & 0 & 2 & & & \\
& & & & & 0 & \\
& & & & & 0 & 1
\end{array}\right] \in \mathbb{R}^{8 \times 8} .
$$

We encountered this matrix in Exercise 6.1. The eigenvalues together with their algebraic and geometric multiplicities can be read off directly from the Jordan factorization.

- $\boldsymbol{U}_{1}=\operatorname{diag}\left(\boldsymbol{J}_{3}(2), \boldsymbol{J}_{2}(2), \boldsymbol{J}_{1}(2)\right)$ and $\boldsymbol{U}_{2}=\boldsymbol{J}_{2}(3)$.
- 2 is an eigenvalue of algebraic multiplicity 6 and geometric multiplicity 3, the number of Jordan blocks corresponding to $\lambda=2$.
- 3 is an eigenvalue of algebraic multiplicity 2 and geometric multiplicity 1.

The columns of $\boldsymbol{S}=\left[\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{8}\right]$ are determined from the columns of $\boldsymbol{J}$ as follows

$$
\begin{aligned}
& \boldsymbol{A} \boldsymbol{s}_{1}=2 \boldsymbol{s}_{1}, \quad \boldsymbol{A} \boldsymbol{s}_{2}=\boldsymbol{s}_{1}+2 \boldsymbol{s}_{2}, \quad \boldsymbol{A} \boldsymbol{s}_{3}=\boldsymbol{s}_{2}+2 \boldsymbol{s}_{3}, \\
& \boldsymbol{A} \boldsymbol{s}_{4}=2 \boldsymbol{s}_{4}, \quad \boldsymbol{A} \boldsymbol{s}_{5}=\boldsymbol{s}_{4}+2 \boldsymbol{s}_{5} \\
& \boldsymbol{A} \boldsymbol{s}_{6}=2 \boldsymbol{s}_{6}, \\
& \boldsymbol{A} \boldsymbol{s}_{7}=3 \boldsymbol{s}_{7}, \quad \boldsymbol{A} \boldsymbol{s}_{8}=\boldsymbol{s}_{7}+3 \boldsymbol{s}_{8} .
\end{aligned}
$$

We see that the generalized eigenvector corresponding to the first column in a Jordan block is an eigenvector of $\boldsymbol{A}$. The remaining generalized eigenvectors are not eigenvectors.

The matrix

$$
\boldsymbol{J}:=\left[\begin{array}{ccccccc}
3 & 1 & & & & & \\
0 & 3 & & & & & \\
& & 2 & 1 & & & \\
& & 0 & 2 & & & \\
& & & & 2 & & \\
& & & & 0 & 1 & 0 \\
& & & & 0 & 2 & 1 \\
& & & & 0 & 2
\end{array}\right]
$$

is also a Jordan factorization of $\boldsymbol{A}$. In any Jordan factorization of this $\boldsymbol{A}$ the sizes of the 4 Jordan blocks $\boldsymbol{J}_{2}(3), \boldsymbol{J}_{2}(2), \boldsymbol{J}_{1}(2), \boldsymbol{J}_{3}(2)$ are uniquely given.

Proof of Theorem 6.3

1. The algebraic multiplicity $a_{i}$ of an eigenvalue $\lambda_{i}$ is equal to the size of the corresponding $\boldsymbol{U}_{i}$. Moreover each $\boldsymbol{U}_{i}$ contains $g_{i}$ Jordan blocks of size $m_{i, j} \geq 1$. Thus $g_{i} \leq a_{i}$.
2. Since $\boldsymbol{A}$ and $\boldsymbol{J}$ are similar the geometric multiplicities of the eigenvalues of these matrices are the same, and it is enough to prove statement 2 for the Jordan factor $\boldsymbol{J}$. We show this only for the matrix $\boldsymbol{J}$ given by (6.7). The general case should then be clear. There are only 4 eigenvectors of $\boldsymbol{J}$, namely $\boldsymbol{e}_{1}, \boldsymbol{e}_{4}, \boldsymbol{e}_{6}, \boldsymbol{e}_{7}$ corresponding to the 4 Jordan blocks. These 4 vectors are clearly linearly independent. Moreover there are $k=2$ distinct eigenvalues and $g_{1}+g_{2}=$ $3+1=4$.
3. Since $g_{i} \leq a_{i}$ for all $i$ and $\sum_{i} a_{i}=n$ we have $\sum_{i} g_{i}=n$ if and only if $a_{i}=g_{i}$ for $i=1, \ldots, k$.

### 6.3 The Schur Factorization and Normal Matrices

### 6.3.1 The Schur Factorization

We turn now to unitary similarity transformations $\boldsymbol{S}^{-1} \boldsymbol{A} \boldsymbol{S}$, where $\boldsymbol{S}=\boldsymbol{U}$ is unitary. Thus $\boldsymbol{S}^{-1}=\boldsymbol{U}^{*}$ and a unitary similarity transformation takes the form $\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}$.

### 6.3.2 Unitary and Orthogonal Matrices

Although not every matrix can be diagonalized it can be brought into triangular form by a unitary similarity transformation.

Theorem 6.5 (Schur Factorization) For each $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ there exists a unitary matrix $\boldsymbol{U} \in \mathbb{C}^{n \times n}$ such that $\boldsymbol{R}:=\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}$ is upper triangular.

The matrices $\boldsymbol{U}$ and $\boldsymbol{R}$ in the Schur factorization are called Schur factors. We call $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{R} \boldsymbol{U}^{*}$ the Schur factorization of $\boldsymbol{A}$.

Proof We use induction on $n$. For $n=1$ the matrix $\boldsymbol{U}$ is the $1 \times 1$ identity matrix. Assume that the theorem is true for all $k \times k$ matrices, and suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$, where $n:=k+1$. Let $\left(\lambda_{1}, \boldsymbol{v}_{1}\right)$ be an eigenpair for $\boldsymbol{A}$ with $\left\|\boldsymbol{v}_{1}\right\|_{2}=1$. By Theorem 5.5 we can extend $\boldsymbol{v}_{1}$ to an orthonormal basis $\left\{\boldsymbol{v}_{1}, \boldsymbol{v}_{2}, \ldots, \boldsymbol{v}_{n}\right\}$ for $\mathbb{C}^{n}$. The matrix $\boldsymbol{V}:=$ $\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right] \in \mathbb{C}^{n \times n}$ is unitary, and

$$
\boldsymbol{V}^{*} \boldsymbol{A} \boldsymbol{V} \boldsymbol{e}_{1}=\boldsymbol{V}^{*} \boldsymbol{A} \boldsymbol{v}_{1}=\lambda_{1} \boldsymbol{V}^{*} \boldsymbol{v}_{1}=\lambda_{1} \boldsymbol{e}_{1} .
$$

It follows that

$$
\boldsymbol{V}^{*} \boldsymbol{A} \boldsymbol{V}=\left[\begin{array}{c|c}
\lambda_{1} & \boldsymbol{x}^{*} \\
\hline \mathbf{0} & \boldsymbol{M}
\end{array}\right], \text { for some } \boldsymbol{M} \in \mathbb{C}^{k \times k} \text { and } \boldsymbol{x} \in \mathbb{C}^{k} .
$$

By the induction hypothesis there is a unitary matrix $\boldsymbol{W}_{1} \in \mathbb{C}^{(n-1) \times(n-1)}$ such that $\boldsymbol{W}_{1}^{*} \boldsymbol{M} \boldsymbol{W}_{1}$ is upper triangular. Define

$$
\boldsymbol{W}=\left[\begin{array}{c|c}
1 & \mathbf{0}^{*} \\
\hline \mathbf{0} & \boldsymbol{W}_{1}
\end{array}\right] \text { and } \boldsymbol{U}=\boldsymbol{V} \boldsymbol{W} .
$$

Then $\boldsymbol{W}$ and $\boldsymbol{U}$ are unitary and

$$
\begin{aligned}
\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}=\boldsymbol{W}^{*}\left(\boldsymbol{V}^{*} \boldsymbol{A} \boldsymbol{V}\right) \boldsymbol{W} & =\left[\begin{array}{l|l}
1 & \mathbf{0}^{*} \\
\hline \mathbf{0} & \boldsymbol{W}_{1}^{*}
\end{array}\right]\left[\begin{array}{l|l}
\lambda_{1} & \boldsymbol{x}^{*} \\
\hline \mathbf{0} & \boldsymbol{M}
\end{array}\right]\left[\begin{array}{l|l}
1 & \mathbf{0}^{*} \\
\hline \mathbf{0} & \boldsymbol{W}_{1}
\end{array}\right] \\
& =\left[\begin{array}{l|l}
\lambda_{1} & \boldsymbol{x}^{*} \boldsymbol{W}_{1} \\
\hline \mathbf{0} & \boldsymbol{W}_{1}^{*} \boldsymbol{M} \boldsymbol{W}_{1}
\end{array}\right]
\end{aligned}
$$

is upper triangular. $\square$

If $\boldsymbol{A}$ has complex eigenvalues then $\boldsymbol{U}$ will be complex even if $\boldsymbol{A}$ is real. The following is a real version of Theorem 6.5.

Theorem 6.6 (Schur Form, Real Eigenvalues) For each $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ with real eigenvalues there exists an orthogonal matrix $\boldsymbol{U} \in \mathbb{R}^{n \times n}$ such that $\boldsymbol{U}^{T} \boldsymbol{A U}$ is upper triangular.

Proof Consider the proof of Theorem 6.5. Since $\boldsymbol{A}$ and $\lambda_{1}$ are real the eigenvector $\boldsymbol{v}_{1}$ is real and the matrix $\boldsymbol{W}$ is real and $\boldsymbol{W}^{T} \boldsymbol{W}=\boldsymbol{I}$. By the induction hypothesis $\boldsymbol{V}$ is real and $\boldsymbol{V}^{T} \boldsymbol{V}=\boldsymbol{I}$. But then also $\boldsymbol{U}=\boldsymbol{V} \boldsymbol{W}$ is real and $\boldsymbol{U}^{T} \boldsymbol{U}=\boldsymbol{I}$. $\square$

A real matrix with some complex eigenvalues can only be reduced to block triangular form by a real unitary similarity transformation. We consider this in Sect. 6.3.5.

Example 6.5 (Deflation Example) By using the unitary transformation $\boldsymbol{V}$ on the $n \times n$ matrix $\boldsymbol{A}$, we obtain a matrix $\boldsymbol{M}$ of order $n-1 . \boldsymbol{M}$ has the same eigenvalues as $\boldsymbol{A}$ except $\lambda$. Thus we can find another eigenvalue of $\boldsymbol{A}$ by working with a smaller matrix $\boldsymbol{M}$. This is an example of a deflation technique which is very useful in numerical work. The second derivative matrix $\boldsymbol{T}:=\left[\begin{array}{ccc}2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2\end{array}\right]$ has an eigenpair $\left(2, \boldsymbol{x}_{1}\right)$, where $\boldsymbol{x}_{1}=[-1,0,1]^{T}$. Find the remaining eigenvalues using deflation. For this we extend $\boldsymbol{x}_{1}$ to a basis $\left\{\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \boldsymbol{x}_{3}\right\}$ for $\mathbb{R}^{3}$ by defining $\boldsymbol{x}_{2}=[0,1,0]^{T}$, $\boldsymbol{x}_{3}=[1,0,1]^{T}$. This is already an orthogonal basis and normalizing we obtain the orthogonal matrix

$$
\boldsymbol{V}=\left[\begin{array}{ccc}
-\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \\
0 & 1 & 0 \\
\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}}
\end{array}\right] .
$$

We obtain (6.8) with $\lambda=2$ and

$$
\boldsymbol{M}=\left[\begin{array}{cc}
2 & -\sqrt{2} \\
-\sqrt{2} & 2
\end{array}\right] .
$$

We can now find the remaining eigenvalues of $\boldsymbol{A}$ from the $2 \times 2$ matrix $\boldsymbol{M}$.

### 6.3.3 Normal Matrices

A matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is normal if $\boldsymbol{A}^{*} \boldsymbol{A}=\boldsymbol{A} \boldsymbol{A}^{*}$. In this section we show that a matrix has orthogonal eigenvectors if and only if it is normal.

Examples of normal matrices are

1. $\boldsymbol{A}^{*}=\boldsymbol{A}$,

(Hermitian)

2. $\boldsymbol{A}^{*}=-\boldsymbol{A}$,

(Skew-Hermitian)

3. $\boldsymbol{A}^{*}=\boldsymbol{A}^{-1}$,

(Unitary)

4. $\boldsymbol{A}=\operatorname{diag}\left(d_{1}, \ldots, d_{n}\right)$.

(Diagonal)
Clearly the matrices in 1. 2. 3. are normal. If $\boldsymbol{A}$ is diagonal then

$$
\boldsymbol{A}^{*} \boldsymbol{A}=\operatorname{diag}\left(\overline{d_{1}} d_{1}, \ldots, \overline{d_{n}} d_{n}\right)=\operatorname{diag}\left(\left|d_{1}\right|^{2}, \ldots,\left|d_{n}\right|^{2}\right)=\boldsymbol{A} \boldsymbol{A}^{*},
$$

and $\boldsymbol{A}$ is normal. The 2. derivative matrix $\boldsymbol{T}$ in (2.27) is symmetric and therefore normal. The eigenvalues of a normal matrix can be complex (cf. Exercise 6.21). However in the Hermitian case the eigenvalues are real (cf. Lemma 2.3).

The following theorem shows that $\boldsymbol{A}$ has a set of orthogonal eigenvectors if and only if it is normal.

Theorem 6.7 (Spectral Theorem for Normal Matrices) A matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is normal if and only if there exists a unitary matrix $\boldsymbol{U} \in \mathbb{C}^{n \times n}$ such that $\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}=\boldsymbol{D}$ is diagonal. If $\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ and $\boldsymbol{U}=\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{n}\right]$ then $\left(\lambda_{j}, \boldsymbol{u}_{j}\right), j=$ $1, \ldots, n$ are orthonormal eigenpairs for $\boldsymbol{A}$.

Proof If $\boldsymbol{B}=\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}$, with $\boldsymbol{B}$ diagonal, and $\boldsymbol{U}^{*} \boldsymbol{U}=\boldsymbol{I}$, then $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{B} \boldsymbol{U}^{*}$ and

$$
\begin{aligned}
\boldsymbol{A} \boldsymbol{A}^{*} & =\left(\boldsymbol{U} \boldsymbol{B} \boldsymbol{U}^{*}\right)\left(\boldsymbol{U} \boldsymbol{B}^{*} \boldsymbol{U}^{*}\right)=\boldsymbol{U} \boldsymbol{B} \boldsymbol{B}^{*} \boldsymbol{U}^{*} \text { and } \\
\boldsymbol{A}^{*} \boldsymbol{A} & =\left(\boldsymbol{U} \boldsymbol{B}^{*} \boldsymbol{U}^{*}\right)\left(\boldsymbol{U} \boldsymbol{B} \boldsymbol{U}^{*}\right)=\boldsymbol{U} \boldsymbol{B}^{*} \boldsymbol{B} \boldsymbol{U}^{*} .
\end{aligned}
$$

Now $\boldsymbol{B} \boldsymbol{B}^{*}=\boldsymbol{B}^{*} \boldsymbol{B}$ since $\boldsymbol{B}$ is diagonal, and $\boldsymbol{A}$ is normal.
Conversely, suppose $\boldsymbol{A}^{*} \boldsymbol{A}=\boldsymbol{A} \boldsymbol{A}^{*}$. By Theorem 6.5 we can find $\boldsymbol{U}$ with $\boldsymbol{U}^{*} \boldsymbol{U}=$ $\boldsymbol{I}$ such that $\boldsymbol{B}:=\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}$ is upper triangular. Since $\boldsymbol{A}$ is normal $\boldsymbol{B}$ is normal. Indeed,

$$
\boldsymbol{B} \boldsymbol{B}^{*}=\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U} \boldsymbol{U}^{*} \boldsymbol{A}^{*} \boldsymbol{U}=\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{A}^{*} \boldsymbol{U}=\boldsymbol{U}^{*} \boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{U}=\boldsymbol{B}^{*} \boldsymbol{B} .
$$

The proof is complete if we can show that an upper triangular normal matrix $\boldsymbol{B}$ must be diagonal. The diagonal elements $e_{i i}$ in $\boldsymbol{E}:=\boldsymbol{B}^{*} \boldsymbol{B}$ and $f_{i i}$ in $\boldsymbol{F}:=\boldsymbol{B B}^{*}$ are given by

$$
e_{i i}=\sum_{k=1}^{n} \bar{b}_{k i} b_{k i}=\sum_{k=1}^{i}\left|b_{k i}\right|^{2} \text { and } f_{i i}=\sum_{k=1}^{n} b_{i k} \bar{b}_{i k}=\sum_{k=i}^{n}\left|b_{i k}\right|^{2} .
$$

The result now follows by equating $e_{i i}$ and $f_{i i}$ for $i=1,2, \ldots, n$. In particular for $i=1$ we have $\left|b_{11}\right|^{2}=\left|b_{11}\right|^{2}+\left|b_{12}\right|^{2}+\cdots+\left|b_{1 n}\right|^{2}$, so $b_{1 k}=0$ for $k=2,3, \ldots, n$. Suppose $\boldsymbol{B}$ is diagonal in its first $i-1$ rows so that $b_{j k}=0$ for $j=1, \ldots, i-1$, $k=j+1, \ldots, n$. Then

$$
e_{i i}=\sum_{k=1}^{i}\left|b_{k i}\right|^{2}=\left|b_{i i}\right|^{2}=\sum_{k=i}^{n}\left|b_{i k}\right|^{2}=f_{i i}
$$

and it follows that $b_{i k}=0, k=i+1, \ldots, n$. By induction on the rows we see that $\boldsymbol{B}$ is diagonal. The last part of the theorem follows from Sect. 6.1.1. $\square$

Example 6.6 The orthogonal diagonalization of $\boldsymbol{A}=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$ is $\boldsymbol{U}^{T} \boldsymbol{A} \boldsymbol{U}=$ $\operatorname{diag}(1,3)$, where $\boldsymbol{U}=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}1 & 1 \\ 1 & -1\end{array}\right]$.

### 6.3.4 The Rayleigh Quotient

The Rayleigh quotient is a useful tool when studying eigenvalues.
Definition 6.4 (Rayleigh Quotient) For $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ and a nonzero $\boldsymbol{x}$ the number

$$
R(x)=R_{A}(x):=\frac{x^{*} A x}{x^{*} x}
$$

is called a Rayleigh quotient.
If ( $\lambda, \boldsymbol{x}$ ) is an eigenpair for $\boldsymbol{A}$ then $R(\boldsymbol{x})=\frac{\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}}{\boldsymbol{x}^{*} \boldsymbol{x}}=\lambda$.
Equation (6.9) in the following theorem shows that the Rayleigh quotient of a normal matrix is a convex combination of its eigenvalues.

Theorem 6.8 (Convex Combination of the Eigenvalues) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is normal with orthonormal eigenpairs ( $\lambda_{j}, \boldsymbol{u}_{j}$ ), for $j=1,2, \ldots, n$. Then the Rayleigh quotient is a convex combination of the eigenvalues of $\boldsymbol{A}$

$$
R_{\boldsymbol{A}}(\boldsymbol{x})=\frac{\sum_{i=1}^{n} \lambda_{i}\left|c_{i}\right|^{2}}{\sum_{j=1}^{n}\left|c_{j}\right|^{2}}, \quad \boldsymbol{x} \neq \mathbf{0}, \quad \boldsymbol{x}=\sum_{j=1}^{n} c_{j} \boldsymbol{u}_{j} .
$$

Proof By orthonormality of the eigenvectors $\boldsymbol{x}^{*} \boldsymbol{x}=\sum_{i=1}^{n} \sum_{j=1}^{n} \bar{c}_{i} \overline{\boldsymbol{u}}_{i} c_{j} \boldsymbol{u}_{j}=$ $\sum_{j=1}^{n}\left|c_{j}\right|^{2}$. Similarly, $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=\sum_{i=1}^{n} \sum_{j=1}^{n} \bar{c}_{i} \overline{\boldsymbol{u}}_{i} c_{j} \lambda_{j} \boldsymbol{u}_{j}=\sum_{i=1}^{n} \lambda_{i}\left|c_{i}\right|^{2}$. and (6.9) follows. This is clearly a combination of nonnegative quantities and a convex combination since $\sum_{i=1}^{n}\left|c_{i}\right|^{2} / \sum_{j=1}^{n}\left|c_{j}\right|^{2}=1$. $\square$

### 6.3.5 The Quasi-Triangular Form

How far can we reduce a real matrix $\boldsymbol{A}$ with some complex eigenvalues by a real unitary similarity transformation? To study this we note that the complex eigenvalues of a real matrix occur in conjugate pairs, $\lambda=\mu+i \nu, \bar{\lambda}=\mu-i \nu$, where $\mu, \nu$ are real. The real $2 \times 2$ matrix

$$
\boldsymbol{M}=\left[\begin{array}{cc}
\mu & v \\
-v & \mu
\end{array}\right]
$$

has eigenvalues $\lambda=\mu+i \nu$ and $\bar{\lambda}=\mu-i \nu$.
Definition 6.5 (Quasi-Triangular Matrix) We say that a matrix is quasitriangular if it is block triangular with only 1 × 1 and 2 × 2 blocks on the diagonal. Moreover, no 2 × 2 block should have real eigenvalues.

As an example consider the matrix

$$
\boldsymbol{R}:=\left[\begin{array}{ccc}
\boldsymbol{D}_{1} & \boldsymbol{R}_{1,2} & \boldsymbol{R}_{1,3} \\
\mathbf{0} & \boldsymbol{D}_{2} & \boldsymbol{R}_{2,3} \\
\mathbf{0} & \mathbf{0} & \boldsymbol{D}_{3}
\end{array}\right], \boldsymbol{D}_{1}:=\left[\begin{array}{cc}
2 & 1 \\
-1 & 2
\end{array}\right], \boldsymbol{D}_{2}:=[1], \boldsymbol{D}_{3}:=\left[\begin{array}{cc}
3 & 2 \\
-1 & 1
\end{array}\right] .
$$

Since $\boldsymbol{R}$ is block triangular the characteristic polynomial of $\boldsymbol{R}$ is given by $\pi_{\boldsymbol{R}}=$ $\boldsymbol{\pi}_{\boldsymbol{D}_{1}} \boldsymbol{\pi}_{\boldsymbol{D}_{2}} \boldsymbol{\pi}_{\boldsymbol{D}_{3}}$. We find

$$
\pi_{D_{1}}(\lambda)=\pi_{D_{3}}(\lambda)=\lambda^{2}-4 \lambda+5, \quad \pi_{D_{2}}(\lambda)=\lambda-1,
$$

and the eigenvalues $\boldsymbol{D}_{1}$ and $\boldsymbol{D}_{3}$ are $\lambda_{1}=2+i, \lambda_{2}=2-i$, while $\boldsymbol{D}_{2}$ obviously has the eigenvalue $\lambda=1$.

Any $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ can be reduced to quasi-triangular form by a real orthogonal similarity transformation. For a proof see [16]. We will encounter the quasitriangular form in Chap. 15.

### 6.3.6 Hermitian Matrices

The special cases where $\boldsymbol{A}$ is Hermitian, or real and symmetric, deserve special attention.

Theorem 6.9 (Spectral Theorem, Complex Form) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is Hermitian. Then $\boldsymbol{A}$ has real eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$. Moreover, there is a unitary matrix $\boldsymbol{U} \in \mathbb{C}^{n \times n}$ such that

$$
\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right) .
$$

For any such $\boldsymbol{U}$ the columns $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{n}\right\}$ of $\boldsymbol{U}$ are orthonormal eigenvectors of $\boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{u}_{j}=\lambda_{j} \boldsymbol{u}_{j}$ for $j=1, \ldots, n$.

Proof That the eigenvalues are real was shown in Lemma 2.3. The rest follows from Theorem 6.7. $\square$

There is also a real version.
Theorem 6.10 (Spectral Theorem (Real Form)) Suppose $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is symmetric. Then $\boldsymbol{A}$ has real eigenvalues $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}$. Moreover, there is an orthogonal matrix $\boldsymbol{U} \in \mathbb{R}^{n \times n}$ such that

$$
\boldsymbol{U}^{T} \boldsymbol{A} \boldsymbol{U}=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{n}\right) .
$$

For any such $\boldsymbol{U}$ the columns $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{n}\right\}$ of $\boldsymbol{U}$ are orthonormal eigenvectors of $\boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{u}_{j}=\lambda_{j} \boldsymbol{u}_{j}$ for $j=1, \ldots, n$.

Proof Since a real symmetric matrix has real eigenvalues and eigenvectors this follows from Theorem 6.9. $\square$

### 6.4 Minmax Theorems

There are some useful characterizations of the eigenvalues of a Hermitian matrix in terms of the Rayleigh quotient $R(\boldsymbol{x})=R_{\boldsymbol{A}}(\boldsymbol{x}):=\frac{\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}}{\boldsymbol{x}^{*} \boldsymbol{x}}$. First we show
Theorem 6.11 (Minmax) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is Hermitian with orthonormal eigenpairs $\left(\lambda_{j}, \boldsymbol{u}_{j}\right), 1 \leq j \leq n$, ordered so that $\lambda_{1} \geq \cdots \geq \lambda_{n}$. Let $1 \leq k \leq n$. For any subspace $\mathcal{S}$ of $\mathbb{C}^{n}$ of dimension $n-k+1$

$$
\lambda_{k} \leq \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\ \boldsymbol{x} \neq \mathbf{0}}} R(\boldsymbol{x}),
$$

with equality for $\mathcal{S}=\tilde{\mathcal{S}}:=\operatorname{span}\left(\boldsymbol{u}_{k}, \ldots, \boldsymbol{u}_{n}\right)$ and $\boldsymbol{x}=\boldsymbol{u}_{k}$.
Proof Let $\mathcal{S}$ be any subspace of $\mathbb{C}^{n}$ of dimension $n-k+1$ and define $\mathcal{S}^{\prime}:=$ $\operatorname{span}\left(\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{k}\right)$. It is enough to find $\boldsymbol{y} \in \mathcal{S}$ so that $R(\boldsymbol{y}) \geq \lambda_{k}$. Now $\mathcal{S}+\mathcal{S}^{\prime}:=$ $\left\{\boldsymbol{s}+\boldsymbol{s}^{\prime}: \boldsymbol{s} \in \mathcal{S}, \boldsymbol{s}^{\prime} \in \mathcal{S}^{\prime}\right\}$ is a subspace of $\mathbb{C}^{n}$ and by (1.7)

$$
\operatorname{dim}\left(\mathcal{S} \cap \mathcal{S}^{\prime}\right)=\operatorname{dim}(\mathcal{S})+\operatorname{dim}\left(\mathcal{S}^{\prime}\right)-\operatorname{dim}\left(\mathcal{S}+\mathcal{S}^{\prime}\right) \geq(n-k+1)+k-n=1 .
$$

It follows that $\mathcal{S} \cap \mathcal{S}^{\prime}$ is nonempty. Let $\boldsymbol{y} \in \mathcal{S} \cap \mathcal{S}^{\prime}=\sum_{j=1}^{k} c_{j} \boldsymbol{u}_{j}$ with $\sum_{j=1}^{k}\left|c_{j}\right|^{2}=$ 1. Defining $c_{j}=0$ for $k+1 \leq j \leq n$, we obtain by Theorem 6.8

$$
\max _{\substack{x \in \mathcal{S} \\ \boldsymbol{x} \neq \mathbf{0}}} R(\boldsymbol{x}) \geq R(\boldsymbol{y})=\sum_{j=1}^{n} \lambda_{j}\left|c_{j}\right|^{2}=\sum_{j=1}^{k} \lambda_{j}\left|c_{j}\right|^{2} \geq \sum_{j=1}^{k} \lambda_{k}\left|c_{j}\right|^{2}=\lambda_{k},
$$

and (6.11) follows. To show equality suppose $\boldsymbol{z} \in \mathcal{S}=\tilde{\mathcal{S}}$. Now $\boldsymbol{z}=\sum_{j=k}^{n} d_{j} \boldsymbol{u}_{j}$ for some $d_{k}, \ldots, d_{n}$ with $\sum_{j=k}^{n}\left|d_{j}\right|^{2}=1$ and by Lemma $6.8 R(z)=\sum_{j=k}^{n} \lambda_{j}\left|d_{j}\right|^{2} \leq$ $\lambda_{k}$. Since $\boldsymbol{z} \in \tilde{\mathcal{S}}$ is arbitrary we have $\max _{\substack{\boldsymbol{x} \in \tilde{\mathcal{S}} \\ \boldsymbol{x} \neq \mathbf{0}}} R(\boldsymbol{x}) \leq \lambda_{k}$ and equality in (6.11) follows for $\mathcal{S}=\tilde{\mathcal{S}}$. Moreover, $R\left(\boldsymbol{u}_{k}\right)=\lambda_{k}$. $\square$

There is also a maxmin version of this result.
Theorem 6.12 (Maxmin) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is Hermitian with eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$, ordered so that $\lambda_{1} \geq \cdots \geq \lambda_{n}$. Let $1 \leq k \leq n$. For any subspace $\mathcal{S}$ of $\mathbb{C}^{n}$ of dimension $k$

$$
\lambda_{k} \geq \min _{\substack{\boldsymbol{x} \in \mathcal{S} \\ \boldsymbol{x} \neq \mathbf{0}}} R(\boldsymbol{x}),
$$

with equality for $\mathcal{S}=\tilde{\mathcal{S}}:=\operatorname{span}\left(\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{k}\right)$ and $\boldsymbol{x}=\boldsymbol{u}_{k}$. Here $\left(\lambda_{j}, \boldsymbol{u}_{j}\right), 1 \leq j \leq$ $n$ are orthonormal eigenpairs for $\boldsymbol{A}$.

Proof The proof is very similar to the proof of Theorem 6.11. We define $\mathcal{S}^{\prime}:=$ $\operatorname{span}\left(\boldsymbol{u}_{k}, \ldots, \boldsymbol{u}_{n}\right)$ and show that $R(\boldsymbol{y}) \leq \lambda_{k}$ for some $\boldsymbol{y} \in \mathcal{S} \cap \mathcal{S}^{\prime}$. It is easy to see that $R(\boldsymbol{y}) \geq \lambda_{k}$ for any $\boldsymbol{y} \in \tilde{\mathcal{S}}$. $\square$

These theorems immediately lead to classical minmax and maxmin characterizations.

Corollary 6.1 (The Courant-Fischer Theorem) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is Hermitian with eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$, ordered so that $\lambda_{1} \geq \cdots \geq \lambda_{n}$. Then

$$
\lambda_{k}=\min _{\operatorname{dim}(\mathcal{S})=n-k+1} \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\ \boldsymbol{x} \neq \mathbf{0}}} R(\boldsymbol{x})=\max _{\operatorname{dim}(\mathcal{S})=k} \min _{\substack{\boldsymbol{x} \in \mathcal{S} \\ \boldsymbol{x} \neq \mathbf{0}}} R(\boldsymbol{x}), \quad k=1, \ldots, n .
$$

Using Theorem 6.11 we can prove inequalities of eigenvalues without knowing the eigenvectors and we can get both upper and lower bounds.

Theorem 6.13 (Eigenvalue Perturbation for Hermitian Matrices) Let $\boldsymbol{A}, \boldsymbol{B} \in$ $\mathbb{C}^{n \times n}$ be Hermitian with eigenvalues $\alpha_{1} \geq \alpha_{2} \geq \cdots \geq \alpha_{n}$ and $\beta_{1} \geq \beta_{2} \geq \cdots \geq \beta_{n}$. Then

$$
\alpha_{k}+\varepsilon_{n} \leq \beta_{k} \leq \alpha_{k}+\varepsilon_{1}, \text { for } k=1, \ldots, n,
$$

where $\varepsilon_{1} \geq \varepsilon_{2} \geq \cdots \geq \varepsilon_{n}$ are the eigenvalues of $\boldsymbol{E}:=\boldsymbol{B}-\boldsymbol{A}$.
Proof Since $\boldsymbol{E}$ is a difference of Hermitian matrices it is Hermitian and the eigenvalues are real. Let $\left(\alpha_{j}, \boldsymbol{u}_{j}\right), j=1, \ldots, n$ be orthonormal eigenpairs for $\boldsymbol{A}$ and let $\mathcal{S}:=\operatorname{span}\left\{\boldsymbol{u}_{k}, \ldots, \boldsymbol{u}_{n}\right\}$. By Theorem 6.11 we obtain

$$
\begin{aligned}
\beta_{k} & \leq \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\
\boldsymbol{x} \neq \mathbf{0}}} R_{\boldsymbol{B}}(\boldsymbol{x}) \leq \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\
\boldsymbol{x} \neq \mathbf{0}}} R_{\boldsymbol{A}}(\boldsymbol{x})+\max _{\substack{\boldsymbol{x} \in S \\
\boldsymbol{x} \neq \mathbf{0}}} R_{\boldsymbol{E}}(\boldsymbol{x}) \\
& \leq \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\
\boldsymbol{x} \neq \mathbf{0}}} R_{\boldsymbol{A}}(\boldsymbol{x})+\max _{\substack{\boldsymbol{x} \in \mathbb{C}^{n} \\
\boldsymbol{x} \neq \mathbf{0}}} R_{\boldsymbol{E}}(\boldsymbol{x})=\alpha_{k}+\varepsilon_{1},
\end{aligned}
$$

and this proves the upper inequality. For the lower one we define $\boldsymbol{D}:=-\boldsymbol{E}$ and observe that $-\varepsilon_{n}$ is the largest eigenvalue of $\boldsymbol{D}$. Since $\boldsymbol{A}=\boldsymbol{B}+\boldsymbol{D}$ it follows from the result just proved that $\alpha_{k} \leq \beta_{k}-\varepsilon_{n}$, which is the same as the lower inequality. $\square$

In many applications of this result the eigenvalues of the matrix $\boldsymbol{E}$ will be small and then the theorem states that the eigenvalues of $\boldsymbol{B}$ are close to those of $\boldsymbol{A}$. Moreover, it associates a unique eigenvalue of $\boldsymbol{A}$ with each eigenvalue of $\boldsymbol{B}$.

### 6.4.1 The Hoffman-Wielandt Theorem

We can also give a bound involving all eigenvalues. The following theorem shows that the eigenvalue problem for a normal matrix is well conditioned.

Theorem 6.14 (Hoffman-Wielandt Theorem) Suppose $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$ are both normal matrices with eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$ and $\mu_{1}, \ldots, \mu_{n}$, respectively. Then there is a permutation $i_{1}, \ldots, i_{n}$ of $1,2, \ldots, n$ such that

$$
\sum_{j=1}^{n}\left|\mu_{i_{j}}-\lambda_{j}\right|^{2} \leq \sum_{i=1}^{n} \sum_{j=1}^{n}\left|a_{i j}-b_{i j}\right|^{2}
$$

For a proof of this theorem see [19, p. 190]. For a Hermitian matrix we can use the identity permutation if we order both set of eigenvalues in nonincreasing or nondecreasing order.

### 6.5 Left Eigenvectors

Definition 6.6 (Left and Right Eigenpairs) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is a square matrix, $\lambda \in \mathbb{C}$ and $\boldsymbol{y} \in \mathbb{C}^{n}$ is nonzero. We say that ( $\lambda, \boldsymbol{y}$ ) is a left eigenpair for $\boldsymbol{A}$ if $\boldsymbol{y}^{*} \boldsymbol{A}=\lambda \boldsymbol{y}^{*}$ or equivalently $\boldsymbol{A}^{*} \boldsymbol{y}=\bar{\lambda} \boldsymbol{y}$. We say that ( $\lambda, \boldsymbol{y}$ ) is a right eigenpair for $\boldsymbol{A}$ if $\boldsymbol{A} \boldsymbol{y}=\lambda \boldsymbol{y}$. If $(\lambda, \boldsymbol{y})$ is a left eigenpair then $\lambda$ is called a left eigenvalue and $\boldsymbol{y}$ a left eigenvector. Similarly if $(\lambda, y)$ is a right eigenpair then $\lambda$ is called a right eigenvalue and $\boldsymbol{y}$ a right eigenvector.

In this book an eigenpair will always mean a right eigenpair. A left eigenvector is an eigenvector of $\boldsymbol{A}^{*}$. If $\lambda$ is a left eigenvalue of $\boldsymbol{A}$ then $\bar{\lambda}$ is an eigenvalue of $\boldsymbol{A}^{*}$ and then $\lambda$ is an eigenvalue of $\boldsymbol{A}$ (cf. Exercise 6.3). Thus left and right eigenvalues are identical, but left and right eigenvectors are in general different. For a Hermitian matrix the right and left eigenpairs are the same.

Using right and left linearly independent eigenpairs we get some useful eigenvector expansions.

Theorem 6.15 (Biorthogonal Eigenvector Expansion) If $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has linearly independent right eigenvectors $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ then there exists a set of left eigenvectors $\left\{\boldsymbol{y}_{1}, \ldots, \boldsymbol{y}_{n}\right\}$ with $\boldsymbol{y}_{i}^{*} \boldsymbol{x}_{j}=\delta_{i, j}$. Conversely, if $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has linearly independent left eigenvectors $\left\{\boldsymbol{y}_{1}, \ldots, \boldsymbol{y}_{n}\right\}$ then there exists a set of right eigenvectors $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ with $\boldsymbol{y}_{i}^{*} \boldsymbol{x}_{j}=\delta_{i, j}$. For any scaling of these sets we have the eigenvector expansions

$$
\boldsymbol{v}=\sum_{j=1}^{n} \frac{\boldsymbol{y}_{j}^{*} \boldsymbol{v}}{\boldsymbol{y}_{j}^{*} \boldsymbol{x}_{j}} \boldsymbol{x}_{j}=\sum_{k=1}^{n} \frac{\boldsymbol{x}_{k}^{*} \boldsymbol{v}}{\boldsymbol{y}_{k}^{*} \boldsymbol{x}_{k}} \boldsymbol{y}_{k}, \quad \boldsymbol{v} \in \mathbb{C}^{n}
$$

Proof For any right eigenpairs $\left(\lambda_{1}, \boldsymbol{x}_{1}\right), \ldots,\left(\lambda_{n}, \boldsymbol{x}_{n}\right)$ and left eigenpairs $\left(\lambda_{1}, \boldsymbol{y}_{1}\right), \ldots,\left(\lambda_{n}, \boldsymbol{y}_{n}\right)$ of $\boldsymbol{A}$ we have $\boldsymbol{A} \boldsymbol{X}=\boldsymbol{X} \boldsymbol{D}, \boldsymbol{Y}^{*} \boldsymbol{A}=\boldsymbol{D} \boldsymbol{Y}^{*}$, where

$$
\boldsymbol{X}:=\left[\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right], \quad \boldsymbol{Y}:=\left[\boldsymbol{y}_{1}, \ldots, \boldsymbol{y}_{n}\right], \quad \boldsymbol{D}:=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right) .
$$

Suppose $\boldsymbol{X}$ is nonsingular. Then $\boldsymbol{A} \boldsymbol{X}=\boldsymbol{X} \boldsymbol{D} \Longrightarrow \boldsymbol{A}=\boldsymbol{X} \boldsymbol{D} \boldsymbol{X}^{-1} \Longrightarrow \boldsymbol{X}^{-1} \boldsymbol{A}=$ $\boldsymbol{D} \boldsymbol{X}^{-1}$ and it follows that $\boldsymbol{Y}^{*}:=\boldsymbol{X}^{-1}$ contains a collection of left eigenvectors such that $\boldsymbol{Y}^{*} \boldsymbol{X}=\boldsymbol{I}$. Thus the columns of $\boldsymbol{Y}$ are linearly independent and $\boldsymbol{y}_{i}^{*} \boldsymbol{x}_{j}=\delta_{i, j}$. Similarly, if $\boldsymbol{Y}$ is nonsingular then $\boldsymbol{A} \boldsymbol{Y}^{-*}=\boldsymbol{Y}^{-*} \boldsymbol{D}$ and it follows that $\boldsymbol{X}:=\boldsymbol{Y}^{-*}$ contains a collection of linearly independent right eigenvectors such that $\boldsymbol{Y}^{*} \boldsymbol{X}=\boldsymbol{I}$. If $\boldsymbol{v}=\sum_{j=1}^{n} c_{j} \boldsymbol{x}_{j}$ then $\boldsymbol{y}_{i}^{*} \boldsymbol{v}=\sum_{j=1}^{n} c_{j} \boldsymbol{y}_{i}^{*} \boldsymbol{x}_{j}=c_{i} \boldsymbol{y}_{i}^{*} \boldsymbol{x}_{i}$, so $c_{i}=\boldsymbol{y}_{i}^{*} \boldsymbol{v} / \boldsymbol{y}_{i}^{*} \boldsymbol{x}_{i}$ for $i=1, \ldots, n$ and the first expansion in (6.16) follows. The second expansion follows similarly. $\square$

For a Hermitian matrix the right eigenvectors $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ are also left eigenvectors and (6.16) takes the form

$$
\boldsymbol{v}=\sum_{j=1}^{n} \frac{\boldsymbol{x}_{j}^{*} \boldsymbol{v}}{\boldsymbol{x}_{j}^{*} \boldsymbol{x}_{j}} \boldsymbol{x}_{j} .
$$

### 6.5.1 Biorthogonality

Left- and right eigenvectors corresponding to distinct eigenvalues are orthogonal.
Theorem 6.16 (Biorthogonality) Suppose ( $\mu, \boldsymbol{y}$ ) and ( $\lambda, \boldsymbol{x}$ ) are left and right eigenpairs of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. If $\lambda \neq \mu$ then $\boldsymbol{y}^{*} \boldsymbol{x}=0$.

Proof Using the eigenpair relation in two ways we obtain $\boldsymbol{y}^{*} \boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{y}^{*} \boldsymbol{x}=\mu \boldsymbol{y}^{*} \boldsymbol{x}$ and we conclude that $\boldsymbol{y}^{*} \boldsymbol{x}=0$. $\square$

Right and left eigenvectors corresponding to the same eigenvalue are sometimes orthogonal, sometimes not.

Theorem 6.17 (Simple Eigenvalue) Suppose ( $\lambda, \boldsymbol{x}$ ) and ( $\lambda, \boldsymbol{y}$ ) are right and left eigenpairs of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. If $\lambda$ has algebraic multiplicity one then $\boldsymbol{y}^{*} \boldsymbol{x} \neq 0$.

Proof Assume that $\|\boldsymbol{x}\|_{2}=1$. We have (cf. (6.8))

$$
\boldsymbol{V}^{*} \boldsymbol{A} \boldsymbol{V}=\left[\begin{array}{c|c}
\lambda & z^{*} \\
\hline \mathbf{0} & \boldsymbol{M}
\end{array}\right],
$$

where $\boldsymbol{V}$ is unitary and $\boldsymbol{V} \boldsymbol{e}_{1}=\boldsymbol{x}$. We show that if $\boldsymbol{y}^{*} \boldsymbol{x}=0$ then $\lambda$ is also an eigenvalue of $\boldsymbol{M}$ contradicting the multiplicity assumption of $\lambda$. Let $\boldsymbol{u}:=\boldsymbol{V}^{*} \boldsymbol{y}$. Then

$$
\left(\boldsymbol{V}^{*} \boldsymbol{A}^{*} \boldsymbol{V}\right) \boldsymbol{u}=\boldsymbol{V}^{*} \boldsymbol{A}^{*} \boldsymbol{y}=\bar{\lambda} \boldsymbol{V}^{*} \boldsymbol{y}=\bar{\lambda} \boldsymbol{u},
$$

so $(\bar{\lambda}, \boldsymbol{u})$ is an eigenpair of $\boldsymbol{V}^{*} \boldsymbol{A}^{*} \boldsymbol{V}$. But then $\boldsymbol{y}^{*} \boldsymbol{x}=\boldsymbol{u}^{*} \boldsymbol{V}^{*} \boldsymbol{V} \boldsymbol{e}_{1}=\boldsymbol{u}^{*} \boldsymbol{e}_{1}$. Suppose that $\boldsymbol{u}^{*} \boldsymbol{e}_{1}=0$, i.e., $\boldsymbol{u}=\left[\begin{array}{l}0 \\ \boldsymbol{v}\end{array}\right]$ for some nonzero $\boldsymbol{v} \in \mathbb{C}^{n-1}$. Then

$$
\boldsymbol{V}^{*} \boldsymbol{A}^{*} \boldsymbol{V} \boldsymbol{u}=\left[\begin{array}{c|c}
\bar{\lambda} & \mathbf{0}^{*} \\
\hline \boldsymbol{z} & \boldsymbol{M}^{*}
\end{array}\right]\left[\begin{array}{l}
0 \\
\boldsymbol{v}
\end{array}\right]=\left[\begin{array}{c}
0 \\
\boldsymbol{M}^{*} \boldsymbol{v}
\end{array}\right]=\bar{\lambda}\left[\begin{array}{l}
0 \\
\boldsymbol{v}
\end{array}\right]
$$

and $\lambda$ is an eigenvalue of $\boldsymbol{M}$. $\square$

The case with multiple eigenvalues is more complicated. For example, the matrix $\boldsymbol{A}:=\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right]$ has one eigenvalue $\lambda=1$ of algebraic multiplicity two, one right eigenvector $\boldsymbol{x}=\boldsymbol{e}_{1}$ and one left eigenvector $\boldsymbol{y}=\boldsymbol{e}_{2}$. Thus $\boldsymbol{x}$ and $\boldsymbol{y}$ are orthogonal.

### 6.6 Exercises Chap. 6

### 6.6.1 Exercises Sect. 6.1

Exercise 6.1 (Eigenvalues of a Block Triangular Matrix) What are the eigenvalues of the matrix

$$
\left[\begin{array}{llllllll}
0 & 2 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 2 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 2 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1
\end{array}\right] \in \mathbb{R}^{8,8} ?
$$

Exercise 6.2 (Characteristic Polynomial of Transpose) We have $\operatorname{det}\left(\boldsymbol{B}^{T}\right)=$ $\operatorname{det}(\boldsymbol{B})$ and $\operatorname{det}(\overline{\boldsymbol{B}})=\overline{\operatorname{det}(\boldsymbol{B})}$ for any square matrix $\boldsymbol{B}$. Use this to show that

a) $\pi_{\boldsymbol{A}^{T}}=\pi_{\boldsymbol{A}}$,
b) $\pi_{A^{*}}(\bar{\lambda})=\overline{\pi_{A}(\lambda)}$.

Exercise 6.3 (Characteristic Polynomial of Inverse) Suppose $(\lambda, \boldsymbol{x})$ is an eigenpair for $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Show that

a) If $\boldsymbol{A}$ is nonsingular then $\left(\lambda^{-1}, \boldsymbol{x}\right)$ is an eigenpair for $\boldsymbol{A}^{-1}$.
b) $\left(\lambda^{k}, \boldsymbol{x}\right)$ is an eigenpair for $\boldsymbol{A}^{k}$ for $k \in \mathbb{Z}$.

Exercise 6.4 (The Power of the Eigenvector Expansion) Show that if $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nondefective with eigenpairs $\left(\lambda_{j}, \boldsymbol{x}_{j}\right), j=1, \ldots, n$ then for any $\boldsymbol{x} \in \mathbb{C}^{n}$ and $k \in \mathbb{N}$

$$
\boldsymbol{A}^{k} \boldsymbol{x}=\sum_{j=1}^{n} c_{j} \lambda_{j}^{k} \boldsymbol{x}_{j} \text { for some scalars } c_{1}, \ldots, c_{n}
$$

Show that if $\boldsymbol{A}$ is nonsingular then (6.18) holds for all $k \in \mathbb{Z}$.
Exercise 6.5 (Eigenvalues of an Idempotent Matrix) Let $\lambda \in \sigma(\boldsymbol{A})$ where $\boldsymbol{A}^{2}=$ $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Show that $\lambda=0$ or $\lambda=1$. (A matrix is called idempotent if $\boldsymbol{A}^{2}=\boldsymbol{A}$ ).

Exercise 6.6 (Eigenvalues of a Nilpotent Matrix) Let $\lambda \in \sigma(\boldsymbol{A})$ where $\boldsymbol{A}^{k}=0$ for some $k \in \mathbb{N}$. Show that $\lambda=0$. (A matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ such that $\boldsymbol{A}^{k}=0$ for some $k \in \mathbb{N}$ is called nilpotent).

Exercise 6.7 (Eigenvalues of a Unitary Matrix) Let $\lambda \in \sigma(\boldsymbol{A})$, where $\boldsymbol{A}^{*} \boldsymbol{A}=\boldsymbol{I}$. Show that $|\lambda|=1$.

Exercise 6.8 (Nonsingular Approximation of a Singular Matrix) Suppose $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$ is singular. Then we can find $\epsilon_{0}>0$ such that $\boldsymbol{A}+\epsilon \boldsymbol{I}$ is nonsingular for all $\epsilon \in \mathbb{C}$ with $|\epsilon|<\epsilon_{0}$. Hint: $\operatorname{det}(\boldsymbol{A})=\lambda_{1} \lambda_{2} \cdots \lambda_{n}$, where $\lambda_{i}$ are the eigenvalues of $\boldsymbol{A}$.

Exercise 6.9 (Companion Matrix) For $q_{0}, \ldots, q_{n-1} \in \mathbb{C}$ let $p(\lambda)=\lambda^{n}+$ $q_{n-1} \lambda^{n-1}+\cdots+q_{0}$ be a polynomial of degree $n$ in $\lambda$. We derive two matrices that have $(-1)^{n} p$ as its characteristic polynomial.

a) Show that $p=(-1)^{n} \pi_{\boldsymbol{A}}$ where
$$
\boldsymbol{A}=\left[\begin{array}{ccccc}
-q_{n-1} & -q_{n-2} & \cdots & -q_{1} & -q_{0} \\
1 & 0 & \cdots & 0 & 0 \\
0 & 1 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & 0
\end{array}\right] .
$$
$\boldsymbol{A}$ is called a companion matrix of $p$.
b) Show that $p=(-1)^{n} \pi_{\boldsymbol{B}}$ where
$$
\boldsymbol{B}=\left[\begin{array}{ccccc}
0 & 0 & \cdots & 0 & -q_{0} \\
1 & 0 & \cdots & 0 & -q_{1} \\
0 & 1 & \cdots & 0 & -q_{2} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & -q_{n-1}
\end{array}\right] .
$$
Thus $\boldsymbol{B}$ can also be regarded as a companion matrix for $p$.

Exercise 6.10 (Find Eigenpair Example) Find eigenvalues and eigenvectors of $\boldsymbol{A}=\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 2 & 3 \\ 0 & 0 & 2\end{array}\right]$. Is $\boldsymbol{A}$ defective?

Exercise 6.11 (Right or Wrong? (Exam Exercise 2005-1)) Decide if the following statements are right or wrong. Give supporting arguments for your decisions.

a) The matrix
$$
\boldsymbol{A}=\frac{1}{6}\left[\begin{array}{cc}
3 & 4 \\
4 & -3
\end{array}\right]
$$
is orthogonal?
b) Let
$$
\boldsymbol{A}=\left[\begin{array}{cc}
a & 1 \\
0 & a
\end{array}\right]
$$
where $a \in \mathbb{R}$. There is a nonsingular matrix $\boldsymbol{Y} \in \mathbb{R}^{2 \times 2}$ and a diagonal matrix $\boldsymbol{D} \in \mathbb{R}^{2 \times 2}$ such that $\boldsymbol{A}=\boldsymbol{Y} \boldsymbol{D} \boldsymbol{Y}^{-1}$ ?

Exercise 6.12 (Eigenvalues of Tridiagonal Matrix (Exam Exercise 2009-3)) Let $\boldsymbol{A} \in \mathbb{R}^{n, n}$ be tridiagonal (i.e. $a_{i j}=0$ when $|i-j|>1$ ) and suppose also that $a_{i+1, i} a_{i, i+1}>0$ for $i=1, \ldots, n-1$. Show that the eigenvalues of $\boldsymbol{A}$ are real. ${ }^{2}$

### 6.6.2 Exercises Sect. 6.2

Exercise 6.13 (Jordan Example)
For the Jordan factorization of the matrix $\boldsymbol{A}=\left[\begin{array}{rrr}3 & 0 & 1 \\ -4 & 1 & -2 \\ -4 & 0 & -1\end{array}\right]$ we have $\boldsymbol{J}=\left[\begin{array}{lll}1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$. Find $\boldsymbol{S}$.
Exercise 6.14 (A Nilpotent Matrix) Show that $\left(\boldsymbol{J}_{m}(\lambda)-\lambda \boldsymbol{I}\right)^{r}=\left[\begin{array}{cc}\mathbf{0} & \boldsymbol{I}_{m-r} \\ \mathbf{0} & \mathbf{0}\end{array}\right]$ for $1 \leq r \leq m-1$ and conclude that $\left(\boldsymbol{J}_{m}(\lambda)-\lambda \boldsymbol{I}\right)^{m}=0$.

Exercise 6.15 (Properties of the Jordan Factorization)
Let $\boldsymbol{J}$ be the Jordan factorization of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ as given in Theorem 6.4. Then for $r=0,1,2, \ldots, m=2,3, \ldots$, and any $\lambda \in \mathbb{C}$

a) $\boldsymbol{A}^{r}=\boldsymbol{S} \boldsymbol{J}^{r} \boldsymbol{S}^{-1}$,
b) $\boldsymbol{J}^{r}=\operatorname{diag}\left(\boldsymbol{U}_{1}^{r}, \ldots, \boldsymbol{U}_{k}^{r}\right)$,

[^12]

c)$\boldsymbol{U}_{i}^{r}=\operatorname{diag}\left(\boldsymbol{J}_{m_{i, 1}}\left(\lambda_{i}\right)^{r}, \ldots, \boldsymbol{J}_{m_{i, g_{i}}}\left(\lambda_{i}\right)^{r}\right)$,
d)$\boldsymbol{J}_{m}(\lambda)^{r}=\left(\boldsymbol{E}_{m}+\lambda \boldsymbol{I}_{m}\right)^{r}=\sum_{k=0}^{\min \{r, m-1\}}\binom{r}{k} \lambda^{r-k} \boldsymbol{E}_{m}^{k}$.


Exercise 6.16 (Powers of a Jordan Block) Find $\boldsymbol{J}^{100}$ and $\boldsymbol{A}^{100}$ for the matrix in Exercise 6.13.

Exercise 6.17 (The Minimal Polynomial) Let $\boldsymbol{J}$ be the Jordan factorization of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ as given in Theorem 6.4. The polynomial

$$
\mu_{\boldsymbol{A}}(\lambda):=\prod_{i=1}^{k}\left(\lambda_{i}-\lambda\right)^{m_{i}} \text { where } m_{i}:=\max _{1 \leq j \leq g_{i}} m_{i, j} \text {, }
$$

is called the minimal polynomial of $\boldsymbol{A}$. We define the matrix polynomial $\mu_{\boldsymbol{A}}(\boldsymbol{A})$ by replacing the factors $\lambda_{i}-\lambda$ by $\lambda_{i} \boldsymbol{I}-\boldsymbol{A}$.

a) We have $\pi_{\boldsymbol{A}}(\lambda)=\prod_{i=1}^{k} \prod_{j=1}^{g_{i}}\left(\lambda_{i}-\lambda\right)^{m_{i, j}}$. Use this to show that the minimal polynomial divides the characteristic polynomial, i.e., $\pi_{\boldsymbol{A}}=\mu_{\boldsymbol{A}} \nu_{\boldsymbol{A}}$ for some polynomial $\nu_{\boldsymbol{A}}$.
b) Show that $\mu_{\boldsymbol{A}}(\boldsymbol{A})=\mathbf{0} \Longleftrightarrow \mu_{\boldsymbol{A}}(\boldsymbol{J})=\mathbf{0}$.
c) (can be difficult) Use Exercises 6.14, 6.15 and the maximality of $m_{i}$ to show that $\mu_{\boldsymbol{A}}(\boldsymbol{A})=0$. Thus a matrix satisfies its minimal equation. Finally show that the degree of any polynomial $p$ such that $p(\boldsymbol{A})=\mathbf{0}$ is at least as large as the degree of the minimal polynomial.
d) Use 2. to show the Cayley-Hamilton Theorem which says that a matrix satisfies its characteristic equation $\pi_{\boldsymbol{A}}(\boldsymbol{A})=\mathbf{0}$.

Exercise 6.18 (Cayley Hamilton Theorem (Exam Exercise 1996-3)) Suppose $p$ is a polynomial given by $p(t):=\sum_{j=0}^{r} b_{j} t^{j}$, where $b_{j} \in \mathbb{C}$ and $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. We define the matrix $p(\boldsymbol{A}) \in \mathbb{C}^{n \times n}$ by

$$
p(\boldsymbol{A}):=\sum_{j=0}^{r} b_{j} \boldsymbol{A}^{j},
$$

where $\boldsymbol{A}^{0}:=\boldsymbol{I}$. From this it follows that if $p(t):=\left(t-\alpha_{1}\right) \cdots\left(t-\alpha_{r}\right)$ for some $\alpha_{0}, \ldots, \alpha_{r} \in \mathbb{C}$ then $p(\boldsymbol{A})=\left(\boldsymbol{A}-\alpha_{1}\right) \cdots\left(\boldsymbol{A}-\alpha_{r}\right)$. We accept this without proof.

Let $\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}=\boldsymbol{T}$, where $\boldsymbol{U}$ is unitary and $\boldsymbol{T}$ upper triangular with the eigenvalues of $\boldsymbol{A}$ on the diagonal.

a) Find the characteristic polynomial $\pi_{\boldsymbol{A}}$ to $\left[\begin{array}{rr}2 & 1 \\ -1 & 4\end{array}\right]$. Show that $\pi(\boldsymbol{A})=\mathbf{0}$.
b) Let now $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ be arbitrary. For any polynomial $p$ show that $p(\boldsymbol{A})=$ $\boldsymbol{U} p(\boldsymbol{T}) \boldsymbol{U}^{*}$.
c) Let $n, k \in \mathbb{N}$ with $1 \leq k<n$. Let $\boldsymbol{C}, \boldsymbol{D} \in \mathbb{C}^{n \times n}$ be upper triangular. Moreover, $c_{i, j}=0$ for $i, j \leq k$ and $d_{k+1, k+1}=0$. Define $\boldsymbol{E}:=\boldsymbol{C} \boldsymbol{D}$ and show that $e_{i, j}=0$ for $i, j \leq k+1$.

d) Now let $p:=\pi_{\boldsymbol{A}}$ be the characteristic polynomial of $\boldsymbol{A}$. Show that $p(\boldsymbol{T})=\mathbf{0} .^{3}$ Then show that $p(\boldsymbol{A})=\mathbf{0}$. (Cayley Hamilton Theorem)

### 6.6.3 Exercises Sect. 6.3

Exercise 6.19 (Schur Factorization Example) Show that a Schur factorization of $\boldsymbol{A}=\left[\begin{array}{ll}1 & 2 \\ 3 & 2\end{array}\right]$ is $\boldsymbol{U}^{T} \boldsymbol{A} \boldsymbol{U}=\left[\begin{array}{cc}-1 & -1 \\ 0 & 4\end{array}\right]$, where $\boldsymbol{U}=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}1 & 1 \\ -1 & 1\end{array}\right]$.

Exercise 6.20 (Skew-Hermitian Matrix) Suppose $\boldsymbol{C}=\boldsymbol{A}+i \boldsymbol{B}$, where $\boldsymbol{A}, \boldsymbol{B} \in$ $\mathbb{R}^{n \times n}$. Show that $\boldsymbol{C}$ is skew-Hermitian if and only if $\boldsymbol{A}^{T}=-\boldsymbol{A}$ and $\boldsymbol{B}^{T}=\boldsymbol{B}$.

Exercise 6.21 (Eigenvalues of a Skew-Hermitian Matrix) Show that any eigenvalue of a skew-Hermitian matrix is purely imaginary.

Exercise 6.22 (Eigenvector Expansion Using Orthogonal Eigenvectors) Show that if the eigenpairs $\left(\lambda_{1}, \boldsymbol{u}_{1}\right), \ldots,\left(\lambda_{n}, \boldsymbol{u}_{n}\right)$ of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ are orthogonal, i.e., $\boldsymbol{u}_{j}^{*} \boldsymbol{u}_{k}=0$ for $j \neq k$ then the eigenvector expansions of $\boldsymbol{x}$ and $\boldsymbol{A} \boldsymbol{x} \in \mathbb{C}^{n}$ take the form

$$
\boldsymbol{x}=\sum_{j=1}^{n} c_{j} \boldsymbol{u}_{j}, \quad \boldsymbol{A} \boldsymbol{x}=\sum_{j=1}^{n} c_{j} \lambda_{j} \boldsymbol{u}_{j}, \text { where } c_{j}=\frac{\boldsymbol{u}_{j}^{*} \boldsymbol{x}}{\boldsymbol{u}_{j}^{*} \boldsymbol{u}_{j}} .
$$

Exercise 6.23 (Rayleigh Quotient (Exam Exercise 2015-3))

a) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be a symmetric matrix. Explain how we can use the spectral theorem for symmetric matrices to show that
$$
\lambda_{\min }=\min _{\boldsymbol{x} \neq 0} R(\boldsymbol{x})=\min _{\|\boldsymbol{x}\|_{2}=1} R(\boldsymbol{x}),
$$
where $\lambda_{\text {min }}$ is the smallest eigenvalue of $\boldsymbol{A}$, and $R(\boldsymbol{x})$ is the Rayleigh quotient given by
$$
R(x):=\frac{x^{T} A x}{x^{T} x} .
$$

[^13]

b)Let $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$ such that $\|\boldsymbol{x}\|_{2}=1$ and $\boldsymbol{y} \neq 0$. Show that
$$
R(\boldsymbol{x}-t \boldsymbol{y})=R(\boldsymbol{x})-2 t(\boldsymbol{A x}-R(\boldsymbol{x}) \boldsymbol{x})^{T} \boldsymbol{y}+\mathcal{O}\left(t^{2}\right),
$$
where $t>0$ is small. ${ }^{4}$
c)Based on the characterization given in a) above it is tempting to develop an algorithm for computing $\lambda_{\text {min }}$ by approximating the minimum of $R(\boldsymbol{x})$ over the unit ball
$$
B_{1}:=\left\{\boldsymbol{x} \in \mathbb{R}^{n} \mid\|\boldsymbol{x}\|_{2}=1\right\} .
$$
Assume that $\boldsymbol{x}^{0} \in B_{1}$ satisfies $\boldsymbol{A} \boldsymbol{x}^{0}-R\left(\boldsymbol{x}^{0}\right) \boldsymbol{x}^{0} \neq 0$, i.e., $\left(R\left(\boldsymbol{x}^{0}\right), \boldsymbol{x}^{0}\right)$ is not an eigenpair for $\boldsymbol{A}$. Explain how we can find a vector $\boldsymbol{x}^{1} \in B_{1}$ such that $R\left(\boldsymbol{x}^{1}\right)<$ $R\left(\boldsymbol{x}^{0}\right)$.


### 6.6.4 Exercises Sect. 6.4

Exercise 6.24 (Eigenvalue Perturbation for Hermitian Matrices) Show that in Theorem 6.13, if $\boldsymbol{E}$ is symmetric positive semidefinite then $\beta_{i} \geq \alpha_{i}$.

Exercise 6.25 (Hoffman-Wielandt) Show that (6.15) does not hold for the matrices $\boldsymbol{A}:=\left[\begin{array}{ll}0 & 0 \\ 0 & 4\end{array}\right]$ and $\boldsymbol{B}:=\left[\begin{array}{cc}-1 & -1 \\ 1 & 1\end{array}\right]$. Why does this not contradict the Hoffman-Wielandt theorem?

Exercise 6.26 (Biorthogonal Expansion) Determine right and left eigenpairs for the matrix $\boldsymbol{A}:=\left[\begin{array}{ll}3 & 1 \\ 2 & 2\end{array}\right]$ and the two expansions in (6.16) for any $\boldsymbol{v} \in \mathbb{R}^{2}$.

Exercise 6.27 (Generalized Rayleigh Quotient) For $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ and any $\boldsymbol{y}, \boldsymbol{x} \in$ $\mathbb{C}^{n}$ with $\boldsymbol{y}^{*} \boldsymbol{x} \neq 0$ the quantity $R(\boldsymbol{y}, \boldsymbol{x})=R_{\boldsymbol{A}}(\boldsymbol{y}, \boldsymbol{x}):=\frac{\boldsymbol{y}^{*} \boldsymbol{A} \boldsymbol{x}}{\boldsymbol{y}^{*} \boldsymbol{x}}$ is called a generalized Rayleigh quotient for $\boldsymbol{A}$. Show that if ( $\lambda, \boldsymbol{x}$ ) is a right eigenpair for $\boldsymbol{A}$ then $R(\boldsymbol{y}, \boldsymbol{x})=\lambda$ for any $\boldsymbol{y}$ with $\boldsymbol{y}^{*} \boldsymbol{x} \neq 0$. Also show that if $(\lambda, \boldsymbol{y})$ is a left eigenpair for $\boldsymbol{A}$ then $R(\boldsymbol{y}, \boldsymbol{x})=\lambda$ for any $\boldsymbol{x}$ with $\boldsymbol{y}^{*} \boldsymbol{x} \neq 0$.

### 6.7 Review Questions

6.7.1 Does $\boldsymbol{A}, \boldsymbol{A}^{T}$ and $\boldsymbol{A}^{*}$ have the same eigenvalues? What about $\boldsymbol{A}^{*} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{*}$ ?
6.7.2 Can a matrix with multiple eigenvalues be similar to a diagonal matrix?

[^14]

6.7.3What is the geometric multiplicity of an eigenvalue? Can it be bigger than the algebraic multiplicity?
6.7.4What is the Jordan factorization of a matrix?
6.7.5What are the eigenvalues of a diagonal matrix?
6.7.6What are the Schur factors of a matrix?
6.7.7What is a quasi-triangular matrix?
6.7.8Give some classes of normal matrices. Why are normal matrices important?
6.7.9State the Courant-Fischer theorem.
6.7.10State the Hoffman-Wielandt theorem for Hermitian matrices.
6.7.11What is a left eigenvector of a matrix?


## Chapter 7 <br> The Singular Value Decomposition

The singular value decomposition and the reduced form called the singular value factorization are useful both for theory and practice. Some of their applications include solving over-determined equations, principal component analysis in statistics, numerical determination of the rank of a matrix, algorithms used in search engines, and the theory of matrices.

We know from Theorem 6.7 that a square matrix $\boldsymbol{A}$ can be diagonalized by a unitary similarity transformation if and only if it is normal, that is $\boldsymbol{A}^{*} \boldsymbol{A}=$ $\boldsymbol{A} \boldsymbol{A}^{*}$. In particular, if $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is normal then it has a set of orthonormal eigenpairs $\left(\lambda_{1}, \boldsymbol{u}_{1}\right), \ldots,\left(\lambda_{n}, \boldsymbol{u}_{n}\right)$. Letting $\boldsymbol{U}:=\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{n}\right] \in \mathbb{C}^{n \times n}$ and $\boldsymbol{D}:=$ $\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ we have the spectral decomposition

$$
\boldsymbol{A}=\boldsymbol{U} \boldsymbol{D} \boldsymbol{U}^{*}, \text { where } \boldsymbol{U}^{*} \boldsymbol{U}=\boldsymbol{I} .
$$

The singular value decomposition (SVD) is a decomposition of a matrix in the form $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$, where $\boldsymbol{U}$ and $\boldsymbol{V}$ are unitary, and $\boldsymbol{\Sigma}$ is a nonnegative diagonal matrix, i.e., $\Sigma_{i j}=0$ for all $i \neq j$ and $\Sigma_{i i} \geq 0$ for all $i$. The diagonal elements $\sigma_{i}:=\Sigma_{i i}$ are called singular values, while the columns of $\boldsymbol{U}$ and $\boldsymbol{V}$ are called singular vectors. To be a singular value decomposition the singular values should be ordered, i.e., $\sigma_{i} \geq \sigma_{i+1}$ for all $i$.

Example 7.1 (SVD) The following is a singular value decomposition of a rectangular matrix.

$$
\boldsymbol{A}=\frac{1}{15}\left[\begin{array}{cc}
14 & 2 \\
4 & 22 \\
16 & 13
\end{array}\right]=\frac{1}{3}\left[\begin{array}{rrr}
1 & 2 & 2 \\
2 & -2 & 1 \\
2 & 1 & -2
\end{array}\right]\left[\begin{array}{ll}
2 & 0 \\
0 & 1 \\
0 & 0
\end{array}\right] \frac{1}{5}\left[\begin{array}{rr}
3 & 4 \\
4 & -3
\end{array}\right]=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*} .
$$

Indeed, $\boldsymbol{U}$ and $\boldsymbol{V}$ are unitary since the columns (the singular vectors) are orthonormal, and $\boldsymbol{\Sigma}$ is a nonnegative diagonal matrix with singular values $\sigma_{1}=2$ and $\sigma_{2}=1$.

### 7.1 The SVD Always Exists

The singular value decomposition is closely related to the eigenpairs of $\boldsymbol{A}^{*} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{*}$.

### 7.1.1 The Matrices $\boldsymbol{A}^{*} \boldsymbol{A}, \boldsymbol{A} \boldsymbol{A}^{*}$

To start we show that bases for the four fundamental subspaces $\mathcal{R}(\boldsymbol{A}), \mathcal{N}(\boldsymbol{A})$, $\mathcal{R}\left(\boldsymbol{A}^{*}\right)$ and $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$ of a matrix $\boldsymbol{A}$ can be determined from the eigenpairs of $\boldsymbol{A}^{*} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{*}$.

Theorem 7.1 (The Matrices $\left.\boldsymbol{A}^{*} \boldsymbol{A}, \boldsymbol{A} \boldsymbol{A}^{*}\right)$ Suppose $m, n \in \mathbb{N}$ and $\boldsymbol{A} \in \mathbb{C}^{m \times n}$.

1. The matrices $\boldsymbol{A}^{*} \boldsymbol{A} \in \mathbb{C}^{n \times n}$ and $\boldsymbol{A} \boldsymbol{A}^{*} \in \mathbb{C}^{m \times m}$ have the same nonzero eigenvalues with the same algebraic multiplicities. Moreover the extra eigenvalues of the larger matrix are all zero.
2. The matrices $\boldsymbol{A}^{*} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{*}$ are Hermitian with nonnegative eigenvalues.
3. Let $\left(\lambda_{j}, \boldsymbol{v}_{j}\right)$ be orthonormal eigenpairs for $\boldsymbol{A}^{*} \boldsymbol{A}$ with
$$
\lambda_{1} \geq \cdots \geq \lambda_{r}>0=\lambda_{r+1}=\cdots=\lambda_{n} .
$$
Then $\left\{\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}\right\}$ is an orthogonal basis for the column space $\mathcal{R}(\boldsymbol{A}):=$ $\left\{\boldsymbol{A} \boldsymbol{y} \in \mathbb{C}^{m}: \boldsymbol{y} \in \mathbb{C}^{n}\right\}$ and $\left\{\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{n}\right\}$ is an orthonormal basis for the nullspace $\mathcal{N}(\boldsymbol{A}):=\left\{\boldsymbol{y} \in \mathbb{C}^{n}: \boldsymbol{A} \boldsymbol{y}=\mathbf{0}\right\}$.
4. Let $\left(\lambda_{j}, \boldsymbol{u}_{j}\right)$ be orthonormal eigenpairs for $\boldsymbol{A} \boldsymbol{A}^{*}$. If $\lambda_{j}>0, j=1, \ldots, r$ and $\lambda_{j}=0, j=r+1, \ldots, m$ then $\left\{\boldsymbol{A}^{*} \boldsymbol{u}_{1}, \ldots, \boldsymbol{A}^{*} \boldsymbol{u}_{r}\right\}$ is an orthogonal basis for the column space $\mathcal{R}\left(\boldsymbol{A}^{*}\right)$ and $\left\{\boldsymbol{u}_{r+1}, \ldots, \boldsymbol{u}_{m}\right\}$ is an orthonormal basis for the nullspace $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$.
5. The rank of $\boldsymbol{A}$ equals the number of positive eigenvalues of $\boldsymbol{A}^{*} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{*}$.

Proof

1. Consider the characteristic polynomials $\pi_{\boldsymbol{A}^{*} \boldsymbol{A}}$ and $\pi_{\boldsymbol{A} \boldsymbol{A}^{*}}$. By (6.1) we have
$$
\lambda^{m} \pi_{\boldsymbol{A}^{*} \boldsymbol{A}}(\lambda)=\lambda^{n} \pi_{\boldsymbol{A} \boldsymbol{A}^{*}}(\lambda), \quad \lambda \in \mathbb{C},
$$
and the claim follows.
2. The matrices $\boldsymbol{A}^{*} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{*}$ are Hermitian and positive semidefinite and therefore has nonnegative eigenvalues (cf. Lemmas 4.2 and 4.5). Moreover, if

$\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{v}=\lambda \boldsymbol{v}$ with $\boldsymbol{v} \neq \mathbf{0}$, then
$$
\lambda=\frac{\boldsymbol{v}^{*} \boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{v}}{\boldsymbol{v}^{*} \boldsymbol{v}}=\frac{\|\boldsymbol{A} \boldsymbol{v}\|_{2}^{2}}{\|\boldsymbol{v}\|_{2}^{2}} \geq 0 .
$$
3. By orthonormality of $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}$ we have $\left(\boldsymbol{A} \boldsymbol{v}_{j}\right)^{*} \boldsymbol{A} \boldsymbol{v}_{k}=\boldsymbol{v}_{j}^{*} \boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{v}_{k}=\lambda_{k} \boldsymbol{v}_{j}^{*} \boldsymbol{v}_{k}$ $=0$ for $j \neq k$, showing that $\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{n}$ are orthogonal vectors. Moreover, (7.3) implies that $\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}$ are nonzero and $\boldsymbol{A} \boldsymbol{v}_{j}=\mathbf{0}$ for $j=r+$ $1, \ldots, n$. In particular, the elements of $\left\{\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}\right\}$ and $\left\{\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{n}\right\}$ are linearly independent vectors in $\mathcal{R}(\boldsymbol{A})$ and $\mathcal{N}(\boldsymbol{A})$, respectively. The proof will be complete once it is shown that $\mathcal{R}(\boldsymbol{A}) \subset \operatorname{span}\left(\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}\right)$ and $\mathcal{N}(\boldsymbol{A}) \subset$ $\operatorname{span}\left(\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{n}\right)$. Suppose $\boldsymbol{x} \in \mathcal{R}(\boldsymbol{A})$. Then $\boldsymbol{x}=\boldsymbol{A} \boldsymbol{y}$ for some $\boldsymbol{y} \in \mathbb{C}^{n}$, Let $\boldsymbol{y}=\sum_{j=1}^{n} c_{j} \boldsymbol{v}_{j}$ be an eigenvector expansion of $\boldsymbol{y}$. Since $\boldsymbol{A} \boldsymbol{v}_{j}=\mathbf{0}$ for $j=r+1, \ldots, n$ we obtain $\boldsymbol{x}=\boldsymbol{A} \boldsymbol{y}=\sum_{j=1}^{n} c_{j} \boldsymbol{A} \boldsymbol{v}_{j}=\sum_{j=1}^{r} c_{j} \boldsymbol{A} \boldsymbol{v}_{j} \in$ $\operatorname{span}\left(\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}\right)$. Finally, if $\boldsymbol{y}=\sum_{j=1}^{n} c_{j} \boldsymbol{v}_{j} \in \mathcal{N}(\boldsymbol{A})$, then we have $\boldsymbol{A} \boldsymbol{y}=\sum_{j=1}^{r} c_{j} \boldsymbol{A} \boldsymbol{v}_{j}=\mathbf{0}$, and $c_{1}=\cdots=c_{r}=0$ since $\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}$ are linearly independent. But then $\boldsymbol{y}=\sum_{j=r+1}^{n} c_{j} \boldsymbol{v}_{j} \in \operatorname{span}\left(\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{n}\right)$.
4. Since $\boldsymbol{A} \boldsymbol{A}^{*}=\boldsymbol{B}^{*} \boldsymbol{B}$ with $\boldsymbol{B}:=\boldsymbol{A}^{*}$ this follows from part 3 with $\boldsymbol{A}=\boldsymbol{B}$.
5. By part 1 and $2 \boldsymbol{A}^{*} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{*}$ have the same number $r$ of positive eigenvalues and by part 3 and $4 r$ is the rank of $\boldsymbol{A}$. $\square$

The following theorem shows, in a constructive way, that any matrix has a singular value decomposition.

Theorem 7.2 (Existence of SVD) Suppose for $m, n, r \in \mathbb{N}$ that $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has rank $r$, and that $\left(\lambda_{j}, \boldsymbol{v}_{j}\right)$ are orthonormal eigenpairs for $\boldsymbol{A}^{*} \boldsymbol{A}$ with $\lambda_{1} \geq \cdots \geq$ $\lambda_{r}>0=\lambda_{r+1}=\cdots=\lambda_{n}$. Define

1. $\boldsymbol{V}:=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right] \in \mathbb{C}^{n \times n}$,
2. $\Sigma \in \mathbb{R}^{m \times n}$ is a diagonal matrix with diagonal elements $\sigma_{j}:=\sqrt{\lambda_{j}}$ for $j=$ $1, \ldots, \min (m, n)$,
3. $\boldsymbol{U}:=\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{m}\right] \in \mathbb{C}^{m \times m}$, where $\boldsymbol{u}_{j}=\sigma_{j}^{-1} \boldsymbol{A} \boldsymbol{v}_{j}$ for $j=1, \ldots, r$ and $\boldsymbol{u}_{r+1}, \ldots, \boldsymbol{u}_{m}$ is any extension of $\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}$ to an orthonormal basis $\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{m}$ for $\mathbb{C}^{m}$.

Then $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ is a singular value decomposition of $\boldsymbol{A}$.
Proof Let $\boldsymbol{U}, \boldsymbol{\Sigma}, \boldsymbol{V}$ be as in the theorem. The vectors $\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}$ are orthonormal since $\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}$ are orthogonal and $\sigma_{j}=\left\|\boldsymbol{A} \boldsymbol{v}_{j}\right\|_{2}>0, j=1, \ldots, r$ by (7.3). But then $\boldsymbol{U}$ and $\boldsymbol{V}$ are unitary and $\boldsymbol{\Sigma}$ is a nonnegative diagonal matrix. Moreover,

$$
\begin{aligned}
\boldsymbol{U} \boldsymbol{\Sigma} & =\boldsymbol{U}\left[\sigma_{1} \boldsymbol{e}_{1}, \ldots, \sigma_{r} \boldsymbol{e}_{r}, 0, \ldots, 0\right] \\
& =\left[\sigma_{1} \boldsymbol{u}_{1}, \ldots, \sigma_{r} \boldsymbol{u}_{r}, 0, \ldots, 0\right] \\
& =\left[\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{n}\right] .
\end{aligned}
$$

Thus $\boldsymbol{U} \boldsymbol{\Sigma}=\boldsymbol{A} \boldsymbol{V}$ and since $\boldsymbol{V}$ is square and unitary we find $\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}=\boldsymbol{A} \boldsymbol{V} \boldsymbol{V}^{*}=\boldsymbol{A}$ and we have an SVD of $\boldsymbol{A}$ with $\sigma_{1} \geq \sigma_{2} \geq \cdots \geq \sigma_{r}$. $\square$

Example 7.2 (Find SVD) To derive the SVD in (7.2) where $\boldsymbol{A}=\frac{1}{15}\left[\begin{array}{cc}14 & 2 \\ 4 & 22 \\ 16 & 13\end{array}\right]$, we first compute the eigenpairs of

$$
\boldsymbol{B}:=\boldsymbol{A}^{T} \boldsymbol{A}=\frac{1}{25}\left[\begin{array}{ll}
52 & 36 \\
36 & 73
\end{array}\right]
$$

as

$$
\boldsymbol{B}\left[\begin{array}{l}
3 \\
4
\end{array}\right]=4\left[\begin{array}{l}
3 \\
4
\end{array}\right], \quad \boldsymbol{B}\left[\begin{array}{r}
4 \\
-3
\end{array}\right]=1\left[\begin{array}{r}
4 \\
-3
\end{array}\right] .
$$

Thus $\sigma_{1}=2, \sigma_{2}=1$, and $\boldsymbol{V}=\frac{1}{5}\left[\begin{array}{rr}3 & 4 \\ 4 & -3\end{array}\right]$. Now $\boldsymbol{u}_{1}=\boldsymbol{A} \boldsymbol{v}_{1} / \sigma_{1}=[1,2,2]^{T} / 3$, $\boldsymbol{u}_{2}=\boldsymbol{A} \boldsymbol{v}_{2} / \sigma_{2}=[2,-2,1]^{T} / 3$. For an SVD we also need $\boldsymbol{u}_{3}$ which is any vector of length one orthogonal to $\boldsymbol{u}_{1}$ and $\boldsymbol{u}_{2} . \boldsymbol{u}_{3}=[2,1,-2]^{T} / 3$ is such a vector and we obtain the singular value decomposition (7.2).

### 7.2 Further Properties of SVD

We first consider a reduced SVD that is often convenient.

### 7.2.1 The Singular Value Factorization

Suppose $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ is a singular value decomposition of $\boldsymbol{A}$ of rank $r$. Consider the block partitions

$$
\begin{aligned}
& \boldsymbol{U}=\left[\boldsymbol{U}_{1}, \boldsymbol{U}_{2}\right] \in \mathbb{C}^{m \times m}, \quad \boldsymbol{U}_{1}:=\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}\right], \quad \boldsymbol{U}_{2}:=\left[\boldsymbol{u}_{r+1}, \ldots, \boldsymbol{u}_{m}\right], \\
& \boldsymbol{V}=\left[\boldsymbol{V}_{1}, \boldsymbol{V}_{2}\right] \in \mathbb{C}^{n \times n}, \quad \boldsymbol{V}_{1}:=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{r}\right], \quad \boldsymbol{V}_{2}:=\left[\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{n}\right], \\
& \boldsymbol{\Sigma}=\left[\begin{array}{cc}
\boldsymbol{\Sigma}_{1} & \mathbf{0}_{r, n-r} \\
\mathbf{0}_{m-r, r} & \mathbf{0}_{m-r, n-r}
\end{array}\right] \in \mathbb{R}^{m \times n}, \text { where } \boldsymbol{\Sigma}_{1}:=\operatorname{diag}\left(\sigma_{1}, \ldots, \sigma_{r}\right) .
\end{aligned}
$$

Thus $\Sigma_{1}$ contains the $r$ positive singular values on the diagonal and for $k, l \geq 0$ the symbol $\mathbf{0}_{k, l}=[]$ denotes the empty matrix if $k=0$ or $l=0$, and the zero matrix
with $k$ rows and $l$ columns otherwise. We obtain by block multiplication a reduced factorization

$$
\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}=\boldsymbol{U}_{1} \boldsymbol{\Sigma}_{1} \boldsymbol{V}_{1}^{*} .
$$

As an example:

$$
\left[\begin{array}{ll}
1 & -1 \\
1 & -1
\end{array}\right]=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right]\left[\begin{array}{ll}
2 & 0 \\
0 & 0
\end{array}\right] \frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & -1 \\
1 & 1
\end{array}\right]=\frac{1}{\sqrt{2}}\left[\begin{array}{l}
1 \\
1
\end{array}\right][2] \frac{1}{\sqrt{2}}\left[\begin{array}{ll}
1 & -1
\end{array}\right] .
$$

Definition 7.1 (SVF) Let $m, n, r \in \mathbb{N}$ and suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has $r$ positive singular values, i.e., $\boldsymbol{A}$ has rank $r$. A singular value factorization (SVF) is a factorization of $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ of the form $\boldsymbol{A}=\boldsymbol{U}_{1} \boldsymbol{\Sigma}_{1} \boldsymbol{V}_{1}^{*}$, where $\boldsymbol{U}_{1} \in \mathbb{C}^{m \times r}$ and $\boldsymbol{V}_{1} \in \mathbb{C}^{n \times r}$ have orthonormal columns, and $\boldsymbol{\Sigma}_{1} \in \mathbb{R}^{r \times r}$ is a diagonal matrix with $\sigma_{1} \geq \cdots \geq \sigma_{r}>0$.

An SVD and an SVF of a matrix $\boldsymbol{A}$ of rank $r$ are closely related.

1. Let $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ be an SVD of $\boldsymbol{A}$. Then $\boldsymbol{A}=\boldsymbol{U}_{1} \boldsymbol{\Sigma}_{1} \boldsymbol{V}_{1}^{*}$ is an SVF of $\boldsymbol{A}$, where $\boldsymbol{U}_{1}, \boldsymbol{V}_{1}$ contain the first $r$ columns of $\boldsymbol{U}, \boldsymbol{V}$ respectively, and $\Sigma_{1} \in \mathbb{R}^{r \times r}$ is a diagonal matrix with the positive singular values on the diagonal.
2. Conversely, suppose $\boldsymbol{A}=\boldsymbol{U}_{1} \boldsymbol{\Sigma}_{1} \boldsymbol{V}_{1}^{*}$ is a singular value factorization of $\boldsymbol{A}$. Extend $\boldsymbol{U}_{1}$ and $\boldsymbol{V}_{1}$ in any way to unitary matrices $\boldsymbol{U} \in \mathbb{C}^{m \times m}$ and $\boldsymbol{V} \in \mathbb{C}^{n \times n}$, and let $\boldsymbol{\Sigma}$ be given by (7.4). Then $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ is an SVD of $\boldsymbol{A}$.
3. If $\boldsymbol{A}=\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}\right] \operatorname{diag}\left(\sigma_{1}, \ldots, \sigma_{r}\right)\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{r}\right]^{*}$ is a singular value factorization of $\boldsymbol{A}$ then
$$
\boldsymbol{A}=\sum_{j=1}^{r} \sigma_{j} \boldsymbol{u}_{j} \boldsymbol{v}_{j}^{*} .
$$
This is known as the outer product form of the SVD and SVF.
4. We note that a nonsingular square matrix has full rank and only positive singular values. Thus the SVD and SVF are the same for a nonsingular matrix.

Example $7.3(r<n<m)$ To find the SVF and SVD of

$$
\boldsymbol{A}=\left[\begin{array}{ll}
1 & 1 \\
1 & 1 \\
0 & 0
\end{array}\right] .
$$

we first compute eigenpairs of

$$
\boldsymbol{B}:=\boldsymbol{A}^{T} \boldsymbol{A}=\left[\begin{array}{ll}
2 & 2 \\
2 & 2
\end{array}\right]
$$

as

$$
\boldsymbol{B}\left[\begin{array}{l}
1 \\
1
\end{array}\right]=4\left[\begin{array}{l}
1 \\
1
\end{array}\right], \quad \boldsymbol{B}\left[\begin{array}{r}
1 \\
-1
\end{array}\right]=0\left[\begin{array}{r}
1 \\
-1
\end{array}\right],
$$

and we find $\sigma_{1}=2, \sigma_{2}=0$, Thus $r=1, m=3, n=2$ and

$$
\boldsymbol{\Sigma}=\left[\begin{array}{cc}
\boldsymbol{\Sigma}_{1} & 0 \\
0 & 0 \\
0 & 0
\end{array}\right], \quad \boldsymbol{\Sigma}_{1}=[2], \quad \boldsymbol{V}=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right] .
$$

We find $\boldsymbol{u}_{1}=\boldsymbol{A} \boldsymbol{v}_{1} / \sigma_{1}=\boldsymbol{s}_{1} / \sqrt{2}$, where $\boldsymbol{s}_{1}=[1,1,0]^{T}$, and the SVF of $\boldsymbol{A}$ is given by

$$
\boldsymbol{A}=\frac{1}{\sqrt{2}}\left[\begin{array}{l}
1 \\
1 \\
0
\end{array}\right][2] \frac{1}{\sqrt{2}}\left[\begin{array}{ll}
1 & 1
\end{array}\right] .
$$

To find an SVD we need to extend $\boldsymbol{u}_{1}$ to an orthonormal basis for $\mathbb{R}^{3}$. We first extend $\boldsymbol{s}_{1}$ to a basis $\left\{\boldsymbol{s}_{1}, \boldsymbol{s}_{2}, \boldsymbol{s}_{3}\right\}$ for $\mathbb{R}^{3}$, apply the Gram-Schmidt orthogonalization process to $\left\{\boldsymbol{s}_{1}, \boldsymbol{s}_{2}, \boldsymbol{s}_{3}\right\}$, and then normalize. Choosing the basis

$$
\boldsymbol{s}_{1}=\left[\begin{array}{l}
1 \\
1 \\
0
\end{array}\right], \quad \boldsymbol{s}_{2}=\left[\begin{array}{l}
0 \\
1 \\
0
\end{array}\right], \quad \boldsymbol{s}_{3}=\left[\begin{array}{l}
0 \\
0 \\
1
\end{array}\right],
$$

we find from (5.8) $\boldsymbol{w}_{1}=\boldsymbol{s}_{1}, \boldsymbol{w}_{2}=\boldsymbol{s}_{2}-\frac{\boldsymbol{s}_{2}^{T} \boldsymbol{w}_{1}}{\boldsymbol{w}_{1}^{T} \boldsymbol{w}_{1}} \boldsymbol{w}_{1}=\left[\begin{array}{c}-1 / 2 \\ 1 / 2 \\ 0\end{array}\right], \boldsymbol{w}_{3}=\boldsymbol{s}_{3}-$ $\frac{\boldsymbol{s}_{3}^{T} \boldsymbol{w}_{1}}{\boldsymbol{w}_{1}^{T} \boldsymbol{w}_{1}} \boldsymbol{w}_{1}-\frac{\boldsymbol{s}_{3}^{T} \boldsymbol{w}_{2}}{\boldsymbol{w}_{2}^{T} \boldsymbol{w}_{2}} \boldsymbol{w}_{2}=\left[\begin{array}{l}0 \\ 0 \\ 1\end{array}\right]$. Normalizing the $\boldsymbol{w}_{i}$ 's we obtain $\boldsymbol{u}_{1}=\boldsymbol{w}_{1} /\left\|\boldsymbol{w}_{1}\right\|_{2}=$ $[1 / \sqrt{2}, 1 / \sqrt{2}, 0]^{T}, \boldsymbol{u}_{2}=\boldsymbol{w}_{2} /\left\|\boldsymbol{w}_{2}\right\|_{2}=[-1 / \sqrt{2}, 1 / \sqrt{2}, 0]^{T}$, and $\boldsymbol{u}_{3}=\boldsymbol{s}_{3} /\left\|\boldsymbol{s}_{3}\right\|_{2}=$ $[0,0,1]^{T}$. Therefore, $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{T}$, is an SVD, where

$$
\boldsymbol{U}:=\left[\begin{array}{ccc}
1 / \sqrt{2} & -1 / \sqrt{2} & 0 \\
1 / \sqrt{2} & 1 / \sqrt{2} & 0 \\
0 & 0 & 1
\end{array}\right] \in \mathbb{R}^{3,3}, \quad \boldsymbol{\Sigma}:=\left[\begin{array}{ll}
2 & 0 \\
0 & 0 \\
0 & 0
\end{array}\right] \in \mathbb{R}^{3,2}, \quad \boldsymbol{V}:=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right] \in \mathbb{R}^{2,2} .
$$

The method we used to find the singular value decomposition in the examples and exercises can be suitable for hand calculation with small matrices, but it is not appropriate as a basis for a general purpose numerical method. In particular, the Gram-Schmidt orthogonalization process is not numerically stable, and forming $\boldsymbol{A}^{*} \boldsymbol{A}$ can lead to extra errors in the computation. Standard computer implementations of the singular value decomposition [16] first reduces $\boldsymbol{A}$ to bidiagonal form and then use an adapted version of the QR algorithm where the matrix $\boldsymbol{A}^{*} \boldsymbol{A}$ is not formed. The QR algorithm is discussed in Chap. 15.

### 7.2.2 SVD and the Four Fundamental Subspaces

The singular vectors form orthonormal bases for the four fundamental subspaces $\mathcal{R}(\boldsymbol{A}), \mathcal{N}(\boldsymbol{A}), \mathcal{R}\left(\boldsymbol{A}^{*}\right)$, and $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$.

Theorem 7.3 (Singular Vectors and Orthonormal Bases) For positive integers $m, n$ let $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ have rank $r$ and a singular value decomposition $\boldsymbol{A}=$ $\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{m}\right] \boldsymbol{\Sigma}\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right]^{*}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$. Then the singular vectors satisfy

$$
\begin{aligned}
\boldsymbol{A} \boldsymbol{v}_{i} & =\sigma_{i} \boldsymbol{u}_{i}, i=1, \ldots, r, \quad \boldsymbol{A} \boldsymbol{v}_{i}=0, i=r+1, \ldots, n, \\
\boldsymbol{A}^{*} \boldsymbol{u}_{i} & =\sigma_{i} \boldsymbol{v}_{i}, i=1, \ldots, r, \quad \boldsymbol{A}^{*} \boldsymbol{u}_{i}=0, i=r+1, \ldots, m .
\end{aligned}
$$

Moreover,

1. $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}\right\}$ is an orthonormal basis for $\mathcal{R}(\boldsymbol{A})$,
2. $\left\{\boldsymbol{u}_{r+1}, \ldots, \boldsymbol{u}_{m}\right\}$ is an orthonormal basis for $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$,
3. $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{r}\right\}$ is an orthonormal basis for $\mathcal{R}\left(\boldsymbol{A}^{*}\right)$,
4. $\left\{\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{n}\right\}$ is an orthonormal basis for $\mathcal{N}(\boldsymbol{A})$.

Proof If $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ then $\boldsymbol{A} \boldsymbol{V}=\boldsymbol{U} \boldsymbol{\Sigma}$, or in terms of the block partition (7.4) $\boldsymbol{A}\left[\boldsymbol{V}_{1}, \boldsymbol{V}_{2}\right]=\left[\boldsymbol{U}_{1}, \boldsymbol{U}_{2}\right]\left[\begin{array}{cc}\Sigma_{1} & \mathbf{0} \\ \mathbf{0} & \mathbf{0}\end{array}\right]$. But then $\boldsymbol{A} \boldsymbol{V}_{1}=\boldsymbol{U}_{1} \boldsymbol{\Sigma}_{1}, \boldsymbol{A} \boldsymbol{V}_{2}=\mathbf{0}$, and this implies the first part of (7.7). Taking conjugate transpose of $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ gives $\boldsymbol{A}^{*}=\boldsymbol{V} \boldsymbol{\Sigma}^{*} \boldsymbol{U}^{*}$ or $\boldsymbol{A}^{*} \boldsymbol{U}=\boldsymbol{V} \boldsymbol{\Sigma}^{*}$. Using the block partition as before we obtain the last part of (7.7).

It follows from Theorem 7.1 that $\left\{\boldsymbol{A} \boldsymbol{v}_{1}, \ldots, \boldsymbol{A} \boldsymbol{v}_{r}\right\}$ is an orthogonal basis for $\mathcal{R}(\boldsymbol{A}),\left\{\boldsymbol{A}^{*} \boldsymbol{u}_{1}, \ldots, \boldsymbol{A}^{*} \boldsymbol{u}_{r}\right\}$ is an orthogonal basis for $\mathcal{R}\left(\boldsymbol{A}^{*}\right),\left\{\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{m}\right\}$ is an orthonormal basis for $\mathcal{N}(\boldsymbol{A})$ and $\left\{\boldsymbol{u}_{r+1}, \ldots, \boldsymbol{u}_{m}\right\}$ is an orthonormal basis for $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$. By (7.7) $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}\right\}$ is an orthonormal basis for $\mathcal{R}(\boldsymbol{A})$ and $\left\{\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{r}\right\}$ is an orthonormal basis for $\mathcal{R}\left(\boldsymbol{A}^{*}\right)$. $\square$

### 7.3 A Geometric Interpretation

The singular value decomposition and factorization give insight into the geometry of a linear transformation. Consider the linear transformation $\boldsymbol{T}: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$ given by $\boldsymbol{T} \boldsymbol{z}:=\boldsymbol{A} \boldsymbol{z}$ where $\boldsymbol{A} \in \mathbb{R}^{m \times n}$. Assume that rank $(\boldsymbol{A})=n$. In the following theorem we show that the function $\boldsymbol{T}$ maps the unit sphere in $\mathbb{R}^{n}$ given by $\mathcal{S}:=\left\{z \in \mathbb{R}^{n}\right.$ : $\left.\|\boldsymbol{z}\|_{2}=1\right\}$ onto an ellipsoid $\mathcal{E}:=\boldsymbol{A} \mathcal{S}=\{\boldsymbol{A} \boldsymbol{z}: \boldsymbol{z} \in \mathcal{S}\}$ in $\mathbb{R}^{m}$.

Theorem 7.4 (SVF Ellipse) Suppose $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ has rank $r=n$, and let $\boldsymbol{A}=$ $\boldsymbol{U}_{1} \Sigma_{1} \boldsymbol{V}_{1}^{T}$ be a singular value factorization of $\boldsymbol{A}$. Then

$$
\mathcal{E}=\boldsymbol{U}_{1} \tilde{\mathcal{E}} \text { where } \tilde{\mathcal{E}}:=\left\{\boldsymbol{y}=\left[y_{1}, \ldots, y_{n}\right]^{T} \in \mathbb{R}^{n}: \frac{y_{1}^{2}}{\sigma_{1}^{2}}+\cdots+\frac{y_{n}^{2}}{\sigma_{n}^{2}}=1\right\} .
$$

Proof Suppose $z \in \mathcal{S}$. Now $\boldsymbol{A} z=\boldsymbol{U}_{1} \Sigma_{1} \boldsymbol{V}_{1}^{T} z=\boldsymbol{U}_{1} \boldsymbol{y}$, where $\boldsymbol{y}:=\Sigma_{1} \boldsymbol{V}_{1}^{T} \boldsymbol{z}$. Since $\operatorname{rank}(\boldsymbol{A})=n$ it follows that $\boldsymbol{V}_{1}=\boldsymbol{V}$ is square so that $\boldsymbol{V}_{1} \boldsymbol{V}_{1}^{T}=\boldsymbol{I}$. But then $\boldsymbol{V}_{1} \boldsymbol{\Sigma}_{1}^{-1} \boldsymbol{y}=\boldsymbol{z}$ and we obtain

$$
1=\|z\|_{2}^{2}=\left\|\boldsymbol{V}_{1} \boldsymbol{\Sigma}_{1}^{-1} \boldsymbol{y}\right\|_{2}^{2}=\left\|\boldsymbol{\Sigma}_{1}^{-1} \boldsymbol{y}\right\|_{2}^{2}=\frac{y_{1}^{2}}{\sigma_{1}^{2}}+\cdots+\frac{y_{n}^{2}}{\sigma_{n}^{2}} .
$$

This implies that $\boldsymbol{y} \in \tilde{\mathcal{E}}$. Finally, $\boldsymbol{x}=\boldsymbol{A} \boldsymbol{z}=\boldsymbol{U}_{1} \Sigma_{1} \boldsymbol{V}_{1}^{T} \boldsymbol{z}=\boldsymbol{U}_{1} \boldsymbol{y}$, where $\boldsymbol{y} \in \tilde{\mathcal{E}}$ implies that $\mathcal{E}=\boldsymbol{U}_{1} \tilde{\mathcal{E}}$. $\square$

The equation $1=\frac{y_{1}^{2}}{\sigma_{1}^{2}}+\cdots+\frac{y_{n}^{2}}{\sigma_{n}^{2}}$ describes an ellipsoid in $\mathbb{R}^{n}$ with semiaxes of length $\sigma_{j}$ along the unit vectors $\boldsymbol{e}_{j}$ for $j=1, \ldots, n$. Since the orthonormal transformation $\boldsymbol{U}_{1} \boldsymbol{y} \rightarrow \boldsymbol{x}$ preserves length, the image $\mathcal{E}=\boldsymbol{A} \mathcal{S}$ is a rotated ellipsoid with semiaxes along the left singular vectors $\boldsymbol{u}_{j}=\boldsymbol{U} \boldsymbol{e}_{j}$, of length $\sigma_{j}, j=1, \ldots, n$. Since $\boldsymbol{A} \boldsymbol{v}_{j}=\sigma_{j} \boldsymbol{u}_{j}$, for $j=1, \ldots, n$ the right singular vectors defines points in $\mathcal{S}$ that are mapped onto the semiaxes of $\mathcal{E}$.
Example 7.4 (Ellipse) Consider the transformation $\boldsymbol{A}: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$ given by the matrix

$$
A:=\frac{1}{25}\left[\begin{array}{ll}
11 & 48 \\
48 & 39
\end{array}\right]
$$

in Example 7.8. Recall that $\sigma_{1}=3, \sigma_{2}=1, \boldsymbol{u}_{1}=[3,4]^{T} / 5$ and $\boldsymbol{u}_{2}=[-4,3]^{T} / 5$. The ellipses $y_{1}^{2} / \sigma_{1}^{2}+y_{2}^{2} / \sigma_{2}^{2}=1$ and $\mathcal{E}=\boldsymbol{A} \mathcal{S}=\boldsymbol{U}_{1} \tilde{\mathcal{E}}$ are shown in Fig. 7.1. Since

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-175.jpg?height=524&width=1142&top_left_y=1371&top_left_x=196)
Fig. 7.1 The ellipse $y_{1}^{2} / 9+y_{2}^{2}=1$ (left) and the rotated ellipse $\boldsymbol{A} \mathcal{S}$ (right)

$\boldsymbol{y}=\boldsymbol{U}_{1}^{T} \boldsymbol{x}=\left[3 / 5 x_{1}+4 / 5 x_{2},-4 / 5 x_{1}+3 / 5 x_{2}\right]^{T}$, the equation for the ellipse on the right is

$$
\frac{\left(\frac{3}{5} x_{1}+\frac{4}{5} x_{2}\right)^{2}}{9}+\frac{\left(-\frac{4}{5} x_{1}+\frac{3}{5} x_{2}\right)^{2}}{1}=1,
$$

### 7.4 Determining the Rank of a Matrix Numerically

In many elementary linear algebra courses a version of Gaussian elimination, called Gauss-Jordan elimination, is used to determine the rank of a matrix. To carry this out by hand for a large matrix can be a Herculean task and using a computer and floating point arithmetic the result will not be reliable. Entries, which in the final result should have been zero, will have nonzero values because of round-off errors. As an alternative we can use the singular value decomposition to determine rank. Although success is not at all guaranteed, the result will be more reliable than if Gauss-Jordan elimination is used.

By Theorem 7.2 the rank of a matrix is equal to the number of nonzero singular values, and if we have computed the singular values, then all we have to do is to count the nonzero ones. The problem however is the same as for Gaussian elimination. Due to round-off errors none of the computed singular values are likely to be zero.

### 7.4.1 The Frobenius Norm

This commonly occurring matrix norm will be used here in a discussion of how many of the computed singular values can possibly be considered to be zero. The Frobenius norm, of a matrix $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ is defined by

$$
\|\boldsymbol{A}\|_{F}:=\left(\sum_{i=1}^{m} \sum_{j=1}^{n}\left|a_{i j}\right|^{2}\right)^{1 / 2} .
$$

There is a relation between the Frobenius norm of a matrix and its singular values. First we derive some elementary properties of this norm. A systematic study of matrix norms is given in the next chapter.

Lemma 7.1 (Frobenius Norm Properties) For any $m, n \in \mathbb{N}$ and any matrix $\boldsymbol{A} \in$ $\mathbb{C}^{m \times n}$

1. $\left\|\boldsymbol{A}^{*}\right\|_{F}=\|\boldsymbol{A}\|_{F}$,
2. $\|\boldsymbol{A}\|_{F}^{2}=\sum_{j=1}^{n}\left\|\boldsymbol{a}_{: j}\right\|_{2}^{2}$,

3. $\|\boldsymbol{U} \boldsymbol{A}\|_{F}=\|\boldsymbol{A} \boldsymbol{V}\|_{F}=\|\boldsymbol{A}\|_{F}$ for any unitary matrices $\boldsymbol{U} \in \mathbb{C}^{m \times m}$ and $\boldsymbol{V} \in$ $\mathbb{C}^{n \times n}$,
4. $\|\boldsymbol{A} \boldsymbol{B}\|_{F} \leq\|\boldsymbol{A}\|_{F}\|\boldsymbol{B}\|_{F}$ for any $\boldsymbol{B} \in \mathbb{C}^{n, k}, \quad k \in \mathbb{N}$,
5. $\|\boldsymbol{A} \boldsymbol{x}\|_{2} \leq\|\boldsymbol{A}\|_{F}\|\boldsymbol{x}\|_{2}$, for all $\boldsymbol{x} \in \mathbb{C}^{n}$.

Proof

1. $\left\|\boldsymbol{A}^{*}\right\|_{F}^{2}=\sum_{j=1}^{n} \sum_{i=1}^{m}\left|\bar{a}_{i j}\right|^{2}=\sum_{i=1}^{m} \sum_{j=1}^{n}\left|a_{i j}\right|^{2}=\|\boldsymbol{A}\|_{F}^{2}$.
2. This follows since the Frobenius norm is the Euclidian norm of a vector, $\|\boldsymbol{A}\|_{F}:=\|\operatorname{vec}(\boldsymbol{A})\|_{2}$, where $\operatorname{vec}(\boldsymbol{A}) \in \mathbb{C}^{m n}$ is the vector obtained by stacking the columns $\boldsymbol{a}_{: j}$ of $\boldsymbol{A}$ on top of each other.
3. Recall that if $\boldsymbol{U}^{*} \boldsymbol{U}=I$ then $\|\boldsymbol{U} \boldsymbol{x}\|_{2}=\|\boldsymbol{x}\|_{2}$ for all $\boldsymbol{x} \in \mathbb{C}^{n}$. Applying this to each column $\boldsymbol{a}_{: j}$ of $\boldsymbol{A}$ we find $\|\boldsymbol{U} \boldsymbol{A}\|_{F}^{2} \stackrel{2 .}{=} \sum_{j=1}^{n}\left\|\boldsymbol{U} \boldsymbol{a}_{: j}\right\|_{2}^{2}=\sum_{j=1}^{n}\left\|\boldsymbol{a}_{: j}\right\|_{2}^{2} \stackrel{2 .}{=}\|\boldsymbol{A}\|_{F}^{2}$. Similarly, since $\boldsymbol{V} \boldsymbol{V}^{*}=I$ we find $\|\boldsymbol{A} \boldsymbol{V}\|_{F} \stackrel{1 .}{=}\left\|\boldsymbol{V}^{*} \boldsymbol{A}^{*}\right\|_{F}=\left\|\boldsymbol{A}^{*}\right\|_{F} \stackrel{1 .}{=}\|\boldsymbol{A}\|_{F}$.
4. Using the Cauchy-Schwarz inequality and 2. we obtain
$$
\|\boldsymbol{A} \boldsymbol{B}\|_{F}^{2}=\sum_{i=1}^{m} \sum_{j=1}^{k}\left|\boldsymbol{a}_{i:}^{*} \boldsymbol{b}_{: j}\right|^{2} \leq \sum_{i=1}^{m} \sum_{j=1}^{k}\left\|\boldsymbol{a}_{i:}\right\|_{2}^{2}\left\|\boldsymbol{b}_{: j}\right\|_{2}^{2}=\|\boldsymbol{A}\|_{F}^{2}\|\boldsymbol{B}\|_{F}^{2} .
$$
5. Since $\|\boldsymbol{v}\|_{F}=\|\boldsymbol{v}\|_{2}$ for a vector this follows by taking $k=1$ and $\boldsymbol{B}=\boldsymbol{x}$ in 4 .

Theorem 7.5 (Frobenius Norm and Singular Values) We have $\|\boldsymbol{A}\|_{F}=$ $\sqrt{\sigma_{1}^{2}+\cdots+\sigma_{n}^{2}}$, where $\sigma_{1}, \ldots, \sigma_{n}$ are the singular values of $\boldsymbol{A}$.

Proof Using Lemma 7.1 we find

$$
\|\boldsymbol{A}\|_{F} \stackrel{\text { 3. }}{=}\left\|\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{V}\right\|_{F}=\|\boldsymbol{\Sigma}\|_{F}=\sqrt{\sigma_{1}^{2}+\cdots+\sigma_{n}^{2}} .
$$ $\square$

### 7.4.2 Low Rank Approximation

Suppose $m \geq n \geq 1$ and $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has a singular value decomposition $\boldsymbol{A}=$ $\boldsymbol{U}\left[\begin{array}{c}\boldsymbol{D} \\ \mathbf{0}\end{array}\right] \boldsymbol{V}^{*}$, where $\boldsymbol{D}=\operatorname{diag}\left(\sigma_{1}, \ldots, \sigma_{n}\right)$. We choose $\epsilon>0$ and let $1 \leq r \leq n$ be the smallest integer such that $\sigma_{r+1}^{2}+\cdots+\sigma_{n}^{2}<\epsilon^{2}$. Define $\boldsymbol{A}^{\prime}:=\boldsymbol{U}\left[\begin{array}{c}\boldsymbol{D}^{\prime} \\ \mathbf{0}\end{array}\right] \boldsymbol{V}^{*}$, where $\boldsymbol{D}^{\prime}:=\operatorname{diag}\left(\sigma_{1}, \ldots, \sigma_{r}, 0, \ldots, 0\right) \in \mathbb{R}^{n \times n}$. By Lemma 7.1

$$
\left\|\boldsymbol{A}-\boldsymbol{A}^{\prime}\right\|_{F}=\left\|\boldsymbol{U}\left[\begin{array}{c}
\boldsymbol{D}-\boldsymbol{D}^{\prime} \\
\mathbf{0}
\end{array}\right] \boldsymbol{V}^{*}\right\|_{F}=\left\|\left[\begin{array}{c}
\boldsymbol{D}-\boldsymbol{D}^{\prime} \\
\mathbf{0}
\end{array}\right]\right\|_{F}=\sqrt{\sigma_{r+1}^{2}+\cdots+\sigma_{n}^{2}}<\epsilon .
$$

Thus, if $\epsilon$ is small then $\boldsymbol{A}$ is near a matrix $\boldsymbol{A}^{\prime}$ of rank $r$. This can be used to determine rank numerically. We choose an $r$ such that $\sqrt{\sigma_{r+1}^{2}+\cdots+\sigma_{n}^{2}}$ is "small". Then we postulate that $\operatorname{rank}(\boldsymbol{A})=r$ since $\boldsymbol{A}$ is close to a matrix of rank $r$.

The following theorem shows that of all $m \times n$ matrices of rank $r, \boldsymbol{A}^{\prime}$ is closest to $\boldsymbol{A}$ measured in the Frobenius norm.

Theorem 7.6 (Best Low Rank Approximation) Suppose $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ has singular values $\sigma_{1} \geq \cdots \geq \sigma_{n} \geq 0$. For any $r \leq \operatorname{rank}(\boldsymbol{A})$ we have

$$
\left\|\boldsymbol{A}-\boldsymbol{A}^{\prime}\right\|_{F}=\min _{\substack{\boldsymbol{B} \in \mathbb{R}^{m \times n} \\ \operatorname{rank}(\boldsymbol{B})=r}}\|\boldsymbol{A}-\boldsymbol{B}\|_{F}=\sqrt{\sigma_{r+1}^{2}+\cdots+\sigma_{n}^{2}} .
$$

For the proof of this theorem we refer to p. 322 of [16].

### 7.5 Exercises Chap. 7

### 7.5.1 Exercises Sect. 7.1

Exercise 7.1 (SVD1) Show that the decomposition

$$
\boldsymbol{A}:=\left[\begin{array}{ll}
1 & 1 \\
1 & 1
\end{array}\right]=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right]\left[\begin{array}{ll}
2 & 0 \\
0 & 0
\end{array}\right] \frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right]=\boldsymbol{U} \boldsymbol{D} \boldsymbol{U}^{T}
$$

is both a spectral decomposition and a singular value decomposition.
Exercise 7.2 (SVD2) Show that the decomposition

$$
\boldsymbol{A}:=\left[\begin{array}{ll}
1 & -1 \\
1 & -1
\end{array}\right]=\frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right]\left[\begin{array}{ll}
2 & 0 \\
0 & 0
\end{array}\right] \frac{1}{\sqrt{2}}\left[\begin{array}{cc}
1 & -1 \\
1 & 1
\end{array}\right]=: \boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{T}
$$

is a singular value decomposition. Show that $\boldsymbol{A}$ is defective so it cannot be diagonalized by any similarity transformation.

Exercise 7.3 (SVD Examples) Find the singular value decomposition of the following matrices

a) $\boldsymbol{A}=\left[\begin{array}{l}3 \\ 4\end{array}\right]$.
b) $\boldsymbol{A}=\left[\begin{array}{ll}1 & 1 \\ 2 & 2 \\ 2 & 2\end{array}\right]$.

Exercise 7.4 (More SVD Examples) Find the singular value decomposition of the following matrices

a) $\boldsymbol{A}=\boldsymbol{e}_{1}$ the first unit vector in $\mathbb{R}^{m}$.
b) $\boldsymbol{A}=\boldsymbol{e}_{n}^{T}$ the last unit vector in $\mathbb{R}^{n}$.
c) $\boldsymbol{A}=\left[\begin{array}{rr}-1 & 0 \\ 0 & 3\end{array}\right]$.

Exercise 7.5 (Singular Values of a Normal Matrix) Show that

a) the singular values of a normal matrix are the absolute values of its eigenvalues,
b) the singular values of a symmetric positive semidefinite matrix are its eigenvalues.

Exercise 7.6 (The Matrices $\boldsymbol{A}^{*} \boldsymbol{A}, \boldsymbol{A} \boldsymbol{A}^{*}$ and SVD) Show the following: If $\boldsymbol{A}=$ $\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}$ is a singular value decomposition of $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ then

a) $\boldsymbol{A}^{*} \boldsymbol{A}=\boldsymbol{V} \operatorname{diag}\left(\sigma_{1}^{2}, \ldots, \sigma_{n}^{2}\right) \boldsymbol{V}^{*}$ is a spectral decomposition of $\boldsymbol{A}^{*} \boldsymbol{A}$.
b) $\boldsymbol{A} \boldsymbol{A}^{*}=\boldsymbol{U} \operatorname{diag}\left(\sigma_{1}^{2}, \ldots, \sigma_{m}^{2}\right) \boldsymbol{U}^{*}$ is a spectral decomposition of $\boldsymbol{A} \boldsymbol{A}^{*}$.
c) The columns of $\boldsymbol{U}$ are orthonormal eigenvectors of $\boldsymbol{A} \boldsymbol{A}^{*}$.
d) The columns of $\boldsymbol{V}$ are orthonormal eigenvectors of $\boldsymbol{A}^{*} \boldsymbol{A}$.

Exercise 7.7 (Singular Values (Exam Exercise 2005-2)) Given the statement: "If $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ has singular values $\left(\sigma_{1}, \ldots, \sigma_{n}\right)$ then $\boldsymbol{A}^{2}$ has singular values $\left(\sigma_{1}^{2}, \ldots, \sigma_{n}^{2}\right)$ ". Find a class of matrices for which the statement is true. Show that the statement is not true in general.

### 7.5.2 Exercises Sect. 7.2

Exercise 7.8 (Nonsingular Matrix) Derive the SVF and SVD of the matrix ${ }^{1}$ $\boldsymbol{A}=\frac{1}{25}\left[\begin{array}{ll}11 & 48 \\ 48 & 39\end{array}\right]$. Also, using possibly a computer, find its spectral decomposition $\boldsymbol{U} \boldsymbol{D} \boldsymbol{U}^{T}$. The matrix $\boldsymbol{A}$ is normal, but the spectral decomposition is not an SVD. Why?

Exercise 7.9 (Full Row Rank) Find ${ }^{2}$ the SVF and SVD of

$$
A:=\frac{1}{15}\left[\begin{array}{ccc}
14 & 4 & 16 \\
2 & 22 & 13
\end{array}\right] \in \mathbb{R}^{2 \times 3} .
$$

[^15]Exercise 7.10 (Counting Dimensions of Fundamental Subspaces) Suppose $\boldsymbol{A} \in$ $\mathbb{C}^{m \times n}$. Show using SVD that

a) $\operatorname{rank}(\boldsymbol{A})=\operatorname{rank}\left(\boldsymbol{A}^{*}\right)$.
b) $\operatorname{rank}(\boldsymbol{A})+\operatorname{null}(\boldsymbol{A})=n$,
c) $\operatorname{rank}(\boldsymbol{A})+\operatorname{null}\left(\boldsymbol{A}^{*}\right)=m$,

where $\operatorname{null}(\boldsymbol{A})$ is defined as the dimension of $\mathcal{N}(\boldsymbol{A})$.
Exercise 7.11 (Rank and Nullity Relations) Use Theorem 7.1 to show that for any $\boldsymbol{A} \in \mathbb{C}^{m \times n}$

a) $\operatorname{rank} \boldsymbol{A}=\operatorname{rank}\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)=\operatorname{rank}\left(\boldsymbol{A} \boldsymbol{A}^{*}\right)$,
b) $\operatorname{null}\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)=\operatorname{null} \boldsymbol{A}$, and $\operatorname{null}\left(\boldsymbol{A} \boldsymbol{A}^{*}\right)=\operatorname{null}\left(\boldsymbol{A}^{*}\right)$.

Exercise 7.12 (Orthonormal Bases Example) Let $\boldsymbol{A}$ and $\boldsymbol{B}$ be as in Example 7.2. Give orthonormal bases for $\mathcal{R}(\boldsymbol{B})$ and $\mathcal{N}(\boldsymbol{B})$.

Exercise 7.13 (Some Spanning Sets) Show for any $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ that $\mathcal{R}\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)=$ $\mathcal{R}\left(\boldsymbol{V}_{1}\right)=\mathcal{R}\left(\boldsymbol{A}^{*}\right)$

Exercise 7.14 (Singular Values and Eigenpair of Composite Matrix) Let $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ with $m \geq n$ have singular values $\sigma_{1}, \ldots, \sigma_{n}$, left singular vectors $\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{m} \in \mathbb{C}^{m}$, and right singular vectors $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n} \in \mathbb{C}^{n}$. Show that the matrix

$$
\boldsymbol{C}:=\left[\begin{array}{cc}
\mathbf{0} & \boldsymbol{A} \\
\boldsymbol{A}^{*} & \mathbf{0}
\end{array}\right] \in \mathbb{R}^{(m+n) \times(m+n)}
$$

has the $n+m$ eigenpairs

$$
\left\{\left(\sigma_{1}, \boldsymbol{p}_{1}\right), \ldots,\left(\sigma_{n}, \boldsymbol{p}_{n}\right),\left(-\sigma_{1}, \boldsymbol{q}_{1}\right), \ldots,\left(-\sigma_{n}, \boldsymbol{q}_{n}\right),\left(0, \boldsymbol{r}_{n+1}\right), \ldots,\left(0, \boldsymbol{r}_{m}\right)\right\},
$$

where

$$
\boldsymbol{p}_{i}=\left[\begin{array}{c}
\boldsymbol{u}_{i} \\
\boldsymbol{v}_{i}
\end{array}\right], \quad \boldsymbol{q}_{i}=\left[\begin{array}{c}
\boldsymbol{u}_{i} \\
-\boldsymbol{v}_{i}
\end{array}\right], \quad \boldsymbol{r}_{j}=\left[\begin{array}{c}
\boldsymbol{u}_{j} \\
\mathbf{0}
\end{array}\right], \text { for } i=1, \ldots, n, j=n+1, \ldots, m .
$$

Exercise 7.15 (Polar Decomposition (Exam Exercise 2011-2)) Given $n \in \mathbb{N}$ and a singular value decomposition $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{T}$ of a square matrix $\boldsymbol{A} \in \mathbb{R}^{n, n}$, consider the matrices

$$
\boldsymbol{Q}:=\boldsymbol{U} \boldsymbol{V}^{T}, \quad \boldsymbol{P}:=\boldsymbol{V} \boldsymbol{\Sigma} \boldsymbol{V}^{T}
$$

of order $n$.

a) Show that
$$
A=Q P
$$
and show that $\boldsymbol{Q}$ is orthonormal.

b) Show that $\boldsymbol{P}$ is symmetric positive semidefinite and positive definite if $\boldsymbol{A}$ is nonsingular. The factorization in (7.13) is called a polar factorization
c) Use the singular value decomposition of $\boldsymbol{A}$ to give a suitable definition of $\boldsymbol{B}:=$ $\sqrt{\boldsymbol{A}^{T} \boldsymbol{A}}$ so that $\boldsymbol{P}=\boldsymbol{B}$.

For the rest of this problem assume that $\boldsymbol{A}$ is nonsingular. Consider the iterative method

$$
\boldsymbol{X}_{k+1}=\frac{1}{2}\left(\boldsymbol{X}_{k}+\boldsymbol{X}_{k}^{-T}\right), k=0,1,2, \ldots \text { with } \boldsymbol{X}_{0}=\boldsymbol{A},
$$

for finding $\boldsymbol{Q}$.

d) Show that the iteration (7.14) is well defined by showing that $\boldsymbol{X}_{k}=\boldsymbol{U} \boldsymbol{\Sigma}_{k} \boldsymbol{V}^{T}$, for a diagonal matrix $\Sigma_{k}$ with positive diagonal elements, $k=0,1,2, \ldots$.
e) Show that
$$
\boldsymbol{X}_{k+1}-\boldsymbol{Q}=\frac{1}{2} \boldsymbol{X}_{k}^{-T}\left(\boldsymbol{X}_{k}^{T}-\boldsymbol{Q}^{T}\right)\left(\boldsymbol{X}_{k}-\boldsymbol{Q}\right)
$$
and use (7.15) and the Frobenius norm to show (quadratic convergence to $\boldsymbol{Q}$ )
$$
\left\|\boldsymbol{X}_{k+1}-\boldsymbol{Q}\right\|_{F} \leq \frac{1}{2}\left\|\boldsymbol{X}_{k}^{-1}\right\|_{F}\left\|\boldsymbol{X}_{k}-\boldsymbol{Q}\right\|_{F}^{2} .
$$
f) Write a MATLAB program
function $[\mathrm{Q}, \mathrm{P}, \mathrm{k}]=$ polardecomp $(\mathrm{A}, \mathrm{tol}, \mathrm{K})$ to carry out the iteration in (7.14). The output is approximations $\boldsymbol{Q}$ and $\boldsymbol{P}=\boldsymbol{Q}^{T} \boldsymbol{A}$ to the polar decomposition $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{P}$ of $\boldsymbol{A}$ and the number of iterations $k$ such that $\left\|\boldsymbol{X}_{k+1}-\boldsymbol{X}_{k}\right\|_{F}<$ tol $*\left\|\boldsymbol{X}_{k+1}\right\|_{F}$. Set $k=K+1$ if convergence is not achieved in $K$ iterations. The Frobenius norm in MATLAB is written norm (A, ' fro' ).

Exercise 7.16 (Underdetermined System (Exam Exercise 2015-1))

a) Let $\boldsymbol{A}$ be the matrix
$$
\boldsymbol{A}=\left[\begin{array}{cc}
1 & 2 \\
0 & 1 \\
-1 & 3
\end{array}\right] .
$$
Compute $\|\boldsymbol{A}\|_{1}$ and $\|\boldsymbol{A}\|_{\infty}$.
b) Let $\boldsymbol{B}$ be the matrix
$$
\boldsymbol{B}=\left[\begin{array}{ccc}
1 & 0 & -1 \\
1 & 1 & 1
\end{array}\right] .
$$
Find the spaces span $\left(\boldsymbol{B}^{T}\right)$ and $\operatorname{ker}(\boldsymbol{B})$.

c) Consider the underdetermined linear system
$$
\begin{aligned}
& x_{1}-x_{3}=4, \\
& x_{1}+x_{2}+x_{3}=12 .
\end{aligned}
$$
Find the solution $\boldsymbol{x} \in \mathbb{R}^{3}$ with $\|\boldsymbol{x}\|_{2}$ as small as possible.
d) Let $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ be a matrix with linearly independent columns, and $\boldsymbol{b} \in \mathbb{R}^{m}$ a vector. Assume that we use the Gauss-Seidel method (cf. Chap. 12) to solve the normal equations $\boldsymbol{A}^{T} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{T} \boldsymbol{b}$. Will the method converge? Justify your answer.

### 7.5.3 Exercises Sect. 7.4

Exercise 7.17 (Rank Example) Consider the singular value decomposition

$$
\boldsymbol{A}:=\left[\begin{array}{rrr}
0 & 3 & 3 \\
4 & 1 & -1 \\
4 & 1 & -1 \\
0 & 3 & 3
\end{array}\right]=\left[\begin{array}{rrrr}
\frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2}
\end{array}\right]\left[\begin{array}{lll}
6 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]\left[\begin{array}{rrr}
\frac{2}{3} & \frac{2}{3} & \frac{1}{3} \\
\frac{2}{3} & -\frac{1}{3} & -\frac{2}{3} \\
\frac{1}{3} & -\frac{2}{3} & \frac{2}{3}
\end{array}\right]
$$

a) Give orthonormal bases for $\mathcal{R}(\boldsymbol{A}), \mathcal{R}\left(\boldsymbol{A}^{T}\right), \mathcal{N}(\boldsymbol{A})$ and $\mathcal{N}\left(\boldsymbol{A}^{T}\right)$.
b) Explain why for all matrices $\boldsymbol{B} \in \mathbb{R}^{4,3}$ of rank one we have $\|\boldsymbol{A}-\boldsymbol{B}\|_{F} \geq 6$.
c) Give a matrix $\boldsymbol{A}_{1}$ of rank one such that $\left\|\boldsymbol{A}-\boldsymbol{A}_{1}\right\|_{F}=6$.

Exercise 7.18 (Another Rank Example) Let $\boldsymbol{A}$ be the $n \times n$ matrix that for $n=4$ takes the form

$$
\boldsymbol{A}=\left[\begin{array}{rrrr}
1 & -1 & -1 & -1 \\
0 & 1 & -1 & -1 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & 1
\end{array}\right] .
$$

Thus $\boldsymbol{A}$ is upper triangular with diagonal elements one and all elements above the diagonal equal to -1 . Let $\boldsymbol{B}$ be the matrix obtained from $\boldsymbol{A}$ by changing the $(n, 1)$ element from zero to $-2^{2-n}$.

a) Show that $\boldsymbol{B} \boldsymbol{x}=\mathbf{0}$, where $\boldsymbol{x}:=\left[2^{n-2}, 2^{n-3}, \ldots, 2^{0}, 1\right]^{T}$. Conclude that $\boldsymbol{B}$ is singular, $\operatorname{det}(\boldsymbol{A})=1$, and $\|\boldsymbol{A}-\boldsymbol{B}\|_{F}=2^{2-n}$. Thus even if $\operatorname{det}(\boldsymbol{A})$ is not small the Frobenius norm of $\boldsymbol{A}-\boldsymbol{B}$ is small for large $n$, and the matrix $\boldsymbol{A}$ is very close to being singular for large $n$.
b) Use Theorem 7.6 to show that the smallest singular vale $\sigma_{n}$ of $\boldsymbol{A}$ is bounded above by $2^{2-n}$.

Exercise 7.19 (Norms, Cholesky and SVD (Exam Exercise 2016-1))

a) Let $\boldsymbol{A}$ be the matrix
$$
\boldsymbol{A}=\left[\begin{array}{cc}
3 & 1 \\
2 & 3 \\
-1 & 5
\end{array}\right] .
$$
Compute $\|\boldsymbol{A}\|_{1},\|\boldsymbol{A}\|_{\infty}$ and $\|\boldsymbol{A}\|_{F}$.
b) Let $\boldsymbol{T}$ be the matrix
$$
\boldsymbol{T}=\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right] .
$$
Show that $\boldsymbol{T}$ is symmetric positive definite, and find the Cholesky factorization $\boldsymbol{T}=\boldsymbol{L} \boldsymbol{L}^{T}$ of $\boldsymbol{T}$.
c) Let $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ be a singular value decomposition of the $m \times n$-matrix $\boldsymbol{A}$ with $m \geq n$, and let $\boldsymbol{A}^{\prime}=\sum_{i=1}^{r} \sigma_{i} \boldsymbol{u}_{i} \boldsymbol{v}_{i}^{*}$, where $1 \leq r \leq n, \sigma_{i}$ are the singular values of $\boldsymbol{A}$, and where $\boldsymbol{u}_{i}, \boldsymbol{v}_{i}$ are the columns of $\boldsymbol{U}$ and $\boldsymbol{V}$. Prove that
$$
\left\|\boldsymbol{A}-\boldsymbol{A}^{\prime}\right\|_{F}^{2}=\sigma_{r+1}^{2}+\cdots+\sigma_{n}^{2} .
$$

### 7.6 Review Questions

7.6.1 Consider an SVD and an SVF of a matrix $\boldsymbol{A}$.
    - What are the singular values of $\boldsymbol{A}$ ?
    - how is the SVD defined?
    - how can we find an SVF if we know an SVD?
    - how can we find an SVD if we know an SVF?
    - what are the relations between the singular vectors?
    - which singular vectors form bases for $\mathcal{R}(\boldsymbol{A})$ and $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$ ?
7.6.2 How are the Frobenius norm and singular values related?

## Part III <br> Matrix Norms and Least Squares

We introduce vector and matrix norms and use them to study how sensitive the solution of a linear system is to perturbation in the data. This leads to the important concept of condition number.

In the second chapter in this part we consider solving linear systems in the least squares sense. We give examples, the basic theory, discuss numerical methods and perturbation theory. Singular values and the important concept of generalized inverses play a central role in our presentation.

## Chapter 8 <br> Matrix Norms and Perturbation Theory for Linear Systems

Norms are used to measure the size of vector and matrices.

### 8.1 Vector Norms

Definition 8.1 (Vector Norm) A (vector) norm in a real (resp. complex) vector space $\mathcal{V}$ is a function $\|\cdot\|: \mathcal{V} \rightarrow \mathbb{R}$ that satisfies for all $\boldsymbol{x}, \boldsymbol{y}$ in $\mathcal{V}$ and all $a$ in $\mathbb{R}$ (resp. $\mathbb{C}$ )

1. $\|\boldsymbol{x}\| \geq 0$ with equality if and only if $\boldsymbol{x}=\mathbf{0}$.
2. $\|a \boldsymbol{x}\|=|a|\|\boldsymbol{x}\|$.
3. $\|\boldsymbol{x}+\boldsymbol{y}\| \leq\|\boldsymbol{x}\|+\|\boldsymbol{y}\|$.

The triple $(\mathcal{V}, \mathbb{R},\|\cdot\|)$ (resp. $(\mathcal{V}, \mathbb{C},\|\cdot\|)$ ) is called a normed vector space and the inequality 3. is called the triangle inequality.

In this book the vector space will be one of $\mathbb{R}^{n}, \mathbb{C}^{n}$ or one of the matrix spaces $\mathbb{R}^{m \times n}$, or $\mathbb{C}^{m \times n}$. Vector addition is defined by element wise addition and scalar multiplication is defined by multiplying every element by the scalar.

We encountered norms associated with any inner product in $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$ in Chap. 5. That these inner product norms are really norms was shown in Theorem 5.2. In this book we will use the following family of vector norms on $\mathcal{V}=\mathbb{C}^{n}$ and $\mathcal{V}=\mathbb{R}^{n}$.

Definition 8.2 (Vector p-Norms) We define for $p \geq 1$ and $\boldsymbol{x} \in \mathbb{R}^{n}$ or $\boldsymbol{x} \in \mathbb{C}^{n}$ the $p$-norms by

$$
\begin{aligned}
\|\boldsymbol{x}\|_{p} & :=\left(\sum_{j=1}^{n}\left|x_{j}\right|^{p}\right)^{1 / p}, \\
\|\boldsymbol{x}\|_{\infty} & :=\max _{1 \leq j \leq n}\left|x_{j}\right| .
\end{aligned}
$$

The most important cases are $p=1,2, \infty$ :

1. $\|\boldsymbol{x}\|_{1}:=\sum_{j=1}^{n}\left|x_{j}\right|$,

(the one-norm or $l_{1}$-norm)

2. $\|\boldsymbol{x}\|_{2}:=\sqrt{\sum_{j=1}^{n}\left|x_{j}\right|^{2}}$, (the two-norm, $l_{2}$-norm, or Euclidian norm)
3. $\|\boldsymbol{x}\|_{\infty}:=\max _{1 \leq j \leq n}\left|x_{j}\right|$, (the infinity-norm, $l_{\infty}$-norm, or max norm) Some remarks are in order.
1. In Sect. 8.4, we show that the $p$-norms are vector norms for $1 \leq p \leq \infty$.
2. The triangle inequality $\|\boldsymbol{x}+\boldsymbol{y}\|_{p} \leq\|\boldsymbol{x}\|_{p}+\|\boldsymbol{y}\|_{p}$ is called Minkowski's inequality.
3. To prove it one first establishes Hölder's inequality
$$
\sum_{j=1}^{n}\left|x_{j} y_{j}\right| \leq\|\boldsymbol{x}\|_{p}\|\boldsymbol{y}\|_{q}, \quad \frac{1}{p}+\frac{1}{q}=1, \quad \boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n} .
$$
The relation $\frac{1}{p}+\frac{1}{q}=1$ means that if $p=1$ then $q=\infty$ and vice versa. The Hölder's inequality is the same as the Cauchy-Schwarz inequality (cf. Theorem 5.1) for the Euclidian norm $p=2$.
4. The infinity norm is related to the other $p$-norms by
$$
\lim _{p \rightarrow \infty}\|\boldsymbol{x}\|_{p}=\|\boldsymbol{x}\|_{\infty} \text { for all } \boldsymbol{x} \in \mathbb{C}^{n} .
$$
5. The equation (8.4) clearly holds for $\boldsymbol{x}=\mathbf{0}$. For $\boldsymbol{x} \neq \mathbf{0}$ we write
$$
\|\boldsymbol{x}\|_{p}:=\|\boldsymbol{x}\|_{\infty}\left(\sum_{j=1}^{n}\left(\frac{\left|x_{j}\right|}{\|\boldsymbol{x}\|_{\infty}}\right)^{p}\right)^{1 / p} .
$$
Now each term in the sum is not greater than one and at least one term is equal to one, and we obtain
$$
\|x\|_{\infty} \leq\|x\|_{p} \leq n^{1 / p}\|x\|_{\infty}, \quad p \geq 1 .
$$
Since $\lim _{p \rightarrow \infty} n^{1 / p}=1$ for any fixed $n \in \mathbb{N}$, we see that (8.4) follows.
6. In Exercise 8.28 we show the following generalization of inequality (8.5)

$$
\|\boldsymbol{x}\|_{p^{\prime}} \leq\|\boldsymbol{x}\|_{p} \leq n^{1 / p-1 / p^{\prime}}\|\boldsymbol{x}\|_{p^{\prime}}, \quad \boldsymbol{x} \in \mathbb{C}^{n}, \quad 1 \leq p \leq p^{\prime} \leq \infty .
$$

We return now to the general vector norm case.
Definition 8.3 (Equivalent Norms) We say that two norms $\|\cdot\|$ and $\|\cdot\|^{\prime}$ on $\mathcal{V}$ are equivalent if there are positive constants $m$ and $M$ such that for all vectors $\boldsymbol{x} \in \mathcal{V}$ we have

$$
m\|\boldsymbol{x}\|^{\prime} \leq\|\boldsymbol{x}\| \leq M\|\boldsymbol{x}\|^{\prime} .
$$

By (8.5) the $p$ - and $\infty$-norms are equivalent for any $p \geq 1$. This result is generalized in the following theorem.

Theorem 8.1 (Basic Properties of Vector Norms) The following holds for a normed vector space $(\mathcal{V}, \mathbb{C},\|\cdot\|)$.

1. $\|\boldsymbol{x}-\boldsymbol{y}\| \geq|\|\boldsymbol{x}\|-\|\boldsymbol{y}\||$, for all $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n} \quad$ (inverse triangle inequality).
2. The vector norm is a continuous function $\mathcal{V} \rightarrow \mathbb{R}$.
3. All vector norms on $\mathcal{V}$ are equivalent provided $\mathcal{V}$ is finite dimensional.

Proof

1. Since $\|\boldsymbol{x}\|=\|\boldsymbol{x}-\boldsymbol{y}+\boldsymbol{y}\| \leq\|\boldsymbol{x}-\boldsymbol{y}\|+\|\boldsymbol{y}\|$ we obtain $\|\boldsymbol{x}-\boldsymbol{y}\| \geq\|\boldsymbol{x}\|-\|\boldsymbol{y}\|$. By symmetry $\|\boldsymbol{x}-\boldsymbol{y}\|=\|\boldsymbol{y}-\boldsymbol{x}\| \geq\|\boldsymbol{y}\|-\|\boldsymbol{x}\|$ and we obtain the inverse triangle inequality.
2. This follows from the inverse triangle inequality.
3. The following proof can be skipped by those who do not have the necessary background in advanced calculus. Define the $\|\cdot\|^{\prime}$ unit sphere
$$
\mathcal{S}:=\left\{\boldsymbol{y} \in \mathcal{V}:\|\boldsymbol{y}\|^{\prime}=1\right\} .
$$
The set $\mathcal{S}$ is a closed and bounded set and the function $f: \mathcal{S} \rightarrow \mathbb{R}$ given by $f(\boldsymbol{y})=\|\boldsymbol{y}\|$ is continuous by what we just showed. Therefore $f$ attains its minimum and maximum value on $\mathcal{S}$. Thus, there are positive constants $m$ and $M$ such that
$$
m \leq\|\boldsymbol{y}\| \leq M, \quad \boldsymbol{y} \in \mathcal{S} .
$$
For any $\boldsymbol{x} \in \mathcal{V}$ we have $\boldsymbol{y}:=\boldsymbol{x} /\|\boldsymbol{x}\|^{\prime} \in \mathcal{S}$, and (8.7) follows if we apply (8.8) to these $\boldsymbol{y}$. $\square$

### 8.2 Matrix Norms

For simplicity we consider only norms on the vector space $\left(\mathbb{C}^{m \times n}, \mathbb{C}\right)$. All results also holds for $\left(\mathbb{R}^{m \times n}, \mathbb{R}\right)$. A matrix norm $\left\|\|: \mathbb{C}^{m \times n}, \rightarrow \mathbb{R}\right.$ is simply a vector norm on $\mathbb{C}^{m \times n}$. Thus 1., 2. and 3. in Definition 8.1 holds, where we replace $\boldsymbol{x}$ and $\boldsymbol{y}$ by $m \times n$ matrices $\boldsymbol{A}$ and $\boldsymbol{B}$, respectively. The Frobenius norm

$$
\|\boldsymbol{A}\|_{F}:=\left(\sum_{i=1}^{m} \sum_{j=1}^{n}\left|a_{i j}\right|^{2}\right)^{1 / 2}
$$

is a matrix norm. Indeed, writing all elements in $\boldsymbol{A}$ in a string of length $m n$ we see that the Frobenius norm is the Euclidian norm on the space $\mathbb{C}^{m n}$.

Adapting Theorem 8.1 to the matrix situation gives
Theorem 8.2 (Matrix Norm Equivalence) All matrix norms on $\mathbb{C}^{m \times n}$ are equivalent. Thus, if $\|\cdot\|$ and $\|\cdot\|^{\prime}$ are two matrix norms on $\mathbb{C}^{m \times n}$ then there are positive constants $\mu$ and $M$ such that

$$
\mu\|\boldsymbol{A}\| \leq\|\boldsymbol{A}\|^{\prime} \leq M\|\boldsymbol{A}\|
$$

holds for all $\boldsymbol{A} \in \mathbb{C}^{m \times n}$. Moreover, a matrix norm is a continuous function.
Any vector norm $\|\cdot\|_{V}$ on $\mathbb{C}^{m n}$ defines a matrix norm on $\mathbb{C}^{m \times n}$ given by $\|\boldsymbol{A}\|:=$ $\|\operatorname{vec}(\boldsymbol{A})\|_{V}$, where $\operatorname{vec}(\boldsymbol{A}) \in \mathbb{C}^{m n}$ is the vector obtained by stacking the columns of $\boldsymbol{A}$ on top of each other. In particular, to the $p$ vector norms for $p=1,2, \infty$, we have the corresponding sum norm, Frobenius norm, and max norm defined by

$$
\|\boldsymbol{A}\|_{S}:=\sum_{i=1}^{m} \sum_{j=1}^{n}\left|a_{i j}\right|, \quad\|\boldsymbol{A}\|_{F}:=\left(\sum_{i=1}^{m} \sum_{j=1}^{n}\left|a_{i j}\right|^{2}\right)^{1 / 2}, \quad\|\boldsymbol{A}\|_{M}:=\max _{i, j}\left|a_{i j}\right| .
$$

Of these norms the Frobenius norm is the most useful. Some of its properties were derived in Lemma 7.1 and Theorem 7.5.

### 8.2.1 Consistent and Subordinate Matrix Norms

Since matrices can be multiplied it is useful to have an analogue of subadditivity for matrix multiplication. For square matrices the product $\boldsymbol{A} \boldsymbol{B}$ is defined in a fixed space $\mathbb{C}^{n \times n}$, while in the rectangular case matrix multiplication combines matrices in different spaces. The following definition captures this distinction.

Definition 8.4 (Consistent Matrix Norms) A matrix norm is called consistent on $\mathbb{C}^{n \times n}$ if
4. $\|\boldsymbol{A} \boldsymbol{B}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{B}\|$ (submultiplicativity) holds for all $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$. A matrix norm is consistent if it is defined on $\mathbb{C}^{m \times n}$ for all $m, n \in \mathbb{N}$, and 4 . holds for all matrices $\boldsymbol{A}, \boldsymbol{B}$ for which the product $\boldsymbol{A} \boldsymbol{B}$ is defined.

Clearly the Frobenius norm is defined for all $m, n \in \mathbb{N}$. From Lemma 7.1 it follows that the Frobenius norm is consistent.

For a consistent matrix norm on $\mathbb{C}^{n \times n}$ we have the inequality

$$
\left\|\boldsymbol{A}^{k}\right\| \leq\|\boldsymbol{A}\|^{k} \text { for } \boldsymbol{A} \in \mathbb{C}^{n \times n} \text { and } k \in \mathbb{N} \text {. }
$$

When working with norms one often has to bound the vector norm of a matrix times a vector by the norm of the matrix times the norm of the vector. This leads to the following definition.

Definition 8.5 (Subordinate Matrix Norms) Suppose $m, n \in \mathbb{N}$ are given, let $\|\|$ on $\mathbb{C}^{m}$ and $\left\|\|_{\beta}\right.$ on $\mathbb{C}^{n}$ be vector norms, and let $\| \|$ be a matrix norm on $\mathbb{C}^{m \times n}$. We say that the matrix norm $\|\|$ is subordinate to the vector norms $\| \|$ and $\left\|\|_{\beta}\right.$ if $\|\boldsymbol{A} \boldsymbol{x}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{x}\|_{\beta}$ for all $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ and all $\boldsymbol{x} \in \mathbb{C}^{n}$.

By Lemma 7.1 we have $\|\boldsymbol{A} \boldsymbol{x}\|_{2} \leq\|\boldsymbol{A}\|_{F}\|\boldsymbol{x}\|_{2}$, for all $\boldsymbol{x} \in \mathbb{C}^{n}$. Thus the Frobenius norm is subordinate to the Euclidian vector norm.

For consistent matrix norms we have
Proposition 8.1 For $m, n \in \mathbb{N}, \boldsymbol{A} \in \mathbb{C}^{m \times n}$, all $\boldsymbol{x} \in \mathbb{C}^{n}$ and any consistent matrix norm $\|\|$

$$
\|\boldsymbol{A} \boldsymbol{x}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{x}\|,
$$

i.e., a consistent matrix norm is subordinate to itself. Moreover, the matrix power bound (8.10) holds for all square matrices $\boldsymbol{A} \in \mathbb{C}^{n \times n}$.

Proof Since a consistent matrix norm is defined on $\mathbb{C}^{m \times n}$ for all $m, n \in \mathbb{N}$ the consistency implies that (8.11) holds for $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ and $\boldsymbol{B}:=\boldsymbol{x} \in \mathbb{C}^{n \times 1}$. The last statement also follows immediately from the consistency. $\square$

### 8.2.2 Operator Norms

Corresponding to vector norms on $\mathbb{C}^{n}$ and $\mathbb{C}^{m}$ there is an induced matrix norm on $\mathbb{C}^{m \times n}$ which we call the operator norm. It is possible to consider one vector norm
on $\mathbb{C}^{m}$ and another vector norm on $\mathbb{C}^{n}$, but we treat only the case of one vector norm defined on $\mathbb{C}^{n}$ for all $n \in \mathbb{N} .^{1}$

Definition 8.6 (Operator Norm) Let $\left\|\|\right.$ be a vector norm defined on $\mathbb{C}^{n}$ for all $n \in \mathbb{N}$. For given $m, n \in \mathbb{N}$ and $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ we define

$$
\|\boldsymbol{A}\|:=\max _{\boldsymbol{x} \neq 0} \frac{\|\boldsymbol{A} \boldsymbol{x}\|}{\|\boldsymbol{x}\|} .
$$

We call this the operator norm corresponding to the vector norm $\|\|$.
With a risk of confusion we use the same symbol for the operator norm and the corresponding vector norm. Before we show that the operator norm is a matrix norm we make some observations.

1. It is enough to take the max over subsets of $\mathbb{C}^{n}$. For example
$$
\|\boldsymbol{A}\|=\max _{\|\boldsymbol{x}\|=1}\|\boldsymbol{A} \boldsymbol{x}\| .
$$
The set
$$
\mathcal{S}:=\left\{x \in \mathbb{C}^{n}:\|\boldsymbol{x}\|=1\right\}
$$
is the unit sphere in $\mathbb{C}^{n}$ with respect to the vector norm $\|\|$. It is enough to take the max over this unit sphere since
$$
\max _{\boldsymbol{x} \neq 0} \frac{\|\boldsymbol{A} \boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\max _{\boldsymbol{x} \neq 0}\left\|\boldsymbol{A}\left(\frac{\boldsymbol{x}}{\|\boldsymbol{x}\|}\right)\right\|=\max _{\|\boldsymbol{y}\|=1}\|\boldsymbol{A} \boldsymbol{y}\| .
$$
2. The operator norm is subordinate to the corresponding vector norm. Thus,
$$
\|\boldsymbol{A} \boldsymbol{x}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{x}\| \text { for all } \boldsymbol{A} \in \mathbb{C}^{m \times n} \text { and } \boldsymbol{x} \in \mathbb{C}^{n} .
$$
3. We can use max instead of sup in (8.12). This follows by the following compactness argument. The unit sphere $\mathcal{S}$ given by (8.14) is bounded. It is also finite dimensional and closed, and hence compact. Moreover, since the vector norm $\|\|: \mathcal{S} \rightarrow \mathbb{R}$ is a continuous function, it follows that the function $f: \mathcal{S} \rightarrow \mathbb{R}$ given by $f(\boldsymbol{x})=\|\boldsymbol{A} \boldsymbol{x}\|$ is continuous. But then $f$ attains its max and min and we have
$$
\|\boldsymbol{A}\|=\left\|\boldsymbol{A} \boldsymbol{x}^{*}\right\| \text { for some } \boldsymbol{x}^{*} \in \mathcal{S} .
$$
[^16]Lemma 8.1 (The Operator Norm Is a Consistent Matrix Norm) If || || is vector norm defined on $\mathbb{C}^{n}$ for all $n \in \mathbb{N}$, then the operator norm given by (8.12) is a consistent matrix norm. Moreover, $\|\boldsymbol{I}\|=1$.

Proof We use (8.13). In 2. and 3. below we take the max over the unit sphere $\mathcal{S}$ given by (8.14).

1. Nonnegativity is obvious. If $\|\boldsymbol{A}\|=0$ then $\|\boldsymbol{A} \boldsymbol{y}\|=0$ for each $\boldsymbol{y} \in \mathbb{C}^{n}$. In particular, each column $\boldsymbol{A} \boldsymbol{e}_{j}$ in $\boldsymbol{A}$ is zero. Hence $\boldsymbol{A}=0$.
2. $\|c \boldsymbol{A}\|=\max _{\boldsymbol{x}}\|c \boldsymbol{A} \boldsymbol{x}\|=\max _{\boldsymbol{x}}|c|\|\boldsymbol{A} \boldsymbol{x}\|=|c|\|\boldsymbol{A}\|$.
3. $\|\boldsymbol{A}+\boldsymbol{B}\|=\max _{\boldsymbol{x}}\|(\boldsymbol{A}+\boldsymbol{B}) \boldsymbol{x}\| \leq \max _{\boldsymbol{x}}\|\boldsymbol{A} \boldsymbol{x}\|+\max _{\boldsymbol{x}}\|\boldsymbol{B} \boldsymbol{x}\|=\|\boldsymbol{A}\|+\|\boldsymbol{B}\|$.
4. $$
\begin{aligned}
& \|\boldsymbol{A} \boldsymbol{B}\|=\max _{\boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{A} \boldsymbol{B} \boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\max _{\boldsymbol{B} \boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{A} \boldsymbol{B} \boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\max _{\boldsymbol{B} \boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{A} \boldsymbol{B} \boldsymbol{x}\|}{\|\boldsymbol{B} \boldsymbol{x}\|} \frac{\|\boldsymbol{B} \boldsymbol{x}\|}{\|\boldsymbol{x}\|} \\
& \quad \leq \max _{\boldsymbol{y} \neq \mathbf{0}} \frac{\|\boldsymbol{A} \boldsymbol{y}\|}{\|\boldsymbol{y}\|} \max _{\boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{B} \boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\|\boldsymbol{A}\|\|\boldsymbol{B}\|
\end{aligned}
$$
That $\|\boldsymbol{I}\|=1$ for any operator norm follows immediately from the definition. $\square$

Since $\|\boldsymbol{I}\|_{F}=\sqrt{n}$, we see that the Frobenius norm is not an operator norm for $n>1$.

### 8.2.3 The Operator $\boldsymbol{p}$-Norms

Recall that the $p$ or $\ell_{p}$ vector norms (8.1) are given by

$$
\|x\|_{p}:=\left(\sum_{j=1}^{n}\left|x_{j}\right|^{p}\right)^{1 / p}, p \geq 1, \quad\|x\|_{\infty}:=\max _{1 \leq j \leq n}\left|x_{j}\right| .
$$

The operator norms $\left\|\|_{p}\right.$ defined from these $p$-vector norms are used quite frequently for $p=1,2, \infty$. We define for any $1 \leq p \leq \infty$

$$
\|\boldsymbol{A}\|_{p}:=\max _{\boldsymbol{x} \neq 0} \frac{\|\boldsymbol{A} \boldsymbol{x}\|_{p}}{\|\boldsymbol{x}\|_{p}}=\max _{\|\boldsymbol{y}\|_{p}=1}\|\boldsymbol{A} \boldsymbol{y}\|_{p} .
$$

For $p=1,2, \infty$ we have explicit expressions for these norms.
Theorem 8.3 (One-Two-Inf-Norms) For $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ we have

$$
\begin{aligned}
& \|\boldsymbol{A}\|_{1}:=\max _{1 \leq j \leq n}\left\|\boldsymbol{A} \boldsymbol{e}_{j}\right\|_{1}=\max _{1 \leq j \leq n} \sum_{k=1}^{m}\left|a_{k, j}\right|, \quad \text { (max column sum) } \\
& \|\boldsymbol{A}\|_{2}:=\sigma_{1}, \quad \text { (largest singular value of } \boldsymbol{A} \text { ) } \\
& \|\boldsymbol{A}\|_{\infty}=\max _{1 \leq k \leq m}\left\|\boldsymbol{e}_{k}^{T} \boldsymbol{A}\right\|_{1}=\max _{1 \leq k \leq m} \sum_{j=1}^{n}\left|a_{k, j}\right| . \quad \text { (max row sum) }
\end{aligned}
$$

The two-norm $\|\boldsymbol{A}\|_{2}$ is also called the spectral norm of $\boldsymbol{A}$.
Proof We proceed as follows:

(a) We derive a constant $K_{p}$ such that $\|\boldsymbol{A} \boldsymbol{x}\|_{p} \leq K_{p}$ for any $\boldsymbol{x} \in \mathbb{C}^{n}$ with $\|\boldsymbol{x}\|_{p}=1$.
(b) We give an extremal vector $\boldsymbol{y}_{e} \in \mathbb{C}^{n}$ with $\left\|\boldsymbol{y}_{e}\right\|_{p}=1$ so that $\left\|\boldsymbol{A} \boldsymbol{y}_{e}\right\|_{p}=K_{p}$.

It then follows from (8.17) that $\|\boldsymbol{A}\|_{p}=\left\|\boldsymbol{A} \boldsymbol{y}_{e}\right\|_{p}=K_{p}$.
2-norm: Let $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}$ be a singular value decomposition of $\boldsymbol{A}$, define $K_{2}=$ $\sigma_{1}, \boldsymbol{c}:=\boldsymbol{V}^{*} \boldsymbol{x}$, and $\boldsymbol{y}_{e}=\boldsymbol{v}_{1}$ the singular vector corresponding to $\sigma_{1}$. Then $\boldsymbol{x}=$ $\boldsymbol{V} \boldsymbol{c},\|\boldsymbol{c}\|_{2}=\|\boldsymbol{x}\|_{2}=1$, and using (7.7) in (b) we find

(a) $\|\boldsymbol{A} \boldsymbol{x}\|_{2}^{2}=\left\|\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*} \boldsymbol{x}\right\|_{2}^{2}=\|\boldsymbol{\Sigma} \boldsymbol{c}\|_{2}^{2}=\sum_{j=1}^{n} \sigma_{j}^{2}\left|c_{j}\right|^{2} \leq \sigma_{1}^{2} \sum_{j=1}^{n}\left|c_{j}\right|^{2}=\sigma_{1}^{2}$.
(b) $\left\|\boldsymbol{A} \boldsymbol{v}_{1}\right\|_{2}=\left\|\sigma_{1} \boldsymbol{u}_{1}\right\|_{2}=\sigma_{1}$.

1-norm: Define $K_{1}, c$ and $\boldsymbol{y}_{e}$ by $K_{1}:=\left\|\boldsymbol{A} \boldsymbol{e}_{c}\right\|_{1}=\max _{1 \leq j \leq n}\left\|\boldsymbol{A} \boldsymbol{e}_{j}\right\|_{1}$ and $\boldsymbol{y}_{e}:=$ $\boldsymbol{e}_{c}$, a unit vector. Then $\left\|\boldsymbol{y}_{e}\right\|_{1}=1$ and we obtain

(a) $$
\|\boldsymbol{A} \boldsymbol{x}\|_{1}=\sum_{k=1}^{m}\left|\sum_{j=1}^{n} a_{k j} x_{j}\right| \leq \sum_{k=1}^{m} \sum_{j=1}^{n}\left|a_{k j}\right|\left|x_{j}\right|=\sum_{j=1}^{n}\left(\sum_{k=1}^{m}\left|a_{k j}\right|\right)\left|x_{j}\right| \leq K_{1} .
$$
(b) $\left\|\boldsymbol{A} \boldsymbol{y}_{e}\right\|_{1}=K_{1}$.

$\infty$-norm: Define $K_{\infty}, r$ and $\boldsymbol{y}_{e}$ by $K_{\infty}:=\left\|\boldsymbol{e}_{r}^{T} \boldsymbol{A}\right\|_{1}=\max _{1 \leq k \leq m}\left\|\boldsymbol{e}_{k}^{T} \boldsymbol{A}\right\|_{1}$ and $\boldsymbol{y}_{e}:=\left[e^{-i \theta_{1}}, \ldots, e^{-i \theta_{n}}\right]^{T}$, where $a_{r j}=\left|a_{r j}\right| e^{i \theta_{j}}$ for $j=1, \ldots, n$.

(a) $$
\|\boldsymbol{A} \boldsymbol{x}\|_{\infty}=\max _{1 \leq k \leq m}\left|\sum_{j=1}^{n} a_{k j} x_{j}\right| \leq \max _{1 \leq k \leq m} \sum_{j=1}^{n}\left|a_{k j}\right|\left|x_{j}\right| \leq K_{\infty} .
$$
(b) $\left\|\boldsymbol{A} \boldsymbol{y}^{*}\right\|_{\infty}=\max _{1 \leq k \leq m}\left|\sum_{j=1}^{n} a_{k j} e^{-i \theta_{j}}\right|=K_{\infty}$.

The last equality is correct because $\left|\sum_{j=1}^{n} a_{k j} e^{-i \theta_{j}}\right| \leq \sum_{j=1}^{n}\left|a_{k j}\right| \leq K_{\infty}$ with equality for $k=r$. $\square$

Example 8.1 (Comparing One-Two-Inf-Norms) The largest singular value of the matrix $\boldsymbol{A}:=\frac{1}{15}\left[\begin{array}{ccc}14 & 4 & 16 \\ 2 & 22 & 13\end{array}\right]$, is $\sigma_{1}=2$ (cf. Example 7.9). We find

$$
\|\boldsymbol{A}\|_{1}=\frac{29}{15}, \quad\|\boldsymbol{A}\|_{2}=2, \quad\|\boldsymbol{A}\|_{\infty}=\frac{37}{15}, \quad\|\boldsymbol{A}\|_{F}=\sqrt{5} .
$$

The values of these norms do not differ by much.
In some cases the spectral norm is equal to an eigenvalue of the matrix.

Theorem 8.4 (Spectral Norm) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has singular values $\sigma_{1} \geq \sigma_{2} \geq$ $\cdots \geq \sigma_{n}$ and eigenvalues $\left|\lambda_{1}\right| \geq\left|\lambda_{2}\right| \geq \cdots \geq\left|\lambda_{n}\right|$. Then

$$
\begin{aligned}
& \|\boldsymbol{A}\|_{2}=\sigma_{1} \text { and }\left\|\boldsymbol{A}^{-1}\right\|_{2}=\frac{1}{\sigma_{n}} \\
& \|\boldsymbol{A}\|_{2}=\lambda_{1} \text { and }\left\|\boldsymbol{A}^{-1}\right\|_{2}=\frac{1}{\lambda_{n}}, \text { if } \boldsymbol{A} \text { is positive definite, } \\
& \|\boldsymbol{A}\|_{2}=\left|\lambda_{1}\right| \text { and }\left\|\boldsymbol{A}^{-1}\right\|_{2}=\frac{1}{\left|\lambda_{n}\right|}, \text { if } \boldsymbol{A} \text { is normal. }
\end{aligned}
$$

For the norms of $\boldsymbol{A}^{-1}$ we assume that $\boldsymbol{A}$ is nonsingular.
Proof Since $1 / \sigma_{n}$ is the largest singular value of $\boldsymbol{A}^{-1}$, (8.19) follows. By Exercise 7.5 the singular values of a positive definite matrix (normal matrix) are equal to the eigenvalues (absolute value of the eigenvalues). This implies (8.20) and (8.21). $\square$

The following result is sometimes useful.
Theorem 8.5 (Spectral Norm Bound) For any $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ we have $\|\boldsymbol{A}\|_{2}^{2} \leq$ $\|\boldsymbol{A}\|_{1}\|\boldsymbol{A}\|_{\infty}$.

Proof Let $\left(\sigma^{2}, \boldsymbol{v}\right)$ be an eigenpair for $\boldsymbol{A}^{*} \boldsymbol{A}$ corresponding to the largest singular value $\sigma$ of $\boldsymbol{A}$. Then

$$
\|\boldsymbol{A}\|_{2}^{2}\|\boldsymbol{v}\|_{1}=\sigma^{2}\|\boldsymbol{v}\|_{1}=\left\|\sigma^{2} \boldsymbol{v}\right\|_{1}=\left\|\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{v}\right\|_{1} \leq\left\|\boldsymbol{A}^{*}\right\|_{1}\|\boldsymbol{A}\|_{1}\|\boldsymbol{v}\|_{1} .
$$

Observing that $\left\|\boldsymbol{A}^{*}\right\|_{1}=\|\boldsymbol{A}\|_{\infty}$ by Theorem 8.3 and canceling $\|\boldsymbol{v}\|_{1}$ proves the result. $\square$

### 8.2.4 Unitary Invariant Matrix Norms

Definition 8.7 (Unitary Invariant Norm) A matrix norm $\left\|\|\right.$ on $\mathbb{C}^{m \times n}$ is called unitary invariant if $\|\boldsymbol{U} \boldsymbol{A} \boldsymbol{V}\|=\|\boldsymbol{A}\|$ for any $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ and any unitary matrices $\boldsymbol{U} \in \mathbb{C}^{m \times m}$ and $\boldsymbol{V} \in \mathbb{C}^{n \times n}$.

When a unitary invariant matrix norm is used, the size of a perturbation is not increased by a unitary transformation. Thus if $\boldsymbol{U}$ and $\boldsymbol{V}$ are unitary then $\boldsymbol{U}(\boldsymbol{A}+$ $\boldsymbol{E}) \boldsymbol{V}=\boldsymbol{U} \boldsymbol{A} \boldsymbol{V}+\boldsymbol{F}$, where $\|\boldsymbol{F}\|=\|\boldsymbol{E}\|$.

It follows from Lemma 7.1 that the Frobenius norm is unitary invariant. We show here that this also holds for the spectral norm.

Theorem 8.6 (Unitary Invariant Norms) The Frobenius norm and the spectral norm are unitary invariant. Moreover,

$$
\left\|\boldsymbol{A}^{*}\right\|_{F}=\|\boldsymbol{A}\|_{F} \text { and }\left\|\boldsymbol{A}^{*}\right\|_{2}=\|\boldsymbol{A}\|_{2} .
$$

Proof The results for the Frobenius norm follow from Lemma 7.1. Suppose $\boldsymbol{A} \in$ $\mathbb{C}^{m \times n}$ and let $\boldsymbol{U} \in \mathbb{C}^{m \times m}$ and $\boldsymbol{V} \in \mathbb{C}^{n \times n}$ be unitary. Since the 2-vector norm is unitary invariant we obtain

$$
\|\boldsymbol{U} \boldsymbol{A}\|_{2}=\max _{\|\boldsymbol{x}\|_{2}=1}\|\boldsymbol{U} \boldsymbol{A} \boldsymbol{x}\|_{2}=\max _{\|\boldsymbol{x}\|_{2}=1}\|\boldsymbol{A} \boldsymbol{x}\|_{2}=\|\boldsymbol{A}\|_{2} .
$$

Now $\boldsymbol{A}$ and $\boldsymbol{A}^{*}$ have the same nonzero singular values, and it follows from Theorem 8.3 that $\left\|\boldsymbol{A}^{*}\right\|_{2}=\|\boldsymbol{A}\|_{2}$. Moreover $\boldsymbol{V}^{*}$ is unitary. Using these facts we find

$$
\|\boldsymbol{A} \boldsymbol{V}\|_{2}=\left\|(\boldsymbol{A} \boldsymbol{V})^{*}\right\|_{2}=\left\|\boldsymbol{V}^{*} \boldsymbol{A}^{*}\right\|_{2}=\left\|\boldsymbol{A}^{*}\right\|_{2}=\|\boldsymbol{A}\|_{2} .
$$ $\square$

It can be shown that the spectral norm is the only unitary invariant operator norm, see [10] p. 357.

### 8.2.5 Absolute and Monotone Norms

A vector norm on $\mathbb{C}^{n}$ is an absolute norm if $\|\boldsymbol{x}\|=\||\boldsymbol{x}|\|$ for all $\boldsymbol{x} \in \mathbb{C}^{n}$. Here $|\boldsymbol{x}|:=\left[\left|x_{1}\right|, \ldots,\left|x_{n}\right|\right]^{T}$, the absolute values of the components of $\boldsymbol{x}$. Clearly the vector $p$ norms are absolute norms. We state without proof (see Theorem 5.5.10 of [10]) that a vector norm on $\mathbb{C}^{n}$ is an absolute norm if and only if it is a monotone norm, i.e.,

$$
\left|x_{i}\right| \leq\left|y_{i}\right|, i=1, \ldots, n \Longrightarrow\|\boldsymbol{x}\| \leq\|\boldsymbol{y}\| \text {, for all } \boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n} .
$$

Absolute and monotone matrix norms are defined as for vector norms.
The study of matrix norms will be continued in Chap. 12.

### 8.3 The Condition Number with Respect to Inversion

Consider the system of two linear equations

$$
\begin{aligned}
& x_{1}+\left(1-10^{-16}\right) x_{2}=20 \\
& x_{1}+\left(1-10^{-15}\right.
\end{aligned}
$$

whose exact solution is $x_{1}=x_{2}=10$. If we replace the second equation by

$$
x_{1}+\left(1+10^{-16}\right) x_{2}=20-10^{-15},
$$

the exact solution changes to $x_{1}=30, x_{2}=-10$. Here a small change in one of the coefficients, from $1-10^{-16}$ to $1+10^{-16}$, changed the exact solution by a large amount.

A mathematical problem in which the solution is very sensitive to changes in the data is called ill-conditioned. Such problems can be difficult to solve on a computer.

In this section we consider what effect a small change (perturbation) in the data $\boldsymbol{A}, \boldsymbol{b}$ has on the inverse of $\boldsymbol{A}$ and on the solution $\boldsymbol{x}$ of a linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. To measure this we use vector and matrix norms. In this section $\|\|$ will denote a vector norm on $\mathbb{C}^{n}$ and also a matrix norm on $\mathbb{C}^{n \times n}$. We assume that the matrix norm is consistent on $\mathbb{C}^{n \times n}$ and subordinate to the vector norm. Thus, for any $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$ and any $\boldsymbol{x} \in \mathbb{C}^{n}$ we have

$$
\|\boldsymbol{A} \boldsymbol{B}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{B}\| \text { and }\|\boldsymbol{A} \boldsymbol{x}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{x}\| .
$$

Recall that this holds if the matrix norm is the operator norm corresponding to the given vector norm. It also holds for the Frobenius matrix norm and the Euclidian vector norm. This follows from Lemma 7.1. We recall that if $\boldsymbol{I} \in \mathbb{R}^{n \times n}$ then $\|\boldsymbol{I}\|=1$ for an operator norm, while $\|\boldsymbol{I}\|_{F}=\sqrt{n}$.

### 8.3.1 Perturbation of the Right Hand Side in a Linear Systems

Suppose $\boldsymbol{x}, \boldsymbol{y}$ solve $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ and $(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{y}=\boldsymbol{b}+\boldsymbol{e}$, respectively. where $\boldsymbol{A}, \boldsymbol{A}+\boldsymbol{E} \in$ $\mathbb{C}^{n \times n}$ are nonsingular and $\boldsymbol{b}, \boldsymbol{e} \in \mathbb{C}^{n}$. How large can $\boldsymbol{y}-\boldsymbol{x}$ be? The difference $\|\boldsymbol{y}-\boldsymbol{x}\|$ measures the absolute error in $\boldsymbol{y}$ as an approximation to $\boldsymbol{x}$, while $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{x}\|$ and $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{y}\|$ are measures for the relative error.

We consider first the simpler case of a perturbation in the right-hand side $\boldsymbol{b}$.
Theorem 8.7 (Perturbation in the Right-Hand Side) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular, $\boldsymbol{b}, \boldsymbol{e} \in \mathbb{C}^{n}, \boldsymbol{b} \neq \mathbf{0}$ and $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}, \boldsymbol{A} \boldsymbol{y}=\boldsymbol{b}+\boldsymbol{e}$. Then

$$
\frac{1}{K(\boldsymbol{A})} \frac{\|\boldsymbol{e}\|}{\|\boldsymbol{b}\|} \leq \frac{\|\boldsymbol{y}-\boldsymbol{x}\|}{\|\boldsymbol{x}\|} \leq K(\boldsymbol{A}) \frac{\|\boldsymbol{e}\|}{\|\boldsymbol{b}\|},
$$

where $K(\boldsymbol{A})=\|\boldsymbol{A}\|\left\|\boldsymbol{A}^{-1}\right\|$ is the condition number of $\boldsymbol{A}$.
Proof Subtracting $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ from $\boldsymbol{A} \boldsymbol{y}=\boldsymbol{b}+\boldsymbol{e}$ we have $\boldsymbol{A}(\boldsymbol{y}-\boldsymbol{x})=\boldsymbol{e}$ or $\boldsymbol{y}-\boldsymbol{x}=\boldsymbol{A}^{-1} \boldsymbol{e}$. Combining $\|\boldsymbol{y}-\boldsymbol{x}\|=\left\|\boldsymbol{A}^{-1} \boldsymbol{e}\right\| \leq\left\|\boldsymbol{A}^{-1}\right\|\|\boldsymbol{e}\|$ and $\|\boldsymbol{b}\|=\|\boldsymbol{A} \boldsymbol{x}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{x}\|$ we obtain the upper bound in (8.22). Combining $\|\boldsymbol{e}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{y}-\boldsymbol{x}\|$ and $\|\boldsymbol{x}\| \leq$ $\left\|\boldsymbol{A}^{-1}\right\|\|\boldsymbol{b}\|$ we obtain the lower bound. $\square$

Consider (8.22). $\|\boldsymbol{e}\| /\|\boldsymbol{b}\|$ is a measure of the size of the perturbation $\boldsymbol{e}$ relative to the size of $\boldsymbol{b}$. The upper bound says that $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{x}\|$ in the worst case can be $K(\boldsymbol{A})$ times as large as $\|\boldsymbol{e}\| /\|\boldsymbol{b}\|$.

The bounds in (8.22) depends on $K(\boldsymbol{A})$. This number is called the condition number with respect to inversion of a matrix, or just the condition number of $\boldsymbol{A}$, if it is clear from the context that we are talking about inverting a matrix. The condition number depends on the matrix $\boldsymbol{A}$ and on the norm used. If $K(\boldsymbol{A})$ is large, $\boldsymbol{A}$ is called ill-conditioned (with respect to inversion). If $K(\boldsymbol{A})$ is small, $\boldsymbol{A}$ is called well-conditioned (with respect to inversion). We always have $K(\boldsymbol{A}) \geq 1$. For since $\|\boldsymbol{x}\|=\|\boldsymbol{I} \boldsymbol{x}\| \leq\|\boldsymbol{I}\|\|\boldsymbol{x}\|$ for any $\boldsymbol{x}$ we have $\|\boldsymbol{I}\| \geq 1$ and therefore $\|\boldsymbol{A}\|\left\|\boldsymbol{A}^{-1}\right\| \geq$ $\left\|\boldsymbol{A} \boldsymbol{A}^{-1}\right\|=\|\boldsymbol{I}\| \geq 1$.

Since all matrix norms are equivalent, the dependence of $K(\boldsymbol{A})$ on the norm chosen is less important than the dependence on $\boldsymbol{A}$. Example 8.1 provided an illustration of this. See also Exercise 8.19. Sometimes one chooses the spectral norm when discussing properties of the condition number, and the $\ell_{1}, \ell_{\infty}$, or Frobenius norm when one wishes to compute it or estimate it.

Suppose we have computed an approximate solution $\boldsymbol{y}$ to $\boldsymbol{A x}=\boldsymbol{b}$. The vector $\boldsymbol{r}(\boldsymbol{y}):=\boldsymbol{A} \boldsymbol{y}-\boldsymbol{b}$ is called the residual vector, or just the residual. We can bound $\boldsymbol{x}-\boldsymbol{y}$ in terms of $\boldsymbol{r}$.

Theorem 8.8 (Perturbation and Residual) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}, \boldsymbol{b} \in \mathbb{C}^{n}$, $\boldsymbol{A}$ is nonsingular and $\boldsymbol{b} \neq \mathbf{0}$. Let $\boldsymbol{r}(\boldsymbol{y})=\boldsymbol{A} \boldsymbol{y}-\boldsymbol{b}$ for $\boldsymbol{y} \in \mathbb{C}^{n}$. If $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ then

$$
\frac{1}{K(\boldsymbol{A})} \frac{\|\boldsymbol{r}(\boldsymbol{y})\|}{\|\boldsymbol{b}\|} \leq \frac{\|\boldsymbol{y}-\boldsymbol{x}\|}{\|\boldsymbol{x}\|} \leq K(\boldsymbol{A}) \frac{\|\boldsymbol{r}(\boldsymbol{y})\|}{\|\boldsymbol{b}\|} .
$$

Proof We simply take $\boldsymbol{e}=\boldsymbol{r}(\boldsymbol{y})$ in Theorem 8.7. $\square$

Consider next a perturbation in the coefficient matrix in a linear system. Suppose $\boldsymbol{A}, \boldsymbol{E} \in \mathbb{C}^{n \times n}$ with $\boldsymbol{A}, \boldsymbol{A}+\boldsymbol{E}$ nonsingular. We like to compare the solution $\boldsymbol{x}$ and $\boldsymbol{y}$ of the systems $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ and $(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{y}=\boldsymbol{b}$.

Theorem 8.9 (Perturbation in Matrix) Suppose $\boldsymbol{A}, \boldsymbol{E} \in \mathbb{C}^{n \times n}, \boldsymbol{b} \in \mathbb{C}^{n}$ with $\boldsymbol{A}$ nonsingular and $\boldsymbol{b} \neq \mathbf{0}$. If $r:=\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\|<1$ then $\boldsymbol{A}+\boldsymbol{E}$ is nonsingular. If $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ and $(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{y}=\boldsymbol{b}$ then

$$
\begin{aligned}
& \frac{\|\boldsymbol{y}-\boldsymbol{x}\|}{\|\boldsymbol{y}\|} \leq r \leq K(\boldsymbol{A}) \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|}, \\
& \frac{\|\boldsymbol{y}-\boldsymbol{x}\|}{\|\boldsymbol{x}\|} \leq \frac{r}{1-r} \leq \frac{K(\boldsymbol{A})}{1-r} \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|} .
\end{aligned}
$$

Proof We show $\boldsymbol{A}+\boldsymbol{E}$ singular implies $r \geq 1$. Suppose $\boldsymbol{A}+\boldsymbol{E}$ is singular. Then $(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{x}=\mathbf{0}$ for some nonzero $\boldsymbol{x} \in \mathbb{C}^{n}$. Multiplying by $\boldsymbol{A}^{-1}$ it follows that $\left(\boldsymbol{I}+\boldsymbol{A}^{-1} \boldsymbol{E}\right) \boldsymbol{x}=\mathbf{0}$ and this implies that $\|\boldsymbol{x}\|=\left\|\boldsymbol{A}^{-1} \boldsymbol{E} \boldsymbol{x}\right\| \leq r\|\boldsymbol{x}\|$. But then $r \geq 1$.

Subtracting $(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{y}=\boldsymbol{b}$ from $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ gives $\boldsymbol{A}(\boldsymbol{x}-\boldsymbol{y})=\boldsymbol{E} \boldsymbol{y}$ or $\boldsymbol{x}-\boldsymbol{y}=\boldsymbol{A}^{-1} \boldsymbol{E} \boldsymbol{y}$. Taking norms and dividing by $\|\boldsymbol{y}\|$ proves (8.24). Solving
$\boldsymbol{x}-\boldsymbol{y}=\boldsymbol{A}^{-1} \boldsymbol{E} \boldsymbol{y}$ for $\boldsymbol{y}$ we obtain $\boldsymbol{y}=\left(\boldsymbol{I}+\boldsymbol{A}^{-1} \boldsymbol{E}\right)^{-1} \boldsymbol{x}$. By Theorem 12.14 we have $\|\boldsymbol{y}\| \leq\left\|\left(\boldsymbol{I}+\boldsymbol{A}^{-1} \boldsymbol{E}\right)^{-1}\right\|\|\boldsymbol{x}\| \leq \frac{\|\boldsymbol{x}\|}{1-r}$ and (8.24) implies $\|\boldsymbol{y}-\boldsymbol{x}\| \leq r\|\boldsymbol{y}\| \leq$ $\frac{r}{1-r}\|\boldsymbol{x}\| \leq \frac{K(\boldsymbol{A})}{1-r}\|\boldsymbol{E}\|\|\boldsymbol{A}\|$. Dividing by $\|\boldsymbol{x}\|$ gives (8.25). $\square$

In Theorem 8.9 we gave bounds for the relative error in $\boldsymbol{x}$ as an approximation to $\boldsymbol{y}$ and the relative error in $\boldsymbol{y}$ as an approximation to $\boldsymbol{x} .\|\boldsymbol{E}\| /\|\boldsymbol{A}\|$ is a measure for the size of the perturbation $\boldsymbol{E}$ in $\boldsymbol{A}$ relative to the size of $\boldsymbol{A}$. The condition number again plays a crucial role. $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{y}\|$ can be as large as $K(\boldsymbol{A})$ times $\|\boldsymbol{E}\| /\|\boldsymbol{A}\|$. It can be shown that the upper bound can be attained for any $\boldsymbol{A}$ and any $\boldsymbol{b}$. In deriving the upper bound we used the inequality $\left\|\boldsymbol{A}^{-1} \boldsymbol{E} \boldsymbol{y}\right\| \leq\left\|\boldsymbol{A}^{-1}\right\|\|\boldsymbol{E}\|\|\boldsymbol{y}\|$. For a more or less random perturbation $\boldsymbol{E}$ this is not a severe overestimate for $\left\|\boldsymbol{A}^{-1} \boldsymbol{E} \boldsymbol{y}\right\|$. In the situation where $\boldsymbol{E}$ is due to round-off errors (8.24) can give a fairly realistic estimate for $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{y}\|$.

The following explicit expressions for the 2-norm condition number follow from Theorem 8.4.

Theorem 8.10 (Spectral Condition Number) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular with singular values $\sigma_{1} \geq \sigma_{2} \geq \cdots \geq \sigma_{n}>0$ and eigenvalues $\left|\lambda_{1}\right| \geq\left|\lambda_{2}\right| \geq \cdots \geq$ $\left|\lambda_{n}\right|>0$. Then

$$
K_{2}(\boldsymbol{A})= \begin{cases}\lambda_{1} / \lambda_{n}, & \text { if } \boldsymbol{A} \text { is positive definite, } \\ \left|\lambda_{1}\right| /\left|\lambda_{n}\right|, & \text { if } \boldsymbol{A} \text { is normal, } \\ \sigma_{1} / \sigma_{n}, & \text { in general. }\end{cases}
$$

It follows that $\boldsymbol{A}$ is ill-conditioned with respect to inversion if and only if $\sigma_{1} / \sigma_{n}$ is large, or $\lambda_{1} / \lambda_{n}$ is large when $\boldsymbol{A}$ is positive definite.

If $\boldsymbol{A}$ is well-conditioned, (8.23) says that $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{x}\| \approx\|\boldsymbol{r}(\boldsymbol{y})\| /\|\boldsymbol{b}\|$. In other words, the accuracy in $\boldsymbol{y}$ is about the same order of magnitude as the residual as long as $\|\boldsymbol{b}\| \approx 1$. If $\boldsymbol{A}$ is ill-conditioned, anything can happen. We can for example have an accurate solution even if the residual is large.

### 8.3.2 Perturbation of a Square Matrix

Suppose $\boldsymbol{A}$ is nonsingular and $\boldsymbol{E}$ a perturbation of $\boldsymbol{A}$. We expect $\boldsymbol{B}:=\boldsymbol{A}+\boldsymbol{E}$ to be nonsingular when $\boldsymbol{E}$ is small relative to $\boldsymbol{A}$. But how small is small? It is also useful to have bounds on $\left\|\boldsymbol{B}^{-1}\right\|$ in terms of $\left\|\boldsymbol{A}^{-1}\right\|$ and the difference $\left\|\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right\|$. We consider the relative errors $\left\|\boldsymbol{B}^{-1}\right\| /\left\|\boldsymbol{A}^{-1}\right\|,\left\|\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right\| /\left\|\boldsymbol{B}^{-1}\right\|$ and $\| \boldsymbol{B}^{-1}-$ $\boldsymbol{A}^{-1}\|/\| \boldsymbol{A}^{-1} \|$.

Theorem 8.11 (Perturbation of Inverse Matrix) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular and let $\boldsymbol{B}:=\boldsymbol{A}+\boldsymbol{E} \in \mathbb{C}^{n \times n}$ be nonsingular. For any consistent matrix norm $\|\|$ we have

$$
\frac{\left\|\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right\|}{\left\|\boldsymbol{B}^{-1}\right\|} \leq\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\| \leq K(\boldsymbol{A}) \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|},
$$

where $K(\boldsymbol{A}):=\|\boldsymbol{A}\|\left\|\boldsymbol{A}^{-1}\right\|$. If $r:=\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\|<1$ then $\boldsymbol{B}$ is nonsingular and

$$
\frac{1}{1+r} \leq \frac{\left\|\boldsymbol{B}^{-1}\right\|}{\left\|\boldsymbol{A}^{-1}\right\|} \leq \frac{1}{1-r} .
$$

We also have

$$
\frac{\left\|\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right\|}{\left\|\boldsymbol{A}^{-1}\right\|} \leq \frac{r}{1-r} \leq \frac{K(\boldsymbol{A})}{1-r} \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|} .
$$

We can replace $\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\|$ by $\left\|\boldsymbol{E} \boldsymbol{A}^{-1}\right\|$ everywhere.
Proof That $\boldsymbol{B}$ is nonsingular if $r<1$ follows from Theorem 8.9. We have $-\boldsymbol{E}=$ $\boldsymbol{A}-\boldsymbol{B}=\boldsymbol{A}\left(\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right) \boldsymbol{B}=\boldsymbol{B}\left(\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right) \boldsymbol{A}$ so that

$$
\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}=-\boldsymbol{A}^{-1} \boldsymbol{E} \boldsymbol{B}^{-1}=-\boldsymbol{B}^{-1} \boldsymbol{E} \boldsymbol{A}^{-1} .
$$

Therefore, if $\boldsymbol{B}$ is nonsingular then by (8.30)

$$
\left\|\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right\| \leq\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\|\left\|\boldsymbol{B}^{-1}\right\| \leq K(A) \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|}\left\|\boldsymbol{B}^{-1}\right\| .
$$

Dividing through by $\left\|\boldsymbol{B}^{-1}\right\|$ gives the upper bounds in (8.27). Next, (8.30) implies

$$
\left\|\boldsymbol{B}^{-1}\right\| \leq\left\|\boldsymbol{A}^{-1}\right\|+\left\|\boldsymbol{A}^{-1} \boldsymbol{E} \boldsymbol{B}^{-1}\right\| \leq\left\|\boldsymbol{A}^{-1}\right\|+r\left\|\boldsymbol{B}^{-1}\right\| .
$$

Solving for $\left\|\boldsymbol{B}^{-1}\right\|$ and dividing by $\left\|\boldsymbol{A}^{-1}\right\|$ we obtain the upper bound in (8.28). Similarly we obtain the lower bound in (8.28) from $\left\|\boldsymbol{A}^{-1}\right\| \leq\left\|\boldsymbol{B}^{-1}\right\|+r\left\|\boldsymbol{B}^{-1}\right\|$.

The bound in (8.29) follows by multiplying (8.27) by $\left\|\boldsymbol{B}^{-1}\right\| /\left\|\boldsymbol{A}^{-1}\right\|$ and using (8.28).

That we can replace $\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\|$ by $\left\|\boldsymbol{E} \boldsymbol{A}^{-1}\right\|$ everywhere follows from (8.30). $\square$

### 8.4 Proof That the $\boldsymbol{p}$-Norms Are Norms

We want to show
Theorem 8.12 (The $p$ Vector Norms Are Norms) Let for $1 \leq p \leq \infty$ and $\boldsymbol{x} \in \mathbb{C}^{n}$

$$
\|\boldsymbol{x}\|_{p}:=\left(\sum_{j=1}^{n}\left|x_{j}\right|^{p}\right)^{1 / p}, \quad\|\boldsymbol{x}\|_{\infty}:=\max _{1 \leq j \leq n}\left|x_{j}\right| .
$$

Then for all $1 \leq p \leq \infty, \boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ and all $a \in \mathbb{C}$

1. $\|\boldsymbol{x}\|_{p} \geq 0$ with equality if and only if $\boldsymbol{x}=\mathbf{0}$.

2. $\|a \boldsymbol{x}\|_{p}=|a|\|\boldsymbol{x}\|_{p}$. (homogeneity)
3. $\|\boldsymbol{x}+\boldsymbol{y}\|_{p} \leq\|\boldsymbol{x}\|_{p}+\|\boldsymbol{y}\|_{p}$. (subadditivity)

Positivity and homogeneity follows immediately. To show the subadditivity we need some elementary properties of convex functions.

Definition 8.8 (Convex Function) Let $I \subset \mathbb{R}$ be an interval. A function $f: I \rightarrow \mathbb{R}$ is convex if

$$
f\left((1-\lambda) x_{1}+\lambda x_{2}\right) \leq(1-\lambda) f\left(x_{1}\right)+\lambda f\left(x_{2}\right)
$$

for all $x_{1}, x_{2} \in I$ with $x_{1}<x_{2}$ and all $\lambda \in[0,1]$. The sum $\sum_{j=1}^{n} \lambda_{j} x_{j}$ is called a convex combination of $x_{1}, \ldots, x_{n}$ if $\lambda_{j} \geq 0$ for $j=1, \ldots, n$ and $\sum_{j=1}^{n} \lambda_{j}=1$.

The convexity condition is illustrated in Fig. 8.1.

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-199.jpg?height=550&width=851&top_left_y=1359&top_left_x=337)
Fig. 8.1 A convex function

Lemma 8.2 (A Sufficient Condition for Convexity) If $f \in C^{2}[a, b]$ and $f^{\prime \prime}(x) \geq$ 0 for $x \in[a, b]$ then $f$ is convex.

Proof We recall the formula for linear interpolation with remainder, (cf a book on numerical methods) For any $a \leq x_{1} \leq x \leq x_{2} \leq b$ there is a $c \in\left[x_{1}, x_{2}\right]$ such that

$$
\begin{aligned}
f(x) & =\frac{x_{2}-x}{x_{2}-x_{1}} f\left(x_{1}\right)+\frac{x-x_{1}}{x_{2}-x_{1}} f\left(x_{2}\right)+\left(x-x_{1}\right)\left(x-x_{2}\right) f^{\prime \prime}(c) / 2 \\
& =(1-\lambda) f\left(x_{1}\right)+\lambda f\left(x_{2}\right)+\left(x_{2}-x_{1}\right)^{2} \lambda(\lambda-1) f^{\prime \prime}(c) / 2, \quad \lambda:=\frac{x-x_{1}}{x_{2}-x_{1}}
\end{aligned}
$$

Since $\lambda \in[0,1]$ we have $f(x) \leq(1-\lambda) f\left(x_{1}\right)+\lambda f\left(x_{2}\right)$. Moreover,

$$
x=\frac{x_{2}-x}{x_{2}-x_{1}} x_{1}+\frac{x-x_{1}}{x_{2}-x_{1}} x_{2}=(1-\lambda) x_{1}+\lambda x_{2}
$$

so that (8.31) holds, and $f$ is convex. $\square$

The following inequality is elementary, but can be used to prove many nontrivial inequalities.

Theorem 8.13 (Jensen's Inequality) Suppose $I \in \mathbb{R}$ is an interval and $f: I \rightarrow \mathbb{R}$ is convex. Then for all $n \in \mathbb{N}$, all $\lambda_{1}, \ldots, \lambda_{n}$ with $\lambda_{j} \geq 0$ for $j=1, \ldots, n$ and $\sum_{j=1}^{n} \lambda_{j}=1$, and all $z_{1}, \ldots, z_{n} \in I$

$$
f\left(\sum_{j=1}^{n} \lambda_{j} z_{j}\right) \leq \sum_{j=1}^{n} \lambda_{j} f\left(z_{j}\right) .
$$

Proof We use induction on $n$. The result is trivial for $n=1$. Let $n \geq 2$, assume the inequality holds for $n-1$, and let $\lambda_{j}, z_{j}$ for $j=1, \ldots, n$ be given as in the theorem. Since $n \geq 2$ we have $\lambda_{i}<1$ for at least one $i$ so assume without loss of generality that $\lambda_{1}<1$, and define $u:=\sum_{j=2}^{n} \frac{\lambda_{j}}{1-\lambda_{1}} z_{j}$. Since $\sum_{j=2}^{n} \lambda_{j}=1-\lambda_{1}$ this is a convex combination of $n-1$ terms and the induction hypothesis implies that $f(u) \leq \sum_{j=2}^{n} \frac{\lambda_{j}}{1-\lambda_{1}} f\left(z_{j}\right)$. But then by the convexity of $f$

$$
f\left(\sum_{j=1}^{n} \lambda_{j} z_{j}\right)=f\left(\lambda_{1} z_{1}+\left(1-\lambda_{1}\right) u\right) \leq \lambda_{1} f\left(z_{1}\right)+\left(1-\lambda_{1}\right) f(u) \leq \sum_{j=1}^{n} \lambda_{j} f\left(z_{j}\right)
$$

and the inequality holds for $n$. $\square$

Corollary 8.1 (Weighted Geometric/Arithmetic Mean Inequality) Suppose $\sum_{j=1}^{n} \lambda_{j} a_{j}$ is a convex combination of nonnegative numbers $a_{1}, \ldots, a_{n}$. Then

$$
a_{1}^{\lambda_{1}} a_{2}^{\lambda_{2}} \cdots a_{n}^{\lambda_{n}} \leq \sum_{j=1}^{n} \lambda_{j} a_{j},
$$

where $0^{0}:=0$.
Proof The result is trivial if one or more of the $a_{j}$ 's are zero so assume $a_{j}>0$ for all $j$. Consider the function $f:(0, \infty) \rightarrow \mathbb{R}$ given by $f(x)=-\log x$. Since $f^{\prime \prime}(x)=1 / x^{2}>0$ for $x \in(0, \infty)$, it follows from Lemma 8.2 that this function is convex. By Jensen's inequality

$$
-\log \left(\sum_{j=1}^{n} \lambda_{j} a_{j}\right) \leq-\sum_{j=1}^{n} \lambda_{j} \log \left(a_{j}\right)=-\log \left(a_{1}^{\lambda_{1}} \cdots a_{n}^{\lambda_{n}}\right)
$$

or $\log \left(a_{1}^{\lambda_{1}} \cdots a_{n}^{\lambda_{n}}\right) \leq \log \left(\sum_{j=1}^{n} \lambda_{j} a_{j}\right)$. The inequality follows since $\exp (\log x)$ $=x$ for $x>0$ and the exponential function is monotone increasing. $\square$

Taking $\lambda_{j}=\frac{1}{n}$ for all $j$ in (8.32) we obtain the classical geometric/arithmetic mean inequality

$$
\left(a_{1} a_{2} \cdots a_{n}\right)^{\frac{1}{n}} \leq \frac{1}{n} \sum_{j=1}^{n} a_{j} .
$$

Corollary 8.2 (Hölder's Inequality) For $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ and $1 \leq p \leq \infty$

$$
\sum_{j=1}^{n}\left|x_{j} y_{j}\right| \leq\|\boldsymbol{x}\|_{p}\|\boldsymbol{y}\|_{q}, \text { where } \frac{1}{p}+\frac{1}{q}=1
$$

Proof We leave the proof for $p=1$ and $p=\infty$ as an exercise so assume $1<p<$ $\infty$. For any $a, b \geq 0$ the weighted arithmetic/geometric mean inequality implies that

$$
a^{\frac{1}{p}} b^{\frac{1}{q}} \leq \frac{1}{p} a+\frac{1}{q} b, \text { where } \frac{1}{p}+\frac{1}{q}=1 .
$$

If $\boldsymbol{x}=\mathbf{0}$ or $\boldsymbol{y}=\mathbf{0}$ there is nothing to prove so assume that both $\boldsymbol{x}$ and $\boldsymbol{y}$ are nonzero. Using 8.34 on each term in the middle sum we obtain

$$
\frac{1}{\|\boldsymbol{x}\|_{p}\|\boldsymbol{y}\|_{q}} \sum_{j=1}^{n}\left|x_{j} y_{j}\right|=\sum_{j=1}^{n}\left(\frac{\left|x_{j}\right|^{p}}{\|\boldsymbol{x}\|_{p}^{p}}\right)^{\frac{1}{p}}\left(\frac{\left|y_{j}\right|^{q}}{\|\boldsymbol{y}\|_{q}^{q}}\right)^{\frac{1}{q}} \leq \sum_{j=1}^{n}\left(\frac{1}{p} \frac{\left|x_{j}\right|^{p}}{\|\boldsymbol{x}\|_{p}^{p}}+\frac{1}{q} \frac{\left|y_{j}\right|^{q}}{\|\boldsymbol{y}\|_{q}^{q}}\right)=1
$$

and the proof of the inequality is complete. $\square$

Corollary 8.3 (Minkowski's Inequality) For $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ and $1 \leq p \leq \infty$

$$
\|\boldsymbol{x}+\boldsymbol{y}\|_{p} \leq\|\boldsymbol{x}\|_{p}+\|\boldsymbol{y}\|_{p} .
$$

Proof We leave the proof for $p=1$ and $p=\infty$ as an exercise so assume $1<p<$ $\infty$. We write

$$
\|\boldsymbol{x}+\boldsymbol{y}\|_{p}^{p}=\sum_{j=1}^{n}\left|x_{j}+y_{j}\right|^{p} \leq \sum_{j=1}^{n}\left|x_{j}\right|\left|x_{j}+y_{j}\right|^{p-1}+\sum_{j=1}^{n}\left|y_{j}\right|\left|x_{j}+y_{j}\right|^{p-1} .
$$

We apply Hölder's inequality with exponent $p$ and $q$ to each sum. In view of the relation $(p-1) q=p$ the result is

$$
\|\boldsymbol{x}+\boldsymbol{y}\|_{p}^{p} \leq\|\boldsymbol{x}\|_{p}\|\boldsymbol{x}+\boldsymbol{y}\|_{p}^{p / q}+\|\boldsymbol{y}\|_{p}\|\boldsymbol{x}+\boldsymbol{y}\|_{p}^{p / q}=\left(\|\boldsymbol{x}\|_{p}+\|\boldsymbol{y}\|_{p}\right)\|\boldsymbol{x}+\boldsymbol{y}\|_{p}^{p-1},
$$

and canceling the common factor, the inequality follows. $\square$

### 8.4.1 $\boldsymbol{p}$-Norms and Inner Product Norms

It is possible to characterize the p-norms that are derived from an inner product. We start with the following identity.

Theorem 8.14 (Parallelogram Identity) For all $\boldsymbol{x}, \boldsymbol{y}$ in a real or complex inner product space

$$
\|\boldsymbol{x}+\boldsymbol{y}\|^{2}+\|\boldsymbol{x}-\boldsymbol{y}\|^{2}=2\|\boldsymbol{x}\|^{2}+2\|\boldsymbol{y}\|^{2},
$$

where $\|\|$ is the inner product norm in the space.
Proof We set $a= \pm 1$ in (5.5) and add the two equations. $\square$

Theorem 8.15 (When Is a Norm an Inner Product Norm?) To a given norm on a real or complex vector space $\mathcal{V}$ there exists an inner product on $\mathcal{V}$ such that $\langle\boldsymbol{x}, \boldsymbol{x}\rangle=\|\boldsymbol{x}\|^{2}$ if and only if the parallelogram identity (8.35) holds for all $\boldsymbol{x}, \boldsymbol{y} \in \mathcal{V}$.

Proof If $\langle\boldsymbol{x}, \boldsymbol{x}\rangle=\|\boldsymbol{x}\|^{2}$ then

$$
\|\boldsymbol{x}+\boldsymbol{y}\|^{2}+\|\boldsymbol{x}-\boldsymbol{y}\|^{2}=\langle\boldsymbol{x}+\boldsymbol{y}, \boldsymbol{x}+\boldsymbol{y}\rangle+\langle\boldsymbol{x}-\boldsymbol{y}, \boldsymbol{x}-\boldsymbol{y}\rangle=2\|\boldsymbol{x}\|^{2}+2\|\boldsymbol{y}\|^{2}
$$

and the parallelogram identity holds. For the converse we prove the real case and leave the complex case as an exercise. Suppose (8.35) holds for all $\boldsymbol{x}, \boldsymbol{y}$ in the real vector space $\mathcal{V}$. We show that

$$
\langle\boldsymbol{x}, \boldsymbol{y}\rangle:=\frac{1}{4}\left(\|\boldsymbol{x}+\boldsymbol{y}\|^{2}-\|\boldsymbol{x}-\boldsymbol{y}\|^{2}\right), \quad \boldsymbol{x}, \boldsymbol{y} \in \mathcal{V}
$$

defines an inner product on $\mathcal{V}$. Clearly 1. and 2. in Definition 5.1 hold. The hard part is to show 3. We need to show that

$$
\begin{gathered}
\langle\boldsymbol{x}, \boldsymbol{z}\rangle+\langle\boldsymbol{y}, \boldsymbol{z}\rangle=\langle\boldsymbol{x}+\boldsymbol{y}, \boldsymbol{z}\rangle, \quad \boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z} \in \mathcal{V} \\
\langle a \boldsymbol{x}, \boldsymbol{y}\rangle=a\langle\boldsymbol{x}, \boldsymbol{y}\rangle, \quad a \in \mathbb{R}, \quad \boldsymbol{x}, \boldsymbol{y} \in \mathcal{V} .
\end{gathered}
$$

Now

$$
\begin{aligned}
& 4\langle x, z\rangle+4\langle y, z\rangle \stackrel{(8.36)}{=}\|x+z\|^{2}-\|x-z\|^{2}+\|y+z\|^{2}-\|y-z\|^{2} \\
& =\left\|\left(z+\frac{x+y}{2}\right)+\frac{x-y}{2}\right\|^{2}-\left\|\left(z-\frac{x+y}{2}\right)+\frac{y-x}{2}\right\|^{2} \\
& +\left\|\left(z+\frac{x+y}{2}\right)-\frac{x-y}{2}\right\|^{2}-\left\|\left(z-\frac{x+y}{2}\right)-\frac{y-x}{2}\right\|^{2} \\
& \stackrel{(8.35)}{=} 2\left\|z+\frac{x+y}{2}\right\|^{2}+2\left\|\frac{x-y}{2}\right\|^{2}-2\left\|z-\frac{x+y}{2}\right\|^{2}-2\left\|\frac{y-x}{2}\right\|^{2} \\
& \stackrel{(8.36)}{=} 8\left\langle\frac{x+y}{2}, z\right\rangle
\end{aligned}
$$

or

$$
\langle\boldsymbol{x}, \boldsymbol{z}\rangle+\langle\boldsymbol{y}, \boldsymbol{z}\rangle=2\left\langle\frac{\boldsymbol{x}+\boldsymbol{y}}{2}, \boldsymbol{z}\right\rangle, \quad \boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z} \in \mathcal{V} .
$$

In particular, since $\boldsymbol{y}=\mathbf{0}$ implies $\langle\boldsymbol{y}, \boldsymbol{z}\rangle=0$ we obtain $\langle\boldsymbol{x}, \boldsymbol{z}\rangle=2\left\langle\frac{\boldsymbol{x}}{2}, \boldsymbol{z}\right\rangle$ for all $\boldsymbol{x}, \boldsymbol{z} \in \mathcal{V}$. This means that $2\left\langle\frac{\boldsymbol{x}+\boldsymbol{y}}{2}, \boldsymbol{z}\right\rangle=\langle\boldsymbol{x}+\boldsymbol{y}, \boldsymbol{z}\rangle$ for all $\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z} \in \mathcal{V}$ and (8.37) follows.

We first show (8.38) when $a=n$ is a positive integer. By induction

$$
\langle n \boldsymbol{x}, \boldsymbol{y}\rangle=\langle(n-1) \boldsymbol{x}+\boldsymbol{x}, \boldsymbol{y}\rangle \stackrel{\text { (8.37) }}{=}\langle(n-1) \boldsymbol{x}, \boldsymbol{y}\rangle+\langle\boldsymbol{x}, \boldsymbol{y}\rangle=n\langle\boldsymbol{x}, \boldsymbol{y}\rangle .
$$

If $m, n \in \mathbb{N}$ then

$$
m^{2}\left\langle\frac{n}{m} \boldsymbol{x}, \boldsymbol{y}\right\rangle \stackrel{\text { (8.39) }}{=} m\langle n \boldsymbol{x}, \boldsymbol{y}\rangle \stackrel{\text { (8.39) }}{=} m n\langle\boldsymbol{x}, \boldsymbol{y}\rangle,
$$

implying that (8.38) holds for positive rational numbers

$$
\left\langle\frac{n}{m} \boldsymbol{x}, \boldsymbol{y}\right\rangle=\frac{n}{m}\langle\boldsymbol{x}, \boldsymbol{y}\rangle .
$$

Now if $a>0$ there is a sequence $\left\{a_{n}\right\}$ of positive rational numbers converging to $a$. For each $n$

$$
a_{n}\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\left\langle a_{n} \boldsymbol{x}, \boldsymbol{y}\right\rangle \stackrel{(8.36)}{=} \frac{1}{4}\left(\left\|a_{n} \boldsymbol{x}+\boldsymbol{y}\right\|^{2}-\left\|a_{n} \boldsymbol{x}-\boldsymbol{y}\right\|^{2}\right) .
$$

Taking limits and using continuity of norms we obtain $a\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\langle a \boldsymbol{x}, \boldsymbol{y}\rangle$. This also holds for $a=0$. Finally, if $a<0$ then $(-a)>0$ and from what we just showed

$$
(-a)\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\langle(-a) \boldsymbol{x}, \boldsymbol{y}\rangle \stackrel{(8.36)}{=} \frac{1}{4}\left(\|-a \boldsymbol{x}+\boldsymbol{y}\|^{2}-\|-a \boldsymbol{x}-\boldsymbol{y}\|^{2}\right)=-\langle a \boldsymbol{x}, \boldsymbol{y}\rangle,
$$

so (8.38) also holds for negative $a$. $\square$

Corollary 8.4 (Are the $p$-Norms Inner Product Norms?) For the $p$ vector norms on $\mathcal{V}=\mathbb{R}^{n}$ or $\mathcal{V}=\mathbb{C}^{n}, 1 \leq p \leq \infty, n \geq 2$, there is an inner product on $\mathcal{V}$ such that $\langle\boldsymbol{x}, \boldsymbol{x}\rangle=\|\boldsymbol{x}\|_{p}^{2}$ for all $\boldsymbol{x} \in \mathcal{V}$ if and only if $p=2$.

Proof For $p=2$ the $p$-norm is the Euclidian norm which corresponds to the standard inner product. If $p \neq 2$ then the parallelogram identity (8.35) does not hold for say $\boldsymbol{x}:=\boldsymbol{e}_{1}$ and $\boldsymbol{y}:=\boldsymbol{e}_{2}$. $\square$

### 8.5 Exercises Chap. 8

### 8.5.1 Exercises Sect. 8.1

Exercise 8.1 (An A-Norm Inequality (Exam Exercise 1982-4)) Given a symmetric positive definite matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ with eigenvalues $0<\lambda_{n} \leq \cdots \leq \lambda_{1}$. Show that

$$
\|\boldsymbol{x}\|_{\boldsymbol{A}} \leq\|\boldsymbol{y}\|_{\boldsymbol{A}} \Longrightarrow\|\boldsymbol{x}\|_{2} \leq \sqrt{\frac{\lambda_{1}}{\lambda_{n}}}\|\boldsymbol{y}\|_{2},
$$

where

$$
\|\boldsymbol{x}\|_{\boldsymbol{A}}:=\sqrt{\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x}}, \quad \boldsymbol{x} \in \mathbb{R}^{n} .
$$

Exercise 8.2 (A Orthogonal Bases (Exam Exercise 1995-4)) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be a symmetric and positive definite matrix and assume $\boldsymbol{b}_{1}, \ldots, \boldsymbol{b}_{n}$ is a basis for $\mathbb{R}^{n}$. We define $\boldsymbol{B}_{k}:=\left[\boldsymbol{b}_{1}, \ldots, \boldsymbol{b}_{k}\right] \in \mathbb{R}^{n \times k}$ for $k=1, \ldots, n$. We consider in this exercise the inner product $\langle\cdot, \cdot\rangle$ defined by $\langle\boldsymbol{x}, \boldsymbol{y}\rangle:=\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{y}$ for $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}$ and the corresponding norm $\|\boldsymbol{x}\|_{\boldsymbol{A}}:=\langle\boldsymbol{x}, \boldsymbol{x}\rangle^{1 / 2}$. We define $\tilde{\boldsymbol{b}}_{1}:=\boldsymbol{b}_{1}$ and

$$
\tilde{\boldsymbol{b}}_{k}:=\boldsymbol{b}_{k}-\boldsymbol{B}_{k-1}\left(\boldsymbol{B}_{k-1}^{T} \boldsymbol{A} \boldsymbol{B}_{k-1}\right)^{-1} \boldsymbol{B}_{k-1}^{T} \boldsymbol{A} \boldsymbol{b}_{k}, \quad k=2, \ldots, n .
$$

a) Show that $\boldsymbol{B}_{k}^{T} \boldsymbol{A} \boldsymbol{B}_{k}$ is positive definite for $k=1, \ldots, n$.
b) Show that for $k=2, \ldots, n$ we have (i) $\left\langle\tilde{\boldsymbol{b}}_{k}, \boldsymbol{b}_{j}\right\rangle=0$ for $j=1, \ldots, k-1$ and (ii) $\tilde{\boldsymbol{b}}_{k}-\boldsymbol{b}_{k} \in \operatorname{span}\left(\boldsymbol{b}_{1}, \ldots, \boldsymbol{b}_{k-1}\right)$.

c) Explain why $\tilde{\boldsymbol{b}}_{1}, \ldots, \tilde{\boldsymbol{b}}_{n}$ is a basis for $\mathbb{R}^{n}$ which in addition is $\boldsymbol{A}$-orthogonal, i.e., $\left\langle\tilde{\boldsymbol{b}}_{i}, \tilde{\boldsymbol{b}}_{j}\right\rangle=0$ for all $i, j \leq n, i \neq j$.
d) Define $\tilde{\boldsymbol{B}}_{n}:=\left[\tilde{\boldsymbol{b}}_{1}, \ldots, \tilde{\boldsymbol{b}}_{n}\right]$. Show that there is an upper triangular matrix $\boldsymbol{T} \in$ $\mathbb{R}^{n \times n}$ with ones on the diagonal and satisfies $\boldsymbol{B}_{n}=\tilde{\boldsymbol{B}}_{n} \boldsymbol{T}$.
e) Assume that the matrix $\boldsymbol{T}$ in d) is such that $\left|t_{i j}\right| \leq \frac{1}{2}$ for all $i, j \leq n, i \neq j$. Assume also that $\left\|\tilde{\boldsymbol{b}}_{k}\right\|_{\boldsymbol{A}}^{2} \leq 2\left\|\tilde{\boldsymbol{b}}_{k+1}\right\|_{\boldsymbol{A}}^{2}$ for $k=1, \ldots, n-1$ and that $\operatorname{det}\left(\boldsymbol{B}_{n}\right)=1$. Show that then ${ }^{2}$
$$
\left\|\boldsymbol{b}_{1}\right\|_{\boldsymbol{A}}\left\|\boldsymbol{b}_{2}\right\|_{\boldsymbol{A}} \cdots\left\|\boldsymbol{b}_{n}\right\|_{\boldsymbol{A}} \leq 2^{n(n-1) / 4} \sqrt{\operatorname{det}(\boldsymbol{A})} .
$$

### 8.5.2 Exercises Sect. 8.2

Exercise 8.3 (Consistency of Sum Norm?) Show that the sum norm is consistent.
Exercise 8.4 (Consistency of Max Norm?) Show that the max norm is not consistent by considering $\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$.

Exercise 8.5 (Consistency of Modified Max Norm)

a) Show that the norm
$$
\|\boldsymbol{A}\|:=\sqrt{m n}\|\boldsymbol{A}\|_{M}, \quad \boldsymbol{A} \in \mathbb{C}^{m \times n}
$$
is a consistent matrix norm.
b) Show that the constant $\sqrt{m n}$ can be replaced by $m$ and by $n$.

Exercise 8.6 (What Is the Sum Norm Subordinate to?) Show that the sum norm is subordinate to the $l_{1}$-norm.

Exercise 8.7 (What Is the Max Norm Subordinate to?)

a) Show that the max norm is subordinate to the $\infty$ and 1 norm, i.e., $\|\boldsymbol{A} \boldsymbol{x}\|_{\infty} \leq$ $\|\boldsymbol{A}\|_{M}\|\boldsymbol{x}\|_{1}$ holds for all $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ and all $\boldsymbol{x} \in \mathbb{C}^{n}$.
b) Show that if $\|\boldsymbol{A}\|_{M}=\left|a_{k l}\right|$, then $\left\|\boldsymbol{A} \boldsymbol{e}_{l}\right\|_{\infty}=\|\boldsymbol{A}\|_{M}\left\|\boldsymbol{e}_{l}\right\|_{1}$.
c) Show that $\|\boldsymbol{A}\|_{M}=\max _{\boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{A} \boldsymbol{x}\|_{\infty}}{\|\boldsymbol{x}\|_{1}}$.

Exercise 8.8 (Spectral Norm) Let $m, n \in \mathbb{N}$ and $\boldsymbol{A} \in \mathbb{C}^{m \times n}$. Show that

$$
\|\boldsymbol{A}\|_{2}=\max _{\|\boldsymbol{x}\|_{2}=\|\boldsymbol{y}\|_{2}=1}\left|\boldsymbol{y}^{*} \boldsymbol{A} \boldsymbol{x}\right| .
$$

[^17]Exercise 8.9 (Spectral Norm of the Inverse) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular. Show that $\|\boldsymbol{A} \boldsymbol{x}\|_{2} \geq \sigma_{n}$ for all $\boldsymbol{x} \in \mathbb{C}^{n}$ with $\|\boldsymbol{x}\|_{2}=1$. Show that

$$
\left\|\boldsymbol{A}^{-1}\right\|_{2}=\max _{\boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{x}\|_{2}}{\|\boldsymbol{A} \boldsymbol{x}\|_{2}} .
$$

Exercise 8.10 ( $p$-Norm Example) Let

$$
\boldsymbol{A}=\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right] .
$$

Compute $\|\boldsymbol{A}\|_{p}$ and $\left\|\boldsymbol{A}^{-1}\right\|_{p}$ for $p=1,2, \infty$.
Exercise 8.11 (Unitary Invariance of the Spectral Norm) Show that $\|\boldsymbol{V} \boldsymbol{A}\|_{2}=$ $\|\boldsymbol{A}\|_{2}$ holds even for a rectangular $\boldsymbol{V}$ as long as $\boldsymbol{V}^{*} \boldsymbol{V}=\boldsymbol{I}$.

Exercise $8.12\left(\|\boldsymbol{A} \boldsymbol{U}\|_{2}\right.$ Rectangular $\left.\boldsymbol{A}\right)$ Find $\boldsymbol{A} \in \mathbb{R}^{2 \times 2}$ and $\boldsymbol{U} \in \mathbb{R}^{2 \times 1}$ with $\boldsymbol{U}^{T} \boldsymbol{U}=\boldsymbol{I}$ such that $\|\boldsymbol{A} \boldsymbol{U}\|_{2}<\|\boldsymbol{A}\|_{2}$. Thus, in general, $\|\boldsymbol{A} \boldsymbol{U}\|_{2}=\|\boldsymbol{A}\|_{2}$ does not hold for a rectangular $\boldsymbol{U}$ even if $\boldsymbol{U}^{*} \boldsymbol{U}=\boldsymbol{I}$.

Exercise 8.13 ( $p$-Norm of Diagonal Matrix) Show that $\|\boldsymbol{A}\|_{p}=\rho(\boldsymbol{A}):=$ $\max \left|\lambda_{i}\right|$ (the largest eigenvalue of $\boldsymbol{A}$ ), $1 \leq p \leq \infty$, when $\boldsymbol{A}$ is a diagonal matrix.

Exercise 8.14 (Spectral Norm of a Column Vector) A vector $\boldsymbol{a} \in \mathbb{C}^{m}$ can also be considered as a matrix $\boldsymbol{A} \in \mathbb{C}^{m, 1}$.

a) Show that the spectral matrix norm (2-norm) of $\boldsymbol{A}$ equals the Euclidean vector norm of $\boldsymbol{a}$.
b) Show that $\|\boldsymbol{A}\|_{p}=\|\boldsymbol{a}\|_{p}$ for $1 \leq p \leq \infty$.

Exercise 8.15 (Norm of Absolute Value Matrix) If $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has elements $a_{i j}$, let $|\boldsymbol{A}| \in \mathbb{R}^{m \times n}$ be the matrix with elements $\left|a_{i j}\right|$.

a) Compute $|\boldsymbol{A}|$ if $\boldsymbol{A}=\left[\begin{array}{cc}1+i & -2 \\ 1 & 1-i\end{array}\right], \quad i=\sqrt{-1}$.
b) Show that for any $\boldsymbol{A} \in \mathbb{C}^{m \times n}\|\boldsymbol{A}\|_{F}=\||\boldsymbol{A}|\|_{F},\|\boldsymbol{A}\|_{p}=\||\boldsymbol{A}|\|_{p}$ for $p=1, \infty$.
c) Show that for any $\boldsymbol{A} \in \mathbb{C}^{m \times n}\|\boldsymbol{A}\|_{2} \leq\||\boldsymbol{A}|\|_{2}$.
d) Find a real symmetric $2 \times 2$ matrix $\boldsymbol{A}$ such that $\|\boldsymbol{A}\|_{2}<\||\boldsymbol{A}|\|_{2}$.

Exercise 8.16 (An Iterative Method (Exam Exercise 2017-3)) Assume that $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is non-singular and nondefective (the eigenvectors of $\boldsymbol{A}$ form a basis for $\mathbb{C}^{n}$ ). We wish to solve $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Assume that we have a list of the eigenvalues $\left\{\lambda_{1}, \lambda_{2}, \ldots, \lambda_{m}\right\}$, in no particular order. We have that $m \leq n$, since some of the eigenvalues may have multiplicity larger than one. Given $\boldsymbol{x}_{0} \in \mathbb{C}^{n}$, and $k \geq 0$, we
define the sequence $\left\{\boldsymbol{x}_{k}\right\}_{k=0}^{m-1}$ by

$$
\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\frac{1}{\lambda_{k+1}} \boldsymbol{r}_{k}, \text { where } \boldsymbol{r}_{k}=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k} .
$$

a) Let the coefficients $c_{i k}$ be defined by
$$
\boldsymbol{r}_{k}=\sum_{i=1}^{n} c_{i k} \boldsymbol{u}_{i},
$$
where $\left\{\left(\sigma_{i}, \boldsymbol{u}_{i}\right)\right\}_{i=1}^{n}$ are the eigenpairs of $\boldsymbol{A}$. Show that
$$
c_{i, k+1}= \begin{cases}0 & \text { if } \sigma_{i}=\lambda_{k+1}, \\ c_{i, k}\left(1-\frac{\sigma_{i}}{\lambda_{k+1}}\right) & \text { otherwise } .\end{cases}
$$
b) Show that for some $l \leq m$, we have that $\boldsymbol{x}_{l}=\boldsymbol{x}_{l+1}=\cdots=\boldsymbol{x}_{m}=\boldsymbol{x}$, where $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$.
c) Consider this iteration for the $n \times n$ matrix $\boldsymbol{T}=\operatorname{tridiag}(c, d, c)$, where $d$ and $c$ are positive real numbers and $d>2 c$. The eigenvalues of $\boldsymbol{T}$ are
$$
\lambda_{j}=d+2 c \cos \left(\frac{j \pi}{n+1}\right), \quad j=1, \ldots, n .
$$
What is the operation count for solving $\boldsymbol{T} \boldsymbol{x}=\boldsymbol{b}$ using the iterative algorithm above?
d) Let now $\boldsymbol{B}$ be a symmetric $n \times n$ matrix which is zero on the "tridiagonal", i.e., $b_{i j}=0$ if $|i-j| \leq 1$. Set $\boldsymbol{A}=\boldsymbol{T}+\boldsymbol{B}$, where $\boldsymbol{T}$ is the tridiagonal matrix above. We wish to solve $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ by the iterative scheme
$$
\boldsymbol{T} \boldsymbol{x}_{k+1}=\boldsymbol{b}-\boldsymbol{B} \boldsymbol{x}_{k} .
$$
Recall that if $\boldsymbol{E} \in \mathbb{R}^{n \times n}$ has eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$ then $\rho(\boldsymbol{E}):=\max _{i}\left|\lambda_{i}\right|$ is the spectral radius of $\boldsymbol{E}$. Show that $\rho\left(\boldsymbol{T}^{-1} \boldsymbol{B}\right) \leq \rho\left(\boldsymbol{T}^{-1}\right) \rho(\boldsymbol{B})$.
e) Show that the iteration (8.40) will converge if ${ }^{3}$
$$
\min \left\{\max _{i} \sum_{j=1}^{n}\left|b_{i j}\right|, \max _{j} \sum_{i=1}^{n}\left|b_{i j}\right|\right\}<d-2 c .
$$
[^18]
### 8.5.3 Exercises Sect. 8.3

Exercise 8.17 (Perturbed Linear Equation (Exam Exercise 1981-2)) Given the systems $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}, \boldsymbol{A} \boldsymbol{y}=\boldsymbol{b}+\boldsymbol{e}$, where

$$
\boldsymbol{A}:=\left[\begin{array}{cc}
1.1 & 1 \\
1 & 1
\end{array}\right], \quad \boldsymbol{b}:=\left[\begin{array}{l}
b_{1} \\
b_{2}
\end{array}\right]=\left[\begin{array}{l}
2.1 \\
2.0
\end{array}\right], \quad \boldsymbol{e}:=\left[\begin{array}{l}
e_{1} \\
e_{2}
\end{array}\right], \quad\|\boldsymbol{e}\|_{2}=0.1 .
$$

We define $\delta:=\|\boldsymbol{x}-\boldsymbol{y}\|_{2} /\|\boldsymbol{x}\|_{2}$.

a) Determine $K_{2}(\boldsymbol{A})=\|\boldsymbol{A}\|_{2}\left\|\boldsymbol{A}^{-1}\right\|_{2}$. Give an upper bound and a positive lower bound for $\delta$ without computing $\boldsymbol{x}$ and $\boldsymbol{y}$.
b) Suppose as before that $b_{2}=2.0$ and $\|\boldsymbol{e}\|_{2}=0.1$. Determine $b_{1}$ and $\boldsymbol{e}$ which maximize $\delta$.

Exercise 8.18 (Sharpness of Perturbation Bounds) The upper and lower bounds for $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{x}\|$ given by (8.22) can be attained for any matrix $\boldsymbol{A}$, but only for special choices of $\boldsymbol{b}$. Suppose $\boldsymbol{y}_{\boldsymbol{A}}$ and $\boldsymbol{y}_{\boldsymbol{A}^{-1}}$ are vectors with $\left\|\boldsymbol{y}_{\boldsymbol{A}}\right\|=\left\|\boldsymbol{y}_{\boldsymbol{A}^{-1}}\right\|=1$ and $\|\boldsymbol{A}\|=\left\|\boldsymbol{A} \boldsymbol{y}_{\boldsymbol{A}}\right\|$ and $\left\|\boldsymbol{A}^{-1}\right\|=\left\|\boldsymbol{A}^{-1} \boldsymbol{y}_{\boldsymbol{A}^{-1}}\right\|$.

a) Show that the upper bound in (8.22) is attained if $\boldsymbol{b}=\boldsymbol{A} \boldsymbol{y}_{\boldsymbol{A}}$ and $\boldsymbol{e}=\boldsymbol{y}_{\boldsymbol{A}^{-1}}$.
b) Show that the lower bound is attained if $\boldsymbol{b}=\boldsymbol{y}_{\boldsymbol{A}^{-1}}$ and $\boldsymbol{e}=\boldsymbol{A} \boldsymbol{y}_{\boldsymbol{A}}$.

Exercise 8.19 (Condition Number of 2. Derivative Matrix) In this exercise we will show that for $m \geq 1$

$$
\frac{4}{\pi^{2}}(m+1)^{2}-2 / 3<\operatorname{cond}_{p}(\boldsymbol{T}) \leq \frac{1}{2}(m+1)^{2}, \quad p=1,2, \infty,
$$

where $\boldsymbol{T}:=\operatorname{tridiag}(-1,2,-1) \in \mathbb{R}^{m \times m}$ and $\operatorname{cond}_{p}(\boldsymbol{T}):=\|\boldsymbol{T}\|_{p}\left\|\boldsymbol{T}^{-1}\right\|_{p}$ is the $p$ norm condition number of $\boldsymbol{T}$. The $p$ matrix norm is given by (8.17). You will need the explicit inverse of $\boldsymbol{T}$ given by (2.39) and the eigenvalues given in Lemma 2.2. As usual we define $h:=1 /(m+1)$.

a) Show that for $m \geq 3$
$$
\operatorname{cond}_{1}(\boldsymbol{T})=\operatorname{cond}_{\infty}(\boldsymbol{T})=\frac{1}{2} \begin{cases}h^{-2}, & m \text { odd } \\ h^{-2}-1, & m \text { even }\end{cases}
$$
and that $\operatorname{cond}_{1}(\boldsymbol{T})=\operatorname{cond}_{\infty}(\boldsymbol{T})=3$ for $m=2$.
b) Show that for $p=2$ and $m \geq 1$ we have
$$
\operatorname{cond}_{2}(\boldsymbol{T})=\cot ^{2}\left(\frac{\pi h}{2}\right)=1 / \tan ^{2}\left(\frac{\pi h}{2}\right) .
$$

c) Show the bounds
$$
\frac{4}{\pi^{2}} h^{-2}-\frac{2}{3}<\operatorname{cond}_{2}(\boldsymbol{T})<\frac{4}{\pi^{2}} h^{-2} .
$$
Hint: For the upper bound use the inequality $\tan x>x$ valid for $0<x<\pi / 2$. For the lower bound we use (without proof) the inequality $\cot ^{2} x>\frac{1}{x^{2}}-\frac{2}{3}$ for $x>0$.
d) Show (8.41).

Exercise 8.20 (Perturbation of the Identity Matrix) Let $\boldsymbol{E}$ be a square matrix.

a) Show that if $\boldsymbol{I}-\boldsymbol{E}$ is nonsingular then
$$
\frac{\left\|(\boldsymbol{I}-\boldsymbol{E})^{-1}-\boldsymbol{I}\right\|}{\left\|(\boldsymbol{I}-\boldsymbol{E})^{-1}\right\|} \leq\|\boldsymbol{E}\|
$$
b) If $\|\boldsymbol{E}\|<1$ then $(\boldsymbol{I}-\boldsymbol{E})^{-1}$ is nonsingular by exists and
$$
\frac{1}{1+\|\boldsymbol{E}\|} \leq\left\|(\boldsymbol{I}-\boldsymbol{E})^{-1}\right\| \leq \frac{1}{1-\|\boldsymbol{E}\|}
$$
Show the lower bound. Show the upper bound if $\|\boldsymbol{I}\|=1$. In general for a consistent matrix norm (i.e., the Frobenius norm) the upper bound follows from Theorem 12.14 using Neumann series.
c) Show that if $\|\boldsymbol{E}\|<1$ then
$$
\left\|(\boldsymbol{I}-\boldsymbol{E})^{-1}-\boldsymbol{I}\right\| \leq \frac{\|\boldsymbol{E}\|}{1-\|\boldsymbol{E}\|} .
$$

Exercise 8.21 (Lower Bounds in (8.27) and (8.29))

a) Solve for $\boldsymbol{E}$ in (8.30) and show that
$$
K(\boldsymbol{B})^{-1} \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|} \leq \frac{\left\|\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right\|}{\left\|\boldsymbol{B}^{-1}\right\|} .
$$
b) Show using a) and (8.28) that
$$
\frac{K(\boldsymbol{B})^{-1}}{1+r} \frac{\|\boldsymbol{E}\|}{\|\boldsymbol{A}\|} \leq \frac{\left\|\boldsymbol{B}^{-1}-\boldsymbol{A}^{-1}\right\|}{\left\|\boldsymbol{A}^{-1}\right\|} .
$$

Exercise 8.22 (Periodic Spline Interpolation (Exam Exercise 1993-2)) Let the components of $\boldsymbol{x}=\left[x_{0}, \ldots, x_{n}\right]^{T} \in \mathbb{R}^{n+1}$ define a partition of the interval $[a, b]$,

$$
a=x_{0}<x_{1}<\cdots<x_{n}=b,
$$

and given a dataset $\boldsymbol{y}:=\left[y_{0}, \ldots, y_{n}\right]^{T} \in \mathbb{R}^{n+1}$, where we assume $y_{0}=y_{n}$. The periodic cubic spline interpolation problem is defined by finding a cubic spline function $g$ satisfying the conditions

$$
\begin{array}{ll}
g\left(x_{i}\right)=y_{i}, & i=0,1, \ldots, n, \\
g^{\prime}(a)=g^{\prime}(b), & g^{\prime \prime}(a)=g^{\prime \prime}(b) .
\end{array}
$$

(Recall that $g$ is a cubic polynomial on each interval $\left(x_{i-1}, x_{i}\right)$, for $i=1, \ldots, n$ with smoothness $C^{2}[a, b]$.)

We define $s_{i}:=g^{\prime}\left(x_{i}\right), i=0, \ldots, n$. It can be shown that the vector $\boldsymbol{s}:=$ $\left[s_{1}, \ldots, s_{n}\right]^{T}$ is determined from a linear system

$$
\boldsymbol{A} \boldsymbol{s}=\boldsymbol{b},
$$

where $\boldsymbol{b} \in \mathbb{R}^{n}$ is a given vector determined by $\boldsymbol{x}$ and $\boldsymbol{y}$. The matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is given by

$$
A:=\left[\begin{array}{cccccc}
2 & \mu_{1} & 0 & \cdots & 0 & \lambda_{1} \\
\lambda_{2} & 2 & \mu_{2} & \ddots & & 0 \\
0 & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & 0 \\
0 & & \ddots & \lambda_{n-1} & 2 & \mu_{n-1} \\
\mu_{n} & 0 & \cdots & 0 & \lambda_{n} & 2
\end{array}\right],
$$

where

$$
\lambda_{i}:=\frac{h_{i}}{h_{i-1}+h_{i}}, \quad \mu_{i}:=\frac{h_{i-1}}{h_{i-1}+h_{i}}, \quad, i=1, \ldots, n,
$$

and

$$
h_{i}=x_{i+1}-x_{i}, \quad i=0, \ldots, n-1, \text { and } h_{n}=h_{0} .
$$

You shall not argue or prove the system (8.44). Throughout this exercise we assume that

$$
\frac{1}{2} \leq \frac{h_{i}}{h_{i-1}} \leq 2, \quad i=1, \ldots, n .
$$

a) Show that
$$
\|\boldsymbol{A}\|_{\infty}=3 \quad \text { and that } \quad\|\boldsymbol{A}\|_{1} \leq \frac{10}{3} .
$$
b) Show that $\left\|\boldsymbol{A}^{-1}\right\|_{\infty} \leq 1$.
c) Show that $\left\|\boldsymbol{A}^{-1}\right\|_{1} \leq \frac{3}{2}$.
d) Let $\boldsymbol{s}$ and $\boldsymbol{b}$ be as in (8.44), where we assume $\boldsymbol{b} \neq \mathbf{0}$. Let $\boldsymbol{e} \in \mathbb{R}^{n}$ be such that $\|\boldsymbol{e}\|_{p} /\|\boldsymbol{b}\|_{p} \leq 0.01$. Suppose $\hat{\boldsymbol{s}}$ satisfies
$$
\boldsymbol{A} \hat{\boldsymbol{s}}=\boldsymbol{b}+\boldsymbol{e} .
$$
Give estimates for
$$
\frac{\|\hat{\boldsymbol{s}}-\boldsymbol{s}\|_{\infty}}{\|\boldsymbol{s}\|_{\infty}} \quad \text { and } \quad \frac{\|\hat{\boldsymbol{s}}-\boldsymbol{s}\|_{1}}{\|\boldsymbol{s}\|_{1}} .
$$

Exercise 8.23 (LSQ MATLAB Program (Exam Exercise 2013-4)) Suppose $\boldsymbol{A} \in \mathbb{R}^{m \times n}, \boldsymbol{b} \in \mathbb{R}^{m}$, where $\boldsymbol{A}$ has rank $n$ and let $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{T}$ be a singular value factorization of $\boldsymbol{A}$. Thus $\boldsymbol{U} \in \mathbb{R}^{m \times n}$ and $\boldsymbol{\Sigma}, \boldsymbol{V} \in \mathbb{R}^{n \times n}$. Write a MATLAB function $[\mathrm{x}, \mathrm{K}]=l \mathrm{sq}(\mathrm{A}, \mathrm{b})$ that uses the singular value factorization of $\boldsymbol{A}$ to calculate a least squares solution $\boldsymbol{x}=\boldsymbol{V} \boldsymbol{\Sigma}^{-1} \boldsymbol{U}^{T} \boldsymbol{b}$ to the system $\boldsymbol{A} \boldsymbol{x}=$ $\boldsymbol{b}$ and the spectral (2-norm) condition number of $\boldsymbol{A}$. The MATLAB command $[\mathrm{U}, \mathrm{Sigma}, \mathrm{V}]=\operatorname{svd}(\mathrm{A}, 0)$ computes the singular value factorization of $\boldsymbol{A}$.

### 8.5.4 Exercises Sect. 8.4

Exercise 8.24 (When Is a Complex Norm an Inner Product Norm?) Given a vector norm in a complex vector space $\mathcal{V}$, and suppose (8.35) holds for all $\boldsymbol{x}, \boldsymbol{y} \in \mathcal{V}$. Show that

$$
\langle\boldsymbol{x}, \boldsymbol{y}\rangle:=\frac{1}{4}\left(\|\boldsymbol{x}+\boldsymbol{y}\|^{2}-\|\boldsymbol{x}-\boldsymbol{y}\|^{2}+i\|\boldsymbol{x}+i \boldsymbol{y}\|^{2}-i\|\boldsymbol{x}-i \boldsymbol{y}\|^{2}\right),
$$

defines an inner product on $\mathcal{V}$, where $i=\sqrt{-1}$. The identity (8.45) is called the polarization identity. ${ }^{4}$

Exercise 8.25 ( $p$ Norm for $p=1$ and $p=\infty$ ) Show that $\|\cdot\| p$ is a vector norm in $\mathbb{R}^{n}$ for $p=1, p=\infty$.

[^19]Exercise 8.26 (The $p$-Norm Unit Sphere) The set

$$
S_{p}=\left\{\boldsymbol{x} \in \mathbb{R}^{n}:\|\boldsymbol{x}\|_{p}=1\right\}
$$

is called the unit sphere in $\mathbb{R}^{n}$ with respect to $p$. Draw $S_{p}$ for $p=1,2, \infty$ for $n=2$.
Exercise 8.27 (Sharpness of $p$-Norm Inequality) For $p \geq 1$, and any $\boldsymbol{x} \in \mathbb{C}^{n}$ we have $\|\boldsymbol{x}\|_{\infty} \leq\|\boldsymbol{x}\|_{p} \leq n^{1 / p}\|\boldsymbol{x}\|_{\infty}$ (cf. (8.5)).

Produce a vector $\boldsymbol{x}_{l}$ such that $\left\|\boldsymbol{x}_{l}\right\|_{\infty}=\left\|\boldsymbol{x}_{l}\right\|_{p}$ and another vector $\boldsymbol{x}_{u}$ such that $\left\|\boldsymbol{x}_{u}\right\|_{p}=n^{1 / p}\left\|\boldsymbol{x}_{u}\right\|_{\infty}$. Thus, these inequalities are sharp.

Exercise 8.28 ( $p$-Norm Inequalities for Arbitrary $p$ ) If $1 \leq q \leq p \leq \infty$ then

$$
\|\boldsymbol{x}\|_{p} \leq\|\boldsymbol{x}\|_{q} \leq n^{1 / q-1 / p}\|\boldsymbol{x}\|_{p}, \quad \boldsymbol{x} \in \mathbb{C}^{n} .
$$

Hint: For the rightmost inequality use Jensen's inequality Cf. Theorem 8.13 with $f(z)=z^{p / q}$ and $z_{i}=\left|x_{i}\right|^{q}$. For the left inequality consider first $y_{i}=x_{i} /\|\boldsymbol{x}\|_{\infty}$, $i=1,2, \ldots, n$.

### 8.6 Review Questions

8.6.1

- What is a consistent matrix norm?
- what is a subordinate matrix norm?
- is an operator norm consistent?
- why is the Frobenius norm not an operator norm?
- what is the spectral norm of a matrix?
- how do we compute $\|\boldsymbol{A}\|_{\infty}$ ?
- what is the spectral condition number of a symmetric positive definite matrix?
8.6.2 Does there exist a vector norm $\|\|$ such that $\| \boldsymbol{A} \boldsymbol{x}\|\leq\| \boldsymbol{A}\left\|_{F}\right\| \boldsymbol{x} \|$ for all $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}, \boldsymbol{x} \in \mathbb{C}^{n}, m, n \in \mathbb{N}$ ?
8.6.3 Why is $\|\boldsymbol{A}\|_{2} \leq\|\boldsymbol{A}\|_{F}$ for any matrix $\boldsymbol{A}$ ?
8.6.4 What is the spectral norm of the inverse of a normal matrix?

## Chapter 9 <br> Least Squares

Consider the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ of $m$ equations in $n$ unknowns. It is overdetermined, if $m>n$, square, if $m=n$, and underdetermined, if $m<n$. In either case the system can only be solved approximately if $\boldsymbol{b} \notin \mathcal{R}(\boldsymbol{A})$, the column space of $\boldsymbol{A}$. One way to solve $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ approximately is to select a vector norm $\|\cdot\|$, say a $p$-norm, and look for $\boldsymbol{x} \in \mathbb{C}^{n}$ which minimizes $\|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|$. The use of the one and $\infty$ norm can be formulated as linear programming problems, while the Euclidian norm leads to a linear system and has applications in statistics. Only this norm is considered here.

Definition 9.1 (Least Squares Problem (LSQ)) Suppose $m, n \in \mathbb{N}, \boldsymbol{A} \in \mathbb{C}^{m \times n}$ and $\boldsymbol{b} \in \mathbb{C}^{m}$. To find $\boldsymbol{x} \in \mathbb{C}^{n}$ that minimizes $E: \mathbb{C}^{n} \rightarrow \mathbb{R}$ given by

$$
E(\boldsymbol{x}):=\|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}^{2},
$$

is called the least squares problem. A minimizer $\boldsymbol{x}$ is called a least squares solution.

Since the square root function is monotone, minimizing $E(\boldsymbol{x})$ or $\sqrt{E(\boldsymbol{x})}$ is equivalent.

Example 9.1 (Average) Consider an overdetermined linear system of 3 equations in one unknown

$$
\begin{aligned}
& x_{1}=1 \\
& x_{1}=1, \quad \boldsymbol{A}=\left[\begin{array}{l}
1 \\
1 \\
x_{1}=2
\end{array}\right], \quad \boldsymbol{x}=\left[x_{1}\right], \quad \boldsymbol{b}=\left[\begin{array}{l}
1 \\
1 \\
1
\end{array}\right] .
\end{aligned}
$$

To solve this as a least squares problem we compute

$$
\|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}^{2}=\left(x_{1}-1\right)^{2}+\left(x_{1}-1\right)^{2}+\left(x_{1}-2\right)^{2}=3 x_{1}^{2}-8 x_{1}+6 .
$$

Setting the first derivative with respect to $x_{1}$ equal to zero we obtain $6 x_{1}-8=0$ or $x_{1}=4 / 3$, the average of $b_{1}, b_{2}, b_{3}$. The second derivative is positive and $x_{1}=4 / 3$ is a global minimum.

We will show below the following results, valid for any $m, n \in \mathbb{N}, \boldsymbol{A} \in \mathbb{C}^{m \times n}$ and $\boldsymbol{b} \in \mathbb{C}^{n}$.

Theorem 9.1 (Existence) The least squares problem always has a solution.
Theorem 9.2 (Uniqueness) The solution of the least squares problem is unique if and only if $\boldsymbol{A}$ has linearly independent columns.

Theorem 9.3 (Characterization) $\boldsymbol{x} \in \mathbb{C}^{n}$ is a solution of the least squares problem if and only if $\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{*} \boldsymbol{b}$.

The linear system $\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{*} \boldsymbol{b}$ is known as the normal equations. By Lemma 4.2 the coefficient matrix $\boldsymbol{A}^{*} \boldsymbol{A}$ is symmetric and positive semidefinite, and it is positive definite if and only if $\boldsymbol{A}$ has linearly independent columns. This is the same condition which guarantees that the least squares problem has a unique solution.

### 9.1 Examples

Example 9.2 (Linear Regression) We want to fit a straight line $p(t)=x_{1}+x_{2} t$ to $m \geq 2$ given data $\left(t_{k}, y_{k}\right) \in \mathbb{R}^{2}, k=1, \ldots, m$. This is part of the linear regression process in statistics. We obtain the linear system

$$
\boldsymbol{A} \boldsymbol{x}=\left[\begin{array}{c}
p\left(t_{1}\right) \\
\vdots \\
p\left(t_{m}\right)
\end{array}\right]=\left[\begin{array}{ll}
1 & t_{1} \\
\vdots \\
1 & t_{m}
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{c}
y_{1} \\
\vdots \\
y_{m}
\end{array}\right]=\boldsymbol{b} .
$$

This is square for $m=2$ and overdetermined for $m>2$. The matrix $\boldsymbol{A}$ has linearly independent columns if and only if the set $\left\{t_{1}, \ldots, t_{m}\right\}$ of sites contains at least two distinct elements. For if say $t_{i} \neq t_{j}$ then

$$
c_{1}\left[\begin{array}{c}
1 \\
\vdots \\
1
\end{array}\right]+c_{2}\left[\begin{array}{c}
t_{1} \\
\vdots \\
t_{m}
\end{array}\right]=\left[\begin{array}{c}
0 \\
\vdots \\
0
\end{array}\right] \Longrightarrow\left[\begin{array}{cc}
1 & t_{i} \\
1 & t_{j}
\end{array}\right]\left[\begin{array}{c}
c_{1} \\
c_{2}
\end{array}\right]=\left[\begin{array}{c}
0 \\
0
\end{array}\right] \Longrightarrow c_{1}=c_{2}=0 .
$$

Conversely, if $t_{1}=\cdots=t_{m}$ then the columns of $\boldsymbol{A}$ are linearly dependent. The normal equations are

$$
\begin{aligned}
\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x} & =\left[\begin{array}{ccc}
1 & \cdots & 1 \\
t_{1} & \cdots & t_{m}
\end{array}\right]\left[\begin{array}{c}
1 \\
\vdots \\
1 \\
1 \\
m
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{cc}
m & \sum t_{k} \\
\sum t_{k} & \sum t_{k}^{2}
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right], \\
& =\left[\begin{array}{ccc}
1 & \cdots & 1 \\
t_{1} & \cdots & t_{m}
\end{array}\right]\left[\begin{array}{c}
y_{1} \\
\vdots \\
y_{m}
\end{array}\right]=\left[\begin{array}{c}
\sum y_{k} \\
\sum t_{k} y_{k}
\end{array}\right]=\boldsymbol{A}^{*} \boldsymbol{b},
\end{aligned}
$$

where $k$ ranges from 1 to $m$ in the sums. By what we showed the coefficient matrix is positive semidefinite and positive definite if we have at least two distinct cites. If $m=2$ and $t_{1} \neq t_{2}$ then both systems $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ and $\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{*} \boldsymbol{b}$ are square, and $p$ is the linear interpolant to the data. Indeed, $p$ is linear and $p\left(t_{k}\right)=y_{k}, k=1,2$.

With the data

$$
\begin{array}{c|c|c|c|c}
t & 1.0 & 2.0 & 3.0 & 4.0 \\
\hline y & 3.1 & 1.8 & 1.0 & 0.1
\end{array}
$$

the normal equations become $\left[\begin{array}{cc}4 & 10 \\ 10 & 30\end{array}\right]\left[\begin{array}{l}x_{1} \\ x_{2}\end{array}\right]=\left[\begin{array}{c}6 \\ 10.1\end{array}\right]$. The data and the least squares polynomial $p(t)=x_{1}+x_{2} t=3.95-0.98 t$ are shown in Fig. 9.1.

Example 9.3 (Input/Output Model) Suppose we have a simple input/output model. To every input $\boldsymbol{u} \in \mathbb{R}^{n}$ we obtain an output $y \in \mathbb{R}$. Assuming we have a linear relation

$$
y=\boldsymbol{u}^{*} \boldsymbol{x}=\sum_{i=1}^{n} u_{i} x_{i},
$$

Fig. 9.1 A least squares fit to data
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-215.jpg?height=543&width=636&top_left_y=1546&top_left_x=706)

between $\boldsymbol{u}$ and $y$, how can we determine $\boldsymbol{x}$ ?
Performing $m \geq n$ experiments we obtain a table of values

$$
\begin{array}{c|c|c|c|c}
\boldsymbol{u} & \boldsymbol{u}_{1} & \boldsymbol{u}_{2} & \cdots & \boldsymbol{u}_{m} \\
\hline \hline & y_{1} & y_{2} & \cdots & y_{m}
\end{array} .
$$

We would like to find $\boldsymbol{x}$ such that

$$
\boldsymbol{A} \boldsymbol{x}=\left[\begin{array}{c}
\boldsymbol{u}_{1}^{*} \\
\boldsymbol{u}_{2}^{*} \\
\vdots \\
\boldsymbol{u}_{m}^{*}
\end{array}\right] \boldsymbol{x}=\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{m}
\end{array}\right]=\boldsymbol{b} .
$$

We can estimate $\boldsymbol{x}$ by solving the least squares problem $\min \|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}^{2}$.

### 9.1.1 Curve Fitting

Given

- size: $1 \leq n \leq m$,
- sites: $\mathcal{S}:=\left\{t_{1}, t_{2}, \ldots, t_{m}\right\} \subset[a, b]$,
- $y$-values: $\boldsymbol{y}=\left[y_{1}, y_{2}, \ldots, y_{m}\right]^{*} \in \mathbb{R}^{m}$,
- functions: $\phi_{j}:[a, b] \rightarrow \mathbb{R}, j=1, \ldots, n$.

Find a function (curve fit) $p:[a, b] \rightarrow \mathbb{R}$ given by $p:=\sum_{j=1}^{n} x_{j} \phi_{j}$ such that $p\left(t_{k}\right) \approx y_{k}$ for $k=1, \ldots, m$.

A solution to the curve fitting problem is found by finding an approximate solution to the following overdetermined set of linear equations

$$
\boldsymbol{A} \boldsymbol{x}=\left[\begin{array}{c}
p\left(t_{1}\right) \\
\vdots \\
p\left(t_{m}\right)
\end{array}\right]=\left[\begin{array}{ccc}
\phi_{1}\left(t_{1}\right) & \cdots & \phi_{n}\left(t_{1}\right) \\
\vdots & & \vdots \\
\phi_{1}\left(t_{m}\right) & \cdots & \phi_{n}\left(t_{m}\right)
\end{array}\right]\left[\begin{array}{c}
x_{1} \\
\vdots \\
x_{n}
\end{array}\right]=\left[\begin{array}{c}
y_{1} \\
\vdots \\
y_{m}
\end{array}\right]=: \boldsymbol{b} .
$$

We propose to find $\boldsymbol{x} \in \mathbb{R}^{n}$ as a solution of the corresponding least squares problem given by

$$
E(\boldsymbol{x}):=\|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}^{2}=\sum_{k=1}^{m}\left(\sum_{j=1}^{n} x_{j} \phi_{j}\left(t_{k}\right)-y_{k}\right)^{2} .
$$

Typical examples of functions $\phi_{j}$ are polynomials, trigonometric functions, exponential functions, or splines.

In (9.2) one can also include weights $w_{k}>0$ for $k=1, \ldots, m$ and minimize

$$
E(\boldsymbol{x}):=\sum_{k=1}^{m} w_{k}\left(\sum_{j=1}^{n} x_{j} \phi_{j}\left(t_{k}\right)-y_{k}\right)^{2} .
$$

If $y_{k}$ is an accurate observation, we can choose a large weight $w_{k}$. This will force $p\left(t_{k}\right)-y_{k}$ to be small. Similarly, a small $w_{k}$ will allow $p\left(t_{k}\right)-y_{k}$ to be large. If an estimate for the standard deviation $\delta y_{k}$ in $y_{k}$ is known for each $k$, we can choose $w_{k}=1 /\left(\delta y_{k}\right)^{2}, k=1,2, \ldots, m$. For simplicity we will assume in the following that $w_{k}=1$ for all $k$.

Lemma 9.1 (Curve Fitting) Let $\boldsymbol{A}$ be given by (9.1). The matrix $\boldsymbol{A}^{*} \boldsymbol{A}$ is symmetric positive definite if and only if

$$
p\left(t_{k}\right):=\sum_{j=1}^{n} x_{j} \phi_{j}\left(t_{k}\right)=0, \quad k=1, \ldots, m \Rightarrow x_{1}=\cdots=x_{n}=0 .
$$

Proof By Lemma $4.2 \boldsymbol{A}^{*} \boldsymbol{A}$ is positive definite if and only if $\boldsymbol{A}$ has linearly independent columns. Since $(\boldsymbol{A} \boldsymbol{x})_{k}=\sum_{j=1}^{n} x_{j} \phi_{j}\left(t_{k}\right), k=1, \ldots, m$ this is equivalent to (9.3). $\square$

Example 9.4 (Ill Conditioning and the Hilbert Matrix) The normal equations can be extremely ill-conditioned. Consider the curve fitting problem using the polynomials $\phi_{j}(t):=t^{j-1}$, for $j=1, \ldots, n$ and equidistant sites $t_{k}=(k-1) /(m-1)$ for $k=1, \ldots, m$. The normal equations are $\boldsymbol{B}_{n} \boldsymbol{x}=\boldsymbol{c}_{n}$, where for $n=3$

$$
\boldsymbol{B}_{3} \boldsymbol{x}:=\left[\begin{array}{ccc}
m & \sum t_{k} & \sum t_{k}^{2} \\
\sum t_{k} & \sum t_{k}^{2} & \sum t_{k}^{3} \\
\sum t_{k}^{2} & \sum t_{k}^{3} & \sum t_{k}^{4}
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right]=\left[\begin{array}{c}
\sum y_{k} \\
\sum t_{k} y_{k} \\
\sum t_{k}^{2} y_{k}
\end{array}\right] .
$$

$\boldsymbol{B}_{n}$ is positive definite if at least $n$ of the $t$ 's are distinct. However $\boldsymbol{B}_{n}$ is extremely ill-conditioned even for moderate $n$. Indeed, $\frac{1}{m} \boldsymbol{B}_{n} \approx \boldsymbol{H}_{n}$, where $\boldsymbol{H}_{n} \in \mathbb{R}^{n \times n}$ is the Hilbert Matrix with $i, j$ element $1 /(i+j-1)$. Thus, for $n=3$

$$
\boldsymbol{H}_{3}=\left[\begin{array}{lll}
1 & \frac{1}{2} & \frac{1}{3} \\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4} \\
\frac{1}{3} & \frac{1}{4} & \frac{1}{5}
\end{array}\right] .
$$

The elements of $\frac{1}{m} \boldsymbol{B}_{n}$ are Riemann sums approximations to the elements of $\boldsymbol{H}_{n}$. In fact, if $\boldsymbol{B}_{n}=\left[b_{i, j}\right]_{i, j=1}^{n}$ then

$$
\begin{aligned}
\frac{1}{m} b_{i, j} & =\frac{1}{m} \sum_{k=1}^{m} t_{k}^{i+j-2}=\frac{1}{m} \sum_{k=1}^{m}\left(\frac{k-1}{m-1}\right)^{i+j-2} \\
& \approx \int_{0}^{1} x^{i+j-2} d x=\frac{1}{i+j-1}=h_{i, j}
\end{aligned}
$$

The elements of $\boldsymbol{H}_{n}^{-1}$ are determined in Exercise 1.13. We find $K_{1}\left(\boldsymbol{H}_{6}\right):=$ $\left\|\boldsymbol{H}_{6}\right\|_{1}\left\|\boldsymbol{H}_{6}^{-1}\right\|_{1} \approx 3 \cdot 10^{7}$. It appears that $\frac{1}{m} \boldsymbol{B}_{n}$ and hence $\boldsymbol{B}_{n}$ is ill-conditioned for moderate $n$ at least if $m$ is large. The cure for this problem is to use a different basis for polynomials. Orthogonal polynomials are an excellent choice. Another possibility is to use the shifted power basis $(t-\tilde{t})^{j-1}, j=1, \ldots, n$, for a suitable $\tilde{t}$.

### 9.2 Geometric Least Squares Theory

The least squares problem can be studied as a quadratic minimization problem. In the real case we have

$$
E(\boldsymbol{x}):=\|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}^{2}=(\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b})^{*}(\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b})=\boldsymbol{x}^{*} \boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}-2 \boldsymbol{x}^{*} \boldsymbol{A}^{*} \boldsymbol{b}+\boldsymbol{b}^{*} \boldsymbol{b} .
$$

Minimization of a quadratic function like $E(\boldsymbol{x})$ will be considered in Chap. 13. Here we consider a geometric approach based on orthogonal sums of subspaces, cf. Sect. 5.1.3.

With the usual inner product $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\boldsymbol{y}^{*} \boldsymbol{x}$, orthogonal sums and projections we can prove the existence, uniqueness and characterization theorems for least squares problems. For $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ we consider the column space $\mathcal{S}:=\mathcal{R}(\boldsymbol{A})$ of $\boldsymbol{A}$ and the null space $\mathcal{T}:=\mathcal{N}\left(\boldsymbol{A}^{*}\right)$ of $\boldsymbol{A}^{*}$. These are subspaces of $\mathbb{C}^{m}$ and by Theorem 7.3 we have the orthogonal sum

$$
\mathbb{C}^{m}=\mathcal{R}(\boldsymbol{A}) \stackrel{\perp}{\oplus} \mathcal{N}\left(\boldsymbol{A}^{*}\right) .
$$

Proof of Theorem 9.1 It follows from (9.4) that any $\boldsymbol{b} \in \mathbb{C}^{m}$ can be decomposed uniquely as $\boldsymbol{b}=\boldsymbol{b}_{1}+\boldsymbol{b}_{2}$, where $\boldsymbol{b}_{1}$ is the orthogonal projection of $\boldsymbol{b}$ into $\mathcal{R}(\boldsymbol{A})$ and $\boldsymbol{b}_{2}$ is the orthogonal projection of $\boldsymbol{b}$ into $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$. Suppose $\boldsymbol{x} \in \mathbb{C}^{n}$. Clearly $\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}_{1} \in \mathcal{R}(\boldsymbol{A})$ since it is a subspace and $\boldsymbol{b}_{2} \in \mathcal{N}\left(\boldsymbol{A}^{*}\right)$. But then $\left\langle\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}_{1}, \boldsymbol{b}_{2}\right\rangle=0$ and by Pythagoras

$$
\|A x-b\|_{2}^{2}=\left\|\left(A x-b_{1}\right)-b_{2}\right\|_{2}^{2}=\left\|A x-b_{1}\right\|_{2}^{2}+\left\|b_{2}\right\|_{2}^{2} \geq\left\|b_{2}\right\|_{2}^{2}
$$

with equality if and only if $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}_{1}$. It follows that the set of all least squares solutions is

$$
\left\{\boldsymbol{x} \in \mathbb{C}^{n}: \boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}_{1}\right\} .
$$

This set is nonempty since $\boldsymbol{b}_{1} \in \mathcal{R}(\boldsymbol{A})$. $\square$

Proof of Theorem 9.2 The set (9.5) contains exactly one element if and only if $\boldsymbol{A}$ has linearly independent columns. $\square$

Proof of Theorem 9.3 If $\boldsymbol{x}$ solves the least squares problem then $\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}_{1}=\mathbf{0}$ and it follows that $\boldsymbol{A}^{*}(\boldsymbol{A x}-\boldsymbol{b})=\boldsymbol{A}^{*}\left(\boldsymbol{A x}-\boldsymbol{b}_{1}\right)=\mathbf{0}$ since $\boldsymbol{b}_{2} \in \mathcal{N}\left(\boldsymbol{A}^{*}\right)$. This shows that the normal equations hold. Conversely, if $\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{*} \boldsymbol{b}$ then $\boldsymbol{A}^{*} \boldsymbol{b}_{2}=\mathbf{0}$ implies that $\boldsymbol{A}^{*}\left(\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}_{1}\right)=\mathbf{0}$. But then $\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}_{1} \in \mathcal{R}(\boldsymbol{A}) \cap \mathcal{N}\left(\boldsymbol{A}^{*}\right)$ showing that $\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}_{1}=\mathbf{0}$, and $\boldsymbol{x}$ is a least squares solution. $\square$

### 9.3 Numerical Solution

We assume that $m \geq n, \boldsymbol{A} \in \mathbb{C}^{m \times n}, \boldsymbol{b} \in \mathbb{C}^{m}$. We consider numerical methods based on normal equations, QR factorization, or Singular Value Factorization. For more see [2]. We discuss the first two approaches in this section. Another possibility is to use an iterative method like the conjugate gradient method (cf. Exercise 13.10).

### 9.3.1 Normal Equations

We assume that $\operatorname{rank}(\boldsymbol{A})=n$, i.e., $\boldsymbol{A}$ has linearly independent columns. The coefficient matrix $\boldsymbol{B}:=\boldsymbol{A}^{*} \boldsymbol{A}$ in the normal equations is positive definite, and we can solve these equations using the Cholesky factorization of $\boldsymbol{B}$. Consider forming the normal equations. We can use either a column oriented (inner product)- or a row oriented (outer product) approach.

1. inner product: $\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)_{i, j}=\sum_{k=1}^{m} \bar{a}_{k, i} a_{k, j}, i, j=1, \ldots, n$,
$$
\left(\boldsymbol{A}^{*} \boldsymbol{b}\right)_{i}=\sum_{k=1}^{m} \bar{a}_{k, i} b_{k}, i=1, \ldots, n,
$$
2. outer product: $\boldsymbol{A}^{*} \boldsymbol{A}=\sum_{k=1}^{m}\left[\begin{array}{c}\bar{a}_{k, 1} \\ \vdots \\ \bar{a}_{k, n}\end{array}\right]\left[a_{k 1} \cdots a_{k n}\right], \boldsymbol{A}^{*} \boldsymbol{b}=\sum_{k=1}^{m}\left[\begin{array}{c}\bar{a}_{k, 1} \\ \vdots \\ \bar{a}_{k, n}\end{array}\right] b_{k}$.

The outer product form is suitable for large problems since it uses only one pass through the data importing one row of $\boldsymbol{A}$ at a time from some separate storage.

Consider the number of operations to find the least squares solution for real data. We need $2 m$ arithmetic operations for each inner product. Since $\boldsymbol{B}$ is symmetric we only need to compute $n(n+1) / 2$ such inner products. It follows that $\boldsymbol{B}$ can be computed in approximately $m n^{2}$ arithmetic operations. In conclusion the number
of operations are $m n^{2}$ to find $\boldsymbol{B}, 2 m n$ to find $\boldsymbol{c}:=\boldsymbol{A}^{*} \boldsymbol{b}, n^{3} / 3$ to find $\boldsymbol{L}$ such that $\boldsymbol{B}=\boldsymbol{L} \boldsymbol{L}^{*}, n^{2}$ to solve $\boldsymbol{L} \boldsymbol{y}=\boldsymbol{c}$ and $n^{2}$ to solve $\boldsymbol{L}^{*} \boldsymbol{x}=\boldsymbol{y}$. If $m \approx n$ it takes $\frac{4}{3} n^{3}=$ $2 G_{n}$ arithmetic operations. If $m$ is much bigger than $n$ the number of operations is approximately $m n^{2}$, the work to compute $\boldsymbol{B}$.

Conditioning of $\boldsymbol{A}$ can be a problem with the normal equation approach. We have
Theorem 9.4 (Spectral Condition Number of $\boldsymbol{A}^{*} \boldsymbol{A}$ ) Suppose $1 \leq n \leq m$ and that $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has linearly independent columns. Then

$$
K_{2}\left(\boldsymbol{A}^{*} \boldsymbol{A}\right):=\left\|\boldsymbol{A}^{*} \boldsymbol{A}\right\|_{2}\left\|\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)^{-1}\right\|_{2}=\frac{\lambda_{1}}{\lambda_{n}}=\frac{\sigma_{1}^{2}}{\sigma_{n}^{2}}=K_{2}(\boldsymbol{A})^{2},
$$

where $\lambda_{1} \geq \cdots \geq \lambda_{n}>0$ are the eigenvalues of $\boldsymbol{A}^{*} \boldsymbol{A}$, and $\sigma_{1} \geq \cdots \geq \sigma_{n}>0$ are the singular values of $\boldsymbol{A}$.

Proof Since $\boldsymbol{A}^{*} \boldsymbol{A}$ is Hermitian it follows from Theorem 8.10 that $K_{2}(\boldsymbol{A})=\frac{\sigma_{1}}{\sigma_{n}}$ and $K_{2}\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)=\frac{\lambda_{1}}{\lambda_{n}}$. But $\lambda_{i}=\sigma_{i}^{2}$ by Theorem 7.2 and the proof is complete. $\square$

It follows from Theorem 9.4 that the 2-norm condition number of $\boldsymbol{B}:=\boldsymbol{A}^{*} \boldsymbol{A}$ is the square of the condition number of $\boldsymbol{A}$ and therefore can be quite large even if $\boldsymbol{A}$ is only mildly ill-conditioned. Another difficulty which can be encountered is that the computed $\boldsymbol{A}^{*} \boldsymbol{A}$ might not be positive definite. See Problem 9.21 for an example.

### 9.3.2 QR Factorization

The QR factorization can be used to solve the least squares problem. We assume that $\operatorname{rank}(\boldsymbol{A})=n$, i.e., $\boldsymbol{A}$ has linearly independent columns. Suppose $\boldsymbol{A}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$ is a QR factorization of $\boldsymbol{A}$. Since $\boldsymbol{Q}_{1} \in \mathbb{C}^{m \times n}$ has orthonormal columns we find

$$
\boldsymbol{A}^{*} \boldsymbol{A}=\boldsymbol{R}_{1}^{*} \boldsymbol{Q}_{1}^{*} \boldsymbol{Q}_{1} \boldsymbol{R}_{1}=\boldsymbol{R}_{1}^{*} \boldsymbol{R}_{1}, \quad \boldsymbol{A}^{*} \boldsymbol{b}=\boldsymbol{R}_{1}^{*} \boldsymbol{Q}_{1}^{*} \boldsymbol{b} .
$$

Since $\boldsymbol{A}$ has rank $n$ the matrix $\boldsymbol{R}_{1}^{*}$ is nonsingular and can be canceled. Thus

$$
\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{*} \boldsymbol{b} \Longrightarrow \boldsymbol{R}_{1} \boldsymbol{x}=\boldsymbol{c}_{1}, \quad \boldsymbol{c}_{1}:=\boldsymbol{Q}_{1}^{*} \boldsymbol{b} .
$$

We can use Householder transformations or Givens rotations to find $\boldsymbol{R}_{1}$ and $\boldsymbol{c}_{1}$. Consider using the Householder triangulation algorithm Algorithm 5.2. We find $\boldsymbol{R}=\boldsymbol{Q}^{*} \boldsymbol{A}$ and $\boldsymbol{c}=\boldsymbol{Q}^{*} \boldsymbol{b}$, where $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ is the QR decomposition of $\boldsymbol{A}$. The matrices $\boldsymbol{R}_{1}$ and $\boldsymbol{c}_{1}$ are located in the first $n$ rows of $\boldsymbol{R}$ and $\boldsymbol{c}$. Using also Algorithm 3.2 we have the following method to solve the full rank least squares problem.

1. $[\mathrm{R}, \mathrm{c}]=$ housetriang (A, b) .
2. x=rbacksolve (R(1:n,1:n),c(1:n),n).

Example 9.5 (Solution Using QR Factorization) Consider the least squares problem with

$$
\boldsymbol{A}=\left[\begin{array}{ccc}
1 & 3 & 1 \\
1 & 3 & 7 \\
1 & -1 & -4 \\
1 & -1 & 2
\end{array}\right] \text { and } \boldsymbol{b}=\left[\begin{array}{l}
1 \\
1 \\
1 \\
1
\end{array}\right] .
$$

This is the matrix in Example 5.2. The least squares solution $\boldsymbol{x}$ is found by solving the system

$$
\left[\begin{array}{lll}
2 & 2 & 3 \\
0 & 4 & 5 \\
0 & 0 & 6
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right]=\frac{1}{2}\left[\begin{array}{rrcr}
1 & 1 & 1 & 1 \\
1 & 1 & -1 & -1 \\
-1 & 1 & -1 & 1
\end{array}\right] \times\left[\begin{array}{l}
1 \\
1 \\
1 \\
1
\end{array}\right]=\left[\begin{array}{l}
2 \\
0 \\
0
\end{array}\right],
$$

and we find $\boldsymbol{x}=[1,0,0]^{*}$.
Using Householder triangulation is a useful alternative to normal equations for solving full rank least squares problems. It can even be extended to rank deficient problems, see [2]. The 2 norm condition number for the system $\boldsymbol{R}_{1} \boldsymbol{x}=\boldsymbol{c}_{1}$ is $K_{2}\left(\boldsymbol{R}_{1}\right)=K_{2}\left(\boldsymbol{Q}_{1} \boldsymbol{R}_{1}\right)=K_{2}(\boldsymbol{A})$, and as discussed in the previous section this is the square root of $K_{2}\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)$, the condition number for the normal equations. Thus if $\boldsymbol{A}$ is mildly ill-conditioned the normal equations can be quite ill-conditioned and solving the normal equations can give inaccurate results. On the other hand Algorithm 5.2 is quite stable.

But using Householder transformations requires more work. The leading term in the number of arithmetic operations in Algorithm 5.2 is approximately $2 m n^{2}-$ $2 n^{3} / 3$, (cf. (5.16)) while the number of arithmetic operations needed to form the normal equations, taking advantage of symmetry is approximately $m n^{2}$. Thus for $m$ much larger than $n$ using Householder triangulation requires twice as many arithmetic operations as the approach based on the normal equations. Also, Householder triangulation have problems taking advantage of the structure in sparse problems.

Using MATLAB a least squares solution can be found using $\mathrm{x}=\mathrm{A} \backslash \mathrm{b}$ if $\boldsymbol{A}$ has full rank.For rank deficient problems the function $\mathrm{x}=\operatorname{lscov}(\mathrm{A}, \mathrm{b})$ finds a least squares solution with a maximal number of zeros in $\boldsymbol{x}$.

### 9.3.3 Singular Value Decomposition, Generalized Inverses and Least Squares

Further insight into the least squares problem can be obtained by considering a singular value decomposition of $\boldsymbol{A}$ and the corresponding singular value factorization.

If $\boldsymbol{A}$ has rank $r$ then

$$
\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*}=\left[\boldsymbol{U}_{1}, \boldsymbol{U}_{2}\right]\left[\begin{array}{cc}
\boldsymbol{\Sigma}_{1} & \mathbf{0} \\
\mathbf{0} & \mathbf{0}
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{V}_{1}^{*} \\
\boldsymbol{V}_{2}^{*}
\end{array}\right]=\boldsymbol{U}_{1} \boldsymbol{\Sigma}_{1} \boldsymbol{V}_{1}^{*}, \quad \boldsymbol{\Sigma}_{1}=\operatorname{diag}\left(\sigma_{1}, \ldots, \sigma_{r}\right),
$$

where

$$
\begin{array}{ll}
\boldsymbol{U}_{1}=\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}\right], & \boldsymbol{U}_{2}=\left[\boldsymbol{u}_{r+1}, \ldots, \boldsymbol{u}_{m}\right], \\
\boldsymbol{V}_{1}=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{r}^{*}\right], & \boldsymbol{V}_{2}=\left[\boldsymbol{v}_{r+1}, \ldots, \boldsymbol{v}_{n}\right],
\end{array} \quad \begin{aligned}
& \boldsymbol{V}_{1}^{*} \boldsymbol{V}_{1}=\boldsymbol{I}, \quad \boldsymbol{V}_{2}^{*} \boldsymbol{V}_{2}=\boldsymbol{I},
\end{aligned}
$$

and $\sigma_{1} \geq \cdots \geq \sigma_{r}>0$. We recall (cf. Theorem 7.3)

- the set of columns of $\boldsymbol{U}_{1}$ is an orthonormal basis for $\mathcal{R}(\boldsymbol{A})$,
- the set of columns of $\boldsymbol{U}_{2}$ is an orthonormal basis for $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$,
- the set of columns of $\boldsymbol{V}_{1}$ is an orthonormal basis for $\mathcal{R}\left(\boldsymbol{A}^{*}\right)$,
- the set of columns of $\boldsymbol{V}_{2}$ is an orthonormal basis for $\mathcal{N}(\boldsymbol{A})$.

The concept of the inverse of a matrix can be generalized to any rectangular matrix.

Theorem 9.5 (The Generalized Inverse) For any $m, n \in \mathbb{N}$ and any $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ there is a unique matrix $\boldsymbol{A}^{\dagger} \in \mathbb{C}^{n \times m}$ such that

$$
\boldsymbol{A} \boldsymbol{A}^{\dagger} \boldsymbol{A}=\boldsymbol{A}, \boldsymbol{A}^{\dagger} \boldsymbol{A} \boldsymbol{A}^{\dagger}=\boldsymbol{A}^{\dagger},\left(\boldsymbol{A}^{\dagger} \boldsymbol{A}\right)^{*}=\boldsymbol{A}^{\dagger} \boldsymbol{A},\left(\boldsymbol{A} \boldsymbol{A}^{\dagger}\right)^{*}=\boldsymbol{A} \boldsymbol{A}^{\dagger} .
$$

If $\boldsymbol{U}_{1} \boldsymbol{\Sigma}_{1} \boldsymbol{V}_{1}^{*}$ is a singular value factorization of $\boldsymbol{A}$ then

$$
\boldsymbol{A}^{\dagger}=\boldsymbol{V}_{1} \boldsymbol{\Sigma}_{1}^{-1} \boldsymbol{U}_{1}^{*} .
$$

Proof For existence we show that the matrices

$$
A=U_{1} \Sigma_{1} V_{1}^{*}, \quad A^{\dagger}:=V_{1} \Sigma_{1}^{-1} U_{1}^{*}
$$

satisfies (9.8). Since $\boldsymbol{U}_{1}$ and $\boldsymbol{V}_{1}$ have orthonormal columns we find

$$
\begin{aligned}
& A^{\dagger} A=V_{1} \Sigma_{1}^{-1} U_{1}^{*} U_{1} \Sigma_{1} V_{1}^{*}=V_{1} V_{1}^{*} \\
& A A^{\dagger}=U_{1} \Sigma_{1} V_{1}^{*} V_{1} \Sigma_{1}^{-1} U_{1}^{*}=U_{1} U_{1}^{*}
\end{aligned}
$$

A similar calculation shows that $\left(\boldsymbol{A}^{\dagger} \boldsymbol{A}\right)^{*}=\boldsymbol{V}_{1} \boldsymbol{V}_{1}^{*}$ and $\left(\boldsymbol{A} \boldsymbol{A}^{\dagger}\right)^{*}=\boldsymbol{U}_{1} \boldsymbol{U}_{1}^{*}$ showing that $\boldsymbol{A}^{\dagger} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{\dagger}$ are Hermitian. Moreover, by (9.10)

$$
\begin{aligned}
A A^{\dagger} A & =U_{1} \Sigma_{1} V_{1}^{*} V_{1} V_{1}^{*}=U_{1} \Sigma_{1} V_{1}^{*}=A \\
A^{\dagger} A A^{\dagger} & =V_{1} \Sigma_{1}^{-1} U_{1}^{*} U_{1} U_{1}^{*}=V_{1} \Sigma^{-1} U_{1}^{*}=A^{\dagger}
\end{aligned}
$$

Thus (9.8) follows.
That there is only one matrix $\boldsymbol{A}^{\dagger} \in \mathbb{C}^{n \times m}$ satisfying (9.8) is shown in Exercise 9.5. $\square$

The matrix $\boldsymbol{A}^{\dagger}$ is called the generalized inverse of $\boldsymbol{A}$. We note that

1. If $\boldsymbol{A}$ is square and nonsingular then $\boldsymbol{A}^{-1}$ satisfies (9.8) so that $\boldsymbol{A}^{-1}=\boldsymbol{A}^{\dagger}$. Indeed, $\boldsymbol{A}^{-1} \boldsymbol{A}=\boldsymbol{A} \boldsymbol{A}^{-1}=\boldsymbol{I}$ implies that $\boldsymbol{A}^{-1} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{A}^{-1}$ are Hermitian. Moreover, $\boldsymbol{A} \boldsymbol{A}^{-1} \boldsymbol{A}=\boldsymbol{A}, \boldsymbol{A}^{-1} \boldsymbol{A} \boldsymbol{A}^{-1}=\boldsymbol{A}^{-1}$. By uniqueness $\boldsymbol{A}^{-1}=\boldsymbol{A}^{\dagger}$.
2. We show in Exercise 9.7 that if $\boldsymbol{A}$ has linearly independent columns then
$$
\boldsymbol{A}^{\dagger}=\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)^{-1} \boldsymbol{A}^{*} .
$$
For further properties and examples of the generalized inverse see the exercises.
Orthogonal projections can be expressed in terms of generalized inverses and singular vectors.

Theorem 9.6 (Orthogonal Projections) Given $m, n \in \mathbb{N}, \boldsymbol{A} \in \mathbb{C}^{m \times n}$ of rank $r$, and let $\mathcal{S}$ be one of the subspaces $\mathcal{R}(\boldsymbol{A}), \mathcal{N}\left(\boldsymbol{A}^{*}\right)$. The orthogonal projection of $\boldsymbol{v} \in \mathbb{C}^{m}$ into $\mathcal{S}$ can be written as a matrix $\boldsymbol{P}_{\mathcal{S}}$ times the vector $\boldsymbol{v}$ in the form $\boldsymbol{P}_{\mathcal{S}} \boldsymbol{v}$, where

$$
\begin{gathered}
\boldsymbol{P}_{\mathcal{R}(\boldsymbol{A})}=\boldsymbol{A} \boldsymbol{A}^{\dagger}=\boldsymbol{U}_{1} \boldsymbol{U}_{1}^{*}=\sum_{j=1}^{r} \boldsymbol{u}_{j} \boldsymbol{u}_{j}^{*} \in \mathbb{C}^{m \times m}, \\
\boldsymbol{P}_{\mathcal{N}\left(\boldsymbol{A}^{*}\right)}=\boldsymbol{I}-\boldsymbol{A} \boldsymbol{A}^{\dagger}=\boldsymbol{U}_{2} \boldsymbol{U}_{2}^{*}=\sum_{j=r+1}^{m} \boldsymbol{u}_{j} \boldsymbol{u}_{j}^{*} \in \mathbb{C}^{m \times m} .
\end{gathered}
$$

where $\boldsymbol{A}^{\dagger}$ is the generalized inverse of $\boldsymbol{A}$, and $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*} \in \mathbb{C}^{m \times n}$ is a singular value decomposition of $\boldsymbol{A}$ (cf. (9.7)).

Proof By block multiplication we have for any $\boldsymbol{v} \in \mathbb{C}^{m}$

$$
\boldsymbol{v}=\boldsymbol{U} \boldsymbol{U}^{*} \boldsymbol{v}=\left[\boldsymbol{U}_{1}, \boldsymbol{U}_{2}\left[\begin{array}{l}
\boldsymbol{U}_{1}^{*} \\
\boldsymbol{U}_{2}^{*}
\end{array}\right] \boldsymbol{v}=\boldsymbol{s}+\boldsymbol{t},\right.
$$

where $\boldsymbol{s}=\boldsymbol{U}_{1} \boldsymbol{U}_{1}^{*} \boldsymbol{v} \in \mathcal{R}(\boldsymbol{A})$ and $\boldsymbol{t}=\boldsymbol{U}_{2} \boldsymbol{U}_{2}^{*} \boldsymbol{v} \in \mathcal{N}\left(\boldsymbol{A}^{*}\right)$. By uniqueness and (9.10) we obtain the first equation in (9.12). Since $\boldsymbol{v}=\left(\boldsymbol{U}_{1} \boldsymbol{U}_{1}^{*}+\boldsymbol{U}_{2} \boldsymbol{U}_{2}^{*}\right) \boldsymbol{v}$ for any $\boldsymbol{v} \in \mathbb{C}^{m}$ we have $\boldsymbol{U}_{1} \boldsymbol{U}_{1}^{*}+\boldsymbol{U}_{2} \boldsymbol{U}_{2}^{*}=\boldsymbol{I}$, and hence $\boldsymbol{U}_{2} \boldsymbol{U}_{2}^{*}=\boldsymbol{I}-\boldsymbol{U}_{1} \boldsymbol{U}_{1}^{*}=\boldsymbol{I}-\boldsymbol{A} \boldsymbol{A}^{\dagger}$ and the second equation in (9.12) follows. $\square$

Corollary 9.1 (LSQ Characterization Using Generalized Inverse) $\boldsymbol{x} \in \mathbb{C}^{n}$ solves the least squares problem $\min _{x}\|\boldsymbol{A} \boldsymbol{x}-b\|_{2}^{2}$ if and only if $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}+\boldsymbol{z}$, where $\boldsymbol{A}^{\dagger}$ is the generalized inverse of $\boldsymbol{A}$ and $\boldsymbol{z} \in \mathcal{N}(\boldsymbol{A})$.

Proof It follows from Theorem 9.6 that $\boldsymbol{b}_{1}:=\boldsymbol{A} \boldsymbol{A}^{\dagger} \boldsymbol{b}$ is the orthogonal projection of $\boldsymbol{b} \in \mathbb{C}^{m}$ into $\mathcal{R}(\boldsymbol{A})$. Moreover, (9.5) implies that $\boldsymbol{x}$ is a least squares solution if and only if $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}_{1}$.

Let $\boldsymbol{x}$ be a least squares solution, i.e., $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}_{1}$. If $\boldsymbol{z}:=\boldsymbol{x}-\boldsymbol{A}^{\dagger} \boldsymbol{b}$ then $\boldsymbol{A} \boldsymbol{z}=$ $\boldsymbol{A} \boldsymbol{x}-\boldsymbol{A} \boldsymbol{A}^{\dagger} \boldsymbol{b}=\boldsymbol{b}_{1}-\boldsymbol{b}_{1}=\mathbf{0}$ and $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}+\boldsymbol{z}$.

Conversely, if $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}+\boldsymbol{z}$ with $\boldsymbol{A} \boldsymbol{z}=\mathbf{0}$ then $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}\left(\boldsymbol{A}^{\dagger} \boldsymbol{b}+\boldsymbol{z}\right)=\boldsymbol{b}_{1}$ and $\boldsymbol{x}$ is a least squares solution. $\square$

The least squares solution $\boldsymbol{A}^{\dagger} \boldsymbol{b}$ has an interesting property.
Theorem 9.7 (Minimal Norm Solution) The least squares solution with minimal Euclidian norm is $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}$ corresponding to $\boldsymbol{z}=\mathbf{0}$.

Proof Consider a singular value decomposition of $\boldsymbol{A}$ using the notation in (9.7). Suppose $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}+\boldsymbol{z}$, with $\boldsymbol{z} \in \mathcal{N}(\boldsymbol{A})$. Since the columns of $\boldsymbol{V}_{2}$ form a basis for $\mathcal{N}(\boldsymbol{A})$ we have $\boldsymbol{z}=\boldsymbol{V}_{2} \boldsymbol{y}$ for some $\boldsymbol{y}$. Moreover, $\boldsymbol{V}_{2}^{*} \boldsymbol{V}_{1}=\mathbf{0}$ since $\boldsymbol{V}$ has orthonormal columns. But then $\boldsymbol{z}^{*} \boldsymbol{A}^{\dagger} \boldsymbol{b}=\boldsymbol{y}^{*} \boldsymbol{V}_{2}^{*} \boldsymbol{V}_{1} \boldsymbol{\Sigma}^{-1} \boldsymbol{U}_{1}^{*} \boldsymbol{b}=\mathbf{0}$. Thus $\boldsymbol{z}$ and $\boldsymbol{A}^{\dagger} \boldsymbol{b}$ are orthogonal so that by Pythagoras $\|\boldsymbol{x}\|_{2}^{2}=\left\|\boldsymbol{A}^{\dagger} \boldsymbol{b}+\boldsymbol{z}\right\|_{2}^{2}=\left\|\boldsymbol{A}^{\dagger} \boldsymbol{b}\right\|_{2}^{2}+\|\boldsymbol{z}\|_{2}^{2} \geq\left\|\boldsymbol{A}^{\dagger} \boldsymbol{b}\right\|_{2}^{2}$ with equality for $\boldsymbol{z}=\mathbf{0}$. $\square$

Example 9.6 (Rank Deficient Least Squares Solution) Consider the least squares problem with $\boldsymbol{A}=\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$ and $\boldsymbol{b}=[1,1]^{*}$. The singular value factorization, $\boldsymbol{A}^{\dagger}$ and $\boldsymbol{A}^{\dagger} \boldsymbol{b}$ are given by

$$
\boldsymbol{A}:=\frac{1}{\sqrt{2}}\left[\begin{array}{l}
1 \\
1
\end{array}\right][2] \frac{1}{\sqrt{2}}\left[\begin{array}{ll}
1 & 1
\end{array}\right], \boldsymbol{A}^{\dagger}=\frac{1}{\sqrt{2}}\left[\begin{array}{l}
1 \\
1
\end{array}\right]\left[\frac{1}{2}\right] \frac{1}{\sqrt{2}}\left[\begin{array}{ll}
1 & 1
\end{array}\right]=\frac{1}{4} \boldsymbol{A}, \boldsymbol{A}^{\dagger} \boldsymbol{b}=\left[\begin{array}{l}
1 / 2 \\
1 / 2
\end{array}\right] .
$$

Using Corollary 9.1 we find the general solution $[1 / 2,1 / 2]+[a,-a]$ for any $a \in \mathbb{C}$. The MATLAB function lscov gives the solution [1, 0] * corresponding to $a=1 / 2$, while the minimal norm solution is $[1 / 2,1 / 2]$ obtained for $a=0$.

### 9.4 Perturbation Theory for Least Squares

In this section we consider what effect small changes in the data $\boldsymbol{A}, \boldsymbol{b}$ have on the solution $\boldsymbol{x}$ of the least squares problem $\min \|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}$.

If $\boldsymbol{A}$ has linearly independent columns then we can write the least squares solution $\boldsymbol{x}$ (the solution of $\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{*} \boldsymbol{b}$ ) as (cf. Exercise 9.7)

$$
\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}=\boldsymbol{A}^{\dagger} \boldsymbol{b}_{1}, \quad \boldsymbol{A}^{\dagger}=\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)^{-1} \boldsymbol{A}^{*},
$$

where $\boldsymbol{b}_{1}$ is the orthogonal projection of $\boldsymbol{b}$ into the column space $\mathcal{R}(\boldsymbol{A})$.

### 9.4.1 Perturbing the Right Hand Side

Let us now consider the effect of a perturbation in $\boldsymbol{b}$ on $\boldsymbol{x}$.
Theorem 9.8 (Perturbing the Right Hand Side) Suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has linearly independent columns, and let $\boldsymbol{b}, \boldsymbol{e} \in \mathbb{C}^{m}$. Let $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{C}^{n}$ be the solutions of $\min \|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}$ and $\min \|\boldsymbol{A} \boldsymbol{y}-\boldsymbol{b}-\boldsymbol{e}\|_{2}$. Finally, let $\boldsymbol{b}_{1}, \boldsymbol{e}_{1}$ be the orthogonal projections of $\boldsymbol{b}$ and $\boldsymbol{e}$ into $\mathcal{R}(\boldsymbol{A})$. If $\boldsymbol{b}_{1} \neq \mathbf{0}$, we have for any operator norm

$$
\frac{1}{K(\boldsymbol{A})} \frac{\left\|\boldsymbol{e}_{1}\right\|}{\left\|\boldsymbol{b}_{1}\right\|} \leq \frac{\|\boldsymbol{y}-\boldsymbol{x}\|}{\|\boldsymbol{x}\|} \leq K(\boldsymbol{A}) \frac{\left\|\boldsymbol{e}_{1}\right\|}{\left\|\boldsymbol{b}_{1}\right\|}, \quad K(\boldsymbol{A})=\|\boldsymbol{A}\|\left\|\boldsymbol{A}^{\dagger}\right\| .
$$

Proof Subtracting $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}_{1}$ from $\boldsymbol{y}=\boldsymbol{A}^{\dagger} \boldsymbol{b}_{1}+\boldsymbol{A}^{\dagger} \boldsymbol{e}_{1}$ we have $\boldsymbol{y}-\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{e}_{1}$. Thus $\|\boldsymbol{y}-\boldsymbol{x}\|=\left\|\boldsymbol{A}^{\dagger} \boldsymbol{e}_{1}\right\| \leq\left\|\boldsymbol{A}^{\dagger}\right\|\left\|\boldsymbol{e}_{1}\right\|$. Moreover, $\left\|\boldsymbol{b}_{1}\right\|=\|\boldsymbol{A} \boldsymbol{x}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{x}\|$. Therefore $\|\boldsymbol{y}-\boldsymbol{x}\| /\|\boldsymbol{x}\| \leq\|\boldsymbol{A}\|\left\|\boldsymbol{A}^{\dagger}\right\|\left\|\boldsymbol{e}_{1}\right\| /\left\|\boldsymbol{b}_{1}\right\|$ proving the rightmost inequality. From $\boldsymbol{A}(\boldsymbol{x}-\boldsymbol{y})=\boldsymbol{e}_{1}$ and $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}_{1}$ we obtain the leftmost inequality. $\square$

Equation (9.13) is analogous to the bound (8.22) for linear systems. We see that the number $K(\boldsymbol{A})=\|\boldsymbol{A}\|\left\|\boldsymbol{A}^{\dagger}\right\|$ generalizes the condition number $\|\boldsymbol{A}\|\left\|\boldsymbol{A}^{-1}\right\|$ for a square matrix. The main difference between (9.13) and (8.22) is however that $\|\boldsymbol{e}\| /\|\boldsymbol{b}\|$ in (8.22) has been replaced by $\left\|\boldsymbol{e}_{1}\right\| /\left\|\boldsymbol{b}_{1}\right\|$, the orthogonal projections of $\boldsymbol{e}$ and $\boldsymbol{b}$ into $\mathcal{R}(\boldsymbol{A})$. If $\boldsymbol{b}$ lies almost entirely in $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$, i.e. $\|\boldsymbol{b}\| /\left\|\boldsymbol{b}_{1}\right\|$ is large, then $\left\|\boldsymbol{e}_{1}\right\| /\left\|\boldsymbol{b}_{1}\right\|$ can be much larger than $\|\boldsymbol{e}\| /\|\boldsymbol{b}\|$. This is illustrated in Fig. 9.2. If $\boldsymbol{b}$ is almost orthogonal to $\mathcal{R}(\boldsymbol{A})$, then $\left\|\boldsymbol{e}_{1}\right\| /\left\|\boldsymbol{b}_{1}\right\|$ will normally be much larger than $\|\boldsymbol{e}\| /\|\boldsymbol{b}\|$.

Example 9.7 (Perturbing the Right Hand Side) Suppose

$$
\boldsymbol{A}=\left[\begin{array}{ll}
1 & 1 \\
0 & 1 \\
0 & 0
\end{array}\right], \quad \boldsymbol{b}=\left[\begin{array}{c}
10^{-4} \\
0 \\
1
\end{array}\right], \quad \boldsymbol{e}=\left[\begin{array}{c}
10^{-6} \\
0 \\
0
\end{array}\right] .
$$

Fig. 9.2 Graphical interpretation of the bounds in Theorem 9.8
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-225.jpg?height=449&width=765&top_left_y=1559&top_left_x=575)

For this example we can compute $K(\boldsymbol{A})$ by finding $\boldsymbol{A}^{\dagger}$ explicitly. Indeed,

$$
\boldsymbol{A}^{*} \boldsymbol{A}=\left[\begin{array}{ll}
1 & 1 \\
1 & 2
\end{array}\right],\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)^{-1}=\left[\begin{array}{cc}
2 & -1 \\
-1 & 1
\end{array}\right], \boldsymbol{A}^{\dagger}=\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)^{-1} \boldsymbol{A}^{*}=\left[\begin{array}{ccc}
1 & -1 & 0 \\
0 & 1 & 0
\end{array}\right] .
$$

Thus $K_{\infty}(\boldsymbol{A})=\|\boldsymbol{A}\|_{\infty}\left\|\boldsymbol{A}^{\dagger}\right\|_{\infty}=2 \cdot 2=4$ is quite small.
Consider now the projections $\boldsymbol{b}_{1}$ and $\boldsymbol{e}_{1}$. We find $\boldsymbol{A} \boldsymbol{A}^{\dagger}=\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{array}\right]$. Hence

$$
\boldsymbol{b}_{1}=\boldsymbol{A} \boldsymbol{A}^{\dagger} \boldsymbol{b}=\left[10^{-4}, 0,0\right]^{*}, \quad \text { and } \quad \boldsymbol{e}_{1}=\boldsymbol{A} \boldsymbol{A}^{\dagger} \boldsymbol{e}=\left[10^{-6}, 0,0\right]^{*} .
$$

Thus $\left\|\boldsymbol{e}_{1}\right\|_{\infty} /\left\|\boldsymbol{b}_{1}\right\|_{\infty}=10^{-2}$ and (9.13) takes the form

$$
\frac{1}{4} 10^{-2} \leq \frac{\|\boldsymbol{y}-\boldsymbol{x}\|_{\infty}}{\|\boldsymbol{x}\|_{\infty}} \leq 4 \cdot 10^{-2} .
$$

To verify the bounds we compute the solutions as $\boldsymbol{x}=\boldsymbol{A}^{\dagger} \boldsymbol{b}=\left[10^{-4}, 0\right]^{*}$ and $\boldsymbol{y}=\boldsymbol{A}^{\dagger}(\boldsymbol{b}+\boldsymbol{e})=\left[10^{-4}+10^{-6}, 0\right]^{*}$. Hence

$$
\frac{\|\boldsymbol{x}-\boldsymbol{y}\|_{\infty}}{\|\boldsymbol{x}\|_{\infty}}=\frac{10^{-6}}{10^{-4}}=10^{-2}
$$

in agreement with (9.14)
For each $\boldsymbol{A}$ we can find $\boldsymbol{b}$ and $\boldsymbol{e}$ so that we have equality in the upper bound in (9.13). The lower bound is best possible in a similar way.

### 9.4.2 Perturbing the Matrix

The analysis of the effects of a perturbation $\boldsymbol{E}$ in $\boldsymbol{A}$ is quite difficult. The following result is stated without proof, see [12, p. 51]. For other estimates see [2] and [19].

Theorem 9.9 (Perturbing the Matrix) Suppose $\boldsymbol{A}, \boldsymbol{E} \in \mathbb{C}^{m \times n}, m>n$, where $\boldsymbol{A}$ has linearly independent columns and $\alpha:=1-\|\boldsymbol{E}\|_{2}\left\|\boldsymbol{A}^{\dagger}\right\|_{2}>0$. Then $\boldsymbol{A}+\boldsymbol{E}$ has linearly independent columns. Let $\boldsymbol{b}=\boldsymbol{b}_{1}+\boldsymbol{b}_{2} \in \mathbb{C}^{m}$ where $\boldsymbol{b}_{1}$ and $\boldsymbol{b}_{2}$ are the orthogonal projections into $\mathcal{R}(\boldsymbol{A})$ and $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$ respectively. Suppose $\boldsymbol{b}_{1} \neq \mathbf{0}$. Let $\boldsymbol{x}$ and $\boldsymbol{y}$ be the solutions of $\min \|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}$ and $\min \|(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{y}-\boldsymbol{b}\|_{2}$. Then

$$
\rho=\frac{\|\boldsymbol{x}-\boldsymbol{y}\|_{2}}{\|\boldsymbol{x}\|_{2}} \leq \frac{1}{\alpha} K(1+\beta K) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}}, \quad \beta=\frac{\left\|\boldsymbol{b}_{2}\right\|_{2}}{\left\|\boldsymbol{b}_{1}\right\|_{2}}, \quad K=\|\boldsymbol{A}\|_{2}\left\|\boldsymbol{A}^{\dagger}\right\|_{2} .
$$

Equation (9.15) says that the relative error in $\boldsymbol{y}$ as an approximation to $\boldsymbol{x}$ can be at most $K(1+\beta K) / \alpha$ times as large as the size $\|\boldsymbol{E}\|_{2} /\|\boldsymbol{A}\|_{2}$ of the relative perturbation
in $\boldsymbol{A} . \beta$ will be small if $\boldsymbol{b}$ lies almost entirely in $\mathcal{R}(\boldsymbol{A})$, and we have approximately $\rho \leq \frac{1}{\alpha} K\|\boldsymbol{E}\|_{2} /\|\boldsymbol{A}\|_{2}$. This corresponds to the estimate (8.25) for linear systems. If $\beta$ is not small, the term $\frac{1}{\alpha} K^{2} \beta\|\boldsymbol{E}\|_{2} /\|\boldsymbol{A}\|_{2}$ will dominate. In other words, the condition number is roughly $K(\boldsymbol{A})$ if $\beta$ is small and $K(\boldsymbol{A})^{2} \beta$ if $\beta$ is not small. Note that $\beta$ is large if $\boldsymbol{b}$ is almost orthogonal to $\mathcal{R}(\boldsymbol{A})$ and that $\boldsymbol{b}_{2}=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}$ is the residual of $\boldsymbol{x}$.

### 9.5 Perturbation Theory for Singular Values

In this section we consider what effect a small change in the matrix $\boldsymbol{A}$ has on the singular values.

### 9.5.1 The Minmax Theorem for Singular Values and the Hoffman-Wielandt Theorem

We have a minmax and maxmin characterization for singular values.
Theorem 9.10 (The Courant-Fischer Theorem for Singular Values) Suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has singular values $\sigma_{1}, \sigma_{2}, \ldots, \sigma_{n}$ ordered so that $\sigma_{1} \geq \cdots \geq \sigma_{n}$. Then for $k=1, \ldots, n$

$$
\sigma_{k}=\min _{\operatorname{dim}(\mathcal{S})=n-k+1} \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\ \boldsymbol{x} \neq \mathbf{0}}} \frac{\|\boldsymbol{A} \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}}=\max _{\operatorname{dim}(\mathcal{S})=k} \min _{\substack{\boldsymbol{x} \in \mathcal{S} \\ \boldsymbol{x} \neq \mathbf{0}}} \frac{\|\boldsymbol{A} \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} .
$$

Proof We have

$$
\frac{\|\boldsymbol{A} \boldsymbol{x}\|_{2}^{2}}{\|\boldsymbol{x}\|_{2}^{2}}=\frac{(\boldsymbol{A} \boldsymbol{x})^{*}(\boldsymbol{A} \boldsymbol{x})}{\boldsymbol{x}^{*} \boldsymbol{x}}=\frac{\boldsymbol{x}^{*} \boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}}{\boldsymbol{x}^{*} \boldsymbol{x}}=R_{\boldsymbol{A}^{*} \boldsymbol{A}}(\boldsymbol{x}),
$$

the Rayleigh quotient of $\boldsymbol{A}^{*} \boldsymbol{A}$. Since the singular values of $\boldsymbol{A}$ are the nonnegative square roots of the eigenvalues of $\boldsymbol{A}^{*} \boldsymbol{A}$, the results follow from the Courant-Fischer Theorem for eigenvalues, see Theorem 6.1. $\square$

By taking $k=1$ and $k=n$ in (9.16) we obtain for any $\boldsymbol{A} \in \mathbb{C}^{m \times n}$

$$
\sigma_{1}=\max _{\substack{\boldsymbol{x} \in \mathbb{C}^{n} \\ \boldsymbol{x} \neq \mathbf{0}}} \frac{\|\boldsymbol{A} \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}}, \quad \sigma_{n}=\min _{\substack{\boldsymbol{x} \in \mathbb{C}^{n} \\ \boldsymbol{x} \neq \mathbf{0}}} \frac{\|\boldsymbol{A} \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} .
$$

This follows since the only subspace of $\mathbb{C}^{n}$ of dimension $n$ is $\mathbb{C}^{n}$ itself.
Using Theorem 9.10 we obtain the following result.

Theorem 9.11 (Perturbation of Singular Values) Let $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{R}^{m \times n}$ be rectangular matrices with singular values $\alpha_{1} \geq \alpha_{2} \geq \cdots \geq \alpha_{n}$ and $\beta_{1} \geq \beta_{2} \geq \cdots \geq \beta_{n}$. Then

$$
\left|\alpha_{j}-\beta_{j}\right| \leq\|\boldsymbol{A}-\boldsymbol{B}\|_{2}, \text { for } j=1,2, \ldots, n .
$$

Proof Fix $j$ and let $\mathcal{S}$ be the $n-j+1$ dimensional subspace for which the minimum in Theorem 9.10 is obtained for $\boldsymbol{B}$. Then

$$
\begin{aligned}
\alpha_{j} & \leq \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\
\boldsymbol{x} \neq \mathbf{0}}} \frac{\|(\boldsymbol{B}+(\boldsymbol{A}-\boldsymbol{B})) \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} \leq \max _{\substack{\boldsymbol{x} \in \mathcal{S} \\
\boldsymbol{x} \neq \mathbf{0}}} \frac{\|\boldsymbol{B} \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}}+\max _{\substack{\boldsymbol{x} \in \mathcal{S} \\
\boldsymbol{x} \neq \mathbf{0}}} \frac{\|(\boldsymbol{A}-\boldsymbol{B}) \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} \\
& \leq \beta_{j}+\|\boldsymbol{A}-\boldsymbol{B}\|_{2} .
\end{aligned}
$$

By symmetry we obtain $\beta_{j} \leq \alpha_{j}+\|\boldsymbol{A}-\boldsymbol{B}\|_{2}$ and the proof is complete. $\square$

The following result is an analogue of Theorem 8.11.
Theorem 9.12 (Generalized Inverse When Perturbing the Matrix) Let $\boldsymbol{A}, \boldsymbol{E} \in$ $\mathbb{R}^{m \times n}$ have singular values $\alpha_{1} \geq \cdots \geq \alpha_{n}$ and $\epsilon_{1} \geq \cdots \geq \epsilon_{n}$. If $\operatorname{rank}(\boldsymbol{A}+\boldsymbol{E}) \leq$ $\operatorname{rank}(\boldsymbol{A})=r$ and $\left\|\boldsymbol{A}^{\dagger}\right\|_{2}\|\boldsymbol{E}\|_{2}<1$ then

1. $\operatorname{rank}(\boldsymbol{A}+\boldsymbol{E})=\operatorname{rank}(\boldsymbol{A})$,
2. $\left\|(\boldsymbol{A}+\boldsymbol{E})^{\dagger}\right\|_{2} \leq \frac{\left\|\boldsymbol{A}^{\dagger}\right\|_{2}}{1-\left\|\boldsymbol{A}^{\dagger}\right\|_{2}\|\boldsymbol{E}\|_{2}}=\frac{1}{\alpha_{r}-\epsilon_{1}}$.

Proof Suppose $\boldsymbol{A}$ has rank $r$ and let $\boldsymbol{B}:=\boldsymbol{A}+\boldsymbol{E}$ have singular values $\beta_{1} \geq$ $\cdots \geq \beta_{n}$. In terms of singular values the inequality $\left\|\boldsymbol{A}^{\dagger}\right\|_{2}\|\boldsymbol{E}\|_{2}<1$ can be written $\epsilon_{1} / \alpha_{r}<1$ or $\alpha_{r}>\epsilon_{1}$. By Theorem 9.11 we have $\alpha_{r}-\beta_{r} \leq\|\boldsymbol{E}\|_{2}=\epsilon_{1}$, which implies $\beta_{r} \geq \alpha_{r}-\epsilon_{1}>0$, and this shows that $\operatorname{rank}(\boldsymbol{A}+\boldsymbol{E}) \geq r$. Thus 1. follows. To prove 2., the inequality $\beta_{r} \geq \alpha_{r}-\epsilon_{1}$ implies that

$$
\left\|(\boldsymbol{A}+\boldsymbol{E})^{\dagger}\right\|_{2}=\frac{1}{\beta_{r}} \leq \frac{1}{\alpha_{r}-\epsilon_{1}}=\frac{1 / \alpha_{r}}{1-\epsilon_{1} / \alpha_{r}}=\frac{\left\|\boldsymbol{A}^{\dagger}\right\|_{2}}{1-\left\|\boldsymbol{A}^{\dagger}\right\|_{2}\|\boldsymbol{E}\|_{2}} .
$$ $\square$

The Hoffman-Wielandt Theorem, see Theorem 6.14, for eigenvalues of Hermitian matrices can be written

$$
\sum_{j=1}^{n}\left|\mu_{j}-\lambda_{j}\right|^{2} \leq\|\boldsymbol{A}-\boldsymbol{B}\|_{F}^{2}:=\sum_{i=1}^{n} \sum_{j=1}^{n}\left|a_{i j}-b_{i j}\right|^{2},
$$

where $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$ are both Hermitian matrices with eigenvalues $\lambda_{1} \geq \cdots \geq \lambda_{n}$ and $\mu_{1} \geq \cdots \geq \mu_{n}$, respectively.

For singular values we have a similar result.

Theorem 9.13 (Hoffman-Wielandt Theorem for Singular Values) For any $m, n \in \mathbb{N}$ and $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{m \times n}$ we have

$$
\sum_{j=1}^{n}\left|\beta_{j}-\alpha_{j}\right|^{2} \leq\|\boldsymbol{A}-\boldsymbol{B}\|_{F}^{2} .
$$

where $\alpha_{1} \geq \cdots \geq \alpha_{n}$ and $\beta_{1} \geq \cdots \geq \beta_{n}$ are the singular values of $\boldsymbol{A}$ and $\boldsymbol{B}$, respectively.

Proof We apply the Hoffman-Wielandt Theorem for eigenvalues to the Hermitian matrices

$$
\boldsymbol{C}:=\left[\begin{array}{cc}
\mathbf{0} & \boldsymbol{A} \\
\boldsymbol{A}^{*} & \mathbf{0}
\end{array}\right] \text { and } \boldsymbol{D}:=\left[\begin{array}{cc}
\mathbf{0} & \boldsymbol{B} \\
\boldsymbol{B}^{*} & \mathbf{0}
\end{array}\right] \in \mathbb{C}^{(m+n) \times(m+n)} .
$$

If $\boldsymbol{C}$ and $\boldsymbol{D}$ have eigenvalues $\lambda_{1} \geq \cdots \geq \lambda_{m+n}$ and $\mu_{1} \geq \cdots \geq \mu_{m+n}$, respectively then

$$
\sum_{j=1}^{m+n}\left|\lambda_{j}-\mu_{j}\right|^{2} \leq\|\boldsymbol{C}-\boldsymbol{D}\|_{F}^{2} .
$$

Suppose $\boldsymbol{A}$ has rank $r$ and $\operatorname{SVD}\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{m}\right] \boldsymbol{\Sigma}\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{n}\right]^{*}$. We use (7.7) and determine the eigenpairs of $\boldsymbol{C}$ as follows.

$$
\begin{aligned}
{\left[\begin{array}{cc}
\boldsymbol{0} & \boldsymbol{A} \\
\boldsymbol{A}^{*} & \boldsymbol{0}
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{u}_{i} \\
\boldsymbol{v}_{i}
\end{array}\right] } & =\left[\begin{array}{c}
\boldsymbol{A} \boldsymbol{v}_{i} \\
\boldsymbol{A}^{*} \boldsymbol{u}_{i}
\end{array}\right]=\left[\begin{array}{l}
\alpha_{i} \boldsymbol{u}_{i} \\
\alpha_{i} \boldsymbol{v}_{i}
\end{array}\right]=\alpha_{i}\left[\begin{array}{l}
\boldsymbol{u}_{i} \\
\boldsymbol{v}_{i}
\end{array}\right], \quad i=1, \ldots, r, \\
{\left[\begin{array}{cc}
\mathbf{0} & \boldsymbol{A} \\
\boldsymbol{A}^{*} & \mathbf{0}
\end{array}\right]\left[\begin{array}{c}
\boldsymbol{u}_{i} \\
-\boldsymbol{v}_{i}
\end{array}\right] } & =\left[\begin{array}{c}
-\boldsymbol{A} \boldsymbol{v}_{i} \\
\boldsymbol{A}^{*} \boldsymbol{u}_{i}
\end{array}\right]=\left[\begin{array}{c}
-\alpha_{i} \boldsymbol{u}_{i} \\
\alpha_{i} \boldsymbol{v}_{i}
\end{array}\right]=-\alpha_{i}\left[\begin{array}{c}
\boldsymbol{u}_{i} \\
-\boldsymbol{v}_{i}
\end{array}\right], \quad i=1, \ldots, r, \\
{\left[\begin{array}{cc}
\mathbf{0} & \boldsymbol{A} \\
\boldsymbol{A}^{*} & \mathbf{0}
\end{array}\right]\left[\begin{array}{c}
\boldsymbol{u}_{i} \\
\mathbf{0}
\end{array}\right] } & =\left[\begin{array}{c}
\mathbf{0} \\
\boldsymbol{A}^{*} \boldsymbol{u}_{i}
\end{array}\right]=\left[\begin{array}{l}
\mathbf{0} \\
\mathbf{0}
\end{array}\right]=0\left[\begin{array}{c}
\boldsymbol{u}_{i} \\
\mathbf{0}
\end{array}\right], \quad i=r+1, \ldots, m, \\
{\left[\begin{array}{cc}
\mathbf{0} & \boldsymbol{A} \\
\boldsymbol{A}^{*} & \mathbf{0}
\end{array}\right]\left[\begin{array}{c}
\mathbf{0} \\
\boldsymbol{v}_{i}
\end{array}\right] } & =\left[\begin{array}{c}
\boldsymbol{A} \boldsymbol{v}_{i} \\
\mathbf{0}
\end{array}\right]=\left[\begin{array}{l}
\mathbf{0} \\
\mathbf{0}
\end{array}\right]=0\left[\begin{array}{c}
\mathbf{0} \\
\boldsymbol{v}_{i}
\end{array}\right], \quad i=r+1, \ldots, n
\end{aligned}
$$

Thus $\boldsymbol{C}$ has the $2 r$ eigenvalues $\alpha_{1},-\alpha_{1}, \ldots, \alpha_{r},-\alpha_{r}$ and $m+n-2 r$ additional zero eigenvalues. Similarly, if $\boldsymbol{B}$ has rank $s$ then $\boldsymbol{D}$ has the $2 s$ eigenvalues $\beta_{1},-\beta_{1}, \ldots, \beta_{s},-\beta_{s}$ and $m+n-2 s$ additional zero eigenvalues. Let

$$
t:=\max (r, s) .
$$

Then

$$
\begin{gathered}
\lambda_{1} \geq \cdots \geq \lambda_{m+n}=\alpha_{1} \geq \cdots \geq \alpha_{t} \geq 0=\cdots=0 \geq-\alpha_{t} \geq \cdots \geq-\alpha_{1}, \\
\mu_{1} \geq \cdots \geq \mu_{m+n}=\beta_{1} \geq \cdots \geq \beta_{t} \geq 0=\cdots=0 \geq-\beta_{t} \geq \cdots \geq-\beta_{1} .
\end{gathered}
$$

We find

$$
\sum_{j=1}^{m+n}\left|\lambda_{j}-\mu_{j}\right|^{2}=\sum_{i=1}^{t}\left|\alpha_{i}-\beta_{i}\right|^{2}+\sum_{i=1}^{t}\left|-\alpha_{i}+\beta_{i}\right|^{2}=2 \sum_{i=1}^{t}\left|\alpha_{i}-\beta_{i}\right|^{2}
$$

and

$$
\|\boldsymbol{C}-\boldsymbol{D}\|_{F}^{2}=\left\|\left[\begin{array}{cc}
\mathbf{0} & \boldsymbol{A}-\boldsymbol{B} \\
\boldsymbol{A}^{*}-\boldsymbol{B}^{*} & \mathbf{0}
\end{array}\right]\right\|_{F}^{2}=\|\boldsymbol{B}-\boldsymbol{A}\|_{F}^{2}+\left\|(\boldsymbol{B}-\boldsymbol{A})^{*}\right\|_{F}^{2}=2\|\boldsymbol{B}-\boldsymbol{A}\|_{F}^{2} .
$$

But then (9.21) implies $\sum_{i=1}^{t}\left|\alpha_{i}-\beta_{i}\right|^{2} \leq\|\boldsymbol{B}-\boldsymbol{A}\|_{F}^{2}$. Since $t \leq n$ and $\alpha_{i}=\beta_{i}=0$ for $i=t+1, \ldots, n$ we obtain (9.20). $\square$

Because of Theorem 9.11 and the Hoffman-Wielandt Theorem for singular values, Theorem 9.13 we will say that the singular values of a matrix are well conditioned. Changing the Frobenius norm or the spectral norm of a matrix by small amount only changes the singular values by a small amount.

### 9.6 Exercises Chap. 9

### 9.6.1 Exercises Sect. 9.1

Exercise 9.1 (Fitting a Circle to Points) In this problem we derive an algorithm to fit a circle $\left(t-c_{1}\right)^{2}+\left(y-c_{2}\right)^{2}=r^{2}$ to $m \geq 3$ given points $\left(t_{i}, y_{i}\right)_{i=1}^{m}$ in the $(t, y)$-plane. We obtain the overdetermined system

$$
\left(t_{i}-c_{1}\right)^{2}+\left(y_{i}-c_{2}\right)^{2}=r^{2}, i=1, \ldots, m,
$$

of $m$ equations in the three unknowns $c_{1}, c_{2}$ and $r$. This system is nonlinear, but it can be solved from the linear system

$$
t_{i} x_{1}+y_{i} x_{2}+x_{3}=t_{i}^{2}+y_{i}^{2}, i=1, \ldots, m,
$$

and then setting $c_{1}=x_{1} / 2, c_{2}=x_{2} / 2$ and $r^{2}=c_{1}^{2}+c_{2}^{2}+x_{3}$.

a) Derive (9.23) from (9.22). Explain how we can find $c_{1}, c_{2}, r$ once $\left[x_{1}, x_{2}, x_{3}\right]$ is determined.
b) Formulate (9.23) as a linear least squares problem for suitable $\boldsymbol{A}$ and $\boldsymbol{b}$.
c) Does the matrix $\boldsymbol{A}$ in b) have linearly independent columns?
d) Use (9.23) to find the circle passing through the three points $(1,4),(3,2),(1,0)$.

Exercise 9.2 (Least Square Fit (Exam Exercise 2018-1))

a) Let $\boldsymbol{A}$ be the matrix $\left[\begin{array}{cc}\sqrt{2} & \sqrt{2} \\ 0 & \sqrt{3}\end{array}\right]$. Find the singular values of $\boldsymbol{A}$, and compute $\|\boldsymbol{A}\|_{2}$.
b) Consider the matrix $\boldsymbol{A}=\left[\begin{array}{cc}3 & \alpha \\ \alpha & 1\end{array}\right]$, where $\alpha$ is a real number. For which values of $\alpha$ is $\boldsymbol{A}$ positive definite?
c) We would like to fit the points $\boldsymbol{p}_{1}=(0,1), \boldsymbol{p}_{2}=(1,0), \boldsymbol{p}_{3}=(2,1)$ to a straight line in the plane. Find a line $p(x)=m x+b$ which minimizes
$$
\sum_{i=1}^{3}\left\|p\left(x_{i}\right)-y_{i}\right\|^{2},
$$
where $\boldsymbol{p}_{i}=\left(x_{i}, y_{i}\right)$. Is this solution unique?

### 9.6.2 Exercises Sect. 9.2

Exercise 9.3 (A Least Squares Problem (Exam Exercise 1983-2)) Suppose $\boldsymbol{A} \in$ $\mathbb{R}^{m \times n}$ and let $\boldsymbol{I} \in \mathbb{R}^{n \times n}$ be the identity matrix. We define $F: \mathbb{R}^{n} \rightarrow \mathbb{R}$ by

$$
F(\boldsymbol{x}):=\|\boldsymbol{A} \boldsymbol{x}-\boldsymbol{b}\|_{2}^{2}+\|\boldsymbol{x}\|_{2}^{2} .
$$

a) Show that the matrix $\boldsymbol{B}:=\boldsymbol{I}+\boldsymbol{A}^{T} \boldsymbol{A}$ is symmetric and positive definite.
b) Show that
$$
F(\boldsymbol{x})=\boldsymbol{x}^{T} \boldsymbol{B} \boldsymbol{x}-2 \boldsymbol{c}^{T} \boldsymbol{x}+\boldsymbol{b}^{T} \boldsymbol{b}, \quad \text { where } \quad \boldsymbol{c}=\boldsymbol{A}^{T} \boldsymbol{b} .
$$
c) Show that to every $\boldsymbol{b} \in \mathbb{R}^{m}$ there is a unique $\boldsymbol{x}$ which minimizes $F$. Moreover, $\boldsymbol{x}$ is the unique solution of the linear system $\left(\boldsymbol{I}+\boldsymbol{A}^{T} \boldsymbol{A}\right) \boldsymbol{x}=\boldsymbol{A}^{T} \boldsymbol{b}$.

Exercise 9.4 (Weighted Least Squares (Exam Exercise 1977-2)) For $m \geq n$ we are given $\boldsymbol{A} \in \mathbb{R}^{m \times n}$ with linearly independent columns, $\boldsymbol{b} \in \mathbb{R}^{m}$, and $\boldsymbol{D}:=$ $\operatorname{diag}\left(d_{1}, d_{2}, \ldots, d_{m}\right) \in \mathbb{R}^{m \times m}$, where $d_{i}>0, i=1,2, \ldots, m$. We want to minimize

$$
\|\boldsymbol{r}(\boldsymbol{x})\|_{D}^{2}:=\sum_{i=1}^{m} r_{i}(x)^{2} d_{i}, \quad \boldsymbol{x} \in \mathbb{R}^{n}
$$

where $r_{i}=r_{i}(\boldsymbol{x}), i=1,2, \ldots, m$ are the components of the vector

$$
r=r(x)=b-A x .
$$

a) Show that $\|\boldsymbol{r}(\boldsymbol{x})\|_{D}^{2}$ in (9.24) obtains a unique minimum when $\boldsymbol{x}=\boldsymbol{x}_{\text {min }}$ is the solution of the system
$$
\boldsymbol{A}^{T} \boldsymbol{D} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{T} \boldsymbol{D} \boldsymbol{b} .
$$
b) Show that
$$
K_{2}\left(\boldsymbol{A}^{T} \boldsymbol{D} \boldsymbol{A}\right) \leq K_{2}\left(\boldsymbol{A}^{T} \boldsymbol{A}\right) K_{2}(\boldsymbol{D}),
$$
where for any nonsingular matrix $K_{2}(\boldsymbol{B}):=\|\boldsymbol{B}\|_{2}\left\|\boldsymbol{B}^{-1}\right\|_{2}$.

### 9.6.3 Exercises Sect. 9.3

Exercise 9.5 (Uniqueness of Generalized Inverse) Given $\boldsymbol{A} \in \mathbb{C}^{m \times n}$, and suppose $\boldsymbol{B}, \boldsymbol{C} \in \mathbb{C}^{n \times m}$ satisfy

$$
\begin{array}{cl}
\boldsymbol{A B A}=\boldsymbol{A} & (1) \quad \boldsymbol{A C A}=\boldsymbol{A}, \\
\boldsymbol{B A B}=\boldsymbol{B} & (2) \quad \boldsymbol{C A C}=\boldsymbol{C}, \\
(\boldsymbol{A B})^{*}=\boldsymbol{A B} & (3) \quad(\boldsymbol{A C})^{*}=\boldsymbol{A C}, \\
(\boldsymbol{B A})^{*}=\boldsymbol{B A} & (4) \quad(\boldsymbol{C A})^{*}=\boldsymbol{C A} .
\end{array}
$$

Verify the following proof that $\boldsymbol{B}=\boldsymbol{C}$.

$$
\begin{aligned}
B & =(B A) B=\left(A^{*}\right) B^{*} B=\left(A^{*} C^{*}\right) A^{*} B^{*} B=C A\left(A^{*} B^{*}\right) B \\
& =C A(B A B)=(C) A B=C(A C) A B=C C^{*} A^{*}(A B) \\
& =C C^{*}\left(A^{*} B^{*} A^{*}\right)=C\left(C^{*} A^{*}\right)=C A C=C .
\end{aligned}
$$

Exercise 9.6 (Verify That a Matrix Is a Generalized Inverse) Show that the generalized inverse of $\boldsymbol{A}=\left[\begin{array}{ll}1 & 1 \\ 1 & 1 \\ 0 & 0\end{array}\right]$ is $\boldsymbol{A}^{\dagger}=\frac{1}{4}\left[\begin{array}{lll}1 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]$ without using the singular value decomposition of $\boldsymbol{A}$.

Exercise 9.7 (Linearly Independent Columns and Generalized Inverse) Suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has linearly independent columns. Show that $\boldsymbol{A}^{*} \boldsymbol{A}$ is nonsingular and $\boldsymbol{A}^{\dagger}=\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)^{-1} \boldsymbol{A}^{*}$. If $\boldsymbol{A}$ has linearly independent rows, then show that $\boldsymbol{A} \boldsymbol{A}^{*}$ is nonsingular and $\boldsymbol{A}^{\dagger}=\boldsymbol{A}^{*}\left(\boldsymbol{A} \boldsymbol{A}^{*}\right)^{-1}$.

Exercise 9.8 (More Orthogonal Projections) Given $m, n \in \mathbb{N}, \boldsymbol{A} \in \mathbb{C}^{m \times n}$ of rank $r$, and let $\mathcal{S}$ be one of the subspaces $\mathcal{R}\left(\boldsymbol{A}^{*}\right), \mathcal{N}(\boldsymbol{A})$. Show that the orthogonal projection of $\boldsymbol{v} \in \mathbb{C}^{n}$ into $\mathcal{S}$ can be written as a matrix $\boldsymbol{P}_{\mathcal{S}}$ times the vector $\boldsymbol{v}$ in the form $\boldsymbol{P}_{\mathcal{S}} \boldsymbol{v}$, where

$$
\begin{aligned}
& \boldsymbol{P}_{\mathcal{R}\left(\boldsymbol{A}^{*}\right)}=\boldsymbol{A}^{\dagger} \boldsymbol{A}=\boldsymbol{V}_{1} \boldsymbol{V}_{1}^{*}=\sum_{j=1}^{r} \boldsymbol{v}_{j} \boldsymbol{v}_{j}^{*} \in \mathbb{C}^{n \times n} \\
& \boldsymbol{P}_{\mathcal{N}(\boldsymbol{A})}=\boldsymbol{I}-\boldsymbol{A}^{\dagger} \boldsymbol{A}=\boldsymbol{V}_{2} \boldsymbol{V}_{2}^{*}=\sum_{j=r+1}^{n} \boldsymbol{v}_{j} \boldsymbol{v}_{j}^{*} \in \mathbb{C}^{n \times n} .
\end{aligned}
$$

where $\boldsymbol{A}^{\dagger}$ is the generalized inverse of $\boldsymbol{A}$ and $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^{*} \in \mathbb{C}^{m \times n}$, is a singular value decomposition of $\boldsymbol{A}$ (cf. (9.7)). Thus (9.12) and (9.25) give the orthogonal projections into the 4 fundamental subspaces. Hint: by Theorem 7.3 we have the orthogonal sum $\quad \mathbb{C}^{n}=\mathcal{R}\left(\boldsymbol{A}^{*}\right) \stackrel{\perp}{\oplus} \mathcal{N}(\boldsymbol{A})$.

Exercise 9.9 (The Generalized Inverse of a Vector) Show that $\boldsymbol{u}^{\dagger}=\left(\boldsymbol{u}^{*} \boldsymbol{u}\right)^{-1} \boldsymbol{u}^{*}$ if $\boldsymbol{u} \in \mathbb{C}^{n, 1}$ is nonzero.

Exercise 9.10 (The Generalized Inverse of an Outer Product) If $\boldsymbol{A}=\boldsymbol{u} \boldsymbol{v}^{*}$ where $\boldsymbol{u} \in \mathbb{C}^{m}, \boldsymbol{v} \in \mathbb{C}^{n}$ are nonzero, show that

$$
\boldsymbol{A}^{\dagger}=\frac{1}{\alpha} \boldsymbol{A}^{*}, \quad \alpha=\|\boldsymbol{u}\|_{2}^{2}\|\boldsymbol{v}\|_{2}^{2} .
$$

Exercise 9.11 (The Generalized Inverse of a Diagonal Matrix) Show that $\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)^{\dagger}=\operatorname{diag}\left(\lambda_{1}^{\dagger}, \ldots, \lambda_{n}^{\dagger}\right)$ where

$$
\lambda_{i}^{\dagger}=\left\{\begin{array}{cc}
1 / \lambda_{i}, & \lambda_{i} \neq 0 \\
0 & \lambda_{i}=0 .
\end{array}\right.
$$

Exercise 9.12 (Properties of the Generalized Inverse) Suppose $\boldsymbol{A} \in \mathbb{C}^{m \times n}$. Show that

a) $\left(\boldsymbol{A}^{*}\right)^{\dagger}=\left(\boldsymbol{A}^{\dagger}\right)^{*}$.
b) $\left(\boldsymbol{A}^{\dagger}\right)^{\dagger}=\boldsymbol{A}$.
c) $(\alpha \boldsymbol{A})^{\dagger}=\frac{1}{\alpha} \boldsymbol{A}^{\dagger}, \quad \alpha \neq 0$.

Exercise 9.13 (The Generalized Inverse of a Product) Suppose $k, m, n \in \mathbb{N}, \boldsymbol{A} \in$ $\mathbb{C}^{m \times n}, \boldsymbol{B} \in \mathbb{C}^{n \times k}$. Suppose $\boldsymbol{A}$ has linearly independent columns and $\boldsymbol{B}$ has linearly independent rows.

a) Show that $(\boldsymbol{A} \boldsymbol{B})^{\dagger}=\boldsymbol{B}^{\dagger} \boldsymbol{A}^{\dagger}$.
Hint: Let $\boldsymbol{E}=\boldsymbol{A} \boldsymbol{B}, \boldsymbol{F}=\boldsymbol{B}^{\dagger} \boldsymbol{A}^{\dagger}$. Show by using $\boldsymbol{A}^{\dagger} \boldsymbol{A}=\boldsymbol{B} \boldsymbol{B}^{\dagger}=\boldsymbol{I}$ that $\boldsymbol{F}$ is the generalized inverse of $\boldsymbol{E}$.
b) Find $\boldsymbol{A} \in \mathbb{R}^{1,2}, \boldsymbol{B} \in \mathbb{R}^{2,1}$ such that $(\boldsymbol{A} \boldsymbol{B})^{\dagger} \neq \boldsymbol{B}^{\dagger} \boldsymbol{A}^{\dagger}$.

Exercise 9.14 (The Generalized Inverse of the Conjugate Transpose) Show that $\boldsymbol{A}^{*}=\boldsymbol{A}^{\dagger}$ if and only if all singular values of $\boldsymbol{A}$ are either zero or one.

Exercise 9.15 (Linearly Independent Columns) Show that if $\boldsymbol{A}$ has rank $n$ then $\boldsymbol{A}\left(\boldsymbol{A}^{*} \boldsymbol{A}\right)^{-1} \boldsymbol{A}^{*} \boldsymbol{b}$ is the projection of $\boldsymbol{b}$ into $\mathcal{R}(\boldsymbol{A})$. (Cf. Exercise 9.8.)

Exercise 9.16 (Analysis of the General Linear System) Consider the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ where $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has rank $r>0$ and $\boldsymbol{b} \in \mathbb{C}^{n}$. Let

$$
U^{*} A V=\left[\begin{array}{cc}
\Sigma_{1} & 0 \\
\mathbf{0} & \mathbf{0}
\end{array}\right]
$$

represent the singular value decomposition of $\boldsymbol{A}$.

a) Let $\boldsymbol{c}=\left[c_{1}, \ldots, c_{n}\right]^{*}=\boldsymbol{U}^{*} \boldsymbol{b}$ and $\boldsymbol{y}=\left[y_{1}, \ldots, y_{n}\right]^{*}=\boldsymbol{V}^{*} \boldsymbol{x}$. Show that $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ if and only if
$$
\left[\begin{array}{cc}
\Sigma_{1} & 0 \\
0 & 0
\end{array}\right] y=c .
$$
b) Show that $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ has a solution $\boldsymbol{x}$ if and only if $c_{r+1}=\cdots=c_{n}=0$.
c) Deduce that a linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ has either no solution, one solution or infinitely many solutions.

Exercise 9.17 (Fredholm's Alternative) For any $\boldsymbol{A} \in \mathbb{C}^{m \times n}, \boldsymbol{b} \in \mathbb{C}^{n}$ show that one and only one of the following systems has a solution

$$
\text { (1) } \quad \boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}, \quad \text { (2) } \quad \boldsymbol{A}^{*} \boldsymbol{y}=\mathbf{0}, \boldsymbol{y}^{*} \boldsymbol{b} \neq 0 \text {. }
$$

In other words either $\boldsymbol{b} \in \mathcal{R}(\boldsymbol{A})$, or we can find $\boldsymbol{y} \in \mathcal{N}\left(\boldsymbol{A}^{*}\right)$ such that $\boldsymbol{y}^{*} \boldsymbol{b} \neq 0$. This is called Fredholm's alternative.

Exercise 9.18 (SVD (Exam Exercise 2017-2)) Let $\boldsymbol{A} \in \mathbb{C}^{m \times n}$, with $m \geq n$, be a matrix on the form

$$
A=\left[\begin{array}{l}
B \\
C
\end{array}\right]
$$

where $\boldsymbol{B}$ is a non-singular $n \times n$ matrix and $\boldsymbol{C}$ is in $\mathbb{C}^{(m-n) \times n}$. Let $\boldsymbol{A}^{\dagger}$ denote the pseudoinverse of $\boldsymbol{A}$. Show that $\left\|\boldsymbol{A}^{\dagger}\right\|_{2} \leq\left\|\boldsymbol{B}^{-1}\right\|_{2}$.

### 9.6.4 Exercises Sect. 9.4

Exercise 9.19 (Condition Number) Let

$$
\boldsymbol{A}=\left[\begin{array}{ll}
1 & 2 \\
1 & 1 \\
1 & 1
\end{array}\right], \quad \boldsymbol{b}=\left[\begin{array}{l}
b_{1} \\
b_{2} \\
b_{3}
\end{array}\right] .
$$

a) Determine the projections $\boldsymbol{b}_{1}$ and $\boldsymbol{b}_{2}$ of $\boldsymbol{b}$ on $\mathcal{R}(\boldsymbol{A})$ and $\mathcal{N}\left(\boldsymbol{A}^{*}\right)$.
b) Compute $K(\boldsymbol{A})=\|\boldsymbol{A}\|_{2}\left\|\boldsymbol{A}^{\dagger}\right\|_{2}$.

Exercise 9.20 (Equality in Perturbation Bound) Let $\boldsymbol{A} \in \mathbb{C}^{m \times n}$. Suppose $\boldsymbol{y}_{\boldsymbol{A}}$ and $\boldsymbol{y}_{A^{\dagger}}$ are vectors with $\left\|\boldsymbol{y}_{\boldsymbol{A}}\right\|=\left\|\boldsymbol{y}_{A^{\dagger}}\right\|=1$ and $\|\boldsymbol{A}\|=\left\|\boldsymbol{A} \boldsymbol{y}_{\boldsymbol{A}}\right\|$ and $\left\|\boldsymbol{A}^{\dagger}\right\|=$ $\left\|\boldsymbol{A}^{\dagger} \boldsymbol{y}_{A^{\dagger}}\right\|$.

a) Show that we have equality to the right in (9.13) if $\boldsymbol{b}=\boldsymbol{A} \boldsymbol{y}_{A}, \boldsymbol{e}_{1}=\boldsymbol{y}_{A^{\dagger}}$.
b) Show that we have equality to the left if we switch $\boldsymbol{b}$ and $\boldsymbol{e}_{1}$ in a).
c) Let $\boldsymbol{A}$ be as in Example 9.7. Find extremal $\boldsymbol{b}$ and $\boldsymbol{e}$ when the $l_{\infty}$ norm is used.

This generalizes the sharpness results in Exercise 8.18. For if $m=n$ and $\boldsymbol{A}$ is nonsingular then $\boldsymbol{A}^{\dagger}=\boldsymbol{A}^{-1}$ and $\boldsymbol{e}_{1}=\boldsymbol{e}$.

Exercise 9.21 (Problem Using Normal Equations) Consider the least squares problems where

$$
\boldsymbol{A}=\left[\begin{array}{cc}
1 & 1 \\
1 & 1 \\
1 & 1+\epsilon
\end{array}\right], \quad \boldsymbol{b}=\left[\begin{array}{l}
2 \\
3 \\
2
\end{array}\right], \quad \in \in \mathbb{R} .
$$

a) Find the normal equations and the exact least squares solution.
b) Suppose $\epsilon$ is small and we replace the $(2,2)$ entry $3+2 \epsilon+\epsilon^{2}$ in $\boldsymbol{A}^{*} \boldsymbol{A}$ by $3+2 \epsilon$. (This will be done in a computer if $\epsilon<\sqrt{u}, u$ being the round-off unit). For example, if $u=10^{-16}$ then $\sqrt{u}=10^{-8}$. Solve $\boldsymbol{A}^{*} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{*} \boldsymbol{b}$ for $\boldsymbol{x}$ and compare with the $\boldsymbol{x}$ found in a). (We will get a much more accurate result using the QR factorization or the singular value decomposition on this problem).

### 9.6.5 Exercises Sect. 9.5

Exercise 9.22 (Singular Values Perturbation (Exam Exercise 1980-2)) Let $\boldsymbol{A}(\epsilon) \in \mathbb{R}^{n \times n}$ be bidiagonal with $a_{i, j}=0$ for $i, j=1, \ldots, n$ and $j \neq i, i+1$. Moreover, for some $1 \leq k \leq n-1$ we have $a_{k, k+1}=\epsilon \in \mathbb{R}$. Show that

$$
\left|\sigma_{i}(\epsilon)-\sigma_{i}(0)\right| \leq|\epsilon|, \quad i=1, \ldots, n,
$$

where $\sigma_{i}(\epsilon), i=1, \ldots, n$ are the singular values of $\boldsymbol{A}(\epsilon)$.

### 9.7 Review Questions

9.7.1 Do the normal equations always have a solution?
9.7.2 When is the least squares solution unique?
9.7.3 Express the general least squares solution in terms of the generalized inverse.
9.7.4 Consider perturbing the right-hand side in a linear equation and a least squares problem. What is the main difference in the perturbation inequalities?
9.7.5 Why does one often prefer using QR factorization instead of normal equations for solving least squares problems.
9.7.6 What is an orthogonal sum?
9.7.7 How is an orthogonal projection defined?

## Part IV <br> Kronecker Products and Fourier Transforms

We give an introduction to Kronecker products of matrices and the fast Fourier transform. We illustrate the usefulness by giving a fast method for solving the 2 dimensional discrete Poison Equation based on the fast Fourier transform.

## Chapter 10 <br> The Kronecker Product

Matrices arising from 2D and 3D problems sometimes have a Kronecker product structure. Identifying a Kronecker structure can be very rewarding since it simplifies the derivation of properties of such matrices.

### 10.1 The 2D Poisson Problem

Let $\Omega:=(0,1)^{2}=\{(x, y): 0<x, y<1\}$ be the open unit square with boundary $\partial \Omega$. Consider the problem

$$
\begin{gathered}
-\Delta u:=-\frac{\partial^{2} u}{\partial x^{2}}-\frac{\partial^{2} u}{\partial y^{2}}=f \text { on } \Omega, \\
u:=0 \text { on } \partial \Omega .
\end{gathered}
$$

Here the function $f$ is given and continuous on $\Omega$, and we seek a function $u=$ $u(x, y)$ such that (10.1) holds and which is zero on $\partial \Omega$.

Let $m$ be a positive integer. We solve the problem numerically by finding approximations $v_{j, k} \approx u(j h, k h)$ on a grid of points given by

$$
\bar{\Omega}_{h}:=\{(j h, k h): j, k=0,1, \ldots, m+1\}, \quad \text { where } \quad h=1 /(m+1) .
$$

The points $\Omega_{h}:=\{(j h, k h): j, k=1, \ldots, m\}$ are called the interior points, while $\bar{\Omega}_{h} \backslash \Omega_{h}$ are the boundary points. The solution is zero at the boundary points. Using the difference approximation from Chap. 2 for the second derivative we obtain the
following approximations for the partial derivatives

$$
\frac{\partial^{2} u(j h, k h)}{\partial x^{2}} \approx \frac{v_{j-1, k}-2 v_{j, k}+v_{j+1, k}}{h^{2}}, \frac{\partial^{2} u(j h, k h)}{\partial y^{2}} \approx \frac{v_{j, k-1}-2 v_{j, k}+v_{j, k+1}}{h^{2}} .
$$

Inserting this in (10.1) we get the following discrete analog of (10.1)

$$
\begin{aligned}
-\Delta_{h} v_{j, k} & =f_{j, k}, \quad(j h, k h) \in \Omega_{h}, \\
v_{j, k} & =0, \quad(j h, k h) \in \partial \Omega_{h},
\end{aligned}
$$

where $f_{j, k}:=f(j h, k h)$ and

$$
-\Delta_{h} v_{j, k}:=\frac{-v_{j-1, k}+2 v_{j, k}-v_{j+1, k}}{h^{2}}+\frac{-v_{j, k-1}+2 v_{j, k}-v_{j, k+1}}{h^{2}} .
$$

Let us take a closer look at (10.2). It consists of $n:=m^{2}$ linear equations. Since the values at the boundary points are known, the unknowns are the $n$ numbers $v_{j, k}$ at the interior points. These linear equations can be written as a matrix equation in the form

$$
\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}=h^{2} \boldsymbol{F} \quad \text { with } \quad h=1 /(m+1),
$$

where $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1) \in \mathbb{R}^{m \times m}$ is the second derivative matrix given by (2.27) and

$$
\boldsymbol{V}:=\left[\begin{array}{ccc}
v_{1,1} & \cdots & v_{1, m} \\
\vdots & & \vdots \\
v_{m, 1} & \cdots & v_{m, m}
\end{array}\right] \in \mathbb{R}^{m \times m}, \quad \boldsymbol{F}:=\left[\begin{array}{ccc}
f_{1,1} & \cdots & f_{1, m} \\
\vdots & & \vdots \\
f_{m, 1} & \cdots & f_{m, m}
\end{array}\right] \in \mathbb{R}^{m \times m} .
$$

Indeed, the ( $j, k$ ) element in $\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V T}$ is given by

$$
\sum_{i=1}^{m} \boldsymbol{T}_{j, i} v_{i, k}+\sum_{i=1}^{m} v_{j, i} \boldsymbol{T}_{i, k}=-v_{j-1, k}+2 v_{j, k}-v_{j+1, k}-v_{j, k-1}+2 v_{j, k}-v_{j, k+1},
$$

and if we divide by $h^{2}$ this is precisely the left hand side of (10.2).
To write (10.5) in standard form $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ we need to order the unknowns $v_{j, k}$ in some way. The following operation of vectorization of a matrix gives one possible ordering.

Definition 10.1 (vec Operation) For any $\boldsymbol{B} \in \mathbb{R}^{m \times n}$ we define the vector

$$
\operatorname{vec}(\boldsymbol{B}):=\left[b_{11}, \ldots, b_{m 1}, b_{12}, \ldots, b_{m 2}, \ldots, b_{1 n}, \ldots, b_{m n}\right]^{T} \in \mathbb{R}^{m n}
$$

by stacking the columns of $\boldsymbol{B}$ on top of each other.

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-240.jpg?height=385&width=935&top_left_y=211&top_left_x=295)
Fig. 10.1 Numbering of grid points

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-240.jpg?height=316&width=958&top_left_y=704&top_left_x=284)
Fig. 10.2 The 5-point stencil

Let $\boldsymbol{x}:=\operatorname{vec}(\boldsymbol{V}) \in \mathbb{R}^{n}$, where $n=m^{2}$. Note that forming $\boldsymbol{x}$ by stacking the columns of $\boldsymbol{V}$ on top of each other means an ordering of the grid points. For $m=3$ this is illustrated in Fig. 10.1. We call this the natural ordering. The elements in (10.2) defines a 5-point stencil, as shown in Fig. 10.2.

To find the matrix $\boldsymbol{A}$ we note that for values of $j, k$ where the 5-point stencil does not touch the boundary, (10.2) implies

$$
4 x_{i}-x_{i-1}-x_{i+1}-x_{i-m}-x_{i+m}=b_{i},
$$

where $x_{i}=v_{j, k}$ and $b_{i}=h^{2} f_{j, k}$. This must be modified close to the boundary. We then obtain the linear system

$$
\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}, \quad \boldsymbol{A} \in \mathbb{R}^{n \times n}, \quad b \in \mathbb{R}^{n}, \quad n=m^{2},
$$

where $\boldsymbol{x}=\operatorname{vec}(\boldsymbol{V}), \boldsymbol{b}=h^{2} \operatorname{vec}(\boldsymbol{F})$ and $\boldsymbol{A}$ is the Poisson matrix given by

$$
\begin{aligned}
a_{i i}=4, & i=1, \ldots, n, \\
a_{i+1, i}=a_{i, i+1}=-1, & i=1, \ldots, n-1, \quad i \neq m, 2 m, \ldots,(m-1) m, \\
a_{i+m, i}=a_{i, i+m}=-1, & i=1, \ldots, n-m, \\
a_{i j}=0, & \text { otherwise } .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-241.jpg?height=398&width=1079&top_left_y=209&top_left_x=230)
Fig. 10.3 Band structure of the 2D test matrix

For $m=3$ we have the following matrix

$$
\boldsymbol{A}=\left[\begin{array}{rrrrrrrr}
4 & -1 & 0 & -1 & 0 & 0 & 0 & 0 \\
-1 & 4 & -1 & 0 & -1 & 0 & 0 & 0 \\
0 & -1 & 4 & 0 & 0 & -1 & 0 & 0 \\
-1 & 0 & 0 & 4 & -1 & 0 & -1 & 0 \\
0 & -1 & 0 & -1 & 4 & -1 & 0 & -1 \\
0 & 0 & -1 & 0 & -1 & 4 & 0 & 0 \\
0 & 0 & 0 & -1 & 0 & 0 & 4 & -1 \\
0 & 0 & 0 & 0 & -1 & 0 & -1 & 4 \\
0 & 0 & 0 & 0 & 0 & -1 & 0 & -1
\end{array}\right] .
$$

The bands of the weakly diagonally dominant matrix $\boldsymbol{A}$ are illustrated in Fig. 10.3.

### 10.1.1 The Test Matrices

In Sect. 2.4 we encountered the 1-dimensional test matrix $\boldsymbol{T}_{1} \in \mathbb{R}^{m \times m}$ defined for any real numbers $a, d$ by

$$
\boldsymbol{T}_{1}:=\operatorname{tridiag}(a, d, a) .
$$

The (2-dimensional) Poisson matrix is a special case of the matrix $\boldsymbol{T}_{2}=\left[a_{i j}\right] \in$ $\mathbb{R}^{n \times n}$ with elements

$$
\begin{aligned}
a_{i i} & =2 d, i=1, \ldots, n, \\
a_{i, i+1}=a_{i+1, i} & =a, \quad i=1, \ldots, n-1, \quad i \neq m, 2 m, \ldots,(m-1) m, \\
a_{i, i+m}=a_{i+m, i} & =a, \quad i=1, \ldots, n-m, \\
a_{i j} & =0, \text { otherwise }
\end{aligned}
$$

and where $a, d$ are real numbers. We will refer to this matrix as simply the 2D test matrix. For $m=3$ the 2D test matrix looks as follows

$$
\boldsymbol{T}_{2}=\left[\begin{array}{rrr|rrr|rrr}
2 d & a & 0 & a & 0 & 0 & 0 & 0 & 0 \\
a & 2 d & a & 0 & a & 0 & 0 & 0 & 0 \\
0 & a & 2 d & 0 & 0 & a & 0 & 0 & 0 \\
\hline a & 0 & 0 & 2 d & a & 0 & a & 0 & 0 \\
0 & a & 0 & a & 2 d & a & 0 & a & 0 \\
0 & 0 & a & 0 & a & 2 d & 0 & 0 & a \\
\hline 0 & 0 & 0 & a & 0 & 0 & 2 d & a & 0 \\
0 & 0 & 0 & 0 & a & 0 & a & 2 d & a \\
0 & 0 & 0 & 0 & 0 & a & 0 & a & 2 d
\end{array}\right] .
$$

The partition into $3 \times 3$ sub matrices shows that $\boldsymbol{T}_{2}$ is block tridiagonal.
Properties of $\boldsymbol{T}_{2}$ can be derived from properties of $\boldsymbol{T}_{1}$ by using properties of the Kronecker product.

### 10.2 The Kronecker Product

Definition 10.2 (Kronecker Product) For any positive integers $p, q, r, s$ we define the Kronecker product of two matrices $\boldsymbol{A} \in \mathbb{R}^{p \times q}$ and $\boldsymbol{B} \in \mathbb{R}^{r \times s}$ as a matrix $\boldsymbol{C} \in \mathbb{R}^{p r \times q s}$ given in block form as

$$
\boldsymbol{C}=\left[\begin{array}{cccc}
\boldsymbol{A} b_{1,1} & \boldsymbol{A} b_{1,2} & \cdots & \boldsymbol{A} b_{1, s} \\
\boldsymbol{A} b_{2,1} & \boldsymbol{A} b_{2,2} & \cdots & \boldsymbol{A} b_{2, s} \\
\vdots & \vdots & \ddots & \vdots \\
\boldsymbol{A} b_{r, 1} & \boldsymbol{A} b_{r, 2} & \cdots & \boldsymbol{A} b_{r, s}
\end{array}\right] .
$$

We denote the Kronecker product of $\boldsymbol{A}$ and $\boldsymbol{B}$ by $\boldsymbol{C}=\boldsymbol{A} \otimes \boldsymbol{B}$.
This definition of the Kronecker product is known more precisely as the left Kronecker product. In the literature one often finds the right Kronecker product which in our notation is given by $\boldsymbol{B} \otimes \boldsymbol{A}$.

The Kronecker product $\boldsymbol{u} \otimes \boldsymbol{v}=\left[\boldsymbol{u}^{T} v_{1}, \ldots, \boldsymbol{u}^{T} v_{r}\right]^{T}$ of two column vectors $\boldsymbol{u} \in \mathbb{R}^{p}$ and $\boldsymbol{v} \in \mathbb{R}^{r}$ is a column vector of length $p \cdot r$.

The test matrix $\boldsymbol{T}_{2}$ can be written as a sum of Kronecker products. Indeed, if $m=3$ then

$$
\boldsymbol{T}_{1}=\left[\begin{array}{ccc}
d & a & 0 \\
a & d & a \\
0 & a & d
\end{array}\right], \quad \boldsymbol{I}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
$$

and

$$
\boldsymbol{T}_{1} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T}_{1}=\left[\begin{array}{ccc}
\boldsymbol{T}_{1} & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{T}_{1} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \boldsymbol{T}_{1}
\end{array}\right]+\left[\begin{array}{ccc}
d \boldsymbol{I} & a \boldsymbol{I} & \mathbf{0} \\
a \boldsymbol{I} & d \boldsymbol{I} & a \boldsymbol{I} \\
\mathbf{0} & a \boldsymbol{I} & d \boldsymbol{I}
\end{array}\right]=\boldsymbol{T}_{2}
$$

given by (10.11). This formula holds for any integer $m \geq 2$

$$
\boldsymbol{T}_{2}=\boldsymbol{T}_{1} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T}_{1}, \quad \boldsymbol{T}_{1}, \boldsymbol{I} \in \mathbb{R}^{m \times m}, \quad \boldsymbol{T}_{2} \in \mathbb{R}^{\left(m^{2}\right) \times\left(m^{2}\right)} .
$$

The sum of two Kronecker products involving the identity matrix is worthy of a special name.

Definition 10.3 (Kronecker Sum) For positive integers $r, s, k$, let $\boldsymbol{A} \in \mathbb{R}^{r \times r}, \boldsymbol{B} \in$ $\mathbb{R}^{s \times s}$, and $\boldsymbol{I}_{k}$ be the identity matrix of order $k$. The sum $\boldsymbol{A} \otimes \boldsymbol{I}_{s}+\boldsymbol{I}_{r} \otimes \boldsymbol{B}$ is known as the Kronecker sum of $\boldsymbol{A}$ and $\boldsymbol{B}$.

In other words, the 2D test matrix $\boldsymbol{T}_{2}$ is the Kronecker sum involving the 1D test matrix $\boldsymbol{T}_{1}$.

The following simple arithmetic rules hold for Kronecker products. For scalars $\lambda, \mu$ and matrices $\boldsymbol{A}, \boldsymbol{A}_{1}, \boldsymbol{A}_{2}, \boldsymbol{B}, \boldsymbol{B}_{1}, \boldsymbol{B}_{2}, \boldsymbol{C}$ of dimensions such that the operations are defined, we have

$$
\begin{aligned}
(\lambda \boldsymbol{A}) \otimes(\mu \boldsymbol{B}) & =\lambda \mu(\boldsymbol{A} \otimes \boldsymbol{B}) \\
\left(\boldsymbol{A}_{1}+\boldsymbol{A}_{2}\right) \otimes \boldsymbol{B} & =\boldsymbol{A}_{1} \otimes \boldsymbol{B}+\boldsymbol{A}_{2} \otimes \boldsymbol{B}, \\
\boldsymbol{A} \otimes\left(\boldsymbol{B}_{1}+\boldsymbol{B}_{2}\right) & =\boldsymbol{A} \otimes \boldsymbol{B}_{1}+\boldsymbol{A} \otimes \boldsymbol{B}_{2} \\
(\boldsymbol{A} \otimes \boldsymbol{B}) \otimes \boldsymbol{C} & =\boldsymbol{A} \otimes(\boldsymbol{B} \otimes \boldsymbol{C}) .
\end{aligned}
$$

Note however that in general we have $\boldsymbol{A} \otimes \boldsymbol{B} \neq \boldsymbol{B} \otimes \boldsymbol{A}$, but it can be shown that there are permutation matrices $\boldsymbol{P}, \boldsymbol{Q}$ such that $\boldsymbol{B} \otimes \boldsymbol{A}=\boldsymbol{P}(\boldsymbol{A} \otimes \boldsymbol{B}) \boldsymbol{Q}$, see [9].

The following mixed product rule is an essential tool for dealing with Kronecker products and sums.

Lemma 10.1 (Mixed Product Rule) Suppose A, B, C, D are rectangular matrices with dimensions so that the products $\boldsymbol{A} \boldsymbol{C}$ and $\boldsymbol{B} \boldsymbol{D}$ are well defined. Then the product $(\boldsymbol{A} \otimes \boldsymbol{B})(\boldsymbol{C} \otimes \boldsymbol{D})$ is defined and

$$
(\boldsymbol{A} \otimes \boldsymbol{B})(\boldsymbol{C} \otimes \boldsymbol{D})=(\boldsymbol{A} \boldsymbol{C}) \otimes(\boldsymbol{B} \boldsymbol{D}) .
$$

Proof If $\boldsymbol{B} \in \mathbb{R}^{r, t}$ and $\boldsymbol{D} \in \mathbb{R}^{t, s}$ for some integers $r, s, t$, then

$$
(\boldsymbol{A} \otimes \boldsymbol{B})(\boldsymbol{C} \otimes \boldsymbol{D})=\left[\begin{array}{ccc}
\boldsymbol{A} b_{1,1} & \cdots & \boldsymbol{A} b_{1, t} \\
\vdots & & \vdots \\
\boldsymbol{A} b_{r, 1} & \cdots & \boldsymbol{A} b_{r, t}
\end{array}\right]\left[\begin{array}{ccc}
\boldsymbol{C} d_{1,1} & \cdots & \boldsymbol{C} d_{1, s} \\
\vdots & & \vdots \\
\boldsymbol{C} d_{t, 1} & \cdots & \boldsymbol{C} d_{t, s}
\end{array}\right] .
$$

Thus for all $i, j$

$$
((\boldsymbol{A} \otimes \boldsymbol{B})(\boldsymbol{C} \otimes \boldsymbol{D}))_{i, j}=\boldsymbol{A} \boldsymbol{C} \sum_{k=1}^{t} b_{i, k} d_{k, j}=(\boldsymbol{A} \boldsymbol{C})(\boldsymbol{B} \boldsymbol{D})_{i, j}=((\boldsymbol{A} \boldsymbol{C}) \otimes(\boldsymbol{B} \boldsymbol{D}))_{i, j} .
$$ $\square$

Using the mixed product rule we obtain the following properties of Kronecker products and sums.

Theorem 10.1 (Properties of Kronecker Products) Suppose for $r, s \in \mathbb{N}$ that $\boldsymbol{A} \in \mathbb{R}^{r \times r}$ and $\boldsymbol{B} \in \mathbb{R}^{s \times s}$ are square matrices with eigenpairs $\left(\lambda_{i}, \boldsymbol{u}_{i}\right) i=1, \ldots, r$ and $\left(\mu_{j}, \boldsymbol{v}_{j}\right), j=1, \ldots, s$. Moreover, let $\boldsymbol{F}, \boldsymbol{V} \in \mathbb{R}^{r \times s}$. Then

1. $(\boldsymbol{A} \otimes \boldsymbol{B})^{T}=\boldsymbol{A}^{T} \otimes \boldsymbol{B}^{T}$, (this also holds for rectangular matrices).
2. If $\boldsymbol{A}$ and $\boldsymbol{B}$ are nonsingular then $\boldsymbol{A} \otimes \boldsymbol{B}$ is nonsingular. with $(\boldsymbol{A} \otimes \boldsymbol{B})^{-1}=$ $\boldsymbol{A}^{-1} \otimes \boldsymbol{B}^{-1}$.
3. If $\boldsymbol{A}$ and $\boldsymbol{B}$ are symmetric then $\boldsymbol{A} \otimes \boldsymbol{B}$ and $\boldsymbol{A} \otimes \boldsymbol{I}_{s}+\boldsymbol{I}_{r} \otimes \boldsymbol{B}$ are symmetric.
4. $(\boldsymbol{A} \otimes \boldsymbol{B})\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right)=\lambda_{i} \mu_{j}\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right), \quad i=1, \ldots, r, \quad j=1, \ldots, s$,
5. $\left(\boldsymbol{A} \otimes \boldsymbol{I}_{s}+\boldsymbol{I}_{r} \otimes \boldsymbol{B}\right)\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right)=\left(\lambda_{i}+\mu_{j}\right)\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right), \quad i=1, \ldots, r, \quad j=1, \ldots, s$.,
6. If one of $\boldsymbol{A}, \boldsymbol{B}$ is positive definite and the other is positive semidefinite then $\boldsymbol{A} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{B}$ is positive definite.
7. $\boldsymbol{A} \boldsymbol{V} \boldsymbol{B}^{T}=\boldsymbol{F} \quad \Leftrightarrow \quad(\boldsymbol{A} \otimes \boldsymbol{B}) \operatorname{vec}(\boldsymbol{V})=\operatorname{vec}(\boldsymbol{F})$,
8. $\boldsymbol{A} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{B}^{T}=\boldsymbol{F} \quad \Leftrightarrow \quad\left(\boldsymbol{A} \otimes \boldsymbol{I}_{s}+\boldsymbol{I}_{r} \otimes \boldsymbol{B}\right) \operatorname{vec}(\boldsymbol{V})=\operatorname{vec}(\boldsymbol{F})$.

Before giving the simple proofs of this theorem we present some comments.

1. The transpose (or the inverse) of an ordinary matrix product equals the transpose (or the inverse) of the matrices in reverse order. For Kronecker products the order is kept.
2. The eigenvalues of the Kronecker product (sum) are the product (sum) of the eigenvalues of the factors. The eigenvectors are the Kronecker products of the eigenvectors of the factors. In particular, the eigenvalues of the test matrix $\boldsymbol{T}_{2}$ are sums of eigenvalues of $\boldsymbol{T}_{1}$.
3. Since we already know that $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1)$ is positive definite the 2D Poisson matrix $\boldsymbol{A}=\boldsymbol{T} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T}$ is also positive definite.
4. The system $\boldsymbol{A} \boldsymbol{V} \boldsymbol{B}^{T}=\boldsymbol{F}$ in part 7 can be solved by first finding $\boldsymbol{W}$ from $\boldsymbol{A} \boldsymbol{W}=$ $\boldsymbol{F}$, and then finding $\boldsymbol{V}$ from $\boldsymbol{B} \boldsymbol{V}^{T}=\boldsymbol{W}^{T}$. This is preferable to solving the much larger linear system $(\boldsymbol{A} \otimes \boldsymbol{B}) \operatorname{vec}(\boldsymbol{V})=\operatorname{vec}(\boldsymbol{F})$.
5. A fast way to solve the 2D Poisson problem in the form $\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V T}=\boldsymbol{F}$ will be considered in the next chapter.

Proof of Theorem 10.1

1. Exercise.
2. By the mixed product rule $(\boldsymbol{A} \otimes \boldsymbol{B})\left(\boldsymbol{A}^{-1} \otimes \boldsymbol{B}^{-1}\right)=\left(\boldsymbol{A} \boldsymbol{A}^{-1}\right) \otimes\left(\boldsymbol{B} \boldsymbol{B}^{-1}\right)=$ $\boldsymbol{I}_{r} \otimes \boldsymbol{I}_{s}=\boldsymbol{I}_{r s}$. Thus $(\boldsymbol{A} \otimes \boldsymbol{B})$ is nonsingular with the indicated inverse.
3. By $1,(\boldsymbol{A} \otimes \boldsymbol{B})^{T}=\boldsymbol{A}^{T} \otimes \boldsymbol{B}^{T}=\boldsymbol{A} \otimes \boldsymbol{B}$. Moreover, since then $\boldsymbol{A} \otimes \boldsymbol{I}$ and $\boldsymbol{I} \otimes \boldsymbol{B}$ are symmetric, their sum is symmetric.
4. $(\boldsymbol{A} \otimes \boldsymbol{B})\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right)=\left(\boldsymbol{A} \boldsymbol{u}_{i}\right) \otimes\left(\boldsymbol{B} \boldsymbol{v}_{j}\right)=\left(\lambda_{i} \boldsymbol{u}_{i}\right) \otimes\left(\mu_{j} \boldsymbol{v}_{j}\right)=\left(\lambda_{i} \mu_{j}\right)\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right)$, for all $i, j$, where we used the mixed product rule.
5. $\left(\boldsymbol{A} \otimes \boldsymbol{I}_{s}\right)\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right)=\lambda_{i}\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right), \quad$ and $\quad\left(\boldsymbol{I}_{r} \otimes \boldsymbol{B}\right)\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right)=\mu_{j}\left(\boldsymbol{u}_{i} \otimes \boldsymbol{v}_{j}\right)$. The result now follows by summing these relations.
6. By $1, \boldsymbol{A} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{B}$ is symmetric. Moreover, the eigenvalues $\lambda_{i}+\mu_{j}$ are positive since for all $i, j$, both $\lambda_{i}$ and $\mu_{j}$ are nonnegative and one of them is positive. It follows that $\boldsymbol{A} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{B}$ is positive definite.
7. We partition $\boldsymbol{V}, \boldsymbol{F}$, and $\boldsymbol{B}^{T}$ by columns as $\boldsymbol{V}=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{s}\right], \boldsymbol{F}=\left[\boldsymbol{f}_{1}, \ldots, \boldsymbol{f}_{s}\right]$ and $\boldsymbol{B}^{T}=\left[\boldsymbol{b}_{1}, \ldots, \boldsymbol{b}_{s}\right]$. Then we have
$$
\begin{aligned}
(\boldsymbol{A} \otimes \boldsymbol{B}) \operatorname{vec}(\boldsymbol{V}) & =\operatorname{vec}(\boldsymbol{F}) \\
& \Leftrightarrow\left[\begin{array}{ccc}
\boldsymbol{A} b_{11} & \cdots & \boldsymbol{A} b_{1 s} \\
\vdots & & \vdots \\
\boldsymbol{A} b_{s 1} & \cdots & \boldsymbol{A} b_{s s}
\end{array}\right]\left[\begin{array}{c}
\boldsymbol{v}_{1} \\
\vdots \\
\boldsymbol{v}_{s}
\end{array}\right]=\left[\begin{array}{c}
\boldsymbol{f}_{1} \\
\vdots \\
\boldsymbol{f}_{s}
\end{array}\right] \\
& \Leftrightarrow \boldsymbol{A}\left[\sum_{j} b_{1 j} \boldsymbol{v}_{j}, \ldots, \sum_{j} b_{s j} \boldsymbol{v}_{j}\right]=\left[\boldsymbol{f}_{1}, \ldots, \boldsymbol{f}_{s}\right] \\
& \Leftrightarrow \boldsymbol{A}\left[\boldsymbol{V} \boldsymbol{b}_{1}, \ldots, \boldsymbol{V} \boldsymbol{b}_{s}\right]=\boldsymbol{F} \quad \Leftrightarrow \quad \boldsymbol{A} \boldsymbol{V} \boldsymbol{B}^{T}=\boldsymbol{F} .
\end{aligned}
$$
8. From the proof of 7. we have $\left(\boldsymbol{A} \otimes \boldsymbol{I}_{s}\right) \operatorname{vec}(\boldsymbol{V})=\boldsymbol{A} \boldsymbol{V} \boldsymbol{I}_{s}^{T}$ and $\left(\boldsymbol{I}_{r} \otimes \boldsymbol{B}\right) \operatorname{vec}(\boldsymbol{V})=$ $\boldsymbol{I}_{r} \boldsymbol{V} \boldsymbol{B}^{T}$. But then
$$
\begin{aligned}
\left(\boldsymbol{A} \otimes \boldsymbol{I}_{s}+\boldsymbol{I}_{r} \otimes \boldsymbol{B}\right) \operatorname{vec}(\boldsymbol{V}) & =\operatorname{vec}(\boldsymbol{F}) \\
\Leftrightarrow \quad\left(\boldsymbol{A} \boldsymbol{V} \boldsymbol{I}_{s}^{T}+\boldsymbol{I}_{r} \boldsymbol{V} \boldsymbol{B}^{T}\right) & =\boldsymbol{F} \quad \Leftrightarrow \quad \boldsymbol{A} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{B}^{T}=\boldsymbol{F} .
\end{aligned}
$$
For more on Kronecker products see [9]. $\square$

### 10.3 Properties of the 2D Test Matrices

Using Theorem 10.1 we can derive properties of the 2D test matrix $\boldsymbol{T}_{2}$ from those of $\boldsymbol{T}_{1}$. Recall (cf. Lemma 2.2) that $\boldsymbol{T}_{1} \boldsymbol{s}_{j}=\lambda_{j} \boldsymbol{s}_{j}$ for $j=1, \ldots, m$, where

$$
\lambda_{j}=d+2 a \cos (j \pi h), \quad h:=\frac{1}{m+1},
$$

$$
\boldsymbol{s}_{j}=[\sin (j \pi h), \sin (2 j \pi h), \ldots, \sin (m j \pi h)]^{T} .
$$

Moreover, the eigenvalues are distinct and the eigenvectors are orthogonal

$$
\boldsymbol{s}_{j}^{T} \boldsymbol{s}_{k}=\frac{m+1}{2} \delta_{j, k}=\frac{1}{2 h} \delta_{j, k}, \quad j, k=1, \ldots, m .
$$

Theorem 10.2 (Eigenpairs of 2D Test Matrix) For fixed $m \geq 2$ let $\boldsymbol{T}_{2}$ be the matrix given by (10.10) and let $h=1 /(m+1)$. Then

$$
\boldsymbol{T}_{2}\left(\boldsymbol{s}_{j} \otimes \boldsymbol{s}_{k}\right)=\left(\lambda_{j}+\lambda_{k}\right)\left(\boldsymbol{s}_{j} \otimes \boldsymbol{s}_{k}\right) \quad j, k=1, \ldots, m,
$$

where $\left(\lambda_{j}, \boldsymbol{s}_{j}\right)$ are the eigenpairs of $\boldsymbol{T}_{1}$ given by (10.15) and (10.16). The eigenvectors $\boldsymbol{s}_{j} \otimes \boldsymbol{s}_{k}$ are orthogonal

$$
\left(\boldsymbol{s}_{j} \otimes \boldsymbol{s}_{k}\right)^{T}\left(\boldsymbol{s}_{p} \otimes \boldsymbol{s}_{q}\right)=\frac{1}{4 h^{2}} \delta_{j, p} \delta_{k, q}, \quad j, k, p, q=1, \ldots, m,
$$

and $\boldsymbol{T}_{2}$ is positive definite if $d>0$ and $d \geq 2|a|$.
Proof Equation (10.18) follows from Part 5. of Theorem 10.1. Using the transpose rule, the mixed product rule and (2.32) we find for $j, k, p, q=1, \ldots, m$

$$
\left(\boldsymbol{s}_{j} \otimes \boldsymbol{s}_{k}\right)^{T}\left(\boldsymbol{s}_{p} \otimes \boldsymbol{s}_{q}\right)=\left(\boldsymbol{s}_{j}^{T} \otimes \boldsymbol{s}_{k}^{T}\right)\left(\boldsymbol{s}_{p} \otimes \boldsymbol{s}_{q}\right)=\left(\boldsymbol{s}_{j}^{T} \boldsymbol{s}_{p}\right) \otimes\left(\boldsymbol{s}_{k}^{T} \boldsymbol{s}_{q}\right)=\frac{1}{4 h^{2}} \delta_{j, p} \delta_{k, q}
$$

and (10.19) follows. Since $\boldsymbol{T}_{2}$ is symmetric, $\boldsymbol{T}_{2}$ is positive definite if the $\lambda_{j}$ given by (10.15) are positive. But this is true whenever $d>0$ and $d \geq 2|a|$ (cf. Exercise 10.5). $\square$

Corollary 10.1 The spectral condition number of the discrete Poisson matrix $\boldsymbol{A} \in$ $\mathbb{R}^{m^{2} \times m^{2}}$ given by (10.8) is given by

$$
\|\boldsymbol{A}\|_{2}\left\|\boldsymbol{A}^{-1}\right\|_{2}=\frac{\cos ^{2} w}{\sin ^{2} w}, \quad w:=\frac{\pi}{2(m+1)}
$$

Proof Recall that by (10.15) with $d=2, a=-1$, and (10.18), the eigenvalues $\lambda_{j, k}$ of $\boldsymbol{A}$ are

$$
\lambda_{j, k}=4-2 \cos (2 j w)-2 \cos (2 k w)=4 \sin ^{2}(j w)+4 \sin ^{2}(k w), \quad j, k=1, \ldots, m .
$$

Using trigonometric formulas, it follows that the largest and smallest eigenvalue of $\boldsymbol{A}$, are given by

$$
\lambda_{\max }=8 \cos ^{2} w, \quad \lambda_{\min }=8 \sin ^{2} w .
$$

Since $d>0$ and $d \geq 2|a|$ it follows that $\boldsymbol{A}$ is positive definite. By (8.26) we have $\|\boldsymbol{A}\|_{2}\left\|\boldsymbol{A}^{-1}\right\|_{2}=\frac{\lambda_{\text {max }}}{\lambda_{\text {min }}}$ and (10.20) follows. $\square$

### 10.4 Exercises Chap. 10

### 10.4.1 Exercises Sects. 10.1, 10.2

Exercise 10.1 (4 × 4 Poisson Matrix) Write down the Poisson matrix for $m=2$ and show that it is strictly diagonally dominant.

Exercise 10.2 (Properties of Kronecker Products) Prove (10.13).
Exercise 10.3 (Eigenpairs of Kronecker Products (Exam Exercise 2008-3)) Let $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{R}^{n \times n}$. Show that the eigenvalues of the Kronecker product $\boldsymbol{A} \otimes \boldsymbol{B}$ are products of the eigenvalues of $\boldsymbol{A}$ and $\boldsymbol{B}$ and that the eigenvectors of $\boldsymbol{A} \otimes \boldsymbol{B}$ are Kronecker products of the eigenvectors of $\boldsymbol{A}$ and $\boldsymbol{B}$.

### 10.4.2 Exercises Sect. 10.3

Exercise 10.4 (2. Derivative Matrix Is Positive Definite) Write down the eigenvalues of $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1)$ using (10.15) and conclude that $\boldsymbol{T}$ is symmetric positive definite.

Exercise 10.5 (1D Test Matrix Is Positive Definite?) Show that the matrix $\boldsymbol{T}_{1}$ is symmetric positive definite if $d>0$ and $d \geq 2|a|$.

Exercise 10.6 (Eigenvalues for 2D Test Matrix of Order 4) For $m=2$ the matrix (10.10) is given by

$$
\boldsymbol{A}=\left[\begin{array}{rrrr}
2 d & a & a & 0 \\
a & 2 d & 0 & a \\
a & 0 & 2 d & a \\
0 & a & a & 2 d
\end{array}\right] .
$$

Show that $\lambda=2 a+2 d$ is an eigenvalue corresponding to the eigenvector $\boldsymbol{x}=$ $[1,1,1,1]^{T}$. Verify that apart from a scaling of the eigenvector this agrees with (10.15) and (10.16) for $j=k=1$ and $m=2$.

Exercise 10.7 (Nine Point Scheme for Poisson Problem) Consider the following 9 point difference approximation to the Poisson problem $-\Delta u=f, u=0$ on the
boundary of the unit square (cf. (10.1))


(a) $-\left(\square_{h} v\right)_{j, k}=(\mu f)_{j, k}$ $j, k=1, \ldots, m$
(b) $0=v_{0, k}=v_{m+1, k}=v_{j, 0}=v_{j, m+1}, j, k=0,1, \ldots, m+1$,
(c) $-\left(\square_{h} v\right)_{j, k}=\left[20 v_{j, k}-4 v_{j-1, k}-4 v_{j, k-1}-4 v_{j+1, k}-4 v_{j, k+1}\right.$ $\left.-v_{j-1, k-1}-v_{j+1, k-1}-v_{j-1, k+1}-v_{j+1, k+1}\right] /\left(6 h^{2}\right)$,
(d) $(\mu f)_{j, k}=\left[8 f_{j, k}+f_{j-1, k}+f_{j, k-1}+f_{j+1, k}+f_{j, k+1}\right] / 12$.
a) Write down the 4-by-4 system we obtain for $m=2$.
b) Find $v_{j, k}$ for $j, k=1,2$, if $f(x, y)=2 \pi^{2} \sin (\pi x) \sin (\pi y)$ and $m=2$. Answer: $v_{j, k}=5 \pi^{2} / 66$.

It can be shown that (10.21) defines an $O\left(h^{4}\right)$ approximation to (10.1).
Exercise 10.8 (Matrix Equation for Nine Point Scheme) Consider the nine point difference approximation to (10.1) given by (10.21) in Problem 10.7.

a) Show that (10.21) is equivalent to the matrix equation
$$
\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}-\frac{1}{6} \boldsymbol{T} \boldsymbol{V} \boldsymbol{T}=h^{2} \mu \boldsymbol{F}
$$
Here $\mu \boldsymbol{F}$ has elements $(\mu f)_{j, k}$ given by (10.21d) and $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1)$.
b) Show that the standard form of the matrix equation (10.22) is $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A}=\boldsymbol{T} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T}-\frac{1}{6} \boldsymbol{T} \otimes \boldsymbol{T}, \boldsymbol{x}=\operatorname{vec}(\boldsymbol{V})$, and $\boldsymbol{b}=h^{2} \operatorname{vec}(\mu \boldsymbol{F})$.

Exercise 10.9 (Biharmonic Equation) Consider the biharmonic equation

$$
\begin{array}{ll}
\Delta^{2} u(s, t):=\Delta(\Delta u(s, t))=f(s, t) & (s, t) \in \Omega, \\
u(s, t)=0, & \Delta u(s, t)=0
\end{array}
$$

Here $\Omega$ is the open unit square. The condition $\Delta u=0$ is called the Navier boundary condition. Moreover, $\Delta^{2} u=u_{x x x x}+2 u_{x x y y}+u_{y y y y}$.

a) Let $v=-\Delta u$. Show that (10.23) can be written as a system
$$
\begin{array}{rlrl}
-\Delta v(s, t) & =f(s, t) & & (s, t) \in \Omega \\
-\Delta u(s, t) & =v(s, t) & & (s, t) \in \Omega \\
u(s, t) & =v(s, t)=0 & (s, t) \in \partial \Omega
\end{array}
$$
b) Discretizing, using (10.4), with $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1) \in \mathbb{R}^{m \times m}, h=1 /(m+$ 1 ), and $\boldsymbol{F}=(f(j h, k h))_{j, k=1}^{m}$ we get two matrix equations
$$
\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}=h^{2} \boldsymbol{F}, \quad \boldsymbol{T} \boldsymbol{U}+\boldsymbol{U} \boldsymbol{T}=h^{2} \boldsymbol{V} .
$$

Show that
$$
(\boldsymbol{T} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T}) \operatorname{vec}(\boldsymbol{V})=h^{2} \operatorname{vec}(\boldsymbol{F}), \quad(\boldsymbol{T} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T}) \operatorname{vec}(\boldsymbol{U})=h^{2} \operatorname{vec}(\boldsymbol{V}) .
$$
and hence $\boldsymbol{A}=(\boldsymbol{T} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T})^{2}$ is the matrix for the standard form of the discrete biharmonic equation.
c) Show that with $n=m^{2}$ the vector form and standard form of the systems in b) can be written
$$
\boldsymbol{T}^{2} \boldsymbol{U}+2 \boldsymbol{T} \boldsymbol{U} \boldsymbol{T}+\boldsymbol{U} \boldsymbol{T}^{2}=h^{4} \boldsymbol{F} \quad \text { and } \quad \boldsymbol{A} \boldsymbol{x}=\boldsymbol{b},
$$
where $\boldsymbol{A}=\boldsymbol{T}^{2} \otimes \boldsymbol{I}+2 \boldsymbol{T} \otimes \boldsymbol{T}+\boldsymbol{I} \otimes \boldsymbol{T}^{2} \in \mathbb{R}^{n \times n}, \boldsymbol{x}=\operatorname{vec}(\boldsymbol{U})$, and $\boldsymbol{b}=h^{4} \operatorname{vec}(\boldsymbol{F})$.
d) Determine the eigenvalues and eigenvectors of the matrix $\boldsymbol{A}$ in c) and show that it is positive definite. Also determine the bandwidth of $\boldsymbol{A}$.
e) Suppose we want to solve the standard form equation $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. We have two representations for the matrix $\boldsymbol{A}$, the product one in $\mathbf{b}$ ) and the one in $\mathbf{c}$ ). Which one would you prefer for the basis of an algorithm? Why?

### 10.5 Review Questions

10.5.1 Consider the Poisson matrix.
    - Write this matrix as a Kronecker sum,
    - how are its eigenvalues and eigenvectors related to the second derivative matrix?
    - is it symmetric? positive definite?
10.5.2 What are the eigenpairs of $\boldsymbol{T}_{1}:=\operatorname{tridiagonal}(a, d, a)$ ?
10.5.3 What are the inverse and transpose of a Kronecker product?
10.5.4
    - give an economical general way to solve the linear system $(\boldsymbol{A} \otimes$ $\boldsymbol{B}) \operatorname{vec}(\boldsymbol{V})=\operatorname{vec}(\boldsymbol{F})$ ?
    - Same for $\left(\boldsymbol{A} \otimes \boldsymbol{I}_{s}+\boldsymbol{I}_{r} \otimes \boldsymbol{B}\right) \operatorname{vec}(\boldsymbol{V})=\operatorname{vec}(\boldsymbol{F})$.

## Chapter 11 <br> Fast Direct Solution of a Large Linear System

### 11.1 Algorithms for a Banded Positive Definite System

In this chapter we present a fast method for solving $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A}$ is the Poisson matrix (10.8). Thus, for $n=9$

$$
\begin{aligned}
\boldsymbol{A} & =\left[\begin{array}{rrr|rrr|rrr}
4 & -1 & 0 & -1 & 0 & 0 & 0 & 0 & 0 \\
-1 & 4 & -1 & 0 & -1 & 0 & 0 & 0 & 0 \\
0 & -1 & 4 & 0 & 0 & -1 & 0 & 0 & 0 \\
\hline-1 & 0 & 0 & 4 & -1 & 0 & -1 & 0 & 0 \\
0 & -1 & 0 & -1 & 4 & -1 & 0 & -1 & 0 \\
0 & 0 & -1 & 0 & -1 & 4 & 0 & 0 & -1 \\
\hline 0 & 0 & 0 & -1 & 0 & 0 & 4 & -1 & 0 \\
0 & 0 & 0 & 0 & -1 & 0 & -1 & 4 & -1 \\
0 & 0 & 0 & 0 & 0 & -1 & 0-1 & 4
\end{array}\right] \\
& =\left[\begin{array}{ccc}
\boldsymbol{T}+2 \boldsymbol{I} & -\boldsymbol{I} & \mathbf{0} \\
-\boldsymbol{I} & \boldsymbol{T}+2 \boldsymbol{I} & -\boldsymbol{I} \\
\mathbf{0} & -\boldsymbol{I} & \boldsymbol{T}+2 \boldsymbol{I}
\end{array}\right],
\end{aligned}
$$

where $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1)$. For the matrix $\boldsymbol{A}$ we know by now that

1. It is positive definite.
2. It is banded.
3. It is block-tridiagonal.
4. We know the eigenvalues and eigenvectors of $\boldsymbol{A}$.
5. The eigenvectors are orthogonal.

### 11.1.1 Cholesky Factorization

Since $\boldsymbol{A}$ is positive definite we can use the Cholesky factorization $\boldsymbol{A}=\boldsymbol{L} \boldsymbol{L}^{*}$, with $\boldsymbol{L}$ lower triangular, to solve $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Since $\boldsymbol{A}$ and $\boldsymbol{L}$ has the same bandwidth $d=\sqrt{n}$ the complexity of this factorization is $O\left(n d^{2}\right)=O\left(n^{2}\right)$, cf. Algorithm 4.2. We need to store $\boldsymbol{A}$, and this can be done in sparse form.

The nonzero elements in $\boldsymbol{L}$ are shown in Fig. 11.1 for $n=100$. Note that most of the zeros between the diagonals in $\boldsymbol{A}$ have become nonzero in $\boldsymbol{L}$. This is known as fill-inn.

### 11.1.2 Block LU Factorization of a Block Tridiagonal Matrix

The Poisson matrix has a block tridiagonal structure. Consider finding the block LU factorization of a block tridiagonal matrix. We are looking for a factorization of the form

$$
\left[\begin{array}{cccc}
\boldsymbol{D}_{1} & \boldsymbol{C}_{1} & & \\
\boldsymbol{A}_{1} & \boldsymbol{D}_{2} & \boldsymbol{C}_{2} & \\
& \ddots & \ddots & \ddots \\
& & \boldsymbol{A}_{m-2} & \boldsymbol{D}_{m-1} \\
& & \boldsymbol{A}_{m-1} & \boldsymbol{D}_{m}
\end{array}\right]=\left[\begin{array}{cccc}
\boldsymbol{I} & & & \\
\boldsymbol{L}_{1} & \boldsymbol{I} & & \\
& \ddots & \ddots & \\
& & \boldsymbol{L}_{m-1} & \boldsymbol{I}
\end{array}\right]\left[\begin{array}{cccc}
\boldsymbol{U}_{1} & \boldsymbol{C}_{1} & & \\
& \ddots & \ddots & \\
& & \boldsymbol{U}_{m-1} & \boldsymbol{C}_{m-1} \\
& & & \boldsymbol{U}_{m}
\end{array}\right] .
$$

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-251.jpg?height=788&width=777&top_left_y=1215&top_left_x=376)
Fig. 11.1 Fill-inn in the Cholesky factor of the Poisson matrix $(n=100)$

Here $\boldsymbol{D}_{1}, \ldots, \boldsymbol{D}_{m}$ and $\boldsymbol{U}_{1}, \ldots, \boldsymbol{U}_{m}$ are square matrices while $\boldsymbol{A}_{1}, \ldots, \boldsymbol{A}_{m-1}, \boldsymbol{L}_{1}$, $\ldots, \boldsymbol{L}_{m-1}$ and $\boldsymbol{C}_{1}, \ldots, \boldsymbol{C}_{m-1}$ can be rectangular.

Using block multiplication the formulas (2.16) generalize to

$$
\boldsymbol{U}_{1}=\boldsymbol{D}_{1}, \quad \boldsymbol{L}_{k}=\boldsymbol{A}_{k} \boldsymbol{U}_{k}^{-1}, \quad \boldsymbol{U}_{k+1}=\boldsymbol{D}_{k+1}-\boldsymbol{L}_{k} \boldsymbol{C}_{k}, \quad k=1,2, \ldots, m-1 .
$$

To solve the system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ we partition $\boldsymbol{b}$ conformally with $\boldsymbol{A}$ in the form $\boldsymbol{b}^{T}=$ $\left[\boldsymbol{b}_{1}^{T}, \ldots, \boldsymbol{b}_{m}^{T}\right]$. The formulas for solving $\boldsymbol{L} \boldsymbol{y}=\boldsymbol{b}$ and $\boldsymbol{U} \boldsymbol{x}=\boldsymbol{y}$ are as follows:

$$
\begin{aligned}
\boldsymbol{y}_{1} & =\boldsymbol{b}_{1}, \quad \boldsymbol{y}_{k}=\boldsymbol{b}_{k}-\boldsymbol{L}_{k-1} \boldsymbol{y}_{k-1}, \quad k=2,3, \ldots, m, \\
\boldsymbol{x}_{m} & =\boldsymbol{U}_{m}^{-1} \boldsymbol{y}_{m}, \quad \boldsymbol{x}_{k}=\boldsymbol{U}_{k}^{-1}\left(\boldsymbol{y}_{k}-\boldsymbol{C}_{k} \boldsymbol{x}_{k+1}\right), \quad k=m-1, \ldots, 2,1 .
\end{aligned}
$$

The solution is then $\boldsymbol{x}^{T}=\left[\boldsymbol{x}_{1}^{T}, \ldots, \boldsymbol{x}_{m}^{T}\right]$. To find $\boldsymbol{L}_{k}$ in (11.2) we solve the linear systems $\boldsymbol{L}_{k} \boldsymbol{U}_{k}=\boldsymbol{A}_{k}$. Similarly we need to solve a linear system to find $\boldsymbol{x}_{k}$ in (11.3).

The number of arithmetic operations using block factorizations is $O\left(n^{2}\right)$, asymptotically the same as for Cholesky factorization. However we only need to store the $m \times m$ blocks, and using matrix operations can be advantageous.

### 11.1.3 Other Methods

Other methods include

- Iterative methods, (we study this in Chaps. 12 and 13),
- multigrid. See [5],
- fast solvers based on diagonalization and the fast Fourier transform. See Sects. 11.2, 11.3.

### 11.2 A Fast Poisson Solver Based on Diagonalization

The algorithm we now derive will only require $O\left(n^{3 / 2}\right)$ arithmetic operations and we only need to work with matrices of order $m$. Using the fast Fourier transform the number of arithmetic operations can be reduced further to $O(n \log n)$.

To start we recall that $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ can be written as a matrix equation in the form (cf. (10.5))

$$
\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}=h^{2} \boldsymbol{F} \quad \text { with } \quad h=1 /(m+1),
$$

where $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1) \in \mathbb{R}^{m \times m}$ is the second derivative matrix, $\boldsymbol{V}=$ $\left(v_{j, k}\right) \in \mathbb{R}^{m \times m}$ are the unknowns, and $\boldsymbol{F}=\left(f_{j, k}\right)=(f(j h, k h)) \in \mathbb{R}^{m \times m}$ contains function values.

Recall (cf. Lemma 2.2) that the eigenpairs of $\boldsymbol{T}$ are given by

$$
\begin{aligned}
\boldsymbol{T s}_{j} & =\lambda_{j} \boldsymbol{s}_{j}, \quad j=1, \ldots, m, \\
\boldsymbol{s}_{j} & =[\sin (j \pi h), \sin (2 j \pi h), \ldots, \sin (m j \pi h)]^{T}, \\
\lambda_{j} & =2-2 \cos (j \pi h)=4 \sin ^{2}(j \pi h / 2), \quad h=1 /(m+1), \\
\boldsymbol{s}_{j}^{T} \boldsymbol{s}_{k} & =\delta_{j, k} /(2 h) \text { for all } j, k .
\end{aligned}
$$

Let

$$
\boldsymbol{S}:=\left[\boldsymbol{s}_{1}, \ldots, \boldsymbol{s}_{m}\right]=[\sin (j k \pi h)]_{j, k=1}^{m} \in \mathbb{R}^{m \times m}, \quad \boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{m}\right) .
$$

Then

$$
\boldsymbol{T} \boldsymbol{S}=\left[\boldsymbol{T} \boldsymbol{s}_{1}, \ldots, \boldsymbol{T} \boldsymbol{s}_{m}\right]=\left[\lambda_{1} \boldsymbol{s}_{1}, \ldots, \lambda_{m} \boldsymbol{s}_{m}\right]=\boldsymbol{S} \boldsymbol{D}, \quad \boldsymbol{S}^{2}=\boldsymbol{S}^{T} \boldsymbol{S}=\frac{1}{2 h} \boldsymbol{I} .
$$

Define $\boldsymbol{X} \in \mathbb{R}^{m \times m}$ by $\boldsymbol{V}=\boldsymbol{S} \boldsymbol{X} \boldsymbol{S}$, where $\boldsymbol{V}$ is the solution of $\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}=h^{2} \boldsymbol{F}$. Then

$$
\begin{array}{rl}
\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T} & =h^{2} \boldsymbol{F} \\
\boldsymbol{V}^{\boldsymbol{V}=\boldsymbol{S} \boldsymbol{X} \boldsymbol{S}} \boldsymbol{T} \boldsymbol{S} \boldsymbol{X} \boldsymbol{S}+\boldsymbol{S} \boldsymbol{X} \boldsymbol{S} \boldsymbol{T} & =h^{2} \boldsymbol{F} \\
\stackrel{\boldsymbol{S}() \boldsymbol{S}}{\Longleftrightarrow} \boldsymbol{S} \boldsymbol{T} \boldsymbol{S} \boldsymbol{X} \boldsymbol{S}^{2}+\boldsymbol{S}^{2} \boldsymbol{X} \boldsymbol{S} \boldsymbol{T} \boldsymbol{S} & =h^{2} \boldsymbol{S} \boldsymbol{F} \boldsymbol{S}=h^{2} \boldsymbol{G} \\
\stackrel{\boldsymbol{T}}{\Leftrightarrow} \boldsymbol{S}^{\mathbf{2}} \boldsymbol{D} & \boldsymbol{S} \boldsymbol{X} \boldsymbol{S}^{2}+\boldsymbol{S}^{2} \boldsymbol{X} \boldsymbol{S}^{2} \boldsymbol{D} \\
\boldsymbol{S}^{2} & =h^{2} \boldsymbol{G} \\
\Longleftrightarrow & \boldsymbol{I} /(2 h)
\end{array}
$$

Since $\boldsymbol{D}$ is diagonal, the equation $\boldsymbol{D} \boldsymbol{X}+\boldsymbol{X} \boldsymbol{D}=4 h^{4} \boldsymbol{G}$, is easy to solve. For the $j, k$ element we find

$$
(\boldsymbol{D} \boldsymbol{X}+\boldsymbol{X} \boldsymbol{D})_{j, k}=\sum_{\ell=1}^{m} d_{j, \ell} x_{\ell, k}+\sum_{\ell=1}^{m} x_{j, \ell} d_{\ell, k}=\lambda_{j} x_{j, k}+\lambda_{k} x_{j, k}
$$

so that for all $j, k$

$$
x_{j, k}=4 h^{4} g_{j, k} /\left(\lambda_{j}+\lambda_{k}\right)=h^{4} g_{j, k} /\left(\sigma_{j}+\sigma_{k}\right), \quad \sigma_{j}:=\lambda_{j} / 4=\sin ^{2}(j \pi h / 2) .
$$

Thus to find $\boldsymbol{V}$ we compute

1. $\boldsymbol{G}=\boldsymbol{S} \boldsymbol{F} \boldsymbol{S}$,
2. $x_{j, k}=h^{4} g_{j, k} /\left(\sigma_{j}+\sigma_{k}\right), \quad j, k=1, \ldots, m$,
3. $\boldsymbol{V}=\boldsymbol{S} \boldsymbol{X} \boldsymbol{S}$.

We can compute $\boldsymbol{X}, \boldsymbol{S}$ and the $\sigma$ 's without using loops. Using outer products, element by element division, and raising a matrix element by element to a power we find

$$
\begin{aligned}
& \boldsymbol{X}=h^{4} \boldsymbol{G} / \boldsymbol{M}, \text { where } \boldsymbol{M}:=\left[\begin{array}{c}
\sigma_{1} \\
\vdots \\
\sigma_{m}
\end{array}\right][1, \ldots, 1]+\left[\begin{array}{c}
1 \\
\vdots \\
i
\end{array}\right]\left[\sigma_{1} \ldots . \sigma_{m}\right], \\
& \boldsymbol{S}=\sin \left(\pi h\left[\begin{array}{c}
1 \\
2 \\
\vdots \\
m
\end{array}\right][12 \ldots m]\right), \quad \boldsymbol{\sigma}=\sin \left(\frac{\pi h}{2}\left[\begin{array}{c}
1 \\
2 \\
\vdots \\
m
\end{array}\right]\right) \wedge 2 .
\end{aligned}
$$

We now get the following algorithm to solve numerically the Poisson problem $-\Delta u=f$ on $\Omega=(0,1)^{2}$ and $u=0$ on $\partial \Omega$ using the 5-point scheme, i.e., let $m \in$ $\mathbb{N}, h=1 /(m+1)$, and $\boldsymbol{F}=(f(j h, k h)) \in \mathbb{R}^{m \times m}$. We compute $\boldsymbol{V} \in \mathbb{R}^{(m+2) \times(m+2)}$ using diagonalization of $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1) \in \mathbb{R}^{m \times m}$.

```
function V=fastpoisson(F)
%function V=fastpoisson (F)
m=length(F); h=1/(m+1); hv=pi*h*(1:m)';
sigma=sin(hv/2).^2;
S=sin(hv*(1:m));
G=S*F*S;
X=h^4*G./(sigma*ones(1,m)+ ones(m,1)*sigma′);
V=zeros (m+2,m+2) ;
V(2:m+1,2:m+1)=S*X*S;
end
```

Listing 11.1 fastpoisson

The formulas are fully vectorized. Since the 6th line in Algorithm 11.1 only requires $O\left(m^{3}\right)$ arithmetic operations, the complexity of this algorithm is for large $m$ determined by $4 m$-by- $m$ matrix multiplications and is given by $O\left(4 \times 2 m^{3}\right)=$ $O\left(8 n^{3 / 2}\right) .{ }^{1}$ The method is very fast and will be used as a preconditioner for a more complicated problem in Chap. 13. In 2012 it took about 0.2 seconds on a laptop to find the $10^{6}$ unknowns $v_{j, k}$ on a $1000 \times 1000$ grid.

[^20]
### 11.3 A Fast Poisson Solver Based on the Discrete Sine and Fourier Transforms

In Algorithm 11.1 we need to compute the product of the sine matrix $\boldsymbol{S} \in \mathbb{R}^{m \times m}$ given by (11.4) and a matrix $\boldsymbol{A} \in \mathbb{R}^{m \times m}$. Since the matrices are $m$-by- $m$ this will normally require $O\left(m^{3}\right)$ operations. In this section we show that it is possible to calculate the products $\boldsymbol{S} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{S}$ in $O\left(m^{2} \log _{2} m\right)$ operations.

We need to discuss certain transforms known as the discrete sine transform, the discrete Fourier transform and the fast Fourier transform. In addition we have the discrete cosine transform which will not be discussed here. These transforms are of independent interest. They have applications to signal processing and image analysis, and are often used when one is dealing with discrete samples of data on a computer.

### 11.3.1 The Discrete Sine Transform (DST)

Given $\boldsymbol{v}=\left[v_{1}, \ldots, v_{m}\right]^{T} \in \mathbb{R}^{m}$ we say that the vector $\boldsymbol{w}=\left[w_{1}, \ldots, w_{m}\right]^{T}$ given by

$$
w_{j}=\sum_{k=1}^{m} \sin \left(\frac{j k \pi}{m+1}\right) v_{k}, \quad j=1, \ldots, m
$$

is the discrete sine transform (DST) of $\boldsymbol{v}$. In matrix form we can write the DST as the matrix times vector $\boldsymbol{w}=\boldsymbol{S} \boldsymbol{v}$, where $\boldsymbol{S}$ is the sine matrix given by (11.4). We can then identify the matrix $\boldsymbol{B}=\boldsymbol{S} \boldsymbol{A}$ as the DST of $\boldsymbol{A} \in \mathbb{R}^{m, n}$, i.e. as the DST of the columns of $\boldsymbol{A}$. The product $\boldsymbol{B}=\boldsymbol{A} \boldsymbol{S}$ can also be interpreted as a DST. Indeed, since $\boldsymbol{S}$ is symmetric we have $\boldsymbol{B}=\left(\boldsymbol{S} \boldsymbol{A}^{T}\right)^{T}$ which means that $\boldsymbol{B}$ is the transpose of the DST of the rows of $\boldsymbol{A}$. It follows that we can compute the unknowns $\boldsymbol{V}$ in Algorithm 11.1 by carrying out discrete sine transforms on $4 m$-by- $m$ matrices in addition to the computation of $\boldsymbol{X}$.

### 11.3.2 The Discrete Fourier Transform (DFT)

The fast computation of the DST is based on its relation to the discrete Fourier transform (DFT) and the fact that the DFT can be computed by a technique known as the fast Fourier transform (FFT). To define the DFT let for $N \in \mathbb{N}$

$$
\omega_{N}=\exp ^{-2 \pi i / N}=\cos (2 \pi / N)-i \sin (2 \pi / N),
$$

where $i=\sqrt{-1}$ is the imaginary unit. Given $\boldsymbol{y}=\left[y_{1}, \ldots, y_{N}\right]^{T} \in \mathbb{R}^{N}$ we say that $z=\left[z_{1}, \ldots, z_{N}\right]^{T}$ given by

$$
z_{j+1}=\sum_{k=0}^{N-1} \omega_{N}^{j k} y_{k+1}, \quad j=0, \ldots, N-1,
$$

is the discrete Fourier transform (DFT) of $\boldsymbol{y}$. We can write this as a matrix times vector product $\boldsymbol{z}=\boldsymbol{F}_{N} \boldsymbol{y}$, where the Fourier matrix $\boldsymbol{F}_{N} \in \mathbb{C}^{N \times N}$ has elements $\omega_{N}^{j k}, j, k=0,1, \ldots, N-1$. For a matrix we say that $\boldsymbol{B}=\boldsymbol{F}_{N} \boldsymbol{A}$ is the DFT of $\boldsymbol{A}$.

As an example, since

$$
\omega_{4}=\exp ^{-2 \pi i / 4}=\cos (\pi / 2)-i \sin (\pi / 2)=-i
$$

we find $\omega_{4}^{2}=(-i)^{2}=-1, \omega_{4}^{3}=(-i)(-1)=i, \omega_{4}^{4}=(-1)^{2}=1, \omega_{4}^{6}=i^{2}=-1$, $\omega_{4}^{9}=i^{3}=-i$, and so

$$
\boldsymbol{F}_{4}=\left[\begin{array}{cccc}
1 & 1 & 1 & 1 \\
1 & \omega_{4} & \omega_{4}^{2} & \omega_{4}^{3} \\
1 & \omega_{4}^{2} & \omega_{4}^{4} & \omega_{4}^{6} \\
1 & \omega_{4}^{3} & \omega_{4}^{6} & \omega_{4}^{9}
\end{array}\right]=\left[\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
1 & -i & -1 & i \\
1 & -1 & 1 & -1 \\
1 & i & -1 & -i
\end{array}\right] .
$$

The following lemma shows how the discrete sine transform of order $m$ can be computed from the discrete Fourier transform of order $2 m+2$. We recall that for any complex number $w$

$$
\sin w=\frac{e^{i w}-e^{-i w}}{2 i} .
$$

Lemma 11.1 (Sine Transform as Fourier Transform) Given a positive integer $m$ and a vector $\boldsymbol{x} \in \mathbb{R}^{m}$. Component $k$ of $\boldsymbol{S} \boldsymbol{x}$ is equal to $i / 2$ times component $k+1$ of $\boldsymbol{F}_{2 m+2} \boldsymbol{z}$ where

$$
\boldsymbol{z}^{T}=\left[0, \boldsymbol{x}^{T}, 0,-\boldsymbol{x}_{B}^{T}\right] \in \mathbb{R}^{2 m+2}, \quad \boldsymbol{x}_{B}^{T}:=\left[x_{m}, \ldots, x_{2}, x_{1}\right] .
$$

In symbols

$$
(\boldsymbol{S} \boldsymbol{x})_{k}=\frac{i}{2}\left(\boldsymbol{F}_{2 m+2} \boldsymbol{z}\right)_{k+1}, \quad k=1, \ldots, m .
$$

Proof Let $\omega=\omega_{2 m+2}=e^{-2 \pi i /(2 m+2)}=e^{-\pi i /(m+1)}$. We note that

$$
\omega^{j k}=e^{-\pi i j k /(m+1)}, \quad \omega^{(2 m+2-j) k}=e^{-2 \pi i} e^{\pi i j k /(m+1)}=e^{\pi i j k /(m+1)} .
$$

Component $k+1$ of $\boldsymbol{F}_{2 m+2} \boldsymbol{z}$ is then given by

$$
\begin{aligned}
\left(\boldsymbol{F}_{2 m+2} \boldsymbol{z}\right)_{k+1} & =\sum_{j=0}^{2 m-1} \omega^{j k} z_{j+1}=\sum_{j=1}^{m} x_{j} \omega^{j k}-\sum_{j=1}^{m} x_{j} \omega^{(2 m+2-j) k} \\
& =\sum_{j=1}^{m} x_{j}\left(e^{-\pi i j k /(m+1)}-e^{\pi i j k /(m+1)}\right) \\
& =-2 i \sum_{j=1}^{m} x_{j} \sin \left(\frac{j k \pi}{m+1}\right)=-2 i\left(\boldsymbol{S}_{m} \boldsymbol{x}\right)_{k} .
\end{aligned}
$$

Dividing both sides by $-2 i$ and noting $-1 /(2 i)=-i /\left(2 i^{2}\right)=i / 2$, proves the lemma. $\square$

It follows that we can compute the DST of length $m$ by extracting $m$ components from the DFT of length $N=2 m+2$.

### 11.3.3 The Fast Fourier Transform (FFT)

From a linear algebra viewpoint the fast Fourier transform is a quick way to compute the matrix- vector product $\boldsymbol{F}_{N} \boldsymbol{y}$. Suppose $N$ is even. The key to the FFT is a connection between $\boldsymbol{F}_{N}$ and $\boldsymbol{F}_{N / 2}$ which makes it possible to compute the FFT of order $N$ as two FFT's of order $N / 2$. By repeating this process we can reduce the number of arithmetic operations to compute a DFT from $O\left(N^{2}\right)$ to $O\left(N \log _{2} N\right)$.

Suppose $N$ is even. The connection between $\boldsymbol{F}_{N}$ and $\boldsymbol{F}_{N / 2}$ involves a permutation matrix $\boldsymbol{P}_{N} \in \mathbb{R}^{N \times N}$ given by

$$
\boldsymbol{P}_{N}=\left[\boldsymbol{e}_{1}, \boldsymbol{e}_{3}, \ldots, \boldsymbol{e}_{N-1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{4}, \ldots, \boldsymbol{e}_{N}\right],
$$

where the $\boldsymbol{e}_{k}=\left(\delta_{j, k}\right)$ are unit vectors. If $\boldsymbol{A}$ is a matrix with $N$ columns $\left[\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{N}\right]$ then

$$
\boldsymbol{A} \boldsymbol{P}_{N}=\left[\boldsymbol{a}_{1}, \boldsymbol{a}_{3}, \ldots, \boldsymbol{a}_{N-1}, \boldsymbol{a}_{2}, \boldsymbol{a}_{4}, \ldots, \boldsymbol{a}_{N}\right],
$$

i.e. post multiplying $\boldsymbol{A}$ by $\boldsymbol{P}_{N}$ permutes the columns of $\boldsymbol{A}$ so that all the odd-indexed columns are followed by all the even-indexed columns. For example we have from (11.6)

$$
\boldsymbol{P}_{4}=\left[\begin{array}{lll}
\boldsymbol{e}_{1} & \boldsymbol{e}_{3} & \boldsymbol{e}_{2} \\
\boldsymbol{e}_{4}
\end{array}\right]=\left[\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right] \quad \boldsymbol{F}_{4} \boldsymbol{P}_{4}=\left[\begin{array}{rr|rr}
1 & 1 & 1 & 1 \\
1 & -1 & -i & i \\
\hline 1 & 1 & -1 & -1 \\
1 & -1 & i & -i
\end{array}\right],
$$

where we have indicated a certain block structure of $\boldsymbol{F}_{4} \boldsymbol{P}_{4}$. These blocks can be related to the 2-by-2 matrix $\boldsymbol{F}_{2}$. We define the diagonal scaling matrix $\boldsymbol{D}_{2}$ by

$$
\boldsymbol{D}_{2}=\operatorname{diag}\left(1, \omega_{4}\right)=\left[\begin{array}{rr}
1 & 0 \\
0 & -i
\end{array}\right] .
$$

Since $\omega_{2}=\exp ^{-2 \pi i / 2}=-1$ we find

$$
\boldsymbol{F}_{2}=\left[\begin{array}{rr}
1 & 1 \\
1 & -1
\end{array}\right], \quad \boldsymbol{D}_{2} \boldsymbol{F}_{2}=\left[\begin{array}{rr}
1 & 1 \\
-i & i
\end{array}\right],
$$

and we see that

$$
\boldsymbol{F}_{4} \boldsymbol{P}_{4}=\left[\begin{array}{r|r}
\boldsymbol{F}_{2} & \boldsymbol{D}_{2} \boldsymbol{F}_{2} \\
\hline \boldsymbol{F}_{2} & -\boldsymbol{D}_{2} \boldsymbol{F}_{2}
\end{array}\right] .
$$

This result holds in general.
Theorem 11.1 (Fast Fourier Transform) If $N=2 m$ is even then

$$
\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m}=\left[\begin{array}{c|c}
\boldsymbol{F}_{m} & \boldsymbol{D}_{m} \boldsymbol{F}_{m} \\
\hline \boldsymbol{F}_{m} & -\boldsymbol{D}_{m} \boldsymbol{F}_{m}
\end{array}\right],
$$

where

$$
\boldsymbol{D}_{m}=\operatorname{diag}\left(1, \omega_{N}, \omega_{N}^{2}, \ldots, \omega_{N}^{m-1}\right) .
$$

Proof Fix integers $p, q$ with $1 \leq p, q \leq m$ and set $j:=p-1$ and $k:=q-1$. Since

$$
\omega_{m}^{m}=1, \omega_{2 m}^{2 k}=\omega_{m}^{k}, \omega_{2 m}^{m}=-1,\left(\boldsymbol{F}_{m}\right)_{p, q}=\omega_{m}^{j k},\left(\boldsymbol{D}_{m} \boldsymbol{F}_{m}\right)_{p, q}=\omega_{2 m}^{j} \omega_{m}^{j k},
$$

we find by considering elements in the four sub-blocks in turn

$$
\begin{array}{lll}
\left(\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m}\right)_{p, q} & =\omega_{2 m}^{j(2 k)} & =\omega_{m}^{j k}, \\
\left(\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m}\right)_{p+m, q} & =\omega_{2 m}^{(j+m)(2 k)} & =\omega_{m}^{j+m) k} \\
\left(\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m}\right)_{p, q+m} & =\omega_{2 m}^{j(2 k+1)} & =\omega_{2 m}^{j} \omega_{m}^{j k}, \\
\left(\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m}\right)_{p+m, q+m} & \left.=\omega_{2 m}^{j+m}\right)(2 k+1) & \left.=\omega_{2 m}^{j+m} \omega_{m}^{j+m}\right) k \\
& \\
(j+m & &
\end{array}
$$

It follows that the four $m$-by- $m$ blocks of $\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m}$ have the required structure. $\square$

Using Theorem 11.1 we can carry out the DFT as a block multiplication. Let $\boldsymbol{y} \in \mathbb{R}^{2 m}$ and set $\boldsymbol{w}=\boldsymbol{P}_{2 m}^{T} \boldsymbol{y}=\left[\boldsymbol{w}_{1}^{T}, \boldsymbol{w}_{2}^{T}\right]^{T}$, where

$$
\boldsymbol{w}_{1}^{T}=\left[y_{1}, y_{3}, \ldots, y_{2 m-1}\right], \quad \boldsymbol{w}_{2}^{T}=\left[y_{2}, y_{4}, \ldots, y_{2 m}\right] .
$$

Then

$$
\begin{aligned}
\boldsymbol{F}_{2 m} \boldsymbol{y} & =\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m} \boldsymbol{P}_{2 m}^{T} \boldsymbol{y}=\boldsymbol{F}_{2 m} \boldsymbol{P}_{2 m} \boldsymbol{w} \\
& =\left[\begin{array}{r|r}
\boldsymbol{F}_{m} & \boldsymbol{D}_{m} \boldsymbol{F}_{m} \\
\hline \boldsymbol{F}_{m} & -\boldsymbol{D}_{m} \boldsymbol{F}_{m}
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{w}_{1} \\
\boldsymbol{w}_{2}
\end{array}\right]=\left[\begin{array}{l}
\boldsymbol{q}_{1}+\boldsymbol{q}_{2} \\
\boldsymbol{q}_{1}-\boldsymbol{q}_{2}
\end{array}\right],
\end{aligned}
$$

where

$$
\boldsymbol{q}_{1}=\boldsymbol{F}_{m} \boldsymbol{w}_{1}, \quad \text { and } \quad \boldsymbol{q}_{2}=\boldsymbol{D}_{m}\left(\boldsymbol{F}_{m} \boldsymbol{w}_{2}\right) .
$$

In order to compute $\boldsymbol{F}_{2 m} \boldsymbol{y}$ we need to compute $\boldsymbol{F}_{m} \boldsymbol{w}_{1}$ and $\boldsymbol{F}_{m} \boldsymbol{w}_{2}$. Thus, by combining two FFT's of order $m$ we obtain an FFT of order $2 m$. If $n=2^{k}$ then this process can be applied recursively as in the following MATLAB function:

```
function z=fftrec(y)
%function z=fftrec(y)
y=y(:);
n=length(y);
if n==1
    z=y;
else
    q1=fftrec(y(1:2:n-1));
    q2=exp(-2*pi*1i/n).^(0:n/2-1)'.*fftrec(y(2:2:n));
    z=[q1+q2; q1-q2];
end
```

Listing 11.2 fftrec

Statement 3 is included so that the input $\boldsymbol{y} \in \mathbb{R}^{n}$ can be either a row or column vector, while the output $z$ is a column vector.

Such a recursive version of FFT is useful for testing purposes, but is much too slow for large problems. A challenge for FFT code writers is to develop nonrecursive versions and also to handle efficiently the case where $N$ is not a power of two. We refer to [14] for further details.

The complexity of the FFT is given by $\gamma N \log _{2} N$ for some constant $\gamma$ independent of $N$. To show this for the special case when $N$ is a power of two let $x_{k}$ be the complexity (the number of arithmetic operations) when $N=2^{k}$. Since we need two FFT's of order $N / 2=2^{k-1}$ and a multiplication with the diagonal matrix $\boldsymbol{D}_{N / 2}$, it is reasonable to assume that $x_{k}=2 x_{k-1}+\gamma 2^{k}$ for some constant $\gamma$ independent of $k$. Since $x_{0}=0$ we obtain by induction on $k$ that $x_{k}=\gamma k 2^{k}$. Indeed, this holds for $k=0$ and if $x_{k-1}=\gamma(k-1) 2^{k-1}$ then $x_{k}=2 x_{k-1}+\gamma 2^{k}=2 \gamma(k-1) 2^{k-1}+\gamma 2^{k}=\gamma k 2^{k}$. Reasonable implementations of FFT typically have $\gamma \approx 5$, see [14].

The efficiency improvement using the FFT to compute the DFT is spectacular for large $N$. The direct multiplication $\boldsymbol{F}_{N} \boldsymbol{y}$ requires $O\left(8 n^{2}\right)$ arithmetic operations since
complex arithmetic is involved. Assuming that the FFT uses $5 N \log _{2} N$ arithmetic operations we find for $N=2^{20} \approx 10^{6}$ the ratio

$$
\frac{8 N^{2}}{5 N \log _{2} N} \approx 84000 .
$$

Thus if the FFT takes one second of computing time and the computing time is proportional to the number of arithmetic operations then the direct multiplication would take something like 84000 seconds or 23 hours.

### 11.3.4 A Poisson Solver Based on the FFT

We now have all the ingredients to compute the matrix products $\boldsymbol{S} \boldsymbol{A}$ and $\boldsymbol{A} \boldsymbol{S}$ using FFT's of order $2 m+2$ where $m$ is the order of $\boldsymbol{S}$ and $\boldsymbol{A}$. This can then be used for quick computation of the exact solution $\boldsymbol{V}$ of the discrete Poisson problem in Algorithm 11.1. We first compute $\boldsymbol{H}=\boldsymbol{S} \boldsymbol{F}$ using Lemma 11.1 and $m$ FFT's, one for each of the $m$ columns of $\boldsymbol{F}$. We then compute $\boldsymbol{G}=\boldsymbol{H} \boldsymbol{S}$ by $m$ FFT's, one for each of the rows of $\boldsymbol{H}$. After $\boldsymbol{X}$ is determined we compute $\boldsymbol{Z}=\boldsymbol{S} \boldsymbol{X}$ and $\boldsymbol{V}=\boldsymbol{Z} \boldsymbol{S}$ by another $2 m$ FFT's. In total the work amounts to $4 m$ FFT's of order $2 m+2$. Since one FFT requires $O\left(\gamma(2 m+2) \log _{2}(2 m+2)\right)$ arithmetic operations the $4 m$ FFT's amount to

$$
8 \gamma m(m+1) \log _{2}(2 m+2) \approx 8 \gamma m^{2} \log _{2} m=4 \gamma n \log _{2} n,
$$

where $n=m^{2}$ is the size of the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ we would be solving if Cholesky factorization was used. This should be compared to the $O\left(8 n^{3 / 2}\right)$ arithmetic operations used in Algorithm 11.1 requiring 4 straightforward matrix multiplications with $\boldsymbol{S}$. What is faster will depend heavily on the programming of the FFT and the size of the problem. We refer to [14] for other efficient ways to implement the DST.

### 11.4 Exercises Chap. 11

### 11.4.1 Exercises Sect. 11.3

Exercise 11.1 (Fourier Matrix) Show that the Fourier matrix $\boldsymbol{F}_{4}$ is symmetric, but not Hermitian.

Exercise 11.2 (Sine Transform as Fourier Transform) Verify Lemma 11.1 directly when $m=1$.

Exercise 11.3 (Explicit Solution of the Discrete Poisson Equation) Show that the exact solution of the discrete Poisson equation (10.5) can be written $\boldsymbol{V}=$ $\left(v_{i, j}\right)_{i, j=1}^{m}$, where

$$
v_{i j}=\frac{1}{(m+1)^{4}} \sum_{p=1}^{m} \sum_{r=1}^{m} \sum_{k=1}^{m} \sum_{l=1}^{m} \frac{\sin \left(\frac{i p \pi}{m+1}\right) \sin \left(\frac{j r \pi}{m+1}\right) \sin \left(\frac{k p \pi}{m+1}\right) \sin \left(\frac{l r \pi}{m+1}\right)}{\left[\sin \left(\frac{p \pi}{2(m+1)}\right)\right]^{2}+\left[\sin \left(\frac{r \pi}{2(m+1)}\right)\right]^{2}} f_{k, l} .
$$

Exercise 11.4 (Improved Version of Algorithm 11.1) Algorithm 11.1 involves multiplying a matrix by $\boldsymbol{S}$ four times. In this problem we show that it is enough to multiply by $\boldsymbol{S}$ two times. We achieve this by diagonalizing only the second $\boldsymbol{T}$ in $\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V T}=h^{2} \boldsymbol{F}$. Let $\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{m}\right)$, where $\lambda_{j}=4 \sin ^{2}(j \pi h / 2)$, $j=1, \ldots, m$.

a) Show that
$$
\boldsymbol{T} \boldsymbol{X}+\boldsymbol{X} \boldsymbol{D}=\boldsymbol{C}, \text { where } \boldsymbol{X}=\boldsymbol{V} \boldsymbol{S}, \text { and } \boldsymbol{C}=h^{2} \boldsymbol{F} \boldsymbol{S} .
$$
b) Show that
$$
\left(\boldsymbol{T}+\lambda_{j} \boldsymbol{I}\right) \boldsymbol{x}_{j}=\boldsymbol{c}_{j} \quad j=1, \ldots, m,
$$
where $\boldsymbol{X}=\left[\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{m}\right]$ and $\boldsymbol{C}=\left[\boldsymbol{c}_{1}, \ldots, \boldsymbol{c}_{m}\right]$. Thus we can find $\boldsymbol{X}$ by solving $m$ linear systems, one for each of the columns of $\boldsymbol{X}$. Recall that a tridiagonal $m \times m$ system can be solved by Algorithms 2.1 and 2.2 in $8 m-7$ arithmetic operations. Give an algorithm to find $\boldsymbol{X}$ which only requires $O\left(\delta m^{2}\right)$ arithmetic operations for some constant $\delta$ independent of $m$.
c) Describe a method to compute $\boldsymbol{V}$ which only requires $O\left(4 m^{3}\right)=O\left(4 n^{3 / 2}\right)$ arithmetic operations.
d) Describe a method based on the fast Fourier transform which requires $O\left(2 \gamma n \log _{2} n\right)$ where $\gamma$ is the same constant as mentioned at the end of the last section.

Exercise 11.5 (Fast Solution of 9 Point Scheme) Consider the equation

$$
\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}-\frac{1}{6} \boldsymbol{T} \boldsymbol{V} \boldsymbol{T}=h^{2} \mu \boldsymbol{F},
$$

that was derived in Exercise 10.8 for the 9-point scheme. Define the matrix $\boldsymbol{X}$ by $\boldsymbol{V}=\boldsymbol{S} \boldsymbol{X} \boldsymbol{S}=\left(x_{j, k}\right)$ where $\boldsymbol{V}$ is the solution of (10.22). Show that

$$
\boldsymbol{D} \boldsymbol{X}+\boldsymbol{X} \boldsymbol{D}-\frac{1}{6} \boldsymbol{D} \boldsymbol{X} \boldsymbol{D}=4 h^{4} \boldsymbol{G}, \text { where } \boldsymbol{G}=\boldsymbol{S} \mu \boldsymbol{F} \boldsymbol{S},
$$

where $\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{m}\right)$, with $\lambda_{j}=4 \sin ^{2}(j \pi h / 2), j=1, \ldots, m$, and that

$$
x_{j, k}=\frac{h^{4} g_{j, k}}{\sigma_{j}+\sigma_{k}-\frac{2}{3} \sigma_{j} \sigma_{k}}, \text { where } \sigma_{j}=\sin ^{2}((j \pi h) / 2) \text { for } j, k=1,2, \ldots, m .
$$

Show that $\sigma_{j}+\sigma_{k}-\frac{2}{3} \sigma_{j} \sigma_{k}>0$ for $j, k=1,2, \ldots, m$. Conclude that the matrix $\boldsymbol{A}$ in Exercise 10.8 b) is symmetric positive definite and that (10.21) always has a solution $\boldsymbol{V}$.

Exercise 11.6 (Algorithm for Fast Solution of 9 Point Scheme) Derive an algorithm for solving (10.21) which for large $m$ requires essentially the same number of operations as in Algorithm 11.1. (We assume that $\mu \boldsymbol{F}$ already has been formed).

Exercise 11.7 (Fast Solution of Biharmonic Equation) For the biharmonic problem we derived in Exercise 10.9 the equation

$$
\boldsymbol{T}^{2} \boldsymbol{U}+2 \boldsymbol{T} \boldsymbol{U} \boldsymbol{T}+\boldsymbol{U} \boldsymbol{T}^{2}=h^{4} \boldsymbol{F} .
$$

Define the matrix $\boldsymbol{X}=\left(x_{j, k}\right)$ by $\boldsymbol{U}=\boldsymbol{S} \boldsymbol{X} \boldsymbol{S}$ where $\boldsymbol{U}$ is the solution of (10.25). Show that

$$
\boldsymbol{D}^{2} \boldsymbol{X}+2 \boldsymbol{D} \boldsymbol{X} \boldsymbol{D}+\boldsymbol{X} \boldsymbol{D}^{2}=4 h^{6} \boldsymbol{G}, \text { where } \boldsymbol{G}=\boldsymbol{S} \boldsymbol{F} \boldsymbol{S},
$$

and that

$$
x_{j, k}=\frac{h^{6} g_{j, k}}{4\left(\sigma_{j}+\sigma_{k}\right)^{2}}, \text { where } \sigma_{j}=\sin ^{2}((j \pi h) / 2) \text { for } j, k=1,2, \ldots, m .
$$

Exercise 11.8 (Algorithm for Fast Solution of Biharmonic Equation) Use Exercise 11.7 to derive an algorithm

```
function U=simplefastbiharmonic(F)
```

which requires only $O\left(\delta n^{3 / 2}\right)$ operations to find $\boldsymbol{U}$ in Problem 10.9. Here $\delta$ is some constant independent of $n$.

Exercise 11.9 (Check Algorithm for Fast Solution of Biharmonic Equation) In Exercise 11.8 compute the solution $\boldsymbol{U}$ corresponding to $\boldsymbol{F}=$ ones (m, m). For some small $m$ 's check that you get the same solution obtained by solving the standard form $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ in (10.25). You can use $\boldsymbol{x}=\boldsymbol{A} \backslash \boldsymbol{b}$ for solving $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Use F ( : ) to vectorize a matrix and reshape (x, m, m) to turn a vector $\boldsymbol{x} \in \mathbb{R}^{m^{2}}$ into an $m \times m$ matrix. Use the MATLAB command surf (U) for plotting $U$ for, say, $m=50$. Compare the result with Exercise 11.8 by plotting the difference between both matrices.

Exercise 11.10 (Fast Solution of Biharmonic Equation Using 9 Point Rule) Repeat Exercises 10.9, 11.8 and 11.9 using the nine point rule (10.21) to solve the system (10.24).

### 11.5 Review Questions

11.5.1 Consider the Poisson matrix.
    - What is the bandwidth of its Cholesky factor?
    - approximately how many arithmetic operations does it take to find the Cholesky factor?
    - same question for block LU,
    - same question for the fast Poisson solver with and without FFT.
11.5.2 What is the discrete sine transform and discrete Fourier transform of a vector?

## Part V <br> Iterative Methods for Large Linear Systems

Gaussian elimination, LU and Cholesky factorization are direct methods. In absence of rounding errors they are used to find the exact solution of a linear system using a finite number of arithmetic operations. In an iterative method we start with an approximation $\boldsymbol{x}_{0}$ to the exact solution $\boldsymbol{x}$ and then compute a sequence $\left\{\boldsymbol{x}_{k}\right\}$ such that hopefully $\boldsymbol{x}_{k} \rightarrow \boldsymbol{x}$. Iterative methods are mainly used for large sparse systems, i.e., where many of the elements in the coefficient matrix are zero. The main advantages of iterative methods are reduced storage requirements and ease of implementation. In an iterative method the main work in each iteration is a matrix times vector multiplication, an operation which often does not need storing the matrix, not even in sparse form.

In this part we consider the iterative methods of Jacobi, Gauss-Seidel, successive over relaxation (SOR), steepest descent and conjugate gradients.

## Chapter 12 <br> The Classical Iterative Methods

In this chapter we consider the classical iterative methods of Richardson, Jacobi, Gauss-Seidel and an accelerated version of Gauss-Seidel's method called successive overrelaxation (SOR). David Young developed in his thesis a beautiful theory describing the convergence rate of SOR, see [22].

We give the main points of this theory specialized to the discrete Poisson matrix. With a careful choice of an acceleration parameter the amount of work using SOR on the discrete Poisson problem is the same as for the fast Poisson solver without FFT (cf. Algorithm 11.1). Moreover, SOR is not restricted to constant coefficient methods on a rectangle. However, to obtain fast convergence using SOR it is necessary to have a good estimate for an acceleration parameter.

For convergence we need to study convergence of powers of matrices. In this chapter we only use matrix norms which are consistent on $\mathbb{C}^{n \times n}$ and subordinate to a vector norm on $\mathbb{C}^{n}$, (cf. Definitions 8.4 and 8.5).

### 12.1 Classical Iterative Methods; Component Form

We start with an example showing how a linear system can be solved using an iterative method.

Example 12.1 (Iterative Methods on a Special 2 × 2 Matrix) Solving for the diagonal elements, the linear system $\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]\left[\begin{array}{l}y \\ z\end{array}\right]=\left[\begin{array}{l}1 \\ 1\end{array}\right]$ can be written in component form as $y=(z+1) / 2$ and $z=(y+1) / 2$. Starting with $y_{0}, z_{0}$ we generate two sequences $\left\{y_{k}\right\}$ and $\left\{z_{k}\right\}$ using the difference equations $y_{k+1}=\left(z_{k}+1\right) / 2$ and $z_{k+1}=\left(y_{k}+1\right) / 2$. This is an example of Jacobi's method. If $y_{0}=z_{0}=0$ then we find $y_{1}=z_{1}=1 / 2$ and in general $y_{k}=z_{k}=1-2^{-k}$ for $k=0,1,2,3, \ldots$. The iteration converges to the exact solution $[1,1]^{T}$, and the error is halved in each iteration.

We can improve the convergence rate by using the most current approximation in each iteration. This leads to Gauss-Seidel's method: $y_{k+1}=\left(z_{k}+1\right) / 2$ and $z_{k+1}=\left(y_{k+1}+1\right) / 2$. If $y_{0}=z_{0}=0$ then we find $y_{1}=1 / 2, z_{1}=3 / 4, y_{2}=7 / 8$, $z_{2}=15 / 16$, and in general $y_{k}=1-2 \cdot 4^{-k}$ and $z_{k}=1-4^{-k}$ for $k=1,2,3, \ldots$. The error is now reduced by a factor 4 in each iteration.

Consider the general case. Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular and $\boldsymbol{b} \in \mathbb{C}^{n}$. Suppose we know an approximation $\boldsymbol{x}_{k}=\left[\boldsymbol{x}_{k}(1), \ldots, \boldsymbol{x}_{k}(n)\right]^{T}$ to the exact solution $\boldsymbol{x}$ of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. We need to assume that the rows are ordered so that $\boldsymbol{A}$ has nonzero diagonal elements. Solving the $i$ th equation of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ for $\boldsymbol{x}(i)$, we obtain a fixedpoint form of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$

$$
\boldsymbol{x}(i)=\left(-\sum_{j=1}^{i-1} a_{i j} \boldsymbol{x}(j)-\sum_{j=i+1}^{n} a_{i j} \boldsymbol{x}(j)+b_{i}\right) / a_{i i}, \quad i=1,2, \ldots, n .
$$

1. In Jacobi's method (J method) we substitute $\boldsymbol{x}_{k}$ into the right hand side of (12.1) and compute a new approximation by
$$
\boldsymbol{x}_{k+1}(i)=\left(-\sum_{j=1}^{i-1} a_{i j} \boldsymbol{x}_{k}(j)-\sum_{j=i+1}^{n} a_{i j} \boldsymbol{x}_{k}(j)+b_{i}\right) / a_{i i}, \text { for } i=1,2, \ldots, n .
$$
2. Gauss-Seidel's method (GS method) is a modification of Jacobi's method, where we use the new $\boldsymbol{x}_{k+1}(i)$ immediately after it has been computed.
$$
\boldsymbol{x}_{k+1}(i)=\left(-\sum_{j=1}^{i-1} a_{i j} \boldsymbol{x}_{k+1}(j)-\sum_{j=i+1}^{n} a_{i j} \boldsymbol{x}_{k}(j)+b_{i}\right) / a_{i i}, \text { for } i=1,2, \ldots, n .
$$
3. The Successive overrelaxation method (SOR method) is obtained by introducing an acceleration parameter $0<\omega<2$ in the GS method. We write $\boldsymbol{x}(i)=\omega \boldsymbol{x}(i)+(1-\omega) \boldsymbol{x}(i)$ and this leads to the method
$$
\boldsymbol{x}_{k+1}(i)=\omega\left(-\sum_{j=1}^{i-1} a_{i j} \boldsymbol{x}_{k+1}(j)-\sum_{j=i+1}^{n} a_{i j} \boldsymbol{x}_{k}(j)+b_{i}\right) / a_{i i}+(1-\omega) \boldsymbol{x}_{k}(i) .
$$
The SOR method reduces to the Gauss-Seidel method for $\omega=1$. Denoting the right hand side of (12.3) by $\boldsymbol{x}_{k+1}^{g s}$ we can write (12.4) as $\boldsymbol{x}_{k+1}=\omega \boldsymbol{x}_{k+1}^{g s}+(1-$ $\omega) \boldsymbol{x}_{k}$, and we see that $\boldsymbol{x}_{k+1}$ is located on the straight line passing through the two points $\boldsymbol{x}_{k+1}^{g s}$ and $\boldsymbol{x}_{k}$. The restriction $0<\omega<2$ is necessary for convergence

(cf. Theorem 12.6). Normally, the best results are obtained for the relaxation parameter $\omega$ in the range $1 \leq \omega<2$ and then $\boldsymbol{x}_{k+1}$ is computed by linear extrapolation, i.e., it is not located between $\boldsymbol{x}_{k+1}^{g s}$ and $\boldsymbol{x}_{k}$.
4. We mention also briefly the symmetric successive overrelaxation method SSOR. One iteration in SSOR consists of two SOR sweeps. A forward SOR sweep (12.4), computing an approximation denoted $\boldsymbol{x}_{k+1 / 2}$ instead of $\boldsymbol{x}_{k+1}$, is followed by a backward SOR sweep computing
$$
\boldsymbol{x}_{k+1}(i)=\omega\left(-\sum_{j=1}^{i-1} a_{i j} \boldsymbol{x}_{k+1 / 2}(j)-\sum_{j=i+1}^{n} a_{i j} \boldsymbol{x}_{k+1}(j)+b_{i}\right) / a_{i i}+(1-\omega) \boldsymbol{x}_{k+1 / 2}(i)
$$
in the order $i=n, n-1, \ldots 1$. The method is slower and more complicated than the SOR method. Its main use is as a symmetric preconditioner. For if $\boldsymbol{A}$ is symmetric then SSOR combines the two SOR steps in such a way that the resulting iteration matrix is similar to a symmetric matrix. We will not discuss this method any further here and refer to Sect. 13.6 for an alternative example of a preconditioner.

We will refer to the J, GS and SOR methods as the classical (iterative) methods.

### 12.1.1 The Discrete Poisson System

Consider the classical methods applied to the discrete Poisson matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ given by (10.8). Let $n=m^{2}$ and set $h=1 /(m+1)$. In component form the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ can be written (cf. (10.4))

$$
4 \boldsymbol{v}(i, j)-\boldsymbol{v}(i-1, j)-\boldsymbol{v}(i+1, j)-\boldsymbol{v}(i, j-1)-\boldsymbol{v}(i, j+1)=h^{2} f_{i, j}, \quad i, j=1, \ldots, m,
$$

with homogenous boundary conditions also given in (10.4). Solving for $\boldsymbol{v}(i, j)$ we obtain the fixed point form

$$
\boldsymbol{v}(i, j)=\left(\boldsymbol{v}(i-1, j)+\boldsymbol{v}(i+1, j)+\boldsymbol{v}(i, j-1)+v(i, j+1)+e_{i, j}\right) / 4,
$$

where $e_{i, j}:=f_{i, j} /(m+1)^{2}$. The J, GS , and SOR methods take the form

$$
\begin{array}{r}
J: \boldsymbol{v}_{k+1}(i, j)=\left(\boldsymbol{v}_{k}(i-1, j)+\boldsymbol{v}_{k}(i, j-1)+\boldsymbol{v}_{k}(i+1, j)+\boldsymbol{v}_{k}(i, j+1)\right. \\
+\boldsymbol{e}(i, j)) / 4 \\
G S: \boldsymbol{v}_{k+1}(i, j)=\left(\boldsymbol{v}_{k+1}(i-1, j)+\boldsymbol{v}_{k+1}(i, j-1)+\boldsymbol{v}_{k}(i+1, j)+\boldsymbol{v}_{k}(i, j+1)\right. \\
+\boldsymbol{e}(i, j)) / 4
\end{array}
$$

Table 12.1 The number of iterations $k_{n}$ to solve the discrete Poisson problem with $n$ unknowns using the methods of Jacobi, Gauss-Seidel, and SOR (see text) with a tolerance $10^{-8}$
|  | $k_{100}$ | $k_{2500}$ | $k_{10} 000$ | $k_{40000}$ | $k_{160} 000$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| J | 385 | 8386 |  |  |  |
| GS | 194 | 4194 |  |  |  |
| SOR | 35 | 164 | 324 | 645 | 1286 |


$$
\begin{array}{r}
S O R: \boldsymbol{v}_{k+1}(i, j)=\omega\left(\boldsymbol{v}_{k+1}(i-1, j)+\boldsymbol{v}_{k+1}(i, j-1)+\boldsymbol{v}_{k}(i+1, j)\right. \\
\left.+\boldsymbol{v}_{k}(i, j+1)+\boldsymbol{e}(i, j)\right) / 4+(1-\omega) \boldsymbol{v}_{k}(i, j) .
\end{array}
$$

We note that for GS and SOR we have used the natural ordering, i.e., $\left(i_{1}, j_{1}\right)<$ ( $i_{2}, j_{2}$ ) if and only if $j_{1} \leq j_{2}$ and $i_{1}<i_{2}$ if $j_{1}=j_{2}$. For the J method any ordering can be used.

In Algorithm 12.1 we give a MATLAB program to test the convergence of Jacobi's method on the discrete Poisson problem. We carry out Jacobi iterations on the linear system (12.6) with $\boldsymbol{F}=\left(f_{i, j}\right) \in \mathbb{R}^{m \times m}$, starting with $\boldsymbol{V}_{0}=\mathbf{0} \in$ $\mathbb{R}^{(m+2) \times(m+2)}$. The output is the number of iterations $k$, to obtain $\left\|\boldsymbol{V}^{(k)}-\boldsymbol{U}\right\|_{M}:=$ $\max _{i, j}\left|v_{i j}-u_{i j}\right|<$ tol. Here $\left[u_{i j}\right] \in \mathbb{R}^{(m+2) \times(m+2)}$ is the "exact" solution of (12.6) computed using the fast Poisson solver in Algorithm 11.1. We set $k=K+1$ if convergence is not obtained in $K$ iterations. In Table 12.1 we show the output $k=k_{n}$ from this algorithm using $\boldsymbol{F}=\operatorname{ones}(m, m)$ for $m=10,50, K=10^{4}$, and tol $=10^{-8}$. We also show the number of iterations for Gauss-Seidel and SOR with a value of $\omega$ known as the optimal acceleration parameter $\omega^{*}:=2 /\left(1+\sin \left(\frac{\pi}{m+1}\right)\right)$. We will derive this value later.

```
function k=jdp(F,K,tol)
% k=jdp(F,K,tol)
m=length(F); U=fastpoisson(F);
V=zeros (m+2,m+2) ; E=F/(m+1) ^2;
for k=1:K
    V(2:m+1,2:m+1)=(V(1:m,2:m+1)+V(3:m+2,2:m+1)...
        +V(2:m+1,1:m)+V(2:m+1,3:m+2)+E)/4;
    if max(max(abs(V-U)))<tol, return
    end
end
k=K+1;
end
```

Listing 12.1 jdp

For the GS and SOR methods we have used Algorithm 12.2. This is the analog of Algorithm 12.1 using SOR instead of J to solve the discrete Poisson problem. $w$ is an acceleration parameter with $0<w<2$. For $w=1$ we obtain Gauss-Seidel's method.

```
function k=sordp(F,K,w,tol)
% k=sordp(F,K,w,tol)
m=length(F); U=fastpoisson(F); V=zeros(m+2,m+2); E=F/(m+1)^2;
for k=1:k
    for j=2:m+1
        for i=2:m+1
            V(i,j)=w*(V(i-1,j)+V(i+1,j)+V(i,j-1)...
                +V(i,j+1)+E(i-1,j-1))/4+(1-w)*V(i,j);
        end
    end
    if max(max(abs(V-U)))<tol, return
    end
end
k=K+1;
end
```

Listing 12.2 sordp

We make several remarks about these programs and the results in Table 12.1.

1. The rate (speed) of convergence is quite different for the four methods. The J and GS methods converge, but rather slowly. The J method needs about twice as many iterations as the GS method. The improvement using the SOR method with optimal $\omega$ is spectacular.
2. We show in Sect. 12.3.4 that the number of iterations $k_{n}$ for a size $n$ problem is $k_{n}=O(n)$ for the J and GS method and $k_{n}=O(\sqrt{n})$ for SOR with optimal $\omega$. The choice of tol will only influence the constants multiplying $n$ or $\sqrt{n}$.
3. From (12.1.1) it follows that each iteration requires $O(n)$ arithmetic operations. Thus the number of arithmetic operations to achieve a given tolerance is $O\left(k_{n} \times n\right)$. Therefore the number of arithmetic operations for the J and GS method is $O\left(n^{2}\right)$, while it is only $O\left(n^{3 / 2}\right)$ for the SOR method with optimal $\omega$. Asymptotically, for J and GS this is the same as using banded Cholesky, while SOR competes with the fast method (without FFT).
4. We do not need to store the coefficient matrix so the storage requirements for these methods on the discrete Poisson problem is $O(n)$, asymptotically the same as for the fast methods.
5. Jacobi's method has the advantage that it can be easily parallelized.

### 12.2 Classical Iterative Methods; Matrix Form

To study convergence we need matrix formulations of the classical methods.

### 12.2.1 Fixed-Point Form

In general we can construct an iterative method by choosing a nonsingular matrix $\boldsymbol{M}$ and write $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ in the equivalent form

$$
\boldsymbol{M} \boldsymbol{x}=(\boldsymbol{M}-\boldsymbol{A}) \boldsymbol{x}+\boldsymbol{b} .
$$

The matrix $\boldsymbol{M}$ is known as a splitting matrix.
The corresponding iterative method is given by

$$
\boldsymbol{M} \boldsymbol{x}_{k+1}=(\boldsymbol{M}-\boldsymbol{A}) \boldsymbol{x}_{k}+\boldsymbol{b}
$$

or

$$
\boldsymbol{x}_{k+1}:=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}, \quad \boldsymbol{G}=\boldsymbol{I}-\boldsymbol{M}^{-1} \boldsymbol{A}, \quad, \boldsymbol{c}=\boldsymbol{M}^{-1} b .
$$

This is known as a fixed-point iteration. Starting with $\boldsymbol{x}_{0}$ this defines a sequence $\left\{\boldsymbol{x}_{k}\right\}$ of vectors in $\mathbb{C}^{n}$. For a general $\boldsymbol{G} \in \mathbb{C}^{n \times n}$ and $\boldsymbol{c} \in \mathbb{C}^{n}$ a solution of $\boldsymbol{x}=\boldsymbol{G} \boldsymbol{x}+\boldsymbol{c}$ is called a fixed-point. The fixed-point is unique if $\boldsymbol{I}-\boldsymbol{G}$ is nonsingular.

If $\lim _{k \rightarrow \infty} \boldsymbol{x}_{k}=\boldsymbol{x}$ for some $\boldsymbol{x} \in \mathbb{C}^{n}$ then $\boldsymbol{x}$ is a fixed point since

$$
\boldsymbol{x}=\lim _{k \rightarrow \infty} \boldsymbol{x}_{k+1}=\lim _{k \rightarrow \infty}\left(\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}\right)=\boldsymbol{G} \lim _{k \rightarrow \infty} \boldsymbol{x}_{k}+\boldsymbol{c}=\boldsymbol{G} \boldsymbol{x}+\boldsymbol{c} .
$$

The matrix $\boldsymbol{M}$ can also be interpreted as a preconditioning matrix. We first write $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ in the equivalent form $\boldsymbol{M}^{-1} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{M}^{-1} \boldsymbol{b}$ or $\boldsymbol{x}=\boldsymbol{x}-\boldsymbol{M}^{-1} \boldsymbol{A} \boldsymbol{x}+\boldsymbol{M}^{-1} \boldsymbol{b}$. This again leads to the iterative method (12.10), and $\boldsymbol{M}$ is chosen to reduce the condition number of $\boldsymbol{A}$.

### 12.2.2 The Splitting Matrices for the Classical Methods

Different choices of $\boldsymbol{M}$ in (12.9) lead to different iterative methods. We now derive $\boldsymbol{M}$ for the classical methods. For GS and SOR it is convenient to write $\boldsymbol{A}$ as a sum of three matrices, $\boldsymbol{A}=\boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}-\boldsymbol{A}_{\boldsymbol{R}}$, where $-\boldsymbol{A}_{\boldsymbol{L}}, \boldsymbol{D}$, and $-\boldsymbol{A}_{\boldsymbol{R}}$ are the lower, diagonal, and upper part of $\boldsymbol{A}$, respectively. Thus $\boldsymbol{D}:=\operatorname{diag}\left(a_{11}, \ldots, a_{n n}\right)$,

$$
\boldsymbol{A}_{\boldsymbol{L}}:=\left[\begin{array}{ccc}
0 & & \\
-a_{2,1} & 0 & \\
\vdots & \ddots & \ddots \\
-a_{n, 1} & \cdots & -a_{n, n-1}
\end{array}\right], \quad \boldsymbol{A}_{\boldsymbol{R}}:=\left[\begin{array}{ccc}
0 & -a_{1,2} & \cdots \\
\ddots & \ddots & \vdots \\
& 0 & -a_{n-1, n} \\
& & 0
\end{array}\right] .
$$

Theorem 12.1 (Splitting Matrices for J, GS and SOR) The splitting matrices $\boldsymbol{M}_{J}, \boldsymbol{M}_{1}$ and $\boldsymbol{M}_{\omega}$ for the $J, G S$ and SOR methods are given by

$$
\boldsymbol{M}_{J}=\boldsymbol{D}, \quad \boldsymbol{M}_{1}=\boldsymbol{D}-\boldsymbol{A}_{L}, \quad \boldsymbol{M}_{\omega}=\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{L} .
$$

Proof To find $\boldsymbol{M}$ we write the methods in the form (12.9) where the coefficient of $\boldsymbol{b}$ is equal to one. Moving $a_{i i}$ to the left hand side of the Jacobi iteration (12.2) we obtain the matrix form $\boldsymbol{D} \boldsymbol{x}_{k+1}=(\boldsymbol{D}-\boldsymbol{A}) \boldsymbol{x}_{k}+\boldsymbol{b}$ showing that $\boldsymbol{M}_{J}=\boldsymbol{D}$.

For the SOR method a matrix form is

$$
\boldsymbol{D} \boldsymbol{x}_{k+1}=\omega\left(\boldsymbol{A}_{L} \boldsymbol{x}_{k+1}+\boldsymbol{A}_{R} \boldsymbol{x}_{k}+\boldsymbol{b}\right)+(1-\omega) \boldsymbol{D} \boldsymbol{x}_{k} .
$$

Dividing both sides by $\omega$ and moving $\boldsymbol{A}_{L} \boldsymbol{x}_{k+1}$ to the left hand side this takes the form $\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{L}\right) \boldsymbol{x}_{k+1}=\boldsymbol{A}_{R} \boldsymbol{x}_{k}+\boldsymbol{b}+\left(\omega^{-1}-1\right) \boldsymbol{D} \boldsymbol{x}_{k}$ showing that $\boldsymbol{M}_{\omega}=$ $\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{L}$. We obtain $\boldsymbol{M}_{1}$ by letting $\omega=1$ in $\boldsymbol{M}_{\omega}$. $\square$

Example 12.2 (Splitting Matrices) For the system

$$
\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{l}
1 \\
1
\end{array}\right]
$$

we find

$$
\boldsymbol{A}_{L}=\left[\begin{array}{ll}
0 & 0 \\
1 & 0
\end{array}\right], \quad \boldsymbol{D}=\left[\begin{array}{ll}
2 & 0 \\
0 & 2
\end{array}\right], \quad \boldsymbol{A}_{R}=\left[\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right],
$$

and

$$
\boldsymbol{M}_{J}=\boldsymbol{D}=\left[\begin{array}{ll}
2 & 0 \\
0 & 2
\end{array}\right], \quad \boldsymbol{M}_{\omega}=\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{L}=\left[\begin{array}{cc}
2 \omega^{-1} & 0 \\
-1 & 2 \omega^{-1}
\end{array}\right] .
$$

The iteration matrix $\boldsymbol{G}_{\omega}=\boldsymbol{I}-\boldsymbol{M}_{\omega}^{-1} \boldsymbol{A}$ is given by

$$
\boldsymbol{G}_{\omega}=\left[\begin{array}{ll}
l & 0 \\
0 & 1
\end{array}\right]-\left[\begin{array}{cc}
\omega / 2 & 0 \\
\omega^{2} / 4 & \omega / 2
\end{array}\right]\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right]=\left[\begin{array}{cc}
1-\omega & \omega / 2 \\
\omega(1-\omega) / 2 & 1-\omega+\omega^{2} / 4
\end{array}\right] .
$$

For the J and GS method we have

$$
\boldsymbol{G}_{J}=\boldsymbol{I}-\boldsymbol{D}^{-1} \boldsymbol{A}=\left[\begin{array}{cc}
0 & 1 / 2 \\
1 / 2 & 0
\end{array}\right], \quad \boldsymbol{G}_{1}=\left[\begin{array}{ll}
0 & 1 / 2 \\
0 & 1 / 4
\end{array}\right] .
$$

We could have derived these matrices directly from the component form of the iteration. For example, for the GS method we have the component form

$$
x_{k+1}(1)=\frac{1}{2} x_{k}(2)+\frac{1}{2}, \quad x_{k+1}(2)=\frac{1}{2} x_{k+1}(1)+\frac{1}{2} .
$$

Substituting the value of $\boldsymbol{x}_{k+1}(1)$ from the first equation into the second equation we find

$$
x_{k+1}(2)=\frac{1}{2}\left(\frac{1}{2} x_{k}(2)+\frac{1}{2}\right)+\frac{1}{2}=\frac{1}{4} x_{k}(2)+\frac{3}{4} .
$$

Thus

$$
\boldsymbol{x}_{k+1}=\left[\begin{array}{l}
\boldsymbol{x}_{k+1}(1) \\
\boldsymbol{x}_{k+1}(2)
\end{array}\right]=\left[\begin{array}{ll}
0 & 1 / 2 \\
0 & 1 / 4
\end{array}\right]\left[\begin{array}{l}
\boldsymbol{x}_{k}(1) \\
\boldsymbol{x}_{k}(2)
\end{array}\right]+\left[\begin{array}{l}
1 / 2 \\
3 / 4
\end{array}\right]=\boldsymbol{G}_{1} \boldsymbol{x}_{k}+\boldsymbol{c} .
$$

### 12.3 Convergence

For Newton's method the choice of starting value is important. This is not the case for methods of the form $\boldsymbol{x}_{k+1}:=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$.

In the following we assume that $\boldsymbol{G} \in \mathbb{C}^{n \times n}, \boldsymbol{c} \in \mathbb{C}^{n}$ and $\boldsymbol{I}-\boldsymbol{G}$ is nonsingular. We let $\boldsymbol{x} \in \mathbb{C}^{n}$ be the unique fixed point satisfying $\boldsymbol{x}=\boldsymbol{G} \boldsymbol{x}+\boldsymbol{c}$.

Definition 12.1 (Convergence of $\boldsymbol{x}_{k+1}:=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$ ) We say that the iterative method $\boldsymbol{x}_{k+1}:=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$ converges if the sequence $\left\{\boldsymbol{x}_{k}\right\}$ converges for any starting vector $\boldsymbol{x}_{0}$.

We have the following necessary and sufficient condition for convergence:
Theorem 12.2 (Convergence of an Iterative Method) The iterative method $\boldsymbol{x}_{k+1}:=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$ converges if and only if $\lim _{k \rightarrow \infty} \boldsymbol{G}^{k}=\mathbf{0}$.

Proof Suppose $\lim _{k \rightarrow \infty} \boldsymbol{G}^{k}=\mathbf{0}$, and let $\boldsymbol{x}$ be the unique fixed point. We subtract $\boldsymbol{x}=\boldsymbol{G} \boldsymbol{x}+\boldsymbol{c}$ from $\boldsymbol{x}_{k+1}=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$. The vector $\boldsymbol{c}$ cancels and we obtain $\boldsymbol{x}_{k+1}-\boldsymbol{x}=$ $\boldsymbol{G}\left(\boldsymbol{x}_{k}-\boldsymbol{x}\right)$. By induction on $k$

$$
\boldsymbol{x}_{k}-\boldsymbol{x}=\boldsymbol{G}^{k}\left(\boldsymbol{x}_{0}-\boldsymbol{x}\right), \quad k=0,1,2, \ldots
$$

Clearly $\boldsymbol{x}_{k}-\boldsymbol{x} \rightarrow \mathbf{0}$ if $\boldsymbol{G}^{k} \rightarrow \mathbf{0}$ and the method converges. For the converse we let $\boldsymbol{x}$ be as before and choose $\boldsymbol{x}_{0}-\boldsymbol{x}=\boldsymbol{e}_{j}$, the $j$ th unit vector for $j=1, \ldots, n$. Since $\boldsymbol{x}_{k}-\boldsymbol{x} \rightarrow \mathbf{0}$ for any $\boldsymbol{x}_{0}$ we have $\boldsymbol{G}^{k} \boldsymbol{e}_{j} \rightarrow \mathbf{0}$ for $j=1, \ldots, n$ which implies that $\lim _{k \rightarrow \infty} \boldsymbol{G}^{k}=\mathbf{0}$. $\square$

Theorem 12.3 (Sufficient Condition for Convergence) If $\|\boldsymbol{G}\|<1$ then the iteration $\boldsymbol{x}_{k+1}=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$ converges.

Proof We have

$$
\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\|=\left\|\boldsymbol{G}^{k}\left(\boldsymbol{x}_{0}-\boldsymbol{x}\right)\right\| \leq\left\|\boldsymbol{G}^{k}\right\|\left\|\boldsymbol{x}_{0}-\boldsymbol{x}\right\| \leq\|\boldsymbol{G}\|^{k}\left\|\boldsymbol{x}_{0}-\boldsymbol{x}\right\| \rightarrow \mathbf{0}, \quad k \rightarrow \infty .
$$ $\square$

A necessary and sufficient condition for convergence involves the eigenvalues of $\boldsymbol{G}$. We define the spectral radius of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ as the maximum absolute value of its eigenvalues.

$$
\rho(\boldsymbol{A}):=\max _{\lambda \in \sigma(\boldsymbol{A})}|\lambda| .
$$

Theorem 12.4 (When Does an Iterative Method Converge?) Suppose $\boldsymbol{G} \in \mathbb{C}^{n \times n}$ with $\boldsymbol{I}-\boldsymbol{G}$ nonsingular and let $\boldsymbol{c} \in \mathbb{C}^{n}$. The iteration $\boldsymbol{x}_{k+1}=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$ converges if and only if $\rho(\boldsymbol{G})<1$.

We will prove this theorem using Theorem 12.10 in Sect. 12.4.

### 12.3.1 Richardson's Method

The Richardson's method (R method) is defined by

$$
\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\alpha\left(\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}\right) .
$$

Here we pick an acceleration parameter $\alpha$ and compute a new approximation by adding a multiple of the residual vector $\boldsymbol{r}_{k}:=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}$. Note that we do not need the assumption of nonzero diagonal elements. Richardson considered this method in 1910.

We will assume that $\alpha$ is real. If all eigenvalues of $\boldsymbol{A}$ have positive real parts then the R method converges provided $\alpha$ is positive and sufficiently small. We show this result for positive eigenvalues and leave the more general case to Exercise 12.2.

Theorem 12.5 (Convergence of Richardson's Method) If $\boldsymbol{A}$ has positive eigenvalues $\lambda_{1} \geq \lambda_{2} \geq \cdots \geq \lambda_{n}>0$ then the $R$ method given by $\boldsymbol{x}_{k+1}=(\boldsymbol{I}-\alpha \boldsymbol{A}) \boldsymbol{x}_{k}+\boldsymbol{b}$ converges if and only if $0<\alpha<2 / \lambda_{1}$. Moreover,

$$
\begin{gathered}
\rho(\boldsymbol{I}-\alpha \boldsymbol{A})>\rho\left(\boldsymbol{I}-\alpha_{o} \boldsymbol{A}\right)=\frac{\kappa-1}{\kappa+1}, \quad \alpha \in \mathbb{R} \backslash\left\{\alpha_{o}\right\}, \\
\kappa:=\frac{\lambda_{1}}{\lambda_{n}}, \quad \alpha_{o}:=\frac{2}{\lambda_{1}+\lambda_{n}} .
\end{gathered}
$$

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-274.jpg?height=459&width=956&top_left_y=209&top_left_x=286)
Fig. 12.1 The functions $\alpha \rightarrow\left|1-\alpha \lambda_{1}\right|$ and $\alpha \rightarrow\left|1-\alpha \lambda_{n}\right|$

Proof The eigenvalues of $\boldsymbol{I}-\alpha \boldsymbol{A}$ are $1-\alpha \lambda_{j}, \quad j=1, \ldots, n$. We have

$$
\rho_{\alpha}:=\rho(\boldsymbol{I}-\alpha \boldsymbol{A}):=\max _{j}\left|1-\alpha \lambda_{j}\right|= \begin{cases}1-\alpha \lambda_{1}, & \text { if } \alpha \leq 0 \\ 1-\alpha \lambda_{n}, & \text { if } 0<\alpha \leq \alpha_{o} \\ \alpha \lambda_{1}-1, & \text { if } \alpha>\alpha_{o},\end{cases}
$$

see Fig. 12.1. Clearly $1-\alpha \lambda_{n}=\alpha \lambda_{1}-1$ for $\alpha=\alpha_{o}$ and

$$
\rho_{\alpha_{o}}=\alpha_{o} \lambda_{1}-1=\frac{\lambda_{1}-\lambda_{n}}{\lambda_{1}+\lambda_{n}}=\frac{\kappa-1}{\kappa+1}<1 .
$$

We have $\rho_{\alpha}<1$ if and only if $\alpha>0$ and $\alpha \lambda_{1}-1<1$ showing convergence if and only if $0<\alpha<2 / \lambda_{1}$ and $\rho_{\alpha}>\rho_{\alpha_{o}}$ for $\alpha \leq 0$ and $\alpha \geq 2 / \lambda_{1}$. Finally, if $0<\alpha<\alpha_{o}$ then $\rho_{\alpha}=1-\alpha \lambda_{n}>1-\alpha_{o} \lambda_{n}=\rho_{\alpha_{o}}$ and if $\alpha_{o}<\alpha<2 / \lambda_{1}$ then $\rho_{\alpha}=\alpha \lambda_{1}-1>\alpha_{o} \lambda_{1}-1=\rho_{\alpha_{o}}$. $\square$

For a positive definite matrix we obtain
Corollary 12.1 (Rate of Convergence for the $\mathbf{R}$ Method) Suppose $\boldsymbol{A}$ is positive definite with largest and smallest eigenvalue $\lambda_{\text {max }}$ and $\lambda_{\text {min }}$, respectively. Richardson's method $\boldsymbol{x}_{k+1}=(\boldsymbol{I}-\alpha \boldsymbol{A}) \boldsymbol{x}_{k}+\boldsymbol{b}$ converges if and only if $0<\alpha<2 / \lambda_{\text {max }}$. With $\alpha=\alpha_{o}:=\frac{2}{\lambda_{\text {max }}+\lambda_{\text {min }}}$ we have the error estimate

$$
\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\|_{2} \leq\left(\frac{\kappa-1}{\kappa+1}\right)^{k}\left\|\boldsymbol{x}_{0}-\boldsymbol{x}\right\|_{2}, \quad k=0,1,2, \ldots
$$

where $\kappa:=\lambda_{\text {max }} / \lambda_{\text {min }}$ is the spectral condition number of $\boldsymbol{A}$.
Proof The spectral norm $\left\|\|_{2}\right.$ is consistent and therefore $\| \boldsymbol{x}_{k}-\boldsymbol{x}\left\|_{2} \leq\right\| \boldsymbol{I}-$ $\alpha_{o} \boldsymbol{A}\left\|_{2}^{k}\right\| \boldsymbol{x}_{0}-\boldsymbol{x} \|_{2}$. But for a positive definite matrix the spectral norm is equal to the spectral radius and the result follows form (12.19). $\square$

### 12.3.2 Convergence of SOR

The condition $\omega \in(0,2)$ is necessary for convergence of the SOR method.
Theorem 12.6 (Necessary Condition for Convergence of SOR) Suppose $\boldsymbol{A} \in$ $\mathbb{C}^{n \times n}$ is nonsingular with nonzero diagonal elements. If the SOR method applied to $\boldsymbol{A}$ converges then $\omega \in(0,2)$.

Proof We have (cf. (12.13)) $\boldsymbol{D} \boldsymbol{x}_{k+1}=\omega\left(\boldsymbol{A}_{L} \boldsymbol{x}_{k+1}+\boldsymbol{A}_{R} \boldsymbol{x}_{k}+\boldsymbol{b}\right)+(1-\omega) \boldsymbol{D} \boldsymbol{x}_{k}$ or $\boldsymbol{x}_{k+1}=\omega\left(\boldsymbol{L} \boldsymbol{x}_{k+1}+\boldsymbol{R} \boldsymbol{x}_{k}+\boldsymbol{D}^{-1} \boldsymbol{b}\right)+(1-\omega) \boldsymbol{x}_{k}$, where $\boldsymbol{L}:=\boldsymbol{D}^{-1} \boldsymbol{A}_{\boldsymbol{L}}$ and $\boldsymbol{R}:=\boldsymbol{D}^{-1} \boldsymbol{A}_{\boldsymbol{R}}$. Thus $(\boldsymbol{I}-\omega \boldsymbol{L}) \boldsymbol{x}_{k+1}=(\omega \boldsymbol{R}+(1-\omega) \boldsymbol{I}) \boldsymbol{x}_{k}+\omega \boldsymbol{D}^{-1} \boldsymbol{b}$ so the following form of the iteration matrix is obtained

$$
\boldsymbol{G}_{\omega}=(\boldsymbol{I}-\omega \boldsymbol{L})^{-1}(\omega \boldsymbol{R}+(1-\omega) \boldsymbol{I}) .
$$

We next compute the determinant of $\boldsymbol{G}_{\omega}$. Since $\boldsymbol{I}-\omega \boldsymbol{L}$ is lower triangular with ones on the diagonal, the same holds for the inverse by Lemma 2.5, and therefore the determinant of this matrix is equal to one. The matrix $\omega \boldsymbol{R}+(1-\omega) \boldsymbol{I}$ is upper triangular with $1-\omega$ on the diagonal and therefore its determinant equals $(1-\omega)^{n}$. It follows that $\operatorname{det}\left(\boldsymbol{G}_{\omega}\right)=(1-\omega)^{n}$. Since the determinant of a matrix equals the product of its eigenvalues we must have $|\lambda| \geq|1-\omega|$ for at least one eigenvalue $\lambda$ of $\boldsymbol{G}_{\omega}$ and we conclude that $\rho\left(\boldsymbol{G}_{\omega}\right) \geq|\omega-1|$. But then $\rho\left(\boldsymbol{G}_{\omega}\right) \geq 1$ if $\omega$ is not in the interval $(0,2)$ and by Theorem 12.4 SOR diverges. $\square$

The SOR method always converges for a positive definite matrix.
Theorem 12.7 (SOR on Positive Definite Matrix) SOR converges for a positive definite matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ if and only if $0<\omega<2$. In particular, Gauss-Seidel's method converges for a positive definite matrix.

Proof By Theorem 12.6 convergence implies $0<\omega<2$. Suppose now $0<\omega<2$ and let ( $\lambda, \boldsymbol{x}$ ) be an eigenpair for $\boldsymbol{G}_{\omega}$. Note that $\lambda$ and $\boldsymbol{x}$ can be complex. We need to show that $|\lambda|<1$. The following identity will be shown below:

$$
\omega^{-1}(2-\omega)|1-\lambda|^{2} \boldsymbol{x}^{*} \boldsymbol{D} \boldsymbol{x}=\left(1-|\lambda|^{2}\right) \boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x},
$$

where $\boldsymbol{D}:=\operatorname{diag}\left(a_{11}, \ldots, a_{n n}\right)$. Now $\boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}$ and $\boldsymbol{x}^{*} \boldsymbol{D} \boldsymbol{x}$ are positive for all nonzero $x \in \mathbb{C}^{n}$ since a positive definite matrix has positive diagonal elements $a_{i i}=$ $\boldsymbol{e}_{i}^{T} \boldsymbol{A} \boldsymbol{e}_{i}>0$. It follows that the left hand side of (12.22) is nonnegative and then the right hand side must be nonnegative as well. This implies $|\lambda| \leq 1$. If $|\lambda|=1$ then (12.22) implies that $\lambda=1$ and it remains to show that this is not possible. By (12.10) and (12.12) we have

$$
\boldsymbol{G}_{\omega} \boldsymbol{x}=\left(\boldsymbol{I}-\boldsymbol{M}_{\omega}^{-1} \boldsymbol{A}\right) \boldsymbol{x}=\boldsymbol{x}-\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}\right)^{-1} \boldsymbol{A} \boldsymbol{x}
$$

and the eigenpair equation $\boldsymbol{G}_{\omega} \boldsymbol{x}=\lambda \boldsymbol{x}$ can be written $\boldsymbol{x}-\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}\right)^{-1} \boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ or

$$
\boldsymbol{A} \boldsymbol{x}=\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}\right) \boldsymbol{y}, \quad \boldsymbol{y}:=(1-\lambda) \boldsymbol{x} .
$$

Now $\boldsymbol{A} \boldsymbol{x} \neq \mathbf{0}$ implies that $\lambda \neq 1$.
To prove equation (12.22) we first show that

$$
\boldsymbol{E} \boldsymbol{y}=\lambda \boldsymbol{A} \boldsymbol{x}, \quad \boldsymbol{E}:=\omega^{-1} \boldsymbol{D}+\boldsymbol{A}_{\boldsymbol{R}}-\boldsymbol{D}=\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}-\boldsymbol{A} .
$$

The second equality follows immediately from $\boldsymbol{A}=\boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}-\boldsymbol{A}_{\boldsymbol{R}}$. By (12.23) and (12.24) we have

$$
\boldsymbol{E} \boldsymbol{y}=\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}-\boldsymbol{A}\right) \boldsymbol{y}=\boldsymbol{A} \boldsymbol{x}-\boldsymbol{A} \boldsymbol{y}=\boldsymbol{A} \boldsymbol{x}-(1-\lambda) \boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{A} \boldsymbol{x} .
$$

Again using (12.23), (12.24) and adding $(\boldsymbol{A} \boldsymbol{x})^{*} \boldsymbol{y}=\boldsymbol{y}^{*}\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{L}}\right)^{*} \boldsymbol{y}=$ $\boldsymbol{y}^{*}\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{R}}\right) \boldsymbol{y}$ and $\boldsymbol{y}^{*}(\lambda \boldsymbol{A} \boldsymbol{x})=\boldsymbol{y}^{*} \boldsymbol{E} \boldsymbol{y}=\boldsymbol{y}^{*}\left(\omega^{-1} \boldsymbol{D}+\boldsymbol{A}_{\boldsymbol{R}}-\boldsymbol{D}\right) \boldsymbol{y}$ we find

$$
\begin{aligned}
(\boldsymbol{A} \boldsymbol{x})^{*} \boldsymbol{y}+\boldsymbol{y}^{*}(\lambda \boldsymbol{A} \boldsymbol{x}) & =\boldsymbol{y}^{*}\left(\omega^{-1} \boldsymbol{D}-\boldsymbol{A}_{\boldsymbol{R}}\right) \boldsymbol{y}+\boldsymbol{y}^{*}\left(\omega^{-1} \boldsymbol{D}+\boldsymbol{A}_{\boldsymbol{R}}-\boldsymbol{D}\right) \boldsymbol{y} \\
& =\boldsymbol{y}^{*}\left(2 \omega^{-1}-1\right) \boldsymbol{D} \boldsymbol{y}=\omega^{-1}(2-\omega)|1-\lambda|^{2} \boldsymbol{x}^{*} \boldsymbol{D} \boldsymbol{x} .
\end{aligned}
$$

Since $(\boldsymbol{A} \boldsymbol{x})^{*}=\boldsymbol{x}^{*} \boldsymbol{A}^{*}=\boldsymbol{x}^{*} \boldsymbol{A}, \boldsymbol{y}:=(1-\lambda) \boldsymbol{x}$ and $\boldsymbol{y}^{*}=(1-\bar{\lambda}) \boldsymbol{x}^{*}$ this also equals

$$
(\boldsymbol{A} \boldsymbol{x})^{*} \boldsymbol{y}+\boldsymbol{y}^{*}(\lambda \boldsymbol{A} \boldsymbol{x})=(1-\lambda) \boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}+\lambda(1-\bar{\lambda}) \boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x}=\left(1-|\lambda|^{2}\right) \boldsymbol{x}^{*} \boldsymbol{A} \boldsymbol{x},
$$

and (12.22) follows. $\square$

### 12.3.3 Convergence of the Classical Methods for the Discrete Poisson Matrix

We know the eigenvalues of the discrete Poisson matrix $\boldsymbol{A}$ given by (10.8) and we can use this to estimate the number of iterations necessary to achieve a given accuracy for the various methods.

Recall that by (10.15) the eigenvalues $\lambda_{j, k}$ of $\boldsymbol{A}$ are

$$
\lambda_{j, k}=4-2 \cos (j \pi h)-2 \cos (k \pi h), \quad j, k=1, \ldots, m, h=1 /(m+1) .
$$

Consider first the J method. The matrix $\boldsymbol{G}_{J}=\boldsymbol{I}-\boldsymbol{D}^{-1} \boldsymbol{A}=\boldsymbol{I}-\boldsymbol{A} / 4$ has eigenvalues

$$
\mu_{j, k}=1-\frac{1}{4} \lambda_{j, k}=\frac{1}{2} \cos (j \pi h)+\frac{1}{2} \cos (k \pi h), \quad j, k=1, \ldots, m .
$$

It follows that $\rho\left(\boldsymbol{G}_{J}\right)=\cos (\pi h)<1$. Since $\boldsymbol{G}_{J}$ is symmetric it is normal, and the spectral norm is equal to the spectral radius (cf. Theorem 8.4). We obtain

$$
\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\|_{2} \leq\left\|\boldsymbol{G}_{J}\right\|_{2}^{k}\left\|\boldsymbol{x}_{0}-\boldsymbol{x}\right\|_{2}=\cos ^{k}(\pi h)\left\|\boldsymbol{x}_{0}-\boldsymbol{x}\right\|_{2}, \quad k=0,1,2, \ldots
$$

The R method given by $\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\alpha \boldsymbol{r}_{k}$ with $\alpha=2 /\left(\lambda_{\text {max }}+\lambda_{\text {min }}\right)=1 / 4$ is the same as the J-method so (12.26) holds in this case as well. This also follows from Corollary 12.1 with $\kappa$ given by (10.20).

For the SOR method it is possible to explicitly determine $\rho\left(\boldsymbol{G}_{\omega}\right)$ for any $\omega \in$ (0, 2). The following result will be shown in Sect. 12.5.

Theorem 12.8 (The Spectral Radius of SOR Matrix) Consider the SOR iteration (12.1.1), with the natural ordering. The spectral radius of $\boldsymbol{G}_{\omega}$ is

$$
\rho\left(\boldsymbol{G}_{\omega}\right)= \begin{cases}\frac{1}{4}\left(\omega \beta+\sqrt{(\omega \beta)^{2}-4(\omega-1)}\right)^{2}, & \text { for } 0<\omega \leq \omega^{*}, \\ \omega-1, & \text { for } \omega^{*}<\omega<2,\end{cases}
$$

where $\beta:=\rho\left(\boldsymbol{G}_{J}\right)=\cos (\pi h)$ and

$$
\omega^{*}:=\frac{2}{1+\sqrt{1-\beta^{2}}}>1 .
$$

Moreover,

$$
\rho\left(\boldsymbol{G}_{\omega}\right)>\rho\left(\boldsymbol{G}_{\omega^{*}}\right) \text { for } \omega \in(0,2) \backslash\left\{\omega^{*}\right\} .
$$

A plot of $\rho\left(\boldsymbol{G}_{\omega}\right)$ as a function of $\omega \in(0,2)$ is shown in Fig. 12.2 for $n=100$ (lower curve) and $n=2500$ (upper curve). As $\omega$ increases the spectral radius of $\boldsymbol{G}_{\omega}$ decreases monotonically to the minimum $\omega^{*}$. Then it increases linearly to the value one for $\omega=2$. We call $\omega^{*}$ the optimal relaxation parameter.

For the discrete Poisson problem we have $\beta=\cos (\pi h)$ and it follows from (12.27), (12.28) that

$$
\omega^{*}=\frac{2}{1+\sin (\pi h)}, \quad \rho\left(\boldsymbol{G}_{\omega^{*}}\right)=\omega^{*}-1=\frac{1-\sin (\pi h)}{1+\sin (\pi h)}, \quad h=\frac{1}{m+1} .
$$

Letting $\omega=1$ in (12.27) we find $\rho\left(\boldsymbol{G}_{1}\right)=\beta^{2}=\rho\left(\boldsymbol{G}_{J}\right)^{2}=\cos ^{2}(\pi h)$ for the GS method. Thus, for the discrete Poisson problem the J method needs twice as many iterations as the GS method for a given accuracy.

The values of $\rho\left(\boldsymbol{G}_{J}\right), \rho\left(\boldsymbol{G}_{1}\right)$, and $\rho\left(\boldsymbol{G}_{\omega^{*}}\right)=\omega^{*}-1$ are shown in Table 12.2 for $n=100$ and $n=2500$. We also show the smallest integer $k_{n}$ such that $\rho(\boldsymbol{G})^{k_{n}} \leq$ $10^{-8}$. This is an estimate for the number of iteration needed to obtain an accuracy of $10^{-8}$. These values are comparable to the exact values given in Table 12.1.

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-278.jpg?height=609&width=969&top_left_y=215&top_left_x=278)
Fig. $12.2 \rho\left(\boldsymbol{G}_{\omega}\right)$ with $\omega \in[0,2]$ for $n=100$, (lower curve) and $n=2500$ (upper curve)

Table 12.2 Spectral radial for $\boldsymbol{G}_{J}, \boldsymbol{G}_{1}, \boldsymbol{G}_{\omega^{*}}$ and the smallest integer $k_{n}$ such that $\rho(\boldsymbol{G})^{k_{n}} \leq 10^{-8}$
|  | $\mathrm{n}=100$ | $\mathrm{n}=2500$ | $k_{100}$ | $k_{2500}$ |
| :--- | :--- | :--- | :--- | :--- |
| J | 0.959493 | 0.998103 | 446 | 9703 |
| GS | 0.920627 | 0.99621 | 223 | 4852 |
| SOR | 0.56039 | 0.88402 | 32 | 150 |


### 12.3.4 Number of Iterations

Consider next the rate of convergence of the iteration $\boldsymbol{x}_{k+1}=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$. We like to know how fast the iterative method converges. Recall that $\boldsymbol{x}_{k}-\boldsymbol{x}=\boldsymbol{G}^{k}\left(\boldsymbol{x}_{0}-\boldsymbol{x}\right)$. For $k$ sufficiently large

$$
\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\| \leq\left\|\boldsymbol{G}^{k}\right\|\left\|\boldsymbol{x}_{0}-\boldsymbol{x}\right\| \approx \rho(\boldsymbol{G})^{k}\left\|\boldsymbol{x}_{0}-\boldsymbol{x}\right\| .
$$

For the last formula we apply Theorem 12.13 which says that $\lim _{k \rightarrow \infty}\left\|\boldsymbol{G}^{k}\right\|^{1 / k}=$ $\rho(\boldsymbol{G})$. For Jacobi's method and the spectral norm we have $\left\|\boldsymbol{G}_{J}^{k}\right\|_{2}=\rho\left(\boldsymbol{G}_{J}\right)^{k}$ (cf. (12.26)).

For fast convergence we should use a $\boldsymbol{G}$ with small spectral radius.
Lemma 12.1 (Number of Iterations) Suppose $\rho(\boldsymbol{G})=1-\eta$ for some $0<\eta<1$ and let $s \in \mathbb{N}$. Then

$$
\tilde{k}:=\frac{s \log (10)}{\eta}
$$

is an estimate for the smallest number of iterations $k$ so that $\rho(\boldsymbol{G})^{k} \leq 10^{-s}$.

Proof The estimate $\tilde{k}$ is an approximate solution of the equation $\rho(\boldsymbol{G})^{k}=10^{-s}$. Thus, since $-\log (1-\eta) \approx \eta$ when $\eta$ is small

$$
k=-\frac{s \log (10)}{\log (1-\eta)} \approx \frac{s \log (10)}{\eta}=\tilde{k} .
$$ $\square$

The following estimates are obtained. They agree with those we found numerically in Sect. 12.1.1.

- R and J: $\rho\left(\boldsymbol{G}_{J}\right)=\cos (\pi h)=1-\eta, \eta=1-\cos (\pi h)=\frac{1}{2} \pi^{2} h^{2}+O\left(h^{4}\right)=$ $\frac{\pi^{2}}{2} / n+O\left(n^{-2}\right)$. Thus,
$$
\tilde{k}_{n}=\frac{2 \log (10) s}{\pi^{2}} n+O\left(n^{-1}\right)=O(n) .
$$
- $\operatorname{GS}: \rho\left(\boldsymbol{G}_{1}\right)=\cos ^{2}(\pi h)=1-\eta, \eta=1-\cos ^{2}(\pi h)=\sin ^{2} \pi h=\pi^{2} h^{2}+$ $O\left(h^{4}\right)=\pi^{2} / n+O\left(n^{-2}\right)$. Thus,
$$
\tilde{k}_{n}=\frac{\log (10) s}{\pi^{2}} n+O\left(n^{-1}\right)=O(n) .
$$
- SOR: $\rho\left(\boldsymbol{G}_{\omega^{*}}\right)=\frac{1-\sin (\pi h)}{1+\sin (\pi h)}=1-2 \pi h+O\left(h^{2}\right)$. Thus,
$$
\tilde{k}_{n}=\frac{\log (10) s}{2 \pi} \sqrt{n}+O\left(n^{-1 / 2}\right)=O(\sqrt{n}) .
$$
We note that
1. The convergence depends on the behavior of the powers $\boldsymbol{G}^{k}$ as $k$ increases. The matrix $\boldsymbol{M}$ should be chosen so that all elements in $\boldsymbol{G}^{k}$ converge quickly to zero and such that the linear system (12.9) is easy to solve for $\boldsymbol{x}_{k+1}$. These are conflicting demands. $\boldsymbol{M}$ should be an approximation to $\boldsymbol{A}$ to obtain a $\boldsymbol{G}$ with small elements, but then (12.9) might not be easy to solve for $\boldsymbol{x}_{k+1}$.
2. The convergence $\lim _{k \rightarrow \infty}\left\|\boldsymbol{G}^{k}\right\|^{1 / k}=\rho(\boldsymbol{G})$ can be quite slow (cf. Exercise 12.15).

### 12.3.5 Stopping the Iteration

In Algorithms 12.1 and 12.2 we had access to the exact solution and could stop the iteration when the error was sufficiently small in the infinity norm. The decision when to stop is obviously more complicated when the exact solution is not known. One possibility is to choose a vector norm, keep track of $\left\|\boldsymbol{x}_{k+1}-\boldsymbol{x}_{k}\right\|$, and stop
when this number is sufficiently small. The following result indicates that $\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\|$ can be quite large if $\|\boldsymbol{G}\|$ is close to one.

Lemma 12.2 (Be Careful When Stopping) If $\boldsymbol{x}_{k}=\boldsymbol{G} \boldsymbol{x}_{k-1}+\boldsymbol{c}, \boldsymbol{x}=\boldsymbol{G} \boldsymbol{x}+\boldsymbol{c}$ and $\|\boldsymbol{G}\|<1$ then

$$
\left\|\boldsymbol{x}_{k}-\boldsymbol{x}_{k-1}\right\| \geq \frac{1-\|\boldsymbol{G}\|}{\|\boldsymbol{G}\|}\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\|, \quad k \geq 1 .
$$

Proof We find

$$
\begin{aligned}
\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\| & =\left\|\boldsymbol{G}\left(\boldsymbol{x}_{k-1}-\boldsymbol{x}\right)\right\| \leq\|\boldsymbol{G}\|\left\|\boldsymbol{x}_{k-1}-\boldsymbol{x}\right\| \\
& =\|\boldsymbol{G}\|\left\|\boldsymbol{x}_{k-1}-\boldsymbol{x}_{k}+\boldsymbol{x}_{k}-\boldsymbol{x}\right\| \leq\|\boldsymbol{G}\|\left(\left\|\boldsymbol{x}_{k-1}-\boldsymbol{x}_{k}\right\|+\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\|\right)
\end{aligned}
$$

Thus $(1-\|\boldsymbol{G}\|)\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\| \leq\|\boldsymbol{G}\|\left\|\boldsymbol{x}_{k-1}-\boldsymbol{x}_{k}\right\|$ which implies (12.32). $\square$

Another possibility is to stop when the residual vector $\boldsymbol{r}_{k}:=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}$ is sufficiently small in some norm. To use the residual vector for stopping it is convenient to write the iterative method (12.10) in an alternative form. If $\boldsymbol{M}$ is the splitting matrix of the method then by (12.9) we have $\boldsymbol{M} \boldsymbol{x}_{k+1}=\boldsymbol{M} \boldsymbol{x}_{k}-\boldsymbol{A} \boldsymbol{x}_{k}+\boldsymbol{b}$. This leads to

$$
\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\boldsymbol{M}^{-1} \boldsymbol{r}_{k}, \quad \boldsymbol{r}_{k}=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k} .
$$

Testing on $\boldsymbol{r}_{k}$ works fine if $\boldsymbol{A}$ is well conditioned, but Theorem 8.8 shows that the relative error in the solution can be much larger than the relative error in $\boldsymbol{r}_{k}$ if $\boldsymbol{A}$ is ill-conditioned.

### 12.4 Powers of a Matrix

Let $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ be a square matrix. In this section we consider the special matrix sequence $\left\{\boldsymbol{A}^{k}\right\}$ of powers of $\boldsymbol{A}$. We want to know when this sequence converges to the zero matrix. Such a sequence occurs in iterative methods (cf. (12.16)), in Markov processes in statistics, in the converge of geometric series of matrices (Neumann series cf. Sect. 12.4.2) and in many other applications.

### 12.4.1 The Spectral Radius

In this section we show the following important theorem.

Theorem 12.10 (When Is $\lim _{k \rightarrow \infty} \boldsymbol{A}^{k}=\mathbf{0}$ ?) For any $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ we have

$$
\lim _{k \rightarrow \infty} \boldsymbol{A}^{k}=\mathbf{0} \Longleftrightarrow \rho(\boldsymbol{A})<1,
$$

where $\rho(\boldsymbol{A})$ is the spectral radius of $\boldsymbol{A}$ given by (12.17).
Clearly $\rho(\boldsymbol{A})<1$ is a necessary condition for $\lim _{k \rightarrow \infty} \boldsymbol{A}^{k}=\mathbf{0}$. For if $(\lambda, \boldsymbol{x})$ is an eigenpair of $\boldsymbol{A}$ with $|\lambda| \geq 1$ and $\|\boldsymbol{x}\|_{2}=1$ then $\boldsymbol{A}^{k} \boldsymbol{x}=\lambda^{k} \boldsymbol{x}$, and this implies $\left\|\boldsymbol{A}^{k}\right\|_{2} \geq\left\|\boldsymbol{A}^{k} \boldsymbol{x}\right\|_{2}=\left\|\lambda^{k} \boldsymbol{x}\right\|_{2}=|\lambda|^{k}$, and it follows that $\boldsymbol{A}^{k}$ does not tend to zero.

The sufficiency condition is harder to show. We construct a consistent matrix norm on $\mathbb{C}^{n \times n}$ such that $\|\boldsymbol{A}\|<1$ and then use Theorems 12.2 and 12.3.

We start with
Theorem 12.11 (Any Consistent Norm Majorizes the Spectral Radius) For any matrix norm $\|\cdot\|$ that is consistent on $\mathbb{C}^{n \times n}$ and any $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ we have $\rho(\boldsymbol{A}) \leq$ $\|\boldsymbol{A}\|$.

Proof Let $(\lambda, \boldsymbol{x})$ be an eigenpair for $\boldsymbol{A},\| \|$ a consistent matrix norm on $\mathbb{C}^{n \times n}$ and define $\boldsymbol{X}:=[\boldsymbol{x}, \ldots, \boldsymbol{x}] \in \mathbb{C}^{n \times n}$. Then $\lambda \boldsymbol{X}=\boldsymbol{A} \boldsymbol{X}$, which implies $|\lambda|\|\boldsymbol{X}\|=$ $\|\lambda \boldsymbol{X}\|=\|\boldsymbol{A} \boldsymbol{X}\| \leq\|\boldsymbol{A}\|\|\boldsymbol{X}\|$. Since $\|\boldsymbol{X}\| \neq 0$ we obtain $|\lambda| \leq\|\boldsymbol{A}\|$. $\square$

The next theorem shows that if $\rho(\boldsymbol{A})<1$ then $\|\boldsymbol{A}\|<1$ for some consistent matrix norm on $\mathbb{C}^{n \times n}$, thus completing the proof of Theorem 12.10.

Theorem 12.12 (The Spectral Radius Can Be Approximated by a Norm) Let $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ and $\epsilon>0$ be given. There is a consistent matrix norm $\|\cdot\|$ on $\mathbb{C}^{n \times n}$ such that $\rho(\boldsymbol{A}) \leq\|\boldsymbol{A}\| \leq \rho(\boldsymbol{A})+\epsilon$.

Proof Let $\boldsymbol{A}$ have eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$. By the Schur Triangulation Theorem 6.5 there is a unitary matrix $\boldsymbol{U}$ and an upper triangular matrix $\boldsymbol{R}=\left[r_{i j}\right]$ such that $\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}=\boldsymbol{R}$. For $t>0$ we define $\boldsymbol{D}_{t}:=\operatorname{diag}\left(t, t^{2}, \ldots, t^{n}\right) \in \mathbb{R}^{n \times n}$, and note that the $(i, j)$ element in $\boldsymbol{D}_{t} \boldsymbol{R} \boldsymbol{D}_{t}^{-1}$ is given by $t^{i-j} r_{i j}$ for all $i, j$. For $n=3$

$$
\boldsymbol{D}_{t} \boldsymbol{R} \boldsymbol{D}_{t}^{-1}=\left[\begin{array}{ccc}
\lambda_{1} & t^{-1} r_{12} & t^{-2} r_{13} \\
0 & \lambda_{2} & t^{-1} r_{23} \\
0 & 0 & \lambda_{3}
\end{array}\right] .
$$

For each $\boldsymbol{B} \in \mathbb{C}^{n \times n}$ and $t>0$ we use the one norm to define the matrix norm $\|\boldsymbol{B}\|_{t}:=\left\|\boldsymbol{D}_{t} \boldsymbol{U}^{*} \boldsymbol{B} \boldsymbol{U} \boldsymbol{D}_{t}^{-1}\right\|_{1}$. We leave it as an exercise to show that $\left\|\|_{t}\right.$ is a consistent matrix norm on $\mathbb{C}^{n \times n}$. We define $\|\boldsymbol{B}\|:=\|\boldsymbol{B}\|_{t}$, where $t$ is chosen so large that the sum of the absolute values of all off-diagonal elements in $\boldsymbol{D}_{t} \boldsymbol{R} \boldsymbol{D}_{t}^{-1}$ is less than $\epsilon$. Then

$$
\begin{aligned}
\|\boldsymbol{A}\| & =\left\|\boldsymbol{D}_{t} \boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U} \boldsymbol{D}_{t}^{-1}\right\|_{1}=\left\|\boldsymbol{D}_{t} \boldsymbol{R} \boldsymbol{D}_{t}^{-1}\right\|_{1}=\max _{1 \leq j \leq n} \sum_{i=1}^{n}\left|\left(\boldsymbol{D}_{t} \boldsymbol{R} \boldsymbol{D}_{t}^{-1}\right)_{i j}\right| \\
& \leq \max _{1 \leq j \leq n}\left(\left|\lambda_{j}\right|+\epsilon\right)=\rho(\boldsymbol{A})+\epsilon .
\end{aligned}
$$ $\square$

A consistent matrix norm of a matrix can be much larger than the spectral radius. However the following result holds.

Theorem 12.13 (Spectral Radius Convergence) For any consistent matrix norm $\|\cdot\|$ on $\mathbb{C}^{n \times n}$ and any $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ we have

$$
\lim _{k \rightarrow \infty}\left\|\boldsymbol{A}^{k}\right\|^{1 / k}=\rho(\boldsymbol{A}) .
$$

Proof Let $\left\|\|\right.$ be a consistent matrix norm on $\mathbb{C}^{n \times n}$. If $\lambda$ is an eigenvalue of $\boldsymbol{A}$ then $\lambda^{k}$ is an eigenvalue of $\boldsymbol{A}^{k}$ for any $k \in \mathbb{N}$. By Theorem 12.11 we then obtain $\rho(\boldsymbol{A})^{k}=\rho\left(\boldsymbol{A}^{k}\right) \leq\left\|\boldsymbol{A}^{k}\right\|$ for any $k \in \mathbb{N}$ so that $\rho(\boldsymbol{A}) \leq\left\|\boldsymbol{A}^{k}\right\|^{1 / k}$. Let $\epsilon>0$ and consider the matrix $\boldsymbol{B}:=(\rho(\boldsymbol{A})+\epsilon)^{-1} \boldsymbol{A}$. Then $\rho(\boldsymbol{B})=\rho(\boldsymbol{A}) /(\rho(\boldsymbol{A})+\epsilon)<1$ and $\left\|\boldsymbol{B}^{k}\right\| \rightarrow 0$ by Theorem 12.10 as $k \rightarrow \infty$. Choose $N \in \mathbb{N}$ such that $\left\|\boldsymbol{B}^{k}\right\|<1$ for all $k \geq N$. Then for $k \geq N$

$$
\left\|\boldsymbol{A}^{k}\right\|=\left\|(\rho(\boldsymbol{A})+\epsilon)^{k} \boldsymbol{B}^{k}\right\|=(\rho(\boldsymbol{A})+\epsilon)^{k}\left\|\boldsymbol{B}^{k}\right\|<(\rho(\boldsymbol{A})+\epsilon)^{k} .
$$

We have shown that $\rho(\boldsymbol{A}) \leq\left\|\boldsymbol{A}^{k}\right\|^{1 / k} \leq \rho(\boldsymbol{A})+\epsilon$ for $k \geq N$. Since $\epsilon$ is arbitrary the result follows. $\square$

### 12.4.2 Neumann Series

Let $\boldsymbol{B}$ be a square matrix. In this section we consider the Neumann series

$$
\sum_{k=0}^{\infty} \boldsymbol{B}^{k}
$$

which is a matrix analogue of a geometric series of numbers.
Consider an infinite series $\sum_{k=0}^{\infty} \boldsymbol{A}_{k}$ of matrices in $\mathbb{C}^{n \times n}$. We say that the series converges if the sequence of partial sums $\left\{\boldsymbol{S}_{m}\right\}$ given by $\boldsymbol{S}_{m}=\sum_{k=0}^{m} \boldsymbol{A}_{k}$ converges. The series converges if and only if $\left\{\boldsymbol{S}_{m}\right\}$ is a Cauchy sequence, i.e. to each $\epsilon>0$ there exists an integer $N$ so that $\left\|\boldsymbol{S}_{l}-\boldsymbol{S}_{m}\right\|<\epsilon$ for all $l>m \geq N$.

Theorem 12.14 (Neumann Series) Suppose $\boldsymbol{B} \in \mathbb{C}^{n \times n}$. Then

1. The series $\sum_{k=0}^{\infty} \boldsymbol{B}^{k}$ converges if and only if $\rho(\boldsymbol{B})<1$.
2. If $\rho(\boldsymbol{B})<1$ then $(\boldsymbol{I}-\boldsymbol{B})$ is nonsingular and $(\boldsymbol{I}-\boldsymbol{B})^{-1}=\sum_{k=0}^{\infty} \boldsymbol{B}^{k}$.
3. If $\|\boldsymbol{B}\|<1$ for some consistent matrix norm $\|\cdot\|$ on $\mathbb{C}^{n \times n}$ then
$$
\left\|(\boldsymbol{I}-\boldsymbol{B})^{-1}\right\| \leq \frac{1}{1-\|\boldsymbol{B}\|} .
$$

Proof

1. Suppose $\rho(\boldsymbol{B})<1$. We show that $\boldsymbol{S}_{m}:=\sum_{k=0}^{m} \boldsymbol{B}^{k}$ is a Cauchy sequence and hence convergent. Let $\epsilon>0$. By Theorem 12.12 there is a consistent matrix norm $\|\cdot\|$ on $\mathbb{C}^{n \times n}$ such that $\|\boldsymbol{B}\|<1$. Then for $l>m$
$$
\left\|\boldsymbol{S}_{l}-\boldsymbol{S}_{m}\right\|=\left\|\sum_{k=m+1}^{l} \boldsymbol{B}^{k}\right\| \leq \sum_{k=m+1}^{l}\|\boldsymbol{B}\|^{k} \leq\|\boldsymbol{B}\|^{m+1} \sum_{k=0}^{\infty}\|\boldsymbol{B}\|^{k}=\frac{\|\boldsymbol{B}\|^{m+1}}{1-\|\boldsymbol{B}\|} .
$$
But then $\left\{\boldsymbol{S}_{m}\right\}$ is a Cauchy sequence provided $N$ is such that $\frac{\|\boldsymbol{B}\|^{N+1}}{1-\|\boldsymbol{B}\|}<\epsilon$.
Conversely, suppose ( $\lambda, \boldsymbol{x}$ ) is an eigenpair for $\boldsymbol{B}$ with $|\lambda| \geq 1$. We find $\boldsymbol{S}_{m} \boldsymbol{x}=$ $\sum_{k=0}^{m} \boldsymbol{B}^{k} \boldsymbol{x}=\left(\sum_{k=0}^{m} \lambda^{k}\right) \boldsymbol{x}$. Since $\lambda^{k}$ does not tend to zero the series $\sum_{k=0}^{\infty} \lambda^{k}$ is not convergent and therefore $\left\{\boldsymbol{S}_{m} \boldsymbol{x}\right\}$ and hence $\left\{\boldsymbol{S}_{m}\right\}$ does not converge.
2. We have
$$
\left(\sum_{k=0}^{m} \boldsymbol{B}^{k}\right)(\boldsymbol{I}-\boldsymbol{B})=\boldsymbol{I}+\boldsymbol{B}+\cdots+\boldsymbol{B}^{m}-\left(\boldsymbol{B}+\cdots+\boldsymbol{B}^{m+1}\right)=\boldsymbol{I}-\boldsymbol{B}^{m+1} .
$$
Since $\rho(\boldsymbol{B})<1$ we conclude that $\boldsymbol{B}^{m+1} \rightarrow 0$ and hence taking limits in (12.36) we obtain $\left(\sum_{k=0}^{\infty} \boldsymbol{B}^{k}\right)(\boldsymbol{I}-\boldsymbol{B})=\boldsymbol{I}$ which completes the proof of 2 .
3. By 2: $\left\|(\boldsymbol{I}-\boldsymbol{B})^{-1}\right\|=\left\|\sum_{k=0}^{\infty} \boldsymbol{B}^{k}\right\| \leq \sum_{k=0}^{\infty}\|\boldsymbol{B}\|^{k}=\frac{1}{1-\|\boldsymbol{B}\|}$. $\square$

### 12.5 The Optimal SOR Parameter $\boldsymbol{\omega}$

The following analysis is only carried out for the discrete Poisson matrix. It also holds for the averaging matrix given by (10.10). A more general theory is presented in [22]. We will compare the eigenpair equations for $\boldsymbol{G}_{J}$ and $\boldsymbol{G}_{\omega}$. It is convenient to write these equations using the matrix formulation $\boldsymbol{T} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}=h^{2} \boldsymbol{F}$. If $\boldsymbol{G}_{J} \boldsymbol{v}=\mu \boldsymbol{v}$ is an eigenpair of $\boldsymbol{G}_{J}$ then

$$
\frac{1}{4}\left(v_{i-1, j}+v_{i, j-1}+v_{i+1, j}+v_{i, j+1}\right)=\mu v_{i, j}, \quad i, j=1, \ldots, m,
$$

where $\boldsymbol{v}:=\operatorname{vec}(\boldsymbol{V}) \in \mathbb{R}^{m^{2}}$ and $v_{i, j}=0$ if $i \in\{0, m+1\}$ or $j \in\{0, m+1\}$.
Suppose $(\lambda, \boldsymbol{w})$ is an eigenpair for $\boldsymbol{G}_{\omega}$. By $(12.21)(\boldsymbol{I}-\omega \boldsymbol{L})^{-1}(\omega \boldsymbol{R}+(1-$ $\omega) \boldsymbol{I}) \boldsymbol{w}=\lambda \boldsymbol{w}$ or

$$
(\omega \boldsymbol{R}+\lambda \omega \boldsymbol{L}) \boldsymbol{w}=(\lambda+\omega-1) \boldsymbol{w} .
$$

Let $\boldsymbol{w}=\operatorname{vec}(\boldsymbol{W})$, where $\boldsymbol{W} \in \mathbb{C}^{m \times m}$. Then (12.38) can be written

$$
\frac{\omega}{4}\left(\lambda w_{i-1, j}+\lambda w_{i, j-1}+w_{i+1, j}+w_{i, j+1}\right)=(\lambda+\omega-1) w_{i, j}
$$

where $w_{i, j}=0$ if $i \in\{0, m+1\}$ or $j \in\{0, m+1\}$.
Theorem 12.15 (The Optimal $\omega$ ) Consider the SOR method applied to the discrete Poisson matrix (10.10), where we use the natural ordering. Moreover, assume $\omega \in(0,2)$.

1. If $\lambda \neq 0$ is an eigenvalue of $\boldsymbol{G}_{\omega}$ then
$$
\mu:=\frac{\lambda+\omega-1}{\omega \lambda^{1 / 2}}
$$
is an eigenvalue of $\boldsymbol{G}_{J}$.
2. If $\mu$ is an eigenvalue of $\boldsymbol{G}_{J}$ and $\lambda$ satisfies the equation
$$
\mu \omega \lambda^{1 / 2}=\lambda+\omega-1
$$
then $\lambda$ is an eigenvalue of $\boldsymbol{G}_{\omega}$.

Proof Suppose $(\lambda, \boldsymbol{w})$ is an eigenpair for $\boldsymbol{G}_{\omega}$. We claim that $(\mu, \boldsymbol{v})$ is an eigenpair for $\boldsymbol{G}_{J}$, where $\mu$ is given by (12.40) and $\boldsymbol{v}=(\boldsymbol{V})$ with $v_{i, j}:=\lambda^{-(i+j) / 2} w_{i, j}$. Indeed, replacing $w_{i, j}$ by $\lambda^{(i+j) / 2} v_{i, j}$ in (12.39) and cancelling the common factor $\lambda^{(i+j) / 2}$ we obtain

$$
\frac{\omega}{4}\left(v_{i-1, j}+v_{i, j-1}+v_{i+1, j}+v_{i, j+1}\right)=\lambda^{-1 / 2}(\lambda+\omega-1) v_{i, j} .
$$

But then

$$
\boldsymbol{G}_{J} \boldsymbol{v}=(\boldsymbol{L}+\boldsymbol{R}) \boldsymbol{v}=\frac{\lambda+\omega-1}{\omega \lambda^{1 / 2}} \boldsymbol{v}=\mu \boldsymbol{v} .
$$

For the converse let $(\mu, \boldsymbol{v})$ be an eigenpair for $\boldsymbol{G}_{J}$ and let et $\lambda$ be a solution of (12.41). We define as before $\boldsymbol{v}=: \operatorname{vec}(\boldsymbol{V}), \boldsymbol{W}=\operatorname{vec}(\boldsymbol{W})$ with $w_{i, j}:=\lambda^{(i+j) / 2} v_{i, j}$. Inserting this in (12.37) and canceling $\lambda^{-(i+j) / 2}$ we obtain

$$
\frac{1}{4}\left(\lambda^{1 / 2} w_{i-1, j}+\lambda^{1 / 2} w_{i, j-1}+\lambda^{-1 / 2} w_{i+1, j}+\lambda^{-1 / 2} w_{i, j+1}\right)=\mu w_{i, j} .
$$

Multiplying by $\omega \lambda^{1 / 2}$ we obtain

$$
\frac{\omega}{4}\left(\lambda w_{i-1, j}+\lambda w_{i, j-1}+w_{i+1, j}+w_{i, j+1}\right)=\omega \mu \lambda^{1 / 2} w_{i, j}
$$

Thus, if $\omega \mu \lambda^{1 / 2}=\lambda+\omega-1$ then by (12.39) ( $\lambda, \boldsymbol{w}$ ) is an eigenpair for $\boldsymbol{G}_{\omega}$. $\square$

Proof of Theorem 12.8 Combining statement 1 and 2 in Theorem 12.15 we see that $\rho\left(\boldsymbol{G}_{\omega}\right)=|\lambda(\mu)|$, where $\lambda(\mu)$ is an eigenvalue of $\boldsymbol{G}_{\omega}$ satisfying (12.41) for some eigenvalue $\mu$ of $\boldsymbol{G}_{J}$. The eigenvalues of $\boldsymbol{G}_{J}$ are $\frac{1}{2} \cos (j \pi h)+\frac{1}{2} \cos (k \pi h)$, $j, k=1, \ldots, m$, so $\mu$ is real and both $\mu$ and $-\mu$ are eigenvalues. Thus, to compute $\rho\left(\boldsymbol{G}_{\omega}\right)$ it is enough to consider (12.41) for a positive eigenvalue $\mu$ of $\boldsymbol{G}_{J}$. Solving (12.41) for $\lambda=\lambda(\mu)$ gives

$$
\lambda(\mu):=\frac{1}{4}\left(\omega \mu \pm \sqrt{(\omega \mu)^{2}-4(\omega-1)}\right)^{2} .
$$

Both roots $\lambda(\mu)$ are eigenvalues of $\boldsymbol{G}_{\omega}$. The discriminant

$$
d(\omega):=(\omega \mu)^{2}-4(\omega-1) .
$$

is strictly decreasing on $(0,2)$ since

$$
d^{\prime}(\omega)=2\left(\omega \mu^{2}-2\right)<2(\omega-2)<0 .
$$

Moreover $d(0)=4>0$ and $d(2)=4 \mu^{2}-4<0$. As a function of $\omega, \lambda(\mu)$ changes from real to complex when $d(\omega)=0$. The root in (0, 2) is

$$
\omega=\tilde{\omega}(\mu):=2 \frac{1-\sqrt{1-\mu^{2}}}{\mu^{2}}=\frac{2}{1+\sqrt{1-\mu^{2}}} .
$$

In the complex case we find

$$
|\lambda(\mu)|=\frac{1}{4}\left((\omega \mu)^{2}+4(\omega-1)-(\omega \mu)^{2}\right)=\omega-1, \quad \tilde{\omega}(\mu)<\omega<2 .
$$

In the real case both roots of (12.42) are positive and the larger one is

$$
\lambda(\mu)=\frac{1}{4}\left(\omega \mu+\sqrt{(\omega \mu)^{2}-4(\omega-1)}\right)^{2}, \quad 0<\omega \leq \tilde{\omega}(\mu) .
$$

Both $\lambda(\mu)$ and $\tilde{\omega}(\mu)$ are strictly increasing as functions of $\mu$. It follows that $|\lambda(\mu)|$ is maximized for $\mu=\rho\left(\boldsymbol{G}_{J}\right)=: \beta$ and for this value of $\mu$ we obtain (12.27) for $0<\omega \leq \tilde{\omega}(\beta)=\omega^{*}$.

Evidently $\rho\left(\boldsymbol{G}_{\omega}\right)=\omega-1$ is strictly increasing in $\omega^{*}<\omega<2$. Equation (12.29) will follow if we can show that $\rho\left(\boldsymbol{G}_{\omega}\right)$ is strictly decreasing in $0<\omega<\omega^{*}$. By differentiation

$$
\frac{d}{d \omega}\left(\omega \beta+\sqrt{(\omega \beta)^{2}-4(\omega-1)}\right)=\frac{\beta \sqrt{(\omega \beta)^{2}-4(\omega-1)}+\omega \beta^{2}-2}{\sqrt{(\omega \beta)^{2}-4(\omega-1)}} .
$$

Since $\beta^{2}\left(\omega^{2} \beta^{2}-4 \omega+4\right)<\left(2-\omega \beta^{2}\right)^{2}$ the numerator is negative and the strict decrease of $\rho\left(\boldsymbol{G}_{\omega}\right)$ in $0<\omega<\omega^{*}$ follows. $\square$

### 12.6 Exercises Chap. 12

### 12.6.1 Exercises Sect. 12.3

Exercise 12.1 (Richardson and Jacobi) Show that if $a_{i i}=d \neq 0$ for all $i$ then Richardson's method with $\alpha:=1 / d$ is the same as Jacobi's method.

Exercise 12.2 (R-Method When Eigenvalues Have Positive Real Part) Suppose all eigenvalues $\lambda_{j}$ of $\boldsymbol{A}$ have positive real parts $u_{j}$ for $j=1, \ldots, n$ and that $\alpha$ is real. Show that the R method converges if and only if $0<\alpha<\min _{j}\left(2 u_{j} /\left|\lambda_{j}\right|^{2}\right)$.

Exercise 12.3 (Divergence Example for J and GS) Show that both Jacobi's method and Gauss-Seidel's method diverge for $\boldsymbol{A}=\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]$.

Exercise 12.4 (2 by 2 Matrix) We want to show that Gauss-Seidel converges if and only if Jacobi converges for a 2 by 2 matrix $\boldsymbol{A}:=\left[\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22}\end{array}\right] \in \mathbb{R}^{2 \times 2}$.

a) Show that the spectral radius for the Jacobi method is
$$
\rho\left(\boldsymbol{G}_{J}\right)=\sqrt{\left|a_{21} a_{12} / a_{11} a_{22}\right|} .
$$
b) Show that the spectral radius for the Gauss-Seidel method is
$$
\rho\left(\boldsymbol{G}_{1}\right)=\left|a_{21} a_{12} / a_{11} a_{22}\right| .
$$
c) Conclude that Gauss-Seidel converges if and only if Jacobi converges.

Exercise 12.5 (Example: GS Converges, J Diverges) Show (by finding its eigenvalues) that the matrix $\left[\begin{array}{ccc}1 & a & a \\ a & 1 & a \\ a & a & 1\end{array}\right]$ is positive definite for $-1 / 2<a<1$. Thus, GS converges for these values of $a$. Show that the J method does not converge for $1 / 2<a<1$.

Exercise 12.6 (Example: GS Diverges, J Converges) Let $\boldsymbol{G}_{J}$ and $\boldsymbol{G}_{1}$ be the iteration matrices for the Jacobi and Gauss-Seidel methods applied to the matrix $\boldsymbol{A}:=\left[\begin{array}{ccc}1 & 0 & 1 / 2 \\ 1 & 1 & 0 \\ -1 & 1 & 1\end{array}\right] .1$

a) Show that $\boldsymbol{G}_{1}:=\left[\begin{array}{ccc}0 & 0 & -1 / 2 \\ 0 & 0 & 1 / 2 \\ 0 & 0 & -1\end{array}\right]$ and conclude that GS diverges.
b) Show that $p(\lambda):=\operatorname{det}\left(\lambda \boldsymbol{I}-\boldsymbol{G}_{J}\right)=\lambda^{3}+\frac{1}{2} \lambda+\frac{1}{2}$.
c) Show that if $|\lambda| \geq 1$ then $p(\lambda) \neq 0$. Conclude that J converges.

Exercise 12.7 (Strictly Diagonally Dominance; The J Method) Show that the J method converges if $\left|a_{i i}\right|>\sum_{j \neq i}\left|a_{i j}\right|$ for $i=1, \ldots, n$.

[^21]Exercise 12.8 (Strictly Diagonally Dominance; The GS Method) Consider the GS method. Suppose $r:=\max _{i} r_{i}<1$, where $r_{i}=\sum_{j \neq i} \frac{\left|a_{i j}\right|}{\left|a_{i i}\right|}$. Show using induction on $i$ that $\left|\boldsymbol{\epsilon}_{k+1}(j)\right| \leq r\left\|\boldsymbol{\epsilon}_{k}\right\|_{\infty}$ for $j=1, \ldots, i$. Conclude that Gauss-Seidel's method is convergent when $\boldsymbol{A}$ is strictly diagonally dominant.

Exercise 12.9 (Convergence Example for Fix Point Iteration) Consider for $a \in$ $\mathbb{C}$

$$
\boldsymbol{x}:=\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{ll}
0 & a \\
a & 0
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]+\left[\begin{array}{l}
1-a \\
1-a
\end{array}\right]=: \boldsymbol{G} \boldsymbol{x}+\boldsymbol{c} .
$$

Starting with $\boldsymbol{x}_{0}=\mathbf{0}$ show by induction

$$
\boldsymbol{x}_{k}(1)=\boldsymbol{x}_{k}(2)=1-a^{k}, \quad k \geq 0,
$$

and conclude that the iteration converges to the fixed-point $\boldsymbol{x}=[1,1]^{T}$ for $|a|<1$ and diverges for $|a|>1$. Show that $\rho(\boldsymbol{G})=1-\eta$ with $\eta=1-|a|$. Compute the estimate (12.31) for the rate of convergence for $a=0.9$ and $s=16$ and compare with the true number of iterations determined from $|a|^{k} \leq 10^{-16}$.

Exercise 12.10 (Estimate in Lemma 12.1 Can Be Exact) Consider the iteration in Example 12.2. Show that $\rho\left(\boldsymbol{G}_{J}\right)=1 / 2$. Then show that $\boldsymbol{x}_{k}(1)=\boldsymbol{x}_{k}(2)=1-2^{-k}$ for $k \geq 0$. Thus the estimate in Lemma 12.1 is exact in this case.

Exercise 12.11 (Iterative Method (Exam Exercise 1991-3)) Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be a symmetric positive definite matrix with ones on the diagonal and let $\boldsymbol{b} \in \mathbb{R}^{n}$. We will consider an iterative method for the solution of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Observe that $\boldsymbol{A}$ may be written $\boldsymbol{A}=\boldsymbol{I}-\boldsymbol{L}-\boldsymbol{L}^{T}$, where $\boldsymbol{L}$ is lower triangular with zero's on the diagonal, $l_{i, j}=0$, when $j>=i$. The method is defined by

$$
\boldsymbol{M} \boldsymbol{x}_{k+1}=\boldsymbol{N} \boldsymbol{x}_{k}+\boldsymbol{b},
$$

where $\boldsymbol{M}$ and $\boldsymbol{N}$ are given by the splitting

$$
\boldsymbol{A}=\boldsymbol{M}-\boldsymbol{N}, \quad \boldsymbol{M}=(\boldsymbol{I}-\boldsymbol{L})\left(\boldsymbol{I}-\boldsymbol{L}^{T}\right), \quad \boldsymbol{N}=\boldsymbol{L} \boldsymbol{L}^{T} .
$$

a) Let $\boldsymbol{x} \neq \mathbf{0}$ be an eigenvector of $\boldsymbol{M}^{-1} \boldsymbol{N}$ with eigenvalue $\lambda$. Show that
$$
\lambda=\frac{\boldsymbol{x}^{T} \boldsymbol{N} \boldsymbol{x}}{\boldsymbol{x}^{T} \boldsymbol{A x}+\boldsymbol{x}^{T} \boldsymbol{N} \boldsymbol{x}} .
$$
b) Show that the sequence $\left\{\boldsymbol{x}_{k}\right\}$ generated by (12.45) converges to the solution $\boldsymbol{x}$ of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ for any starting vector $\boldsymbol{x}_{0}$.

c) Consider the following algorithm


1. Choose $\boldsymbol{x}=[x(1), x(2), \ldots, x(n)]^{T}$.
2. for $k=1,2,3, \ldots$
for $i=1,2, \ldots, n-1, n, n, n-1, n-2, \ldots, 1$
$$
x(i)=b(i)-\sum_{j \neq i} a(i, j) x(j)
$$

Is there a connection between this algorithm and the method of Gauss-Seidel? Show that the algorithm (12.48) leads up to the splitting (12.46).

Exercise 12.12 (Gauss-Seidel Method (Exam Exercise 2008-1)) Consider the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ in which

$$
A:=\left[\begin{array}{lll}
3 & 0 & 1 \\
0 & 7 & 2 \\
1 & 2 & 4
\end{array}\right]
$$

and $\boldsymbol{b}:=[1,9,-2]^{T}$.

a) With $\boldsymbol{x}_{0}=[1,1,1]^{t}$, carry out one iteration of the Gauss-Seidel method to find $\boldsymbol{x}_{1} \in \mathbb{R}^{3}$.
b) If we continue the iteration, will the method converge? Why?
c) Write a MATLAB program for the Gauss-Seidel method applied to a matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ and right-hand side $\boldsymbol{b} \in \mathbb{R}^{n}$. Use the ratio of the current residual to the initial residual as the stopping criterion, as well as a maximum number of iterations. ${ }^{2}$

### 12.6.2 Exercises Sect. 12.4

Exercise 12.13 (A Special Norm) Show that $\|\boldsymbol{B}\|_{t}:=\left\|\boldsymbol{D}_{t} \boldsymbol{U}^{*} \boldsymbol{B} \boldsymbol{U} \boldsymbol{D}_{t}^{-1}\right\|_{1}$ defined in the proof of Theorem 12.12 is a consistent matrix norm on $\mathbb{C}^{n \times n}$.

Exercise 12.14 (Is $\boldsymbol{A}+\boldsymbol{E}$ Nonsingular?) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular and $\boldsymbol{E} \in \mathbb{C}^{n \times n}$. Show that $\boldsymbol{A}+\boldsymbol{E}$ is nonsingular if $\rho\left(\boldsymbol{A}^{-1} \boldsymbol{E}\right)<1$.

[^22]Exercise 12.15 (Slow Spectral Radius Convergence) The convergence $\lim _{k \rightarrow \infty} \|$ $\boldsymbol{A}^{k} \|^{1 / k}=\rho(\boldsymbol{A})$ can be quite slow. Consider

$$
\boldsymbol{A}:=\left[\begin{array}{cccccc}
\lambda & 0 & \cdots & 0 & 0 \\
0 & \lambda & a & \cdots & 0 & 0 \\
0 & 0 & \lambda & \cdots & 0 & 0 \\
\vdots & & & & \vdots \\
0 & 0 & 0 & \cdots & \lambda & a \\
0 & 0 & 0 & \cdots & 0 & \lambda
\end{array}\right] \in \mathbb{R}^{n \times n} .
$$

If $|\lambda|=\rho(\boldsymbol{A})<1$ then $\lim _{k \rightarrow \infty} \boldsymbol{A}^{k}=\mathbf{0}$ for any $a \in \mathbb{R}$. We show below that the $(1, n)$ element of $\boldsymbol{A}^{k}$ is given by $f(k):=\binom{k}{n-1} a^{n-1} \lambda^{k-n+1}$ for $k \geq n-1$.

a) Pick an $n$, e.g. $n=5$, and make a plot of $f(k)$ for $\lambda=0.9, a=10$, and $n-1 \leq k \leq 200$. Your program should also compute $\max _{k} f(k)$. Use your program to determine how large $k$ must be before $f(k)<10^{-8}$.
b) We can determine the elements of $\boldsymbol{A}^{k}$ explicitly for any $k$. Let $\boldsymbol{E}:=(\boldsymbol{A}-\lambda \boldsymbol{I}) / a$. Show by induction that $\boldsymbol{E}^{k}=\left[\begin{array}{cc}\mathbf{0} & \boldsymbol{I}_{n-k} \\ \mathbf{0} & \mathbf{0}\end{array}\right]$ for $1 \leq k \leq n-1$ and that $\boldsymbol{E}^{n}=\mathbf{0}$.
c) We have $\boldsymbol{A}^{k}=(a \boldsymbol{E}+\lambda \boldsymbol{I})^{k}=\sum_{j=0}^{\min \{k, n-1\}}\binom{k}{j} a^{j} \lambda^{k-j} \boldsymbol{E}^{j}$ and conclude that the $(1, n)$ element is given by $f(k)$ for $k \geq n-1$.

### 12.7 Review Questions

12.7.1 Consider a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ with nonzero diagonal elements.
    - Define the J and GS method in component form,
    - Do they always converge?
    - Give a necessary and sufficient condition that $\boldsymbol{A}^{n} \rightarrow \mathbf{0}$.
    - Is there a matrix norm $\left\|\|\right.$ consistent on $\mathbb{C}^{n \times n}$ such that $\| \boldsymbol{A} \|<\rho(\boldsymbol{A})$ ?
12.7.2 What is a Neumann series? when does it converge?
12.7.3 How do we define convergence of a fixed point iteration $\boldsymbol{x}_{k+1}=\boldsymbol{G} \boldsymbol{x}_{k}+\boldsymbol{c}$ ? When does it converge?
12.7.4 Define Richardson's method.

## Chapter 13 <br> The Conjugate Gradient Method

The conjugate gradient method was published by Hestenes and Stiefel in 1952, [6] as a direct method for solving linear systems. Today its main use is as an iterative method for solving large sparse linear systems. On a test problem we show that it performs as well as the SOR method with optimal acceleration parameter, and we do not have to estimate any such parameter. However the conjugate gradient method is restricted to positive definite systems. We also consider a mathematical formulation of the preconditioned conjugate gradient method. It is used to speed up convergence of the conjugate gradient method. We only give one example of a possible preconditioner. See [1] for a more complete treatment of iterative methods and preconditioning.

The conjugate gradient method can also be used for minimization and is related to a method known as steepest descent. This method and the conjugate gradient method are both minimization methods, and iterative methods, for solving equations.

Throughout this chapter $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ will be a symmetric and positive definite matrix. We recall that $\boldsymbol{A}$ has positive eigenvalues and that the spectral (2-norm) condition number of $\boldsymbol{A}$ is given by $\kappa:=\frac{\lambda_{\text {max }}}{\lambda_{\text {min }}}$, where $\lambda_{\text {max }}$ and $\lambda_{\text {min }}$ are the largest and smallest eigenvalue of $\boldsymbol{A}$.

The analysis of the methods in this chapter is in terms of two inner products on $\mathbb{R}^{n}$, the usual inner product $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\boldsymbol{x}^{T} \boldsymbol{y}$ with the associated Euclidian norm $\|\boldsymbol{x}\|_{2}=\sqrt{\boldsymbol{x}^{T} \boldsymbol{x}}$, and the $\boldsymbol{A}$-inner product and the corresponding $\boldsymbol{A}$-norm given by

$$
\langle\boldsymbol{x}, \boldsymbol{y}\rangle_{\boldsymbol{A}}:=\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{y}, \quad\|\boldsymbol{y}\|_{\boldsymbol{A}}:=\sqrt{\boldsymbol{y}^{T} \boldsymbol{A} \boldsymbol{y}}, \quad \boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n} .
$$

We note that the $\boldsymbol{A}$-inner product is an inner product on $\mathbb{R}^{n}$. Indeed, for any $\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z} \in$ $\mathbb{R}^{n}$

1. $\langle\boldsymbol{x}, \boldsymbol{x}\rangle_{\boldsymbol{A}}=\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x} \geq 0$ and $\langle\boldsymbol{x}, \boldsymbol{x}\rangle_{\boldsymbol{A}}=0$ if and only if $\boldsymbol{x}=\mathbf{0}$, since $\boldsymbol{A}$ is positive definite,
2. $\langle\boldsymbol{x}, \boldsymbol{y}\rangle_{\boldsymbol{A}}:=\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{y}=\left(\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{y}\right)^{T}=\boldsymbol{y}^{T} \boldsymbol{A}^{T} \boldsymbol{x}=\boldsymbol{y}^{T} \boldsymbol{A} \boldsymbol{x}=\langle\boldsymbol{y}, \boldsymbol{x}\rangle_{\boldsymbol{A}}$ by symmetry of $\boldsymbol{A}$,
3. $\langle\boldsymbol{x}+\boldsymbol{y}, \boldsymbol{z}\rangle_{\boldsymbol{A}}:=\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{z}+\boldsymbol{y}^{T} \boldsymbol{A} \boldsymbol{z}=\langle\boldsymbol{x}, \boldsymbol{z}\rangle_{\boldsymbol{A}}+\langle\boldsymbol{y}, \boldsymbol{z}\rangle_{\boldsymbol{A}}$, true for any $\boldsymbol{A}$.

By Theorem 5.2 the $\boldsymbol{A}$-norm is a vector norm on $\mathbb{R}^{n}$ since it is an inner product norm, and the Cauchy-Schwarz inequality holds

$$
\left|\boldsymbol{x}^{T} \boldsymbol{A y}\right|^{2} \leq\left(\boldsymbol{x}^{T} \boldsymbol{A x}\right)\left(\boldsymbol{y}^{T} \boldsymbol{A y}\right), \quad \boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n} .
$$

### 13.1 Quadratic Minimization and Steepest Descent

We start by discussing some aspect of quadratic minimization and its relation to solving linear systems.

Consider for a positive definite $\boldsymbol{A} \in \mathbb{R}^{n \times n}, \boldsymbol{b} \in \mathbb{R}^{n}$ and $c \in \mathbb{R}$ the quadratic function $Q: \mathbb{R}^{n} \rightarrow \mathbb{R}$ given by

$$
Q(\boldsymbol{y}):=\frac{1}{2} \boldsymbol{y}^{T} \boldsymbol{A} \boldsymbol{y}-\boldsymbol{b}^{T} \boldsymbol{y}+c .
$$

As an example, some level curves of

$$
Q(x, y):=\frac{1}{2}\left[\begin{array}{ll}
x & y
\end{array}\right]\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right]\left[\begin{array}{l}
x \\
y
\end{array}\right]=x^{2}-x y+y^{2}
$$

are shown in Fig. 13.1. The level curves are ellipses and the graph of $Q$ is a paraboloid (cf. Exercise 13.2).

The following expansion will be used repeatedly. For $\boldsymbol{y}, \boldsymbol{h} \in \mathbb{R}^{n}$ and $\varepsilon \in \mathbb{R}$

$$
Q(\boldsymbol{y}+\varepsilon \boldsymbol{h})=Q(\boldsymbol{y})-\varepsilon \boldsymbol{h}^{T} r(\boldsymbol{y})+\frac{1}{2} \varepsilon^{2} \boldsymbol{h}^{T} \boldsymbol{A} \boldsymbol{h}, \text { where } r(\boldsymbol{y}):=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{y} .
$$

Minimizing a quadratic function is equivalent to solving a linear system.
Lemma 13.1 (Quadratic Function) A vector $\boldsymbol{x} \in \mathbb{R}^{n}$ minimizes Q given by (13.3) if and only if $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Moreover, the residual $\boldsymbol{r}(\boldsymbol{y}):=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{y}$ for any $\boldsymbol{y} \in \mathbb{R}^{n}$ is equal to the negative gradient, i.e., $\boldsymbol{r}(\boldsymbol{y})=-\nabla Q(\boldsymbol{y})$, where $\nabla:=\left[\frac{\partial}{\partial y_{1}}, \ldots, \frac{\partial}{\partial y_{n}}\right]^{T}$.

Proof If $\boldsymbol{y}=\boldsymbol{x}, \varepsilon=1$, and $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, then (13.5) simplifies to $Q(\boldsymbol{x}+\boldsymbol{h})=$ $Q(\boldsymbol{x})+\frac{1}{2} \boldsymbol{h}^{T} \boldsymbol{A} \boldsymbol{h}$, and since $\boldsymbol{A}$ is positive definite $Q(\boldsymbol{x}+\boldsymbol{h})>Q(\boldsymbol{x})$ for all nonzero $\boldsymbol{h} \in \mathbb{R}^{n}$. It follows that $\boldsymbol{x}$ is the unique minimum of $Q$. Conversely, if $\boldsymbol{A} \boldsymbol{x} \neq \boldsymbol{b}$ and

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-292.jpg?height=586&width=847&top_left_y=211&top_left_x=339)
Fig. 13.1 Level curves for $Q(x, y)$ given by (13.4). Also shown is a steepest descent iteration (left) and a conjugate gradient iteration (right) to find the minimum of $Q$ (cf Examples 13.1,13.2)

$\boldsymbol{h}:=\boldsymbol{r}(\boldsymbol{x})$, then by (13.5), $Q(\boldsymbol{x}+\varepsilon \boldsymbol{h})-Q(\boldsymbol{x})=-\varepsilon\left(\boldsymbol{h}^{T} \boldsymbol{r}(x)-\frac{1}{2} \varepsilon \boldsymbol{h}^{T} \boldsymbol{A} \boldsymbol{h}\right)<0$ for $\varepsilon>0$ sufficiently small. Thus $\boldsymbol{x}$ does not minimize $Q$. By (13.5) for $\boldsymbol{y} \in \mathbb{R}^{n}$

$$
\begin{aligned}
\frac{\partial}{\partial y_{i}} Q(\boldsymbol{y}) & :=\lim _{\varepsilon \rightarrow 0} \frac{1}{\varepsilon}\left(Q\left(\boldsymbol{y}+\varepsilon \boldsymbol{e}_{i}\right)-Q(\boldsymbol{y})\right) \\
& \left.=\lim _{\varepsilon \rightarrow 0} \frac{1}{\varepsilon}\left(-\varepsilon \boldsymbol{e}_{i}^{T} \boldsymbol{r}(\boldsymbol{y})\right)+\frac{1}{2} \varepsilon^{2} \boldsymbol{e}_{i}^{T} \boldsymbol{A} \boldsymbol{e}_{i}\right)=-\boldsymbol{e}_{i}^{T} \boldsymbol{r}(\boldsymbol{y}), \quad i=1, \ldots, n,
\end{aligned}
$$

showing that $\boldsymbol{r}(\boldsymbol{y})=-\nabla Q(\boldsymbol{y})$. $\square$

A general class of minimization algorithms for $Q$ and solution algorithms for a linear system is given as follows:

1. Choose $\boldsymbol{x}_{0} \in \mathbb{R}^{n}$.
2. For $k=0,1,2, \ldots$
Choose a "search direction" $\boldsymbol{p}_{k}$,
Choose a "step length" $\alpha_{k}$,
Compute $\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}$.

We would like to generate a sequence $\left\{\boldsymbol{x}_{k}\right\}$ that converges quickly to the minimum $\boldsymbol{x}$ of $Q$.

For a fixed direction $\boldsymbol{p}_{k}$ we say that $\alpha_{k}$ is optimal if $Q\left(\boldsymbol{x}_{k+1}\right)$ is as small as possible, i.e.

$$
Q\left(\boldsymbol{x}_{k+1}\right)=Q\left(\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}\right)=\min _{\alpha \in \mathbb{R}} Q\left(\boldsymbol{x}_{k}+\alpha \boldsymbol{p}_{k}\right) .
$$

By (13.5) we have $Q\left(\boldsymbol{x}_{k}+\alpha \boldsymbol{p}_{k}\right)=Q\left(\boldsymbol{x}_{k}\right)-\alpha \boldsymbol{p}_{k}^{T} \boldsymbol{r}_{k}+\frac{1}{2} \alpha^{2} \boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k}$, where $\boldsymbol{r}_{k}:=$ $\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}$. Since $\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k} \geq 0$ we find a minimum $\alpha_{k}$ by solving $\frac{\partial}{\partial \alpha} Q\left(\boldsymbol{x}_{k}+\alpha \boldsymbol{p}_{k}\right)=0$. It follows that the optimal $\alpha_{k}$ is uniquely given by

$$
\alpha_{k}:=\frac{\boldsymbol{p}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k}} .
$$

In the method of steepest descent, also known as the gradient method, we choose $\boldsymbol{p}_{k}=\boldsymbol{r}_{k}$ the negative gradient, and the optimal $\alpha_{k}$. Starting from $\boldsymbol{x}_{0}$ we compute for $k=0,1,2 \ldots$

$$
\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\left(\frac{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{r}_{k}^{T} \boldsymbol{A} \boldsymbol{r}_{k}}\right) \boldsymbol{r}_{k} .
$$

This is similar to Richardson's method (12.18), but in that method we used a constant step length. Computationally, a step in the steepest descent iteration can be organized as follows

$$
\begin{aligned}
\boldsymbol{p}_{k} & =\boldsymbol{r}_{k}, \boldsymbol{t}_{k}=\boldsymbol{A} \boldsymbol{p}_{k}, \\
\alpha_{k} & =\left(\boldsymbol{p}_{k}^{T} \boldsymbol{r}_{k}\right) /\left(\boldsymbol{p}_{k}^{T} \boldsymbol{t}_{k}\right), \\
\boldsymbol{x}_{k+1} & =\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}, \\
\boldsymbol{r}_{k+1} & =\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{t}_{k} .
\end{aligned}
$$

Here, and in general, the following update of the residual is used:

$$
\boldsymbol{r}_{k+1}=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k+1}=\boldsymbol{b}-\boldsymbol{A}\left(\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}\right)=\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{A} \boldsymbol{p}_{k} .
$$

In the steepest descent method the choice $\boldsymbol{p}_{k}=\boldsymbol{r}_{k}$ implies that the last two gradients are orthogonal. Indeed, by (13.10), $\boldsymbol{r}_{k+1}^{T} \boldsymbol{r}_{k}=\left(\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{A} \boldsymbol{r}_{k}\right)^{T} \boldsymbol{r}_{k}=0$ since $\alpha_{k}=$ $\frac{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{r}_{k}^{T} \boldsymbol{A} \boldsymbol{r}_{k}}$ and $\boldsymbol{A}$ is symmetric.
Example 13.1 (Steepest Descent Iteration) Suppose $Q(x, y)$ is given by (13.4). Starting with $\boldsymbol{x}_{0}=[-1,-1 / 2]^{T}$ and $\boldsymbol{r}_{0}=-\boldsymbol{A} \boldsymbol{x}_{0}=[3 / 2,0]^{T}$ we find

$$
\begin{aligned}
& \boldsymbol{t}_{0}=3\left[\begin{array}{c}
1 \\
-1 / 2
\end{array}\right], \quad \alpha_{0}=\frac{1}{2}, \quad \boldsymbol{x}_{1}=-4^{-1}\left[\begin{array}{l}
1 \\
2
\end{array}\right], \quad \boldsymbol{r}_{1}=3 * 4^{-1}\left[\begin{array}{l}
0 \\
1
\end{array}\right] \\
& \boldsymbol{t}_{1}=3 * 4^{-1}\left[\begin{array}{c}
-1 \\
2
\end{array}\right], \quad \alpha_{1}=\frac{1}{2}, \quad \boldsymbol{x}_{2}=-4^{-1}\left[\begin{array}{c}
1 \\
1 / 2
\end{array}\right], \quad \boldsymbol{r}_{2}=3 * 4^{-1}\left[\begin{array}{c}
1 / 2 \\
0
\end{array}\right],
\end{aligned}
$$

and in general for $k \geq 1$

$$
\begin{aligned}
& \boldsymbol{t}_{2 k-2}=3 * 4^{1-k}\left[\begin{array}{c}
1 \\
-1 / 2
\end{array}\right], \quad \boldsymbol{x}_{2 k-1}=-4^{-k}\left[\begin{array}{l}
1 \\
2
\end{array}\right], \quad \boldsymbol{r}_{2 k-1}=3 * 4^{-k}\left[\begin{array}{l}
0 \\
1
\end{array}\right] \\
& \boldsymbol{t}_{2 k-1}=3 * 4^{-k}\left[\begin{array}{c}
-1 \\
2
\end{array}\right], \quad \boldsymbol{x}_{2 k}=-4^{-k}\left[\begin{array}{c}
1 \\
1 / 2
\end{array}\right], \quad \boldsymbol{r}_{2 k}=3 * 4^{-k}\left[\begin{array}{c}
1 / 2 \\
0
\end{array}\right] .
\end{aligned}
$$

Since $\alpha_{k}=1 / 2$ is constant for all $k$ the methods of Richardson, Jacobi and steepest descent are the same on this simple problem. See the left part of Fig. 13.1. The rate of convergence is determined from $\left\|\boldsymbol{x}_{j+1}\right\|_{2} /\left\|\boldsymbol{x}_{j}\right\|=\left\|\boldsymbol{r}_{j+1}\right\|_{2} /\left\|\boldsymbol{r}_{j}\right\|_{2}=1 / 2$ for all $j$.

### 13.2 The Conjugate Gradient Method

In the steepest descent method the last two gradients are orthogonal. In the conjugate gradient method all gradients are orthogonal. ${ }^{1}$ We achieve this by using $\boldsymbol{A}$-orthogonal search directions i.e., $\boldsymbol{p}_{i}^{T} \boldsymbol{A} \boldsymbol{p}_{j}=0$ for all $i \neq j$.

### 13.2.1 Derivation of the Method

As in the steepest descent method we choose a starting vector $\boldsymbol{x}_{0} \in \mathbb{R}^{n}$. If $\boldsymbol{r}_{0}=$ $\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{0}=\mathbf{0}$ then $\boldsymbol{x}_{0}$ is the exact solution and we are finished, otherwise we initially make a steepest descent step. It follows that $\boldsymbol{r}_{1}^{T} \boldsymbol{r}_{0}=0$ and $\boldsymbol{p}_{0}:=\boldsymbol{r}_{0}$.

For the general case we define for $j \geq 0$

$$
\begin{aligned}
\boldsymbol{p}_{j} & :=\boldsymbol{r}_{j}-\sum_{i=0}^{j-1}\left(\frac{\boldsymbol{r}_{j}^{T} \boldsymbol{A} \boldsymbol{p}_{i}}{\boldsymbol{p}_{i}^{T} \boldsymbol{A} \boldsymbol{p}_{i}}\right) \boldsymbol{p}_{i}, \\
\boldsymbol{x}_{j+1} & :=\boldsymbol{x}_{j}+\alpha_{j} \boldsymbol{p}_{j} \quad \alpha_{j}:=\frac{\boldsymbol{r}_{j}^{T} \boldsymbol{r}_{j}}{\boldsymbol{p}_{j}^{T} \boldsymbol{A} \boldsymbol{p}_{j}}, \\
\boldsymbol{r}_{j+1} & =\boldsymbol{r}_{j}-\alpha_{j} \boldsymbol{A} \boldsymbol{p}_{j} .
\end{aligned}
$$

We note that

1. $\boldsymbol{p}_{j}$ is computed by the Gram-Schmidt orthogonalization process applied to the residuals $\boldsymbol{r}_{0}, \ldots, \boldsymbol{r}_{j}$ using the $\boldsymbol{A}$-inner product. The search directions are therefore $\boldsymbol{A}$-orthogonal and nonzero as long as the residuals are linearly independent.
2. Equation (13.13) follows from (13.10).
3. It can be shown that the step length $\alpha_{j}$ is optimal for all $j$ (cf. Exercise 13.7).
[^23]Lemma 13.2 (The Residuals Are Orthogonal) Suppose that for some $k \geq 0$ that $\boldsymbol{x}_{j}$ is well defined, $\boldsymbol{r}_{j} \neq 0$, and $\boldsymbol{r}_{i}^{T} \boldsymbol{r}_{j}=0$ for $i, j=0,1, \ldots, k, i \neq j$. Then $\boldsymbol{x}_{k+1}$ is well defined and $\boldsymbol{r}_{k+1}^{T} \boldsymbol{r}_{j}=0$ for $j=0,1, \ldots, k$.

Proof Since the residuals $\boldsymbol{r}_{j}$ are orthogonal and nonzero for $j \leq k$, they are linearly independent, and it follows form the Gram-Schmidt Theorem 5.4 that $\boldsymbol{p}_{k}$ is nonzero and $\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{i}=0$ for $i<k$. But then $\boldsymbol{x}_{k+1}$ and $\boldsymbol{r}_{k+1}$ are well defined. Now

$$
\begin{aligned}
\boldsymbol{r}_{k+1}^{T} \boldsymbol{r}_{j} & \stackrel{(13.13)}{=}\left(\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{A} \boldsymbol{p}_{k}\right)^{T} \boldsymbol{r}_{j} \\
& \stackrel{(13.11)}{=} \boldsymbol{r}_{k}^{T} \boldsymbol{r}_{j}-\alpha_{k} \boldsymbol{p}_{k}^{T} \boldsymbol{A}\left(\boldsymbol{p}_{j}+\sum_{i=0}^{j-1}\left(\frac{\boldsymbol{r}_{j}^{T} \boldsymbol{A} \boldsymbol{p}_{i}}{\boldsymbol{p}_{i}^{T} \boldsymbol{A} \boldsymbol{p}_{i}}\right) \boldsymbol{p}_{i}\right) \\
& \stackrel{\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{i}=0}{=} \boldsymbol{r}_{k}^{T} \boldsymbol{r}_{j}-\alpha_{k} \boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{j}=0, \quad j=0,1, \ldots, k .
\end{aligned}
$$

That the final expression is equal to zero follows by orthogonality and $\boldsymbol{A}$ -orthogonality for $j<k$ and by the definition of $\alpha_{k}$ for $j=k$. This completes the proof. $\square$

The conjugate gradient method is also a direct method. The residuals are orthogonal and therefore linearly independent if they are nonzero. Since $\operatorname{dim} \mathbb{R}^{n}=n$ the $n+1$ residuals $\boldsymbol{r}_{0}, \ldots, \boldsymbol{r}_{n}$ cannot all be nonzero and we must have $\boldsymbol{r}_{k}=0$ for some $k \leq n$. Thus we find the exact solution in at most $n$ iterations.

The expression (13.11) for $\boldsymbol{p}_{k}$ can be greatly simplified. All terms except the last one vanish, since by orthogonality of the residuals

$$
\boldsymbol{r}_{j}^{T} \boldsymbol{A} \boldsymbol{p}_{i} \stackrel{(13.13)}{=} \boldsymbol{r}_{j}^{T}\left(\frac{\boldsymbol{r}_{i}-\boldsymbol{r}_{i+1}}{\alpha_{i}}\right)=0, \quad i=0,1, \ldots, j-2 .
$$

With $j=k+1$ (13.11) therefore takes the simple form $\boldsymbol{p}_{k+1}=\boldsymbol{r}_{k+1}+\beta_{k} \boldsymbol{p}_{k}$ and we find

$$
\beta_{k}:=-\frac{\boldsymbol{r}_{k+1}^{T} \boldsymbol{A} \boldsymbol{p}_{k}}{\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k}} \stackrel{\text { (13.13) }}{=} \frac{\boldsymbol{r}_{k+1}^{T}\left(\boldsymbol{r}_{k+1}-\boldsymbol{r}_{k}\right)}{\alpha_{k} \boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k}} \stackrel{\text { (13.12) }}{=} \frac{\boldsymbol{r}_{k+1}^{T} \boldsymbol{r}_{k+1}}{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}} .
$$

To summarize, in the conjugate gradient method we start with $\boldsymbol{x}_{0}, \boldsymbol{p}_{0}=\boldsymbol{r}_{0}=$ $\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{0}$ and then generate a sequence of vectors $\left\{\boldsymbol{x}_{k}\right\}$ as follows:

$$
\begin{aligned}
& \text { For } k=0,1,2, \ldots \\
& \qquad \boldsymbol{x}_{k+1}:=\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}, \quad \alpha_{k}:=\frac{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k}}, \\
& \boldsymbol{r}_{k+1}:=\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{A} \boldsymbol{p}_{k},
\end{aligned}
$$

$$
\boldsymbol{p}_{k+1}:=\boldsymbol{r}_{k+1}+\beta_{k} \boldsymbol{p}_{k}, \quad \beta_{k}:=\frac{\boldsymbol{r}_{k+1}^{T} \boldsymbol{r}_{k+1}}{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}} .
$$

The residuals and search directions are orthogonal and $\boldsymbol{A}$-orthogonal, respectively.
For computation we organize the iterations as follows for $k=0,1,2, \ldots$

$$
\begin{aligned}
\boldsymbol{t}_{k} & =\boldsymbol{A} \boldsymbol{p}_{k}, \\
\alpha_{k} & =\left(\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}\right) /\left(\boldsymbol{p}_{k}^{T} \boldsymbol{t}_{k}\right), \\
\boldsymbol{x}_{k+1} & =\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}, \\
\boldsymbol{r}_{k+1} & =\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{t}_{k}, \\
\beta_{k} & =\left(\boldsymbol{r}_{k+1}^{T} \boldsymbol{r}_{k+1}\right) /\left(\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}\right), \\
\boldsymbol{p}_{k+1} & :=\boldsymbol{r}_{k+1}+\beta_{k} \boldsymbol{p}_{k} .
\end{aligned}
$$

Note that (13.18) differs from (13.9) only in the computation of the search direction.
Example 13.2 (Conjugate Gradient Iteration) Consider (13.18) applied to the positive definite linear system $\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]\left[\begin{array}{l}x_{1} \\ x_{2}\end{array}\right]=\left[\begin{array}{l}0 \\ 0\end{array}\right]$. Starting as in Example 13.1 with $\boldsymbol{x}_{0}=\left[\begin{array}{c}-1 \\ -1 / 2\end{array}\right]$ we find $\boldsymbol{p}_{0}=\boldsymbol{r}_{0}=\left[\begin{array}{c}3 / 2 \\ 0\end{array}\right]$ and then

$$
\begin{array}{ll}
\boldsymbol{t}_{0}=\left[\begin{array}{c}
3 \\
-3 / 2
\end{array}\right], \quad \alpha_{0}=1 / 2, \quad \boldsymbol{x}_{1}=\left[\begin{array}{l}
-1 / 4 \\
-1 / 2
\end{array}\right], \quad \boldsymbol{r}_{1}=\left[\begin{array}{c}
0 \\
3 / 4
\end{array}\right], \quad \beta_{0}=1 / 4, \\
\boldsymbol{p}_{1}=\left[\begin{array}{l}
3 / 8 \\
3 / 4
\end{array}\right], \quad \boldsymbol{t}_{1}=\left[\begin{array}{c}
0 \\
9 / 8
\end{array}\right], \quad \alpha_{1}=2 / 3, \quad \boldsymbol{x}_{2}=\mathbf{0}, \quad \boldsymbol{r}_{2}=\mathbf{0} .
\end{array}
$$

Thus $\boldsymbol{x}_{2}$ is the exact solution as illustrated in the right part of Fig. 13.1.

### 13.2.2 The Conjugate Gradient Algorithm

In this section we give numerical examples and discuss implementation.
The formulas in (13.18) form a basis for the following algorithm, which solves the positive definite linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ by the conjugate gradient method. $\boldsymbol{x}$ is a starting vector for the iteration. The iteration is stopped when $\left\|\boldsymbol{r}_{k}\right\|_{2} /\|\boldsymbol{b}\|_{2} \leq$ tol or
$k>$ itmax. $K$ is the number of iterations used:

```
function [x,K]=cg(A,b,x,tol,itmax)
% [x,K]=cg(A,b,x,tol,itmax)
r=b-A*x; p=r; rho0=b'*b; rho=r'*r;
for k=0:itmax
    if sqrt(rho/rho0)<= tol
        K=k; return
    end
    t=A*p; a=rho/(p’*t);
    x=x+a*p; r=r-a*t;
    rhos=rho; rho=r'*r;
    p=r+(rho/rhos)*p;
end
K=itmax+1;
end
```

Listing 13.1 cg

The work involved in each iteration is

1. one matrix times vector $(\boldsymbol{t}=\boldsymbol{A} \boldsymbol{p})$,
2. two inner products ( $\left(\boldsymbol{p}^{T} \boldsymbol{t}\right.$ and $\left.\boldsymbol{r}^{T} \boldsymbol{r}\right)$,
3. three vector-plus-scalar-times-vector ( $\boldsymbol{x}=\boldsymbol{x}+a \boldsymbol{p}, \boldsymbol{r}=\boldsymbol{r}-a \boldsymbol{t}$ and $\boldsymbol{p}=\boldsymbol{r}+$ (rho/rhos) p),

The dominating part is the computation of $\boldsymbol{t}=\boldsymbol{A} \boldsymbol{p}$.

### 13.2.3 Numerical Example

We test the conjugate gradient method on two examples. For a similar test for the steepest descent method see Exercise 13.9. Consider the matrix given by the Kronecker sum $\boldsymbol{T}_{2}:=\boldsymbol{T}_{1} \otimes \boldsymbol{I}+\boldsymbol{I} \otimes \boldsymbol{T}_{1}$, where $\boldsymbol{T}_{1}:=\operatorname{tridiag}_{m}(a, d, a) \in \mathbb{R}^{m \times m}$ and $a, d \in \mathbb{R}$. We recall that this matrix is positive definite if $d>0$ and $d \geq 2|a|$ (cf. Theorem 10.2). We set $h=1 /(m+1)$ and $\boldsymbol{f}=[1, \ldots, 1]^{T} \in \mathbb{R}^{n}$.

We consider two problems.

1. $a=1 / 9, d=5 / 18$, the Averaging matrix.
2. $a=-1, d=2$, the Poisson matrix.

### 13.2.4 Implementation Issues

Note that for our test problems $\boldsymbol{T}_{2}$ only has $O(5 n)$ nonzero elements. Therefore, taking advantage of the sparseness of $\boldsymbol{T}_{2}$ we can compute $\boldsymbol{t}$ in Algorithm 13.1
in $O(n)$ arithmetic operations. With such an implementation the total number of arithmetic operations in one iteration is $O(n)$. We also note that it is not necessary to store the matrix $\boldsymbol{T}_{2}$.

To use the conjugate gradient algorithm on the test matrix for large $n$ it is advantageous to use a matrix equation formulation. We define matrices $\boldsymbol{V}, \boldsymbol{R}, \boldsymbol{P}, \boldsymbol{B}, \boldsymbol{T} \in$ $\mathbb{R}^{m \times m}$ by $\boldsymbol{x}=\operatorname{vec}(\boldsymbol{V}), \boldsymbol{r}=\operatorname{vec}(\boldsymbol{R}), \boldsymbol{p}=\operatorname{vec}(\boldsymbol{P}), \boldsymbol{t}=\operatorname{vec}(\boldsymbol{T})$, and $h^{2} \boldsymbol{f}=\operatorname{vec}(\boldsymbol{B})$. Then $\boldsymbol{T}_{2} \boldsymbol{x}=h^{2} \boldsymbol{f} \Longleftrightarrow \boldsymbol{T}_{1} \boldsymbol{V}+\boldsymbol{V} \boldsymbol{T}_{1}=\boldsymbol{B}$, and $\boldsymbol{t}=\boldsymbol{T}_{2} \boldsymbol{p} \Longleftrightarrow \boldsymbol{T}=\boldsymbol{T}_{1} \boldsymbol{P}+\boldsymbol{P} \boldsymbol{T}_{1}$.

This leads to the following algorithm for testing the conjugate gradient algorithm on the matrix

$$
\boldsymbol{A}=\operatorname{tridiag}_{m}(a, d, a) \otimes \boldsymbol{I}_{m}+\boldsymbol{I}_{m} \otimes \operatorname{tridiag}_{m}(a, d, a) \in \mathbb{R}^{\left(m^{2}\right) \times\left(m^{2}\right)}
$$

```
function [V,K]=cgtest(m,a,d,tol,itmax)
% [V,K]=cgtest(m,a,d,tol,itmax)
R=ones (m) / (m+1) ^2; rho=sum(sum(R.*R)) ; rho0=rho; P=R;
V=zeros(m,m); Tl=sparse(tridiagonal(a,d,a,m));
for k=1:itmax
    if sqrt(rho/rho0)<= tol
        K=k; return
    end
    T=T1*P+P*T1;
    a=rho/sum(sum(P.*T)); V=V+a*P; R=R-a*T;
    rhos=rho; rho=sum(sum(R.*R)); P=R+(rho/rhos)*P;
end
K=itmax+1;
end
```

For both the averaging- and Poison matrix we use $t o l=10^{-8}$.
For the averaging matrix we obtain the values in Table 13.1.
The convergence is quite rapid. It appears that the number of iterations can be bounded independently of $n$, and therefore we solve the problem in $O(n)$ operations. This is the best we can do for a problem with $n$ unknowns.

Consider next the Poisson problem. In Table 13.2 we list $K$, the required number of iterations, and $K / \sqrt{n}$.

Listing 13.2 cgtest
| $n$ | 2500 | 10000 | 40000 | 1000000 | 4000000 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $K$ | 19 | 18 | 18 | 16 | 15 |


Table 13.2 The number of iterations $K$ for the Poisson problem on a $\sqrt{n} \times \sqrt{n}$ grid for various $n$

Table 13.1 The number of iterations $K$ for the averaging problem on a $\sqrt{n} \times \sqrt{n}$ grid for various $n$
| $n$ | 2500 | 10000 | 40000 | 160000 |
| :--- | :--- | :--- | :--- | :--- |
| $K$ | 94 | 188 | 370 | 735 |
| $K / \sqrt{n}$ | 1.88 | 1.88 | 1.85 | 1.84 |


The results show that $K$ is much smaller than $n$ and appears to be proportional to $\sqrt{n}$. This is the same speed as for SOR and we don't have to estimate any acceleration parameter.

### 13.3 Convergence

### 13.3.1 The Main Theorem

Recall that the $\boldsymbol{A}$-norm of a vector $\boldsymbol{x} \in \mathbb{R}^{n}$ is given by $\|\boldsymbol{x}\|_{\boldsymbol{A}}:=\sqrt{\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x}}$. The following theorem gives upper bounds for the $\boldsymbol{A}$-norm of the error in both steepest descent and conjugate gradients.

Theorem 13.3 (Error Bound for Steepest Descent and Conjugate Gradients) Suppose $\boldsymbol{A}$ is positive definite. For the $\boldsymbol{A}$-norms of the errors in the steepest descent method (13.8) the following upper bounds hold

$$
\frac{\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}}{\left\|\boldsymbol{x}-\boldsymbol{x}_{0}\right\|_{\boldsymbol{A}}} \leq\left(\frac{\kappa-1}{\kappa+1}\right)^{k}<e^{-\frac{2}{\kappa} k}, \quad, k>0,
$$

while for the conjugate gradient method we have

$$
\frac{\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}}{\left\|\boldsymbol{x}-\boldsymbol{x}_{0}\right\|_{\boldsymbol{A}}} \leq 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^{k}<2 e^{-\frac{2}{\sqrt{\kappa}} k}, \quad k \geq 0 .
$$

Here $\kappa=\operatorname{cond}_{2}(\boldsymbol{A}):=\lambda_{\text {max }} / \lambda_{\text {min }}$ is the spectral condition number of $\boldsymbol{A}$, where $\lambda_{\text {max }}$ and $\lambda_{\text {min }}$ are the largest and smallest eigenvalue of $\boldsymbol{A}$, respectively.

Theorem 13.3 implies

1. Since $\frac{\kappa-1}{\kappa+1}<1$ the steepest descent method always converges for a positive definite matrix. The convergence can be slow when $\frac{\kappa-1}{\kappa+1}$ is close to one, and this happens even for a moderately ill-conditioned $\boldsymbol{A}$.
2. The rate of convergence for the conjugate gradient method appears to be determined by the square root of the spectral condition number. This is much better than the estimate for the steepest descent method. Especially for problems with large condition numbers.
3. The proofs of the estimates in (13.19) and (13.20) are quite different. This is in spite of their similar appearance.

### 13.3.2 The Number of Iterations for the Model Problems

Consider the test matrix

$$
\boldsymbol{T}_{2}:=\operatorname{tridiag}_{m}(a, d, a) \otimes \boldsymbol{I}_{m}+\boldsymbol{I}_{m} \otimes \operatorname{tridiag}_{m}(a, d, a) \in \mathbb{R}^{\left(m^{2}\right) \times\left(m^{2}\right)} .
$$

The eigenvalues were given in (10.15) as

$$
\lambda_{j, k}=2 d+2 a \cos (j \pi h)+2 a \cos (k \pi h), \quad j, k=1, \ldots, m .
$$

For the averaging problem given by $d=5 / 18, a=1 / 9$, the largest and smallest eigenvalue of $\boldsymbol{T}_{2}$ are given by $\lambda_{\text {max }}=\frac{5}{9}+\frac{4}{9} \cos (\pi h)$ and $\lambda_{\text {min }}=\frac{5}{9}-\frac{4}{9} \cos (\pi h)$. Thus

$$
\kappa_{A}=\frac{5+4 \cos (\pi h)}{5-4 \cos (\pi h)} \leq 9,
$$

and the condition number is bounded independently of $n$. It follows from (13.20) that the number of iterations can be bounded independently of the size $n$ of the problem, and this is in agreement with what we observed in Table 13.1.

For the Poisson problem we have by (10.20) the condition number

$$
\kappa_{P}=\frac{\lambda_{\max }}{\lambda_{\min }}=\frac{\cos ^{2}(\pi h / 2)}{\sin ^{2}(\pi h / 2)} \text { and } \sqrt{\kappa_{P}}=\frac{\cos (\pi h / 2)}{\sin (\pi h / 2)} \approx \frac{2}{\pi h} \approx \frac{2}{\pi} \sqrt{n} \text {. }
$$

Thus, (see also Exercise 8.19) we solve the discrete Poisson problem in $O\left(n^{3 / 2}\right)$ arithmetic operations using the conjugate gradient method. This is the same as for the SOR method and for the fast method without the FFT. In comparison the Cholesky Algorithm requires $O\left(n^{2}\right)$ arithmetic operations both for the averaging and the Poisson problem.

### 13.3.3 Krylov Spaces and the Best Approximation Property

For the convergence analysis of the conjugate gradient method certain subspaces of $\mathbb{R}^{n}$ called Krylov spaces play a central role. In fact the iterates in the conjugate gradient method are best approximation of the solution from these subspaces using the $\boldsymbol{A}$-norm to measure the error.

The Krylov spaces are defined by $\mathbb{W}_{0}=\{\mathbf{0}\}$ and

$$
\mathbb{W}_{k}=\operatorname{span}\left(\boldsymbol{r}_{0}, \boldsymbol{A} \boldsymbol{r}_{0}, \boldsymbol{A}^{2} \boldsymbol{r}_{0}, \ldots, \boldsymbol{A}^{k-1} \boldsymbol{r}_{0}\right), \quad k=1,2,3, \cdots .
$$

They are nested subspaces

$$
\mathbb{W}_{0} \subset \mathbb{W}_{1} \subset \mathbb{W}_{2} \subset \cdots \subset \mathbb{W}_{n} \subset \mathbb{R}^{n}
$$

with $\operatorname{dim}\left(\mathbb{W}_{k}\right) \leq k$ for all $k \geq 0$. Moreover, If $\boldsymbol{v} \in \mathbb{W}_{k}$ then $\boldsymbol{A} \boldsymbol{v} \in \mathbb{W}_{k+1}$.
Lemma 13.3 (Krylov Space) For the iterates in the conjugate gradient method we have

$$
\boldsymbol{x}_{k}-\boldsymbol{x}_{0} \in \mathbb{W}_{k}, \quad \boldsymbol{r}_{k}, \boldsymbol{p}_{k} \in \mathbb{W}_{k+1}, \quad k=0,1, \ldots,
$$

and

$$
\boldsymbol{r}_{k}^{T} \boldsymbol{w}=\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{w}=0, \quad \boldsymbol{w} \in \mathbb{W}_{k} .
$$

Proof Equation (13.22) clearly holds for $k=0$ since $\boldsymbol{p}_{0}=\boldsymbol{r}_{0}$. Suppose it holds for some $k \geq 0$. Then $\boldsymbol{r}_{k+1}=\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{A} \boldsymbol{p}_{k} \in \mathbb{W}_{k+2}, \boldsymbol{p}_{k+1}=\boldsymbol{r}_{k+1}+\beta_{k} \boldsymbol{p}_{k} \in$ $\mathbb{W}_{k+2}$ and $\boldsymbol{x}_{k+1}-\boldsymbol{x}_{0} \stackrel{\text { (13.12) }}{=} \boldsymbol{x}_{k}-\boldsymbol{x}_{0}+\alpha_{k} \boldsymbol{p}_{k} \in \mathbb{W}_{k+1}$. Thus (13.22) follows by induction. The equation (13.23) follows since any $\boldsymbol{w} \in \mathbb{W}_{k}$ is a linear combination of $\left\{\boldsymbol{r}_{0}, \boldsymbol{r}_{1}, \ldots, \boldsymbol{r}_{k-1}\right\}$ and also $\left\{\boldsymbol{p}_{0}, \boldsymbol{p}_{1}, \ldots, \boldsymbol{p}_{k-1}\right\}$. $\square$

Theorem 13.4 (Best Approximation Property) Suppose $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$ is positive definite and $\left\{\boldsymbol{x}_{k}\right\}$ is generated by the conjugate gradient method (cf. (13.15)). Then

$$
\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}=\min _{\boldsymbol{w} \in \mathbb{W}_{k}}\left\|\boldsymbol{x}-\boldsymbol{x}_{0}-\boldsymbol{w}\right\|_{\boldsymbol{A}} .
$$

Proof Fix $k$, let $\boldsymbol{w} \in \mathbb{W}_{k}$ and $\boldsymbol{u}:=\boldsymbol{x}_{k}-\boldsymbol{x}_{0}-\boldsymbol{w}$. By (13.22) $\boldsymbol{u} \in \mathbb{W}_{k}$ and then (13.23) implies that $\left\langle\boldsymbol{x}-\boldsymbol{x}_{k}, \boldsymbol{u}\right\rangle=\boldsymbol{r}_{k}^{T} \boldsymbol{u}=0$. Using Corollary 5.2 we obtain

$$
\left\|\boldsymbol{x}-\boldsymbol{x}_{0}-\boldsymbol{w}\right\|_{\boldsymbol{A}}=\left\|\boldsymbol{x}-\boldsymbol{x}_{k}+\boldsymbol{u}\right\|_{\boldsymbol{A}} \geq\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}},
$$

with equality for $\boldsymbol{u}=\mathbf{0}$. $\square$

If $\boldsymbol{x}_{0}=\mathbf{0}$ then (13.24) says that $\boldsymbol{x}_{k}$ is the element in $\mathbb{W}_{k}$ that is closest to the solution $\boldsymbol{x}$ in the $\boldsymbol{A}$-norm. More generally, if $\boldsymbol{x}_{0} \neq \mathbf{0}$ then $\boldsymbol{x}-\boldsymbol{x}_{k}=\left(\boldsymbol{x}-\boldsymbol{x}_{0}\right)-$ $\left(\boldsymbol{x}_{k}-\boldsymbol{x}_{0}\right)$ and $\boldsymbol{x}_{k}-\boldsymbol{x}_{0}$ is the element in $\mathbb{W}_{k}$ that is closest to $\boldsymbol{x}-\boldsymbol{x}_{0}$ in the $\boldsymbol{A}$-norm. This is the orthogonal projection of $\boldsymbol{x}-\boldsymbol{x}_{0}$ into $\mathbb{W}_{k}$, see Fig. 13.2.

Recall that to each polynomial $p(t):=\sum_{j=0}^{m} a_{j} t^{m}$ there corresponds a matrix polynomial $p(\boldsymbol{A}):=a_{0} \boldsymbol{I}+a_{1} \boldsymbol{A}+\cdots+a_{m} \boldsymbol{A}^{m}$. Moreover, if $\left(\lambda_{j}, \boldsymbol{u}_{j}\right)$ are eigenpairs of $\boldsymbol{A}$ then $\left(p\left(\lambda_{j}\right), \boldsymbol{u}_{j}\right)$ are eigenpairs of $p(\boldsymbol{A})$ for $j=1, \ldots, n$.

Lemma 13.4 (Krylov Space and Polynomials) Suppose $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ where $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$ is positive definite with orthonormal eigenpairs $\left(\lambda_{j}, \boldsymbol{u}_{j}\right), j=1,2, \ldots, n$, and let $\boldsymbol{r}_{0}:=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{0}$ for some $\boldsymbol{x}_{0} \in \mathbb{R}^{n}$. To each $\boldsymbol{w} \in \mathbb{W}_{k}$ there corresponds

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-302.jpg?height=596&width=847&top_left_y=211&top_left_x=339)
Fig. 13.2 The orthogonal projection of $\boldsymbol{x}-\boldsymbol{x}_{0}$ into $\mathbb{W}_{k}$

a polynomial $P(t):=\sum_{j=0}^{k-1} a_{j} t^{k-1}$ such that $\boldsymbol{w}=P(\boldsymbol{A}) \boldsymbol{r}_{0}$. Moreover, if $\boldsymbol{r}_{0}=$ $\sum_{j=1}^{n} \sigma_{j} \boldsymbol{u}_{j}$ then

$$
\left\|\boldsymbol{x}-\boldsymbol{x}_{0}-\boldsymbol{w}\right\|_{\boldsymbol{A}}^{2}=\sum_{j=1}^{n} \frac{\sigma_{j}^{2}}{\lambda_{j}} Q\left(\lambda_{j}\right)^{2}, \quad Q(t):=1-t P(t) .
$$

Proof If $\boldsymbol{w} \in \mathbb{W}_{k}$ then $\boldsymbol{w}=a_{0} \boldsymbol{r}_{0}+a_{1} \boldsymbol{A} \boldsymbol{r}_{0}+\cdots+a_{k-1} \boldsymbol{A}^{k-1} \boldsymbol{r}_{0}$ for some scalars $a_{0}, \ldots, a_{k-1}$. But then $\boldsymbol{w}=P(\boldsymbol{A}) \boldsymbol{r}_{0}$. We find $\boldsymbol{x}-\boldsymbol{x}_{0}-P(\boldsymbol{A}) \boldsymbol{r}_{0}=\boldsymbol{A}^{-1}\left(\boldsymbol{r}_{0}-\right.$ $\boldsymbol{A} P(\boldsymbol{A})) \boldsymbol{r}_{0}=\boldsymbol{A}^{-1} Q(\boldsymbol{A}) \boldsymbol{r}_{0}$ and $\boldsymbol{A}\left(\boldsymbol{x}-\boldsymbol{x}_{0}-P(\boldsymbol{A}) \boldsymbol{r}_{0}\right)=Q(\boldsymbol{A}) \boldsymbol{r}_{0}$. Therefore,

$$
\left\|\boldsymbol{x}-\boldsymbol{x}_{0}-P(\boldsymbol{A}) \boldsymbol{r}_{0}\right\|_{\boldsymbol{A}}^{2}=\boldsymbol{c}^{T} \boldsymbol{A}^{-1} \boldsymbol{c} \text { where } \boldsymbol{c}=(\boldsymbol{I}-\boldsymbol{A} P(\boldsymbol{A})) \boldsymbol{r}_{0}=Q(\boldsymbol{A}) \boldsymbol{r}_{0} .
$$

Using the eigenvector expansion for $\boldsymbol{r}_{0}$ we obtain

$$
\boldsymbol{c}=\sum_{j=1}^{n} \sigma_{j} Q\left(\lambda_{j}\right) \boldsymbol{u}_{j}, \quad \boldsymbol{A}^{-1} \boldsymbol{c}=\sum_{i=1}^{n} \sigma_{i} \frac{Q\left(\lambda_{i}\right)}{\lambda_{i}} \boldsymbol{u}_{i} .
$$

Now (13.25) follows by the orthonormality of the eigenvectors. $\square$

We will use the following theorem to estimate the rate of convergence.

Theorem 13.5 (cg and Best Polynomial Approximation) Suppose $[a, b]$ with $0<a<b$ is an interval containing all the eigenvalues of $A$. Then in the conjugate gradient method

$$
\frac{\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}}{\left\|\boldsymbol{x}-\boldsymbol{x}_{0}\right\|_{\boldsymbol{A}}} \leq \min _{\substack{Q \in \Pi_{k} \\ Q(0)=1}} \max _{a \leq x \leq b}|Q(x)|,
$$

where $\Pi_{k}$ denotes the class of univariate polynomials of degree $\leq k$ with real coefficients.

Proof By (13.25) with $Q(t)=1$ (corresponding to $P(\boldsymbol{A})=\mathbf{0}$ ) we find $\| \boldsymbol{x}-$ $\boldsymbol{x}_{0} \|_{\boldsymbol{A}}^{2}=\sum_{j=1}^{n} \frac{\sigma_{j}^{2}}{\lambda_{j}}$. Therefore, by the best approximation property Theorem 13.4 and (13.25), for any $\boldsymbol{w} \in \mathbb{W}_{k}$

$$
\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}^{2} \leq\left\|\boldsymbol{x}-\boldsymbol{x}_{0}-\boldsymbol{w}\right\|_{\boldsymbol{A}}^{2} \leq \max _{a \leq x \leq b}|Q(x)|^{2} \sum_{j=1}^{n} \frac{\sigma_{j}^{2}}{\lambda_{j}}=\max _{a \leq x \leq b}|Q(x)|^{2}\left\|\boldsymbol{x}-\boldsymbol{x}_{0}\right\|_{\boldsymbol{A}}^{2},
$$

where $Q \in \Pi_{k}$ and $Q(0)=1$. Minimizing over such polynomials $Q$ and taking square roots the result follows. $\square$

In the next section we use properties of the Chebyshev polynomials to show that

$$
\frac{\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}}{\left\|\boldsymbol{x}-\boldsymbol{x}_{0}\right\|_{\boldsymbol{A}}} \leq \min _{\substack{Q \in \Pi_{k} \\ Q(0)=1}} \max _{\lambda_{\min } \leq x \leq \lambda_{\max }}|Q(x)|=\frac{2}{a^{-k}+a^{k}}, \quad a:=\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1},
$$

where $\kappa=\lambda_{\text {max }} / \lambda_{\text {min }}$ is the spectral condition number of $\boldsymbol{A}$. Ignoring the second term in the denominator this implies the first inequality in (13.20).

Consider the second inequality in (13.20). The inequality

$$
\frac{x-1}{x+1}<e^{-2 / x} \quad \text { for } \quad x>1
$$

follows from the familiar series expansion of the exponential function. Indeed, with $y=1 / x$, using $2^{k} / k!=2, k=1,2$, and $2^{k} / k!<2$ for $k>2$, we find

$$
e^{2 / x}=e^{2 y}=\sum_{k=0}^{\infty} \frac{(2 y)^{k}}{k!}<-1+2 \sum_{k=0}^{\infty} y^{k}=\frac{1+y}{1-y}=\frac{x+1}{x-1}
$$

and (13.30) follows.

### 13.4 Proof of the Convergence Estimates

### 13.4.1 Chebyshev Polynomials

The proof of the estimate (13.29) for the error in the conjugate gradient method is based on an extremal property of the Chebyshev polynomials. Suppose $a<b$, $c \notin[a, b]$ and $k \in \mathbb{N}$. Consider the set $\mathcal{S}_{k}$ of all polynomials $Q$ of degree $\leq k$ such that $Q(c)=1$. For any continuous function $f$ on $[a, b]$ we define

$$
\|f\|_{\infty}=\max _{a \leq x \leq b}|f(x)| .
$$

We want to find a polynomial $Q^{*} \in \mathcal{S}_{k}$ such that

$$
\left\|Q^{*}\right\|_{\infty}=\min _{Q \in \mathcal{S}_{k}}\|Q\|_{\infty} .
$$

We will show that $Q^{*}$ is uniquely given as a suitably shifted and normalized version of the Chebyshev polynomial. The Chebyshev polynomial $T_{n}$ of degree $n$ can be defined recursively by

$$
T_{n+1}(t)=2 t T_{n}(t)-T_{n-1}(t), \quad n \geq 1, \quad t \in \mathbb{R},
$$

starting with $T_{0}(t)=1$ and $T_{1}(t)=t$. Thus $T_{2}(t)=2 t^{2}-1, T_{3}(t)=4 t^{3}-3 t$ etc. In general $T_{n}$ is a polynomial of degree $n$.

There are some convenient closed form expressions for $T_{n}$.
Lemma 13.5 (Closed Forms of Chebyshev Polynomials) For $n \geq 0$

1. $T_{n}(t)=\cos (n \arccos t)$ for $t \in[-1,1]$,
2. $T_{n}(t)=\frac{1}{2}\left[\left(t+\sqrt{t^{2}-1}\right)^{n}+\left(t+\sqrt{t^{2}-1}\right)^{-n}\right]$ for $|t| \geq 1$.

Proof

1. With $P_{n}(t)=\cos (n \arccos t)$ we have $P_{n}(t)=\cos n \phi$, where $t=\cos \phi$. Therefore,
$$
P_{n+1}(t)+P_{n-1}(t)=\cos (n+1) \phi+\cos (n-1) \phi=2 \cos \phi \cos n \phi=2 t P_{n}(t),
$$
and it follows that $P_{n}$ satisfies the same recurrence relation as $T_{n}$. Since $P_{0}=T_{0}$ and $P_{1}=T_{1}$ we have $P_{n}=T_{n}$ for all $n \geq 0$.
2. Fix $t$ with $|t| \geq 1$ and let $x_{n}:=T_{n}(t)$ for $n \geq 0$. The recurrence relation for the Chebyshev polynomials can then be written
$$
x_{n+1}-2 t x_{n}+x_{n-1}=0 \text { for } n \geq 1, \text { with } x_{0}=1, x_{1}=t .
$$

To solve this difference equation we insert $x_{n}=z^{n}$ into (13.31) and obtain $z^{n+1}-$ $2 t z^{n}+z^{n-1}=0$ or $z^{2}-2 t z+1=0$. The roots of this equation are

$$
z_{1}=t+\sqrt{t^{2}-1}, \quad z_{2}=t-\sqrt{t^{2}-1}=\left(t+\sqrt{t^{2}-1}\right)^{-1} .
$$

Now $z_{1}^{n}, z_{2}^{n}$ and more generally $c_{1} z_{1}^{n}+c_{2} z_{2}^{n}$ are solutions of (13.31) for any constants $c_{1}$ and $c_{2}$. We find these constants from the initial conditions $x_{0}=$ $c_{1}+c_{2}=1$ and $x_{1}=c_{1} z_{1}+c_{2} z_{2}=t$. Since $z_{1}+z_{2}=2 t$ the solution is $c_{1}=c_{2}=\frac{1}{2}$. $\square$

We show that the unique solution to our minimization problem is

$$
Q^{*}(x)=\frac{T_{k}(u(x))}{T_{k}(u(c))}, \quad u(x)=\frac{b+a-2 x}{b-a} .
$$

Clearly $Q^{*} \in \mathcal{S}_{k}$.
Theorem 13.6 (A Minimal Norm Problem) Suppose $a<b, c \notin[a, b]$ and $k \in$ $\mathbb{N}$. If $Q \in \mathcal{S}_{k}$ and $Q \neq Q^{*}$ then $\|Q\|_{\infty}>\left\|Q^{*}\right\|_{\infty}$.

Proof Recall that a nonzero polynomial $p$ of degree $k$ can have at most $k$ zeros. If $p(z)=p^{\prime}(z)=0$, we say that $p$ has a double zero at $z$. Counting such a zero as two zeros it is still true that a nonzero polynomial of degree $k$ has at most $k$ zeros.
$\left|Q^{*}\right|$ takes on its maximum $1 /\left|T_{k}(u(c))\right|$ at the $k+1$ points $\mu_{0}, \ldots, \mu_{k}$ in $[a, b]$ such that $u\left(\mu_{i}\right)=\cos (i \pi / k)$ for $i=0,1, \ldots, k$. Suppose $Q \in S_{k}$ and that $\|Q\|_{\infty} \leq\left\|Q^{*}\right\|_{\infty}$. We have to show that $Q \equiv Q^{*}$. Let $f \equiv Q-Q^{*}$. We show that $f$ has at least $k$ zeros in $[a, b]$. Since $f$ is a polynomial of degree $\leq k$ and $f(c)=0$, this means that $f \equiv 0$ or equivalently $Q \equiv Q^{*}$.

Consider $I_{j}=\left[\mu_{j-1}, \mu_{j}\right]$ for a fixed $j$. Let

$$
\sigma_{j}=f\left(\mu_{j-1}\right) f\left(\mu_{j}\right) .
$$

We have $\sigma_{j} \leq 0$. For if say $Q^{*}\left(\mu_{j}\right)>0$ then

$$
Q\left(\mu_{j}\right) \leq\|Q\|_{\infty} \leq\left\|Q^{*}\right\|_{\infty}=Q^{*}\left(\mu_{j}\right)
$$

so that $f\left(\mu_{j}\right) \leq 0$. Moreover,

$$
-Q\left(\mu_{j-1}\right) \leq\|Q\|_{\infty} \leq\left\|Q^{*}\right\|_{\infty}=-Q^{*}\left(\mu_{j-1}\right) .
$$

Thus $f\left(\mu_{j-1}\right) \geq 0$ and it follows that $\sigma_{j} \leq 0$. Similarly, $\sigma_{j} \leq 0$ if $Q^{*}\left(\mu_{j}\right)<0$.
If $\sigma_{j}<0, f$ must have a zero in $I_{j}$ since it is continuous. Suppose $\sigma_{j}=0$. Then $f\left(\mu_{j-1}\right)=0$ or $f\left(\mu_{j}\right)=0$. If $f\left(\mu_{j}\right)=0$ then $Q\left(\mu_{j}\right)=Q^{*}\left(\mu_{j}\right)$. But then $\mu_{j}$ is a maximum or minimum both for $Q$ and $Q^{*}$. If $\mu_{j} \in(a, b)$ then $Q^{\prime}\left(\mu_{j}\right)=$
$Q^{* \prime}\left(\mu_{j}\right)=0$. Thus $f\left(\mu_{j}\right)=f^{\prime}\left(\mu_{j}\right)=0$, and $f$ has a double zero at $\mu_{j}$. We can count this as one zero for $I_{j}$ and one for $I_{j+1}$. If $\mu_{j}=b$, we still have a zero in $I_{j}$. Similarly, if $f\left(\mu_{j-1}\right)=0$, a double zero of $f$ at $\mu_{j-1}$ appears if $\mu_{j-1} \in(a, b)$. We count this as one zero for $I_{j-1}$ and one for $I_{j}$.

In this way we associate one zero of $f$ for each of the $k$ intervals $I_{j}, j=$ $1,2, \ldots, k$. We conclude that $f$ has at least $k$ zeros in $[a, b]$. $\square$

Theorem 13.6 with $a$, and $b$, the smallest and largest eigenvalue of $\boldsymbol{A}$, and $c=0$ implies that the minimizing polynomial in (13.29) is given by

$$
Q^{*}(x)=T_{k}\left(\frac{b+a-2 x}{b-a}\right) / T_{k}\left(\frac{b+a}{b-a}\right) .
$$

By Lemma 13.5

$$
\max _{a \leq x \leq b}\left|T_{k}\left(\frac{b+a-2 x}{b-a}\right)\right|=\max _{-1 \leq t \leq 1}\left|T_{k}(t)\right|=1 .
$$

Moreover with $t=(b+a) /(b-a)$ we have

$$
t+\sqrt{t^{2}-1}=\frac{\sqrt{\kappa}+1}{\sqrt{\kappa}-1}, \quad \kappa=b / a .
$$

Thus again by Lemma 13.5 we find

$$
T_{k}\left(\frac{b+a}{b-a}\right)=T_{k}\left(\frac{\kappa+1}{\kappa-1}\right)=\frac{1}{2}\left[\left(\frac{\sqrt{\kappa}+1}{\sqrt{\kappa}-1}\right)^{k}+\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^{k}\right]
$$

and (13.29) follows (Fig. 13.3).

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-306.jpg?height=527&width=1156&top_left_y=1449&top_left_x=185)
Fig. 13.3 This is an illustration of the proof of Theorem 13.6 for $k=3 . f \equiv Q-Q^{*}$ has a double zero at $\mu_{1}$ and one zero between $\mu_{2}$ and $\mu_{3}$

### 13.4.2 Convergence Proof for Steepest Descent

For the proof of (13.19) the following inequality will be used.
Theorem 13.7 (Kantorovich Inequality) For any positive definite matrix $\boldsymbol{A} \in$ $\mathbb{R}^{n \times n}$

$$
1 \leq \frac{\left(\boldsymbol{y}^{T} \boldsymbol{A y}\right)\left(\boldsymbol{y}^{T} \boldsymbol{A}^{-1} \boldsymbol{y}\right)}{\left(\boldsymbol{y}^{T} \boldsymbol{y}\right)^{2}} \leq \frac{(M+m)^{2}}{4 M m} \quad \boldsymbol{y} \neq \mathbf{0}, \boldsymbol{y} \in \mathbb{R}^{n},
$$

where $M:=\lambda_{\text {max }}$ and $m:=\lambda_{\text {min }}$ are the largest and smallest eigenvalue of $\boldsymbol{A}$, respectively.

Proof If $\left(\lambda_{j}, \boldsymbol{u}_{j}\right)$ are orthonormal eigenpairs of $\boldsymbol{A}$ then $\left(\lambda_{j}^{-1}, \boldsymbol{u}_{j}\right)$ are eigenpairs for $\boldsymbol{A}^{-1}, j=1, \ldots, n$. Let $\boldsymbol{y}=\sum_{j=1}^{n} c_{j} \boldsymbol{u}_{j}$ be the corresponding eigenvector expansion of a vector $\boldsymbol{y} \in \mathbb{R}^{n}$. By orthonormality, (cf. (6.9))

$$
a:=\frac{\boldsymbol{y}^{T} \boldsymbol{A y}}{\boldsymbol{y}^{T} \boldsymbol{y}}=\sum_{i=1}^{n} t_{i} \lambda_{i}, \quad b:=\frac{\boldsymbol{y}^{T} \boldsymbol{A}^{-1} \boldsymbol{y}}{\boldsymbol{y}^{T} \boldsymbol{y}}=\sum_{i=1}^{n} \frac{t_{i}}{\lambda_{i}},
$$

where

$$
t_{i}=\frac{c_{i}^{2}}{\sum_{j=1}^{n} c_{j}^{2}} \geq 0, \quad i=1, \ldots, n \text { and } \sum_{i=1}^{n} t_{i}=1 .
$$

Thus $a$ and $b$ are convex combinations of the eigenvalues of $\boldsymbol{A}$ and $\boldsymbol{A}^{-1}$, respectively. Let $c$ be a positive constant to be chosen later. By the geometric/arithmetic mean inequality (8.33) and (13.37)

$$
\sqrt{a b}=\sqrt{(a c)(b / c)} \leq(a c+b / c) / 2=\frac{1}{2} \sum_{i=1}^{n} t_{i}\left(\lambda_{i} c+1 /\left(\lambda_{i} c\right)\right)=\frac{1}{2} \sum_{i=1}^{n} t_{i} f\left(\lambda_{i} c\right),
$$

where $f:[m c, M c] \rightarrow \mathbb{R}$ is given by $f(x):=x+1 / x$. By (13.38)

$$
\sqrt{a b} \leq \frac{1}{2} \max _{m c \leq x \leq M c} f(x) .
$$

Since $f \in C^{2}$ and $f^{\prime \prime}$ is positive it follows from Lemma 8.2 that $f$ is a convex function. But a convex function takes it maximum at one of the endpoints of the range (cf. Exercise 13.16) and we obtain

$$
\sqrt{a b} \leq \frac{1}{2} \max \{f(m c), f(M c)\} .
$$

Choosing $c:=1 / \sqrt{m M}$ we find $f(m c)=f(M c)=\sqrt{\frac{M}{m}}+\sqrt{\frac{m}{M}}=\frac{M+m}{\sqrt{m M}}$. By (13.39) we obtain

$$
\frac{\left(\boldsymbol{y}^{T} \boldsymbol{A y}\right)\left(\boldsymbol{y}^{T} \boldsymbol{A}^{-1} \boldsymbol{y}\right)}{\left(\boldsymbol{y}^{T} \boldsymbol{y}\right)^{2}}=a b \leq \frac{(M+m)^{2}}{4 M m},
$$

the upper bound in (13.36). For the lower bound we use the Cauchy-Schwarz inequality as follows

$$
1=\left(\sum_{i=1}^{n} t_{i}\right)^{2}=\left(\sum_{i=1}^{n}\left(t_{i} \lambda_{i}\right)^{1 / 2}\left(t_{i} / \lambda_{i}\right)^{1 / 2}\right)^{2} \leq\left(\sum_{i=1}^{n} t_{i} \lambda_{i}\right)\left(\sum_{i=1}^{n} t_{i} / \lambda_{i}\right)=a b .
$$ $\square$

Proof of (13.19) Let $\boldsymbol{\epsilon}_{j}:=\boldsymbol{x}-\boldsymbol{x}_{j}, j=0,1, \ldots$, where $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. It is enough to show that

$$
\frac{\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{\boldsymbol{A}}^{2}}{\left\|\boldsymbol{\epsilon}_{k}\right\|_{\boldsymbol{A}}^{2}} \leq\left(\frac{\kappa-1}{\kappa+1}\right)^{2}, \quad k=0,1,2, \ldots,
$$

for then $\left\|\boldsymbol{\epsilon}_{k}\right\|_{\boldsymbol{A}} \leq\left(\frac{\kappa-1}{\kappa+1}\right)\left\|\boldsymbol{\epsilon}_{k-1}\right\| \leq \cdots \leq\left(\frac{\kappa-1}{\kappa+1}\right)^{k}\left\|\boldsymbol{\epsilon}_{0}\right\|$. It follows from (13.8) that

$$
\boldsymbol{\epsilon}_{k+1}=\boldsymbol{\epsilon}_{k}-\alpha_{k} \boldsymbol{r}_{k}, \quad \alpha_{k}:=\frac{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{r}_{k}^{T} \boldsymbol{A} \boldsymbol{r}_{k}} .
$$

We find

$$
\begin{aligned}
\left\|\boldsymbol{\epsilon}_{k}\right\|_{\boldsymbol{A}}^{2} & =\boldsymbol{\epsilon}_{k}^{T} \boldsymbol{A} \boldsymbol{\epsilon}_{k}=\boldsymbol{r}_{k}^{T} \boldsymbol{A}^{-1} \boldsymbol{r}_{k}, \\
\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{\boldsymbol{A}}^{2} & =\left(\boldsymbol{\epsilon}_{k}-\alpha_{k} \boldsymbol{r}_{k}\right)^{T} \boldsymbol{A}\left(\boldsymbol{\epsilon}_{k}-\alpha_{k} \boldsymbol{r}_{k}\right) \\
& =\boldsymbol{\epsilon}_{k}^{T} \boldsymbol{A} \boldsymbol{\epsilon}_{k}-2 \alpha_{k} \boldsymbol{r}_{k}^{T} \boldsymbol{A} \boldsymbol{\epsilon}_{k}+\alpha_{k}^{2} \boldsymbol{r}_{k}^{T} \boldsymbol{A} \boldsymbol{r}_{k}=\left\|\boldsymbol{\epsilon}_{k}\right\|_{\boldsymbol{A}}^{2}-\frac{\left(\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}\right)^{2}}{\boldsymbol{r}_{k}^{T} \boldsymbol{A} \boldsymbol{r}_{k}}
\end{aligned}
$$

Combining these and using Kantorovich inequality

$$
\frac{\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{\boldsymbol{A}}^{2}}{\left\|\boldsymbol{\epsilon}_{k}\right\|_{\boldsymbol{A}}^{2}}=1-\frac{\left(\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}\right)^{2}}{\left(\boldsymbol{r}_{k}^{T} \boldsymbol{A} \boldsymbol{r}_{k}\right)\left(\boldsymbol{r}_{k}^{T} \boldsymbol{A}^{-1} \boldsymbol{r}_{k}\right)} \leq 1-\frac{4 \lambda_{\min } \lambda_{\max }}{\left(\lambda_{\min }+\lambda_{\max }\right)^{2}}=\left(\frac{\kappa-1}{\kappa+1}\right)^{2}
$$

and (13.40) is proved. $\square$

### 13.4.3 Monotonicity of the Error

The error analysis for the conjugate gradient method is based on the $\boldsymbol{A}$-norm. We end this chapter by considering the Euclidian norm of the error, and show that it is strictly decreasing.

Theorem 13.8 (The Error in cg Is Strictly Decreasing) Let in the conjugate gradient method $m$ be the smallest integer such that $\boldsymbol{r}_{m+1}=\mathbf{0}$. For $k \leq m$ we have $\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{2}<\left\|\boldsymbol{\epsilon}_{k}\right\|_{2}$. More precisely,

$$
\left\|\boldsymbol{\epsilon}_{k}\right\|_{2}^{2}-\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{2}^{2}=\frac{\left\|\boldsymbol{p}_{k}\right\|_{2}^{2}}{\left\|\boldsymbol{p}_{k}\right\|_{\boldsymbol{A}}^{2}}\left(\left\|\boldsymbol{\epsilon}_{k}\right\|_{\boldsymbol{A}}^{2}+\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{\boldsymbol{A}}^{2}\right)
$$

where $\boldsymbol{\epsilon}_{j}=\boldsymbol{x}-\boldsymbol{x}_{j}$ and $\boldsymbol{A x}=\boldsymbol{b}$.
Proof For $j \leq m$

$$
\boldsymbol{\epsilon}_{j}=\boldsymbol{x}_{m+1}-\boldsymbol{x}_{j}=\boldsymbol{x}_{m}-\boldsymbol{x}_{j}+\alpha_{m} \boldsymbol{p}_{m}=\boldsymbol{x}_{m-1}-\boldsymbol{x}_{j}+\alpha_{m-1} \boldsymbol{p}_{m-1}+\alpha_{m} \boldsymbol{p}_{m}=\ldots
$$

so that

$$
\boldsymbol{\epsilon}_{j}=\sum_{i=j}^{m} \alpha_{i} \boldsymbol{p}_{i}, \quad \alpha_{i}=\frac{\boldsymbol{r}_{i}^{T} \boldsymbol{r}_{i}}{\boldsymbol{p}_{i}^{T} \boldsymbol{A} \boldsymbol{p}_{i}} .
$$

By (13.41) and $\boldsymbol{A}$-orthogonality

$$
\left\|\boldsymbol{\epsilon}_{j}\right\|_{\boldsymbol{A}}^{2}=\boldsymbol{\epsilon}_{j} \boldsymbol{A} \boldsymbol{\epsilon}_{j}=\sum_{i=j}^{m} \alpha_{i}^{2} \boldsymbol{p}_{i}^{T} \boldsymbol{A} \boldsymbol{p}_{i}=\sum_{i=j}^{m} \frac{\left(\boldsymbol{r}_{i}^{T} \boldsymbol{r}_{i}\right)^{2}}{\boldsymbol{p}_{i}^{T} \boldsymbol{A} \boldsymbol{p}_{i}} .
$$

By (13.17) and Lemma 13.3

$$
\boldsymbol{p}_{i}^{T} \boldsymbol{p}_{k}=\left(\boldsymbol{r}_{i}+\beta_{i-1} \boldsymbol{p}_{i-1}\right)^{T} \boldsymbol{p}_{k}=\beta_{i-1} \boldsymbol{p}_{i-1}^{T} \boldsymbol{p}_{k}=\cdots=\beta_{i-1} \cdots \beta_{k}\left(\boldsymbol{p}_{k}^{T} \boldsymbol{p}_{k}\right),
$$

and since $\beta_{i-1} \cdots \beta_{k}=\left(\boldsymbol{r}_{i}^{T} \boldsymbol{r}_{i}\right) /\left(\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}\right)$ we find

$$
\boldsymbol{p}_{i}^{T} \boldsymbol{p}_{k}=\frac{\boldsymbol{r}_{i}^{T} \boldsymbol{r}_{i}}{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}} \boldsymbol{p}_{k}^{T} \boldsymbol{p}_{k}, \quad i \geq k
$$

Since

$$
\left\|\boldsymbol{\epsilon}_{k}\right\|_{2}^{2}=\left\|\boldsymbol{\epsilon}_{k+1}+\boldsymbol{x}_{k+1}-\boldsymbol{x}_{k}\right\|_{2}^{2}=\left\|\boldsymbol{\epsilon}_{k+1}+\alpha_{k} \boldsymbol{p}_{k}\right\|_{2}^{2},
$$

we obtain

$$
\begin{aligned}
& \left\|\boldsymbol{\epsilon}_{k}\right\|_{2}^{2}-\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{2}^{2}=\alpha_{k}\left(2 \boldsymbol{p}_{k}^{T} \boldsymbol{\epsilon}_{k+1}+\alpha_{k} \boldsymbol{p}_{k}^{T} \boldsymbol{p}_{k}\right) \\
& \quad \stackrel{\text { (13.41) }}{=} \alpha_{k}\left(2 \sum_{i=k+1}^{m} \alpha_{i} \boldsymbol{p}_{i}^{T} \boldsymbol{p}_{k}+\alpha_{k} \boldsymbol{p}_{k}^{T} \boldsymbol{p}_{k}\right)=\left(\sum_{i=k}^{m}+\sum_{i=k+1}^{m}\right) \alpha_{k} \alpha_{i} \boldsymbol{p}_{i}^{T} \boldsymbol{p}_{k} \\
& \quad \stackrel{\text { (13.43) }}{=}\left(\sum_{i=k}^{m}+\sum_{i=k+1}^{m}\right) \frac{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k}} \frac{\boldsymbol{r}_{i}^{T} \boldsymbol{r}_{i}}{\boldsymbol{p}_{i}^{T} \boldsymbol{A} \boldsymbol{p}_{i}} \frac{\boldsymbol{r}_{i}^{T} \boldsymbol{r}_{i}}{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}} \boldsymbol{p}_{k}^{T} \boldsymbol{p}_{k} \\
& \quad \stackrel{\text { (13.42) }}{=} \frac{\left\|\boldsymbol{p}_{k}\right\|_{2}^{2}}{\left\|\boldsymbol{p}_{k}\right\|_{\boldsymbol{A}}^{2}}\left(\left\|\boldsymbol{\epsilon}_{k}\right\|_{\boldsymbol{A}}^{2}+\left\|\boldsymbol{\epsilon}_{k+1}\right\|_{\boldsymbol{A}}^{2}\right) .
\end{aligned}
$$

and the Theorem is proved. $\square$

### 13.5 Preconditioning

For problems $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ of size $n$, where both $n$ and $\operatorname{cond}_{2}(\boldsymbol{A})$ are large, it is often possible to improve the performance of the conjugate gradient method by using a technique known as preconditioning. Instead of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ we consider an equivalent system $\boldsymbol{B} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{B} \boldsymbol{b}$, where $\boldsymbol{B}$ is nonsingular and $\operatorname{cond}_{2}(\boldsymbol{B} \boldsymbol{A})$ is smaller than $\operatorname{cond}_{2}(\boldsymbol{A})$. The matrix $\boldsymbol{B}$ will in many cases be the inverse of another matrix, $\boldsymbol{B}=\boldsymbol{M}^{-1}$. We cannot use CG on $\boldsymbol{B} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{B} \boldsymbol{b}$ directly since $\boldsymbol{B} \boldsymbol{A}$ in general is not symmetric even if both $\boldsymbol{A}$ and $\boldsymbol{B}$ are. But if $\boldsymbol{B}$ (and hence $\boldsymbol{M}$ ) is positive definite then we can apply CG to a symmetrized system and then transform the recurrence formulas to an iterative method for the original system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. This iterative method is known as the preconditioned conjugate gradient method. We shall see that the convergence properties of this method is determined by the eigenvalues of $\boldsymbol{B} \boldsymbol{A}$.

Suppose $\boldsymbol{B}$ is positive definite. By Theorem 4.4 there is a nonsingular matrix $\boldsymbol{C}$ such that $\boldsymbol{B}=\boldsymbol{C}^{T} \boldsymbol{C}$. ( $\boldsymbol{C}$ is only needed for the derivation and will not appear in the final formulas). Now

$$
\boldsymbol{B} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{B} \boldsymbol{b} \Leftrightarrow \boldsymbol{C}^{T}\left(\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right) \boldsymbol{C}^{-T} \boldsymbol{x}=\boldsymbol{C}^{T} \boldsymbol{C} \boldsymbol{b} \Leftrightarrow\left(\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right) \boldsymbol{y}=\boldsymbol{C} \boldsymbol{b},
$$

where $\boldsymbol{y}:=\boldsymbol{C}^{-T} \boldsymbol{x}$. We have 3 linear systems

$$
\begin{aligned}
A x & =b \\
B A x & =B b \\
\left(C A C^{T}\right) y & =C b, \& x=C^{T} y .
\end{aligned}
$$

Note that (13.44) and (13.46) are positive definite linear systems. In addition to being positive definite the matrix $\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}$ is similar to $\boldsymbol{B} \boldsymbol{A}$. Indeed,

$$
\boldsymbol{C}^{T}\left(\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right) \boldsymbol{C}^{-T}=\boldsymbol{B} \boldsymbol{A} .
$$

Thus $\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}$ and $\boldsymbol{B} \boldsymbol{A}$ have the same eigenvalues. Therefore, if we apply the conjugate gradient method to (13.46) then the rate of convergence will be determined by the eigenvalues of $\boldsymbol{B} \boldsymbol{A}$.

We apply the conjugate gradient method to $\left(\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right) \boldsymbol{y}=\boldsymbol{C} \boldsymbol{b}$. Denoting the search direction by $\boldsymbol{q}_{k}$ and the residual by $\boldsymbol{z}_{k}:=\boldsymbol{C} \boldsymbol{b}-\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T} \boldsymbol{y}_{k}$ we obtain the following from (13.15), (13.16), and (13.17).

$$
\begin{aligned}
& \boldsymbol{y}_{k+1}=\boldsymbol{y}_{k}+\alpha_{k} \boldsymbol{q}_{k}, \quad \alpha_{k}=z_{k}^{T} z_{k} / \boldsymbol{q}_{k}^{T}\left(\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right) \boldsymbol{q}_{k}, \\
& \boldsymbol{z}_{k+1}=z_{k}-\alpha_{k}\left(\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right) \boldsymbol{q}_{k}, \\
& \boldsymbol{q}_{k+1}=z_{k+1}+\beta_{k} \boldsymbol{q}_{k}, \quad \beta_{k}=z_{k+1}^{T} z_{k+1} / z_{k}^{T} z_{k} .
\end{aligned}
$$

With

$$
\boldsymbol{x}_{k}:=\boldsymbol{C}^{T} \boldsymbol{y}_{k}, \quad \boldsymbol{p}_{k}:=\boldsymbol{C}^{T} \boldsymbol{q}_{k}, \quad \boldsymbol{s}_{k}:=\boldsymbol{C}^{T} z_{k}, \quad \boldsymbol{r}_{k}:=\boldsymbol{C}^{-1} z_{k}
$$

this can be transformed into

$$
\begin{aligned}
& \boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}, \quad \alpha_{k}=\frac{\boldsymbol{s}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{p}_{k}^{T} \boldsymbol{A} \boldsymbol{p}_{k}}, \\
& \boldsymbol{r}_{k+1}=\boldsymbol{r}_{k}-\alpha_{k} \boldsymbol{A} \boldsymbol{p}_{k}, \\
& \boldsymbol{s}_{k+1}=\boldsymbol{s}_{k}-\alpha_{k} \boldsymbol{B} \boldsymbol{A} \boldsymbol{p}_{k}, \\
& \boldsymbol{p}_{k+1}=\boldsymbol{s}_{k+1}+\beta_{k} \boldsymbol{p}_{k}, \quad \beta_{k}=\frac{\boldsymbol{s}_{k+1}^{T} \boldsymbol{r}_{k+1}}{\boldsymbol{s}_{k}^{T} \boldsymbol{r}_{k}} .
\end{aligned}
$$

Here $\boldsymbol{x}_{k}$ will be an approximation to the solution $\boldsymbol{x}$ of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}, \boldsymbol{r}_{k}=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}$ is the residual in the original system, and $\boldsymbol{s}_{k}=\boldsymbol{C}^{T} \boldsymbol{z}_{k}=\boldsymbol{C}^{T}\left(\boldsymbol{C}-\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right) \boldsymbol{y}_{k}=\boldsymbol{B} \boldsymbol{b}-$ $\boldsymbol{B} \boldsymbol{A} \boldsymbol{x}_{k}$ is the residual in the preconditioned system. If we set $\boldsymbol{r}_{0}=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{0}, \boldsymbol{p}_{0}=$ $\boldsymbol{s}_{0}=\boldsymbol{B r}_{0}$, we obtain the following preconditioned conjugate gradient algorithm for determining approximations $\boldsymbol{x}_{k}$ to the solution of a positive definite system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, by considering the system $\boldsymbol{B} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{B} \boldsymbol{b}$, with $\boldsymbol{B}$ positive definite. The iteration is stopped when $\left\|\boldsymbol{r}_{k}\right\|_{2} /\|\boldsymbol{b}\|_{2} \leq$ tol or $k>$ itmax. $K$ is the number of iterations used, and $\mathrm{x}\left(=\boldsymbol{x}_{0}\right)$ is the starting iteration.

```
function [x,K]=pcg(A,B,b,x,tol,itmax)
% [x,K]=pcg(A,B,b,x,tol,itmax)
r=b-A*x; p=B*r; s=p; rho=s'*r; rho0=b'*b;
for k=0:itmax
    if sqrt(rho/rho0)<= tol
        K=k; return
    end
    t=A*p; a=rho/(p’*t);
    x=x+a*p; r=r-a*t;
    w=B*t; s=s-a*w;
    rhos=rho; rho=s'*r;
    p=r+(rho/rhos)*p;
end
K=itmax+1;
end
```

Listing 13.3 pcg

Apart from the calculation of $\rho$ this algorithm is quite similar to Algorithm 13.1. The main additional work is contained in $w=B * t$. We'll discuss this further in connection with an example. There the inverse of $\boldsymbol{B}$ is known and we have to solve a linear system to find $\boldsymbol{w}$.

We have the following convergence result for this algorithm.
Theorem 13.9 (Error Bound Preconditioned cg) Suppose we apply a positive definite preconditioner $\boldsymbol{B}$ to the positive definite system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Then the quantities $\boldsymbol{x}_{k}$ computed in Algorithm 13.3 satisfy the following bound:

$$
\frac{\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}}{\left\|\boldsymbol{x}-\boldsymbol{x}_{0}\right\|_{\boldsymbol{A}}} \leq 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^{k} \quad \text { for } \quad k \geq 0
$$

where $\kappa=\lambda_{\text {max }} / \lambda_{\text {min }}$ is the ratio of the largest and smallest eigenvalue of $\boldsymbol{B} \boldsymbol{A}$.
Proof Since Algorithm 13.3 is equivalent to solving (13.46) by the conjugate gradient method Theorem 13.3 implies that

$$
\frac{\left\|\boldsymbol{y}-\boldsymbol{y}_{k}\right\|_{\boldsymbol{C A C}^{T}}}{\left\|\boldsymbol{y}-\boldsymbol{y}_{0}\right\|_{\boldsymbol{C A C}^{T}}} \leq 2\left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^{k}, \quad \text { for } \quad k \geq 0,
$$

where $\boldsymbol{y}_{k}$ is the conjugate gradient approximation to the solution $\boldsymbol{y}$ of (13.46) and $\kappa$ is the ratio of the largest and smallest eigenvalue of $\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}$. Since $\boldsymbol{B} \boldsymbol{A}$ and $\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}$ are similar this is the same as the $\kappa$ in the theorem. By (13.47) we have

$$
\begin{aligned}
\left\|\boldsymbol{y}-\boldsymbol{y}_{k}\right\|_{\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}}^{2} & =\left(\boldsymbol{y}-\boldsymbol{y}_{k}\right)^{T}\left(\boldsymbol{C} \boldsymbol{A} \boldsymbol{C}^{T}\right)\left(\boldsymbol{y}-\boldsymbol{y}_{k}\right) \\
& =\left(\boldsymbol{C}^{T}\left(\boldsymbol{y}-\boldsymbol{y}_{k}\right)\right)^{T} \boldsymbol{A}\left(\boldsymbol{C}^{T}\left(\boldsymbol{y}-\boldsymbol{y}_{k}\right)\right)=\left\|\boldsymbol{x}-\boldsymbol{x}_{k}\right\|_{\boldsymbol{A}}^{2},
\end{aligned}
$$

and the proof is complete. $\square$

We conclude that $\boldsymbol{B}$ should satisfy the following requirements for a problem of size $n$ :

1. The eigenvalues of $\boldsymbol{B} \boldsymbol{A}$ should be located in a narrow interval. Preferably one should be able to bound the length of the interval independently of $n$.
2. The evaluation of $\boldsymbol{B} \boldsymbol{x}$ for a given vector $\boldsymbol{x}$ should not be expensive in storage and arithmetic operations, ideally $O(n)$ for both.

In this book we only consider one example of a preconditioner. For a comprehensive treatment of preconditioners see [1].

### 13.6 Preconditioning Example

### 13.6.1 A Variable Coefficient Problem

Consider the problem

$$
\begin{aligned}
-\frac{\partial}{\partial x}\left(c(x, y) \frac{\partial u}{\partial x}\right)-\frac{\partial}{\partial y}\left(c(x, y) \frac{\partial u}{\partial y}\right) & =f(x, y), & & (x, y) \in \Omega=(0,1)^{2}, \\
u(x, y) & =0, & & (x, y) \in \partial \Omega .
\end{aligned}
$$

Here $\Omega$ is the open unit square while $\partial \Omega$ is the boundary of $\Omega$. The functions $f$ and $c$ are given and we seek a function $u=u(x, y)$ such that (13.52) holds. We assume that $c$ and $f$ are defined and continuous on $\Omega$ and that $c(x, y)>0$ for all $(x, y) \in \Omega$. The problem (13.52) reduces to the Poisson problem (10.1) in the special case where $c(x, y)=1$ for $(x, y) \in \Omega$.

To solve (13.52) numerically, we choose $m \in \mathbb{N}$, set $h:=1 /(m+1)$, and define index sets

$$
\begin{aligned}
I_{m} & :=\{(j, k): 1 \leq j, k \leq m\}, \\
\bar{I}_{m} & :=\{(j, k): 0 \leq j, k \leq m+1\}, \\
\partial I_{m} & :=\bar{I}_{m} \backslash I_{m} .
\end{aligned}
$$

We compute approximations $v_{j, k} \approx u\left(x_{j}, y_{k}\right)$ on a grid of points

$$
\left\{\left(x_{j}, y_{k}\right)=(j h, k h):(j, k) \in \bar{I}_{m}\right\}
$$

using a finite difference method. For univariate functions $f, g$ we approximate derivatives by using the central difference approximations

$$
\begin{aligned}
\frac{d}{d t}\left(f(t) \frac{d}{d t} g(t)\right) & \approx\left(f\left(t+\frac{h}{2}\right) \frac{d}{d t} g(t+h / 2)-f\left(t-\frac{h}{2}\right) \frac{d}{d t} g\left(t-\frac{h}{2}\right)\right) / h \\
& \approx\left(f\left(t+\frac{h}{2}\right)(g(t+h)-g(t))-f\left(t-\frac{h}{2}\right)(g(t)-g(t-h))\right) / h^{2}
\end{aligned}
$$

to obtain

$$
\begin{array}{rlr}
\left(L_{h} v\right)_{j, k} & :=\frac{(d v)_{j, k}}{h^{2}}=f_{j, k}, & (j, k) \in I_{m}, \\
v_{j, k} & =0, & (j, k) \in \partial I_{m},
\end{array}
$$

where $f_{j, k}:=f\left(x_{j}, y_{k}\right),(d v)_{j, k}:=\left(d_{1} v\right)_{j, k}+\left(d_{2} v\right)_{j, k}$,

$$
\begin{aligned}
& \left(d_{1} v\right)_{j, k}:=c_{j-\frac{1}{2}, k}\left(v_{j, k}-v_{j-1, k}\right)-c_{j+\frac{1}{2}, k}\left(v_{j+1, k}-v_{j, k}\right) \approx-h^{2} \frac{\partial}{\partial x}\left(c \frac{\partial u}{\partial x}\right)_{j, k}, \\
& \left(d_{2} v\right)_{j, k}:=c_{j, k-\frac{1}{2}}\left(v_{j, k}-v_{j, k-1}\right)-c_{j, k+\frac{1}{2}}\left(v_{j, k+1}-v_{j, k}\right) \approx-h^{2} \frac{\partial}{\partial y}\left(c \frac{\partial u}{\partial y}\right)_{j, k},
\end{aligned}
$$

and where $c_{p, q}=c(p h, q h)$ for $p, q \in \mathbb{R}$. The equation (13.53) can be written in matrix form as

$$
L_{h} v=\boldsymbol{F}, \quad L_{h} v:=\frac{1}{h^{2}}\left[\begin{array}{ccc}
(d v)_{1,1} & \ldots & (d v)_{1, m} \\
\vdots & & \vdots \\
(d v)_{m, 1} & \ldots & (d v)_{m, m}
\end{array}\right], \quad \boldsymbol{F}:=\left[\begin{array}{ccc}
f_{1,1} & \ldots & f_{1, m} \\
\vdots & & \vdots \\
f_{m, 1} & \ldots & f_{m, m}
\end{array}\right] .
$$

This is a linear system with the elements of

$$
\boldsymbol{V}:=\left[\begin{array}{ccc}
v_{1,1} & \ldots & v_{1, m} \\
\vdots & & \vdots \\
v_{m, 1} & \ldots & v_{m, m}
\end{array}\right]
$$

as unknowns. The system $h^{2} L_{h} v=h^{2} \boldsymbol{F}$ can be written in standard form $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ where $\boldsymbol{x}=\operatorname{vec}(\boldsymbol{V}), \boldsymbol{b}=h^{2} \operatorname{vec}(\boldsymbol{F})$, and the coefficient matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is defined as follows

$$
\boldsymbol{A} \boldsymbol{x}=\boldsymbol{A} \operatorname{vec}(\boldsymbol{V}):=h^{2} \operatorname{vec}\left(L_{h} \boldsymbol{v}\right) .
$$

If $c(x, y)=1$ for all $(x, y) \in \Omega$ we recover the Poisson matrix (10.8). In general we can show that $\boldsymbol{A}$ is positive definite for all $m \in \mathbb{N}$ provided $c(x, y)>0$ for all $(x, y) \in \Omega$. For this we do not need the explicit form of $\boldsymbol{A}$.

To start we define for $m \in \mathbb{N}$ a discrete inner product on the space of matrices $\mathbb{R}^{m \times m}$

$$
\langle\boldsymbol{V}, \boldsymbol{W}\rangle:=h^{2} \sum_{j, k=1}^{m} v_{j, k} w_{j, k},
$$

We then have the following lemma.
Lemma 13.6 (Discrete Inner Product) If $\boldsymbol{V}, \boldsymbol{W} \in \mathbb{R}^{m \times m}$ and $v_{j, k}=w_{j, k}=0$ for $(j, k) \in \partial I_{m}$, then

$$
\begin{aligned}
\left\langle L_{h} v, \boldsymbol{W}\right\rangle & =\sum_{j=1}^{m} \sum_{k=0}^{m} c_{j, k+\frac{1}{2}}\left(v_{j, k+1}-v_{j, k}\right)\left(w_{j, k+1}-w_{j, k}\right) \\
& +\sum_{j=0}^{m} \sum_{k=1}^{m} c_{j+\frac{1}{2}, k}\left(v_{j+1, k}-v_{j, k}\right)\left(w_{j+1, k}-w_{j, k}\right) .
\end{aligned}
$$

Proof If $m \in \mathbb{N}, a_{i}, b_{i}, c_{i} \in \mathbb{R}$ for $i=0, \ldots, m$ and $b_{0}=c_{0}=b_{m+1}=c_{m+1}=0$ then

$$
\sum_{i=1}^{m}\left(a_{i-1}\left(b_{i}-b_{i-1}\right)-a_{i}\left(b_{i+1}-b_{i}\right)\right) c_{i}=\sum_{i=0}^{m} a_{i}\left(b_{i+1}-b_{i}\right)\left(c_{i+1}-c_{i}\right) .
$$

Indeed, the left hand side can be written

$$
\sum_{i=0}^{m} a_{i}\left(b_{i+1}-b_{i}\right) c_{i+1}-\sum_{i=0}^{m} a_{i}\left(b_{i+1}-b_{i}\right) c_{i},
$$

and the right hand side of (13.60) follows. We apply (13.60) to $\left(d_{1} v\right)_{j, k} w_{j, k}$ and $\left(d_{2} v\right)_{j, k} w_{j, k}$ given by (13.55) and (13.59) follows. $\square$

Theorem 13.10 (Positive Definite Matrix) If $c(x, y)>0$ for $(x, y) \in \Omega$ then the matrix $\boldsymbol{A}$ defined by (13.57) via the linear system (13.56) is positive definite.

Proof By (13.59) $\left\langle L_{h} v, \boldsymbol{W}\right\rangle=\left\langle\boldsymbol{W}, L_{h} v\right\rangle$ and symmetry follows. We take $\boldsymbol{W}=$ $\boldsymbol{V}$ and obtain quadratic factors in (13.59). Since $c_{j+\frac{1}{2}, k}$ and $c_{j, k+\frac{1}{2}}$ correspond to values of $c$ in $\Omega$ for the values of $j, k$ in the sums, it follows that they are positive and $\left\langle L_{h} v, \boldsymbol{V}\right\rangle \geq 0$ for all $\boldsymbol{V} \in \mathbb{R}^{m \times m}$. If $\left\langle L_{h} v, \boldsymbol{V}\right\rangle=0$ then all the quadratic factors must be zero, and $v_{j, k+1}=v_{j, k}$ for $k=0,1, \ldots, m$ and $j=1, \ldots, m$. Now $v_{j, 0}=v_{j, m+1}=0$ implies that $\boldsymbol{V}=\mathbf{0}$. It follows that the linear system (13.56) is positive definite. $\square$

### 13.6.2 Applying Preconditioning

Consider solving $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A}$ is given by (13.57) and $b \in \mathbb{R}^{n}$. Since $\boldsymbol{A}$ is positive definite it is nonsingular and the system has a unique solution $x \in \mathbb{R}^{n}$. Moreover we can use either Cholesky factorization or the block tridiagonal solver to find $\boldsymbol{x}$. Since the bandwidth of $\boldsymbol{A}$ is $m=\sqrt{n}$ both of these methods require $O\left(n^{2}\right)$ arithmetic operations for large $n$.

If we choose $c(x, y) \equiv 1$ in (13.52), we get the Poisson problem. With this in mind, we may think of the coefficient matrix $\boldsymbol{A}_{p}$ arising from the discretization of the Poisson problem as an approximation to the matrix (13.57). This suggests using $\boldsymbol{B}=\boldsymbol{A}_{p}^{-1}$, the inverse of the discrete Poisson matrix as a preconditioner for the system (13.53).

Consider Algorithm 13.3. With this preconditioner the calculation $\boldsymbol{w}=\boldsymbol{B} \boldsymbol{t}$ takes the form $\boldsymbol{A}_{p} \boldsymbol{w}_{k}=\boldsymbol{t}_{k}$.

In Sect. 11.2 we developed a Simple fast Poisson Solver, Cf. Algorithm 11.1. This method can be utilized to solve $\boldsymbol{A}_{p} \boldsymbol{w}=\boldsymbol{t}$.

Consider the specific problem where

$$
c(x, y)=e^{-x+y} \text { and } f(x, y)=1 .
$$

We have used Algorithm 13.1 (conjugate gradient without preconditioning), and Algorithm 13.3 (conjugate gradient with preconditioning) to solve the problem (13.52). We used $\boldsymbol{x}_{0}=0$ and $\epsilon=10^{-8}$. The results are shown in Table 13.3.

Without preconditioning the number of iterations still seems to be more or less proportional to $\sqrt{n}$ although the convergence is slower than for the constant coefficient problem. Using preconditioning speeds up the convergence considerably. The number of iterations appears to be bounded independently of $n$.

Using a preconditioner increases the work in each iteration. For the present example the number of arithmetic operations in each iteration changes from $O(n)$ without preconditioning to $O\left(n^{3 / 2}\right)$ or $O\left(n \log _{2} n\right)$ with preconditioning. This is not a large increase and both the number of iterations and the computing time is reduced significantly.

Let us finally show that the number $\kappa=\lambda_{\text {max }} / \lambda_{\text {min }}$ which determines the rate of convergence for the preconditioned conjugate gradient method applied to (13.52) can be bounded independently of $n$.

Table 13.3 The number of iterations $K$ (no preconditioning) and $K_{p r e}$ (with preconditioning) for the problem (13.52) using the discrete Poisson problem as a preconditioner
| $n$ | 2500 | 10000 | 22500 | 40000 | 62500 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $K$ | 222 | 472 | 728 | 986 | 1246 |
| $K / \sqrt{n}$ | 4.44 | 4.72 | 4.85 | 4.93 | 4.98 |
| $K_{\text {pre }}$ | 22 | 23 | 23 | 23 | 23 |


Theorem 13.12 (Eigenvalues of Preconditioned Matrix) Suppose $0<c_{0} \leq$ $c(x, y) \leq c_{1}$ for all $(x, y) \in[0,1]^{2}$. For the eigenvalues of the matrix $\boldsymbol{B} \boldsymbol{A}=\boldsymbol{A}_{p}^{-1} \boldsymbol{A}$ just described we have

$$
\kappa=\frac{\lambda_{\max }}{\lambda_{\min }} \leq \frac{c_{1}}{c_{0}} .
$$

Proof Suppose $\boldsymbol{A}_{p}^{-1} \boldsymbol{A} \boldsymbol{x}=\lambda x$ for some $\boldsymbol{x} \in \mathbb{R}^{n} \backslash\{0\}$. Then $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{A}_{p} x$. Multiplying this by $\boldsymbol{x}^{T}$ and solving for $\lambda$ we find

$$
\lambda=\frac{x^{T} \boldsymbol{A x}}{x^{T} \boldsymbol{A}_{p} x} .
$$

We computed $\boldsymbol{x}^{T} \boldsymbol{A} \boldsymbol{x}$ in (13.59) and we obtain $\boldsymbol{x}^{T} \boldsymbol{A}_{p} \boldsymbol{x}$ by setting all the $c$ 's there equal to one

$$
\boldsymbol{x}^{T} \boldsymbol{A}_{p} x=\sum_{i=1}^{m} \sum_{j=0}^{m}\left(v_{i, j+1}-v_{i, j}\right)^{2}+\sum_{j=1}^{m} \sum_{i=0}^{m}\left(v_{i+1, j}-v_{i, j}\right)^{2} .
$$

Thus $\boldsymbol{x}^{T} \boldsymbol{A}_{p} x>0$ and bounding all the $c$ 's in (13.59) from below by $c_{0}$ and above by $c_{1}$ we find

$$
c_{0}\left(x^{T} \boldsymbol{A}_{p} x\right) \leq x^{T} \boldsymbol{A} \boldsymbol{x} \leq c_{1}\left(x^{T} \boldsymbol{A}_{p} x\right)
$$

which implies that $c_{0} \leq \lambda \leq c_{1}$ for all eigenvalues $\lambda$ of $\boldsymbol{B} \boldsymbol{A}=\boldsymbol{A}_{p}^{-1} \boldsymbol{A}$. $\square$

Using $c(x, y)=e^{-x+y}$ as above, we find $c_{0}=e^{-2}$ and $c_{1}=1$. Thus $\kappa \leq e^{2} \approx$ 7.4, a quite acceptable matrix condition number which explains the convergence results from our numerical experiment.

### 13.7 Exercises Chap. 13

### 13.7.1 Exercises Sect. 13.1

Exercise 13.1 ( $\boldsymbol{A}$-Norm) One can show that the $\boldsymbol{A}$-norm is a vector norm on $\mathbb{R}^{n}$ without using the fact that it is an inner product norm. Show this with the help of the Cholesky factorization of $\boldsymbol{A}$.
Exercise 13.2 (Paraboloid) Let $\boldsymbol{A}=\boldsymbol{U} \boldsymbol{D} \boldsymbol{U}^{T}$ be the spectral decomposition of $\boldsymbol{A}$, i.e., $\boldsymbol{U}$ is orthogonal and $\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ is diagonal. Define new variables
$\boldsymbol{v}=\left[v_{1}, \ldots, v_{n}\right]^{T}:=\boldsymbol{U}^{T} \boldsymbol{y}$, and set $\boldsymbol{c}:=\boldsymbol{U}^{T} \boldsymbol{b}=\left[c_{1}, \ldots, c_{n}\right]^{T}$. Show that

$$
Q(\boldsymbol{y})=\frac{1}{2} \sum_{j=1}^{n} \lambda_{j} v_{j}^{2}-\sum_{j=1}^{n} c_{j} v_{j} .
$$

Exercise 13.3 (Steepest Descent Iteration) Verify the numbers in Example 13.1.
Exercise 13.4 (Steepest Descent (Exam Exercise 2011-1)) The method of steepest descent can be used to solve a linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ for $\boldsymbol{x} \in \mathbb{R}^{n}$, where $\boldsymbol{A} \in \mathbb{R}^{n, n}$ is symmetric and positive definite, and $\boldsymbol{b} \in \mathbb{R}^{n}$. With $\boldsymbol{x}_{0} \in \mathbb{R}^{n}$ an initial guess, the iteration is $\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{r}_{k}$, where $\boldsymbol{r}_{k}$ is the residual, $\boldsymbol{r}_{k}=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}$, and $\alpha_{k}=\frac{\boldsymbol{r}_{k}^{T} \boldsymbol{r}_{k}}{\boldsymbol{r}_{k}^{T} \boldsymbol{A r}_{k}}$.

a) Compute $\boldsymbol{x}_{1}$ if $\boldsymbol{A}=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right], \boldsymbol{b}=\left[\begin{array}{ll}1 & 1\end{array}\right]^{T}$ and $\boldsymbol{x}_{0}=\mathbf{0}$.
b) If the $k$-th error, $\boldsymbol{e}_{k}=\boldsymbol{x}_{k}-\boldsymbol{x}$, is an eigenvector of $\boldsymbol{A}$, what can you say about $\boldsymbol{x}_{k+1}$ ?

### 13.7.2 Exercises Sect. 13.2

Exercise 13.5 (Conjugate Gradient Iteration, II) Do one iteration with the conjugate gradient method when $\boldsymbol{x}_{0}=\mathbf{0}$. (Answer: $\boldsymbol{x}_{1}=\left(\frac{\boldsymbol{b}^{T} \boldsymbol{b}}{\boldsymbol{b}^{T} \boldsymbol{A} \boldsymbol{b}}\right) \boldsymbol{b}$.)
Exercise 13.6 (Conjugate Gradient Iteration, III) Do two conjugate gradient iterations for the system

$$
\left[\begin{array}{rr}
2 & -1 \\
-1 & 2
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
3
\end{array}\right]
$$

starting with $\boldsymbol{x}_{0}=\mathbf{0}$.
Exercise 13.7 (The cg Step Length Is Optimal) Show that the step length $\alpha_{k}$ in the conjugate gradient method is optimal. ${ }^{2}$

Exercise 13.8 (Starting Value in cg) Show that the conjugate gradient method (13.18) for $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ starting with $\boldsymbol{x}_{0}$ is the same as applying the method to the system $\boldsymbol{A} \boldsymbol{y}=\boldsymbol{r}_{0}:=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{0}$ starting with $\boldsymbol{y}_{0}=\mathbf{0} .^{3}$

[^24]Exercise 13.9 (Program Code for Testing Steepest Descent) Write a function K=sdtest(m,a,d,tol,itmax) to test the steepest descent method on the matrix $\boldsymbol{T}_{2}$. Make the analogues of Tables 13.1 and 13.2. For Table 13.2 it is enough to test for say $n=100,400,1600,2500$, and tabulate $K / n$ instead of $K / \sqrt{n}$ in the last row. Conclude that the upper bound (13.19) is realistic. Compare also with the number of iterations for the J and GS method in Table 12.1.

Exercise 13.10 (Using cg to Solve Normal Equations) Consider solving the linear system $\boldsymbol{A}^{T} \boldsymbol{A} \boldsymbol{x}=\boldsymbol{A}^{T} \boldsymbol{b}$ by using the conjugate gradient method. Here $\boldsymbol{A} \in \mathbb{R}^{m, n}, \boldsymbol{b} \in \mathbb{R}^{m}$ and $\boldsymbol{A}^{T} \boldsymbol{A}$ is positive definite. ${ }^{4}$ Explain why only the following modifications in Algorithm 13.1 are necessary

1. $\mathrm{r}=\mathrm{A}^{\prime}\left(\mathrm{b}-\mathrm{A}^{*} \mathrm{x}\right) ; \mathrm{p}=\mathrm{r}$;
2. a=rho/(t'*t);
3. $\mathrm{r}=\mathrm{r}-\mathrm{a}^{*} \mathrm{~A}^{*} \mathrm{t}$;

Note that the condition number of the normal equations is $\operatorname{cond}_{2}(\boldsymbol{A})^{2}$, the square of the condition number of $\boldsymbol{A}$.

Exercise 13.11 ( $\boldsymbol{A}^{T} \boldsymbol{A}$ Inner Product (Exam Exercise 2018-3)) In this problem we consider linear systems of the form $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$, where $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ and $\boldsymbol{b} \in \mathbb{R}^{n}$ are given, and $\boldsymbol{x} \in \mathbb{R}^{n}$ is the unknown vector. We assume throughout that $\boldsymbol{A}$ is nonsingular.

a) Let $\left\{\boldsymbol{v}_{i}\right\}_{i=1}^{k}$ be a set of linearly independent vectors in $\mathbb{R}^{n}$, and let $\langle\cdot, \cdot\rangle$ be an inner product in $\mathbb{R}^{n}$. Explain that the $k \times k$-matrix $\boldsymbol{N}$ with entries $n_{i j}=\left\langle\boldsymbol{v}_{i}, \boldsymbol{v}_{j}\right\rangle$ is symmetric positive definite.
b) Let $\mathbb{W} \subset \mathbb{R}^{n}$ be any linear subspace. Show that there is one and only one vector $\hat{\boldsymbol{x}} \in \mathbb{W}$ so that
$$
\boldsymbol{w}^{T} \boldsymbol{A}^{T} \boldsymbol{A} \hat{\boldsymbol{x}}=\boldsymbol{w}^{T} \boldsymbol{A}^{T} \boldsymbol{b}, \quad \text { for all } \boldsymbol{w} \in \mathbb{W},
$$
and that $\hat{\boldsymbol{x}}$ satisfies
$$
\|\boldsymbol{b}-\boldsymbol{A} \hat{\boldsymbol{x}}\|_{2} \leq\|\boldsymbol{b}-\boldsymbol{A} \boldsymbol{w}\|_{2}, \quad \text { for all } \boldsymbol{w} \in \mathbb{W} .
$$
c) In the rest of this problem we consider the situation above, but where the vector space $\mathbb{W}$ is taken to be the Krylov space
$$
\mathbb{W}_{k}:=\operatorname{span}\left(\boldsymbol{b}, \boldsymbol{A} \boldsymbol{b}, \ldots, \boldsymbol{A}^{k-1} \boldsymbol{b}\right) .
$$
We use the inner product in $\mathbb{R}^{n}$ given by
$$
\langle\boldsymbol{v}, \boldsymbol{w}\rangle_{\boldsymbol{A}}:=\boldsymbol{v}^{T} \boldsymbol{A}^{T} \boldsymbol{A} \boldsymbol{w}, \quad \boldsymbol{v}, \boldsymbol{w} \in \mathbb{R}^{n} .
$$
[^25]The associated approximations of $\boldsymbol{x}$, corresponding to $\hat{\boldsymbol{x}}$ in $\mathbb{W}_{k}$, are then denoted $\boldsymbol{x}_{k}$. Assume that $\boldsymbol{x}_{k} \in \mathbb{W}_{k}$ is already determined. In addition, assume that we already have computed a "search direction" $\boldsymbol{p}_{k} \in \mathbb{W}_{k+1}$ such that $\left\|\boldsymbol{A} \boldsymbol{p}_{k}\right\|_{2}=$ $\left\|\boldsymbol{p}_{k}\right\|_{\boldsymbol{A}}=1$, and such that

$$
\left\langle\boldsymbol{p}_{k}, \boldsymbol{w}\right\rangle_{\boldsymbol{A}}=0, \quad \text { for all } \boldsymbol{w} \in \mathbb{W}_{k} .
$$

Show that $\boldsymbol{x}_{k+1}=\boldsymbol{x}_{k}+\alpha_{k} \boldsymbol{p}_{k}$ for a suitable $\alpha_{k} \in \mathbb{R}$, and express $\alpha_{k}$ in terms of the residual $\boldsymbol{r}_{k}:=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}$, and $\boldsymbol{p}_{k}$.

d) Assume that $\boldsymbol{A}$ is symmetric, but not necessarily positive definite. Assume further that the vectors $\boldsymbol{p}_{k-2}, \boldsymbol{p}_{k-1}$, and $\boldsymbol{p}_{k}$ are already known with properties as above. Show that
$$
\boldsymbol{A} \boldsymbol{p}_{k-1} \in \operatorname{span}\left(\boldsymbol{p}_{k-2}, \boldsymbol{p}_{k-1}, \boldsymbol{p}_{k}\right) .
$$
Use this to suggest how the search vectors $\boldsymbol{p}_{k}$ can be computed recursively.

### 13.7.3 Exercises Sect. 13.3

Exercise 13.12 (Krylov Space and cg Iterations) Consider the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$ where

$$
\boldsymbol{A}=\left[\begin{array}{rrr}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 2
\end{array}\right], \quad \text { and } \quad \boldsymbol{b}=\left[\begin{array}{l}
4 \\
0 \\
0
\end{array}\right] .
$$

a) Determine the vectors defining the Krylov spaces for $k \leq 3$ taking as initial approximation $\boldsymbol{x}=\mathbf{0}$. Answer: $\left[\boldsymbol{b}, \boldsymbol{A} \boldsymbol{b}, \boldsymbol{A}^{2} \boldsymbol{b}\right]=\left[\begin{array}{rrr}4 & 8 & 20 \\ 0 & -4 & -16 \\ 0 & 0 & 4\end{array}\right]$.
b) Carry out three CG-iterations on $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. Answer:
$$
\begin{aligned}
& {\left[\boldsymbol{x}_{0}, \boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \boldsymbol{x}_{3}\right]=\left[\begin{array}{rrrr}
0 & 2 & 8 / 3 & 3 \\
0 & 0 & 4 / 3 & 2 \\
0 & 0 & 0 & 1
\end{array}\right],} \\
& {\left[\boldsymbol{r}_{0}, \boldsymbol{r}_{1}, \boldsymbol{r}_{2}, \boldsymbol{r}_{3}\right]=\left[\begin{array}{rrrr}
4 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 4 / 3 & 0
\end{array}\right],}
\end{aligned}
$$

$$
\begin{aligned}
{\left[\boldsymbol{A} \boldsymbol{p}_{0}, \boldsymbol{A} \boldsymbol{p}_{1}, \boldsymbol{A} \boldsymbol{p}_{2}\right] } & =\left[\begin{array}{rcr}
8 & 0 & 0 \\
-4 & 3 & 0 \\
0 & -2 & 16 / 9
\end{array}\right], \\
{\left[\boldsymbol{p}_{0}, \boldsymbol{p}_{1}, \boldsymbol{p}_{2}, \boldsymbol{p}_{3}\right] } & =\left[\begin{array}{rrrr}
4 & 1 & 4 / 9 & 0 \\
0 & 2 & 8 / 9 & 0 \\
0 & 0 & 12 / 9 & 0
\end{array}\right],
\end{aligned}
$$

c) Verify that


- $\operatorname{dim}\left(\mathbb{W}_{k}\right)=k$ for $k=0,1,2,3$.
- $\boldsymbol{x}_{3}$ is the exact solution of $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$.
- $\boldsymbol{r}_{0}, \ldots, \boldsymbol{r}_{k-1}$ is an orthogonal basis for $\mathbb{W}_{k}$ for $k=1,2,3$.
- $\boldsymbol{p}_{0}, \ldots, \boldsymbol{p}_{k-1}$ is an $\boldsymbol{A}$-orthogonal basis for $\mathbb{W}_{k}$ for $k=1,2,3$.
- $\left\{\left\|\boldsymbol{r}_{k}\right\|\right.$ is monotonically decreasing.
- $\left\{\left\|\boldsymbol{x}_{k}-\boldsymbol{x}\right\|\right.$ is monotonically decreasing.

Exercise 13.13 (Antisymmetric System (Exam Exercise 1983-3)) In this and the next exercise $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\boldsymbol{x}^{T} \boldsymbol{y}$ is the usual inner product in $\mathbb{R}^{n}$. We note that

$$
\begin{aligned}
\langle\boldsymbol{x}, \boldsymbol{y}\rangle & =\langle\boldsymbol{y}, \boldsymbol{x}\rangle, \quad \boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}, \\
\langle\boldsymbol{C} \boldsymbol{x}, \boldsymbol{y}\rangle & =\left\langle\boldsymbol{y}, \boldsymbol{C}^{T} \boldsymbol{x}\right\rangle \stackrel{(13.61)}{=}\left\langle\boldsymbol{C}^{T} \boldsymbol{x}, \boldsymbol{y}\right\rangle, \quad \boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{n}, \boldsymbol{C} \in \mathbb{R}^{n \times n} .
\end{aligned}
$$

Let $\boldsymbol{B} \in \mathbb{R}^{n \times n}$ be an antisymmetric matrix, i.e., $\boldsymbol{B}^{T}=-\boldsymbol{B}$, and let $\boldsymbol{A}:=\boldsymbol{I}-\boldsymbol{B}$, where $\boldsymbol{I}$ is the unit matrix in $\mathbb{R}^{n}$.

a) Show that
$$
\begin{aligned}
& \langle\boldsymbol{B} \boldsymbol{x}, \boldsymbol{x}\rangle=0, \quad \boldsymbol{x} \in \mathbb{R}^{n}, \\
& \langle\boldsymbol{A} \boldsymbol{x}, \boldsymbol{x}\rangle=\langle\boldsymbol{x}, \boldsymbol{x}\rangle=\|\boldsymbol{x}\|_{2}^{2} .
\end{aligned}
$$
b) Show that $\|\boldsymbol{A} \boldsymbol{x}\|_{2}^{2}=\|\boldsymbol{x}\|_{2}^{2}+\|\boldsymbol{B} \boldsymbol{x}\|_{2}^{2}$ and that $\|\boldsymbol{A}\|_{2}=\sqrt{1+\|\boldsymbol{B}\|_{2}^{2}}$.
c) Show that $\boldsymbol{A}$ is nonsingular,
$$
\left\|\boldsymbol{A}^{-1}\right\|_{2}=\max _{\boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{x}\|_{2}}{\|\boldsymbol{A} \boldsymbol{x}\|_{2}},
$$
and $\|\boldsymbol{A}\|_{2} \leq 1$.
d) Let $1 \leq k \leq n, \mathcal{W}=\operatorname{span}\left(\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{k}\right)$ a $k$-dimensional subspace of $\mathbb{R}^{n}$ and $\boldsymbol{b} \in \mathbb{R}^{n}$. Show that if $\boldsymbol{x} \in \mathcal{W}$ is such that
$$
\langle\boldsymbol{A} \boldsymbol{x}, \boldsymbol{w}\rangle=\langle\boldsymbol{b}, \boldsymbol{w}\rangle \text { for all } \boldsymbol{w} \in \mathcal{W},
$$
then $\|\boldsymbol{x}\|_{2} \leq\|\boldsymbol{b}\|_{2}$.

With $\boldsymbol{x}:=\sum_{j=1}^{k} x_{j} \boldsymbol{w}_{j}$ the problem (13.65) is equivalent to finding real numbers $x_{1}, \ldots, x_{k}$ solving the linear system

$$
\sum_{j=1}^{k} x_{j}\left\langle\boldsymbol{A} \boldsymbol{w}_{j}, \boldsymbol{w}_{i}\right\rangle=\left\langle\boldsymbol{b}, \boldsymbol{w}_{i}\right\rangle, \quad i=1, \ldots, k
$$

Show that (13.65) has a unique solution $\boldsymbol{x} \in \mathcal{W}$.

e) Let $\boldsymbol{x}^{*}:=\boldsymbol{A}^{-1} \boldsymbol{b}$. Show that
$$
\left\|\boldsymbol{x}^{*}-\boldsymbol{x}\right\|_{2} \leq\|\boldsymbol{A}\|_{2} \min _{\boldsymbol{w} \in \mathcal{W}}\left\|\boldsymbol{x}^{*}-\boldsymbol{w}\right\|_{2} .
$$

Exercise 13.14 (cg Antisymmetric System (Exam Exercise 1983-4)) (It is recommended to study Exercise 13.13 before starting this exercise.) As in Exercise 13.13 let $\boldsymbol{B} \in \mathbb{R}^{n \times n}$ be an antisymmetric matrix, i.e., $\boldsymbol{B}^{T}=-\boldsymbol{B}$, let $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=\boldsymbol{x}^{T} \boldsymbol{y}$ be the usual inner product in $\mathbb{R}^{n}$, let $\boldsymbol{A}:=\boldsymbol{I}-\boldsymbol{B}$, where $\boldsymbol{I}$ is the unit matrix in $\mathbb{R}^{n}$ and $\boldsymbol{b} \in \mathbb{R}^{n}$. The purpose of this exercise is to develop an iterative algorithm for the linear system $\boldsymbol{A} \boldsymbol{x}=\boldsymbol{b}$. The algorithm is partly built on the same idea as for the conjugate gradient method for positive definite systems.

Let $\boldsymbol{x}_{0}=0$ be the initial approximation to the exact solution $\boldsymbol{x}^{*}:=\boldsymbol{A}^{-1} \boldsymbol{b}$. For $k=1,2, \ldots, n$ we let

$$
\mathcal{W}_{k}:=\operatorname{span}\left(\boldsymbol{b}, \boldsymbol{B} \boldsymbol{b}, \ldots, \boldsymbol{B}^{k-1} \boldsymbol{b}\right) .
$$

For $k=1,2, \ldots, n$ we define $\boldsymbol{x}_{k} \in \mathcal{W}_{k}$ by

$$
\left\langle\boldsymbol{A} \boldsymbol{x}_{k}, \boldsymbol{w}\right\rangle=\langle\boldsymbol{b}, \boldsymbol{w}\rangle, \text { for all } \boldsymbol{w} \in \mathcal{W}_{k} .
$$

The vector $\boldsymbol{x}_{k}$ is uniquely determined as shown in Exercise 13.13d) and that it is a "good" approximation to $\boldsymbol{x} *$ follows from (13.67). In this exercise we will derive a recursive algorithm to determine $\boldsymbol{x}_{k}$.

For $k=0, \ldots, n$ we set

$$
\boldsymbol{r}_{k}:=\boldsymbol{b}-\boldsymbol{A} \boldsymbol{x}_{k}, \text { and } \rho_{k}:=\left\|\boldsymbol{r}_{k}\right\|_{2}^{2} .
$$

Let $m \in \mathbb{N}$ be such that

$$
\rho_{k} \neq 0, \quad k=0, \ldots, m .
$$

Let $\omega_{0}, \omega_{1}, \ldots, \omega_{m}$ be real numbers defined recursively for $k=1,2, \ldots, m$ by

$$
\omega_{k}:= \begin{cases}1, & \text { if } k=0 \\ \left(1+\omega_{k-1}^{-1} \rho_{k} / \rho_{k-1}\right)^{-1}, & \text { otherwise. }\end{cases}
$$

We will show below that $\boldsymbol{x}_{k}$ and $\boldsymbol{r}_{k}$ satisfy the following recurrence relations for $k=0,1, \ldots, m-1$

$$
\begin{aligned}
& \boldsymbol{x}_{k+1}=\left(1-\omega_{k}\right) \boldsymbol{x}_{k-1}+\omega_{k}\left(\boldsymbol{x}_{k}+\boldsymbol{r}_{k}\right), \\
& \boldsymbol{r}_{k+1}=\left(1-\omega_{k}\right) \boldsymbol{r}_{k-1}+\omega_{k} \boldsymbol{B} \boldsymbol{r}_{k},
\end{aligned}
$$

starting with $\boldsymbol{x}_{0}=\boldsymbol{x}_{-1}=0$ and $\boldsymbol{r}_{0}=\boldsymbol{r}_{-1}=\boldsymbol{b}$.

a) Show that $0<\omega_{k}<1$ for $k=1,2, \ldots, m$.
b) Explain briefly how to define an iterative algorithm for determining $\boldsymbol{x}_{k}$ using the formulas (13.68), (13.69), (13.70) and estimate the number of arithmetic operations in each iteration.
c) Show that $\left\langle\boldsymbol{r}_{k}, \boldsymbol{r}_{j}\right\rangle=0$ for $j=0,1, \ldots, k-1$.
d) Show that if $k \leq m+1$ then $\mathcal{W}_{k}=\operatorname{span}\left(\boldsymbol{r}_{0}, \boldsymbol{r}_{1}, \ldots, \boldsymbol{r}_{k-1}\right)$ and $\operatorname{dim} \mathcal{W}_{k}=k$.
e) Show that if $1 \leq k \leq m-1$ then
$$
\boldsymbol{B} \boldsymbol{r}_{k}=\alpha_{k} \boldsymbol{r}_{k+1}+\beta_{k} \boldsymbol{r}_{k-1},
$$
where $\alpha_{k}:=\left\langle\boldsymbol{B r}_{k}, \boldsymbol{r}_{k+1}\right\rangle / \rho_{k+1}$ and $\beta_{k}:=\left\langle\boldsymbol{B r}_{k}, \boldsymbol{r}_{k-1}\right\rangle / \rho_{k-1}$.
f) Define $\alpha_{0}:=\left\langle\boldsymbol{B r}_{0}, \boldsymbol{r}_{1}\right\rangle / \rho_{1}$ and show that $\alpha_{0}=1$.
g) Show that if $1 \leq k \leq m-1$ then $\beta_{k}=-\alpha_{k-1} \rho_{k} / \rho_{k-1}$.
h) Show that ${ }^{5}$
$$
\left\langle\boldsymbol{r}_{k+1}, \boldsymbol{A}^{-1} \boldsymbol{r}_{k+1}\right\rangle=\left\langle\boldsymbol{r}_{k+1}, \boldsymbol{A}^{-1} \boldsymbol{r}_{j}\right\rangle, \quad j=0,1, \ldots, k .
$$
i) Use (13.71) and (13.72) to show that $\alpha_{k}+\beta_{k}=1$ for $k=1,2, \ldots, m-1$.
j) Show that $\alpha_{k} \geq 1$ for $k=1,2, \ldots, m-1$.
k) Show that $\boldsymbol{x}_{k}, \boldsymbol{r}_{k}$ and $\boldsymbol{\omega}_{k}$ satisfy the recurrence relations (13.68), (13.69) and (13.70).

### 13.7.4 Exercises Sect. 13.4

Exercise 13.15 (Another Explicit Formula for the Chebyshev Polynomial) Show that

$$
T_{n}(t)=\cosh (n \operatorname{arccosh} t) \text { for } t \geq 1,
$$

where $\operatorname{arccosh}$ is the inverse function of $\cosh x:=\left(e^{x}+e^{-x}\right) / 2$.

[^26]Exercise 13.16 (Maximum of a Convex Function) Show that if $f:[a, b] \rightarrow \mathbb{R}$ is convex then $\max _{a \leq x \leq b} f(x) \leq \max \{f(a), f(b)\}$.

### 13.7.5 Exercises Sect. 13.5

Exercise 13.17 (Variable Coefficient) For $m=2$, show that (13.57) takes the form

$$
\boldsymbol{A} \boldsymbol{x}=\left[\begin{array}{cccc}
a_{1,1} & -c_{\frac{3}{2}, 1} & -c_{1, \frac{3}{2}} & 0 \\
-c_{\frac{3}{2}, 1} & a_{2,2} & 0 & -c_{2, \frac{3}{2}} \\
-c_{1, \frac{3}{2}} & 0 & a_{3,3} & -c_{\frac{3}{2}, 2} \\
0 & -c_{2, \frac{3}{2}} & -c_{\frac{3}{2}, 2} & a_{4,4}
\end{array}\right]\left[\begin{array}{l}
v_{1,1} \\
v_{2,1} \\
v_{1,2} \\
v_{2,2}
\end{array}\right]=\left[\begin{array}{l}
(d v)_{1,1} \\
(d v)_{2,1} \\
(d v)_{1,2} \\
(d v)_{2,2}
\end{array}\right],
$$

where

$$
\left[\begin{array}{l}
a_{1,1} \\
a_{2,2} \\
a_{3,3} \\
a_{4,4}
\end{array}\right]=\left[\begin{array}{l}
c_{\frac{1}{2}, 1}+c_{1, \frac{1}{2}}+c_{1, \frac{3}{2}}+c_{\frac{3}{2}, 1} \\
c_{\frac{3}{2}, 1}+c_{2, \frac{1}{2}}+c_{2, \frac{3}{2}}+c_{\frac{5}{2}, 1} \\
c_{\frac{1}{2}, 2}+c_{1, \frac{3}{2}}+c_{1, \frac{5}{2}}+c_{\frac{3}{2}, 2} \\
c_{\frac{3}{2}, 2}+c_{2, \frac{3}{2}}+c_{2, \frac{5}{2}}+c_{\frac{5}{2}, 2}
\end{array}\right] .
$$

Show that the matrix $\boldsymbol{A}$ is symmetric, and if $c(x, y)>0$ for all $(x, y) \in \Omega$ then it is strictly diagonally dominant.

### 13.8 Review Questions

13.8.1 Does the steepest descent and conjugate gradient method always converge?
13.8.2 What kind of orthogonalities occur in the conjugate gradient method?
13.8.3 What is a Krylov space?
13.8.4 What is a convex function?
13.8.5 How do SOR and conjugate gradient compare?

## Part VI Eigenvalues and Eigenvectors

In this and the next chapter we briefly give some numerical methods for finding one or more eigenvalues and eigenvectors of a matrix. Both Hermitian and non hermitian matrices are considered.

But first we consider a location result for eigenvalues and then give a useful upper bound for how much an eigenvalue can change when the elements of the matrix is perturbed.

## Chapter 14 <br> Numerical Eigenvalue Problems

### 14.1 Eigenpairs

Consider the eigenpair problem for some classes of matrices $\boldsymbol{A} \in \mathbb{C}^{n \times n}$.
Diagonal Matrices The eigenpairs are easily determined. Since $\boldsymbol{A} \boldsymbol{e}_{i}=a_{i i} \boldsymbol{e}_{i}$ the eigenpairs are $\left(\lambda_{i}, \boldsymbol{e}_{i}\right)$, where $\lambda_{i}=a_{i i}$ for $i=1, \ldots, n$. Moreover, the eigenvectors of $\boldsymbol{A}$ are linearly independent.
Triangular Matrices Suppose $\boldsymbol{A}$ is upper or lower triangular. Consider finding the eigenvalues Since $\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=\prod_{i=1}^{n}\left(a_{i i}-\lambda\right)$ the eigenvalues are $\lambda_{i}=a_{i i}$ for $i=1, \ldots, n$, the diagonal elements of $\boldsymbol{A}$. To determine the eigenvectors can be more challenging since $\boldsymbol{A}$ can be defective, i.e., the eigenvectors are not necessarily linearly independent, cf. Chap. 6.
Block Diagonal Matrices Suppose

$$
\boldsymbol{A}=\operatorname{diag}\left(\boldsymbol{A}_{1}, \boldsymbol{A}_{2}, \ldots, \boldsymbol{A}_{r}\right), \quad \boldsymbol{A}_{i} \in \mathbb{C}^{m_{i} \times m_{i}} .
$$

Here the eigenpair problem reduces to $r$ smaller problems. Let $\boldsymbol{A}_{i} \boldsymbol{X}_{i}=\boldsymbol{X}_{i} \boldsymbol{D}_{i}$ define the eigenpairs of $\boldsymbol{A}_{i}$ for $i=1, \ldots, r$ and let $\boldsymbol{X}:=\operatorname{diag}\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{r}\right)$, $\boldsymbol{D}:=\operatorname{diag}\left(\boldsymbol{D}_{1}, \ldots, \boldsymbol{D}_{r}\right)$. Then the eigenpairs for $\boldsymbol{A}$ are given by

$$
\begin{aligned}
\boldsymbol{A} \boldsymbol{D} & =\operatorname{diag}\left(\boldsymbol{A}_{1}, \ldots, \boldsymbol{A}_{r}\right) \operatorname{diag}\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{r}\right)=\operatorname{diag}\left(\boldsymbol{A}_{1} \boldsymbol{X}_{1}, \ldots, \boldsymbol{A}_{r} \boldsymbol{X}_{r}\right) \\
& =\operatorname{diag}\left(\boldsymbol{X}_{1} \boldsymbol{D}_{1}, \ldots, \boldsymbol{X}_{r} \boldsymbol{D}_{r}\right)=\boldsymbol{X} \boldsymbol{D} .
\end{aligned}
$$

Block Triangular matrices Matrices Let
$\boldsymbol{A}_{11}, \boldsymbol{A}_{22}, \ldots, \boldsymbol{A}_{r r}$ be the diagonal blocks of $\boldsymbol{A}$. By Property 8. of determinants

$$
\operatorname{det}(\boldsymbol{A}-\lambda \boldsymbol{I})=\prod_{i=1}^{r} \operatorname{det}\left(\boldsymbol{A}_{i i}-\lambda \boldsymbol{I}\right)
$$

and the eigenvalues are found from the eigenvalues of the diagonal blocks.
In this and the next chapter we consider some numerical methods for finding one or more of the eigenvalues and eigenvectors of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Maybe the first method which comes to mind is to form the characteristic polynomial $\pi_{\boldsymbol{A}}$ of $\boldsymbol{A}$, and then use a polynomial root finder, like Newton's method to determine one or several of the eigenvalues.

It turns out that this is not suitable as an all purpose method. One reason is that a small change in one of the coefficients of $\pi_{\boldsymbol{A}}(\lambda)$ can lead to a large change in the roots of the polynomial. For example, if $\left.\pi_{\boldsymbol{A}}(\lambda):\right)=\lambda^{16}$ and $q(\lambda)=\lambda^{16}-10^{-16}$ then the roots of $\pi_{\boldsymbol{A}}$ are all equal to zero, while the roots of $q$ are $\lambda_{j}=10^{-1} e^{2 \pi i j / 16}$, $j=1, \ldots, 16$. The roots of $q$ have absolute value 0.1 and a perturbation in one of the polynomial coefficients of magnitude $10^{-16}$ has led to an error in the roots of approximately 0.1. The situation can be somewhat remedied by representing the polynomials using a different basis.

In this text we will only consider methods which work directly with the matrix. But before that, in Sect. 14.3 we consider how much the eigenvalues change when the elements in the matrix are perturbed. We start with a simple but useful result for locating the eigenvalues.

### 14.2 Gershgorin's Theorem

The following theorem is useful for locating eigenvalues of an arbitrary square matrix.

Theorem 14.1 (Gershgorin's Circle Theorem) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Define for $i=1,2, \ldots, n$

$$
\begin{gathered}
R_{i}=\left\{z \in \mathbb{C}:\left|z-a_{i i}\right| \leq r_{i}\right\}, \quad r_{i}:=\sum_{\substack{j=1 \\
j \neq i}}^{n}\left|a_{i j}\right|, \\
C_{j}=\left\{z \in \mathbb{C}:\left|z-a_{j j}\right| \leq c_{j}\right\}, \quad c_{j}:=\sum_{\substack{i=1 \\
i \neq j}}^{n}\left|a_{i j}\right| .
\end{gathered}
$$

Fig. 14.1 The Gershgorin disk $R_{i}$
![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-328.jpg?height=308&width=484&top_left_y=213&top_left_x=853)

Then any eigenvalue of $\boldsymbol{A}$ lies in $R \cap C$ where $R=R_{1} \cup R_{2} \cup \cdots \cup R_{n}$ and $C=C_{1} \cup C_{2} \cup \cdots \cup C_{n}$.

Proof Suppose $(\lambda, \boldsymbol{x})$ is an eigenpair for $\boldsymbol{A}$. We claim that $\lambda \in R_{i}$, where $i$ is such that $\left|x_{i}\right|=\|\boldsymbol{x}\|_{\infty}$. Indeed, $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ implies that $\sum_{j} a_{i j} x_{j}=\lambda x_{i}$ or $\left(\lambda-a_{i i}\right) x_{i}=$ $\sum_{j \neq i} a_{i j} x_{j}$. Dividing by $x_{i}$ and taking absolute values we find

$$
\left|\lambda-a_{i i}\right|=\left|\sum_{j \neq i} a_{i j} x_{j} / x_{i}\right| \leq \sum_{j \neq i}\left|a_{i j}\right|\left|x_{j} / x_{i}\right| \leq r_{i}
$$

since $\left|x_{j} / x_{i}\right| \leq 1$ for all $j$. Thus $\lambda \in R_{i}$.
Since $\lambda$ is also an eigenvalue of $\boldsymbol{A}^{T}$, it must be in one of the row disks of $\boldsymbol{A}^{T}$. But these are the column disks $C_{j}$ of $\boldsymbol{A}$. Hence $\lambda \in C_{j}$ for some $j$. $\square$

The set $R_{i}$ is a subset of the complex plane consisting of all points inside a circle with center at $a_{i i}$ and radius $r_{i}$, c.f. Fig. 14.1. $R_{i}$ is called a (Gerschgorin) row disk.

An eigenvalue $\lambda$ lies in the union of the row disks $R_{1}, \ldots, R_{n}$ and also in the union of the column disks $C_{1}, \ldots, C_{n}$. If $\boldsymbol{A}$ is Hermitian then $R_{i}=C_{i}$ for $i=$ $1,2, \ldots, n$. Moreover, in this case the eigenvalues of $\boldsymbol{A}$ are real, and the Gerschgorin disks can be taken to be intervals on the real line.

Example 14.1 (Gershgorin) Let $\boldsymbol{T}=\operatorname{tridiag}(-1,2,-1) \in \mathbb{R}^{m \times m}$ be the second derivative matrix. Since $\boldsymbol{A}$ is Hermitian we have $R_{i}=C_{i}$ for all $i$ and the eigenvalues are real. We find $R_{1}=R_{m}=\{z \in \mathbb{R}:|z-2| \leq 1\}$ and

$$
R_{i}=\{z \in \mathbb{R}:|z-2| \leq 2\}, \quad i=2,3, \ldots, m-1 .
$$

We conclude that $\lambda \in[0,4]$ for any eigenvalue $\lambda$ of $\boldsymbol{T}$. To check this, we recall that by Lemma 2.2 the eigenvalues of $\boldsymbol{T}$ are given by

$$
\lambda_{j}=4\left[\sin \frac{j \pi}{2(m+1)}\right]^{2}, \quad j=1,2, \ldots, m .
$$

When $m$ is large the smallest eigenvalue $4\left[\sin \frac{\pi}{2(m+1)}\right]^{2}$ is very close to zero and the largest eigenvalue $4\left[\sin \frac{m \pi}{2(m+1)}\right]^{2}$ is very close to 4 . Thus Gerschgorin's theorem gives a remarkably good estimate for large $m$.

Sometimes some of the Gerschgorin disks are distinct and we have
Corollary 14.1 (Disjoint Gershgorin Disks) If $p$ of the Gershgorin row disks are disjoint from the others, the union of these disks contains precisely $p$ eigenvalues. The same result holds for the column disks.

Proof Consider a family of matrices

$$
\boldsymbol{A}(t):=\boldsymbol{D}+t(\boldsymbol{A}-\boldsymbol{D}), \quad \boldsymbol{D}:=\operatorname{diag}\left(a_{11}, \ldots, a_{n n}\right), \quad t \in[0,1] .
$$

We have $\boldsymbol{A}(0)=\boldsymbol{D}$ and $\boldsymbol{A}(1)=\boldsymbol{A}$. As a function of $t$, every eigenvalue of $\boldsymbol{A}(t)$ is a continuous function of $t$. This follows from Theorem 14.2, see Exercise 14.5. The row disks $R_{i}(t)$ of $\boldsymbol{A}(t)$ have radius proportional to $t$, indeed

$$
R_{i}(t)=\left\{z \in \mathbb{C}:\left|z-a_{i i}\right| \leq t r_{i}\right\}, \quad r_{i}:=\sum_{\substack{j=1 \\ j \neq i}}^{n}\left|a_{i j}\right| .
$$

Clearly $0 \leq t_{1}<t_{2} \leq 1$ implies $R_{i}\left(t_{1}\right) \subset R_{i}\left(t_{2}\right)$ and $R_{i}(1)$ is a row disk of $\boldsymbol{A}$ for all $i$. Suppose $\bigcup_{k=1}^{p} R_{i_{k}}(1)$ are disjoint from the other disks of $\boldsymbol{A}$ and set $R^{p}(t):=\bigcup_{k=1}^{p} R_{i_{k}}(t)$ for $t \in[0,1]$. Now $R^{p}(0)$ contains only the $p$ eigenvalues $a_{i_{1}, i_{1}}, \ldots, a_{i_{p}, i_{p}}$ of $\boldsymbol{A}(0)=\boldsymbol{D}$. As $t$ increases from zero to one the set $R^{p}(t)$ is disjoint from the other row disks of $\boldsymbol{A}$ and by the continuity of the eigenvalues cannot loose or gain eigenvalues. It follows that $R^{p}(1)$ must contain $p$ eigenvalues of $\boldsymbol{A}$. $\square$

Example 14.2 Consider the matrix $\boldsymbol{A}=\left[\begin{array}{ccc}1 & \epsilon_{1} & \epsilon_{2} \\ \epsilon_{3} & 2 & \epsilon_{4} \\ \epsilon_{5} & \epsilon_{6} & 3\end{array}\right]$, where $\left|\epsilon_{i}\right| \leq 10^{-15}$ all $i$. By Corollary 14.1 the eigenvalues $\lambda_{1}, \lambda_{2}, \lambda_{3}$ of $\boldsymbol{A}$ are distinct and satisfy $\left|\lambda_{j}-j\right| \leq$ $2 \times 10^{-15}$ for $j=1,2,3$.

### 14.3 Perturbation of Eigenvalues

In this section we study the following problem. Given matrices $\boldsymbol{A}, \boldsymbol{E} \in \mathbb{C}^{n \times n}$, where we think of $\boldsymbol{E}$ as a perturbation of $\boldsymbol{A}$. By how much do the eigenvalues of $\boldsymbol{A}$ and $\boldsymbol{A}+$ $\boldsymbol{E}$ differ? Not surprisingly this problem is more complicated than the corresponding problem for linear systems.

We illustrate this by considering two examples. Suppose $\boldsymbol{A}_{0}:=\mathbf{0}$ is the zero matrix. If $\lambda \in \sigma\left(\boldsymbol{A}_{0}+\boldsymbol{E}\right)=\sigma(\boldsymbol{E})$, then $|\lambda| \leq\|\boldsymbol{E}\|_{\infty}$ by Theorem 12.11, and any
zero eigenvalue of $\boldsymbol{A}_{0}$ is perturbed by at most $\|\boldsymbol{E}\|_{\infty}$. On the other hand consider for $\epsilon>0$ the matrices

$$
\boldsymbol{A}_{1}:=\left[\begin{array}{cccccc}
0 & 1 & 0 & \cdots & 0 & 0 \\
0 & 0 & 1 & \cdots & 0 & 0 \\
\vdots & \vdots & \vdots & & \vdots & \vdots \\
0 & 0 & 0 & \cdots & 0 & 1 \\
0 & 0 & 0 & \cdots & 0 & 0
\end{array}\right], \quad \boldsymbol{E}:=\left[\begin{array}{cccccc}
0 & 0 & 0 & \cdots & 0 & 0 \\
0 & 0 & 0 & \cdots & 0 & 0 \\
\vdots & \vdots & \vdots & & \vdots & \vdots \\
0 & 0 & 0 & \cdots & 0 & 0 \\
\epsilon & 0 & 0 & \cdots & 0 & 0
\end{array}\right]=\epsilon \boldsymbol{e}_{n} \boldsymbol{e}_{1}^{T} .
$$

The characteristic polynomial of $\boldsymbol{A}_{1}+\boldsymbol{E}$ is $\pi(\lambda):=(-1)^{n}\left(\lambda^{n}-\epsilon\right)$, and the zero eigenvalues of $\boldsymbol{A}_{1}$ are perturbed by the amount $|\lambda|=\|\boldsymbol{E}\|_{\infty}^{1 / n}$. Thus, for $n=16$, a perturbation of say $\epsilon=10^{-16}$ gives a change in eigenvalue of 0.1.

The following theorem shows that a dependence $\|\boldsymbol{E}\|_{\infty}^{1 / n}$ is the worst that can happen.

Theorem 14.2 (Elsner's Theorem (1985)) Suppose $\boldsymbol{A}, \boldsymbol{E} \in \mathbb{C}^{n \times n}$. To every $\mu \in$ $\sigma(\boldsymbol{A}+\boldsymbol{E})$ there is a $\lambda \in \sigma(\boldsymbol{A})$ such that

$$
|\mu-\lambda| \leq K\|E\|_{2}^{1 / n}, \quad K=\left(\|A\|_{2}+\|A+E\|_{2}\right)^{1-1 / n} .
$$

Proof Suppose $\boldsymbol{A}$ has eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$ and let $\lambda_{1}$ be one which is closest to $\mu$. Let $\boldsymbol{u}_{1}$ with $\left\|\boldsymbol{u}_{1}\right\|_{2}=1$ be an eigenvector corresponding to $\mu$, and extend $\boldsymbol{u}_{1}$ to an orthonormal basis $\left\{\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{n}\right\}$ of $\mathbb{C}^{n}$. Note that

$$
\begin{gathered}
\left\|(\mu \boldsymbol{I}-\boldsymbol{A}) \boldsymbol{u}_{1}\right\|_{2}=\left\|(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{u}_{1}-\boldsymbol{A} \boldsymbol{u}_{1}\right\|_{2}=\left\|\boldsymbol{E} \boldsymbol{u}_{1}\right\|_{2} \leq\|\boldsymbol{E}\|_{2}, \\
\prod_{j=2}^{n}\left\|(\mu \boldsymbol{I}-\boldsymbol{A}) \boldsymbol{u}_{j}\right\|_{2} \leq \prod_{j=2}^{n}\left(|\mu|+\left\|\boldsymbol{A} \boldsymbol{u}_{j}\right\|_{2}\right) \leq\left(\|(\boldsymbol{A}+\boldsymbol{E})\|_{2}+\|\boldsymbol{A}\|_{2}\right)^{n-1} .
\end{gathered}
$$

Using this and Hadamard's inequality (5.21) we find

$$
\begin{aligned}
& \left|\mu-\lambda_{1}\right|^{n} \leq \prod_{j=1}^{n}\left|\mu-\lambda_{j}\right|=|\operatorname{det}(\mu \boldsymbol{I}-\boldsymbol{A})|=\left|\operatorname{det}\left((\mu \boldsymbol{I}-\boldsymbol{A})\left[\boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{n}\right]\right)\right| \\
& \leq\left\|(\mu \boldsymbol{I}-\boldsymbol{A}) \boldsymbol{u}_{1}\right\|_{2} \prod_{j=2}^{n}\left\|(\mu \boldsymbol{I}-\boldsymbol{A}) \boldsymbol{u}_{j}\right\|_{2} \leq\|\boldsymbol{E}\|_{2}\left(\|(\boldsymbol{A}+\boldsymbol{E})\|_{2}+\|\boldsymbol{A}\|_{2}\right)^{n-1} .
\end{aligned}
$$

The result follows by taking $n$th roots in this inequality. $\square$

It follows from this theorem that the eigenvalues depend continuously on the elements of the matrix. The factor $\|\boldsymbol{E}\|_{2}^{1 / n}$ shows that this dependence is almost, but not quite, differentiable. As an example, the eigenvalues of the matrix $\left[\begin{array}{cc}1 & 1 \\ \epsilon & 1\end{array}\right]$ are $1 \pm \sqrt{\epsilon}$ and these expressions are not differentiable at $\epsilon=0$.

### 14.3.1 Nondefective Matrices

Recall that a matrix is nondefective if the eigenvectors form a basis for $\mathbb{C}^{n}$. For nondefective matrices we can get rid of the annoying exponent $1 / n$ in $\|\boldsymbol{E}\|_{2}$ in (14.1). For a more general discussion than the one in the following theorem see [19].

Theorem 14.3 (Absolute Errors) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ has linearly independent eigenvectors $\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right\}$ and let $\boldsymbol{X}=\left[\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}\right]$ be the eigenvector matrix. To any $\mu \in \mathbb{C}$ and $\boldsymbol{x} \in \mathbb{C}^{n}$ with $\|\boldsymbol{x}\|_{p}=1$ we can find an eigenvalue $\lambda$ of $\boldsymbol{A}$ such that

$$
|\lambda-\mu| \leq K_{p}(\boldsymbol{X})\|\boldsymbol{r}\|_{p}, \quad 1 \leq p \leq \infty,
$$

where $\boldsymbol{r}:=\boldsymbol{A} \boldsymbol{x}-\mu \boldsymbol{x}$ and $K_{p}(\boldsymbol{X}):=\|\boldsymbol{X}\|_{p}\left\|\boldsymbol{X}^{-1}\right\|_{p}$. If for some $\boldsymbol{E} \in \mathbb{C}^{n \times n}$ it holds that $(\mu, \boldsymbol{x})$ is an eigenpair for $\boldsymbol{A}+\boldsymbol{E}$, then we can find an eigenvalue $\lambda$ of $\boldsymbol{A}$ such that

$$
|\lambda-\mu| \leq K_{p}(\boldsymbol{X})\|\boldsymbol{E}\|_{p}, \quad 1 \leq p \leq \infty,
$$

Proof If $\mu \in \sigma(\boldsymbol{A})$ then we can take $\lambda=\mu$ and (14.2), (14.3) hold trivially. So assume $\mu \notin \sigma(\boldsymbol{A})$. Since $\boldsymbol{A}$ is nondefective it can be diagonalized, we have $\boldsymbol{A}=$ $\boldsymbol{X} \boldsymbol{D} \boldsymbol{X}^{-1}$, where $\boldsymbol{D}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ and $\left(\lambda_{j}, \boldsymbol{x}_{j}\right)$ are the eigenpairs of $\boldsymbol{A}$ for $j=$ $1, \ldots, n$. Define $\boldsymbol{D}_{1}:=\boldsymbol{D}-\mu \boldsymbol{I}$. Then $\boldsymbol{D}_{1}^{-1}=\operatorname{diag}\left(\left(\lambda_{1}-\mu\right)^{-1}, \ldots,\left(\lambda_{n}-\mu\right)^{-1}\right)$ exists and

$$
\boldsymbol{X} \boldsymbol{D}_{1}^{-1} \boldsymbol{X}^{-1} \boldsymbol{r}=\left(\boldsymbol{X}(\boldsymbol{D}-\mu \boldsymbol{I}) \boldsymbol{X}^{-1}\right)^{-1} \boldsymbol{r}=(\boldsymbol{A}-\mu \boldsymbol{I})^{-1}(\boldsymbol{A}-\mu \boldsymbol{I}) \boldsymbol{x}=\boldsymbol{x} .
$$

Using this and Lemma 14.1 below we obtain

$$
1=\|\boldsymbol{x}\|_{p}=\left\|\boldsymbol{X} \boldsymbol{D}_{1}^{-1} \boldsymbol{X}^{-1} \boldsymbol{r}\right\|_{p} \leq\left\|\boldsymbol{D}_{1}^{-1}\right\|_{p} K_{p}(\boldsymbol{X})\|\boldsymbol{r}\|_{p}=\frac{K_{p}(\boldsymbol{X})\|\boldsymbol{r}\|_{p}}{\min _{j}\left|\lambda_{j}-\mu\right|} .
$$

But then (14.2) follows. If $(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{x}=\mu \boldsymbol{x}$ then $\mathbf{0}=\boldsymbol{A} \boldsymbol{x}-\mu \boldsymbol{x}+\boldsymbol{E} \boldsymbol{x}=\boldsymbol{r}+\boldsymbol{E} \boldsymbol{x}$. But then $\|\boldsymbol{r}\|_{p}=\|-\boldsymbol{E} \boldsymbol{x}\|_{p} \leq\|\boldsymbol{E}\|_{p}$. Inserting this in (14.2) proves (14.3). $\square$

The equation (14.3) shows that for a nondefective matrix the absolute error can be magnified by at most $K_{p}(\boldsymbol{X})$, the condition number of the eigenvector matrix with respect to inversion. If $K_{p}(\boldsymbol{X})$ is small then a small perturbation changes the eigenvalues by small amounts.

Even if we get rid of the exponent $1 / n$, the equation (14.3) illustrates that it can be difficult or sometimes impossible to compute accurate eigenvalues and eigenvectors of matrices with almost linearly dependent eigenvectors. On the other hand the eigenvalue problem for normal matrices is better conditioned. Indeed, if $\boldsymbol{A}$ is normal then it has a set of orthonormal eigenvectors and the eigenvector matrix is unitary. If
we restrict attention to the 2-norm then $K_{2}(\boldsymbol{X})=1$ and (14.3) implies the following result.

Theorem 14.4 (Perturbations, Normal Matrix) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is normal and let $\mu$ be an eigenvalue of $\boldsymbol{A}+\boldsymbol{E}$ for some $\boldsymbol{E} \in \mathbb{C}^{n \times n}$. Then we can find an eigenvalue $\lambda$ of $\boldsymbol{A}$ such that $|\lambda-\mu| \leq\|\boldsymbol{E}\|_{2}$.

For an even stronger result for Hermitian matrices see Corollary 6.13. We conclude that the situation for the absolute error in an eigenvalue of a Hermitian matrix is quite satisfactory. Small perturbations in the elements are not magnified in the eigenvalues.

In the proof of Theorem 14.3 we used that the $p$-norm of a diagonal matrix is equal to its spectral radius.

Lemma 14.1 ( $p$-Norm of a Diagonal Matrix) If $\boldsymbol{A}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ is a diagonal matrix then $\|\boldsymbol{A}\|_{p}=\rho(\boldsymbol{A})$ for $1 \leq p \leq \infty$.

Proof For $p=\infty$ the proof is left as an exercise. For any $\boldsymbol{x} \in \mathbb{C}^{n}$ and $p<\infty$ we have

$$
\|\boldsymbol{A} \boldsymbol{x}\|_{p}=\left\|\left[\lambda_{1} x_{1}, \ldots, \lambda_{n} x_{n}\right]^{T}\right\|_{p}=\left(\sum_{j=1}^{n}\left|\lambda_{j}\right|^{p}\left|x_{j}\right|^{p}\right)^{1 / p} \leq \rho(\boldsymbol{A})\|\boldsymbol{x}\|_{p} .
$$

Thus $\|\boldsymbol{A}\|_{p}=\max _{\boldsymbol{x} \neq \mathbf{0}} \frac{\|\boldsymbol{A}\|_{p}}{\|\boldsymbol{x}\|_{p}} \leq \rho(\boldsymbol{A})$. But from Theorem 12.11 we have $\rho(\boldsymbol{A}) \leq$ $\|\boldsymbol{A}\|_{p}$ and the proof is complete. $\square$

For the accuracy of an eigenvalue of small magnitude we are interested in the size of the relative error.

Theorem 14.5 (Relative Errors) Suppose in Theorem 14.3 that $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is nonsingular. To any $\mu \in \mathbb{C}$ and $\boldsymbol{x} \in \mathbb{C}^{n}$ with $\|\boldsymbol{x}\|_{p}=1$, we can find an eigenvalue $\lambda$ of $\boldsymbol{A}$ such that

$$
\frac{|\lambda-\mu|}{|\lambda|} \leq K_{p}(\boldsymbol{X}) K_{p}(\boldsymbol{A}) \frac{\|\boldsymbol{r}\|_{p}}{\|\boldsymbol{A}\|_{p}}, \quad 1 \leq p \leq \infty,
$$

where $\boldsymbol{r}:=\boldsymbol{A} \boldsymbol{x}-\mu \boldsymbol{x}$. If for some $\boldsymbol{E} \in \mathbb{C}^{n \times n}$ it holds that ( $\mu, \boldsymbol{x}$ ) is an eigenpair for $\boldsymbol{A}+\boldsymbol{E}$, then we can find an eigenvalue $\lambda$ of $\boldsymbol{A}$ such that

$$
\frac{|\lambda-\mu|}{|\lambda|} \leq K_{p}(\boldsymbol{X})\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\|_{p} \leq K_{p}(\boldsymbol{X}) K_{p}(\boldsymbol{A}) \frac{\|\boldsymbol{E}\|_{p}}{\|\boldsymbol{A}\|_{p}}, \quad 1 \leq p \leq \infty,
$$

Proof Applying Theorem 12.11 to $\boldsymbol{A}^{-1}$ we have for any $\lambda \in \sigma(\boldsymbol{A})$

$$
\frac{1}{\lambda} \leq\left\|\boldsymbol{A}^{-1}\right\|_{p}=\frac{K_{p}(\boldsymbol{A})}{\|\boldsymbol{A}\|_{p}}
$$

and (14.4) follows from (14.2). To prove (14.5) we define the matrices $\boldsymbol{B}:=\mu \boldsymbol{A}^{-1}$ and $\boldsymbol{F}:=-\boldsymbol{A}^{-1} \boldsymbol{E}$. If $\left(\lambda_{j}, \boldsymbol{x}\right)$ are the eigenpairs for $\boldsymbol{A}$ then $\left(\frac{\mu}{\lambda_{j}}, \boldsymbol{x}\right)$ are the eigenpairs for $\boldsymbol{B}$ for $j=1, \ldots, n$. Since ( $\mu, \boldsymbol{x}$ ) is an eigenpair for $\boldsymbol{A}+\boldsymbol{E}$ we find

$$
(\boldsymbol{B}+\boldsymbol{F}-\boldsymbol{I}) \boldsymbol{x}=\left(\mu \boldsymbol{A}^{-1}-\boldsymbol{A}^{-1} \boldsymbol{E}-\boldsymbol{I}\right) \boldsymbol{x}=\boldsymbol{A}^{-1}(\mu \boldsymbol{I}-(\boldsymbol{E}+\boldsymbol{A})) \boldsymbol{x}=\mathbf{0} .
$$

Thus $(1, \boldsymbol{x})$ is an eigenpair for $\boldsymbol{B}+\boldsymbol{F}$. Applying Theorem 14.3 to this eigenvalue we can find $\lambda \in \sigma(\boldsymbol{A})$ such that $\left|\frac{\mu}{\lambda}-1\right| \leq K_{p}(\boldsymbol{X})\|\boldsymbol{F}\|_{p}=K_{p}(\boldsymbol{X})\left\|\boldsymbol{A}^{-1} \boldsymbol{E}\right\|_{p}$ which proves the first estimate in (14.5). The second inequality in (14.5) follows from the submultiplicativity of the $p$-norm. $\square$

### 14.4 Unitary Similarity Transformation of a Matrix into Upper Hessenberg Form

Before attempting to find eigenvalues and eigenvectors of a matrix (exceptions are made for certain sparse matrices), it is often advantageous to reduce it by similarity transformations to a simpler form. Orthogonal or unitary similarity transformations are particularly important since they are insensitive to round-off errors in the elements of the matrix. In this section we show how this reduction can be carried out.

Recall that a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is upper Hessenberg if $a_{i, j}=0$ for $j=$ $1,2, \ldots, i-2, i=3,4, \ldots, n$. We will reduce $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ to upper Hessenberg form by unitary similarity transformations. Let $\boldsymbol{A}_{1}=\boldsymbol{A}$ and define $\boldsymbol{A}_{k+1}=\boldsymbol{H}_{k} \boldsymbol{A}_{k} \boldsymbol{H}_{k}$ for $k=1,2, \ldots, n-2$. Here $\boldsymbol{H}_{k}$ is a Householder transformation chosen to introduce zeros in the elements of column $k$ of $\boldsymbol{A}_{k}$ under the subdiagonal. The final matrix $\boldsymbol{A}_{n-1}$ will be upper Hessenberg. Householder transformations were used in Chap. 5 to reduce a matrix to upper triangular form. To preserve eigenvalues similarity transformations are needed and then the final matrix in the reduction cannot in general be upper triangular.

If $\boldsymbol{A}_{1}=\boldsymbol{A}$ is Hermitian, the matrix $\boldsymbol{A}_{n-1}$ will be Hermitian and tridiagonal. For if $\boldsymbol{A}_{k}^{*}=\boldsymbol{A}_{k}$ then

$$
\boldsymbol{A}_{k+1}^{*}=\left(\boldsymbol{H}_{k} \boldsymbol{A}_{k} \boldsymbol{H}_{k}\right)^{*}=\boldsymbol{H}_{k} \boldsymbol{A}_{k}^{*} \boldsymbol{H}_{k}=\boldsymbol{A}_{k+1} .
$$

Since $\boldsymbol{A}_{n-1}$ is upper Hessenberg and Hermitian, it must be tridiagonal.
To describe the reduction to upper Hessenberg or tridiagonal form in more detail we partition $\boldsymbol{A}_{k}$ as follows

$$
\boldsymbol{A}_{k}=\left[\begin{array}{ll}
\boldsymbol{B}_{k} & \boldsymbol{C}_{k} \\
\boldsymbol{D}_{k} & \boldsymbol{E}_{k}
\end{array}\right] .
$$

Suppose $\boldsymbol{B}_{k} \in \mathbb{C}^{k, k}$ is upper Hessenberg, and the first $k-1$ columns of $\boldsymbol{D}_{k} \in$ $\mathbb{C}^{n-k, k}$ are zero, i.e. $\boldsymbol{D}_{k}=\left[\mathbf{0}, \mathbf{0}, \ldots, \mathbf{0}, \boldsymbol{d}_{k}\right]$. Let $\boldsymbol{V}_{k}=\boldsymbol{I}-\boldsymbol{v}_{k} \boldsymbol{v}_{k}^{*} \in \mathbb{C}^{n-k, n-k}$ be a Householder transformation such that $\boldsymbol{V}_{k} \boldsymbol{d}_{k}=\alpha_{k} \boldsymbol{e}_{1}$. Define

$$
\boldsymbol{H}_{k}=\left[\begin{array}{cc}
\boldsymbol{I}_{k} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{V}_{k}
\end{array}\right] \in \mathbb{C}^{n \times n} .
$$

The matrix $\boldsymbol{H}_{k}$ is a Householder transformation, and we find

$$
\begin{aligned}
\boldsymbol{A}_{k+1} & =\boldsymbol{H}_{k} \boldsymbol{A}_{k} \boldsymbol{H}_{k}=\left[\begin{array}{cc}
\boldsymbol{I}_{k} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{V}_{k}
\end{array}\right]\left[\begin{array}{ll}
\boldsymbol{B}_{k} & \boldsymbol{C}_{k} \\
\boldsymbol{D}_{k} & \boldsymbol{E}_{k}
\end{array}\right]\left[\begin{array}{cc}
\boldsymbol{I}_{k} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{V}_{k}
\end{array}\right] \\
& =\left[\begin{array}{cc}
\boldsymbol{B}_{k} & \boldsymbol{C}_{k} \boldsymbol{V}_{k} \\
\boldsymbol{V}_{k} \boldsymbol{D}_{k} & \boldsymbol{V}_{k} \boldsymbol{E}_{k} \boldsymbol{V}_{k}
\end{array}\right] .
\end{aligned}
$$

Now $\boldsymbol{V}_{k} \boldsymbol{D}_{k}=\left[\boldsymbol{V}_{k} \mathbf{0}, \ldots, \boldsymbol{V}_{k} \mathbf{0}, \boldsymbol{V}_{k} \boldsymbol{d}_{k}\right]=\left(\mathbf{0}, \ldots, \mathbf{0}, \alpha_{k} \boldsymbol{e}_{1}\right)$. Moreover, the matrix $\boldsymbol{B}_{k}$ is not affected by the $\boldsymbol{H}_{k}$ transformation. Therefore the upper left $(k+1) \times(k+1)$ corner of $\boldsymbol{A}_{k+1}$ is upper Hessenberg and the reduction is carried one step further. The reduction stops with $\boldsymbol{A}_{n-1}$ which is upper Hessenberg.

To find $\boldsymbol{A}_{k+1}$ we use Algorithm 5.1 to find $\boldsymbol{v}_{k}$ and $\alpha_{k}$. We store $\boldsymbol{v}_{k}$ in the $k$ th column of a matrix $\boldsymbol{L}$ as $\boldsymbol{L}(k+1: n, k)=\boldsymbol{v}_{k}$. This leads to the following algorithm for reducing a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ to upper Hessenberg form using Householder transformations. The algorithm returns the reduced matrix $\boldsymbol{B} . \boldsymbol{B}$ is tridiagonal if $\boldsymbol{A}$ is symmetric. Details of the transformations are stored in a lower triangular matrix $\boldsymbol{L}$, also returned by the algorithm. The elements of $\boldsymbol{L}$ can be used to assemble a unitary matrix $\boldsymbol{Q}$ such that $\boldsymbol{B}=\boldsymbol{Q}^{*} \boldsymbol{A} \boldsymbol{Q}$. Algorithm 5.1 is used in each step of the reduction:

```
function [L,B] = hesshousegen(A)
n=length(A); L=zeros(n,n); B=A;
for k=1:n-2
    [v,B(k+1,k)]=housegen(B(k+1:n,k));
    L((k+1):n,k)=v; B((k+2):n,k)=zeros(n-k-1,1);
    C=B((k+1):n, (k+1):n);
    B ( (k+1) :n, (k+1) :n) =C-v* (v'*C) ;
    C=B(1:n, (k+1):n); B(1:n, (k+1):n)=C-(C*v)*v';
end
end
```

Listing 14.1 hesshousegen

### 14.4.1 Assembling Householder Transformations

We can use the output of Algorithm 14.1 to assemble the matrix $\boldsymbol{Q} \in \mathbb{R}^{n \times n}$ such that $\boldsymbol{Q}$ is orthogonal and $\boldsymbol{Q}^{*} \boldsymbol{A} \boldsymbol{Q}$ is upper Hessenberg. We need to compute the product $\boldsymbol{Q}=\boldsymbol{H}_{1} \boldsymbol{H}_{2} \cdots \boldsymbol{H}_{n-2}$, where $\boldsymbol{H}_{k}=\left[\begin{array}{cc}\boldsymbol{I} & \mathbf{0} \\ \mathbf{0} & \boldsymbol{I}-\boldsymbol{v}_{k} \boldsymbol{v}_{k}^{T}\end{array}\right]$ and $\boldsymbol{v}_{k} \in \mathbb{R}^{n-k}$. Since $\boldsymbol{v}_{1} \in \mathbb{R}^{n-1}$ and $\boldsymbol{v}_{n-2} \in \mathbb{R}^{2}$ it is most economical to assemble the product from right to left. We compute

$$
\boldsymbol{Q}_{n-1}=\boldsymbol{I} \text { and } \boldsymbol{Q}_{k}=\boldsymbol{H}_{k} \boldsymbol{Q}_{k+1} \text { for } k=n-2, n-3, \ldots, 1 .
$$

Suppose $\boldsymbol{Q}_{k+1}$ has the form $\left[\begin{array}{cc}\boldsymbol{I}_{k} & \mathbf{0} \\ \mathbf{0} & \boldsymbol{U}_{k}\end{array}\right]$, where $\boldsymbol{U}_{k} \in \mathbb{R}^{n-k, n-k}$. Then

$$
\boldsymbol{Q}_{k}=\left[\begin{array}{cc}
\boldsymbol{I}_{k} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{I}-\boldsymbol{v}_{k} \boldsymbol{v}_{k}^{T}
\end{array}\right] *\left[\begin{array}{cc}
\boldsymbol{I}_{k} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{U}_{k}
\end{array}\right]=\left[\begin{array}{cc}
\boldsymbol{I}_{k} & \mathbf{0} \\
\mathbf{0} & \boldsymbol{U}_{k}-\boldsymbol{v}_{k}\left(\boldsymbol{v}_{k}^{T} \boldsymbol{U}_{k}\right)
\end{array}\right] .
$$

This leads to the following algorithm for assembling Householder transformations. The algorithm assumes that L is output from Algorithm 14.1, and assembles an orthogonal matrix $\boldsymbol{Q}$ from the columns of $\boldsymbol{L}$ so that $\boldsymbol{Q}^{*} \boldsymbol{A} \boldsymbol{Q}$ is upper Hessenberg.

```
function Q = accumulateQ(L)
n=length(L); Q=eye(n);
for k=n-2:-1:1
    v=L((k+1):n,k); C=Q((k+1):n,(k+1):n);
    Q((k+1):n, (k+1):n)=C-v*(v'*C);
end
```

Listing 14.2 accumulateQ

### 14.5 Computing a Selected Eigenvalue of a Symmetric Matrix

Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be symmetric with eigenvalues $\lambda_{1} \geq \lambda_{2} \geq \cdots \geq \lambda_{n}$. In this section we consider a method to compute an approximation to the $m$ th eigenvalue $\lambda_{m}$ for some $1 \leq m \leq n$. Using Householder similarity transformations as outlined in the
previous section we can assume that $\boldsymbol{A}$ is symmetric and tridiagonal.

$$
\boldsymbol{A}=\left[\begin{array}{ccccc}
d_{1} & c_{1} & & & \\
c_{1} & d_{2} & c_{2} & & \\
& \ddots & \ddots & \ddots & \\
& & c_{n-2} & d_{n-1} & c_{n-1} \\
& & & c_{n-1} & d_{n}
\end{array}\right]
$$

Suppose one of the off-diagonal elements is equal to zero, say $c_{i}=0$. We then have $\boldsymbol{A}=\left[\begin{array}{cc}\boldsymbol{A}_{1} & \mathbf{0} \\ \mathbf{0} & \boldsymbol{A}_{2}\end{array}\right]$, where

$$
\boldsymbol{A}_{1}=\left[\begin{array}{ccccc}
d_{1} & c_{1} & & & \\
c_{1} & d_{2} & c_{2} & & \\
& \ddots & \ddots & \ddots & \\
& & c_{i-2} & d_{i-1} & c_{i-1} \\
& & & c_{i-1} & d_{i}
\end{array}\right] \text { and } \boldsymbol{A}_{2}=\left[\begin{array}{ccccc}
d_{i+1} & c_{i+1} & & & \\
c_{i+1} & d_{i+2} & c_{i+2} & & \\
& \ddots & \ddots & \ddots & \\
& & c_{n-2} & d_{n-1} & c_{n-1} \\
& & & c_{n-1} & d_{n}
\end{array}\right] .
$$

Thus $\boldsymbol{A}$ is block diagonal and we can split the eigenvalue problem into two smaller problems involving $\boldsymbol{A}_{1}$ and $\boldsymbol{A}_{2}$. We assume that this reduction has been carried out so that $\boldsymbol{A}$ is irreducible, i.e., $c_{i} \neq 0$ for $i=1, \ldots, n-1$.

We first show that irreducibility implies that the eigenvalues are distinct.
Lemma 14.2 (Distinct Eigenvalues of a Tridiagonal Matrix) An irreducible, tridiagonal and symmetric matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ has $n$ real and distinct eigenvalues.

Proof Let $\boldsymbol{A}$ be given by (14.6). By Theorem 6.10 the eigenvalues are real. Define for $x \in \mathbb{R}$ the polynomial $p_{k}(x):=\operatorname{det}\left(x \boldsymbol{I}_{k}-\boldsymbol{A}_{k}\right)$ for $k=1, \ldots, n$, where $\boldsymbol{A}_{k}$ is the upper left $k \times k$ corner of $\boldsymbol{A}$ (the leading principal submatrix of order $k$ ). The eigenvalues of $\boldsymbol{A}$ are the roots of the polynomial $p_{n}$. Using the last column to expand for $k \geq 2$ the determinant $p_{k+1}(x)$ we find

$$
p_{k+1}(x)=\left(x-d_{k+1}\right) p_{k}(x)-c_{k}^{2} p_{k-1}(x) .
$$

Since $p_{1}(x)=x-d_{1}$ and $p_{2}(x)=\left(x-d_{2}\right)\left(x-d_{1}\right)-c_{1}^{2}$ this also holds for $k=0,1$ if we define $p_{-1}(x)=0$ and $p_{0}(x)=1$. For $M$ sufficiently large we have

$$
p_{2}(-M)>0, \quad p_{2}\left(d_{1}\right)<0, \quad p_{2}(+M)>0 .
$$

Since $p_{2}$ is continuous there are $y_{1} \in\left(-M, d_{1}\right)$ and $y_{2} \in\left(d_{1}, M\right)$ such that $p_{2}\left(y_{1}\right)=p_{2}\left(y_{2}\right)=0$. It follows that the root $d_{1}$ of $p_{1}$ separates the roots of $p_{2}$, so $y_{1}$ and $y_{2}$ must be distinct. Consider next

$$
p_{3}(x)=\left(x-d_{3}\right) p_{2}(x)-c_{2}^{2} p_{1}(x)=\left(x-d_{3}\right)\left(x-y_{1}\right)\left(x-y_{2}\right)-c_{2}^{2}\left(x-d_{1}\right) .
$$

Since $y_{1}<d_{1}<y_{2}$ we have for $M$ sufficiently large

$$
p_{3}(-M)<0, \quad p_{3}\left(y_{1}\right)>0, \quad p_{3}\left(y_{2}\right)<0, \quad p_{3}(+M)>0 .
$$

Thus the roots $x_{1}, x_{2}, x_{3}$ of $p_{3}$ are separated by the roots $y_{1}, y_{2}$ of $p_{2}$. In the general case suppose for $k \geq 2$ that the roots $z_{1}, \ldots, z_{k-1}$ of $p_{k-1}$ separate the roots $y_{1}, \ldots, y_{k}$ of $p_{k}$. Choose $M$ so that $y_{0}:=-M<y_{1}, y_{k+1}:=M>y_{k}$. Then

$$
y_{0}<y_{1}<z_{1}<y_{2}<z_{2} \cdots<z_{k-1}<y_{k}<y_{k+1} .
$$

We claim that for $M$ sufficiently large

$$
p_{k+1}\left(y_{j}\right)=(-1)^{k+1-j}\left|p_{k+1}\left(y_{j}\right)\right| \neq 0, \text { for } j=0,1, \ldots, k+1 .
$$

This holds for $j=0, k+1$, and for $j=1, \ldots, k$ since

$$
p_{k+1}\left(y_{j}\right)=-c_{k}^{2} p_{k-1}\left(y_{j}\right)=-c_{k}^{2}\left(y_{j}-z_{1}\right) \cdots\left(y_{j}-z_{k-1}\right) .
$$

It follows that the roots $x_{1}, \ldots, x_{k+1}$ are separated by the roots $y_{1}, \ldots, y_{k}$ of $p_{k}$ and by induction the roots of $p_{n}$ (the eigenvalues of $\boldsymbol{A}$ ) are distinct. $\square$

### 14.5.1 The Inertia Theorem

We say that two matrices $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$ are congruent if $\boldsymbol{A}=\boldsymbol{E}^{*} \boldsymbol{B} \boldsymbol{E}$ for some nonsingular matrix $\boldsymbol{E} \in \mathbb{C}^{n \times n}$. By Theorem 6.7 a Hermitian matrix $\boldsymbol{A}$ is both congruent and similar to a diagonal matrix $\boldsymbol{D}, \boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{U}=\boldsymbol{D}$ where $\boldsymbol{U}$ is unitary. The eigenvalues of $\boldsymbol{A}$ are the diagonal elements of $\boldsymbol{D}$. Let $\pi(\boldsymbol{A}), \zeta(\boldsymbol{A})$ and $v(\boldsymbol{A})$ denote the number of positive, zero and negative eigenvalues of $\boldsymbol{A}$. If $\boldsymbol{A}$ is Hermitian then all eigenvalues are real and $\pi(\boldsymbol{A})+\zeta(\boldsymbol{A})+v(\boldsymbol{A})=n$.

Theorem 14.6 (Sylvester's Inertia Theorem) If $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{C}^{n \times n}$ are Hermitian and congruent then $\pi(\boldsymbol{A})=\pi(\boldsymbol{B}), \zeta(\boldsymbol{A})=\zeta(\boldsymbol{B})$ and $v(\boldsymbol{A})=v(\boldsymbol{B})$.

Proof Suppose $\boldsymbol{A}=\boldsymbol{E}^{*} \boldsymbol{B} \boldsymbol{E}$, where $\boldsymbol{E}$ is nonsingular. Assume first that $\boldsymbol{A}$ and $\boldsymbol{B}$ are diagonal matrices. Suppose $\pi(\boldsymbol{A})=k$ and $\pi(\boldsymbol{B})=m<k$. We shall show that this leads to a contradiction. Let $\boldsymbol{E}_{1}$ be the upper left $m \times k$ corner of $\boldsymbol{E}$. Since $m<k$, we can find a nonzero $\boldsymbol{x}$ such that $\boldsymbol{E}_{1} \boldsymbol{x}=\mathbf{0}$ (cf. Lemma 1.3). Let $\boldsymbol{y}^{T}=$ $\left[\boldsymbol{x}^{T}, \mathbf{0}^{T}\right] \in \mathbb{C}^{n}$, and $\boldsymbol{z}=\left[z_{1}, \ldots, z_{n}\right]^{T}=\boldsymbol{E} \boldsymbol{y}$. Then $z_{i}=0$ for $i=1,2, \ldots, m$. If $\boldsymbol{A}$ has positive eigenvalues $\lambda_{1}, \ldots, \lambda_{k}$ and $\boldsymbol{B}$ has eigenvalues $\mu_{1}, \ldots, \mu_{n}$, where $\mu_{i} \leq 0$ for $i \geq m+1$ then

$$
\boldsymbol{y}^{*} \boldsymbol{A} \boldsymbol{y}=\sum_{i=1}^{n} \lambda_{i}\left|y_{i}\right|^{2}=\sum_{i=1}^{k} \lambda_{i}\left|x_{i}\right|^{2}>0 .
$$

But

$$
\boldsymbol{y}^{*} \boldsymbol{A} \boldsymbol{y}=\boldsymbol{y}^{*} \boldsymbol{E}^{*} \boldsymbol{B} \boldsymbol{E} \boldsymbol{y}=z^{*} \boldsymbol{B} z=\sum_{i=m+1}^{n} \mu_{i}\left|z_{i}\right|^{2} \leq 0,
$$

a contradiction.
We conclude that $\pi(\boldsymbol{A})=\pi(\boldsymbol{B})$ if $\boldsymbol{A}$ and $\boldsymbol{B}$ are diagonal. Moreover, $v(\boldsymbol{A})=$ $\pi(-\boldsymbol{A})=\pi(-\boldsymbol{B})=v(\boldsymbol{B})$ and $\zeta(\boldsymbol{A})=n-\pi(\boldsymbol{A})-v(\boldsymbol{A})=n-\pi(\boldsymbol{B})-v(\boldsymbol{B})=$ $\zeta(\boldsymbol{B})$. This completes the proof for diagonal matrices.

Let in the general case $\boldsymbol{U}_{1}$ and $\boldsymbol{U}_{2}$ be unitary matrices such that $\boldsymbol{U}_{1}^{*} \boldsymbol{A} \boldsymbol{U}_{1}=\boldsymbol{D}_{1}$ and $\boldsymbol{U}_{2}^{*} \boldsymbol{B} \boldsymbol{U}_{2}=\boldsymbol{D}_{2}$ where $\boldsymbol{D}_{1}$ and $\boldsymbol{D}_{2}$ are diagonal matrices. Since $\boldsymbol{A}=\boldsymbol{E}^{*} \boldsymbol{B} \boldsymbol{E}$, we find $\boldsymbol{D}_{1}=\boldsymbol{F}^{*} \boldsymbol{D}_{2} \boldsymbol{F}$ where $\boldsymbol{F}=\boldsymbol{U}_{2}^{*} \boldsymbol{E} \boldsymbol{U}_{1}$ is nonsingular. Thus $\boldsymbol{D}_{1}$ and $\boldsymbol{D}_{2}$ are congruent diagonal matrices. But since $\boldsymbol{A}$ and $\boldsymbol{D}_{1}, \boldsymbol{B}$ and $\boldsymbol{D}_{2}$ have the same eigenvalues, we find $\pi(\boldsymbol{A})=\pi\left(\boldsymbol{D}_{1}\right)=\pi\left(\boldsymbol{D}_{2}\right)=\pi(\boldsymbol{B})$. Similar results hold for $\zeta$ and $v$. $\square$

Corollary 14.2 (Counting Eigenvalues Using the LDL* Factorization) Suppose $\boldsymbol{A}=\operatorname{tridiag}\left(c_{i}, d_{i}, c_{i}\right) \in \mathbb{R}^{n \times n}$ is symmetric and that $\alpha \in \mathbb{R}$ is such that $\boldsymbol{A}-\alpha \boldsymbol{I}$ has an symmetric $L U$ factorization, i.e. $\boldsymbol{A}-\alpha \boldsymbol{I}=\boldsymbol{L} \boldsymbol{D} \boldsymbol{L}^{T}$ where $\boldsymbol{L}$ is unit lower triangular and $\boldsymbol{D}$ is diagonal. Then the number of eigenvalues of $\boldsymbol{A}$ strictly less than $\alpha$ equals the number of negative diagonal elements in $\boldsymbol{D}$. The diagonal elements $d_{1}(\alpha), \ldots, d_{n}(\alpha)$ in $\boldsymbol{D}$ can be computed recursively as follows

$$
d_{1}(\alpha)=d_{1}-\alpha, d_{k}(\alpha)=d_{k}-\alpha-c_{k-1}^{2} / d_{k-1}(\alpha), k=2,3, \ldots, n .
$$

Proof Since the diagonal elements in $\boldsymbol{L}$ in an LU factorization equal the diagonal elements in $\boldsymbol{D}$ in an $\boldsymbol{L} \boldsymbol{D} \boldsymbol{L}^{T}$ factorization we see that the formulas in (14.8) follows immediately from (2.16). Since $\boldsymbol{L}$ is nonsingular, $\boldsymbol{A}-\alpha \boldsymbol{I}$ and $\boldsymbol{D}$ are congruent. By the previous theorem $v(\boldsymbol{A}-\alpha \boldsymbol{I})=v(\boldsymbol{D})$, the number of negative diagonal elements in $\boldsymbol{D}$. If $\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}$ then $(\boldsymbol{A}-\alpha \boldsymbol{I}) \boldsymbol{x}=(\lambda-\alpha) \boldsymbol{x}$, and $\lambda-\alpha$ is an eigenvalue of $\boldsymbol{A}-\alpha \boldsymbol{I}$. But then $v(\boldsymbol{A}-\alpha \boldsymbol{I})$ equals the number of eigenvalues of $\boldsymbol{A}$ which are less than $\alpha$. $\square$

### 14.5.2 Approximating $\lambda_{m}$

Corollary 14.2 can be used to determine the $m$ th eigenvalue of $\boldsymbol{A}$, where $\lambda_{1} \geq \lambda_{2} \geq$ $\cdots \geq \lambda_{n}$. Using Gerschgorin's theorem we first find an interval $[a, b]$, such that $(a, b)$ contains the eigenvalues of $\boldsymbol{A}$. Let for $x \in[a, b]$

$$
\rho(x):=\#\left\{k: d_{k}(x)>0 \text { for } k=1, \ldots, n\right\}
$$

be the number of eigenvalues of $\boldsymbol{A}$ which are strictly greater than $x$. Clearly $\rho(a)=$ $n, \rho(b)=0$. Choosing a tolerance $\epsilon$ and using bisection we proceed as follows:

```
h = b - a;
for j = 1 : itmax
    c = (a + b)/2;
    if b - a < eps * h
```

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-339.jpg?height=40&width=320&top_left_y=596&top_left_x=624)

```
    end
    k = ρ(c);
    if k 2 m a = c else b = c ;
end
```

We generate a sequence $\left\{\left[a_{j}, b_{j}\right]\right\}$ of intervals, each containing $\lambda_{m}$ and $b_{j}-a_{j}=$ $2^{-j}(b-a)$.

As it stands this method will fail if in (14.8) one of the $d_{k}(\alpha)$ is zero. One possibility is to replace such a $d_{k}(\alpha)$ by a suitable small number, say $\delta_{k}=$ $c_{k} \epsilon_{M}$, where $\epsilon_{M}$ is the Machine epsilon, typically $2 \times 10^{-16}$ for MATLAB. This replacement is done if $\left|d_{k}(\alpha)\right|<\left|\delta_{k}\right|$.

### 14.6 Exercises Chap. 14

### 14.6.1 Exercises Sect. 14.1

Exercise 14.1 (Yes or No (Exam Exercise 2006-1)) Answer simply yes or no to the following questions:

a) Every matrix $\boldsymbol{A} \in \mathbb{C}^{m \times n}$ has a singular value decomposition?
b) The algebraic multiplicity of an eigenvalue is always less than or equal to the geometric multiplicity?
c) The QR factorization of a matrix $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ can be determined by Householder transformations in $O\left(n^{2}\right)$ arithmetic operations?
d) Let $\rho(\boldsymbol{A})$ be the spectral radius of $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. Then $\lim _{k \rightarrow \infty} \boldsymbol{A}^{k}=\mathbf{0}$ if and only if $\rho(\boldsymbol{A})<1$ ?

### 14.6.2 Exercises Sect. 14.2

Exercise 14.2 (Nonsingularity Using Gershgorin) Consider the matrix

$$
\boldsymbol{A}=\left(\begin{array}{llll}
4 & 1 & 0 & 0 \\
1 & 4 & 1 & 0 \\
0 & 1 & 4 & 1 \\
0 & 0 & 1 & 4
\end{array}\right) .
$$

Show using Gershgorin's theorem that $\boldsymbol{A}$ is nonsingular.
Exercise 14.3 (Gershgorin, Strictly Diagonally Dominant Matrix) Show using Gershgorin's circle theorem that a strictly diagonally dominant matrix $\boldsymbol{A}\left(\left|a_{i, i}\right|>\right.$ $\sum_{j \neq i}\left|a_{i, j}\right|$ for all $i$ ) is nonsingular.
Exercise 14.4 (Gershgorin Disks (Exam Exercise 2009-2)) The eigenvalues of $\boldsymbol{A} \in \mathbb{R}^{n, n}$ lie inside $R \cap C$, where $R:=R_{1} \cup \cdots \cup R_{n}$ is the union of the row disks $R_{i}$ of $\boldsymbol{A}$, and $C=C_{1} \cup \cdots \cup C_{n}$ is the union of the column disks $C_{j}$. You do not need to prove this. Write a MATLAB function [s,r,c]=gershgorin(A) that computes the centres $\boldsymbol{s}=\left[s_{1}, \ldots, s_{n}\right] \in \mathbb{R}^{n}$ of the row and column disks, and their radii $\boldsymbol{r}=\left[r_{1}, \ldots, r_{n}\right] \in \mathbb{R}^{n}$ and $\boldsymbol{c}=\left[c_{1}, \ldots, c_{n}\right] \in \mathbb{R}^{n}$, respectively.

### 14.6.3 Exercises Sect. 14.3

Exercise 14.5 (Continuity of Eigenvalues) Suppose

$$
\boldsymbol{A}(t):=\boldsymbol{D}+t(\boldsymbol{A}-\boldsymbol{D}), \quad \boldsymbol{D}:=\operatorname{diag}\left(a_{11}, \ldots, a_{n n}\right), \quad t \in \mathbb{R} .
$$

$0 \leq t_{1}<t_{2} \leq 1$ and that $\mu$ is an eigenvalue of $\boldsymbol{A}\left(t_{2}\right)$. Show, using Theorem 14.2 with $\boldsymbol{A}=\boldsymbol{A}\left(t_{1}\right)$ and $\boldsymbol{E}=\boldsymbol{A}\left(t_{2}\right)-\boldsymbol{A}\left(t_{1}\right)$, that $\boldsymbol{A}\left(t_{1}\right)$ has an eigenvalue $\lambda$ such that

$$
|\lambda-\mu| \leq C\left(t_{2}-t_{1}\right)^{1 / n}, \text { where } C \leq 2\left(\|\boldsymbol{D}\|_{2}+\|\boldsymbol{A}-\boldsymbol{D}\|_{2}\right) .
$$

Thus, as a function of $t$, every eigenvalue of $\boldsymbol{A}(t)$ is a continuous function of $t$.
Exercise 14.6 ( $\infty$-Norm of a Diagonal Matrix) Give a direct proof that $\|\boldsymbol{A}\|_{\infty}=$ $\rho(\boldsymbol{A})$ if $\boldsymbol{A}$ is diagonal.

Exercise 14.7 (Eigenvalue Perturbations (Exam Exercise 2010-2)) Let $\boldsymbol{A}=$ $\left[a_{k j}\right], \boldsymbol{E}=\left[e_{k j}\right]$, and $\boldsymbol{B}=\left[b_{k j}\right]$ be matrices in $\mathbb{R}^{n, n}$ with

$$
a_{k j}=\left\{\begin{array}{ll}
1, & j=k+1, \\
0, & \text { otherwise },
\end{array} \quad e_{k j}= \begin{cases}\epsilon, & k=n, j=1, \\
0, & \text { otherwise },\end{cases}\right.
$$

and $\boldsymbol{B}=\boldsymbol{A}+\boldsymbol{E}$, where $0<\epsilon<1$. Thus for $n=4$,

$$
\boldsymbol{A}:=\left[\begin{array}{llll}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right], \quad \boldsymbol{E}:=\left[\begin{array}{llll}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
\epsilon & 0 & 0 & 0
\end{array}\right], \quad \boldsymbol{B}:=\left[\begin{array}{cccc}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\epsilon & 0 & 0 & 0
\end{array}\right] .
$$

a) Find the eigenvalues of $\boldsymbol{A}$ and $\boldsymbol{B}$.
b) Show that $\|\boldsymbol{A}\|_{2}=\|\boldsymbol{B}\|_{2}=1$ for arbitrary $n \in \mathbb{N}$.
c) Recall Elsner's Theorem (Theorem 14.2). Let $\boldsymbol{A}, \boldsymbol{E}, \boldsymbol{B}$ be given by (14.10). What upper bound does (14.1) in Elsner's theorem give for the eigenvalue $\mu=\epsilon^{1 / n}$ of $\boldsymbol{B}$ ? How sharp is this upper bound?

### 14.6.4 Exercises Sect. 14.4

Exercise 14.8 (Number of Arithmetic Operations, Hessenberg Reduction) Show that the number of arithmetic operations for Algorithm 14.1 is $\frac{10}{3} n^{3}=5 G_{n}$.

Exercise 14.9 (Assemble Householder Transformations) Show that the number of arithmetic operations required by Algorithm 14.2 is $\frac{4}{3} n^{3}=2 G_{n}$.

Exercise 14.10 (Tridiagonalize a Symmetric Matrix) If $\boldsymbol{A}$ is real and symmetric we can modify Algorithm 14.1 as follows. To find $\boldsymbol{A}_{k+1}$ from $\boldsymbol{A}_{k}$ we have to compute $\boldsymbol{V}_{k} \boldsymbol{E}_{k} \boldsymbol{V}_{k}$ where $\boldsymbol{E}_{k}$ is symmetric. Dropping subscripts we have to compute a product of the form $\boldsymbol{G}=\left(\boldsymbol{I}-\boldsymbol{v} \boldsymbol{v}^{T}\right) \boldsymbol{E}\left(\boldsymbol{I}-\boldsymbol{v} \boldsymbol{v}^{T}\right)$. Let $\boldsymbol{w}:=\boldsymbol{E} \boldsymbol{v}, \beta:=\frac{1}{2} \boldsymbol{v}^{T} \boldsymbol{w}$ and $\boldsymbol{z}:=\boldsymbol{w}-\beta \boldsymbol{v}$. Show that $\boldsymbol{G}=\boldsymbol{E}-\boldsymbol{v} \boldsymbol{z}^{T}-\boldsymbol{z} \boldsymbol{v}^{T}$. Since $\boldsymbol{G}$ is symmetric, only the sub- or superdiagonal elements of $\boldsymbol{G}$ need to be computed. Computing $\boldsymbol{G}$ in this way, it can be shown that we need $O\left(4 n^{3} / 3\right)$ operations to tridiagonalize a symmetric matrix by orthonormal similarity transformations. This is less than half the work to reduce a nonsymmetric matrix to upper Hessenberg form. We refer to [18] for a detailed algorithm.

### 14.6.5 Exercises Sect. 14.5

Exercise 14.11 (Counting Eigenvalues) Consider the matrix in Exercise 14.2. Determine the number of eigenvalues greater than 4.5.

Exercise 14.12 (Overflow in LDL* Factorization) Let for $n \in \mathbb{N}$

$$
A_{n}=\left[\begin{array}{ccccc}
10 & 1 & 0 & \cdots & 0 \\
1 & 10 & 1 & \ddots & \vdots \\
0 & \ddots & \ddots & \ddots & 0 \\
\vdots & \ddots & 1 & 10 & 1 \\
0 & \cdots & 0 & 1 & 10
\end{array}\right] \in \mathbb{R}^{n \times n} .
$$

a) Let $d_{k}$ be the diagonal elements of $\boldsymbol{D}$ in an LDL* factorization of $\boldsymbol{A}_{n}$. Show that $5+\sqrt{24}<d_{k} \leq 10, k=1,2, \ldots, n$.
b) Show that $D_{n}:=\operatorname{det}\left(\boldsymbol{A}_{n}\right)>(5+\sqrt{24})^{n}$. Give $n_{0} \in \mathbb{N}$ such that your computer gives an overflow when $D_{n_{0}}$ is computed in floating point arithmetic.

Exercise 14.13 (Simultaneous Diagonalization) (Simultaneous diagonalization of two symmetric matrices by a congruence transformation). Let $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{R}^{n \times n}$ where $\boldsymbol{A}^{T}=\boldsymbol{A}$ and $\boldsymbol{B}$ is symmetric positive definite. Then $\boldsymbol{B}=\boldsymbol{U}^{T} \boldsymbol{D} \boldsymbol{U}$ where $\boldsymbol{U}$ is orthonormal and $\boldsymbol{D}=\operatorname{diag}\left(d_{1}, \ldots, d_{n}\right)$ has positive diagonal elements. Let $\hat{\boldsymbol{A}}=\boldsymbol{D}^{-1 / 2} \boldsymbol{U} \boldsymbol{A} \boldsymbol{U}^{T} \boldsymbol{D}^{-1 / 2}$ where

$$
\boldsymbol{D}^{-1 / 2}:=\operatorname{diag}\left(d_{1}^{-1 / 2}, \ldots, d_{n}^{-1 / 2}\right) .
$$

a) Show that $\hat{\boldsymbol{A}}$ is symmetric.

Let $\hat{\boldsymbol{A}}=\hat{\boldsymbol{U}}^{T} \hat{\boldsymbol{D}} \hat{\boldsymbol{U}}$ where $\hat{\boldsymbol{U}}$ is orthonormal and $\hat{\boldsymbol{D}}$ is diagonal. Set $\boldsymbol{E}=$ $\boldsymbol{U}^{T} \boldsymbol{D}^{-1 / 2} \hat{\boldsymbol{U}}^{T}$.

b) Show that $\boldsymbol{E}$ is nonsingular and that $\boldsymbol{E}^{T} \boldsymbol{A} \boldsymbol{E}=\hat{\boldsymbol{D}}, \boldsymbol{E}^{T} \boldsymbol{B} \boldsymbol{E}=\boldsymbol{I}$.

For a more general result see Theorem 10.1 in [11].
Exercise 14.14 (Program Code for One Eigenvalue) Suppose $\boldsymbol{A}=\operatorname{tridiag}(\boldsymbol{c}, \boldsymbol{d}, \boldsymbol{c})$ is symmetric and tridiagonal with elements $d_{1}, \ldots, d_{n}$ on the diagonal and $c_{1}, \ldots, c_{n-1}$ on the neighboring subdiagonals. Let $\lambda_{1} \geq \lambda_{2} \geq \cdots \geq \lambda_{n}$ be the eigenvalues of $\boldsymbol{A}$. We shall write a program to compute one eigenvalue $\lambda_{m}$ for a given $m$ using bisection and the method outlined in (14.9).

a) Write a function $\mathrm{k}=\operatorname{counting}(\mathrm{c}, \mathrm{d}, \mathrm{x})$ which for given $x$ counts the number of eigenvalues of $\boldsymbol{A}$ strictly greater than $x$. Use the replacement described above if one of the $d_{j}(x)$ is close to zero.
b) Write a function lambda=findeigv(c,d,m) which first estimates an interval $(a, b]$ containing all eigenvalues of $\boldsymbol{A}$ and then generates a sequence $\left\{\left(a_{j}, b_{j}\right]\right\}$ of intervals each containing $\lambda_{m}$. Iterate until $b_{j}-a_{j} \leq(b-a) \epsilon_{M}$, where $\epsilon_{M}$ is MATLAB's machine epsilon eps. Typically $\epsilon_{M} \approx 2.22 \times 10^{-16}$.
c) Test the program on $\boldsymbol{T}:=\operatorname{tridiag}(-1,2,-1)$ of size 100. Compare the exact value of $\lambda_{5}$ with your result and the result obtained by using MATLAB's built-in function eig.

Exercise 14.15 (Determinant of Upper Hessenberg Matrix) Suppose $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ is upper Hessenberg and $x \in \mathbb{C}$. We will study two algorithms to compute $f(x)=$ $\operatorname{det}(\boldsymbol{A}-x \boldsymbol{I})$.

a) Show that Gaussian elimination without pivoting requires $O\left(n^{2}\right)$ arithmetic operations.
b) Show that the number of arithmetic operations is the same if partial pivoting is used.
c) Estimate the number of arithmetic operations if Given's rotations are used.
d) Compare the two methods discussing advantages and disadvantages.

### 14.7 Review Questions

14.7.1 Suppose $\boldsymbol{A}, \boldsymbol{E} \in \mathbb{C}^{n \times n}$. To every $\mu \in \sigma(\boldsymbol{A}+\boldsymbol{E})$ there is a $\lambda \in \sigma(\boldsymbol{A})$ which is in some sense close to $\mu$.
    - What is the general result (Elsner's theorem)?
    - what if $\boldsymbol{A}$ is non defective?
    - what if $\boldsymbol{A}$ is normal?
    - what if $\boldsymbol{A}$ is Hermitian?
14.7.2 Can Gerschgorin's theorem be used to check if a matrix is nonsingular?
14.7.3 How many arithmetic operation does it take to reduce a matrix by similarity transformations to upper Hessenberg form by Householder transformations?
14.7.4 Give a condition ensuring that a tridiagonal symmetric matrix has real and distinct eigenvalues:
14.7.5 What is the content of Sylvester's inertia theorem?
14.7.6 Give an application of this theorem.

## Chapter 15 <br> The QR Algorithm

The QR algorithm is a method to find all eigenvalues and eigenvectors of a matrix. In this chapter we give a brief informal introduction to this important algorithm. For a more complete treatment see [18].

The QR algorithm is related to a simpler method called the power method and we start studying this method and its variants.

### 15.1 The Power Method and Its Variants

These methods can be used to compute a single eigenpair of a matrix. They also play a role when studying properties of the QR algorithm.

### 15.1.1 The Power Method

The power method in its basic form is a technique to compute an approximation to the eigenvector corresponding to the largest (in absolute value) eigenvalue of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. As a by product we can also find an approximation to the corresponding eigenvalue. We define a sequence $\left\{z_{k}\right\}$ of vectors in $\mathbb{C}^{n}$ by

$$
\boldsymbol{z}_{k}:=\boldsymbol{A}^{k} \boldsymbol{z}_{0}=\boldsymbol{A} \boldsymbol{z}_{k-1}, \quad k=1,2, \ldots .
$$

Example 15.1 (Power Method) Let

$$
\boldsymbol{A}=\left[\begin{array}{cc}
2 & -1 \\
-1 & 2
\end{array}\right], \quad \boldsymbol{z}_{0}:=\left[\begin{array}{l}
1 \\
0
\end{array}\right] .
$$

We find

$$
z_{1}=\boldsymbol{A} z_{0}=\left[\begin{array}{c}
2 \\
-1
\end{array}\right], \quad z_{2}=\boldsymbol{A} z_{1}=\left[\begin{array}{c}
5 \\
-4
\end{array}\right], \cdots, z_{k}=\frac{1}{2}\left[\begin{array}{l}
1+3^{k} \\
1-3^{k}
\end{array}\right], \cdots .
$$

It follows that $2 z_{k} / 3^{k}$ converges to $[1,-1]$, an eigenvector corresponding to the dominant eigenvalue $\lambda=3$. The sequence of Rayleigh quotients $\left\{z_{k}^{T} \boldsymbol{A} z_{k} / z_{k}^{T} z_{k}\right\}$ will converge to the dominant eigenvalue $\lambda=3$.

To understand better what happens we expand $\boldsymbol{z}_{0}$ in terms of the eigenvectors

$$
z_{0}=\frac{1}{2}\left[\begin{array}{c}
1 \\
-1
\end{array}\right]+\frac{1}{2}\left[\begin{array}{l}
1 \\
1
\end{array}\right]=c_{1} \boldsymbol{v}_{1}+c_{2} \boldsymbol{v}_{2} .
$$

Since $\boldsymbol{A}^{k}$ has eigenpairs $\left(\lambda_{j}^{k}, \boldsymbol{v}_{j}\right), j=1,2$ we find

$$
z_{k}=c_{1} \lambda_{1}^{k} v_{1}+c_{2} \lambda_{2}^{k} v_{2}=c_{1} 3^{k} v_{1}+c_{2} 1^{k} v_{2} .
$$

Thus $3^{-k} z_{k}=c_{1} \boldsymbol{v}_{1}+3^{-k} c_{2} \boldsymbol{v}_{2} \rightarrow c_{1} \boldsymbol{v}_{1}$. Since $c_{1} \neq 0$ we obtain convergence to the dominant eigenvector.

Let $\boldsymbol{A} \in \mathbb{C}^{n \times n}$ have eigenpairs $\left(\lambda_{j}, \boldsymbol{v}_{j}\right), j=1, \ldots, n$ with $\left|\lambda_{1}\right|>\left|\lambda_{2}\right| \geq \cdots \geq$ $\left|\lambda_{n}\right|$.

Given $z_{0} \in \mathbb{C}^{n}$ we assume that

$$
\begin{aligned}
& \text { (i) }\left|\lambda_{1}\right|>\left|\lambda_{2}\right| \geq\left|\lambda_{3}\right| \geq \cdots \geq\left|\lambda_{n}\right| \text {, } \\
& \text { (ii) } z_{0}^{T} v_{1} \neq 0
\end{aligned}
$$

(iii) $\boldsymbol{A}$ has linearly independent eigenvectors.
The first assumption means that $\boldsymbol{A}$ has a dominant eigenvalue $\lambda_{1}$ of algebraic multiplicity one. The second assumption says that $z_{0}$ has a component in the direction $\boldsymbol{v}_{1}$. The third assumption is not necessary, but is included in order to simplify the analysis.

To see what happens let $z_{0}=c_{1} \boldsymbol{v}_{1}+c_{2} \boldsymbol{v}_{2}+\cdots+c_{n} \boldsymbol{v}_{n}$, where by assumption (ii) of (15.2) we have $c_{1} \neq 0$. Since $\boldsymbol{A}^{k} \boldsymbol{v}_{j}=\lambda_{j}^{k} \boldsymbol{v}_{j}$ for all $j$ we see that

$$
\boldsymbol{z}_{k}=c_{1} \lambda_{1}^{k} \boldsymbol{v}_{1}+c_{2} \lambda_{2}^{k} \boldsymbol{v}_{2}+\cdots+c_{n} \lambda_{n}^{k} \boldsymbol{v}_{n}, \quad k=0,1,2, \ldots .
$$

Dividing by $\lambda_{1}^{k}$ we find

$$
\frac{z_{k}}{\lambda_{1}^{k}}=c_{1} \boldsymbol{v}_{1}+c_{2}\left(\frac{\lambda_{2}}{\lambda_{1}}\right)^{k} \boldsymbol{v}_{2}+\cdots+c_{n}\left(\frac{\lambda_{n}}{\lambda_{1}}\right)^{k} \boldsymbol{v}_{n}, \quad k=0,1,2, \ldots
$$

Assumption (i) of (15.2) implies that $\left(\lambda_{j} / \lambda_{1}\right)^{k} \rightarrow 0$ as $k \rightarrow \infty$ for all $j \geq 2$ and we obtain

$$
\lim _{k \rightarrow \infty} \frac{z_{k}}{\lambda_{1}^{k}}=c_{1} \boldsymbol{v}_{1},
$$

the dominant eigenvector of $\boldsymbol{A}$. It can be shown that this also holds for defective matrices as long as $(i)$ and $(i i)$ of (15.2) hold, see for example page 58 of [18].

In practice we need to scale the iterates $z_{k}$ somehow and we normally do not know $\lambda_{1}$. Instead we choose a norm on $\mathbb{C}^{n}$, set $\boldsymbol{x}_{0}=z_{0} /\left\|z_{0}\right\|$ and generate for $k=1,2, \ldots$ unit vectors as follows:

$$
\begin{array}{ll}
\text { (i) } & \boldsymbol{y}_{k}=\boldsymbol{A} \boldsymbol{x}_{k-1} \\
\text { (ii) } & \boldsymbol{x}_{k}=\boldsymbol{y}_{k} /\left\|\boldsymbol{y}_{k}\right\| .
\end{array}
$$

Lemma 15.1 (Convergence of the Power Method) Suppose (15.2) holds. Then

$$
\lim _{k \rightarrow \infty}\left(\frac{\left|\lambda_{1}\right|}{\lambda_{1}}\right)^{k} \boldsymbol{x}_{k}=\frac{c_{1}}{\left|c_{1}\right|} \frac{\boldsymbol{v}_{1}}{\left\|\boldsymbol{v}_{1}\right\|} .
$$

In particular, if $\lambda_{1}>0$ and $c_{1}>0$ then the sequence $\left\{\boldsymbol{x}_{k}\right\}$ will converge to the eigenvector $\boldsymbol{u}_{1}:=\boldsymbol{v}_{1} /\left\|\boldsymbol{v}_{1}\right\|$ of unit length.

Proof By induction on $k$ it follows that $\boldsymbol{x}_{k}=\boldsymbol{z}_{k} /\left\|\boldsymbol{z}_{k}\right\|$ for all $k \geq 0$, where $\boldsymbol{z}_{k}=$ $\boldsymbol{A}^{k} \boldsymbol{z}_{0}$. Indeed, this holds for $k=1$, and if it holds for $k-1$ then $\boldsymbol{y}_{k}=\boldsymbol{A} \boldsymbol{x}_{k-1}=$ $\boldsymbol{A} \boldsymbol{z}_{k-1} /\left\|\boldsymbol{z}_{k-1}\right\|=\boldsymbol{z}_{k} /\left\|\boldsymbol{z}_{k-1}\right\|$ and $\boldsymbol{x}_{k}=\left(\boldsymbol{z}_{k} /\left\|\boldsymbol{z}_{k-1}\right\|\right)\left(\left\|\boldsymbol{z}_{k-1}\right\| /\left\|\boldsymbol{z}_{k}\right\|\right)=\boldsymbol{z}_{k} /\left\|\boldsymbol{z}_{k}\right\|$. But then

$$
\boldsymbol{x}_{k}=\frac{\boldsymbol{z}_{k}}{\left\|\boldsymbol{z}_{k}\right\|}=\frac{c_{1} \lambda_{1}^{k}}{\left|c_{1} \lambda_{1}^{k}\right|} \frac{\boldsymbol{v}_{1}+\frac{c_{2}}{c_{1}}\left(\frac{\lambda_{2}}{\lambda_{1}}\right)^{k} \boldsymbol{v}_{2}+\cdots+\frac{c_{n}}{c_{1}}\left(\frac{\lambda_{n}}{\lambda_{1}}\right)^{k} \boldsymbol{v}_{n}}{\left\|\boldsymbol{v}_{1}+\frac{c_{2}}{c_{1}}\left(\frac{\lambda_{2}}{\lambda_{1}}\right)^{k} \boldsymbol{v}_{2}+\cdots+\frac{c_{n}}{c_{1}}\left(\frac{\lambda_{n}}{\lambda_{1}}\right)^{k} \boldsymbol{v}_{n}\right\|}, \quad k=0,1,2, \ldots,
$$

and this implies the lemma. $\square$

Suppose we know an approximate eigenvector $\boldsymbol{u}$ of $\boldsymbol{A}$, but not the corresponding eigenvalue $\mu$. One way of estimating $\mu$ is to minimize the Euclidian norm of the residual $r(\lambda):=\boldsymbol{A} \boldsymbol{u}-\lambda \boldsymbol{u}$.

Theorem 15.1 (The Rayleigh Quotient Minimizes the Residual) Let $\boldsymbol{A} \in \mathbb{C}^{n \times n}$, $\boldsymbol{u} \in \mathbb{C}^{n} \backslash\{\mathbf{0}\}$, and let $\rho: \mathbb{C} \rightarrow \mathbb{R}$ be given by $\rho(\lambda)=\|\boldsymbol{A} \boldsymbol{u}-\lambda \boldsymbol{u}\|_{2}$. Then $\rho$ is minimized when $\lambda:=\frac{\boldsymbol{u}^{*} \boldsymbol{A} \boldsymbol{u}}{\boldsymbol{u}^{*} \boldsymbol{u}}$, the Rayleigh quotient for $\boldsymbol{A}$.

Proof Assume $\boldsymbol{u}^{*} \boldsymbol{u}=1$ and extend $\boldsymbol{u}$ to an orthonormal basis $\{\boldsymbol{u}, \boldsymbol{U}\}$ for $\mathbb{C}^{n}$. Then $\boldsymbol{U}^{*} \boldsymbol{u}=\mathbf{0}$ and

$$
\left[\begin{array}{c}
\boldsymbol{u}^{*} \\
\boldsymbol{U}^{*}
\end{array}\right](\boldsymbol{A} \boldsymbol{u}-\lambda \boldsymbol{u})=\left[\begin{array}{c}
\boldsymbol{u}^{*} \boldsymbol{A} \boldsymbol{u}-\lambda \boldsymbol{u}^{*} \boldsymbol{u} \\
\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{u}-\lambda \boldsymbol{U}^{*} \boldsymbol{u}
\end{array}\right]=\left[\begin{array}{c}
\boldsymbol{u}^{*} \boldsymbol{A} \boldsymbol{u}-\lambda \\
\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{u}
\end{array}\right] .
$$

By unitary invariance of the Euclidian norm

$$
\rho(\lambda)^{2}=\left|\boldsymbol{u}^{*} \boldsymbol{A} \boldsymbol{u}-\lambda\right|^{2}+\left\|\boldsymbol{U}^{*} \boldsymbol{A} \boldsymbol{u}\right\|_{2}^{2},
$$

and $\rho$ has a global minimum at $\lambda=\boldsymbol{u}^{*} \boldsymbol{A} \boldsymbol{u}$. $\square$

Using Rayleigh quotients we can incorporate the calculation of the eigenvalue into the power iteration. We can then compute the residual and stop the iteration when the residual is sufficiently small. But what does it mean to be sufficiently small? Recall that if $\boldsymbol{A}$ is nonsingular with a nonsingular eigenvector matrix $\boldsymbol{X}$ and $(\mu, \boldsymbol{u})$ is an approximate eigenpair with $\|\boldsymbol{u}\|_{2}=1$, then by (14.4) we can find an eigenvalue $\lambda$ of $\boldsymbol{A}$ such that

$$
\frac{|\lambda-\mu|}{|\lambda|} \leq K_{2}(\boldsymbol{X}) K_{2}(\boldsymbol{A}) \frac{\|\boldsymbol{A} \boldsymbol{u}-\mu \boldsymbol{u}\|_{2}}{\|\boldsymbol{A}\|_{2}} .
$$

Thus if the relative residual is small and both $\boldsymbol{A}$ and $\boldsymbol{X}$ are well conditioned then the relative error in the eigenvalue will be small.

This discussion leads to the power method with Rayleigh quotient computation. Given $\boldsymbol{A} \in \mathbb{C}^{n \times n}$, a starting vector $\boldsymbol{z} \in \mathbb{C}^{n}$, a maximum number $K$ of iterations, and a convergence tolerance tol. The power method combined with a Rayleigh quotient estimate for the eigenvalue is used to compute a dominant eigenpair ( $l, \boldsymbol{x}$ ) of $\boldsymbol{A}$ with $\|\boldsymbol{x}\|_{2}=1$. The integer it returns the number of iterations needed in order for $\|\boldsymbol{A} \boldsymbol{x}-l \boldsymbol{x}\|_{2} /\|\boldsymbol{A}\|_{F}<t o l$. If no such eigenpair is found in $K$ iterations the value it $=K+1$ is returned.

```
function [l,x,it]=powerit(A,z,K,tol)
% [l,x,it]=powerit(A,z,K,tol)
af=norm(A,'fro'); x=z/norm(z);
for k=1:K
    y=A*x; l=x'*y;
    if norm(y-l*x)/af<tol
        it=k; x=y/norm(y); return
    end
    x=y/norm(y);
end
it=K+1;
end
```

Listing 15.1 powerit

Example 15.2 (Power Method) We try powerit on the three matrices

$$
\boldsymbol{A}_{1}:=\left[\begin{array}{ll}
1 & 2 \\
3 & 4
\end{array}\right], \quad \boldsymbol{A}_{2}:=\left[\begin{array}{cc}
1.7 & -0.4 \\
0.15 & 2.2
\end{array}\right], \quad \text { and } \boldsymbol{A}_{3}=\left[\begin{array}{cc}
1 & 2 \\
-3 & 4
\end{array}\right] .
$$

In each case we start with the random vector $\boldsymbol{z}=[0.6602,0.3420]$ and tol $=10^{-6}$. For $\boldsymbol{A}_{1}$ we get convergence in 7 iterations, for $\boldsymbol{A}_{2}$ it takes 174 iterations, and for $\boldsymbol{A}_{3}$ we do not get convergence.

The matrix $\boldsymbol{A}_{3}$ does not have a dominant eigenvalue since the two eigenvalues are complex conjugate of each other. Thus the basic condition (i) of (15.2) is not satisfied and the power method diverges. The enormous difference in the rate of convergence for $\boldsymbol{A}_{1}$ and $\boldsymbol{A}_{2}$ can be explained by looking at (15.4). The rate of convergence depends on the ratio $\frac{\left|\lambda_{2}\right|}{\left|\lambda_{1}\right|}$. If this ratio is small then the convergence is fast, while it can be quite slow if the ratio is close to one. The eigenvalues of $\boldsymbol{A}_{1}$ are $\lambda_{1}=5.3723$ and $\lambda_{2}=-0.3723$ giving a quite small ratio of 0.07 and the convergence is fast. On the other hand the eigenvalues of $\boldsymbol{A}_{2}$ are $\lambda_{1}=2$ and $\lambda_{2}=1.9$ and the corresponding ratio is 0.95 resulting in slow convergence.

A variant of the power method is the shifted power method. In this method we choose a number $s$ and apply the power method to the matrix $\boldsymbol{A}-s \boldsymbol{I}$. The number $s$ is called a shift since it shifts an eigenvalue $\lambda$ of $\boldsymbol{A}$ to $\lambda-s$ of $\boldsymbol{A}-s \boldsymbol{I}$. Sometimes the convergence can be faster if the shift is chosen intelligently. For example, if we apply the shifted power method to $\boldsymbol{A}_{2}$ in Example 15.2 with shift 1.8, then with the same starting vector and tol as above, we get convergence in 17 iterations instead of 174 for the unshifted algorithm.

### 15.1.2 The Inverse Power Method

Another variant of the power method with Rayleigh quotient is the inverse power method. This method can be used to determine any eigenpair ( $\lambda, \boldsymbol{x}$ ) of $\boldsymbol{A}$ as long as $\lambda$ has algebraic multiplicity one. In the inverse power method we apply the power method to the inverse matrix $(\boldsymbol{A}-s \boldsymbol{I})^{-1}$, where $s$ is a shift. If $\boldsymbol{A}$ has eigenvalues $\lambda_{1}, \ldots, \lambda_{n}$ in no particular order then $(\boldsymbol{A}-s \boldsymbol{I})^{-1}$ has eigenvalues

$$
\mu_{1}(s)=\left(\lambda_{1}-s\right)^{-1}, \mu_{2}(s)=\left(\lambda_{2}-s\right)^{-1}, \ldots, \mu_{n}(s)=\left(\lambda_{n}-s\right)^{-1} .
$$

Suppose $\lambda_{1}$ is a simple eigenvalue of $\boldsymbol{A}$. Then $\lim _{s \rightarrow \lambda_{1}}\left|\mu_{1}(s)\right|=\infty$, while $\lim _{s \rightarrow \lambda_{1}} \mu_{j}(s)=\left(\lambda_{j}-\lambda_{1}\right)^{-1}<\infty$ for $j=2, \ldots, n$. Hence, by choosing $s$ sufficiently close to $\lambda_{1}$ the inverse power method will converge to that eigenvalue.

For the inverse power method (15.6) is replaced by

$$
\begin{array}{ll}
\text { (i) } & (\boldsymbol{A}-s \boldsymbol{I}) \boldsymbol{y}_{k}=\boldsymbol{x}_{k-1} \\
\text { (ii) } & \boldsymbol{x}_{k}=\boldsymbol{y}_{k} /\left\|\boldsymbol{y}_{k}\right\| .
\end{array}
$$

Note that we solve the linear system rather than computing the inverse matrix. Normally the PLU factorization of $\boldsymbol{A}-s \boldsymbol{I}$ is precomputed in order to speed up the computation.

### 15.1.3 Rayleigh Quotient Iteration

A variant of the inverse power method is known simply as Rayleigh quotient iteration. In this method we change the shift from iteration to iteration, using the previous Rayleigh quotient $s_{k-1}$ as the current shift. In each iteration we need to compute the following quantities

$$
\begin{aligned}
\text { (i) } & \left(\boldsymbol{A}-s_{k-1} \boldsymbol{I}\right) \boldsymbol{y}_{k}=\boldsymbol{x}_{k-1}, \\
\text { (ii) } & \boldsymbol{x}_{k}=\boldsymbol{y}_{k} /\left\|\boldsymbol{y}_{k}\right\|, \\
\text { (iii) } & \boldsymbol{s}_{k}=\boldsymbol{x}_{k}^{*} \boldsymbol{A} \boldsymbol{x}_{k}, \\
\text { (iv) } & \boldsymbol{r}_{k}=\boldsymbol{A} \boldsymbol{x}_{k}-s_{k} \boldsymbol{x}_{k} .
\end{aligned}
$$

We can avoid the calculation of $\boldsymbol{A} \boldsymbol{x}_{k}$ in (iii) and (iv). Let

$$
\rho_{k}:=\frac{\boldsymbol{y}_{k}^{*} \boldsymbol{x}_{k-1}}{\boldsymbol{y}_{k}^{*} \boldsymbol{y}_{k}}, \quad \boldsymbol{w}_{k}:=\frac{\boldsymbol{x}_{k-1}}{\left\|\boldsymbol{y}_{k}\right\|_{2}} .
$$

Then

$$
\begin{aligned}
& s_{k}=\frac{\boldsymbol{y}_{k}^{*} \boldsymbol{A} \boldsymbol{y}_{k}}{\boldsymbol{y}_{k}^{*} \boldsymbol{y}_{k}}=s_{k-1}+\frac{\boldsymbol{y}_{k}^{*}\left(\boldsymbol{A}-s_{k-1} \boldsymbol{I}\right) \boldsymbol{y}_{k}}{\boldsymbol{y}_{k}^{*} \boldsymbol{y}_{k}}=s_{k-1}+\frac{\boldsymbol{y}_{k}^{*} \boldsymbol{x}_{k-1}}{\boldsymbol{y}_{k}^{*} \boldsymbol{y}_{k}}=s_{k-1}+\rho_{k}, \\
& \boldsymbol{r}_{k}=\boldsymbol{A} \boldsymbol{x}_{k}-s_{k} \boldsymbol{x}_{k}=\frac{\boldsymbol{A} \boldsymbol{y}_{k}-\left(s_{k-1}+\rho_{k}\right) \boldsymbol{y}_{k}}{\left\|\boldsymbol{y}_{k}\right\|_{2}}=\frac{\boldsymbol{x}_{k-1}-\rho_{k} \boldsymbol{y}_{k}}{\left\|\boldsymbol{y}_{k}\right\|_{2}}=\boldsymbol{w}_{k}-\rho_{k} \boldsymbol{x}_{k} .
\end{aligned}
$$

Another problem is that the linear system in (i) becomes closer and closer to singular as $s_{k}$ converges to the eigenvalue. Thus the system becomes more and more ill-conditioned and we can expect large errors in the computed $\boldsymbol{y}_{k}$. This is indeed true, but we are lucky. Most of the error occurs in the direction of the eigenvector and
this error disappears when we normalize $\boldsymbol{y}_{k}$ in ( $i i$ ). Miraculously, the normalized eigenvector will be quite accurate.

Given an approximation $(s, \boldsymbol{x})$ to an eigenpair $(\lambda, \boldsymbol{v})$ of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. The following algorithm computes a hopefully better approximation to $(\lambda, \boldsymbol{v})$ by doing one Rayleigh quotient iteration. The length $n r$ of the new residual is also returned.

```
function [x,s,nr]=rayleighit(A,x,s)
% [x,s,nr]=rayleighit(A,x,s)
n=length(x);
y=(A-s*eye(n,n))\x;
yn=norm(y);
w=x/yn;
x=y/yn;
rho=x'*w;
s=s+rho;
nr=norm(w-rho*x);
end
```

Since the shift changes from iteration to iteration the computation of $\boldsymbol{y}$ in rayleighit will require $O\left(n^{3}\right)$ arithmetic operations for a full matrix. For such a matrix it might be useful to reduce it to an upper Hessenberg form, or tridiagonal form, before starting the iteration. However, if we have a good approximation to an eigenpair then only a few iterations are necessary to obtain close to machine accuracy.

If Rayleigh quotient iteration converges the convergence will be quadratic and sometimes even cubic. We illustrate this with an example.

Example 15.3 (Rayleigh Quotient Iteration) The smallest eigenvalue of the matrix $\boldsymbol{A}=\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]$ is $\lambda_{1}=(5-\sqrt{33}) / 2 \approx-0.37$. Starting with $\boldsymbol{x}=[1,1]^{T}$ and $s=$ 0 rayleighit converges to this eigenvalue and corresponding eigenvector. In Table 15.1 we show the rate of convergence by iterating rayleighit 5 times. The errors are approximately squared in each iteration indicating quadratic convergence.

Table 15.1 Quadratic convergence of Rayleigh quotient iteration

Listing 15.2 rayleighit
| $k$ | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\\|\boldsymbol{r}\\|_{2}$ | $1.0 \mathrm{e}+000$ | 7.7e-002 | 1.6e-004 | 8.2e-010 | 2.0e-020 |
| $\left\|s-\lambda_{1}\right\|$ | 3.7e-001 | -1.2e-002 | -2.9e-005 | -1.4e-010 | -2.2e-016 |


### 15.2 The Basic QR Algorithm

The QR algorithm is an iterative method to compute all eigenvalues and eigenvectors of a matrix $\boldsymbol{A} \in \mathbb{C}^{n \times n}$. The matrix is reduced to triangular form by a sequence of unitary similarity transformations computed from the QR factorization of $\boldsymbol{A}$. Recall that for a square matrix the QR factorization and the QR decomposition are the same. If $\boldsymbol{A}=\boldsymbol{Q} \boldsymbol{R}$ is a QR factorization then $\boldsymbol{Q} \in \mathbb{C}^{n \times n}$ is unitary, $\boldsymbol{Q}^{*} \boldsymbol{Q}=\boldsymbol{I}$ and $\boldsymbol{R} \in \mathbb{C}^{n \times n}$ is upper triangular.

The basic QR algorithm takes the following form:

$$
\begin{aligned}
& \boldsymbol{A}_{1}=\boldsymbol{A} \\
& \text { for } k=1,2, \ldots \\
& \quad \boldsymbol{Q}_{k} \boldsymbol{R}_{k}=\boldsymbol{A}_{k} \quad\left(\text { QR factorization of } \boldsymbol{A}_{k}\right) \\
& \boldsymbol{A}_{k+1}=\boldsymbol{R}_{k} \boldsymbol{Q}_{k} .
\end{aligned}
$$

end

The determination of the QR factorization of $\boldsymbol{A}_{k}$ and the computation of $\boldsymbol{R}_{k} \boldsymbol{Q}_{k}$ is called a QR step. It is not at all clear that a QR step does anything useful. At this point, since $\boldsymbol{R}_{k}=\boldsymbol{Q}_{k}^{*} \boldsymbol{A}_{k}$ we find

$$
\boldsymbol{A}_{k+1}=\boldsymbol{R}_{k} \boldsymbol{Q}_{k}=\boldsymbol{Q}_{k}^{*} \boldsymbol{A}_{k} \boldsymbol{Q}_{k},
$$

so $\boldsymbol{A}_{k+1}$ is unitary similar to $\boldsymbol{A}_{k}$. By induction $\boldsymbol{A}_{k+1}$ is unitary similar to $\boldsymbol{A}$. Thus, each $\boldsymbol{A}_{k}$ has the same eigenvalues as $\boldsymbol{A}$. We shall see that the basic QR algorithm is related to the power method.

Here are two examples to illustrate what happens.
Example 15.4 (QR Iteration; Real Eigenvalues) We start with

$$
\boldsymbol{A}_{1}=\boldsymbol{A}=\left[\begin{array}{ll}
2 & 1 \\
1 & 2
\end{array}\right]=\left(\frac{1}{\sqrt{5}}\left[\begin{array}{cc}
-2 & -1 \\
-1 & 2
\end{array}\right]\right) *\left(\frac{1}{\sqrt{5}}\left[\begin{array}{cc}
-5 & -4 \\
0 & 3
\end{array}\right]\right)=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}
$$

and obtain

$$
\boldsymbol{A}_{2}=\boldsymbol{R}_{1} \boldsymbol{Q}_{1}=\frac{1}{5}\left[\begin{array}{cc}
-5 & -4 \\
0 & 3
\end{array}\right] *\left[\begin{array}{cc}
-2 & -1 \\
-1 & 2
\end{array}\right]=\frac{1}{5}\left[\begin{array}{cc}
14 & -3 \\
-3 & 6
\end{array}\right]=\left[\begin{array}{cc}
2.8 & -0.6 \\
-0.6 & 1.2
\end{array}\right] .
$$

Continuing we find

$$
\boldsymbol{A}_{4} \approx\left[\begin{array}{cc}
2.997 & -0.074 \\
-0.074 & 1.0027
\end{array}\right], \quad \boldsymbol{A}_{10} \approx\left[\begin{array}{cc}
3.0000 & -0.0001 \\
-0.0001 & 1.0000
\end{array}\right]
$$

$\boldsymbol{A}_{10}$ is almost diagonal and contains approximations to the eigenvalues $\lambda_{1}=3$ and $\lambda_{2}=1$ on the diagonal.

Example 15.5 (QR Iteration; Complex Eigenvalues) Applying the QR iteration (15.8) to the matrix

$$
A_{1}=A=\left[\begin{array}{llll}
0.9501 & 0.8913 & 0.8214 & 0.9218 \\
0.2311 & 0.7621 & 0.4447 & 0.7382 \\
0.6068 & 0.4565 & 0.6154 & 0.1763 \\
0.4860 & 0.0185 & 0.7919 & 0.4057
\end{array}\right]
$$

we obtain

$$
A_{14}=\left[\begin{array}{r|rr|r}
2.323 & 0.047223 & -0.39232 & -0.65056 \\
\hline-2.1 e-10 & 0.13029 & 0.36125 & 0.15946 \\
-4.1 e-10 & -0.58622 & 0.052576 & -0.25774 \\
\hline 1.2 e-14 & 3.3 e-05 & -1.1 e-05 & 0.22746
\end{array}\right] .
$$

This matrix is almost quasi-triangular and estimates for the eigenvalues $\lambda_{1}, \ldots, \lambda_{4}$ of $\boldsymbol{A}$ can now easily be determined from the diagonal blocks of $\boldsymbol{A}_{14}$. The $1 \times 1$ blocks give us two real eigenvalues $\lambda_{1} \approx 2.323$ and $\lambda_{4} \approx 0.2275$. The middle $2 \times 2$ block has complex eigenvalues resulting in $\lambda_{2} \approx 0.0914+0.4586 i$ and $\lambda_{3} \approx$ 0.0914-0.4586i. From Gerschgorin's circle Theorem 14.1 and Corollary 14.1 it follows that the approximations to the real eigenvalues are quite accurate. We would also expect the complex eigenvalues to have small absolute errors.

These two examples illustrate what most often happens in general. The sequence $\left(\boldsymbol{A}_{k}\right)_{k}$ converges to the triangular Schur form (Cf. Theorem 6.5) if all the eigenvalues are real or the quasi-triangular Schur form (Cf. Definition 6.5) if some of the eigenvalues are complex.

### 15.2.1 Relation to the Power Method

Let us show that the basic QR algorithm is related to the power method. We obtain the QR factorization of the powers $\boldsymbol{A}^{k}$ as follows:

Theorem 15.3 (QR and Power) For $k=1,2,3 \ldots$, the $Q R$ factorization of $A^{k}$ is $\boldsymbol{A}^{k}=\tilde{\boldsymbol{Q}}_{k} \tilde{\boldsymbol{R}}_{k}$, where

$$
\tilde{\boldsymbol{Q}}_{k}:=\boldsymbol{Q}_{1} \cdots \boldsymbol{Q}_{k} \text { and } \tilde{\boldsymbol{R}}_{k}:=\boldsymbol{R}_{k} \cdots \boldsymbol{R}_{1},
$$

and $\boldsymbol{Q}_{1}, \ldots, \boldsymbol{Q}_{k}, \boldsymbol{R}_{1}, \ldots, \boldsymbol{R}_{k}$ are the matrices generated by the basic $Q R$ algorithm (15.8).

$$
\boldsymbol{A}=\left[\begin{array}{llll}
x & x & x & x \\
0 & x & x & x \\
0 & 0 & x & x \\
0 & 0 & 0 & x
\end{array}\right] \xrightarrow{\boldsymbol{P}_{12}^{*}}\left[\begin{array}{llll}
x & x & x & x \\
\mathbf{x} & x & x & x \\
0 & 0 & x & x \\
0 & 0 & 0 & x
\end{array}\right] \xrightarrow{\boldsymbol{P}_{23}^{*}}\left[\begin{array}{llll}
x & x & x & x \\
x & x & x & x \\
0 & \mathbf{x} & x & x \\
0 & 0 & 0 & x
\end{array}\right] \xrightarrow{\boldsymbol{P}_{34}^{*}}\left[\begin{array}{llll}
x & x & x & x \\
x & x & x & x \\
0 & x & x & x \\
0 & 0 & \mathbf{x} & x
\end{array}\right] .
$$
Fig. 15.1 Post multiplication in a QR step

Proof By (15.9)

$$
\boldsymbol{A}_{k}=\boldsymbol{Q}_{k-1}^{*} \boldsymbol{A}_{k-1} \boldsymbol{Q}_{k-1}=\boldsymbol{Q}_{k-1}^{*} \boldsymbol{Q}_{k-2}^{*} \boldsymbol{A}_{k-2} \boldsymbol{Q}_{k-2} \boldsymbol{Q}_{k-1}=\cdots=\tilde{\boldsymbol{Q}}_{k-1}^{*} \boldsymbol{A} \tilde{\boldsymbol{Q}}_{k-1} .
$$

The proof is by induction on $k$. Clearly $\tilde{\boldsymbol{Q}}_{1} \tilde{\boldsymbol{R}}_{1}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}=\boldsymbol{A}_{1}$. Suppose $\tilde{\boldsymbol{Q}}_{k-1} \tilde{\boldsymbol{R}}_{k-1}=\boldsymbol{A}^{k-1}$ for some $k \geq 2$. Since $\boldsymbol{Q}_{k} \boldsymbol{R}_{k}=\boldsymbol{A}_{k}$ and using (15.11)

$$
\tilde{\boldsymbol{Q}}_{k} \tilde{\boldsymbol{R}}_{k}=\tilde{\boldsymbol{Q}}_{k-1}\left(\boldsymbol{Q}_{k} \boldsymbol{R}_{k}\right) \tilde{\boldsymbol{R}}_{k-1}=\tilde{\boldsymbol{Q}}_{k-1} \boldsymbol{A}_{k} \tilde{\boldsymbol{R}}_{k-1}=\left(\tilde{\boldsymbol{Q}}_{k-1} \tilde{\boldsymbol{Q}}_{k-1}^{*}\right) \boldsymbol{A} \tilde{\boldsymbol{Q}}_{k-1} \tilde{\boldsymbol{R}}_{k-1}=\boldsymbol{A}^{k} .
$$ $\square$

Since $\tilde{\boldsymbol{R}}_{k}$ is upper triangular, its first column is a multiple of $\boldsymbol{e}_{1}$ so that

$$
\boldsymbol{A}^{k} \boldsymbol{e}_{1}=\tilde{\boldsymbol{Q}}_{k} \tilde{\boldsymbol{R}}_{k} \boldsymbol{e}_{1}=\tilde{r}_{11}^{(k)} \tilde{\boldsymbol{Q}}_{k} \boldsymbol{e}_{1} \text { or } \tilde{\boldsymbol{q}}_{1}^{(k)}:=\tilde{\boldsymbol{Q}}_{k} \boldsymbol{e}_{1}=\frac{1}{\tilde{r}_{11}^{(k)}} \boldsymbol{A}^{k} \boldsymbol{e}_{1} .
$$

Since $\left\|\tilde{\boldsymbol{q}}_{1}^{(k)}\right\|_{2}=1$ the first column of $\tilde{\boldsymbol{Q}}_{k}$ is the result of applying the normalized power iteration (15.6) to the starting vector $\boldsymbol{x}_{0}=\boldsymbol{e}_{1}$. If this iteration converges we conclude that the first column of $\tilde{\boldsymbol{Q}}_{k}$ must converge to a dominant eigenvector of $\boldsymbol{A}$. It can be shown that the first column of $\boldsymbol{A}_{k}$ must then converge to $\lambda_{1} \boldsymbol{e}_{1}$, where $\lambda_{1}$ is a dominant eigenvalue of $\boldsymbol{A}$. This is clearly what happens in Examples 15.4 and 15.5. Indeed, what is observed in practice is that the sequence $\left(\tilde{\boldsymbol{Q}}_{k}^{*} \boldsymbol{A} \tilde{\boldsymbol{Q}}_{k}\right)_{k}$ converges to a (quasi-triangular) Schur form of $\boldsymbol{A}$.

### 15.2.2 Invariance of the Hessenberg Form

One QR step requires $O\left(n^{3}\right)$ arithmetic operations for a matrix $\boldsymbol{A}$ of order $n$. By an initial reduction of $\boldsymbol{A}$ to upper Hessenberg form $\boldsymbol{H}_{1}$ using Algorithm 14.1, the cost of a QR step can be reduced to $O\left(n^{2}\right)$. Consider a QR step on $\boldsymbol{H}_{1}$. We first determine plane rotations $\boldsymbol{P}_{i, i+1}, i=1, \ldots, n-1$ so that $\boldsymbol{P}_{n-1, n} \cdots \boldsymbol{P}_{1,2} \boldsymbol{H}_{1}=\boldsymbol{R}_{1}$ is upper triangular. The details were described in Sect. 5.6. Thus $\boldsymbol{H}_{1}=\boldsymbol{Q}_{1} \boldsymbol{R}_{1}$, where $\boldsymbol{Q}_{1}=\boldsymbol{P}_{1,2}^{*} \cdots \boldsymbol{P}_{n-1, n}^{*}$ is a QR factorization of $\boldsymbol{H}_{1}$. To finish the QR step we compute $\boldsymbol{R}_{1} \boldsymbol{Q}_{1}=\boldsymbol{R}_{1} \boldsymbol{P}_{1,2}^{*} \cdots \boldsymbol{P}_{n-1, n}^{*}$. This postmultiplication step is illustrated by the Wilkinson diagram in Fig. 15.1.

The postmultiplication by $\boldsymbol{P}_{i, i+1}$ introduces a nonzero in position $(i+1, i)$ leaving the other elements marked by a zero in Fig. 15.1 unchanged. Thus the final
matrix $\boldsymbol{R} \boldsymbol{P}_{1,2}^{*} \cdots \boldsymbol{P}_{n-1, n}^{*}$ is upper Hessenberg and a QR step leaves the Hessenberg form invariant.

In conclusion, to compute $\boldsymbol{A}_{k+1}$ from $\boldsymbol{A}_{k}$ requires $O\left(n^{2}\right)$ arithmetic operations if $\boldsymbol{A}_{k}$ is upper Hessenberg and $O(n)$ arithmetic operations if $\boldsymbol{A}_{k}$ is tridiagonal.

### 15.2.3 Deflation

If a subdiagonal element $a_{i+1, i}$ of an upper Hessenberg matrix $\boldsymbol{A}$ is equal to zero, then the eigenvalues of $\boldsymbol{A}$ are the union of the eigenvalues of the two smaller matrices $A(1: i, 1: i)$ and $A(i+1: n, i+1: n)$. Thus, if during the iteration the $(i+1, i)$ element of $\boldsymbol{A}_{k}$ is sufficiently small then we can continue the iteration on the two smaller submatrices separately.

To see what effect this can have on the eigenvalues of $\boldsymbol{A}$ suppose $\left|a_{i+1, i}^{(k)}\right| \leq \epsilon$. Let $\hat{\boldsymbol{A}}_{k}:=\boldsymbol{A}_{k}-a_{i+1, i}^{(k)} \boldsymbol{e}_{i+1} \boldsymbol{e}_{i}^{T}$ be the matrix obtained from $\boldsymbol{A}_{k}$ by setting the $(i+1, i)$ element equal to zero. Since $\boldsymbol{A}_{k}=\tilde{\boldsymbol{Q}}_{k-1}^{*} \boldsymbol{A} \tilde{\boldsymbol{Q}}_{k-1}$ we have

$$
\hat{\boldsymbol{A}}_{k}=\tilde{\boldsymbol{Q}}_{k-1}^{*}(\boldsymbol{A}+\boldsymbol{E}) \tilde{\boldsymbol{Q}}_{k-1}, \quad \boldsymbol{E}=\tilde{\boldsymbol{Q}}_{k-1}\left(a_{i+1, i}^{(k)} \boldsymbol{e}_{i+1} \boldsymbol{e}_{i}^{T}\right) \tilde{\boldsymbol{Q}}_{k-1}^{*} .
$$

Since $\tilde{\boldsymbol{Q}}_{k-1}$ is unitary, $\|\boldsymbol{E}\|_{F}=\left\|a_{i+1, i}^{(k)} \boldsymbol{e}_{i+1} \boldsymbol{e}_{i}^{T}\right\|_{F}=\left|a_{i+1, i}^{(k)}\right| \leq \epsilon$ and setting $a_{i+1, i}^{(k)}=0$ amounts to a perturbation in the original $\boldsymbol{A}$ of at most $\epsilon$. For how to chose $\epsilon$ see the discussion on page 94-95 in [18].

This deflation occurs often in practice and can with a proper implementation reduce the computation time considerably. It should be noted that to find the eigenvectors of the original matrix one has to continue with some care, see [18].

### 15.3 The Shifted QR Algorithms

Like in the inverse power method it is possible to speed up the convergence by introducing shifts. The explicitly shifted QR algorithm works as follows:

```
A = A
for \( k = 1, 2, . . .
Choose a shift sk
㫴采 = A k - sk I (QR factorization of 10k=sI
```

![](https://cdn.mathpix.com/cropped/750c5f9d-6269-44fe-81e3-a3e4f5704d07-354.jpg?height=42&width=316&top_left_y=1949&top_left_x=278)

```
end
```

Since $\boldsymbol{R}_{k}=\boldsymbol{Q}_{k}^{*}\left(\boldsymbol{A}_{k}-s_{k} \boldsymbol{I}\right)$ we find

$$
\boldsymbol{A}_{k+1}=\boldsymbol{Q}_{k}^{*}\left(\boldsymbol{A}_{k}-s_{k} \boldsymbol{I}\right) \boldsymbol{Q}_{k}+s_{k} \boldsymbol{I}=\boldsymbol{Q}_{k}^{*} \boldsymbol{A}_{k} \boldsymbol{Q}_{k}
$$

and $\boldsymbol{A}_{k+1}$ and $\boldsymbol{A}_{k}$ are unitary similar.
The shifted QR algorithm is related to the power method with shift, cf. Theorem 15.3 and also the inverse power method. In fact the last column of $\boldsymbol{Q}_{k}$ is the result of one iteration of the inverse power method to $\boldsymbol{A}^{*}$ with shift $s_{k}$. Indeed, since $\boldsymbol{A}-s_{k} \boldsymbol{I}=\boldsymbol{Q}_{k} \boldsymbol{R}_{k}$ we have $\left(\boldsymbol{A}-s_{k} \boldsymbol{I}\right)^{*}=\boldsymbol{R}_{k}^{*} \boldsymbol{Q}_{k}^{*}$ and $\left(\boldsymbol{A}-s_{k} \boldsymbol{I}\right)^{*} \boldsymbol{Q}_{k}=\boldsymbol{R}_{k}^{*}$. Thus, since $\boldsymbol{R}_{k}^{*}$ is lower triangular with $n, n$ element $\bar{r}_{n n}^{(k)}$ we find $\left(\boldsymbol{A}-s_{k} \boldsymbol{I}\right)^{*} \boldsymbol{Q}_{k} \boldsymbol{e}_{n}=$ $\boldsymbol{R}_{k}^{*} \boldsymbol{e}_{n}=\bar{r}_{n n}^{(k)} \boldsymbol{e}_{n}$ from which the conclusion follows.

The shift $s_{k}:=\boldsymbol{e}_{n}^{T} \boldsymbol{A}_{k} \boldsymbol{e}_{n}$ is called the Rayleigh quotient shift, while the eigenvalue of the lower right $2 \times 2$ corner of $\boldsymbol{A}_{k}$ closest to the $n, n$ element of $\boldsymbol{A}_{k}$ is called theWilkinson shift. This shift can be used to find complex eigenvalues of a real matrix. The convergence is very fast and at least quadratic both for the Rayleigh quotient shift and the Wilkinson shift.

By doing two QR iterations at a time it is possible to find both real and complex eigenvalues of a real matrix without using complex arithmetic. The corresponding algorithm is called the implicitly shifted QR algorithm.

After having computed the eigenvalues we can compute the eigenvectors in steps. First we find the eigenvectors of the triangular or quasi-triangular matrix. We then compute the eigenvectors of the upper Hessenberg matrix and finally we get the eigenvectors of $\boldsymbol{A}$.

The QR Algorithm without shifts does not always converge. A simple example is given by $\boldsymbol{A}:=?\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$. We obtain $\boldsymbol{A}_{k}=\boldsymbol{A}$ for all $k \in \mathbb{N}$. For convergence of the shifted QR algorithm for unitary upper Hessenberg matrices see [20].

Practical experience indicates that only $O(n)$ iterations are needed to find all eigenvalues of $\boldsymbol{A}$. Thus both the explicit- and implicit shift QR algorithms are normally $O\left(n^{3}\right)$ algorithms.

For further remarks and detailed algorithms see [18].

### 15.4 Exercises Chap. 15

### 15.4.1 Exercises Sect. 15.1

Exercise 15.1 (Orthogonal Vectors) Show that $\boldsymbol{u}$ and $\boldsymbol{A} \boldsymbol{u}-\lambda \boldsymbol{u}$ are orthogonal when $\lambda=\frac{\boldsymbol{u}^{*} \boldsymbol{A} \boldsymbol{u}}{\boldsymbol{u}^{*} \boldsymbol{u}}$.

### 15.5 Review Questions

15.4.1 What is the main use of the power method?
15.4.2 Can the QR method be used to find all eigenvectors of a matrix?
15.4.3 Can the power method be used to find an eigenvalue?
15.4.4 Do the power method converge to an eigenvector corresponding to a complex eigenvalue?
15.4.5 What is the inverse power method?
15.4.6 Give a relation between the QR algorithm and the power method.
15.4.7 How can we make the basic QR algorithm converge faster?

## Part VII <br> Appendix

## Chapter 16 <br> Differentiation of Vector Functions

We give a short introduction to differentiation of vector functions.
For any sufficiently differentiable $f: \mathbb{R}^{n} \rightarrow \mathbb{R}$ we recall that the partial derivative with respect to the $i$ th variable of $f$ is defined by

$$
D_{i} f(\boldsymbol{x}):=\frac{\partial f(\boldsymbol{x})}{\partial x_{i}}:=\lim _{h \rightarrow \mathbf{0}} \frac{f\left(\boldsymbol{x}+h \boldsymbol{e}_{i}\right)-f(\boldsymbol{x})}{h}, \quad \boldsymbol{x} \in \mathbb{R}^{n},
$$

where $\boldsymbol{e}_{i}$ is the $i$ th unit vector in $\mathbb{R}^{n}$. For each $\boldsymbol{x} \in \mathbb{R}^{n}$ we define the gradient $\nabla f(\boldsymbol{x}) \in \mathbb{R}^{n}$, and the hessian $\boldsymbol{H} f=\nabla \nabla^{T} f(\boldsymbol{x}) \in \mathbb{R}^{n \times n}$ of $f$ by

$$
\nabla f:=\left[\begin{array}{c}
D_{1} f \\
\vdots \\
D_{n} f
\end{array}\right], \quad \boldsymbol{H} f:=\nabla \nabla^{T} f:=\left[\begin{array}{ccc}
D_{1} D_{1} f & \cdots & D_{1} D_{n} f \\
\vdots & & \vdots \\
D_{n} D_{1} & \cdots & D_{n} D_{n} f
\end{array}\right],
$$

where $\nabla^{T} f:=(\nabla f)^{T}$ is the row vector gradient. The operators $\nabla \nabla^{T}$ and $\nabla^{T} \nabla$ are quite different. Indeed, $\nabla^{T} \nabla f=D_{1}^{2} f+\cdots+D_{n}^{2} f=: \nabla^{2}$ the Laplacian of $f$, while $\nabla \nabla^{T}$ can be thought of as an outer product resulting in a matrix.

Lemma 16.1 (Product Rules) For $f, g: \mathbb{R}^{n} \rightarrow \mathbb{R}$ we have the product rules

1. $\nabla(f g)=f \nabla g+g \nabla f, \quad \nabla^{T}(f g)=f \nabla^{T} g+g \nabla^{T} f$,
2. $\nabla \nabla^{T}(f g)=\nabla f \nabla^{T} g+\nabla g \nabla^{T} f+f \nabla \nabla^{T} g+g \nabla \nabla^{T} f$.
3. $\nabla^{2}(f g)=2 \nabla^{T} f \nabla g+f \nabla^{2} g+g \nabla^{2} f$.

We define the Jacobian of a vector function $\boldsymbol{f}=\left[f_{1}, \ldots f_{m}\right]^{T}: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$ as the $m, n$ matrix

$$
\nabla^{T} \boldsymbol{f}:=\left[\begin{array}{ccc}
D_{1} f_{1} & \cdots & D_{n} f_{1} \\
\vdots & & \vdots \\
D_{1} f_{m} & \cdots & D_{n} f_{m}
\end{array}\right] .
$$

As an example, if $f(\boldsymbol{x})=f(x, y)=x^{2}-x y+y^{2}$ and $\boldsymbol{g}(x, y):=[f(x, y), x-y]^{T}$ then

$$
\begin{aligned}
& \nabla f(x, y)=\left[\begin{array}{c}
2 x-y \\
-x+2 y
\end{array}\right], \quad \nabla^{T} \boldsymbol{g}(x, y)=\left[\begin{array}{cc}
2 x-y-x+2 y \\
1 & -1
\end{array}\right], \\
& \boldsymbol{H} f(x, y)=\left[\begin{array}{cc}
\frac{\partial^{2} f}{\partial x^{2}} & \frac{\partial^{2} f}{\partial x \partial y} \\
\frac{\partial^{2} f}{\partial y \partial x} & \frac{\partial^{2} f}{\partial y^{2}}
\end{array}\right]=\left[\begin{array}{rr}
2 & -1 \\
-1 & 2
\end{array}\right] .
\end{aligned}
$$

The second order Taylor expansion in $n$ variables can be expressed in terms of the gradient and the hessian.

Lemma 16.2 (Second Order Taylor Expansion) Suppose $f \in C^{2}(\Omega)$, where $\Omega \in \mathbb{R}^{n}$ contains two points $\boldsymbol{x}, \boldsymbol{x}+\boldsymbol{h} \in \Omega$, such that the line segment $L:=\{\boldsymbol{x}+t \boldsymbol{h}:$ $t \in(0,1)\} \subset \Omega$. Then

$$
f(\boldsymbol{x}+\boldsymbol{h})=f(\boldsymbol{x})+\boldsymbol{h}^{T} \nabla f(\boldsymbol{x})+\frac{1}{2} \boldsymbol{h}^{T} \nabla \nabla^{T} f(\boldsymbol{c}) \boldsymbol{h}, \text { for some } \boldsymbol{c} \in L .
$$

Proof Let $g:[0,1] \rightarrow \mathbb{R}$ be defined by $g(t):=f(\boldsymbol{x}+t \boldsymbol{h})$. Then $g \in C^{2}[0,1]$ and by the chain rule

$$
\begin{aligned}
g(0) & =f(\boldsymbol{x}) \quad g(1)=f(\boldsymbol{x}+\boldsymbol{h}), \\
g^{\prime}(t) & =\sum_{i=1}^{n} h_{i} \frac{\partial f(\boldsymbol{x}+t \boldsymbol{h})}{\partial x_{i}}=\boldsymbol{h}^{T} \nabla f(\boldsymbol{x}+t \boldsymbol{h}), \\
g^{\prime \prime}(t) & =\sum_{i=1}^{n} \sum_{j=1}^{n} h_{i} h_{j} \frac{\partial^{2} f(\boldsymbol{x}+t \boldsymbol{h})}{\partial x_{i} \partial x_{j}}=\boldsymbol{h}^{T} \nabla \nabla^{T} f(\boldsymbol{x}+t \boldsymbol{h}) \boldsymbol{h} .
\end{aligned}
$$

Inserting these expressions in the second order Taylor expansion

$$
g(1)=g(0)+g^{\prime}(0)+\frac{1}{2} g^{\prime \prime}(u), \text { for some } u \in(0,1),
$$

we obtain (16.2) with $\boldsymbol{c}=\boldsymbol{x}+u \boldsymbol{h}$. $\square$

The gradient and hessian of some functions involving matrices can be found from the following lemma.

Lemma 16.3 (Functions Involving Matrices) For any $m, n \in \mathbb{N}, \boldsymbol{B} \in \mathbb{R}^{n \times n}, \boldsymbol{C} \in$ $\mathbb{R}^{m \times n}$, and $\boldsymbol{x} \in \mathbb{R}^{n}, \boldsymbol{y} \in \mathbb{R}^{m}$ we have

1. $\nabla\left(\boldsymbol{y}^{T} \boldsymbol{C}\right)=\nabla^{T}(\boldsymbol{C} \boldsymbol{x})=\boldsymbol{C}$,
2. $\nabla\left(\boldsymbol{x}^{T} \boldsymbol{B} \boldsymbol{x}\right)=\left(\boldsymbol{B}+\boldsymbol{B}^{T}\right) \boldsymbol{x}, \quad \nabla^{T}\left(\boldsymbol{x}^{T} \boldsymbol{B} \boldsymbol{x}\right)=\boldsymbol{x}^{T}\left(\boldsymbol{B}+\boldsymbol{B}^{T}\right)$,
3. $\nabla \nabla^{T}\left(\boldsymbol{x}^{T} \boldsymbol{B} \boldsymbol{x}\right)=\boldsymbol{B}+\boldsymbol{B}^{T}$.

Proof

1. We find $D_{i}\left(\boldsymbol{y}^{T} \boldsymbol{C}\right)=\lim _{h \rightarrow 0} \frac{1}{h}\left(\left(\boldsymbol{y}+h \boldsymbol{e}_{i}\right)^{T} \boldsymbol{C}-\boldsymbol{y}^{T} \boldsymbol{C}\right)=\boldsymbol{e}_{i}^{T} \boldsymbol{C}$ and $D_{i}(\boldsymbol{C} \boldsymbol{x})=$ $\lim _{h \rightarrow 0} \frac{1}{h}\left(\boldsymbol{C}\left(\boldsymbol{x}+h \boldsymbol{e}_{i}\right)-\boldsymbol{C} \boldsymbol{x}\right)=\boldsymbol{C} \boldsymbol{e}_{i}$ and 1. follows.
2. Here we find
$$
\begin{aligned}
D_{i}\left(\boldsymbol{x}^{T} \boldsymbol{B} \boldsymbol{x}\right) & =\lim _{h \rightarrow 0} \frac{1}{h}\left(\left(\boldsymbol{x}+h \boldsymbol{e}_{i}\right)^{T} \boldsymbol{B}\left(\boldsymbol{x}+h \boldsymbol{e}_{i}\right)-\boldsymbol{x}^{T} \boldsymbol{B} \boldsymbol{x}\right) \\
& =\lim _{h \rightarrow 0}\left(\boldsymbol{e}_{i}^{T} \boldsymbol{B} \boldsymbol{x}+\boldsymbol{x}^{T} \boldsymbol{B} \boldsymbol{e}_{i}+h \boldsymbol{e}_{i}^{T} \boldsymbol{e}_{i}\right)=\boldsymbol{e}_{i}^{T}\left(\boldsymbol{B}+\boldsymbol{B}^{T}\right) \boldsymbol{x},
\end{aligned}
$$
and the first part of 2. follows. Taking transpose we obtain the second part.
3. Combining 1. and 2. we obtain 3.

## References

1. O. Axelsson, Iterative Solution Methods (Cambridge University Press, 1994)
2. Å. Björck, Numerical Methods in Matrix Computations (Springer, 2015)
3. G.H. Golub, C.F. Van Loan, Matrix Computations, 4th Edition (The John Hopkins University Press, Baltimore, MD, 2013)
4. J.F. Grcar, Mathematicians of gaussian elimination. Not. AMS 58, 782-792 (2011)
5. W. Hackbush, Iterative Solution of Large Sparse Systems of Equations, Second edition (Springer International Publishing, Berlin, 2016)
6. M. Hestenes, E. Stiefel, Methods of conjugate gradients for solving linear systems. J. Res. Natl. Bur. Stand. 29, 409-439 (1952)
7. N.J. Higham, Accuracy and Stability of Numerical Algorithms, Second Edition (SIAM, Philadelphia, 2002)
8. M.W. Hirsch, S. Smale, Differential Equations, Dynamical Systems, and Linear Algebra (Academic Press, San Diego, 1974)
9. R.A. Horn, C.R. Johnson, Topics in Matrix Analysis (Cambridge University Press, Cambridge, UK, 1991)
10. R.A. Horn, C.R. Johnson, Matrix Analysis, Second edition (Cambridge University Press, Cambridge, UK, 2013)
11. P. Lancaster, L. Rodman, Canonical forms for hermitian matrix pairs under strict equivalence and congruence. SIAM Rev. 47, 407-443 (2005)
12. C.L. Lawson, R.J. Hanson, Solving Least Squares Problems (Prentice-Hall, Englewood Cliffs, NJ, 1974)
13. D.C. Lay, S.R. Lay, J.J. McDonald, Linear Algebra and Its Applications (Fifth edition) (Pearson Education Limited, 2016)
14. C. Van Loan, Computational Frameworks for the Fast Fourier Transform (SIAM, Philadelphia, 1992)
15. C.D. Meyer, Matrix Analysis and Applied Linear Algebra. (SIAM, Philadelphia, 2000)
16. G.W. Stewart, Introduction to Matrix Computations (Academic press, New York, 1973)
17. G.W. Stewart, Matrix Algorithms Volume I: Basic Decompositions (SIAM, Philadelphia, 1998)
18. G.W. Stewart, Matrix Algorithms Volume II: Eigensystems (SIAM Philadelphia, 2001)
19. G.W. Stewart, J. Sun, Matrix Perturbation Theory (Academic Press, San Diego, 1990)
20. T.L. Wang, W.B. Gragg, Convergence of the shifted QR algorithm for unitary Hessenberg matrices. Math. Comput. 71, 1473-1496 (2002)
21. J.H. Wilkinson, The Algebraic Eigenvalue Problem (Clarendon Press, Oxford, 1965)
22. D.M. Young, Iterative Solution of Large Linear Systems (Academic Press, New York, 1971)

## Index

A
Absolute error, 181
A-inner product, 279
Algebraic multiplicity, 132
Algorithms
assemble Householder transformations, 326
backsolve, 63
backsolve column oriented, 75
bandcholesky, 89
cg, 286
fastpoisson, 241
findsubintervals, 50
forwardsolve, 63
forwardsolve column oriented, 64
housegen, 110
Householder reduction to Hessenberg form, 325
Householder triangulation, 112
Jacobi, 256
L1U factorization, 73
LDL* factorization, 85
the power method, 338
preconditioned cg, 301
Rayleigh quotient iteration, 341
SOR, 257
spline evaluation, 50
splineint, 50
testing conjugate gradient, 287
trifactor, 36
trisolve, 36
upper Hessenberg linear system, 123
A-norm, 279, 306

B
Back substitution, 58
Bandsemi-cholesky, 94
Biharmonic equation, 235
fast solution method, 249
nine point rule, 250
Block LU theorem, 74

C
Cauchy-Binet formula, 17
Cauchy determinant, 23
Cauchy-Schwarz inequality, 101
Cayley Hamilton Theorem, 148
Central difference, 52
Central difference approximation second derivative, 52
Change of basis matrix, 9
Characteristic equation, 19, 129
Characteristic polynomial, 19, 129
Chebyshev polynomial, 293
Cholesky factorization, 83
Column operations, 16
Column space (span), 10
Companion matrix, 146
Complementary subspaces, 104
Complete pivoting, 70
Complexity of an algorithm, 65
Condition number ill-conditioned, 181
Congruent matrices, 328
Conjugate gradient method, 279 convergence, 288
derivation, 283

Krylov spaces, 289
least squares problem, 308
preconditioning, 299
preconditioning algorithm, 301
preconditioning convergence, 301
Convex combinations, 139, 185, 296
Convex function, 185
Courant-Fischer theorem, 142
Cubic spline
minimal norm, 49

D
Defective matrix, 129
Deflation, 137
Determinant
area of a triangle, 23
Cauchy, 23
Cauchy-Binet, 17
cofactor expansion, 16
definition, 15
elementary operations, 16
plane equation, 22
principal minor, 60
straight line equation, 16
Vandermonde, 23
Dirac delta, 3
Direct sum, 104
Discrete cosine transform, 242
Discrete Fourier transform (DFT), 242, 243
Fourier matrix, 243
Discrete sine transform (DST), 242

E
Eigenpair, 18, 40, 129
eigenvalue, 18
eigenvector, 18
left eigenpair, 143
1D test matrix, 42
right eigenpair, 143
spectrum, 18
Eigenvalue, 40, 129
algebraic multiplicity, 132
characteristic equation, 19, 129
characteristic polynomial, 19, 129
Courant-Fischer theorem, 142
geometric multiplicity, 132
Hoffman-Wielandt theorem, 143
left eigenvalue, 143
location, 318
Rayleigh quotient, 139
right eigenvalue, 143
spectral theorem, 140
spectrum, 129
triangular matrix, 20
Eigenvector, 40, 129
left eigenvector, 143
right eigenvector, 143
Eigenvector expansion, 130
Elementary reflector, 107
Elsner's theorem, 321
Equivalent norms, 173
Euclidian norm, 11
Exams
1977-1, inverse update, 21
1977-2, weighted least squares, 217
1977-3, symmetrize matrix, 53
1978-1, computing the inverse, 79
1979-3, $\boldsymbol{x}^{T} \boldsymbol{A y}$ inequality, 119
1980-2, singular values perturbation, 221
1981-2, perturbed linear equation, 194
1981-3, solving $\boldsymbol{T} \boldsymbol{H} \boldsymbol{x}=\boldsymbol{b}, 79$
1982-1, L1U factorization, 96
1982-2, QL-factorization, 121
1982-3, QL-factorization, 121
1982-4, an A-norm inequality, 190
1983-1, L1U factorization update, 80
1983-2, a least squares problem, 217
1983-3, antisymmetric system, 310
1983-4, cg antisymmetric system, 311
1990-1, U1L factorization, 80
1991-3, Iterative method, 275
1993-2, periodic spline interpolation, 195
1994-2, upper Hessenberg system, 76
1995-4, A orthogonal bases, 190
1996-3, Cayley Hamilton Theorem, 148
2005-1, right or wrong?, 147
2005-2, singular values, 164
2006-1, yes or no, 330
2006-2, QR fact. of band matrices, 122
2008-1, Gauss-Seidel method, 276
2008-2, find QR factorization, 122
2008-3, eigenpairs of Kronecker prod, 234
2009-1, matrix products, 21
2009-2, Gershgorin disks, 331
2009-3, eigenvalues of tridiag matrix, 147
2010-1, Householder transformation, 120
2010-2, eigenvalue perturbations, 331
2011-1, steepest descent, 307
2011-2, polar decomposition, 165
2013-2, a Givens transformation, 123
2013-4, LSQ MATLAB program, 197
2015-1, underdetermined system, 166
2015-2, Cholesky update, 97
2015-3, Rayleigh quotient, 149
2016-1, Norms, Cholesky and SVD, 168
2016-2 Cholesky update, 97

2016-3, operation counts, 124
2017-1, Strassen multiplication, 20
2017-2, SVD , 220
2017-3, an iterative method, 192
2018-1, least square fit, 217
2018-2, Cholesky and Givens, 125
2018-3, $\boldsymbol{A}^{T} \boldsymbol{A}$ inner product, 308
Extension of basis, 104

F
Fast Fourier transform (FFT), 242, 244
recursive FFT, 246
Fill-inn, 238
Finite difference method, 37
Fixed-point, 258
Fixed point form of discrete Poisson equation, 255
Fixed-point iteration, 258
Fourier matrix, 243
Fredholm's alternative, 220
Frobenius norm, 161

G
Gaussian elimination, 59
complete pivoting, 70
interchange matrix, 67
multipliers, 60
pivot, 66
pivoting, 66
pivot row, 66
pivots, 60
pivot vector, 67
scaled partial pivoting, 70
Generalized eigenvectors, 134
Generalized inverse, 209
Geometric multiplicity, 132
Gerschgorin's theorem, 318
Given's rotation, 117
Gradient, 86, 351
Gradient method, 282
Gram-Schmidt, 103

H
Hadamard's inequality, 121
Hessian, 86, 351
Hilbert matrix, 24, 203
Hoffman-Wielandt theorem, 143
Hölder's inequality, 172, 187
Householder transformation, 107

I
Ill-conditioned problem, 181
Inequality
geometric/arithmetic mean, 187
Hölder, 187
Kantorovich, 296
Minkowski, 188
Inner product, 99, 100
inner product norm, 100
Pythagoras' theorem, 102
standard, 11
standard inner product in $\mathbb{C}^{n}$, 100
Inner product space
orthogonal basis, 102
orthonormal basis, 102
Interchange matrix, 67
Inverse power method, 339
Inverse triangle inequality, 173
Iterative method
convergence, 260
Gauss-Seidel, 254
Jacobi, 254
SOR, 254
SOR, convergence, 263
SSOR, 255
Iterative methods, 251

J
Jacobian, 352
Jordan factorization, 134
generalized eigenvectors, 134
Jordan block, 133
Jordan canonical form, 133
principal vectors, 134
Jordan factors, 134

K
Kronecker product, 229
eigenvectors, 231
inverse, 231
left product, 229
mixed product rule, 230
nonsingular, 231
positive definite, 231
propertis, 231
right product, 229
symmetry, 231
transpose, 231
Kronecker sum, 230
nonsingular, 231
positive definite, 231
symmetry, 231
Krylov space, 289

L
Laplacian, 351
LDL theorem, 84
Leading principal block submatrices, 74
Leading principal minor, 60
Leading principal submatrices, 60
Least squares
error analysis, 210
Least squares problem, 199
Least squares solution, 199
Left eigenpair, 143
Left eigenvalue, 143
Left eigenvector, 143
Left triangular, 70
Linear combination
nontrivial, 6
span, 6
Linear system
Cramer's rule, 17
existence and uniqueness, 12, 13
homogeneous, 12
overdetermined, 12
residual vector, 182
square, 12
underdetermined, 12
Linearly dependent, 6
Linearly independent, 6
LSQ, 199
LU factorization, 70
LU theorem, 72

M
Matrix
$\boldsymbol{A}^{*} \boldsymbol{A}, 86$
addition, 3
adjoint, 17
adjoint formula for the inverse, 17
banded, 4
block matrix, 44
block triangular, 46
cofactor, 16
column space (span), 10
companion matrix, 146
computing inverse, 75
conjugate transpose, 3
deflation, 137
diagonal, 4
element-by-element operations, 3
Hadamard product, 3
Hermitian, 3, 43
Hilbert, 24
Hilbert matrix, inverse, 24
idempotent, 146
identity matrix, 3
ill-conditioned, 182
inverse, 13
invertible, 13, 14
Kronecker product, 229
LDL* and LL*, 88
leading principal minor, 60
leading principal submatrices, 60
left inverse, 13
left triangular, 4
lower Hessenberg, 4
lower triangular, 4
LU theorem, 72
multiplication, 3
negative (semi)definite, 86
Neumann series, 270
nilpotent, 146
nonsingular, 12, 13
nonsingular products, 13
nullity, 10
null space (N), 10
operator norm, 176
outer product, 54
outer product expansion, 54
permutation, 66
positive definite, 86
positive semidefinite, 86
principal minor, 60
principal submatrix, 60
product of triangular matrices, 47
quasi-triangular, 139
right inverse, 13
right triangular, 4
row space, 10
scalar multiplication, 3
Schur product, 3
second derivative, 38
Sherman-Morrison formula, 21
similar matrices, 131
similarity transformation, 131
singular, 12, 13
spectral radius, 261, 268
Strassen multiplication, 20
strictly diagonally dominant, 33
symmetric, 3
test matrix, 1D , 41
test matrix, 2D, 229
trace, 19
transpose, 3
triangular, 47
tridiagonal, 4
unit triangular, 48
upper Hessenberg, 4
upper trapezoidal, 111
upper triangular, 4
vec Operation, 226
weakly diagonally dominant, 38
well-conditioned, 182
Matrix norm
consistent norm, 175
Frobenius norm, 161, 174
max norm, 174
operator norm, 175
spectral norm, 178
subordinate norm, 175
sum norm, 174
two-norm, 178
Minimal polynomial, 148
Minkowski's inequality, 172, 188
Mixed product rule, 230

N
Natural ordering, 227
Negative (semi)definite, 86
Neumann series, 270
Nilpotent matrix, 146
Nondefective matrix, 129
Nonsingular matrix, 12
Nontrivial subspaces, 8
Norm, 171
$l_{1}$-norm, 172
$l_{2}$-norm, 172
$l_{\infty}$-norm, 172
absolute norm, 180
continuity, 173
Euclidian norm, 172
infinity-norm, 172
max norm, 172
monotone norm, 180
one-norm, 172
triangle inequality, 171
two-norm, 172
Normal matrix, 137
Normal equations, 200
Null space (N), 10

O
Oblique projection, 104
1D test matrix, 41
Operation count, 64
Operator norm, 176
Optimal relaxation parameter, 265
Optimal step length, 282
Orthogonal matrix, 106
Orthogonal projection, 105
Orthogonal sum, 104
Outer product, 54

P
Paraboloid, 306
Parallelogram identity, 188
Partial pivoting, 69
Permutation matrix, 66
Perpendicular vectors, 102
Pivot vector, 67
Plane rotation, 117
p-norms, 172
Poisson matrix, 227
Poisson problem, 225
five point stencil, 227
nine point scheme, 234
Poisson matrix, 227
variable coefficients, 302
Poisson problem (1D), 37
Polarization identity, 197
Polynomial
degree, 6
linear interpolation, 28
nontrivial, 6
Runge phenomenon, 28
zero, 6
Positive definite, 86, 95
Positive semidefinite, 86, 95
Power method, 335
inverse, 339
Rayleigh quotient iteration, 340
shifted, 339
Preconditioned conjugate gradient method, 279
Preconditioning, 299
Preconditioning matrix, 258
Principal submatrix, 60
Principal vectors, 134

Q
QR algorithm
implicit shift, 346
Rayleigh quotient shift, 346
shifted, 345
Wilkinson shift, 346
QR decomposition, 114
QR factorization, 114
Quadratic form, 86

R
Rank of a matrix, 10
Rate of convergence, 266

Rayleigh quotient, 139
generalized, 150
Rayleigh quotient iteration, 340
Relative error, 181
Residual vector, 182
Richardson's method, 261
Right eigenpair, 143
Right eigenvalue, 143
Right eigenvector, 143
Rotation in the $i, j$-plane, 118
Row operations, 16
Row space, 10

## S

Scalar product, 99
Schur factorization, 136
Schur factors, 136
Second derivative matrix, 38
positive definite, 87
Semi-Cholesky factorization, 91
Sherman-Morrison formula, 21
Shifted power method, 339
Similar matrices, 131
Similarity transformation, 131
Singular value
Courant-Fischer theorem, 213
Hoffman-Wielandt theorem, 215
Singular value factorization (SVF), 157
Singular values, 153
error analysis, 213
well conditioned, 216
Singular vectors, 153
Spectral radius, 261, 268
Spectral theorem, 140
Spectrum, 18, 129
Splitting matrices for J, GS and SOR, 259
Splitting matrix, 258
Standard inner product in $\mathbb{C}^{n}$, 106
Steepest descent, 282
Stencil, 227
Sum of subspaces, 104
Sums of integers, 76
Sylvester's inertia theorem, 328

## T

Trace, 19
Triangle inequality, 171
Triangular matrix
lower triangular, 70
upper triangular, 70
2D test matrix, 229
Two point boundary value problem, 37

U
Unitary matrix, 106
Unit vectors, 3
Upper trapezoidal matrix, 111
Upper triangular, 70

## V

Variable coefficient, 313
Vector
addition, 5
angle, 102
linearly dependent, 6
linearly independent, 6
negative, 5
orthogonal, 102
orthonormal, 102
scalar multiplication, 5
zero, 5
Vector norm, 101, 171
Vector space
basis, 7
change of basis, 10
change of basis matrix, 9
complex, 5
complex inner product space, 100
dimension, 7
dimension formula, sums of subspaces, 9
direct sum, 8
enlarging vectors to a basis, 7
examples of subspaces, 8
existence of basis, 7
finite dimensional, 6
intersection, 8
nontrivial subspaces, 8
normed, 171
orthogonal vectors, 102
real, 5
span, 6
subspace, 8
sum, 8
trivial subspace, 8
union, 8
vectors, 5
Vectorization, 226

## W

Weights, 203

## Z

Zero function, 5

## Editorial Policy

1. Textbooks on topics in the field of computational science and engineering will be considered. They should be written for courses in CSE education. Both graduate and undergraduate textbooks will be published in TCSE. Multidisciplinary topics and multidisciplinary teams of authors are especially welcome.
2. Format: Only works in English will be considered. For evaluation purposes, manuscripts may be submitted in print or electronic form, in the latter case, preferably as pdfor zipped ps-files. Authors are requested to use the LaTeX style files available from Springer at: http://www.springer.com/gp/authors-editors/book-authors-editors/resourcesguidelines/rights-permissions-licensing/manuscript-preparation/5636\#c3324 (Layout \& templates - LaTeX template - contributed books).
Electronic material can be included if appropriate. Please contact the publisher.
3. Those considering a book which might be suitable for the series are strongly advised to contact the publisher or the series editors at an early stage.

## General Remarks

Careful preparation of manuscripts will help keep production time short and ensure a satisfactory appearance of the finished book.

The following terms and conditions hold:
Regarding free copies and royalties, the standard terms for Springer mathematics textbooks hold. Please write to martin.peters@springer.com for details.

Authors are entitled to purchase further copies of their book and other Springer books for their personal use, at a discount of 33.3\% directly from Springer-Verlag.

## Series Editors

Timothy J. Barth
NASA Ames Research Center
NAS Division
Moffett Field, CA 94035, USA
barth@nas.nasa.gov

Michael Griebel
Institut für Numerische Simulation der Universität Bonn
Wegelerstr. 6
53115 Bonn, Germany
griebel@ins.uni-bonn.de

David E. Keyes
Mathematical and Computer Sciences and Engineering
King Abdullah University of Science and Technology
P.O. Box 55455
Jeddah 21534, Saudi Arabia
david.keyes@kaust.edu.sa
and

Department of Applied Physics and Applied Mathematics
Columbia University
500 W. 120 th Street
New York, NY 10027, USA
kd2112@columbia.edu

Risto M. Nieminen
Department of Applied Physics
Aalto University School of Science and Technology
00076 Aalto, Finland
risto.nieminen@tkk.fi
Dirk Roose
Department of Computer Science
Katholieke Universiteit Leuven
Celestijnenlaan 200A
3001 Leuven-Heverlee, Belgium
dirk.roose@cs.kuleuven.be
Tamar Schlick
Department of Chemistry
and Courant Institute
of Mathematical Sciences
New York University
251 Mercer Street
New York, NY 10012, USA
schlick@nyu.edu
Editor for Computational Science and Engineering at Springer:
Martin Peters
Springer-Verlag
Mathematics Editorial
Tiergartenstrasse 17
69121 Heidelberg, Germany
martin.peters@springer.com

## Texts in Computational Science and Engineering

1. H. P. Langtangen, Computational Partial Differential Equations. Numerical Methods and Diffpack Programming. 2nd Edition
2. A. Quarteroni, F. Saleri, P. Gervasio, Scientific Computing with MATLAB and Octave. 4th Edition
3. H. P. Langtangen, Python Scripting for Computational Science. 3rd Edition
4. H. Gardner, G. Manduchi, Design Patterns for e-Science.
5. M. Griebel, S. Knapek, G. Zumbusch, Numerical Simulation in Molecular Dynamics.
6. H. P. Langtangen, A Primer on Scientific Programming with Python. 5th Edition
7. A. Tveito, H. P. Langtangen, B. F. Nielsen, X. Cai, Elements of Scientific Computing.
8. B. Gustafsson, Fundamentals of Scientific Computing.
9. M. Bader, Space-Filling Curves.
10. M. Larson, F. Bengzon, The Finite Element Method: Theory, Implementation and Applications.
11. W. Gander, M. Gander, F. Kwok, Scientific Computing: An Introduction using Maple and MATLAB.
12. P. Deuflhard, S. Röblitz, A Guide to Numerical Modelling in Systems Biology.
13. M. H. Holmes, Introduction to Scientific Computing and Data Analysis.
14. S. Linge, H. P. Langtangen, Programming for Computations - A Gentle Introduction to Numerical Simulations with MATLAB/Octave.
15. S. Linge, H. P. Langtangen, Programming for Computations - A Gentle Introduction to Numerical Simulations with Python.
16. H.P. Langtangen, S. Linge, Finite Difference Computing with PDEs - A Modern Software Approach.
17. B. Gustafsson, Scientific Computing from a Historical Perspective
18. J.A. Trangenstein, Scientific Computing - Vol. I. - Linear and Nonlinear Equations
19. J.A. Trangenstein, Scientific Computing - Vol. II. - Eigenvalues and Optimization
20. J.A. Trangenstein, Scientific Computing - Vol. III. - Approximation and Integration
21. H.P. Langtangen, K.-A. Mardal, Introduction to Numerical Methods for Variational Problems.
22. T. Lyche, Numerical Linear Algebra and Matrix Factorizations.

For further information on these books please have a look at our mathematics catalogue at the following URL: www.springer.com/series/5151

## Monographs in Computational Science and Engineering

1. J. Sundnes, G.T. Lines, X. Cai, B.F. Nielsen, K.-A. Mardal, A. Tveito, Computing the Electrical Activity in the Heart.

For further information on this book, please have a look at our mathematics catalogue at the following URL: www.springer.com/series/7417

## Lecture Notes in Computational Science and Engineering

1. D. Funaro, Spectral Elements for Transport-Dominated Equations.
2. H.P. Langtangen, Computational Partial Differential Equations. Numerical Methods and Diffpack Programming.
3. W. Hackbusch, G. Wittum (eds.), Multigrid Methods V.
4. P. Deuflhard, J. Hermans, B. Leimkuhler, A.E. Mark, S. Reich, R.D. Skeel (eds.), Computational Molecular Dynamics: Challenges, Methods, Ideas.
5. D. Kröner, M. Ohlberger, C. Rohde (eds.), An Introduction to Recent Developments in Theory and Numerics for Conservation Laws.
6. S. Turek, Efficient Solvers for Incompressible Flow Problems. An Algorithmic and Computational Approach.
7. R. von Schwerin, Multi Body System SIMulation. Numerical Methods, Algorithms, and Software.
8. H.-J. Bungartz, F. Durst, C. Zenger (eds.), High Performance Scientific and Engineering Computing.
9. T.J. Barth, H. Deconinck (eds.), High-Order Methods for Computational Physics.
10. H.P. Langtangen, A.M. Bruaset, E. Quak (eds.), Advances in Software Tools for Scientific Computing.
11. B. Cockburn, G.E. Karniadakis, C.-W. Shu (eds.), Discontinuous Galerkin Methods. Theory, Computation and Applications.
12. U. van Rienen, Numerical Methods in Computational Electrodynamics. Linear Systems in Practical Applications.
13. B. Engquist, L. Johnsson, M. Hammill, F. Short (eds.), Simulation and Visualization on the Grid.
14. E. Dick, K. Riemslagh, J. Vierendeels (eds.), Multigrid Methods VI.
15. A. Frommer, T. Lippert, B. Medeke, K. Schilling (eds.), Numerical Challenges in Lattice Quantum Chromodynamics.
16. J. Lang, Adaptive Multilevel Solution of Nonlinear Parabolic PDE Systems. Theory, Algorithm, and Applications.

17. B.I. Wohlmuth, Discretization Methods and Iterative Solvers Based on Domain Decomposition.
18. U. van Rienen, M. Günther, D. Hecht (eds.), Scientific Computing in Electrical Engineering.
19. I. Babuška, P.G. Ciarlet, T. Miyoshi (eds.), Mathematical Modeling and Numerical Simulation in Continuum Mechanics.
20. T.J. Barth, T. Chan, R. Haimes (eds.), Multiscale and Multiresolution Methods. Theory and Applications.
21. M. Breuer, F. Durst, C. Zenger (eds.), High Performance Scientific and Engineering Computing.
22. K. Urban, Wavelets in Numerical Simulation. Problem Adapted Construction and Applications.
23. L.F. Pavarino, A. Toselli (eds.), Recent Developments in Domain Decomposition Methods.
24. T. Schlick, H.H. Gan (eds.), Computational Methods for Macromolecules: Challenges and Applications.
25. T.J. Barth, H. Deconinck (eds.), Error Estimation and Adaptive Discretization Methods in Computational Fluid Dynamics.
26. M. Griebel, M.A. Schweitzer (eds.), Meshfree Methods for Partial Differential Equations.
27. S. Müller, Adaptive Multiscale Schemes for Conservation Laws.
28. C. Carstensen, S. Funken, W. Hackbusch, R.H.W. Hoppe, P. Monk (eds.), Computational Electromagnetics.
29. M.A. Schweitzer, A Parallel Multilevel Partition of Unity Method for Elliptic Partial Differential Equations.
30. T. Biegler, O. Ghattas, M. Heinkenschloss, B. van Bloemen Waanders (eds.), Large-Scale PDE-Constrained Optimization.
31. M. Ainsworth, P. Davies, D. Duncan, P. Martin, B. Rynne (eds.), Topics in Computational Wave Propagation. Direct and Inverse Problems.
32. H. Emmerich, B. Nestler, M. Schreckenberg (eds.), Interface and Transport Dynamics. Computational Modelling.
33. H.P. Langtangen, A. Tveito (eds.), Advanced Topics in Computational Partial Differential Equations. Numerical Methods and Diffpack Programming.
34. V. John, Large Eddy Simulation of Turbulent Incompressible Flows. Analytical and Numerical Results for a Class of LES Models.
35. E. Bänsch (ed.), Challenges in Scientific Computing - CISC 2002.
36. B.N. Khoromskij, G. Wittum, Numerical Solution of Elliptic Differential Equations by Reduction to the Interface.
37. A. Iske, Multiresolution Methods in Scattered Data Modelling.
38. S.-I. Niculescu, K. Gu (eds.), Advances in Time-Delay Systems.
39. S. Attinger, P. Koumoutsakos (eds.), Multiscale Modelling and Simulation.
40. R. Kornhuber, R. Hoppe, J. Périaux, O. Pironneau, O. Wildlund, J. Xu (eds.), Domain Decomposition Methods in Science and Engineering.
41. T. Plewa, T. Linde, V.G. Weirs (eds.), Adaptive Mesh Refinement - Theory and Applications.
42. A. Schmidt, K.G. Siebert, Design of Adaptive Finite Element Software. The Finite Element Toolbox ALBERTA.

43. M. Griebel, M.A. Schweitzer (eds.), Meshfree Methods for Partial Differential Equations II.
44. B. Engquist, P. Lötstedt, O. Runborg (eds.), Multiscale Methods in Science and Engineering.
45. P. Benner, V. Mehrmann, D.C. Sorensen (eds.), Dimension Reduction of Large-Scale Systems.
46. D. Kressner, Numerical Methods for General and Structured Eigenvalue Problems.
47. A. Boriçi, A. Frommer, B. Joó, A. Kennedy, B. Pendleton (eds.), QCD and Numerical Analysis III.
48. F. Graziani (ed.), Computational Methods in Transport.
49. B. Leimkuhler, C. Chipot, R. Elber, A. Laaksonen, A. Mark, T. Schlick, C. Schütte, R. Skeel (eds.), New Algorithms for Macromolecular Simulation.
50. M. Bücker, G. Corliss, P. Hovland, U. Naumann, B. Norris (eds.), Automatic Differentiation: Applications, Theory, and Implementations.
51. A.M. Bruaset, A. Tveito (eds.), Numerical Solution of Partial Differential Equations on Parallel Computers.
52. K.H. Hoffmann, A. Meyer (eds.), Parallel Algorithms and Cluster Computing.
53. H.-J. Bungartz, M. Schäfer (eds.), Fluid-Structure Interaction.
54. J. Behrens, Adaptive Atmospheric Modeling.
55. O. Widlund, D. Keyes (eds.), Domain Decomposition Methods in Science and Engineering XVI.
56. S. Kassinos, C. Langer, G. Iaccarino, P. Moin (eds.), Complex Effects in Large Eddy Simulations.
57. M. Griebel, M.A Schweitzer (eds.), Meshfree Methods for Partial Differential Equations III.
58. A.N. Gorban, B. Kégl, D.C. Wunsch, A. Zinovyev (eds.), Principal Manifolds for Data Visualization and Dimension Reduction.
59. H. Ammari (ed.), Modeling and Computations in Electromagnetics: A Volume Dedicated to Jean-Claude Nédélec.
60. U. Langer, M. Discacciati, D. Keyes, O. Widlund, W. Zulehner (eds.), Domain Decomposition Methods in Science and Engineering XVII.
61. T. Mathew, Domain Decomposition Methods for the Numerical Solution of Partial Differential Equations.
62. F. Graziani (ed.), Computational Methods in Transport: Verification and Validation.
63. M. Bebendorf, Hierarchical Matrices. A Means to Efficiently Solve Elliptic Boundary Value Problems.
64. C.H. Bischof, H.M. Bücker, P. Hovland, U. Naumann, J. Utke (eds.), Advances in Automatic Differentiation.
65. M. Griebel, M.A. Schweitzer (eds.), Meshfree Methods for Partial Differential Equations IV.
66. B. Engquist, P. Lötstedt, O. Runborg (eds.), Multiscale Modeling and Simulation in Science.
67. I.H. Tuncer, Ü. Gülcat, D.R. Emerson, K. Matsuno (eds.), Parallel Computational Fluid Dynamics 2007.
68. S. Yip, T. Diaz de la Rubia (eds.), Scientific Modeling and Simulations.
69. A. Hegarty, N. Kopteva, E. O'Riordan, M. Stynes (eds.), BAIL 2008 - Boundary and Interior Layers.
70. M. Bercovier, M.J. Gander, R. Kornhuber, O. Widlund (eds.), Domain Decomposition Methods in Science and Engineering XVIII.
71. B. Koren, C. Vuik (eds.), Advanced Computational Methods in Science and Engineering.
72. M. Peters (ed.), Computational Fluid Dynamics for Sport Simulation.
73. H.-J. Bungartz, M. Mehl, M. Schäfer (eds.), Fluid Structure Interaction II - Modelling, Simulation, Optimization.
74. D. Tromeur-Dervout, G. Brenner, D.R. Emerson, J. Erhel (eds.), Parallel Computational Fluid Dynamics 2008.
75. A.N. Gorban, D. Roose (eds.), Coping with Complexity: Model Reduction and Data Analysis.
76. J.S. Hesthaven, E.M. Rønquist (eds.), Spectral and High Order Methods for Partial Differential Equations.
77. M. Holtz, Sparse Grid Quadrature in High Dimensions with Applications in Finance and Insurance.
78. Y. Huang, R. Kornhuber, O.Widlund, J. Xu (eds.), Domain Decomposition Methods in Science and Engineering XIX.
79. M. Griebel, M.A. Schweitzer (eds.), Meshfree Methods for Partial Differential Equations V.
80. P.H. Lauritzen, C. Jablonowski, M.A. Taylor, R.D. Nair (eds.), Numerical Techniques for Global Atmospheric Models.
81. C. Clavero, J.L. Gracia, F.J. Lisbona (eds.), BAIL 2010 - Boundary and Interior Layers, Computational and Asymptotic Methods.
82. B. Engquist, O. Runborg, Y.R. Tsai (eds.), Numerical Analysis and Multiscale Computations.
83. I.G. Graham, T.Y. Hou, O. Lakkis, R. Scheichl (eds.), Numerical Analysis of Multiscale Problems.
84. A. Logg, K.-A. Mardal, G. Wells (eds.), Automated Solution of Differential Equations by the Finite Element Method.
85. J. Blowey, M. Jensen (eds.), Frontiers in Numerical Analysis - Durham 2010.
86. O. Kolditz, U.-J. Gorke, H. Shao, W. Wang (eds.), Thermo-Hydro-Mechanical-Chemical Processes in Fractured Porous Media - Benchmarks and Examples.
87. S. Forth, P. Hovland, E. Phipps, J. Utke, A. Walther (eds.), Recent Advances in Algorithmic Differentiation.
88. J. Garcke, M. Griebel (eds.), Sparse Grids and Applications.
89. M. Griebel, M.A. Schweitzer (eds.), Meshfree Methods for Partial Differential Equations VI.
90. C. Pechstein, Finite and Boundary Element Tearing and Interconnecting Solvers for Multiscale Problems.
91. R. Bank, M. Holst, O. Widlund, J. Xu (eds.), Domain Decomposition Methods in Science and Engineering $X X$.
92. H. Bijl, D. Lucor, S. Mishra, C. Schwab (eds.), Uncertainty Quantification in Computational Fluid Dynamics.
93. M. Bader, H.-J. Bungartz, T. Weinzierl (eds.), Advanced Computing.
94. M. Ehrhardt, T. Koprucki (eds.), Advanced Mathematical Models and Numerical Techniques for Multi-Band Effective Mass Approximations.
95. M. Azaïez, H. El Fekih, J.S. Hesthaven (eds.), Spectral and High Order Methods for Partial Differential Equations ICOSAHOM 2012.
96. F. Graziani, M.P. Desjarlais, R. Redmer, S.B. Trickey (eds.), Frontiers and Challenges in Warm Dense Matter.
97. J. Garcke, D. Pflüger (eds.), Sparse Grids and Applications - Munich 2012.
98. J. Erhel, M. Gander, L. Halpern, G. Pichot, T. Sassi, O. Widlund (eds.), Domain Decomposition Methods in Science and Engineering XXI.
99. R. Abgrall, H. Beaugendre, P.M. Congedo, C. Dobrzynski, V. Perrier, M. Ricchiuto (eds.), High Order Nonlinear Numerical Methods for Evolutionary PDEs - HONOM 2013.
100. M. Griebel, M.A. Schweitzer (eds.), Meshfree Methods for Partial Differential Equations VII.
101. R. Hoppe (ed.), Optimization with PDE Constraints - OPTPDE 2014.
102. S. Dahlke, W. Dahmen, M. Griebel, W. Hackbusch, K. Ritter, R. Schneider, C. Schwab, H. Yserentant (eds.), Extraction of Quantifiable Information from Complex Systems.
103. A. Abdulle, S. Deparis, D. Kressner, F. Nobile, M. Picasso (eds.), Numerical Mathematics and Advanced Applications - ENUMATH 2013.
104. T. Dickopf, M.J. Gander, L. Halpern, R. Krause, L.F. Pavarino (eds.), Domain Decomposition Methods in Science and Engineering XXII.
105. M. Mehl, M. Bischoff, M. Schäfer (eds.), Recent Trends in Computational Engineering - CE2014. Optimization, Uncertainty, Parallel Algorithms, Coupled and Complex Problems.
106. R.M. Kirby, M. Berzins, J.S. Hesthaven (eds.), Spectral and High Order Methods for Partial Differential Equations - ICOSAHOM'14.
107. B. Jüttler, B. Simeon (eds.), Isogeometric Analysis and Applications 2014.
108. P. Knobloch (ed.), Boundary and Interior Layers, Computational and Asymptotic Methods - BAIL 2014.
109. J. Garcke, D. Pflüger (eds.), Sparse Grids and Applications - Stuttgart 2014.
110. H. P. Langtangen, Finite Difference Computing with Exponential Decay Models.
111. A. Tveito, G.T. Lines, Computing Characterizations of Drugs for Ion Channels and Receptors Using Markov Models.
112. B. Karazösen, M. Manguoğlu, M. Tezer-Sezgin, S. Göktepe, Ö. Uğur (eds.), Numerical Mathematics and Advanced Applications - ENUMATH 2015.
113. H.-J. Bungartz, P. Neumann, W.E. Nagel (eds.), Software for Exascale Computing - SPPEXA 2013-2015.
114. G.R. Barrenechea, F. Brezzi, A. Cangiani, E.H. Georgoulis (eds.), Building Bridges: Connections and Challenges in Modern Approaches to Numerical Partial Differential Equations.
115. M. Griebel, M.A. Schweitzer (eds.), Meshfree Methods for Partial Differential Equations VIII.
116. C.-O. Lee, X.-C. Cai, D.E. Keyes, H.H. Kim, A. Klawonn, E.-J. Park, O.B. Widlund (eds.), Domain Decomposition Methods in Science and Engineering XXIII.
117. T. Sakurai, S. Zhang, T. Imamura, Y. Yusaku, K. Yoshinobu, H. Takeo (eds.), Eigenvalue Problems: Algorithms, Software and Applications, in Petascale Computing. EPASA 2015, Tsukuba, Japan, September 2015.
118. T. Richter (ed.), Fluid-structure Interactions. Models, Analysis and Finite Elements.

119. M.L. Bittencourt, N.A. Dumont, J.S. Hesthaven (eds.), Spectral and High Order Methods for Partial Differential Equations ICOSAHOM 2016.
120. Z. Huang, M. Stynes, Z. Zhang (eds.), Boundary and Interior Layers, Computational and Asymptotic Methods BAIL 2016.
121. S.P.A. Bordas, E.N. Burman, M.G. Larson, M.A. Olshanskii (eds.), Geometrically Unfitted Finite Element Methods and Applications. Proceedings of the UCL Workshop 2016.
122. A. Gerisch, R. Penta, J. Lang (eds.), Multiscale Models in Mechano and Tumor Biology. Modeling, Homogenization, and Applications.
123. J. Garcke, D. Pflüger, C.G. Webster, G. Zhang (eds.), Sparse Grids and Applications - Miami 2016.
124. M. Schäfer, M. Behr, M. Mehl, B. Wohlmuth (eds.), Recent Advances in Computational Engineering. Proceedings of the 4th International Conference on Computational Engineering (ICCE 2017) in Darmstadt.
125. P.E. Bjørstad, S.C. Brenner, L. Halpern, R. Kornhuber, H.H. Kim, T. Rahman, O.B. Widlund (eds.), Domain Decomposition Methods in Science and Engineering XXIV. 24th International Conference on Domain Decomposition Methods, Svalbard, Norway, February 6-10, 2017.
126. F.A. Radu, K. Kumar, I. Berre, J.M. Nordbotten, I.S. Pop (eds.), Numerical Mathematics and Advanced Applications - ENUMATH 2017.
127. X. Roca, A. Loseille (eds.), 27th International Meshing Roundtable.
128. Th. Apel, U. Langer, A. Meyer, O. Steinbach (eds.), Advanced Finite Element Methods with Applications. Selected Papers from the 30th Chemnitz Finite Element Symposium 2017.
129. M. Griebel, M. A. Schweitzer (eds.), Meshfree Methods for Partial Differencial Equations IX.
130. S. Weißer, BEM-based Finite Element Approaches on Polytopal Meshes.
131. V. A. Garanzha, L. Kamenski, H. Si (eds.), Numerical Geometry, Grid Generation and Scientific Computing. Proceedings of the 9th International Conference, NUMGRID 2018/Voronoi 150, Celebrating the 150th Anniversary of G. F. Voronoi, Moscow, Russia, December 2018.
132. E. H. van Brummelen, A. Corsini, S. Perotto, G. Rozza (eds.), Numerical Methods for Flows.

For further information on these books please have a look at our mathematics catalogue at the following URL: www.springer.com/series/3527


[^0]:    ${ }^{1}$ The word "eigen" is derived from German and means "own".

[^1]:    ${ }^{2}$ Hint: $A(T)=A\left(A B P_{3} P_{1}\right)+A\left(P_{3} B C P_{2}\right)-A\left(P_{1} A C P_{2}\right)$, c.f. Fig. 1.1.
    ${ }^{3}$ Hint: subtract $x_{n}^{k}$ times column $k$ from column $k+1$ for $k=n-1, n-2, \ldots, 1$.

[^2]:    ${ }^{1}$ This is due to the fact that the sites are uniformly spaced. High degree interpolation converges uniformly to the function being interpolated when a sequence consisting of the extrema of the Chebyshev polynomial of increasing degree is used as sites. This is not true for any continuous function (the Faber theorem), but holds if the function is Lipschitz continuous.

[^3]:    ${ }^{2}$ We show in Sect. 3.3.2 that Gaussian elimination on a full $n \times n$ system is an $O\left(n^{3}\right)$ process.

[^4]:    ${ }^{3}$ Hint: consider an arbitrary polynomial of degree $n$ and expanded it in Taylor series around $x_{i}$.
    ${ }^{4}$ Hint, use Theorem 2.2.

[^5]:    ${ }^{5}$ The name spline is inherited from a"physical analogue", an elastic ruler that is used to draw smooth curves. Heavy weights, called ducks, are used to force the ruler to pass through, or near given locations. The ruler will take a shape that minimizes its potential energy. Since the potential energy is proportional to the integral of the square of the curvature, and the curvature can be approximated by the second derivative it follows from Theorem 2.5 that the mathematical $N$-spline approximately models the physical spline.

[^6]:    ${ }^{1}$ The method was known long before Gauss used it in 1809. It was further developed by Doolittle in 1881, see [4].

[^7]:    ${ }^{2}$ Hint: Consider the cases $2 \leq k \leq d$ and $d+1 \leq k \leq n$ separately.

[^8]:    ${ }^{1}$ Hint: The matrix $\boldsymbol{E}^{-1}$ is of the form $\boldsymbol{E}^{-1}=\boldsymbol{I}+a \boldsymbol{u} \boldsymbol{u}^{T}$ for some $a \in \mathbb{R}$.

[^9]:    ${ }^{1}$ Show that we have equality $\Longleftrightarrow \boldsymbol{R}$ is diagonal $\Longleftrightarrow \boldsymbol{A}^{*} \boldsymbol{A}$ is diagonal.

[^10]:    ${ }^{2}$ Consider the matrix $\boldsymbol{Q}^{T} \boldsymbol{A}_{-}$.

[^11]:    ${ }^{1}$ This can also be shown without using the Jordan factorization, see [9].

[^12]:    ${ }^{2}$ Hint: show that there is a diagonal matrix $\boldsymbol{D}$ such that $\boldsymbol{D}^{-1} \boldsymbol{A} \boldsymbol{D}$ is symmetric.

[^13]:    ${ }^{3}$ Hint: use a suitable factorization of $p$ and use c).

[^14]:    ${ }^{4}$ Hint: Use Taylor's theorem for the function $f(t)=R(\boldsymbol{x}-t \boldsymbol{y})$.

[^15]:    ${ }^{1}$ Answer: $\boldsymbol{A}=\frac{1}{5}\left[\begin{array}{cc}3 & -4 \\ 4 & 3\end{array}\right]\left[\begin{array}{ll}3 & 0 \\ 0 & 1\end{array}\right] \frac{1}{5}\left[\begin{array}{cc}3 & 4 \\ 4 & -3\end{array}\right]$.
    ${ }^{2}$ Hint: Take the transpose of the matrix in (7.2).

[^16]:    ${ }^{1}$ In the case of one vector norm $\left\|\|\right.$ on $\mathbb{C}^{m}$ and another vector norm $\| \|_{\beta}$ on $\mathbb{C}^{n}$ we would define $\|\boldsymbol{A}\|:=\max _{\boldsymbol{x} \neq 0} \frac{\|\boldsymbol{A} \boldsymbol{x}\|}{\|\boldsymbol{x}\| \beta}$.

[^17]:    ${ }^{2}$ Hint: Show that $\left\|\tilde{\boldsymbol{b}}_{1}\right\|_{\boldsymbol{A}}^{2} \cdots\left\|\tilde{\boldsymbol{b}}_{n}\right\|_{\boldsymbol{A}}^{2}=\operatorname{det}(\boldsymbol{A})$.

[^18]:    ${ }^{3}$ Hint: use Gershgorin's theorem.

[^19]:    ${ }^{4}$ Hint: We have $\langle\boldsymbol{x}, \boldsymbol{y}\rangle=s(\boldsymbol{x}, \boldsymbol{y})+i s(\boldsymbol{x}, i \boldsymbol{y})$, where $s(\boldsymbol{x}, \boldsymbol{y}):=\frac{1}{4}\left(\|\boldsymbol{x}+\boldsymbol{y}\|^{2}-\|\boldsymbol{x}-\boldsymbol{y}\|^{2}\right)$.

[^20]:    ${ }^{1}$ It is possible to compute $\boldsymbol{V}$ using only two matrix multiplications and hence reduce the complexity to $O\left(4 n^{3 / 2}\right)$. This is detailed in Problem 11.4.

[^21]:    ${ }^{1}$ Stewart Venit, "The convergence of Jacobi and Gauss-Seidel iteration", Mathematics Magazine 48 (1975), 163-167.

[^22]:    ${ }^{2}$ Hint: The function C=tril(A) extracts the lower part of A into a lower triangular matrix C.

[^23]:    ${ }^{1}$ It is this property that has given the method its name.

[^24]:    ${ }^{2}$ Hint: use induction on $k$ to show that $\boldsymbol{p}_{k}=\boldsymbol{r}_{k}+\sum_{j=0}^{k-1} a_{k, j} \boldsymbol{r}_{j}$ for some constants $a_{k, j}$.
    ${ }^{3}$ Hint: The conjugate gradient method for $\boldsymbol{A} \boldsymbol{y}=\boldsymbol{r}_{0}$ can be written $\boldsymbol{y}_{k+1}:=\boldsymbol{y}_{k}+\gamma_{k} \boldsymbol{q}_{k}, \gamma_{k}:=$ $\frac{\boldsymbol{s}_{k}^{T} \boldsymbol{s}_{k}}{\boldsymbol{q}_{k}^{T} \boldsymbol{A} \boldsymbol{q}_{k}}, \boldsymbol{s}_{k+1}:=\boldsymbol{s}_{k}-\gamma_{k} \boldsymbol{A} \boldsymbol{q}_{k}, \boldsymbol{q}_{k+1}:=\boldsymbol{s}_{k+1}+\delta_{k} \boldsymbol{q}_{k}, \delta_{k}:=\frac{\boldsymbol{s}_{k+1}^{T} \boldsymbol{s}_{k+1}}{\boldsymbol{s}_{k}^{T} \boldsymbol{s}_{k}}$. Show that $\boldsymbol{y}_{k}=\boldsymbol{x}_{k}-\boldsymbol{x}_{0}$, $\boldsymbol{s}_{k}=\boldsymbol{r}_{k}$, and $\boldsymbol{q}_{k}=\boldsymbol{p}_{k}$, for $k=0,1,2 \ldots$.

[^25]:    ${ }^{4}$ This system known as the normal equations appears in linear least squares problems and was considered in this context in Chap. 9.

[^26]:    ${ }^{5}$ Hint: Show that $\boldsymbol{A}^{-1}\left(\boldsymbol{r}_{k+1}-\boldsymbol{r}_{j}\right) \in \mathcal{W}_{k+1}$.


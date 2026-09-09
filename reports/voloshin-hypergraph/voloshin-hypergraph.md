INTRODUCTION TO Graph and Hypergraph Theory

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-001.jpg?height=1072&width=1403&top_left_y=977&top_left_x=171)
Vitaly I. Voloshin

## Introduction to Graph and Hypergraph Theory

No part of this digital document may be reproduced, stored in a retrieval system or transmitted in any form or by any means. The publisher has taken reasonable care in the preparation of this digital document, but makes no expressed or implied warranty of any kind and assumes no responsibility for any errors or omissions. No liability is assumed for incidental or consequential damages in connection with or arising out of information contained herein. This digital document is sold with the clear understanding that the publisher is not engaged in rendering legal, medical or any other professional services.

# Introduction to Graph and Hypergraph Theory 

Vitaly I. Voloshin

Nova Science Publishers, Inc.
New York

All rights reserved. No part of this book may be reproduced, stored in a retrieval system or transmitted in any form or by any means: electronic, electrostatic, magnetic, tape, mechanical photocopying, recording or otherwise without the written permission of the Publisher.

For permission to use material from this book please contact us:
Telephone 631-231-7269; Fax 631-231-8175
Web Site: http://www.novapublishers.com

## NOTICE TO THE READER

The Publisher has taken reasonable care in the preparation of this book, but makes no expressed or implied warranty of any kind and assumes no responsibility for any errors or omissions. No liability is assumed for incidental or consequential damages in connection with or arising out of information contained in this book. The Publisher shall not be liable for any special, consequential, or exemplary damages resulting, in whole or in part, from the readers' use of, or reliance upon, this material.

Independent verification should be sought for any data, advice or recommendations contained in this book. In addition, no responsibility is assumed by the publisher for any injury and/or damage to persons or property arising from any methods, products, instructions, ideas or otherwise contained in this publication.

This publication is designed to provide accurate and authoritative information with regard to the subject matter cover herein. It is sold with the clear understanding that the Publisher is not engaged in rendering legal or any other professional services. If legal, medical or any other expert assistance is required, the services of a competent person should be sought. FROM A DECLARATION OF PARTICIPANTS JOINTLY ADOPTED BY A COMMITTEE OF THE AMERICAN BAR ASSOCIATION AND A COMMITTEE OF PUBLISHERS.

Library of Congress Cataloging-in-Publication Data
Voloshin, Vitaly I. (Vitaly Ivanovich), 1954-
Introduction to graph and hypergraph theory / Vitaly I. Voloshin.
p. cm.
Includes index.
ISBN978-1-61470-112-5 (eBook)

1. Graph theory. 2. Hypergraphs. I. Title.
QA166.V649 2009
511'.5-dc22
2008047206

To Julian, Olesea and Georgeta for unlimited love and support

The Essence of Mathematics is in its generalizations,

The Beauty of Mathematics is in its ideas,

The Power of Mathematics is in its absolute truth...

## Contents

Preface ..... xi
I Graphs ..... 1
1 Basic Definitions and Concepts ..... 5
1.1. Fundamentals ..... 5
1.2. Graph Modeling Applications ..... 8
1.3. Graph Representations ..... 12
1.4. Generalizations ..... 15
1.5. Basic Graph Classes ..... 18
1.6. Basic Graph Operations ..... 25
1.7. Basic Subgraphs ..... 29
1.8. Separation and Connectivity ..... 34
2 Trees and Bipartite Graphs ..... 39
2.1. Trees and Cycles ..... 39
2.2. Trees and Distance ..... 41
2.3. Minimum Spanning Tree ..... 43
2.4. Bipartite Graphs ..... 45
3 Chordal Graphs ..... 51
3.1. Preliminary ..... 51
3.2. Separators and Simplicial Vertices ..... 52
3.3. Degrees ..... 57
3.4. Distances in Chordal Graphs ..... 59
3.5. Quasi-triangulated Graphs ..... 62
4 Planar Graphs ..... 67
4.1. Plane and Planar Graphs ..... 67
4.2. Euler's Formula ..... 69
4.3. $K_{5}$ and $K_{3,3}$ Are not Planar Graphs ..... 71
4.4. Kuratowski's Theorem and Planarity Testing ..... 73
4.5. Plane Triangulations and Dual Graphs ..... 76
5 Graph Coloring ..... 79
5.1. Preliminary ..... 79
5.2. Definitions and Examples ..... 80
5.3. Structure of Colorings ..... 83
5.4. Chromatic Polynomial ..... 89
5.5. Coloring Chordal Graphs ..... 95
5.6. Coloring Planar Graphs ..... 102
5.7. Perfect Graphs ..... 108
5.8. Edge Coloring and Vizing's Theorem ..... 112
5.9. Upper Chromatic Index ..... 116
6 Traversals and Flows ..... 123
6.1. Eulerian Graphs ..... 123
6.2. Hamiltonian Graphs ..... 125
6.3. Network Flows ..... 127
II Hypergraphs ..... 131
7 Basic Hypergraph Concepts ..... 135
7.1. Preliminary Definitions ..... 135
7.2. Incidence and Duality ..... 139
7.3. Basic Hypergraph Classes ..... 144
7.4. Basic Hypergraph Operations ..... 146
7.5. Subhypergraphs ..... 151
7.6. Conformality and Helly Property ..... 154
8 Hypertrees and Chordal Hypergraphs ..... 161
8.1. Hypertrees and Chordal Conformal Hypergraphs ..... 161
8.2. Algorithms on Hypertrees ..... 168
8.3. Cyclomatic Number of a Hypergraph ..... 174
9 Some Other Remarkable Hypergraph Classes ..... 181
9.1. Balanced Hypergraphs ..... 181
9.2. Interval Hypergraphs ..... 183
9.3. Normal Hypergraphs ..... 185
9.4. Planar Hypergraphs ..... 187
10 Hypergraph Coloring ..... 193
10.1. Basic Kinds of Classic Hypergraph Coloring ..... 193
10.2. Greedy Algorithm for the Lower Chromatic Number ..... 197
10.3. Basic Definitions of Mixed Hypergraph Coloring ..... 201
10.4. Greedy Algorithm for the Upper Chromatic Number ..... 207
10.5. Splitting-Contraction Algorithm ..... 213
10.6. Uncolorability ..... 219
10.7. Unique Colorability ..... 227
10.8. Perfection ..... 236
10.9. Chromatic Spectrum ..... 244
10.10.Coloring Planar Hypergraphs ..... 254
11 Modeling with Hypergraphs ..... 263
11.1. List Colorings without Lists ..... 263
11.2. Resource Allocation ..... 264
12 Appendix ..... 267
12.1. What Is Mathematical Induction ..... 267
12.2. Graph Theory Algorithms and Their Complexity ..... 269
12.3. Answers and Hints to Selected Exercises ..... 270
12.4. Glossary of Additional Concepts ..... 275
References ..... 279
Index ..... 281

## Preface

Graph Theory is an important area of contemporary mathematics with many applications in computer science, genetics, chemistry, engineering, industry, business and in social sciences. It is a young science invented and developing for solving challenging problems of "computerized" society for which traditional areas of mathematics such as algebra or calculus are powerless.

This book is for math and computer science majors, for students and representatives of many other disciplines (like bioinformatics, for example) taking the courses in graph theory, discrete mathematics, data structures, algorithms. It is also for anyone who wants to understand the basics of graph theory, or just is curious. No previous knowledge in graph theory or any other significant mathematics is required. The very basic facts from set theory, proof techniques and algorithms are sufficient to understand it; but even those are explained in the text.

Structurally, the text is divided into two parts where Part II is the generalization of Part I. The first part discusses the key concepts of graph theory with emphasis on trees, bipartite graphs, cycles, chordal graphs, planar graphs and graph coloring. The second part considers generalizations of Part I and discusses hypertrees, bipartite hypergraphs, hypercycles, chordal hypergraphs, planar hypergraphs and hypergraph coloring. There is an interaction between the parts and within the parts to show how ideas of generalizations work. The main point is to exhibit the ways of generalizations and interactions of mathematical concepts from the very simple to the most advanced.

The reader is conducted from the simplest examples, definitions and concepts step by step towards an understanding of a few most fundamental facts in the field. When writing I pursued the following goals:

- to make it as readable as possible;
- to choose the most instructive (not complex!) theorems and algorithms;
- to exhibit sequential generalization of concepts and ideas;
- to show an interaction between the sections and chapters for the sake of integrity;
- clearly expose the essence and core of graph and hypergraph theory, including hypergraph duality and hypergraph coloring;
- in Part I, to prepare the reader for understanding Part II;
- in Part II, to use the knowledge from Part I.

Hypergraphs model practical situations in different sciences in a much more general setting than graphs do. In addition, they help to find optimal solutions for many new optimization problems. While vertices represent the elements of a set (as in graphs), the hyperedges represent subsets of any cardinality (not just 2 as in graphs), or, even more generally, arbitrary statements about arbitrary subsets.

One of the features of this text is the duality of hypergraphs. There are the only two players in graph theory: vertices and edges. In dual hypergraphs, they just swap the roles. This fundamental concept is missing in graph theory (and in its introductory teaching) because dual graphs are not properly graphs, they generally represent hypergraphs. However, as Part II shows, the duality is a very powerful tool in understanding, simplifying and unifying many combinatorial relations; it is basically a look at the same structure from the opposite (vertices versus edges) point of view. Teaching and applying graph theory without hypergraphs does not allow to use duality; it is like teaching graphs without their complements. Among the goals of the text, one is to fill up this gap.

Part I may be used on undergraduate level for one semester introductory course, Part II may be used as a text or supplement for senior and graduate students. Some chapters or sections from Part II may be used on undergraduate level for most advanced students as projects in undergraduate research to report on departmental seminars. The book includes many examples, figures and algorithms; each section ends with a set of exercises and a set of computer projects. The answers and hints to selected exercises are provided at the end of the book. The material has been tested in class during more than 20 years of teaching experience of the author. Math majors will pay more attention to theorems and proofs, computer science majors will work more with the concepts, algorithms and computations, and representatives of other sciences will find models and ideas for solutions of optimization problems in their fields.

On the contents, four core areas of graph theory have been chosen: bipartite graphs, chordal graphs, planar graphs and graph coloring. The text exhibits the survey of basic results and their generalizations to hypergraphs in these areas. Bipartite graphs, planar graphs and graph coloring were the source, the origin of graph theory. Chordal graphs, discovered much later, have a very special place in the entire theory: it is the best playground for introduction to graphs and hypergraphs. The fact is that many unrelated (!) fundamental parameters introduced for general graphs (like, for example, related to degrees, or complements, or colorings), achieve their optimal values on chordal graphs. There are many relations of chordal graphs to trees, but only the language of hypergraphs allows to show that chordal conformal hypergraphs are dual to hypertrees. This is usually very impressive and unexpected to the reader since it is sufficient simply to transpose the incidence matrix of a hypertree to obtain a chordal hypergraph. It explicitly shows the strength of hypergraph theory.

At last graph coloring, generalized to hypergraphs, allows to consider the colorability, upper chromatic number, hypergraph perfection, the gaps in the chromatic spectrum, etc. Such concepts grew up from graph coloring and essentially represent the graph coloring unfolding. Several basic results from mixed hypergraph coloring, taken, adapted and updated from research monograph [6], will lead to unforeseen discoveries in Chapter 10; they demonstrate the power of generalizations. All this reflects the fact that for the last two decades, a significant number of new fundamental ideas, results and publications have led
to the situation where hypergraph theory in general, and hypergraph coloring in particular, are taking a new shape. The theory has a great future since it continues to generate new research problems that never arose before.

The book fills up the gap in educational materials on graphs and hypergraphs; it contributes to diversity of books and textbooks in the field; it is to understand the basic ideas of Graph and Hypergraph Theory. That is why many more special and advanced topics like Directed Graph Theory, Extremal Graph theory, Topological Graph Theory, Ramsey Theory, Random Graphs, Sperner Theory, Block Designs and many other topics (which usually have entirely devoted books) are not covered. The reader, however, will be well prepared to understand and to begin to work in any of these directions.

There are several pedagogical methods consistently used throughout the text:

- when formulating a new definition or concept, a formulation and examples of the negation often follow;
- when formulating a new theorem, the cases and examples when it does not work often follow;
- the names are given to many special graphs and hypergraphs; they are used instead of drawings thereafter;
- the same examples of graphs and hypergraphs are used for many different computational problems; as the opposite, the same problems and algorithms are used for different examples of graphs and hypergraphs;
- structurization of more complex proofs is made in order to ease the understanding of a few basic steps;
- detailed proofs of some long theorems are omitted and only ideas or sketch of the proofs are provided;
- contradictory facts or statements are used to call a surprise and make the reading simply interesting;
- an idea is explained first and then the details follow;
- since the comparison is crucial for understanding, opposite versions of some concepts are provided and the respective graphs, hypergraphs and algorithms are compared;
- since the visualization is the feature of graph theory, "look ⇒ read $\Rightarrow$ look" - rule is implicitly applied;
- the main goal of exercises is to test understanding of concepts and theorems, and the main goal of computer projects is to train in programming for scientific computations in graph and hypergraph theory;
- bold type is used for definitions and paragraph headings, italic type is used to call a special attention, and symbol □ is used to indicate the end of proofs.

After all, the ultimate goal of the book is to popularize graphs and hypergraphs.
Acknowledgements: I am grateful to Troy University for repeated support of this project. I also thank the students of Troy University who took the course Introduction to Graph Theory and helped in polishing the text.

Vitaly I. Voloshin
Troy University
Troy, Alabama
vvoloshin@troy.edu
November 18, 2008

## Part I

## Graphs

"...Graph Theory begins with "Graph"
and
ends with "Theory"...

## Chapter 1

## Basic Definitions and Concepts

"Pictures speak louder than words..."
"- Give me the definition first..."

### 1.1. Fundamentals

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-021.jpg?height=533&width=632&top_left_y=1144&top_left_x=567)
Figure 1.1. This is a graph.

An example of a graph is shown in Figure 1.1. The most simple and least strict definition of a graph is the following: a graph is a set of points and lines connecting some pairs of the points. Mathematicians name and number everything: in graph theory, points are called vertices, and lines are called edges. So, the graph in Figure 1.1 consists of five vertices and seven edges.

Throughout the book, we use the standard notation: upper case letters $A, B, \ldots$, $X, Y, Z$ for sets (all sets are finite), lower case letters $a, b, \ldots, e, \ldots, x, y, z$ for the elements of a set and curly braces \{,\} for listing the elements of a set. It is convenient to assign indices if we have many elements of the same type. A finite set is a list of its elements; no element

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-022.jpg?height=608&width=756&top_left_y=249&top_left_x=502)
Figure 1.2. Graph $G=(X, E)$.

is repeated and the order of elements in the list does not matter (we read the lists from left to right). The number of elements in a set $A$ is denoted by $|A|$, and the empty set is denoted by $\boldsymbol{\emptyset}$. If a set contains other sets as elements, then it is called a family; in a family, elements may be repeated but order still does not matter.

In a graph, the set of vertices is denoted by $X$ and is written as $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ where $x_{i}$ is the $i$-th vertex and $n$ is the number of vertices. The set of edges is denoted by $E$ and is written as $E=\left\{e_{1}, e_{2}, \ldots, e_{m}\right\}$ where $e_{i}$ is the $i$-th edge and $m$ is the number of edges. Each edge $e_{i}$ is identified by the pair of respective vertices which are connected by $e_{i}$. It remains to "invent" the last letter to denote the entire graph: $G$. Now we are ready to present the formal definition of a graph:

Definition 1.1.1 $A$ graph $G$ is a set $X$ of vertices together with a set $E$ of edges. It is written as

$$
G=(X, E) .
$$

Figure 1.2 presents the same graph shown in Figure 1.1 using the definition and agreements above. It has $n=5$ vertices and $m=7$ edges. We write $G=(X, E)$ where $X=\left\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right\}$ and $E=\left\{e_{1}, e_{2}, e_{3}, e_{4}, e_{5}, e_{6}, e_{7}\right\}$. Since each edge is a pair of vertices we write $e_{1}=\left\{x_{1}, x_{2}\right\}, e_{2}=\left\{x_{2}, x_{3}\right\}, e_{3}=\left\{x_{3}, x_{4}\right\}, e_{4}=\left\{x_{4}, x_{5}\right\}, e_{5}=\left\{x_{5}, x_{1}\right\}$, $e_{6}=\left\{x_{2}, x_{5}\right\}, e_{7}=\left\{x_{2}, x_{4}\right\}$, and therefore $E=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{2}, x_{3}\right\},\left\{x_{3}, x_{4}\right\},\left\{x_{4}, x_{5}\right\},\left\{x_{5}, x_{1}\right\}\right.$, $\left.\left\{x_{2}, x_{5}\right\},\left\{x_{2}, x_{4}\right\}\right\}$. Since $E$ is a set of sets it is a family.

If two vertices are connected by an edge, then they are called adjacent, otherwise they are called disjoint. For example, vertices $x_{1}$ and $x_{2}$ are adjacent, but vertices $x_{1}$ and $x_{3}$ are disjoint. For a given vertex $x$, the number of all vertices adjacent to it is called degree of the vertex $x$, denoted by $d(x)$. In our example, $d\left(x_{1}\right)=2, d\left(x_{2}\right)=4$, and so on. The maximum degree over all vertices is called the maximum degree of $G$, denoted by $\Delta(G)$. For graph $G$, see Figure 1.2, $\Delta(G)=d\left(x_{2}\right)=4$.

The adjacent vertices are sometimes called neighbors of each other, and all the neighbors of a given vertex $x$ are called the neighborhood of $x$. The neighborhood of $x$ is denoted by $N(x)$. In our graph, for example, $N\left(x_{1}\right)=\left\{x_{2}, x_{5}\right\}$. Evidently, the degree of a vertex is the cardinality (the number of elements) of its neighborhood: $d\left(x_{1}\right)=\left|N\left(x_{1}\right)\right|=2$, $d\left(x_{2}\right)=\left|N\left(x_{2}\right)\right|=4$, and so on.

For a graph $G$, if we count the degree of each vertex and arrange these degrees in non decreasing order, then we obtain a sequence called the degree sequence of $G$. The degree sequence for $G$, see Figure 1.2, is: (2,2,3,3,4).

Two edges are said to be adjacent if they have a vertex in common and disjoint otherwise. In Figure 1.2 edges $e_{1}$ and $e_{2}$ are adjacent, and edges $e_{1}$ and $e_{3}$ are disjoint. If a vertex $x$ belongs to an edge $e$, then we say that they are incident to each other. In the example above, edge $e_{1}$ is incident to vertex $x_{1}$ and is not incident to vertex $x_{5}$ and so on. As one can see, adjacency is referred to the elements of the same type and incidence is referred to the elements of different types.

Sometimes the vertex set of a graph $G$ is denoted by $V(G)$ and the edge set by $E(G)$. So, generally any graph $G=(V(G), E(G))$. The number of vertices is usually denoted by $n=n(G)$, and the number of edges by $m=m(G)$. The set of edges containing a vertex $x$ is denoted by $E(x)$. In our example, $V(G)=X=\left\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right\},|X|=n=5$, $E(G)=E=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{2}, x_{3}\right\},\left\{x_{3}, x_{4}\right\},\left\{x_{4}, x_{5}\right\},\left\{x_{5}, x_{1}\right\},\left\{x_{2}, x_{5}\right\},\left\{x_{2}, x_{4}\right\}\right\},|E|=m=7$, $E\left(x_{1}\right)=\left\{e_{1}, e_{5}\right\}$, and so on.

Proposition 1.1.1 (Degree equality) For any graph $G=(X, E)$, the following equality holds:

$$
\sum_{i=1}^{n} d\left(x_{i}\right)=2 m .
$$

Proof. Indeed, if we sum the degrees of all the vertices then each edge is counted twice because it has two ends. $\square$

Applying formula (1.1) to graph $G$, see Figure 1.2, gives:

$$
2+4+2+3+3=14=2 \times 7 .
$$

Proposition 1.1.2 In any graph $G=(X, E)$, there are two vertices with the same degree.
Proof. If a graph $G$ has $n$ vertices, then the degree sequence has $n$ integer numbers. For any vertex $x$, the minimum number of neighbors is 0 , and the maximum number of neighbors is $n-1$, therefore $0 \leq d(x) \leq n-1$.

Assume that all $n$ numbers are different. Then they must take all values on the interval of integers from 0 to $n-1.0$ means that there is a vertex with no neighbors, and $n-1$ means that there is a vertex adjacent to all the rest of vertices. This cannot occur simultaneously. Therefore, there must be two vertices with the same degree. $\square$

In graph $G$, see Figure 1.2, for example, $d\left(x_{1}\right)=d\left(x_{3}\right)=2$, and $d\left(x_{4}\right)=d\left(x_{5}\right)=3$.

## Exercises 1.1.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-024.jpg?height=290&width=1071&top_left_y=293&top_left_x=371)
Figure 1.3.

1. For each of the graphs in Figure 1.3, find the number of vertices $n$ and the number of edges $m$.
2. For each of the graphs in Figure 1.3, name or number the vertices and for each pair of vertices show if they are adjacent or not.
3. For each of the graphs in Figure 1.3, name the edges and for each pair of edges show if they are adjacent or not.
4. In each of the graphs in Figure 1.3, for each pair of vertices and edges show whether they are incident.
5. In each of the graphs in Figure 1.3, find degree and neighborhood of every vertex and degree sequence.
6. Apply degree equality (Proposition 1.1.1) to each of the graphs $G_{1}, G_{2}$ and $G_{3}$.
7. In each of the graphs in Figure 1.3, find the vertices of the same degree.
8. For each of the graphs in Figure 1.3, find the maximum degree $\Delta(G)$.

### 1.2. Graph Modeling Applications

Consider a simple instructive problem. Suppose we have a chemical plant that produces five chemical compounds A, B, C, D, and E which must be stored in storage areas. It is known however, that chemical A combined with chemical B might explode, so they must not be stored in the same storage area. The same occurs if chemical A is combined with E, chemical B is combined with C or E, chemical C is combined with D, and chemical D is combined with E. What is the minimum number of storage areas and how the chemical compounds should be stored to avoid any explosion hazards?

Let us "translate" the problem from the wording above into the language of Graph Theory. Denote chemicals A, B, C, D and E respectively by letters $x_{1}, x_{2}, x_{3}, x_{4}$ and $x_{5}$ and draw five vertices with the names $x_{1}, x_{2}, x_{3}, x_{4}$ and $x_{5}$ in the plane (put them, for example, in some imaginary circle clockwise with $x_{1}$ on the top). Now draw the edges: read the problem again and connect by an edge every pair of vertices corresponding to the chemicals which are explosive if combined. Thus, since A and B might explode if combined, connect corresponding vertices $x_{1}$ and $x_{2}$ with an edge; in the same way, connect $x_{1}$ with $x_{5}$, connect

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-025.jpg?height=709&width=999&top_left_y=285&top_left_x=388)
Figure 1.4. Graph $G=(X, E)$.

$x_{2}$ with $x_{3}$ and $x_{5}$, connect $x_{3}$ with $x_{4}$ and connect $x_{4}$ with $x_{5}$. The graph obtained is shown in Figure 1.4. It is visually reflecting the relations between the chemicals. Now the problem can be mathematically formulated in the following way: how can we partition the vertex set $X=\left\{x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right\}$ into the smallest number of parts, i.e. the subsets, in such a way that no subset contains adjacent vertices? Each such subset will be considered as the subset of chemicals that can be safely stored in the same storage area.

Looking at Figure 1.4, we can evidently partition $X$ into five subsets: $\left\{x_{1}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}$, $\left\{x_{4}\right\},\left\{x_{5}\right\}$; this partition is feasible, i.e. good, but not optimal. We can partition $X$ into four subsets: $\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\},\left\{x_{4}\right\},\left\{x_{5}\right\}$, what is better but still not optimal. At last, we can partition $X$ into three subsets: $\left\{x_{1}, x_{4}\right\},\left\{x_{2}\right\},\left\{x_{3}, x_{5}\right\}$, see Figure 1.4 (the partition is shown by dotted closed curves), and show that it is optimal, i. e. minimal. Indeed, visually one can see that any partition of $X$ into two subsets leaves edges in one of the subsets and therefore is not good. Strict mathematical proof would be the following: consider triangle formed by vertices $x_{1}, x_{2}$, and $x_{5}$; any partition of it into two parts (even if one part is empty) leaves an edge in one of the parts. So, two storage areas is not a possible solution, and three storage areas are sufficient and represent the optimal solution of the problem. Looking at the picture, the reader can easily find at least one another optimal solution, say $\left\{x_{1}, x_{3}\right\}$, $\left\{x_{2}, x_{4}\right\}$, and $\left\{x_{5}\right\}$. How many and which optimal solutions do exist?

We will see in Chapter 5 and other chapters how such and many other problems which ask not only for the optimal but for all possible solutions, can efficiently be solved. In all applications, like in the example above, visualization is the key feature. Using vertices, edges and their meanings, one apply graphs to depict situations in different sciences. Different problems, first formulated in ordinary language, as in the example above, are then translated into the language of Graph Theory and solved mathematically. Mathematicians then provide algorithms for finding optimal solutions which are implemented in a software
by computer engineers and passed back to the respective businesses for use in the industry.
We next provide a series of situations from different sciences which can successfully be modeled by graphs. In the next chapters we will consider many mathematical problems which have a respective meaning if applied to graphs as models. In each of the examples below, the reader can easily draw a respective graph with a few vertices and edges keeping in mind their meaning.

Mathematics:

- the vertices are natural numbers from 1 to 100; two vertices are adjacent if the respective numbers have a common divisor different from 1;
- the vertices are intervals on the real line; two vertices are adjacent if the respective intervals intersect;
- the vertices are all $n$-dimensional vectors with binary coordinates (each component is either 0 or 1); two vertices are adjacent if the respective vectors differ in precisely one component.

Computer science:

- vertices are computers in a network; two vertices are adjacent if the respective computers are linked together by telecommunications circuits;
- vertices are processors in parallel architectures; two vertices are adjacent if the respective processors have a direct link;
- vertices are files in a data base; two vertices are adjacent if the respective files cannot be opened simultaneously;
- vertices are all web pages in the world; two vertices are adjacent if the respective web pages are connected by any hypertext link;
- vertices are the image fragments in image segmentation in computer vision; two vertices are adjacent if the respective fragments are related.

Genetics:

- the vertices are fragments of a DNA sequence; two vertices are adjacent if the respective fragments overlap;
- the vertices are species; two vertices are adjacent if the respective species have a common hereditary property.

Chemistry:

- the vertices are atoms in a molecule; two vertices are adjacent if the respective atoms have a bond;

- the vertices are chemical compounds used by a chemical factory; two vertices are adjacent if the respective compounds are explosive when combined.

Engineering:

- the vertices are junction points of an electric circuit; two vertices are adjacent if the respective junction points are connected by a wire.

Economics:

- the vertices are all companies in the world; two vertices are adjacent if the respective companies are the suppliers for each other.

Healthcare:

- the vertices are drugs; two vertices are adjacent if the combination of the respective drugs is lethal.

Sociology:

- the vertices are employees in a company; two vertices are adjacent if the respective people are in conflict;
- the vertices are the people in a town; two vertices are adjacent if the respective people are friends.

Broadcasting:

- the vertices are radio transmitters in a region; two vertices are adjacent if the respective transmitters interfere.

Geographical maps:

- the vertices are cities; two vertices are adjacent if the respective cities are connected by a highway.

Generally, graphs represent the simplest visual models of systems: any system is a set of elements together with a set of relations between the elements. In the most general setting however, the relations are expressed by statements about any subsets rather than just pairs of elements.

Exercises 1.2.

1. Suppose there are the following intervals on the real line: [0, 3], [4, 9], [2.7,5], [5,7], [2,4.3], [1, 4], [10, 11] and [0, 12]. Draw a graph where vertices represent the intervals and two vertices are adjacent if and only if the respective intervals intersect (the "intersection" or "interval" graph).

2. There are following eight possible sequences of length three consisting of 0 and 1: 000, 001, 010, 011, 100, 101, 110, 111. Draw a graph where the vertices represent the sequences and two vertices are adjacent if and only if the respective sequences differ in precisely one digit. Why is this graph called "cube"?
3. Make the list of all your friends. Draw a graph where the vertices are your friends and two vertices are adjacent if and only if the respective friends are friends themselves (the "friendship" graph).
4. For Florida, Alabama, Georgia, Mississippi, South Carolina, Tennessee, Kentucky, Virginia and California construct a graph where the vertices are these states and two vertices are adjacent if and only if the respective states have a common border.
5. There are four workers A, B, C and D and five jobs 1, 2, 3, 4, and 5. Worker A can do jobs 1 and 2, worker B can do jobs 1, 4 and 5, worker C can do jobs 2, 3, and 4, and worker D can do job 5. Draw a graph where the vertices are the workers and jobs and two vertices are adjacent if and only if they correspond to a worker and a job that the worker can do.
6. Think about five different ways you can drive from home to the school. Draw a graph where the vertices are your home, the school and all street crossings on your way; two vertices are adjacent if and only if the respective crossings, home and the school are consecutive on your way.
7. There are three houses and three wells. Draw a graph where the vertices are houses and wells and connect each house with each well by a curve representing an edge. Is it possible to draw the graph in such a way that the curves do not intersect in the plane at points other than a house or a well?

### 1.3. Graph Representations

For the last 50 years, Computer Science became a major provider of problems to Graph Theory and, simultaneously, it became a major consumer of the solutions to such problems. In practical applications, graphs involved have not five, and even not ten, or twenty, but hundreds and thousands of vertices and edges. It is not possible for human being to solve any problem with such a huge number of elements just using the description or even drawing a graph. Computers are used for such tasks, and there are several special ways to store graphs in computer memory.

Adjacency lists. Let us consider graph $G$ shown in Figure 1.5. For every vertex $x$, form a list of all of its neighbors. The set of all such lists is called the adjacency list. In $G$, the neighbors are:

- For $x_{1}: x_{2}, x_{5}$,
- For $x_{2}: x_{1}, x_{3}, x_{4}, x_{5}$,
- For $x_{3}: x_{2}, x_{4}$,
- For $x_{4}: x_{2}, x_{3}, x_{5}$,
- For $x_{5}: x_{1}, x_{2}, x_{4}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-029.jpg?height=707&width=1033&top_left_y=249&top_left_x=365)
Figure 1.5. Graph $G=(X, E)$.

The adjacency list, denoted by $L(G)$, is:

$$
\begin{aligned}
L(G)= & \left\{\left\{x_{2}, x_{5}\right\},\left\{x_{1}, x_{3}, x_{4}, x_{5}\right\},\left\{x_{2}, x_{4}\right\},\right. \\
& \left.\left\{x_{2}, x_{3}, x_{5}\right\},\left\{x_{1}, x_{2}, x_{4}\right\}\right\} .
\end{aligned}
$$

Adjacency matrix. It is a matrix (rectangular table from letters and/or numbers) which has one row and one column for each vertex. If vertex $x_{i}$ is adjacent to vertex $x_{j}$, then $(i, j)$ entry (element at the intersection of ith row and jth column) in the matrix is 1, otherwise it is 0. In fact, adjacency matrix is a square matrix.

For graph $G$, see Figure 1.5, the adjacency matrix denoted by $A(G)$ is:

$$
A(G)=\left(\begin{array}{lllll}
0 & 1 & 0 & 0 & 1 \\
1 & 0 & 1 & 1 & 1 \\
0 & 1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 & 1 \\
1 & 1 & 0 & 1 & 0
\end{array}\right) .
$$

One can compare $A$ with the adjacency lists: in every row, the 1's indicate the respective neighbors from the lists and vice versa.

If we write (from left to right) the rows as columns (1st row as 1st column, 2nd row as 2nd columns and so on), then the columns become rows, and we obtain another matrix, $A^{\prime}$ which in this particular case is the same as $A$. Such an operation is called a transposition of the matrix. Since $A=A^{\prime}$, this matrix is called symmetric. One can think about transposition as of a rotation of the matrix about its diagonal, imaginary line in space connecting upper left and lower right entries.

Incidence matrix. It is a matrix which has one row for each vertex and one column for each edge of a graph. If vertex $x_{i}$ is incident to edge $e_{j}$, then the $(i, j)$-entry in the matrix is 1 , otherwise it is 0 . For our graph $G$, the incidence matrix denoted by $I(G)$ has 5 rows corresponding to the vertices and 7 columns corresponding to the edges:

$$
I(G)=\left(\begin{array}{lllllll}
1 & 0 & 0 & 0 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 & 0 & 1 & 1 \\
0 & 1 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 & 1 & 0
\end{array}\right) .
$$

As one can see, every column has precisely two 1's; their rows point out on the vertices which are connected by the respective edge. If we transpose this matrix (write rows sequentially as columns), we obtain another matrix which is different from $I$. We will se in Part II how important the transposition of the incidence matrix is.

Edge lists. One can describe graph by giving just the list of all of its edges. For graph $G$, the edge list, denoted by $J(G)$ is the following:

$$
\begin{aligned}
& J(G)=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{2}, x_{3}\right\},\left\{x_{3}, x_{4}\right\},\right. \\
& \left.\left\{x_{4}, x_{5}\right\},\left\{x_{1}, x_{5}\right\},\left\{x_{2}, x_{5}\right\},\left\{x_{2}, x_{4}\right\}\right\} .
\end{aligned}
$$

Important comment. If we compare Figure 1.2 and Figure 1.5, then we observe that they represent the same graph $G$; the only difference is in the positions of vertices in the plane. It is the feature of graph theory that the same graph may be drawn in many different ways. Not only the vertices may have different positions, the edges may be drawn as curves connecting the same pairs. As far as the names of vertices and edges remain the same, we accept the agreement that it is the same graph because it has the same mathematical model.

At this moment it is important to understand that all three drawings Figure 1.1, Figure 1.2 and Figure 1.5, the description of pair $G=(X, E)$, adjacency list $L(G)$, adjacency matrix $A(G)$, incidence matrix $I(G)$, and edge list $J(G)$, all are different representations of the same concept called graph and denoted by just one letter $G$. Inverse, having any of these descriptions one can draw a graph and/or construct any other representation as well.

In practice, depending on the problem, some representations are more suitable than the others.

Exercises 1.3.

1. For graphs $G_{1}, G_{2}$ and $G_{3}$, see Figure 1.6, construct an adjacency list.
2. For graphs $G_{1}, G_{2}$ and $G_{3}$, construct an adjacency matrix.
3. For graphs $G_{1}, G_{2}$ and $G_{3}$, construct an incidence matrix.
4. For graphs $G_{1}, G_{2}$ and $G_{3}$, construct an edge list.
5. Write down an arbitrary adjacency list, adjacency matrix, incidence matrix, edge list and draw the respective graph.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-031.jpg?height=286&width=1098&top_left_y=216&top_left_x=344)
Figure 1.6.

Computer Projects 1.3. Write a program with the following input and output.

1. Given an adjacency list, find the adjacency matrix.
2. Given an adjacency list, find the incidence matrix.
3. Given an adjacency list, find the edge list.
4. Given an adjacency matrix, find the adjacency list.
5. Given an adjacency matrix, find the incidence matrix.
6. Given an adjacency matrix, find the edge list.
7. Given an incidence matrix, find the adjacency list.
8. Given an incidence matrix, find the adjacency matrix.
9. Given an incidence matrix, find the edge list.
10. Given an edge list, find the adjacency list.
11. Given an edge list, find the adjacency matrix.
12. Given an edge list, find the incidence matrix.

### 1.4. Generalizations

When degenerated cases may occur. In some cases, especially from theoretical view point, it is convenient to consider an edge connecting a vertex to itself. Such edges are called loops. It may also happen when some vertex has no neighbors, i.e. its degree is 0. These vertices are said to be isolated. Loops and isolated vertices are shown in Figure 1.7.

When repeated edges occur. In some areas of applications, there are many connections between some of the points (for example, in geographic maps), so in graph models, there may be many edges connecting the same pair of vertices. Such edges are called parallel or multiple. The number of repetitions of an edge is its multiplicity. Graphs which admit multiple edges are called multigraphs. Multiple edges are shown in Figure 1.7.

When direction/order is important. Until now we made no distinction in writing the same sets in different ways. Usually, we read from left to right, and the following two writings for the same set are equivalent: $\{a, b\}=\{b, a\}$. However, there are situations in real life when an order is crucially important. For example, a road (no direction specified) is not the same as a one-way street (direction should be strictly observed). To reflect such situations, one introduce an order which becomes important. In writing ordered sets instead

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-032.jpg?height=593&width=1113&top_left_y=184&top_left_x=362)
Figure 1.7. Generalizations.

of curly braces $\{$,$\} , one use parentheses (,). So now (a, b) \neq(b, a)$. In a graph, an ordered pair of vertices is called an arc. If $(x, y)$ is an arc, then $x$ is called the initial vertex and $y$ is called the terminal vertex. A graph in which all edges are ordered pairs is called the directed graph, or digraph. Even loops may be ordered, see Figure 1.7.

Comparing edges and arcs one can accept the following point of view: an edge of a graph is equivalent to two arcs going in opposite directions, see Figure 1.8.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-032.jpg?height=75&width=981&top_left_y=1297&top_left_x=417)
Figure 1.8.

Graphs in which order is not important are called undirected graphs. Figure 1.8 implies that directed graphs represent more general structures than undirected graphs. Or, equivalently, the undirected graphs represent a special case of directed graphs, namely, when each edge is replaced by a pair of arcs going in opposite directions. Undirected graphs without loops and multiple edges are called simple graphs or simply graphs. Usually, unless otherwise stated, one consider simple graphs.

Graph representations can accordingly be adjusted. For undirected multigraphs, adjacency list $L$ may contain multiple elements and empty sets, adjacency matrix $A$ may have zero rows and zero columns and integer numbers different from 1 (=multiplicity), incidence matrix $I$ may have zero rows and repeated columns, and edge list $J$ may have repeated elements. For directed graphs, adjacency list $L$ will not change, adjacency matrix $A$ may not be symmetric (the order may be "row → column"), incidence matrix I will have -1' for initial vertices, and edge list $J$ will become ordered.

An example of a directed multigraph $G$ with a loop is shown in Figure 1.9.
The adjacency list of $G$ is:

$$
L(G)=\{\emptyset,\{2\},\{2,4\},\{1,1,3\}\} ;
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-033.jpg?height=334&width=588&top_left_y=192&top_left_x=567)
Figure 1.9.

the adjacency matrix $A$ is:

$$
A(G)=\left(\begin{array}{llll}
0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 1 & 0 & 1 \\
2 & 0 & 1 & 0
\end{array}\right) ;
$$

the incidence matrix $I$ is:

$$
I(G)=\left(\begin{array}{rrrrrr}
1 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & l & 0 & 0 \\
0 & 0 & -1 & 0 & 1 & -1 \\
-1 & -1 & 0 & 0 & -1 & 1
\end{array}\right) ;
$$

and, at last, the edge list $J$ is:

$$
J(G)=\{(4,1),(4,1),(3,2),(2,2),(4,3),(3,4)\} .
$$

Notice that the columns in $I(G)$ are in the order of arcs $a, b, c, d, e, f$, and "l" in fourth column and second row indicates that arc $d$ is the loop at vertex 2.

Some graph modeling examples where the order is important are:

- the vertices are street crossings in the city map; crossings $x_{i}$ and $x_{j}$ form an arc $\left(x_{i}, x_{j}\right)$ if the traffic is allowed in the direction from $x_{i}$ to $x_{j}$;
- the vertices are all companies in the world; companies $x_{i}$ and $x_{j}$ form an arc $\left(x_{i}, x_{j}\right)$ if company $x_{i}$ is a supplier for the company $x_{j}$;
- the vertices are all web pages in the Internet; the web pages $x_{i}$ and $x_{j}$ form an arc $\left(x_{i}, x_{j}\right)$ if there is a hypertext link from page $x_{i}$ to page $x_{j}$;
- the vertices are folders of a folder system in a computer; folders $x_{i}$ and $x_{j}$ form an arc $\left(x_{i}, x_{j}\right)$ if folder $x_{i}$ contains folder $x_{j}$ as a subfolder;
- the vertices are states of a discrete system; states $x_{i}$ and $x_{j}$ form an arc $\left(x_{i}, x_{j}\right)$ if the probability of transition from state $x_{i}$ to state $x_{j}$ is positive;
- the vertices are all your predecessors; predecessors $x_{i}$ and $x_{j}$ form an arc $\left(x_{i}, x_{j}\right)$ if predecessor $x_{i}$ is the parent of predecessor $x_{j}$;

- the vertices are students in a classroom; students $x_{i}$ and $x_{j}$ form an arc $\left(x_{i}, x_{j}\right)$ if student $x_{i}$ likes student $x_{j}$.

Exercises 1.4.
For graphs in Figures 1.3 and 1.6, replace each edge with an arc and construct the adjacency list $L$, adjacency matrix $A$, incidence matrix $I$, and edge list (i.e. arc list) $J$.

Computer Projects 1.4.
Repeat Computer Projects 1.3. for: a) undirected multigraphs; b) directed multigraphs.

### 1.5. Basic Graph Classes

Empty graphs. Any graph must have at least one vertex. In other words, we do not accept graphs without vertices, though in hypergraph theory we will show how this case may be treated. A graph may have no edges at all; such graphs are called empty, denoted by $E_{n}$ where $n$ is the number of vertices. Graph $E_{4}$ is depicted in Figure 1.7. If a graph is not empty, then it has at least one edge. Notice that an empty graph is not the same as the empty set which is always denoted by $\emptyset$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-034.jpg?height=142&width=832&top_left_y=1201&top_left_x=466)
Figure 1.10. Path $P_{5}$.

Paths. A graph in which all vertices can be numbered (ordered from left to right) $x_{1}, x_{2}, \ldots, x_{n}$ in such a way that there is precisely one edge connecting every two consecutive vertices and there are no other edges, is called a path.

The number of edges in a path is its length. A path on $n$ vertices is denoted by $P_{n}$. Evidently, in any $P_{n}$, the number of edges $m=n-1$. Any edge itself is a path $P_{2}$. The vertices $x_{1}$ and $x_{n}$ both have degree 1 in a path $P_{n}$; we say that the path connects vertices $x_{1}$ and $x_{n}$. Generally, any path connecting vertices $x$ and $y$ is called $(x, y)$-path. In Figure 1.10, path $P_{5}$ of length 4 connects vertices $x_{1}$ and $x_{5}$, or is $\left(x_{1}, x_{5}\right)$-path.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-034.jpg?height=290&width=1028&top_left_y=1850&top_left_x=369)
Figure 1.11. Connected graph $G_{1}$ and disconnected graph $G_{2}$.

Connected graphs. A graph is called connected if in it any two vertices are connected by some path; otherwise it is called disconnected. It means that in a disconnected graph
there always exists a pair of vertices having no path connecting them. Any disconnected graph is a union of two or more connected graphs; each such connected graph is then called a connected component of the original graph.

For example, see Figure 1.11, $G_{1}$ is a connected graph, but $G_{2}$ is a disconnected graph having two connected components. Any isolated vertex is a connected component. Generally, an empty graph $E_{n}$ has $n$ components. If each component of a graph $G$ represents the same graph, say $G^{\prime}$, and if $G$ has $k$ connected components, then we write: $G=k G^{\prime}$.

Cycles. A connected graph in which every vertex has degree 2 is called a cycle, (sometimes "simple cycle") denoted by $C_{n}$ where $n$ is the number of vertices.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-035.jpg?height=588&width=1030&top_left_y=650&top_left_x=368)
Figure 1.12. Cycles $C_{1}, C_{2}, C_{3}, C_{4}, C_{5}$, and $C_{6}$.

If $n$ is an even number, then $C_{n}$ is called even cycle. If $n$ is odd, then $C_{n}$ is odd cycle. In $C_{n}$, the number of edges coincides with the number of vertices and it is called the length of the cycle, see Figure 1.12. $C_{1}$ represents an edge connecting the vertex with itself, it is a loop. $C_{2}$ represents two parallel edges connecting the same pair of vertices. The cycle $C_{3}$ is called triangle. In simple graphs, if there are cycles, then they must have length at least 3. If a graph is not a cycle, then either it has a vertex of degree other than 2, or it is disconnected.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-035.jpg?height=435&width=533&top_left_y=1737&top_left_x=616)
Figure 1.13. Wheel $W_{6}$.

Wheels. If for any cycle $C_{k}, k \geq 3$, we add a new vertex and connect it to each of the
vertices of $C_{k}$, then the graph obtained is called a wheel, denoted by $W_{k+1}$. The wheel $W_{6}$ is shown in Figure 1.13.

Complete graphs. A graph in which every pair of vertices is an edge, is called complete, denoted by $K_{n}$ where as usually, $n$ is the number of vertices. It is called complete because we cannot add any new edge to it and obtain a simple graph. For every $n \geq 1$, the degree of each vertex in $K_{n}$ is $n-1$, and the number of edges is:

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-036.jpg?height=640&width=1043&top_left_y=505&top_left_x=360)
Figure 1.14. Complete graphs $K_{1}, K_{2}, K_{3}, K_{4}, K_{5}$, and $K_{6}$.

$$
m=\binom{n}{2}=\frac{n(n-1)}{2} .
$$

This formula can easily be obtained by counting and adding degrees of every vertex, i.e. applying Proposition 1.1.1: having $n$ vertices of degree $n-1$ each, we obtain the number $n(n-1)=2 m$. For example, the number of edges in $K_{6}$ is: $m=6(6-1) / 2=15$. If a graph is not complete, then it has at least two vertices which are not adjacent.

Complete graphs $K_{1}, K_{2}, K_{3}, K_{4}, K_{5}$, and $K_{6}$ are shown in Figure 1.14. Notice that $K_{2}=$ $P_{2}, K_{3}=C_{3}$, and $K_{4}=W_{4}$.

Trees. A connected graph which has no cycles is called a tree. Usually any tree on $n$ vertices is denoted by $T_{n}$. In contrast to $P_{n}, K_{n}, C_{n}$ and $W_{n}$ there are many distinct trees on $n$ vertices. $P_{n}$ is a special (simplest) case of a tree. We will have the concept of isomorphism to distinguish graphs.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-036.jpg?height=148&width=1030&top_left_y=1947&top_left_x=368)
Figure 1.15. Trees.

Figure 1.15 shows three examples of trees, among which the 1st and the 3rd "are the same" just because they both are $P_{4}$, and the 2nd is "different" from them. There are no other trees

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-037.jpg?height=342&width=1038&top_left_y=233&top_left_x=360)
Figure 1.16. Bipartite graphs.

on 4 vertices. In any tree on $n$ vertices, the number of edges $m=n-1$. Disconnected graph without cycles is called a forest. Evidently, in a forest every component is a tree.

The last example shows that a graph may be drawn in many different ways; different drawings are like different views of the same object. It is not important how a graph is drawn; it is important which vertices are adjacent and which are not. As we have seen, not every intersection of edges in a drawing is a vertex. But every vertex lies on the intersection of the respective edges.

Bipartite graphs. A graph $G=(X, E)$ is called bipartite if its vertex set $X$ can be partitioned into two disjoint sets $X_{1}$ and $X_{2}$, called parts, in such a way that every edge connects vertices from different sets, see Figure 1.16. It means that there are no edges inside $X_{1}$ and there are no edges inside $X_{2}$. In other words, for a bipartite graph, in its drawing, it is possible to color the vertices using just two colors (say blue and red) in such a way that adjacent vertices have different colors. If a graph is not bipartite, then in any partition of its vertex set into two subsets, at least one of the subsets contains at least one edge. Trees and even cycles are bipartite graphs; odd cycles are not. The smallest simple graph which is not bipartite is triangle $C_{3}$. Notice that any graph which contains a triangle or an odd cycle cannot be bipartite. If $G=(X, E)$ is a bipartite graph, it is convenient to write it as $G=\left(X_{1}, X_{2} ; E\right)$ where $X_{1}$ is its left part and $X_{2}$ is its right part (as is the first graph in Figure 1.16).

A complete bipartite graph is a bipartite graph in which every vertex from part $X_{1}$ is adjacent to every vertex from part $X_{2}$. It is called complete because it is not possible to add a new edge to it and obtain another bipartite graph. If in a complete bipartite graph $\left|X_{1}\right|=r$ and $\left|X_{2}\right|=s$, then the graph itself is denoted by $K_{r, s}$. The number of edges in $K_{r, s}$ clearly equals $r s$.

Among the examples of bipartite graphs shown in Figure 1.16, the first is not complete, the second is $K_{1,3}$, and the third is $C_{4}$. Observe that bipartition $X_{1}, X_{2}$ is explicitly shown for graph $G$ and it is not shown for $K_{1,3}$ and $C_{4}$; this fact exhibits the difference between "can be partitioned" (as in definition) and "is partitioned".

Regular graphs. A graph in which every vertex has the same degree $k$ is called regular of degree $k$ or $k$-regular. Empty graph $E_{n}$ is 0 -regular, cycle $C_{n}$ is 2 -regular, and $K_{n}$ is $(n-1)$-regular graph. The 3 -regular graphs are called the cubic graphs.

It is easy to construct cubic graphs. For example, one can take two cycles of the same length, draw one inside another and connect the respective vertices by edges called

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-038.jpg?height=590&width=1131&top_left_y=186&top_left_x=365)
Figure 1.17. Cubic graphs.

"spokes". If we do that with $C_{3}$ we obtain a graph called prism; if we do that with $C_{4}$ we obtain a graph called cube. If we do that with $C_{5}$ by drawing inner cycle differently, we obtain a famous graph called the Petersen graph, see Figure 1.17.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-038.jpg?height=337&width=1121&top_left_y=1175&top_left_x=321)
Figure 1.18. Isomorphic graphs.

Isomorphic graphs. How can we compare different graphs? Consider graph $G_{1}$ in Figure 1.18. Let us re-draw it aside by placing vertex 4 inside triangle formed by vertices 1, 2 and 3, and preserving the edges. We obtain graph $G_{2}$. Is $G_{2}$ different from $G_{1}$, or that is the same graph? Let us re-draw $G_{1}$ again by placing the vertices on a square as in $G_{1}$ but now replacing the segments of straight lines (representing the edges) by arbitrary curves. We obtain graph $G_{3}$. Is $G_{3}$ different from $G_{1}$, or that is the same graph? On one hand, of course, three graphs are pairwise different because the vertices are different points in the plane. On the other hand, they all have the same adjacency matrix, i.e., the same mathematical model. We can say that graphs $G_{1}, G_{2}$ and $G_{3}$ are "essentially the same". But here is an important point: graphs $G_{1}, G_{2}$ and $G_{3}$ have the same adjacency matrix because the vertices have the same names; if we choose a different numbering of vertices in any of the graphs, we obtain a different adjacency matrix. In practical applications, the names of vertices are not given at all; so, how to recognize if two graphs are "essentially the same"?

Mathematical definition for two graphs "to be essentially the same graph" is expressed
in the concept of "isomorphism" (Greek: "iso" = equal, and "morphe" = shape). Two simple graphs $G_{1}=\left(X_{1}, E_{1}\right)$ and $G_{2}=\left(X_{2}, E_{2}\right)$ are called isomorphic if there exists a one-to-one correspondence between vertex sets $X_{1}$ and $X_{2}$ such that any two vertices are adjacent in $G_{1}$ if and only if their images in the correspondence are adjacent in $G_{2}$. Any such one-to-one correspondence is called an isomorphism. If $G_{1}$ and $G_{2}$ are isomorphic, then we say that $G_{1}$ is isomorphic to $G_{2}$, and $G_{2}$ is isomorphic to $G_{1}$, and we write $G_{1} \cong G_{2}$.

Suppose $\left|X_{1}\right|=\left|X_{2}\right|=n$. Generally, how many one-to-one correspondences do exist? The first vertex of $X_{1}$ can be mapped into any of $n$ vertices of $X_{2}$, so we have $n$ possibilities for it. Once the first vertex is mapped, the second vertex has $n-1$ possibilities, then the third vertex has $n-2$ possibilities and so on. Total number of possibilities is $n(n-1)(n-$ $2) \cdots 3 \cdot 2 \cdot 1=n!$. If in at least one of these $n!$ cases there is a complete "coincidence" of $G_{1}$ and $G_{2}$, then they are isomorphic. Otherwise they are not. So, two graphs are not isomorphic, if no matter how we map the vertices of one into the vertices of another, there will always be a pair of vertices which are adjacent in one graph and disjoint in another. In such case the graphs are really different because we can never match them.

We can think about the number of isomorphisms to be 0 (when graphs are not isomorphic), and $1,2, \ldots n!$ when they are isomorphic. In Figure 1.15, for example, the first and the third trees are isomorphic, they both represent $P_{4}$. There are two different choices to map end vertices, then the rest of mapping is determined univocal. So, we can observe that there are two isomorphisms between any two paths $P_{n}$. On the other hand, the second tree is not isomorphic to $P_{4}$. Graphs $E_{n}$ and $K_{n}$ have $n!$ isomorphisms, graphs $C_{n}$ have $2 n$ and so on.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-039.jpg?height=295&width=1131&top_left_y=1302&top_left_x=316)
Figure 1.19. Non isomorphic trees.

To be isomorphic, graphs must have the same number of vertices, the same number of edges, the same number of vertices of each degree. However, graphs may have the same number of vertices and edges and even degrees and still not to be isomorphic, see example in Figure 1.19. Both trees $T_{1}$ and $T_{2}$ have eight vertices, seven edges, four vertices of degree 1, two vertices of degree 2 and two vertices of degree 3. However, in $T_{1}$ the vertices of degree 3 are adjacent but in $T_{2}$ the vertices of degree 3 are disjoint. This observation and common sense tells us that there will be no match in all $8!=40320$ one-to-one correspondences. Generally, to prove that graphs are not isomorphic, instead of considering all $n$ ! mappings, it is sufficient to find some property in one of them and show that it is missing in another. To show that graphs are isomorphic, it is sufficient to exhibit that very same one-to-one correspondence from the definition.

Next example, see Figure 1.20, shows two graphs $G_{1}$ and $G_{2}$ which appear to be iso-

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-040.jpg?height=398&width=1213&top_left_y=183&top_left_x=365)
Figure 1.20. Isomorphic graphs.

morphic. In fact, the figure represents two "very different" drawings of the same graph. The mapping (one-to-one correspondence) of the vertices of $G_{1}$ into the vertices of $G_{2}$ denoted by $\boldsymbol{\sigma}$ is the following:

$$
\sigma=\left(\begin{array}{llllll}
1 & 2 & 3 & 4 & 5 & 6 \\
a & b & c & d & e & f
\end{array}\right) .
$$

One can check manually that every two vertices are adjacent in $G_{1}$ if and only if the respective vertices are adjacent in $G_{2}$. For example, vertices 1 and 2 are disjoint in $G_{1}$, so are the corresponding vertices $a$ and $b$ in $G_{2}$. Vertices 1 and 4 are adjacent in $G_{1}$, so are the corresponding vertices $a$ and $d$ in $G_{2}$, and so on for each pair of the vertices. The number of all such comparisons is $\binom{6}{2}=15$ which is much less than $6!=720$, the number of all one-to-one correspondences.

In determining a graph class, one proceed in the following way: first, observe some graph property, then investigate all graphs having that property. There are hundreds of graph classes that have been investigated. In the simplest classes such as $E_{n}, K_{n}, C_{n}, W_{n}$, etc, the lower index always shows the number of vertices.

## Exercises 1.5.

1. Construct $L(G)$ for each graph $G$ drawn in this section.
2. Construct $A(G)$ for each graph $G$ drawn in this section.
3. Construct $I(G)$ for each graph $G$ drawn in this section.
4. Construct $J(G)$ for each graph $G$ drawn in this section.
5. Find out and explain which graphs in Figure 1.21 are bipartite.
6. For each pair of integer numbers $r$ and $s, 1 \leq r, s \leq 5$, draw a complete bipartite graph $K_{r, s}$.
7. Explain why $K_{r, s}$ and $K_{s, r}$ are isomorphic.
8. Find out and explain which pairs of graphs in Figure 1.21 are isomorphic and which are not.
9. Compare graph representations for two isomorphic graphs $G_{1}$ and $G_{2}$ in Figure 1.20. When are they identical?
10. Explain when two isomorphic graphs have the same adjacency matrix and the same incidence matrix.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-041.jpg?height=738&width=1077&top_left_y=235&top_left_x=319)
Figure 1.21.

Computer Projects 1.5. Write a program with the following input and output.

1. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is a path.
2. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is connected.
3. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is a cycle.
4. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is a complete graph.
5. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is a tree.
6. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is a wheel.
7. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is a complete bipartite graph.
8. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is a bipartite graph.
9. Given any of $L(G), A(G), I(G), J(G)$, recognize if $G$ is regular.
10. Given any of $L\left(G_{1}\right), A\left(G_{1}\right), I\left(G_{1}\right)$, or $J\left(G_{1}\right)$, any of $L\left(G_{2}\right), A\left(G_{2}\right), I\left(G_{2}\right)$, or $J\left(G_{2}\right)$ and a one-to-one correspondence $\sigma$ between the vertices of $G_{1}$ and $G_{2}$. Recognize if $\sigma$ realizes an isomorphism between $G_{1}$ and $G_{2}$.

### 1.6. Basic Graph Operations

In many proofs and algorithms, one often apply graph operations that allow to obtain one graph from another. We now consider some of them.

Deletion of a vertex. Let us have a graph $G=(X, E)$ and a vertex $x \in X$. A deletion of $x$ from $G$ is the removing of $x$ from set $X$ and removing from $E$ all edges of $G$ that contain $x$. Recall that $E(x)$ denotes the set of edges containing vertex $x$ in graph $G$. If $X_{1}=X-\{x\}$, and $E_{1}=E-E(x)$, then deletion of $x$ from $G$ results in obtaining the graph $G_{1}=\left(X_{1}, E_{1}\right)$,

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-042.jpg?height=295&width=981&top_left_y=233&top_left_x=321)
Figure 1.22. Deletion of $x$ from $G$.

see Figure 1.22. We write this operation as $G_{1}=G-x$. In $G_{1}$, we can choose and delete another vertex to obtain a graph $G_{2}$ and so on; sequential deletion of vertices results in a sequence of graphs.

We may want to delete an entire subset of vertices; it is equivalent to a sequential deletion of the respective vertices in any order. Sometimes deletion of vertices is called strong deletion because the vertices are removed from a graph together with all incident edges.

Weak deletion of a vertex. Again, let us have a graph $G=(X, E)$ and a vertex $x \in X$. Weak deletion of $x$ from $G$ is removing of $x$ from set $X$. Now the set $E(x)$ remains in the graph but it loses the vertex $x$. The only exception is if $E(x)$ contains loops: we assume the loops disappear. All other edges from $E(x)$ become loops and remain in the graph obtained.

If the very same vertex is weakly deleted from $G$, see Figure 1.23, we obtain a different graph $G_{1}$. We also write this operation as $G_{1}=G-x$ with understanding that the meaning of deletion (strong or weak) is clear from the context. In our example, see Figure 1.23, $E(x)=\left\{e_{1}, e_{2}, e_{3}\right\}$ and all these edges become loops in $G_{1}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-042.jpg?height=316&width=1108&top_left_y=1465&top_left_x=321)
Figure 1.23. Weak deletion of $x$ from $G$.

Deletion of an edge. It is the simplest operation of deletion: we just remove an edge from the list of edges. All the rest remains unchanged, see Figure 1.24. Sometimes the deletion of an edge is called a weak deletion.

Strong deletion of an edge. It is the removing of an edge from the list of edges and weak deletion of both of its vertices from the graph obtained. Strong deletion of the edge $e_{3}$ is shown in Figure 1.24. In both cases we write: $G_{1}=G-e_{3}$.

In graph theory, the term "deletion of a vertex" by default is meant as "strong deletion of a vertex", and the term "deletion of an edge" by default is meant as "weak deletion of

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-043.jpg?height=709&width=1108&top_left_y=215&top_left_x=321)
Figure 1.24. Strong and weak deletions of $e_{3}$ from $G$.

an edge". However, we are making this distinction here to fit to the general hypergraph approach. In Part II (Section 7.4.), we will see that strong deletions of vertices is the same as strong deletions of edges, and weak deletion of vertices is the same as weak deletion of edges in dual hypergraphs.

Contraction of an edge. Let us have a graph $G=(X, E)$ and an edge $e=\{x, y\} \in E$. Contraction of edge $e$ consists in the following two steps, see Figure 1.25:

1. Identifying vertices $x$ and $y$ in a new vertex called $x y$ and removing $e$ from $E$;
2. All edges of $G$ having one end at $x$ or $y$ will have this end at $x y$ with other end unchanged.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-043.jpg?height=479&width=1108&top_left_y=1763&top_left_x=370)
Figure 1.25. Contraction of $e$ in $G$.

If $G$ is a simple graph and $N(x) \cap N(y) \neq \emptyset$, then each vertex from $N(x) \cap N(y)$ will be connected with vertex $x y$ by two edges, i.e. graph $G_{1}$ will have multiple edges. If $G$ is not simple and has loops at $x$ or $y$, the loops remain in $G_{1}$ at vertex $x y$.

At last, if $G$ is not simple and had another edge $e^{\prime}$ connecting $x$ and $y$, then $e^{\prime}$ becomes a loop at vertex $x y$. So, contraction of an edge indeed means contraction of that edge up to one point. An example of contraction is shown in Figure 1.26.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-044.jpg?height=321&width=1030&top_left_y=528&top_left_x=417)
Figure 1.26. $G_{1}=G \cdot e$.

A graph $G_{1}$ is contractible to a graph $G_{2}$ if $G_{2}$ may be obtained from $G_{1}$ by a sequence of contractions of the edges. For example, any $C_{k}, k \geq 4$ is contractible to $C_{3}=K_{3}$, any tree with at least two vertices is contractible to $K_{2}$, any $K_{n}$ is contractible to $K_{m}$ if $n \geq m$ and so on. On the other hand, no $C_{k}$ can be contracted to $K_{4}$, no tree can be contracted to $K_{3}$. The maximum value of $n$ such that a graph $G$ is contractible to $K_{n}$ is called the Hadwiger number of the graph $G$, denoted by $\eta(G)$.

Taking the complement. Consider a simple graph $G=(X, E)$ with $|X|=n$. The complement of $G$ denoted by $\bar{G}$ is the graph on the same vertex set $X$ in which two vertices are adjacent if and only if they are disjoint in the original graph $G$. In other words, $\bar{G}=\left(X, E^{\prime}\right)$ where $E^{\prime}$ is such an edge set that $E \cup E^{\prime}$ forms the edge set of $K_{n}$. This is why $\bar{G}$ is called the complement of $G$. Evidently, $\overline{\bar{G}}=G, \bar{E}_{n}=K_{n}$ and $\bar{K}_{n}=E_{n}$. Notice that $P_{4}$ is isomorphic to $\overline{P_{4}}, C_{5}$ is isomorphic to $\overline{C_{5}}$, and $\overline{K_{r, s}}=\left\{K_{r}, K_{s}\right\}$. It may happen that $G$ is connected graph but $\bar{G}$ is not, see Figure 1.27.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-044.jpg?height=298&width=1033&top_left_y=1610&top_left_x=365)
Figure 1.27. $G$ and $\bar{G}$.

Sequential application of operations. Any of the basic operations above (except taking complement) may be applied sequentially many times what results in a sequence of graphs. Since we consider finite graphs, there will always be the last graph in this sequence. We then can consider the sequence of inverse operations and reconstruct the original graph from the last graph. This method is very common in graph theory and is used in proofs by mathematical induction.

Exercises 1.6.

1. Implement a weak sequential (in any order) deletion of vertices of $C_{4}, W_{5}, K_{5}, K_{3,3}$ and Petersen graph.
2. Implement a strong sequential (in any order) deletion of vertices of $C_{4}, W_{5}, K_{5}, K_{3,3}$ and Petersen graph.
3. Implement a weak sequential (in any order) deletion of edges of $C_{4}, W_{5}, K_{5}, K_{3,3}$ and Petersen graph.
4. Implement a strong sequential (in any order) deletion of edges of $C_{4}, W_{5}, K_{5}, K_{3,3}$ and Petersen graph; at each step, weakly remove the loops.
5. Implement a sequential (in any order) contraction of edges of $C_{4}, W_{5}, K_{5}, K_{3,3}$ and Petersen graph; at each step, weakly remove multiple edges.
6. Find the Hadwiger number of any tree, $C_{5}, W_{5}, K_{2,3}$.
7. Construct the complement of $C_{3}, C_{4}, C_{5}, C_{6}, K_{5}, K_{3,5}$, Petersen graph, cube, $P_{7}$, any tree on 6 vertices, $E_{5}, 2 C_{3}$.
8. Show that $\bar{C}_{5} \cong C_{5}$.
9. Show that $\bar{C}_{6}$ is isomorphic to a prism.
10. How are the degree sequences of $G$ and $\bar{G}$ related ?

Computer Projects 1.6. Write a program for the following operations.

1. Given any graph representation of a graph, delete a vertex strongly.
2. Given any graph representation of a graph, delete a vertex weakly.
3. Given any graph representation of a graph, delete an edge strongly.
4. Given any graph representation of a graph, delete an edge weakly.
5. Given any graph representation of a graph, construct the same representation for the complement.
6. Given any graph representation, implement exercises 1-5 with drawing on the screen a graph obtained at each intermediate step. Disregard multiple edges and loops.

### 1.7. Basic Subgraphs

Graphs as combinatorial structures may have many different properties. The properties are very often determined by the presence or absence of some specific substructures called subgraphs. We next consider some of them.

Subgraphs. Let us have a graph $G=(X, E)$. Any graph $G^{\prime}=\left(X^{\prime}, E^{\prime}\right)$ is called a subgraph of $G$ if and only if $X^{\prime} \subseteq X$, and $E^{\prime} \subseteq E$. In such case, we write $G^{\prime} \subseteq G$. Since $E^{\prime}$ contains only the elements of $E$, both ends of any edge from $E^{\prime}$ must be in $X^{\prime}$. Therefore, $G^{\prime}$ can be obtained from $G$ by strong deletion of vertices $X-X^{\prime}$ (sequentially in any order or at once) and further weak deletion of remaining edges $E-E^{\prime}$ (sequentially in any order or at once). In Figure 1.28, both $G_{1}$ and $G_{2}$ are subgraphs of $G$ : $G_{1}$ is obtained by strong deletion of vertex $x_{1}$ and weak deletion of edge $\left\{x_{3}, x_{5}\right\}$, and $G_{2}$ is obtained by strong deletion of

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-046.jpg?height=396&width=1134&top_left_y=233&top_left_x=313)
Figure 1.28. Graph $G$, subgraph $G_{1}$ and induced subgraph $G_{2}$.

$x_{2}$ and $x_{4}$. It is evident that the order in which the vertices and edges are deleted is not important.

Induced subgraphs. A graph $G^{\prime}=\left(X^{\prime}, E^{\prime}\right)$ is called an induced subgraph of a graph $G=(X, E)$ if $X^{\prime} \subseteq X$ and all edges of $G$ having both ends in $X^{\prime}$ form edge set $E^{\prime}$. Sometimes we say that $G^{\prime}$ is a subgraph induced by $X^{\prime}$. Induced subgraph $G^{\prime}$ may be obtained from $G$ by just strong deletion of vertices $X-X^{\prime}$ (sequentially in any order or at once). Induced subgraph is a special case of subgraph. A subgraph is not induced if at least one edge of $G$ with both ends in $X^{\prime}$, is missing. In a graph $G$, it is convenient to denote the subgraph induced by a set $Y \subseteq X$ by $G_{Y}$.

In Figure 1.28, $G_{2}$ is an induced subgraph of $G$ but $G_{1}$ is not. One can see that $G$ contains three subgraphs isomorphic to $K_{3}$, two subgraphs isomorphic to $C_{4}$ and one subgraph isomorphic to $C_{5}$. Among these subgraphs, only $K_{3}$ 's are induced.

Cycles. In a graph, any subgraph representing a sequence of vertices such that every two consecutive vertices are connected by an edge, and, the first and the last vertices coincide, is called the cycle. The number of edges in a cycle is called its length. A cycle is called odd or even if its length is respectively odd or even. Cycles may be induced or not; not every induced cycle is isomorphic to the simple cycle $C_{k}$ for some $k \geq 3$. For example, the sequence of vertices $x_{2}, x_{3}, x_{4}, x_{5}, x_{2}$, see Figure 1.28, forms the cycle of length 4, which is isomorphic to $C_{4}$ (represented by graph $G_{1}$ ), however, if we consider an induced subgraph, then we need to add the edge $\left\{x_{3}, x_{5}\right\}$ to $G_{1}$. A cycle which has all the vertices different (except the first and the last) is called simple. For example, the cycle $x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{1}$ is simple, but the cycle $x_{1}, x_{2}, x_{5}, x_{3}, x_{4}, x_{5}, x_{1}$ is not simple because the vertex $x_{5}$ is used twice. Though the length of the last cycle is 6 , it is not isomorphic to $C_{6}$ by the same reason. Notice that any odd cycle, if it is not simple, then it can be split into two cycles one of which is odd and another is even. This implies that if a graph has an odd cycle, then it has a simple odd cycle.

Cliques. Since graphs have vertices, they always contain subgraphs isomorphic to some of $K_{1}, K_{2}, K_{3}, \ldots, K_{n}$. They are called cliques. If we have a subgraph isomorphic to $K_{r}$ which is not contained in a subgraph isomorphic to $K_{r+1}$, then we say that $K_{r}$ is the maximal by inclusion complete subgraph, or, equivalently, the maximal clique. Being maximal by inclusion, different cliques may have different size, i.e. the number of vertices. The largest size of a clique among all the cliques of a graph $G$ is called the clique number of $G$
denoted by $\omega(G)$. Simply, $\omega(G)$ is the maximum number of pairwise adjacent vertices. For any graph $G, 1 \leq \omega(G) \leq n$.

For example, see Figure 1.28, vertices $x_{2}$ and $x_{3}$ induce $K_{2}$ in graph $G$ but it is not a maximal clique since it is not maximal; it is contained in $K_{3}$ induced by vertices $x_{2}, x_{3}, x_{5}$ which is maximal by inclusion. On the other hand, the same vertices $x_{2}$ and $x_{3}$ in graph $G_{1}$ form a maximal clique. We conclude that $\omega(G)=3$ and $\omega\left(G_{1}\right)=\omega\left(G_{2}\right)=2$.

Independent sets. Similarly to complete subgraphs, any graph contains subgraphs isomorphic to some of $E_{1}, E_{2}, \ldots, E_{n}$. In a graph $G$, a subset of vertices which induces a subgraph $E_{k}$ is called the stable set, or independent set. There are also maximal by inclusion and not maximal by inclusion stable sets. The largest size of a stable in a graph $G$ is called the stability number, denoted by $\alpha(G)$. Simply, $\alpha(G)$ is the maximum number of pairwise disjoint vertices. For any graph $G, 1 \leq \alpha(G) \leq n$.

Observe that $\omega(G)=\alpha(\bar{G})$ and $\alpha(G)=\omega(\bar{G})$ because when taking the complement every complete subgraph becomes a stable set and vice versa.

For graph $G$, see Figure 1.28, vertices $x_{1}$ and $x_{3}$ form a stable set, vertices $x_{2}$ and $x_{4}$ form another stable set. Both are maximal by inclusion, and $\alpha(G)=2$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-047.jpg?height=344&width=1030&top_left_y=1028&top_left_x=368)
Figure 1.29. Maximal cliques and stable sets.

One more example is shown in Figure 1.29. In $G_{1}$, vertices 1 and 2 form a clique, and vertices 2, 3, and 4 form a clique, $\omega\left(G_{1}\right)=3$. In $G_{2}$, vertices $a, b$, and $d$ form a maximal by inclusion stable set, and vertices $a, b, e$, and $f$ also form a maximal by inclusion stable set; the last being maximal is maximum, so $\alpha\left(G_{2}\right)=4$.

Important comment. In graph theory, given any property, it is common to use term maximal (minimal) in the sense of maximal (minimal) by inclusion and term maximum (minimum) in the sense of largest (smallest) over all maximal (minimal). The difference is similar to the difference between the local and global maximum (minimum) of a function.

Transversals (vertex covers). In a graph $G=(X, E)$, a subset of vertices $T \subseteq X$ is called a transversal (vertex cover) if its complement $X \backslash T$ is an independent set. It means that every edge of $G$ has at least one end in $T$. The minimum cardinality of a transversal of a graph $G$ is called the transversal number and denoted by $\tau(G)$. It follows from the definitions above that for any graph $G$,

$$
\alpha(G)+\tau(G)=|X| .
$$

Spanning subgraphs. Let us have a graph $G=(X, E),|X|=n$. Any subgraph $G^{\prime} \subseteq G$ such that $G^{\prime}=\left(X, E^{\prime}\right)$ is called a spanning subgraph. Thus spanning subgraphs have the same vertex set as the graph itself. Spanning subgraph which is a tree is called spanning
tree. If a graph has a spanning tree, then it is connected because any tree is a connected graph.

In Figure 1.29, if we weakly delete edges $\{1,2\}$ and $\{2,3\}$, then we obtain a spanning tree of $G_{1}$.

Matchings. In a simple graph $G$, a subgraph in which every vertex has degree 1, is called a matching. Every matching simply represents a collection of edges which have no common vertices, i.e., which are pairwise disjoint. A perfect matching is a matching which is a spanning subgraph. The maximum size of a matching (over all matchings) is denoted by $\nu(G)$. If a graph $G$ has a perfect matching, then clearly, $n$ is an even number and $\nu=n / 2$.

In graph $G_{2}$, see Figure 1.29, edge $\{c, d\}$ forms a maximal by inclusion matching. However, a maximum matching is formed for example by edges $\{a, c\}$ and $\{d, e\}$, and $\nu\left(G_{2}\right)=2$.

Since at least one vertex from every edge of any matching must belong to any transversal, the cardinality of any transversal is at least the cardinality of any matching; i.e, for any graph $G$,

$$
\tau(G) \geq v(G) .
$$

Therefore, if we have a matching and a transversal of the same cardinality, then both are optimal.

Factors. Let $G$ be a simple graph. A $k$-factor of $G$ is a spanning subgraph in which every vertex has degree $k$. In this way, 1-factor represents a perfect matching, 2-factor is a cycle or a collection of disjoint cycles, and so on.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-048.jpg?height=373&width=1227&top_left_y=1326&top_left_x=269)
Figure 1.30. Factors.

Factors not always exist, sometimes there are many distinct $k$-factors. Complete graphs have the largest number of factors. Examples of factors in a graph $G$ (which is a prism) are shown in Figure 1.30. Regular edges show a 1-factor which is a perfect matching; dashed edges show a 2-factor consisting of two connected components being $C_{3}$ each. There is one more 2-factor which is connected and represented by cycle $C_{6}$. The graph itself is a 3-factor.

Partition of the edges of a graph into $k$-factors is called $k$-factorization. The 1 -factorization of $K_{4}$ is shown in Figure 1.30.

Graph minors. A graph $G^{\prime}$ is a minor of a graph $G$, if $G^{\prime}$ can be obtained from $G$ by a sequence of any vertex deletions, edge deletions and edge contractions.

## Exercises 1.7.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-049.jpg?height=325&width=869&top_left_y=274&top_left_x=420)
Figure 1.31.

1. For graph in Figure 1.31, write down the list of all cliques, the list of all maximal cliques, and the list of maximum cliques. Begin with all 1-vertex cliques, then all 2-vertex cliques, and so on.
2. Write down the list of all cliques of $P_{6}, C_{3}, C_{4}, C_{5}, W_{4}, W_{5}, K_{2,3}$, cube and Petersen graph. Begin with all 1-vertex cliques, then all 2-vertex cliques, and so on.
3. Write down the list of all maximal cliques of $P_{6}, C_{3}, C_{4}, C_{5}, W_{4}, W_{5}, K_{2,3}$, cube and Petersen graph.
4. Write down the list of all maximum cliques of $P_{6}, C_{3}, C_{4}, C_{5}, W_{4}, W_{5}, K_{2,3}$, cube and Petersen graph.
5. Using the concept of a tree, suggest a way to construct the list of all maximal independent sets in a graph $G$.
6. Write down the list of all independent sets of $P_{6}, C_{3}, C_{4}, C_{5}, W_{4}, W_{5}, K_{2,3}$, cube and Petersen graph. Begin with all 1-vertex independent sets, then all 2-vertex independent sets, and so on.
7. Write down the list of all maximal independent sets of $P_{6}, C_{3}, C_{4}, C_{5}, W_{4}, W_{5}, K_{2,3}$, cube and Petersen graph.
8. Write down the list of all maximum independent sets of $P_{6}, C_{3}, C_{4}, C_{5}, W_{4}, W_{5}, K_{2,3}$, cube and Petersen graph.
9. Implement exercises 2-6 for the complements of the same graphs.
10. Find the longest path in $C_{7}$, cube, $W_{9}$, Petersen graph.
11. Find the shortest and the longest cycles in $K_{4,4}$, cube, Petersen graph.
12. Find a spanning tree in cube, $K_{6,9}$, Petersen graph.
13. Find $\omega(G)$ for every graph drawn in this section and in Figure 1.21.
14. Find $\alpha(G)$ for every graph drawn in this section and in Figure 1.21.
15. Find $\tau(G)$ for every graph drawn in this section and in Figure 1.21.
16. Find $v(G)$ for every graph drawn in this section and in Figure 1.21.
17. Find $\alpha, \omega, \tau$, and $\nu$ of cube, Petersen graph, $K_{999}, K_{1000}, C_{20}, C_{21}, W_{99}, W_{100}, P_{n}, K_{n}, C_{n}, W_{n}$, for all integers $n \geq 2$.
18. Find all non isomorphic minors of $W_{5}$.

Computer Projects 1.7. Using a convenient graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, a subset of vertices and a subset of edges. Check if the subsets form a subgraph of $G$.
2. Given a graph $G$ and a subset of vertices. Output the subgraph induced by the subset.
3. Given a graph $G$ and a subset of vertices. Check if the subset induces a clique.
4. Given a graph $G$ and a subset of vertices. Check if the subset is an independent set of vertices.
5. Given a graph $G$ and a clique. Check if the clique is maximal.
6. Given graph $G$ and an independent set. Check if the set is maximal.
7. Input: Petersen graph. Output: the collection of all maximal independent subsets.
8. Given a graph $G$ and a subset of vertices. Check if the subset is a transversal.
9. Given a graph $G$ and a list of edges. Check if the edges form a matching in $G$.
10. Given a graph $G$ and a list of edges. Check if the edges form a $k$-factor in $G$.

### 1.8. Separation and Connectivity

Recall that while deleting vertices we always mean strong deletion. Let $G=(X, E)$ be a simple connected graph and $x, y \in X$. If vertices $x$ and $y$ are not adjacent, deleting the set $X$ - $\{x, y\}$ from $G$ leaves only vertices $x$ an $y$, i.e. a disconnected graph. Any set $S \subseteq X$ of vertices which after deletion from $G$ leaves a disconnected graph is called a separator or vertex cut. A subgraph induced by some separator is also called separator. Among connected graphs, only complete graphs do not have separators. For disconnected graphs, a separator is any set of vertices deleting of which increases the number of connected components. So, if $S$ is a separator in $G$, then there are at least two vertices, say $x$ and $y$ which are separated by $S$; in this case, $S$ is called $(x, y)$-separator. The meaning of a separator is that all $(x, y)$-paths pass through it.

Separators may contain other subsets which are also separators. A separator which does not contain any other separator as a proper subset, is called a minimal separator. As usually, minimality is meant by inclusion; different minimal separators may have different size. The minimum over all sizes of all minimal separators is called the connectivity of $G$ and denoted by $\mathrm{k}(G)$. There is only one exception here, namely graph $K_{n}$. Since it has no separators, it is convenient to put by definition $\mathrm{K}\left(K_{n}\right)=n-1$. So, for any incomplete connected graph $G, \mathrm{k}(G)$ is the size of the smallest separator.

There is one more important concept related to separation. A graph $G$ is called $k$ connected if connectivity $\mathrm{K}(G) \geq k$. So, all graphs are 0-connected, connected graphs are 1-connected, connected graphs having $\mathrm{K}(G) \geq 2$ are 2-connected and so on. Generally, if a graph $G$ is $k$-connected, then it is $(k-1)$-connected, $(k-2)$-connected, and so on. But this implication is not working in the opposite way: if a graph is $k$-connected, it may be not $(k+1)$-connected. The inclusion of connectivity classes is shown in Figure 1.32.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-051.jpg?height=792&width=1196&top_left_y=210&top_left_x=285)
Figure 1.32. Connectivity classes.

Figure 1.33 shows a graph $G$ that has many separators. Set $\{2,3,5,6\}$ is a (1,4)separator though it is not a minimal separator. Subsets $\{2,6\}$ and $\{2,5\}$ also represent (1,4)-separators both being minimal. It is seen from the figure that for this graph $\mathrm{K}(G)=2$.

Graph $G$ in Figure 1.33 is 2-connected. Therefore, it is 1-connected and 0-connected. But it is not 3-connected and it is not $k$-connected for any $k \geq 3$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-051.jpg?height=316&width=779&top_left_y=1414&top_left_x=419)
Figure 1.33. 2-connected graph $G$.

Suppose we delete a separator $S$ from a connected graph $G$ and obtain two connected components induced by vertex sets $X_{1}$ and $X_{2}$. The two subgraphs induced by $X_{1} \cup S$ and $X_{2} \cup S$ are called derived subgraphs of the graph $G$ with respect to separator $S$. We will denote them by $G_{X_{1} \cup S}$ and $G_{X_{2} \cup S}$, or simply by $G_{1}$ and $G_{2}$ respectively, see Figure 1.34. Notice that both $X_{1}$ and $X_{2}$ are not empty sets, and none of the vertices from $X_{1}$ is adjacent to any of the vertices from $X_{2}$.

Proposition 1.8.1 In a connected graph $G$, if $S$ is a minimal separator, then each vertex of $S$ has neighbors in both $X_{1}$ and $X_{2}$.

Proof. If some $x \in S$ has no vertex in $X_{1}$ adjacent to it, then $S-\{x\}$ is also a separator of

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-052.jpg?height=375&width=1196&top_left_y=199&top_left_x=285)
Figure 1.34. Derived subgraphs: general scheme.

$G$ what contradicts the minimality of $S$. $\square$

For example in Figure 1.35, vertices 3, 5 and 6 in separator $\{2,3,5,6\}$ do not have neighbors in both components because the separator is not minimal; however, vertices 2 and 5 form a minimal separator and both have neighbors in each of two components. The two connected components produced by this separator are induced by vertex sets $\{3,4\}$ and $\{1,6\}$. The two derived subgraphs produced by separator \{2,5\} are induced by vertex sets \{1,2,5,6\} and \{2,3,4,5\}. They are shown as $G_{1}$ and $G_{2}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-052.jpg?height=712&width=1227&top_left_y=1131&top_left_x=269)
Figure 1.35. Derived subgraphs $G_{1}$ and $G_{2}$.

The separation scheme above and Proposition 1.8.1 easily generalize for the case if deletion of $S$ leaves any number $k \geq 2$ connected components induced by $X_{1}, X_{2}, \ldots, X_{k}$. The derived subgraphs then are: $G_{1}=G_{X_{1} \cup S}, G_{2}=G_{X_{2} \cup S}, \ldots$, and $G_{k}=G_{X_{k} \cup S}$.

Another idea is that one can delete edges from a connected graph and obtain a disconnected graph. Such subsets of edges are called edge-separators or edge-cuts. If an edge itself is a separator, it is called a bridge.

What do we need this for? The answer is that many important properties of graphs
can be successfully investigated by using derived subgraphs. Derived subgraphs have less vertices than original graph what opens the way for mathematical induction.

We end the section with formulation of the important Menger's Theorem:
Theorem 1.8.1 (Menger, 1927) In a connected graph $G$, for two non adjacent vertices $x$ and $y$, the minimum number of vertices in an ( $x, y$ )-separator equals the maximum number of (internally) vertex disjoint $(x, y)$-paths.

Idea behind the proof: to disconnect vertices $x$ and $y$, one need to destroy every $(x, y)$ path. $\square$

## Exercises 1.8.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-053.jpg?height=414&width=915&top_left_y=871&top_left_x=424)
Figure 1.36.

1. For every pair of disjoint vertices of graph $G$, see Figure 1.36, find a separator.
2. For every pair of disjoint vertices of graph $G$, see Figure 1.36, find a minimal separator.
3. For graph $G$ in Figure 1.36, find the connectivity $\mathbf{K}(G)$.
4. For which integer $k \geq 0$, graph $G$ in Figure 1.36 is $k$-connected?
5. For separator $\{1,3,4,7,8\}$, construct the derived subgraphs.
6. For separator $\{1,8,3,4,6\}$, construct the derived subgraphs.
7. For separator $\{5,6,7,8,2\}$, construct the derived subgraphs
8. Apply Proposition 1.8.1 for separator \{1,8,3\}.
9. Find an edge-separator for graph $G$ in Figure 1.36.
10. For graph $G$ in Figure 1.36 find a minimal (1,4)-separator.
11. For graph $G$ in Figure 1.36 find a minimal (1,4)-edge-separator.
12. What is the smallest number of edges that disconnect graph $G$ in Figure 1.36?
13. Apply Menger's Theorem to vertices 3 and 6 in graph $G$, see Figure 1.36.

Computer Projects 1.8. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. For a given subset of vertices in a graph $G$, find out if the subset is a separator.
2. For a separator of a graph $G$, determine if the separator is minimal.
3. Find the connectivity of a graph $G$.
4. For a given subset of edges in a graph $G$, find out if the subset is an edge-separator.

## Chapter 2

## Trees and Bipartite Graphs

"- Why are these graphs called "trees"?

### 2.1. Trees and Cycles

Theorem 2.1.1 For a simple graph $G$, the following statements are equivalent:

1. $G$ is a tree;
2. $G$ is connected and $m(G)=n(G)-1$;
3. $G$ has no cycles and $m(G)=n(G)-1$;
4. There is a unique path connecting any two vertices of $G$;
5. $G$ has no cycles and connecting any of its two nonadjacent vertices by an edge results in precisely one cycle.

Proof. $1 . \Rightarrow 2 . G$ is connected by the definition of tree. Prove the equality by induction on $n$. For $n=1,2$ the statement is trivial. Assume $n(G)>2$. Since $G$ is a tree it has a pendant vertex; strongly delete it and obtain a tree $G_{1}$. For $G_{1}$ by the induction hypothesis, $m\left(G_{1}\right)=n\left(G_{1}\right)-1$. Now return deleted vertex with an edge and reconstruct $G$. Evidently, $m(G)=m\left(G_{1}\right)+1$, and $n(G)=n\left(G_{1}\right)+1$, and the implication follows.
2. ⇒ 3. Prove that $G$ has no cycles. By contradiction, suppose that $G$ has a cycle. Weakly delete an edge $e=\{x, y\}$ of this cycle; $G-e$ is connected since $(x, y)$-path remains. If $G-e$ contains cycles, repeat the procedure until graph obtained contains no cycles. Since it is connected, it is a tree, and by 1. $\Rightarrow 2 . m=n-1$, a contradiction to the fact that we deleted at least one edge.
3.⇒ 4. Let $G$ have no cycles and $m=n-1$. It may have many components. If it has $k>1$ components $G_{1}, G_{2}, \ldots, G_{k}$, every $G_{i}$ is a tree. By $1 . \Rightarrow 2 . m_{i}=n_{i}-1$ for each $G_{i}$. Therefore $m(G)=m_{1}+m_{2}+\cdots+m_{k}=\left(n_{1}-1\right)+\left(n_{2}-1\right)+\cdots+\left(n_{k}-1\right)=n-k$. So we obtain $m=n-1=n-k$ which implies $k=1$ and $G$ is connected. It means that there is a path between any pair of vertices. If there are two different paths connecting a pair of vertices, then there is a cycle what contradicts to condition 3 . Therefore, 4 . holds.
4. ⇒ 5. $G$ cannot have cycles because in any cycle any two vertices are connected by two different paths. Let $x, y$ be two nonadjacent vertices. Hence there is a unique $(x, y)$ path. Therefore adding the edge $\{x, y\}$ to $G$ produces a cycle. This cycle is unique because otherwise, if we obtain two cycles $C_{k}$ and $C_{l}$, the subgraph $\left(C_{k} \cup C_{l}\right)-\{x, y\}$ forms the third cycle, a contradiction to 4.
5.⇒ 1. $G$ has no cycles. If it is not a tree (i.e. it is disconnected), then connect two vertices from different components by an edge. We obtain no cycles, a contradiction. $\square$

Let $G$ be a simple graph having $k$ connected components. The number $\Lambda(G)=m(G)-$ $n(G)+k$ is called the cyclomatic number of $G$. If $G$ is connected, then $k=1$ and $\wedge=$ $m-n+1=m-(n-1)$. Theorem 2.1.1 in fact states that $n-1$ is the minimum number of edges for a graph to be connected, or, equivalently, to be a tree. Therefore, the number $m-(n-1)$ shows how many extra edges graph $G$ has. Starting from any spanning tree, one can sequentially add remaining $\Lambda$ edges to reconstruct $G$. Every such edge forms precisely one cycle with spanning tree. These cycles are called elementary and edges are called chords with respect to the spanning tree.

If $G$ is disconnected, we apply the same reasoning to each component and replace "tree" with "forest". In other words, the cyclomatic number indicates "how far" graph $G$ is from the forest. That is why it is called the "cyclomatic number".

Indeed, the following holds:
Corollary 2.1.1 $\wedge(G)=0$ if and only if $G$ is a forest.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-056.jpg?height=337&width=730&top_left_y=1253&top_left_x=469)
Figure 2.1. Spanning tree, chords and cycles.

An example of a graph and its cyclomatic number is shown in Figure 2.1. The solid edges form a spanning tree, the dashed edges show the chords. Correspondingly, $\Lambda(G)=$ $m-n+1=7-5+1=3$. One can see that every chord forms exactly one elementary cycle with the spanning tree. The total number of cycles however, is greater than $\Lambda$. There are additional cycles that can be expressed as combinations of elementary cycles.

Generally, a graph may have many spanning trees, and therefore many different sets of elementary cycles; important however is that any cycle can be expressed as a combination of elementary cycles and the number of elementary cycles is always the same, namely equal to the cyclomatic number.

Let us agree that two spanning trees of $K_{n}$ are considered different if they are formed by different sets of edges; in fact, some of them may be isomorphic.

Theorem 2.1.2 (Cayley's Formula, 1889) The number of spanning trees in graph $K_{n}$, $n \geq 1$, equals $n^{n-2}$.

Since any tree is a connected graph, with the agreement above Cayley's formula implies that there are total $n^{n-2}$ trees for every $n$. For example, if $n=3$, then there are three "different" trees which in fact all are isomorphic to each other.

Exercises 2.1.

1. Find the cyclomatic number of $E_{n}, C_{n}, K_{n}, W_{n}$, prism, cube and the Petersen graph.
2. Find all spanning trees for graph $G$ in Figure 2.1.
3. Describe the procedure for finding all spanning trees in $C_{6}, K_{4}, W_{6}$.
4. Describe the procedure for finding all spanning trees in cube and prism.

Computer Projects 2.1. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Generate all spanning trees in prism, cube and the Petersen graph.
2. Generate all spanning trees in $K_{n}, W_{n}, n \geq 5$.

### 2.2 Trees and Distance

Graph $E_{n}$ is called trivial. Unless stated otherwise, we consider nontrivial graphs. It means that any graph has at least two vertices and at least one edge.

Let $G=(X, E)$ be a graph, $x, y \in X$. The distance from $x$ to $y$ denoted by $d(x, y)$ is the length of the shortest ( $x, y$ )-path. If there is no such path in $G$, then $d(x, y)=\infty$; evidently, in this case $G$ is disconnected and $x$ and $y$ are in different components. Any segment of a shortest path is a shortest path itself. The distance between $x$ and a set of vertices $Y \subseteq X$ is defined as $d(x, Y)=\min _{y \in Y} d(x, y)$. It is the shortest distance between $x$ and any vertex of $Y$.

For all $x, y, z \in X$, the following properties of distances hold:

1. $d(x, y) \geq 0$, and $d(x, x)=0$;
2. $d(x, y)=d(y, x)$;
3. $d(x, y) \leq d(x, z)+d(z, y)$ (triangle inequality).

The diameter of $G$ denoted by $\operatorname{diam}(G)$ is $\max _{x, y \in X} d(x, y)$; in other words it is the distance between the farthest vertices. For connected graphs, diameter is a positive integer number. An $(x, y)$-path for which $d(x, y)=\operatorname{diam}(G)$ is called a diametral path. There may be many diametral paths in a graph. Let $N_{\infty}(x)$ denote the set of farthest vertices from vertex $x$. It means that if $y \in N_{\infty}(x)$ and $z \notin N_{\infty}(x)$, then $d(x, z)<d(x, y)$. The distance between vertex $x$ and set $N_{\infty}(x)$ is called the eccentricity of $x$. The center of $G$ is a set of vertices of minimum eccentricity. The radius of $G$ is equal to eccentricity of any vertex from the center. At last, a vertex of degree 1 is called pendant vertex or leaf.

Theorem 2.2.1 Let $x \in X$ be an arbitrary vertex in a tree $T$. Then every vertex $y \in N_{\infty}(x)$ is pendant.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-058.jpg?height=216&width=830&top_left_y=247&top_left_x=468)
Figure 2.2.

Proof. Let $y \in N_{\infty}(x)$. Consider $(x, y)$-path and a vertex $z$ on this path adjacent to $y$, see Figure 2.2. By contradiction, assume there is another vertex $z^{\prime}$ adjacent to $y$. The shortest $\left(x, z^{\prime}\right)$-path cannot use $y$ because it would be longer than $d(x, y)$. Therefore, it must use vertex $z$ or any other vertex from $(x, y)$-path. In any case we obtain a cycle (at least triangle) what contradicts that $T$ is a tree. $\square$

Corollary 2.2.1 Any tree has at least two pendant vertices.
Proof. Consider $x, y$ such that $d(x, y)=\operatorname{diam}(T)$. Evidently, $x \in N_{\infty}(y)$ and $y \in N_{\infty}(x)$, hence by Theorem 2.2.1 both $x$ and $y$ are pendant. $\square$

Theorem 2.2.2 (Jordan, 1869) The center of a tree is either $K_{1}$ or $K_{2}$.
Proof. Notice that strong deletion of any pendant vertex from a tree $T$ leaves all distances between remaining vertices unchanged. Delete all pendant vertices from $T$, obtain tree $T_{1}$. Since we delete all pendant vertices, by Theorem 2.2.1, the eccentricity of each vertex in $T_{1}$ is less than the eccentricity of the same vertex in $T$ by 1 . Therefore vertices with minimum eccentricity in $T$ and $T_{1}$ are the same. Repeat the procedure as many time as possible. We obtain a sequence of trees $T_{1}, T_{2}, T_{3}, \ldots$, the last being $K_{2}$ or $K_{1}$ what is the center. $\square$

The theorem explicitly presents an algorithm how to find the center of a tree. One can prove that $\operatorname{diam}(T)$ can be found in the following two steps: 1) start at any vertex $z$ and find any $x \in N_{\infty}(z)$; 2) repeat the procedure for $x$ and find any $y \in N_{\infty}(x): \operatorname{diam}(T)=d(x, y)$.

Exercises 2.2.

1. For the tree in Figure 2.3, find the diameter, radius and center.
2. For each vertex $x$ in the tree in Figure 2.3, find $N_{\infty}(x)$ and the eccentricity.

Computer Projects 2.2. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given any tree, find the diameter.
2. Given any tree, find the center.
3. Given any tree and a vertex $x$, find $N_{\infty}(x)$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-059.jpg?height=474&width=1113&top_left_y=194&top_left_x=326)
Figure 2.3.

### 2.3. Minimum Spanning Tree

Sometimes, as in this section, we use letters $\mathcal{D}$ for an edge set and $D$ for its elements because we need letter $E$ for another purpose. A graph $G=(X, \mathcal{D})$ is called weighted if each edge $D \in \mathcal{D}$ is assigned a positive real number $w(D)$ called the weight of edge $D$. Usually, in many practical applications, the weight represents a distance, time, cost, capacity, resistance, probability, etc. Consider any spanning tree $T=(X, E)$ of $G$. The weight $w(T)$ of tree $T$ is the sum of weights of all edges of $T$. Different spanning trees may have different weights. The problem of finding a spanning tree of minimum (maximum) weight is called the minimum (maximum) spanning tree problem. It is one of the few optimization problems that allows an efficient algorithm for any graph.

Algorithm 2.3.1 Finding minimum spanning tree (Kruskal's algorithm)
INPUT: A connected weighted graph G.
OUTPUT: A tree T of minimum weight.

1. Order the edges of $G$ in increasing (non-decreasing) order of their weights and set $T$ to be an empty graph.
2. Add the first edge from the ordering to $T$.
3. Consider the next edge in the ordering. If it produces a cycle in $T$ with already included edges, skip it. Otherwise, include it in $T$.
4. Repeat step 3. until $T$ is connected.
5. Output T.

Theorem 2.3.1 (Kruskal, 1956) For any connected weighted graph G, Algorithm 2.3.1 constructs a spanning tree of minimum weight.

Proof. First of all, Algorithm produces a tree because it does not create cycles and cannot end when $T$ is disconnected. Since $G$ is connected, some edges between connected components of $T$ exist and at least one must be included in $T$.

Suppose $T$ is not an optimal spanning tree, i.e. there exist a spanning tree $T^{*} \neq T$ of minimum weight such that $w\left(T^{*}\right)<w(T)$. Let $D$ be the first edge in the ordering that was chosen for $T$ and is missing in $T^{*}$. Adding $D$ to $T^{*}$ creates a unique cycle. Since $T$ has no cycles, this cycle contains an edge $D^{\prime}$ which is not in $T$. Construct the spanning tree $T^{*}+D-D^{\prime}$. Now notice that $w(D) \leq w\left(D^{\prime}\right)$, and therefore $w\left(T^{*}+D-D^{\prime}\right)=w\left(T^{*}\right)+$ $w(D)-w\left(D^{\prime}\right) \leq w\left(T^{*}\right)$. We obtain a new spanning tree of the minimum weight which has one edge more in common with $T$. Repeating this procedure as many times as necessary, we eventually obtain $T$ what proves that it is an optimal spanning tree. $\square$

Algorithm and Theorem work if we need to find a spanning tree of maximum weight; we just proceed in inverse ordering of the edges.

Exercises 2.3.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-060.jpg?height=284&width=1038&top_left_y=913&top_left_x=400)
Figure 2.4. Weighted graph $G$ with integer weights.

1. Choose any spanning tree in graph $G$, see Figure 2.4, and compute its weight.
2. In graph $G$ in Figure 2.4, find the minimum spanning tree in two different ways: a) intuitively;
    b) by using Kruskal's algorithm.
3. In graph $G$ in Figure 2.4, find the maximum spanning tree in two different ways: a) intuitively;
    b) by using Kruskal's algorithm.
4. Given weighted complete graph $K_{n}$ with all weights equal $w>0$, how many minimum weighted trees does it have?

Computer Projects 2.3. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a weighted graph $G$, find a spanning tree and compute its weight.
2. Given a weighted graph $G$ and a spanning tree; check if the tree is of maximum (minimum) weight.
3. Given a weighted graph $G$, implement the Kruskal's algorithm.
4. Given a weighted graph $G$, find the maximum spanning tree.

### 2.4. Bipartite Graphs

Theorem 2.4.1 (König, 1936) A graph G is bipartite if and only if it does not have odd cycles.

Proof. ⇒ Let $G$ be a bipartite graph with parts $A$ and $B$, and $C_{k}$ be any cycle in it with a vertex $x \in A$. Traverse $C_{k}$ starting at $x$ in any direction. Since $G$ is bipartite, each time we alternate parts $A$ and $B$. Since we end at $x, k$ is even.

⇐ Let $G=(X, E)$ be a connected nontrivial ( $n \geq 2$ ) graph without odd cycles; choose any $x \in X$. Denote $\{x\}$ by $N_{0}$, neighborhood $N(x)$ by $N_{1}$, vertices at distance 2 from $x$ by $N_{2}$, vertices at distance 3 from $x$ by $N_{3}$ and so on, The last set in this sequence is $N_{\infty}(x)$ denoted by $N_{k}$. We obtain the following partition of $X$ :

$$
X=N_{0} \cup N_{1} \cup N_{2} \cup N_{3} \cup \ldots \cup N_{k} .
$$

Observe that $N_{i} \cap N_{j}=\emptyset, i \neq j$. Moreover, any edge of $G$ connects vertices either from the same $N_{i}$ or from consecutive sets.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-061.jpg?height=287&width=1124&top_left_y=1041&top_left_x=360)
Figure 2.5.

Now form a bipartition of $G$ by placing in $A$ all sets with even indices and placing in $B$ all sets with odd indices, so $X=A \cup B$. It remains to prove that there are no edges of $G$ inside any of sets $N_{i}$. By contrary, assume there is an edge $e=\{y, z\}$, such that $y, z \in N_{i}$ for some $i>0$, see Figure 2.5. Consider the shortest $(x, y)$-path and $(x, z)$-path. They may have common vertices other than $x$. Recall that every segment of a shortest path is also a shortest path. Let $x^{\prime}$ be the last common vertex counting from $x$. Then $\left(x^{\prime}, y\right)$-path and $\left(x^{\prime}, z\right)$-path have the same length, say $l$, and no common vertices other than $x^{\prime}$. Therefore, these paths and edge $e$ form a cycle $C_{2 l+1}$, a contradiction. $\square$

The idea of the proof of König's theorem allows to suggest a simple algorithm which not only gives the possibility to recognize bipartite graphs but is also used for finding solutions of many other problems.

## Algorithm 2.4.1 (Breadth-first search)

INPUT: A graph $G=(X, E)$
OUTPUT: A labeling of vertices of $G$ by the numbers 0,1,2,...

1. Start at arbitrary unmarked vertex and mark it with 0 ; set $i=0$;
2. Mark by $i+1$ all vertices which are not marked and adjacent to vertices marked $i$;

3. If there are unmarked vertices adjacent to marked vertices, set $i:=i+1$ and go to step 2;
4. End.

Clearly, each marked vertex of $G$ has a mark (label) $i$ which equals the distance to or from the initial vertex. To check whether $G$ is bipartite it is sufficient to add one more step: verify that no two vertices with equal labels are adjacent. If two different vertices with the same label induce an edge, then there is an odd cycle, and by Theorem 2.4.1, $G$ is not a bipartite graph. If $G$ is connected, then Algorithm 2.4.1 marks all the vertices. If $G$ is not connected, then some vertices remain unmarked; one can run it again starting at any unmarked vertex. The number of re-runs will coincide with the number of connected components of $G$.

To find the distance, i.e. the length of the shortest path between any two vertices of $G$, it is sufficient to run the algorithm starting at any of these vertices, and the label of the second vertex will be the distance.

If $G$ is a directed graph, then Algorithm 2.4.1 may be used to find the set of vertices that can be reached from a given vertex $x$ of $G$.

As the opposite to the breadth-first algorithm, there is another way of search in a graph which is called the depth-first search algorithm. We next describe the idea of the algorithm.

Assume we need to find a spanning tree in a connected graph $G$. Choose a vertex and declare it visited. Choose any unvisited vertex adjacent to the last visited vertex, declare it "current" and add connecting edge to the spanning tree. If there are edges connecting current vertex with other visited vertices, declare them as back edges. Choose another unvisited vertex adjacent to the last visited vertex and repeat this procedure as long as possible. We get stuck at a vertex which has no unvisited neighbors. At this point, we return back to the vertex from which the current vertex was visited (this step is called backtracking) and look for another unvisited neighbor. If there are such, we visit one and repeat the procedure. If there are none, we return one more step back and repeat the procedure again. We add to the spanning tree one edge at a time when visiting a new vertex; the back edges are not added because they form cycles with the edges of the tree. Eventually algorithm stops at the very first visited vertex. That vertex is called the root of the spanning tree. As the breadth-first search, the depth-first search algorithm can be applied to solve a number of different search problems.

We now continue the discussion of bipartite graphs. Let $G=(X, E)$ be a graph. The neighborhood $N(S)$ of a subset $S \subseteq X$ is the union of all neighborhoods of the vertices from $S$ minus $S$ itself, i.e.,

$$
N(S)=\cup_{x \in S} N(x) \backslash S .
$$

If $G=(X, Y ; E)$ is a bipartite graph, then the neighborhood of any subset of $X$ is in $Y$, and the neighborhood of any subset of $Y$ is in $X$. We will use the notation $N_{G}(S)$ to emphasize that the neighborhood is considered in a graph $G$.

Recall that a matching is a set of pairwise disjoint edges. We say that a matching covers a set of vertices if each vertex from the set is incident to an edge of the matching.

Theorem 2.4.2 (Hall, 1935) A bipartite graph $G=(X, Y ; E)$ has a matching that covers $X$ if and only if for every subset $S \subseteq X$,

$$
\left|N_{G}(S)\right| \geq|S| .
$$

Proof. $\Rightarrow$ If $G=(X, Y ; E)$ has a matching that covers $X$, then evidently, any subset $S \subseteq X$ has at least $|S|$ neighbors in $Y$, i.e., $\left|N_{G}(S)\right| \geq|S|$.

⇐ Let $G=(X, Y ; E)$ be a bipartite graph. We prove the sufficiency of the theorem by induction on $|X|$. If $|X|=1$, then by the definition of bipartite graph, the single vertex $x$ of $X$ has at least one neighbor $y$ in $Y$, thus the edge $x y$ is the required matching.

Let now $|X|>1$ and the theorem be true for all bipartite graphs with the first part on $<|X|$ vertices. There are two cases to consider.

Case 1: for any subset $S \subset X, S \neq X$,

$$
|S|<\left|N_{G}(S)\right| .
$$

Consider an arbitrary edge $x y$ of $G$. Delete strongly vertices $x$ and $y$ from $G$ and denote the bipartite graph obtained by $G^{\prime}=\left(X^{\prime}, Y^{\prime} ; E^{\prime}\right)$. Evidently, $\left|X^{\prime}\right|=|X|-1<|X|$. Since precisely one vertex is deleted from $Y$, the inequality (2.1) implies that in $G^{\prime}$ for any subset $S^{\prime} \subseteq X^{\prime}$, the following holds:

$$
\left|S^{\prime}\right| \leq\left|N_{G}\left(S^{\prime}\right)\right| .
$$

By the induction hypothesis, there exists a matching in $G^{\prime}$ that covers $X^{\prime}$. Add the edge $x y$ to it and obtain a matching that covers $X$ in graph $G$.

Case 2: there exists a subset $S_{0} \subset X, S_{0} \neq X$, such that

$$
\left|S_{0}\right|=\left|N_{G}\left(S_{0}\right)\right| .
$$

In Figure 2.6, which illustrates this case, the respective sets are shown by ellipses. We now split the vertex set of $G$ into two subsets:

$$
A=S_{0} \cup N_{G}\left(S_{0}\right) \text { and } B=(X \cup Y) \backslash A
$$

and consider two induced bipartite subgraphs, $G_{A}$ and $G_{B}$.
In $G_{A}$, for any subset $S \subseteq S_{0}$, we have that $N_{G_{A}}(S)=N_{G}(S)$. Therefore, $|S| \leq\left|N_{G_{A}}(S)\right|$. By the induction hypothesis, $G_{A}$ has a matching that covers $S_{0}$.

In $G_{B}$, for any subset $S \subseteq X-S_{0}$, we have that

$$
N_{G_{B}}(S)=N_{G}(S) \backslash N_{G}\left(S_{0}\right),
$$

see Figure 2.6. Therefore,

$$
\left|S_{0}\right|+|S|=\left|S_{0} \cup S\right| \leq\left|N_{G}\left(S_{0} \cup S\right)\right|=\left|N_{G}\left(S_{0}\right)\right|+\left|N_{G_{B}}(S)\right| .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-064.jpg?height=1098&width=849&top_left_y=202&top_left_x=482)
Figure 2.6.

Since $\left|S_{0}\right|=\left|N_{G}\left(S_{0}\right)\right|$ by (2.2), we obtain that $|S| \leq\left|N_{G_{B}}(S)\right|$. Hence by the induction hypothesis, graph $G_{B}$ has a matching that covers $X-S_{0}$.

Combining matchings of $G_{A}$ and $G_{B}$ we obtain a matching of $G$ that covers $X$. $\square$

Corollary 2.4.1 Every regular bipartite graph has a perfect matching.
Proof. Let $G=(X, Y ; E)$ be a $k$-regular ( $k \geq 1$ ) bipartite graph. Counting the degrees of vertices in $X$ and in $Y$ leads to the equality $k|X|=k|Y|$ what implies $|X|=|Y|$. It means that every matching that covers $X$, also covers $Y$.

Let $S \subseteq X$. Since $G$ is $k$-regular, the number $i$ of edges from $S$ to $N_{G}(S)$ is $i=k|S|$. Since each vertex from $N_{G}(S)$ has degree $k, i \leq k\left|N_{G}(S)\right|$; therefore, for any $S \subseteq X,\left|N_{G}(S)\right| \geq|S|$. By Theorem 2.4.2, $G$ has a perfect matching. $\square$

Recall that $\tau(G)$ is the cardinality of a minimum transversal of a graph $G$, i.e. the minimum number of vertices that "touch" all edges. As we mentioned in Section 1.7., for any graph $G, \tau(G) \geq v(G)$.

Theorem 2.4.3 (König, 1931) For any bipartite graph $G$,

$$
\tau(G)=\mathcal{V}(G) .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-065.jpg?height=606&width=1018&top_left_y=202&top_left_x=363)
Figure 2.7.

Proof. Let $G=(X, Y ; E)$ be a bipartite graph and $T \subseteq(X \cup Y)$ be a minimum transversal of $G$. We will construct a matching of size $\tau(G)=|T|$ what proves the theorem.

Let $X \cap T=A$ and $Y \cap T=B$, and $G_{1}=G_{A \cup(Y \backslash B)}$ and $G_{2}=G_{B \cup(X \backslash A)}$, see Figure 2.7. Since $A \cup B$ is a transversal, there are no edges between $Y \backslash B$ and $X \backslash A$. For each $S \subseteq A$, consider $N_{G_{1}}(S)$. If $\left|N_{G_{1}}(S)\right|<|S|$, then, because $N_{G_{1}}(S)$ "touches" all edges incident to $S$ that are not "touched" by $B$, we could replace $S$ by $N_{G_{1}}(S)$ and obtain a smaller transversal of $G$ than $T$. Since $T$ is a minimum transversal, this is impossible, and therefore, $\left|N_{G_{1}}(S)\right| \geq|S|$ for any subset $S \subseteq A$. By Theorem 2.4.2, graph $G_{1}$ has a matching that covers $A$. Applying the same reasoning to graph $G_{2}$, we obtain a matching in $G_{2}$ that covers $B$. Since graphs $G_{1}$ and $G_{2}$ have disjoint vertex sets, we combine these two matchings in one matching of graph $G$ that has $|A|+|B|=|T|=\tau(G)$ edges. Hence $\tau(G)=v(G)$. $\square$

Exercises 2.4.

1. Run the breadth-first search algorithm for prism, cube and Petersen graph starting at an arbitrary vertex.
2. For integers $m, n \geq 1$, formulate the conditions when $K_{m, n}$ has a perfect matching.
3. Find all perfect matchings in the cube.
4. For integers $m, n \geq 1$, find $\tau\left(K_{m, n}\right)$ and $v\left(K_{m, n}\right)$.
5. Run the breadth-first search algorithm for graph in Figure 2.8 to determine if it is bipartite.
6. For graph in Figure 2.8, find the values of $\tau$ and $\nu$ and the respective transversal and matching.

Computer Projects 2.4. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given an arbitrary graph $G$, run the breadth-first search algorithm to recognize if $G$ is bipartite.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-066.jpg?height=476&width=917&top_left_y=290&top_left_x=424)
Figure 2.8.

2. Given an arbitrary graph $G$, run the breadth-first search algorithm to recognize if $G$ is connected.
3. Given an arbitrary graph $G$, run the breadth-first search algorithm to recognize if $G$ is a tree.
4. Repeat projects 1-3 using the depth-first search algorithm.
5. Given a graph $G$ and a subset of vertices, determine if the subset is a transversal.
6. Given a graph $G$ and a subset of edges, determine if the subset is a matching.

## Chapter 3

## Chordal Graphs

"Smart people find shorter ways, i.e. the chords in common ways..."

### 3.1. Preliminary

If a connected graph $G$ is not a tree, then it has cycles. Some cycles may have two nonconsecutive vertices which are adjacent in $G$. The edge connecting them is a chord, or a diagonal of the cycle. Graph $G$ is called chordal if every cycle of length $\geq 4$ has a chord. Since cycles $C_{k}, k \geq 4$, have no chords as separate graphs, chordal graphs cannot contain them as induced subgraphs. In other words, if a chordal graph contains $C_{k}, k \geq 4$, then none of them is induced. Notice that cycles $C_{1}, C_{2}$, and $C_{3}$ do not have non-consecutive vertices and therefore cannot have chords; it explains why "chordality" begins with the cycles of length $\geq 4$.

A chord splits a cycle into two smaller cycles; if graph is chordal and at least one of the cycles is not a triangle, then it has another chord, and so on. Eventually, every cycle is split into a number of triangles. That is why chordal graphs are also known as "triangulated" or "rigid circuit" graphs.

As follows from the definition, the smallest graph which is not chordal is $C_{4}$. Figure 3.1 shows three graphs among which $G_{1}$ and $G_{3}$ are chordal and $G_{2}$ is not. For $G_{1}$, one can manually check that all cycles of length $\geq 4$ have chords; $G_{3}$ is a tree and has no cycle at all; $G_{2}$ contains an induced cycle $C_{4}$ shown by dashed edges.

Every graph is either chordal, or not. If a graph is not chordal, then it contains an induced cycle $C_{k}, k \geq 4$. Since trees contain no cycles, they all are chordal graphs.

A vertex is called simplicial if all of its neighbors are pairwise adjacent, i.e., the neighbors induce a complete subgraph. It follows that a vertex is not simplicial if it has two disjoint neighbors.

In Figure 3.1, simplicial vertices are labeled by "s". We will see that chordal graphs always have simplicial vertices. Moreover, as trees are the special case of chordal graphs, in the same way pendant vertices represent the special case of simplicial vertices.

Proposition 3.1.1 In a chordal graph, every induced subgraph is chordal.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-068.jpg?height=471&width=1227&top_left_y=210&top_left_x=269)
Figure 3.1.

Proof. If in a chordal graph an induced subgraph is not chordal, then it contains an induced cycle $C_{k}, k \geq 4$. Evidently, $C_{k}$ is an induced subgraph in the original graph, what contradicts that it is chordal. $\square$

The above property is important because it allows to prove many results about chordal graphs by induction: if we delete any vertex from a chordal graph, we obtain a chordal graph again.

### 3.2. Separators and Simplicial Vertices

"Separate and dominate - how old is that?"
Theorem 3.2.1 (Minimal separator theorem) A graph is chordal if and only if every minimal separator is a clique.

Proof. $\Rightarrow$ Let $G=(X, E)$ be a chordal graph with a minimal separator $S$. Assume we have two derived subgraphs $G_{1}=G_{X_{1} \cup S}$ and $G_{2}=G_{X_{2} \cup S}$, see Figure 3.2.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-068.jpg?height=277&width=1191&top_left_y=1722&top_left_x=287)
Figure 3.2. Minimal separator in a chordal graph.

We need to prove that $G_{S}$ is a clique. Consider any pair of vertices $x, y \in S$. Since $S$ is a minimal (by inclusion) separator, each of $x, y$ has neighbors in both $X_{1}$ and $X_{2}$. Choose a shortest $(x, y)$-path through $X_{1}$; its length is at least 2. Next choose a shortest $(x, y)$-path through $X_{2}$; its length is also at least 2. Combining these two $(x, y)$-paths we obtain a cycle
$C_{k}, k \geq 4$. Since there are no edges between $X_{1}$ and $X_{2}$ and $G$ is chordal, vertices $x$ and $y$ must be adjacent. Since $x$ and $y$ are arbitrary vertices of $S$, all vertices of $S$ are pairwise adjacent, i.e., $G_{S}$ is a clique.

In the case when there are more than two derived subgraphs, it is sufficient to consider any two of them.

⇐ Let $G=(X, E)$ be a graph in which every minimal separator is a clique. By contradiction, assume $G$ is not chordal. Then it contains an induced subgraph $C_{k}, k \geq 4$. Consider two nonadjacent vertices of $C_{k}$, say, $x$ and $y . C_{k}$ is formed by two different $(x, y)$-paths. Since $k \geq 4$, each such path contains at least one internal vertex. Since $C_{k}$ is induced, internal vertices of the first path are not adjacent to the internal vertices of the second path. Now notice that any minimal $(x, y)$-separator contains at least one internal vertex from each path, and therefore contains two nonadjacent vertices, a contradiction. $\square$

Theorem 3.2.2 (Dirac theorem, 1961) Every noncomplete connected chordal graph contains at least two simplicial vertices which are not adjacent.

Proof. Let $G=(X, E)$ be a connected chordal graph which is not a clique; hence $|X|=$ $n \geq 2$. We prove the statement by induction on $n$. The theorem is evident for $n=3$. Assume the theorem is true for all noncomplete connected chordal graphs on less than $n$ vertices and prove it for $G$.

Since $G$ is not a complete graph, there are two vertices, say $x$ and $y$, which are not adjacent. Hence vertex set $X-\{x, y\}$ is a separator. Choose any minimal separator from this set and denote it by $S$. By Theorem 3.2.1, $G_{S}$ is a clique.

Suppose deleting of $S$ from $G$ leaves two connected components, $G_{X_{1}}$ and $G_{X_{2}}$; let $G_{1}=G_{X_{1} \cup S}$ and $G_{2}=G_{X_{2} \cup S}$ be two derived subgraphs with respect to $S$, see Figure 3.2. Graphs $G_{1}$ and $G_{2}$ both are chordal as subgraphs of $G$.

Consider subgraph $G_{1}$. If it is a clique, then every vertex from $X_{1}$ being simplicial in $G_{1}$ is simplicial in $G$ because there are no edges between $X_{1}$ and $X_{2}$. Suppose $G_{1}$ is not a clique. It is connected because $G_{X_{1}}$ is connected and $G_{S}$ is a clique. It has $<n$ vertices because $X_{2} \neq \emptyset$. By the induction hypothesis, $G_{1}$ contains at least two simplicial vertices which are not adjacent. Since $G_{S}$ is a clique, both simplicial vertices cannot be in $S$. Therefore, one of them is in $X_{1}$. Again, since there are no edges between $X_{1}$ and $X_{2}$, the simplicial vertex from $X_{1}$ is a simplicial vertex in $G$.

Consider subgraph $G_{2}$ and apply the same reasoning. We obtain that in $G$ there are two simplicial vertices which are not adjacent.

If deletion of $S$ from $G$ leaves $k \geq 3$ connected components, apply the same reasoning to each component; evidently, in such case $G$ will contain $k$ simplicial vertices which are pairwise not adjacent. $\square$

Observe that the statement of Dirac theorem may be extended to any complete graph $K_{n}, n \geq 2$, where all vertices are simplicial, with the exception that all they are pairwise adjacent.

Corollary 3.2.1 Every nontrivial tree contains two pendant vertices.
Proof. Any tree being a chordal graph by Theorem 3.2.2 must have two simplicial vertices which in this case are pendant. $\square$

Let $G_{1}=(X, E)$ be a chordal graph; it contains a simplicial vertex, denote it by $x_{1}$. Delete $x_{1}$ from $G_{1}$ and denote the graph obtained by $G_{2}$. Graph $G_{2}$ is a subgraph of $G_{1}$ and therefore is chordal. It contains a simplicial vertex, denote it by $x_{2}$. Delete $x_{2}$ from $G_{2}$, obtain another chordal graph $G_{3}$, which has a simplicial vertex $x_{3}$; delete it and continue this procedure on. At every step we obtain a chordal graph and apply Theorem 3.2.2. The last step in this procedure will occur when we delete the last vertex $x_{n}$ and arrive to $G_{n+1}=\emptyset$. We obtain the ordering of vertices $x_{1}, x_{2}, \ldots, x_{n}$. Denote it by $\boldsymbol{\sigma}$, so $\boldsymbol{\sigma}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$. The ordering $\sigma$ is called a simplicial elimination ordering or a perfect elimination ordering. The procedure of deleting the vertices in ordering $\sigma$ is called the simplicial decomposition. Its main feature is that every vertex $x_{i}$ is a simplicial vertex in graph $G_{i}$ induced by vertices $x_{i}, x_{i+1}, \ldots, x_{n}$ and $G_{i+1}=G_{i}-x_{i}, i=1,2, \ldots, n$.

It follows from the observations above that any chordal graph has an ordering $\sigma$, or, equivalently, a simplicial decomposition. But if a graph has a simplicial elimination ordering, is it chordal then? Suppose it is not; then it contains an induced $C_{k}, k \geq 4$. If a simplicial decomposition exists, then sooner or later, the first vertex of $C_{k}$ must appear in it. However, no vertex of $C_{k}$ is simplicial in any induced subgraph, a contradiction.

Summarizing the observations above, we arrive to the following conclusion:
Theorem 3.2.3 (Simplicial decomposition theorem) A graph $G$ is chordal if and only if it has a simplicial elimination ordering.

Figure 3.3 shows graph $G_{1}$ and its simplicial elimination ordering. Respectively, one can construct a sequence of graphs $G_{2}, G_{3}, \ldots, G_{8}, G_{9}=\emptyset$ by sequential deletion of simplicial vertices in order $1,2,3, \ldots, 8$, so $\boldsymbol{\sigma}=(1,2,3,4,5,6,7,8)$. Observe that there are only two simplicial vertices in $G_{1}$ : 1 and 2. However, each of the remaining vertices becomes simplicial at some step.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-070.jpg?height=316&width=935&top_left_y=1421&top_left_x=362)
Figure 3.3. $G_{1}$ and simplicial elimination ordering $\boldsymbol{\sigma}=(1,2,3,4,5,6,7,8)$.

The power of simplicial elimination ordering is that in determining if a graph is chordal, it is not necessary to investigate all subsets of sizes 4, 5, 6, ..., and check if every subset does not induce $C_{k}$; instead, it is sufficient to find at least one simplicial elimination ordering or show that none exist. In other words, searching for a simplicial elimination ordering replaces an exhaustive search for recognition of chordal graphs.

For example, consider graph $G_{1}$, see Figure 3.3. If we use only the definition of chordal graph, then we have to check $\binom{8}{4}$ subsets of size 4 for the case if any induces $C_{4}$. Then repeat the procedure for $C_{5}$, it would give us $\binom{8}{5}$ subsets. Then we would have to consider $\binom{8}{6}$ subsets for $C_{6},\binom{8}{7}$ subsets for $C_{8}$ and $\binom{8}{8}$ subsets for $C_{8}$. Visualization of $G$ could save
some steps but only in such small examples. However, using the last theorems, instead of that long procedure, we just look for the simplicial elimination ordering.

Non-chordal graphs may have simplicial vertices but if we start simplicial decomposition, sooner or later we get stuck because in obtained graph no vertex is simplicial. In Figure 3.1, graph $G_{2}$ is not chordal and simplicial decomposition gets stuck after removing of the unique simplicial vertex.

Theorem 3.2.4 In a chordal graph, any vertex may be the last vertex in some simplicial elimination ordering.

Proof. Indeed, let $G$ be a chordal graph and $x$ be any vertex. Since $G$ has at least two simplicial vertices at any step of simplicial decomposition, we can avoid deleting $x$ at every step, except the last one. $\square$

For example, in Figure 3.3 vertex 1 being the first in ordering $\sigma$ will be the last in ordering $\sigma^{\prime}=(2,3,8,7,6,5,4,1)$.

In a chordal graph, if any vertex $z$ may terminate some $\sigma$, then any vertex $y$ adjacent to $z$ may be the last but one. Then any vertex $x$ forming a triangle with $z$ and $y$ may be the third from the end. If we develop this procedure further, then if graph is chordal, we could reconstruct an ordering inverse to simplicial elimination ordering. The main point is that we can start at any vertex. This idea is at the base of the most efficient algorithm for recognizing chordal graphs, the so called "Maximum Cardinality Search".

Theorem 3.2.5 If $x$ is a simplicial vertex in a graph $G=(X, E)$, then there exists a maximum independent set $S \subseteq X$ such that $x \in S$.

Proof. Since $x$ is simplicial, every maximum independent set $S^{\prime}$ contains precisely one vertex from set $\{x\} \cup N(x)$ because otherwise the set $S^{\prime} \cup\{x\}$ would be independent and have greater cardinality. If there is a vertex $y \in N(x)$ such that $y \in S^{\prime}$, then we replace it by $x$ and put $S=S^{\prime} \backslash\{y\} \cup\{x\}$. $\square$

Notice that the theorem above holds for any graph, not necessarily chordal. However, the existence of a simplicial elimination ordering allows to suggest a simple algorithm for finding the independence number and the respective maximum stable set of a chordal graph:

## Algorithm 3.2.1 (Finding maximum stable set of a chordal graph)

INPUT: A chordal graph $G=(X, E)$
OUTPUT: A maximum independent set $S \subseteq X$ with $|S|=\alpha(G)$

1. Set $S=\emptyset$.
2. Find a simplicial vertex $x$, delete strongly $\{x\} \cup N(x)$ and include $x$ in $S$;
3. If at least one vertex remains, repeat step 2.
4. End.

If we run the algorithm for graph $G$ shown in Figure 3.3, then on the first step, vertex 1 is included in $S$, and set $\{1,4,5\}$ is strongly deleted; on the second step, vertex 2 is included in $S$, and set $\{2,3,8\}$ is strongly deleted; at last, on the third step, vertex 6 is included in $S$, and vertices 6 and 7 are deleted. There are no more vertices left; we end and conclude that one of the maximum stable sets of graph $G$ is $S=\{1,2,6\}$, and $\alpha(G)=3$. Respectively, vertices $\{3,4,5,7,8\}$ form a minimum transversal and $\tau(G)=5$. Depending on the simplicial vertices chosen at each step, there are other maximum stable sets and minimum transversals. Notice that Algorithm 3.2.1 also works for graphs which are not chordal.

Further, observe that deleted sets induce cliques; one can prove that they form a minimum number of cliques that cover $X$, namely: the cliques induced by $\{1,4,5\},\{2,3,8\}$ and \{6,7\} have the property that each vertex of $G$ belongs to one of them, and the number of such cliques is the minimum.

In general, the clique cover number $\theta(G)$ of a graph $G$ is the minimum number of cliques in graph $G$ such that each vertex belongs to precisely one clique. We say that the cliques cover the vertex set of $G$. As we will see, clique coverings play an important role in graph theory. So, for the graph in Figure 3.3, $\theta(G)=3$.

Exercises 3.2.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-072.jpg?height=437&width=1121&top_left_y=1156&top_left_x=321)
Figure 3.4.

1. In each of the graphs in Figure 3.4 determine which vertices are simplicial and which are not.
2. For each of the graphs in Figure 3.4 determine if it is chordal or not.
3. Which of the graphs in Figure 3.4 has a minimal separator which is not a clique?
4. For chordal graphs in Figure 3.4, find all simplicial elimination orderings.
5. In each chordal graph shown in Figure 3.4, choose a vertex at random and find a simplicial elimination ordering in which the vertex is the last.
6. Run Algorithm 3.2.1 for each of the graphs in Figure 3.4.
7. For each of the graphs in Figure 3.4 find the minimum clique cover; compare the number of cliques with the independence number.

8. What is the minimum number of edges to be added to the cube (prism, $W_{n}$, Petersen graph) to make it chordal?
9. What is the minimum number of edges to be deleted from the cube (prism, $W_{n}$, Petersen graph) to make it chordal?

Computer Projects 3.2. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$ and a vertex $x$, determine if $x$ is a simplicial vertex.
2. Given a graph $G$, find out if it contains simplicial vertices.
3. Given a graph $G$, recognize if it is chordal.
4. Given a chordal graph $G$, find the maximum independence number and minimum clique cover.

### 3.3. Degrees

Degree of a vertex is the number of its neighbors; it is a very general term defined for all graphs. The vertices of minimum degree play an important role in many optimization problems. Sometimes one investigate the maximum possible value of minimum degree over all subgraphs in a given graph. When we say "the degree of a vertex in a subgraph" we mean the number of its neighbors in the subgraph only.

It appears that chordal graphs have a special place if we investigate the degrees. For a graph $G=(X, E)$, let us define the following parameter, known as Szekeres-Wilf number:

$$
M(G)=\max _{X^{\prime} \subseteq X} \min _{x \in G^{\prime}} d(x) .
$$

As it follows from the definition, to find $M(G)$ one need to consider all induced subgraphs $G^{\prime}$ of the graph $G$, count the minimum degree in each of them and find the maximum value over all of them. However, there is a simple procedure for finding $M(G)$. It consists in decomposition of $G$ by sequential elimination of vertices of minimum degree; maximum value $t$ over all these minimums coincides with $M(G)$.

Indeed, on one hand, $M(G)$ cannot be less than $t$ since $t$ is the minimum degree in just one subgraph from the sequence of graphs. On the other hand, if $M(G)>t$, then there is an induced subgraph $G^{\prime} \subseteq G$ which has minimum degree greater than $t$. But in the decomposition by minimum degrees, the first vertex of $G^{\prime}$ appears at some step $i$, see Figure 3.5; its degree cannot exceed $t$ by definition of $t$. So, we conclude $M(G)=t$.

Generally, notice that the degree of any vertex in subgraph $G^{\prime}$ cannot exceed the degree of the same vertex in $G_{i}$, and moreover in the original graph $G$.

Proposition 3.3.1 For any graph $G, M(G) \geq \omega(G)-1$.
Proof. Indeed, by definition, $\omega(G)$ is the maximum size (number of vertices) of a clique in $G$. Therefore, there is at least one induced complete subgraph of $G$ with minimum degree $\omega(G)-1$. Since $M(G)$ is the maximum of minimum degrees over all induced subgraphs, the inequality follows. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-074.jpg?height=206&width=602&top_left_y=204&top_left_x=581)
Figure 3.5.

As we see, the value $\boldsymbol{\omega}(G)-1$ in fact is the lower bound for $M(G)$ for all graphs. The next theorem shows that chordal graphs realize the absolute minimum for $M(G)$ :

Theorem 3.3.1 The following statements are equivalent:

1) $M\left(G^{\prime}\right)=\omega\left(G^{\prime}\right)-1$ for each induced subgraph $G^{\prime} \subseteq G$;
2) $G$ is chordal.

Proof. 1) ⇒ 2) Let $M\left(G^{\prime}\right)=\omega\left(G^{\prime}\right)-1$ for each induced subgraph $G^{\prime} \subseteq G$ and suppose $G$ is not chordal. Then $G$ contains an induced cycle $C_{k}$ of length $\geq 4$. But $M\left(C_{k}\right)=2=\omega\left(C_{k}\right)$, a contradiction.
2) ⇒ 1) Let $G$ be a chordal graph. Since every subgraph of a chordal graph is also chordal, without loss of generality, prove the equality for $G$. Note that $M(G) \geq \omega(G)-1$. As chordal graph, $G$ has a simplicial decomposition. Let the highest degree of a simplicial vertex in such decomposition be $t$. Then the size of maximum clique in $G$ is $\omega(G)=t+1$. The simplicial vertex of degree $t$ is not necessarily a vertex of minimum degree, therefore we have $M(G) \leq t=\omega(G)-1$. Hence $M(G)=\omega(G)-1$. $\square$

One can see in the conclusion that for chordal graphs, both simplicial decomposition and minimum degree decomposition give the same maximum value of degree equal to $\omega(G)-1$. In special case, when $G$ is a tree, both simplicial decomposition and minimum degree decomposition coincide. In general case, the situation is much less attractive. For example, for complete bipartite graph $K_{n, n}$ with $n \geq 2$, we obtain $M\left(K_{n, n}\right)=n, \omega\left(K_{n, n}\right)=2$, and evidently, there are no simplicial vertices.

Exercises 3.3.

1. For each of the graphs in Figure 3.6, find the value of $M(G)$ and compare with $\omega(G)-1$.
2. Determine which of the graphs in Figure 3.6 is chordal and which is not. For a non chordal graph, find a minimal induced subgraph $G^{\prime}$ such that $M\left(G^{\prime}\right)>\omega\left(G^{\prime}\right)-1$.
3. Determine $M\left(C_{n}\right), M\left(K_{n}\right), M\left(W_{n}\right)$, and the value of Szekeres-Wilf number of the cube, prism and Petersen graph.
4. Construct a graph $G$ with arbitrarily large difference
$$
M(G)-(\omega(G)-1) .
$$
5. Prove that for any $k$-regular graph $G, M(G)=k$.
6. Find the Szekeres-Wilf number for the complements of graphs from 3.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-075.jpg?height=439&width=1121&top_left_y=214&top_left_x=321)
Figure 3.6.

Computer Projects 3.3. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, find a vertex of minimum degree.
2. Given a graph $G$, find $M(G)$.
3. Given a graph $G$ and a subset of vertices; find the minimum vertex degree in the subgraph induced by the subset.

### 3.4. Distances in Chordal Graphs

Next theorem is a generalization of Theorem 2.2.1:
Theorem 3.4.1 If $G$ is a chordal graph, then for every vertex $x$, the set $N_{\infty}(x)$ of farthest vertices contains a vertex which is simplicial in $G$.

Proof. Without loss of generality, consider a connected nontrivial chordal graph $G=$ $(X, E)$. Prove the theorem by induction on $n$. The statement is evident for $n=2$. Assume it holds for all chordal graphs on $<n$ vertices, and $|X|=n$.

Let $N_{i}$ be the set of vertices at distance $i$ from $x$. We obtain the following partition of $X$ :

$$
X=N_{0} \cup N_{1} \cup N_{2} \cup \cdots \cup N_{k-1} \cup N_{k}
$$

where $N_{k}=N_{\infty}(x)$, see Figure 3.7.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-075.jpg?height=325&width=1133&top_left_y=1936&top_left_x=363)
Figure 3.7.

If $k=1$, then $N_{\infty}(x)=X-\{x\}$. Chordal graph $G-x$ has a simplicial vertex. Any simplicial vertex in $G-x$ is simplicial in $G$ because $x$ is adjacent to all other vertices. Therefore in this case, $N_{\infty}(x)$ has a vertex simplicial in $G$.

Let now $k \geq 2$. The set $N_{k-1}$ evidently is a separator in $G$. It contains a minimal separator, and subgraph $G_{N_{k}}$ has at least one connected component. Without loss of generality, suppose $N_{k-1}$ is a minimal separator and, moreover, $G_{N_{k}}$ has just one connected component.

By Theorem 3.2, $G_{N_{k-1}}$ is a clique. If $G_{N_{k-1} \cup N_{k}}$ is a clique, then every vertex from $N_{k}$ is simplicial in $G$. If $G_{N_{k-1} \cup N_{k}}$ is not a clique, then as chordal graph, it contains at least two simplicial vertices which are not adjacent. They both cannot be in $N_{k-1}$ because $N_{k-1}$ induces a clique. Hence at least one of them is in $N_{k}$. It remains to observe, see Figure 3.7, that every vertex $y \in N_{k}$ which is simplicial in $G_{N_{k-1} \cup N_{k}}$, is simplicial in $G$. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-076.jpg?height=404&width=911&top_left_y=761&top_left_x=370)
Figure 3.8.

Next corollary generalizes both Theorem 3.2.2 and Corollary 2.2.1.
Corollary 3.4.1 Any connected nontrivial chordal graph has at least two simplicial vertices.

Proof. Let $G=(X, E)$ be a connected nontrivial chordal graph. Consider vertices $x$ and $y$ such that $d(x, y)=\operatorname{diam}(G)$, see Figure 3.8. By Theorem 3.4.1, there is a vertex $y^{\prime} \in N_{\infty}(x)$ which is simplicial in $G$. Obviously, $d\left(x, y^{\prime}\right)=d(x, y)=\operatorname{diam}(G)$. By the same reason, for vertex $y^{\prime}$, there is a simplicial vertex $x^{\prime} \in N_{\infty}\left(y^{\prime}\right)$ such that $d\left(y^{\prime}, x^{\prime}\right)=d\left(y^{\prime}, x\right)=\operatorname{diam}(G)$. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-076.jpg?height=316&width=1010&top_left_y=1722&top_left_x=321)
Figure 3.9.

Next example (Figure 3.9) shows how it looks in a graph $G$. It is easy to see that $\operatorname{diam}(G)=4$. Let us start at vertex 2. So, $N_{0}=\{2\}$. Then $N_{1}(2)=\{1,12,10,3\}$. Next we find $N_{2}(2)=\{11,4,8,9\}$. At last, $N_{3}(2)=N_{\infty}(2)=\{5,6,7\}$. Observe that vertices 5 and 7 are simplicial.

We now run the same procedure starting at, say, 5. $N_{0}(5)=\{5\}, N_{1}(5)=\{4,6\}$, $N_{2}(5)=\{7,8,9,3\}, N_{3}(5)=\{2,10\}, N_{4}(5)=N_{\infty}(5)=\{1,12,11\}$. We find two simplicial vertices, 11 and 5 such that $d(11,5)=\operatorname{diam}(G)=4$. There are two diametral (11,5)-paths: 11-10-3-4-5 and 11-10-9-4-5.

Notice that simplicial decomposition of a chordal graph does not change any distance in graphs obtained at each step; this is true even if graph is not chordal but has simplicial vertices.

Last example shows that in chordal graphs, $N_{\infty}(x)$ may contain vertices which are not simplicial. In Figure 3.9, $N_{3}(2)=N_{\infty}(2)=\{5,6,7\}$ where vertex 6 is not simplicial. Therefore Theorem 2.2.2 cannot be generalized to chordal graphs. There are other methods for finding the center in chordal graphs.

## Exercises 3.4.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-077.jpg?height=480&width=1117&top_left_y=906&top_left_x=323)
Figure 3.10.

1. In chordal graph $G$, see Figure 3.10, for each vertex $x$, find $N_{\infty}(x)$ and a simplicial vertex in $N_{\infty}(x)$.
2. Find the diameter, radius and center of the graph in Figure 3.10.
3. In chordal graph $G$, see Figure 3.10, find a pair of simplicial vertices which are the ends of a diametral path.
4. In chordal graph $G$, see Figure 3.10, find a diametral path with both ends not being simplicial vertices.
5. For chordal graph $G$ in Figure 3.10, find a simplicial decomposition ordering; reconstruct $G$ in inverse ordering and track the change of the diameter, radius and center.

Computer Projects 3.4. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a chordal graph $G$ and a vertex $x$, find all simplicial vertices from $N_{\infty}(x)$.
2. Given a chordal graph $G$ find a simplicial decomposition ordering; reconstruct $G$ in inverse ordering and track the change of the diameter, radius and center.

3. Given a chordal graph $G$, find a diametral path.
4. Given a chordal graph $G$, find diameter, radius and center.

### 3.5. Quasi-triangulated Graphs

Not only chordal graphs have many interesting properties, but they serve as an important base for further generalizations in graph and hypergraph theory. This section represents an example of such generalization and its application to cyclic structure of graphs and their complements.

In a graph $G$, a vertex is called weakly cyclic if it belongs to no induced $C_{k}, k \geq 4$. Evidently, in any graph, simplicial vertices belong to no induced $C_{k}, k \geq 4$; so they are weakly cyclic. Not only simplicial vertices are weakly cyclic. In chordal graphs, all vertices are weakly cyclic. The concept of weakly cyclic vertex is more general than the concept of simplicial vertex.

A graph $G$ is called latticed if each vertex belongs to some induced $C_{k}, k \geq 4$ and some induced $\overline{C_{l}}, l \geq 4$. Latticed graphs are invariant with respect to taking the complement in the sense that both do not contain weakly cyclic vertices. One can think about latticed graphs as of graphs with all vertices being "strongly" cyclic. All cycles $C_{k}, k \geq 6$ are latticed: each vertex belongs to $C_{k}$ and $\overline{C_{4}}$, see Figure 3.11.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-078.jpg?height=433&width=534&top_left_y=1182&top_left_x=616)
Figure 3.11.

In a graph $G$, a vertex $x$ is called co-simplicial if it is simplicial in the complement $\bar{G}$. That means its non-neighbors form an independent set of vertices, or, equivalently, no edge entirely lies outside the neighborhood $N(x)$.

Definition 3.5.1 A graph $G$ is called quasi-triangulated if it has a decomposition by sequential elimination of vertices that at each step, are simplicial or co-simplicial.

Quasi-triangulated graphs are invariant when taking the complement: if $G$ is quasitriangulated, then its complement $\bar{G}$ is also quasi-triangulated.

For example, $C_{4}$ is a quasi-triangulated graph: every vertex is co-simplicial; when we delete any vertex, the remaining graph is chordal. Graph $\overline{C_{4}}$ is chordal, with all vertices weakly cyclic.

Cycle $C_{5}$ is not quasi-triangulated because it has no simplicial or co-simplicial vertices. Moreover, it is latticed because evidently, $C_{5}$ and $\overline{C_{5}}$ are isomorphic.

Consider all graphs that can be decomposed by sequential elimination of vertices which at each step are weakly cyclic in graph or its complement. How they are related to quasitriangulated graphs? Surprisingly, these two classes of graphs coincide. To prove this, we need the following

Lemma 3.5.1 If $G$ is a graph and $x$ is a vertex that belongs to no induced $C_{k}, k \geq 4$, then every minimal separator $S$ in the neighborhood $N(x)$ is a clique.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-079.jpg?height=419&width=948&top_left_y=691&top_left_x=453)
Figure 3.12.

Proof. Let $G$ be a graph and $x$ be a vertex that belongs to no induced $C_{k}, k \geq 4$. Let $Y$ induce a component of $G-S$ that does not contain $x$, see Figure 3.12. Choose any two vertices $y, z \in S$. Since $S$ is a minimal separator, each of $y$ and $z$ has a neighbor in $Y$. Since $Y$ induces a connected component, there is a shortest path of length at least two joining $y$ to $z$ through $Y$. This path together with $x$ forms an induced $C_{k}, k \geq 4$, a contradiction to our assumption on $x$. Therefore, $y$ and $z$ must be adjacent, i.e. $S$ induces a clique. $\square$

Theorem 3.5.1 (Characterization theorem, Gorgos, 1984) For any graph $G$ the following statements are equivalent:

(i) $G$ is quasi-triangulated.
(ii) $G$ can be decomposed by sequential elimination of weakly cyclic vertices in graph or its complement.
(iii) $G$ does not contain latticed subgraphs.

Proof. If $G$ is quasi-triangulated, then it can be decomposed by sequential elimination of weakly cyclic vertices in graph or its complement because every simplicial vertex is weakly cyclic in graph and every co-simplicial vertex is weakly cyclic in the complement. In turn, if $G$ can be decomposed by sequential elimination of weakly cyclic vertices in graph or its complement, then it does not contain latticed subgraphs because they are not decomposable by definition. So, (i) implies (ii), and (ii) implies (iii). Therefore, we only need to prove that (iii) implies (i).

We prove (iii)⇒(i) by induction on the number of vertices $n(G)$. Let $G=(X, E)$ be a graph satisfying (iii). If $G$ contains a simplicial or co-simplicial vertex, then we delete it, the obtained graph has $<n$ vertices, we use the induction hypothesis and prove the implication. Therefore, assume $G$ contains no simplicial vertex and no co-simplicial vertex. The proof is split into the following steps.

Step 1. Proof that $G$ is a connected graph. Suppose $G$ is disconnected. If at least one connected component is a chordal graph, then it has a simplicial vertex what was already excluded. If no one component is chordal, then each contains an induced $C_{k}, k \geq 4$. Choose any two of them as induced subgraphs, say, $C_{k}, k \geq 4$ and $C_{l}, l \geq 4$. Considered together they form a latticed subgraph because each vertex belongs to some cycle ( $C_{k}, k \geq 4$ or $C_{l}, l \geq 4$ ) and to the complement of $C_{4}$, see Figure 3.13. Therefore, $G$ is a connected graph.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-080.jpg?height=505&width=1093&top_left_y=761&top_left_x=337)
Figure 3.13.

Step 2. Finding subgraph $G^{\prime}$ and vertex $y$. Since $G$ is not a latticed graph, one of $G$ or $\bar{G}$ contains a weakly cyclic vertex. Without loss of generality, suppose $G$ contains a weakly cyclic vertex. Denote the set of all weakly cyclic vertices by $X^{\prime}$. Hence, $X^{\prime} \neq \emptyset$.

Let $G^{\prime}=G-X^{\prime}$. Subgraph $G^{\prime}$ has at least one vertex, because otherwise $X^{\prime}=X$, all vertices of $G$ are weakly cyclic, i.e. $G$ is chordal and contains a simplicial vertex.

Since $X^{\prime} \neq \emptyset$ we conclude that $n\left(G^{\prime}\right)<n(G)$. Evidently, $G^{\prime}$ does not contain latticed subgraphs. By the induction hypothesis, $G^{\prime}$ contains a simplicial or co-simplicial vertex; denote it by $y$.

Since every vertex of $G^{\prime}$ lies in some $C_{k}, k \geq 4, y$ is co-simplicial. We will prove that $y$ is adjacent to all vertices of $X^{\prime}$ : this will imply $y$ is co-simplicial in the initial graph $G$, a contradiction.

Step 3. Proof that $y$ is co-simplicial in $G$. Let $x$ be any vertex in $X^{\prime}$. Since $G$ is connected and $x$ is not co-simplicial, there is a nonempty set $S$ of vertices in $N(x)$ that is a minimal separator of $G$, see Figure 3.14 ( $x$ is not shown). By Lemma 3.5.1, $S$ is a clique. Let $G_{1}, G_{2}$ be induced subgraphs of $G$ such that $G=G_{1} \cup G_{2}, G_{1} \cap G_{2}=S$, and there is no edge between $G_{1}-S$ and $G_{2}-S$. If at least one of $G_{1}$ or $G_{2}$ is chordal, then there is a simplicial vertex in $G_{1}-S$, or $G_{2}-S$, and thus it is a simplicial vertex in $G$, a contradiction.

Therefore, $G_{1}$ contains a $C_{k}, k \geq 4$ and $G_{2}$ contains a $C_{l}, l \geq 4$. Since $S$ is a clique, one edge, say $e_{1}$, of the first cycle lies completely in $G_{1}-S$. Similarly, there is an edge, say $e_{2}$, of the second cycle that lies completely in $G_{2}-S$. All endpoints of $e_{1}, e_{2}$ are in $G^{\prime}$. Since $y$ is co-simplicial in $G^{\prime}$, all of its non-neighbors from $G^{\prime}$ are pairwise disjoint. If $y$ lies in

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-081.jpg?height=513&width=1150&top_left_y=309&top_left_x=332)
Figure 3.14.

$G_{1}-S$, then both ends of $e_{2}$ are adjacent non-neighbors. If $y$ lies in $G_{2}-S$, then both ends of $e_{1}$ are adjacent non-neighbors. Therefore, the only possibility for $y$ is to be in $S$. But $S \subseteq N(x)$, and we obtain that $y$ is adjacent to vertex $x$. Since $x$ was chosen arbitrary from $X^{\prime}, y$ is adjacent to all vertices from $X^{\prime}$ and therefore is co-simplicial for the entire graph $G$. This final contradiction proves the theorem. $\square$

Exercises 3.5.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-081.jpg?height=437&width=1079&top_left_y=1358&top_left_x=363)
Figure 3.15.

1. Which of the graphs in Figure 3.15 is quasi-triangulated and which is not?
2. In a graph which is not quasi-triangulated in Figure 3.15, find a latticed subgraph.
3. Construct a quasi-triangulated graph having only one vertex which is simplicial or cosimplicial.
4. For each of graphs $G_{1}, G_{2}$, and $G_{3}$ in Figure 3.15, find a minimum clique cover and a maximum independent set.

5. Which of the graphs $C_{n}, K_{n}, W_{n}, n \geq 3$, cube, prism and Petersen graph is quasi-triangulated and which is not?

Computer Projects 3.5. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, recognize if it is quasi-triangulated.
2. Given a graph $G$, recognize if $\bar{G}$ is quasi-triangulated.
3. Given a quasi-triangulated graph $G$, find a maximum independent set and a minimum clique cover.
4. Given a quasi-triangulated graph $G$, find a maximum independent set and a minimum clique cover of the complement $\bar{G}$.

## Chapter 4

## Planar Graphs

"Planarity is the cause of car collisions..."

### 4.1. Plane and Planar Graphs

Omitting some topological details we say that a continuous curve in the plane which connects two points (called the first and the last) and has no intersection with itself is called a Jordan curve. A Jordan curve is closed if the first and the last points coincide. We will use the following

Theorem 4.1.1 (Jordan Curve Theorem) A closed Jordan curve L partitions the plane into precisely two regions, bounded and unbounded, each having $L$ as boundary.

It is clear that the unbounded region contains the infinite point. A region is connected in the sense that any pair of its points can be connected by a Jordan curve which lies inside the region. In drawing graphs, the vertices are represented by points in the plane, and the edges are represented by Jordan curves connecting the respective points. Evidently, a segment of a straight line is the simplest case of a Jordan curve. If two Jordan curves intersect at a point different from the first and the last for each of them, then we say that the respective edges cross (intersect), or, alternatively, we have an edge-intersection or crossing.

A planar graph is a graph that can be drawn in the plane without crossings of the edges. If a planar graph is drawn in the plane without intersections, then such drawing is called a plane graph.

Sometimes a plane graph is called plane embedding of a planar graph. Plane graph divides the plane into connected regions called faces. So each face is bounded by some cycle. The number of vertices of such cycle is called the size of the face. For a plane graph $G$, we will denote the number of faces by $f(G)$ or simply by $f$.

Any planar graph may have several plane embeddings. Figure 4.1 shows three drawings of the same graph $K_{4}$; only the first two of them are plane graphs. One can see that in the first drawing, face $f_{1}$ is bounded by the cycle 1-2-4-1, while in the second by the cycle 1-2-3-1 and so on. The number of faces in both embeddings is 4; there is always one face which is not bounded. It is called the unbounded face. The unbounded face in both embeddings of $K_{4}$ is denoted by $f_{4}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-084.jpg?height=451&width=1180&top_left_y=225&top_left_x=317)
Figure 4.1. Three different pictures of $K_{4}$ : only the first two are plane graphs.

Having the third drawing of $K_{4}$ with one crossing, we could re-draw it to obtain one of the first two plane embeddings. However, it is not possible to do that for every graph. Generally, graphs may have different plane embeddings with different number of crossings. The minimum number of crossings over all possible drawings is called the crossing number of a graph. Clearly, for planar graphs the crossing number is 0.

Exercises 4.1.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-084.jpg?height=441&width=1075&top_left_y=1273&top_left_x=321)
Figure 4.2.

1. For each of the graphs $G_{1}$ and $G_{2}$ in Figure 4.2, find the number of crossings. Are $G_{1}$ and $G_{2}$ plane graphs?
2. For each of the graphs $G_{1}$ and $G_{2}$ in Figure 4.2, find a plane embedding, denote the faces and find the size of each face; find the cycle which forms the unbounded face.
3. Are $G_{1}$ and $G_{2}$ planar graphs?
4. Connect the two lower vertices in graph $G_{1}$ (Figure 4.2) by an edge and, if possible, find a plane embedding of the obtained graph.
5. Connect the two upper vertices in graph $G_{2}$ (Figure 4.2) by an edge and, if possible, find a plane embedding of the obtained graph.

6. Find at least two different plane embeddings of the prism, cube, $K_{2,3}$ and $W_{n}(n \geq 4)$.
7. Find a drawing of the Petersen graph with the smallest number of edge-intersections.

Computer Projects 4.1. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a drawing of a graph in the plane (vertices = points, edges = straight line segments) find out if it is a plane graph.
2. Given a drawing of a graph in the plane (vertices = points, edges = arc segments) find out if it is a plane graph.
3. Given a drawing of a graph in the plane (vertices = points, edges = straight line segments) find the number of edge-intersections.

### 4.2 Euler's Formula

Theorem 4.2.1 (Euler, 1750) If $G$ is a connected plane graph with $n$ vertices, $m$ edges and f faces, then

$$
n-m+f=2 .
$$

Proof. Let $T$ be a spanning tree of $G$. Evidently, $m(T)=n-1, f(T)=1$, so $n(T)-$ $m(T)+f(T)=n-(n-1)+1=2$, and the formula holds for $T$.

Now add sequentially the remaining edges of $G$ to $T$ : each such adding increases the number of edges and the number of faces by 1 . Since in the formula $m$ and $f$ are of the opposite signs, the equality holds for $G$ itself. $\square$

Corollary 4.2.1 If a graph $G$ is planar, then all of its plane embeddings have the same number of faces equal to $m-n+2$.

Proof. Indeed, since $n(G)$ and $m(G)$ are constant, Euler's formula implies that $f(G)=$ $m-n+2$. $\square$

Corollary 4.2.2 If $G$ is a connected planar graph without parallel edges, then

$$
m(G) \leq 3 n(G)-6 .
$$

Proof. Consider a plane embedding of $G$. Since there are no parallel edges, the size of each face is at least 3. Count the edges around each face. The minimum number that we can obtain is $3 f$. In fact, each edge is counted twice, so we obtain $2 m$. Therefore, $3 f \leq 2 m$. From Euler's formula, $f=2-n+m$. Hence, $3(2-n+m) \leq 2 m$ what gives $m \leq 3 n-6$. $\square$

Corollary 4.2.3 Every connected planar graph without parallel edges contains a vertex of degree at most 5.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-086.jpg?height=505&width=803&top_left_y=205&top_left_x=482)
Figure 4.3. Stereographic projection.

Proof. If the graph contains at most 6 vertices, then every vertex has degree at most 5 . Therefore, it remains to consider the case when the graph has at least 7 vertices. Suppose each vertex has degree at least 6. Counting edges around each vertex results in $6 n \leq 2 m$, or, equivalently, $3 n \leq m$. Combining this inequality with Corollary 4.2.2 we obtain the following: $3 n \leq m \leq 3 n-6$, which leads to contradiction $0 \leq-6$. $\square$

For any plane graph $G$ and every its bounded face $f$, there exists such a plane embedding of $G$ that face $f$ becomes unbounded. This can be shown using the so called stereographic projection.

Suppose we have a plane embedding of $G$. Put a sphere tangent to the plane and map the plane onto the sphere "to the north pole" as shown in Figure 4.3. In this way we obtain an image of $G$ on the surface of the sphere. We now rotate the sphere in such a way that the desired face contains the north pole. From the new north pole, we then project the sphere back onto the plane. A new plane embedding of $G$ is obtained; the face that was bounded in the first embedding, becomes unbounded in this new plane embedding. Therefore, the following proposition holds.

Proposition 4.2.1 A graph can be drawn on the sphere without intersections of edges if and only if it is planar.

The statement above leads to the following observation about polyhedra (3-dimensional figures bounded by intersections of planes):

Corollary 4.2.4 If a convex polyhedron has $n$ vertices, $m$ edges and $f$ faces, then $n-m+$ $f=2$.

Proof. Indeed, having such a polyhedron, place it into a sphere and project it out onto that sphere. The vertices and edges of the polyhedron form an embedding of a graph on the sphere. We then use stereographic projection to project it onto the plane and obtain a plane embedding of the respective graph. The vertices, edges and faces of such embedding correspond to the vertices, edges and faces of the initial polyhedron. $\square$

For example, consider the cube: $n=8, m=12, f=6$ and evidently, the formula holds.

Exercises 4.2.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-087.jpg?height=332&width=1022&top_left_y=445&top_left_x=371)
Figure 4.4.

1. Draw a plane embedding of the prism, cube, $K_{2,3}$, each of the graphs in Figure 4.2 and verify the Euler's formula.
2. For each of the drawings in 1., check the inequality of Corollary 4.2.2.
3. Using the stereographic projection, show how to obtain from each other all three embeddings of the same graph in Figure 4.4.
4. Check the inequality of Corollary 4.2.2 for prism, cube, $K_{n}, W_{n}, K_{m, n}(m \geq 1, n \geq 3)$, and the Petersen graph.
5. Draw a plane graph on 6 vertices with all the vertices belonging to the unbounded face; redraw it in such a way that all the vertices belong to a bounded face.

Computer Projects 4.2. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a plane graph $G$ and a face $f$, construct a plane embedding of $G$ with $f$ being the unbounded face.
2. Given a planar graph $G$ and its drawing in the plane having one crossing. Construct a plane embedding of $G$.
3. Given a planar graph $G$, a vertex $x$ and a plane embedding of $G-x$. Construct a plane embedding of $G$.

## 4.3. $K_{5}$ and $K_{3,3}$ Are not Planar Graphs

Theorem 4.3.1 $K_{5}$ and $K_{3,3}$ are not planar graphs.
Proof. Suppose $K_{5}$ is planar. Let us try to draw it in the plane, see Figure 4.5. Since it has cycle 1-2-3, any plane drawing must have this cycle. The cycle partitions the plane into two faces. Vertex 4 may be embedded inside or outside of this cycle. In both cases, since it

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-088.jpg?height=1543&width=1245&top_left_y=233&top_left_x=241)
Figure 4.5. $K_{5}$ and $K_{3,3}$ are not planar.

is adjacent to vertices 1, 2, and 3, the inside or outside face is split into three faces of size 3 each. So, all the faces in the plane have size 3. It remains to find the face for vertex 5. However, since vertex 5 has degree 4, there is no face for it (see Figure 4.5).

If we take vertex 5 instead of 4, and embed it inside or outside of the cycle 1-2-3, we will not be able to find a face for vertex 4. All cases are exhausted; it implies that $K_{5}$ cannot be drawn in the plane without crossings of the edges, i.e., it is not planar.

Now suppose $K_{3,3}$ is planar, and vertex set $X=\{1,2,3,4,5,6\}$. Since $K_{3,3}$ is bipartite, without loss of generality assume that vertices 1, 2, and 3 form the first part, and vertices 4, 5, and 6 form the second part, see Figure 4.5.

Let us try to draw $K_{3,3}$ without crossings in the plane. Since it has cycle 1-4-2-5, any plane drawing must have this cycle, so start with it. The plane is now partitioned into two faces. Vertex 3 may be drawn in inside or outside face. Since it is adjacent to vertices 4 and 5, each case leads to three faces of size 4 each. Suppose we draw vertex 3 in inside face. So, there are three faces to draw vertex 6 which must be adjacent to 1, 2, and 3. If we place it in face 1-4-3-5, then it cannot be connected with 2. If we place it in face 2-4-3-5, then it cannot be connected with 1. If we place it in outer face 1-4-2-5, then it cannot be connected with vertex 3 . So, there is no face to place vertex 6 . The case when vertex 3 is drawn in outside face is considered similarly.

If, instead of vertex 3 we proceed with vertex 6 and embed it inside or outside the cycle 1-2-4-5, by similar reasoning we arrive to the conclusion that there is no face for vertex 3.

All possible cases are considered; it implies that $K_{3,3}$ cannot be drawn in the plane without crossings of the edges, i.e., it is not planar as well. $\square$

Exercises 4.3.

1. Find the values of $k$ for which $K_{5}$ and $K_{3,3}$ are $k$-connected.
2. Using graph $K_{3,3}$ disprove the following statement: let $G$ be a graph and $S$ be a minimal separator having at least three vertices with derived subgraphs $G_{1}$ and $G_{2}$. Then $G$ is planar if and only if both $G_{1}$ and $G_{2}$ are planar.
3. Given a graph $G$ and a 2-vertex separator $K_{2}$ producing planar derived subgraphs $G_{1}$ and $G_{2}$. Using plane embeddings of $G_{1}$ and $G_{2}$, construct a plane embedding of $G$.
4. Check the inequality of Corollary 4.2.2 for both $K_{5}$ and $K_{3,3}$.
5. Prove that any graph $G$ containing $K_{5}$ or $K_{3,3}$ as any subgraph (induced or not) is not planar.
6. Find the crossing number of $K_{5}$ and $K_{3,3}$.

Computer Projects 4.3. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a 4-regular graph $G$, determine if it contains $K_{5}$ as a subgraph.
2. Given a 3-regular graph $G$, determine if it contains $K_{3,3}$ as a subgraph.

### 4.4. Kuratowski's Theorem and Planarity Testing

If a graph is planar, then every its subgraph is evidently planar. If a graph contains a nonplanar subgraph, then the graph itself is not planar. Theorem 4.3.1 implies that any graph containing $K_{5}$ or $K_{3,3}$ as subgraphs is not planar. But if a graph is not planar, does it contain $K_{5}$ or $K_{3,3}$ as subgraphs? The answer is that it may not contain $K_{5}$ or $K_{3,3}$ as subgraphs, but it must contain subgraphs closely related to $K_{5}$ or $K_{3,3}$.

Let us define two graphs $G_{1}$ and $G_{2}$ to be homeomorphic if both can be obtained from some graph $G_{3}$ by replacing some edges with some paths. In other words, we simply draw
("put") additional vertices on some edges of $G_{3}$. It is clear that any such replacing does not change the planarity of $G_{3}$ : if $G_{3}$ is planar, then both $G_{1}$ and $G_{2}$ are planar and vice versa. For example, any two cycles $C_{k}$ and $C_{l}$, with $k, l \geq 3$ are homeomorphic because they both can be obtained from $C_{3}$ by such replacing. Observe that any graph homeomorphic to $K_{5}$ or $K_{3,3}$ is not planar even if it does not contain $K_{5}$ and $K_{3,3}$ as subgraphs of any type.

The next theorem is one of the fundamental theorems in graph theory. It shows that graphs that are homeomorphic to $K_{5}$ and $K_{3,3}$ represent the unique cause of non-planarity.

Theorem 4.4.1 (Kuratowski, 1930) A graph is planar if and only if it does not contain subgraphs homeomorphic to $K_{5}$ or $K_{3,3}$.

Proof. We omit the complete proof of this theorem because it is long and involves many additional results. It can be found in several extended texts, such as e.g. [3, 4, 5, 7]. The idea of the proof can be described using the following steps.

1. Observe that if a graph $G$ is planar, then for any edge of $G$, there exists an embedding such that the edge belongs to the unbounded face. This embedding can be found by the stereographic projection.
2. Suppose a graph $G$ contains a separator with two vertices, say $x, y$, such that the derived subgraphs are $G_{1}$ and $G_{2}$. Let $G_{i}^{\prime}=G_{i} \cup\{x, y\}$. Using step 1, one prove then that if $G$ is not planar, then at least one of $G_{1}^{\prime}, G_{2}^{\prime}$ is not planar.
3. The last implies that any minimal non-planar graph must be 3-connected. In other words, it is sufficient to consider further 3-connected graphs only.
4. At this point one use the lemma stating that any 3-connected graph on $\geq 5$ vertices contains an edge whose contraction does not change its 3-connectivity.
5. Next one prove the following lemma. In a graph $G$, contract an edge and obtain a graph $G^{\prime}$. The lemma states that if $G^{\prime}$ contains subgraphs homeomorphic to $K_{5}$ or $K_{3,3}$, then the initial graph $G$ also contains subgraphs homeomorphic to $K_{5}$ or $K_{3,3}$.
6. Final step: one prove that if $G$ is a 3-connected graph without subgraphs homeomorphic to $K_{5}$ or $K_{3,3}$, then it has a plane embedding. The proof is by induction on the number of vertices. In $G$, contract an edge (guaranteed by step 4) to obtain a graph $G^{\prime}$ which has less vertices. By step 4, it is 3-connected. By step 5, $G^{\prime}$ does not contain subgraphs homeomorphic to $K_{5}$ or $K_{3,3}$. Therefore, by the induction hypothesis, there exist a plane embedding of $G^{\prime}$. The final argument consists in considering a few possible cases how the initial graph $G$ can be reconstructed from $G^{\prime}$. In each of these cases one show that it is possible to construct a plane embedding of $G$ unless it contains subgraphs homeomorphic to $K_{5}$ or $K_{3,3}$. $\square$

Planarity testing algorithm. There are many algorithms for determining if a graph is planar. Surprisingly, they do not use search for subgraphs homeomorphic to $K_{5}$ or $K_{3,3}$. Next we informally describe the basic idea of such an algorithm.

Consider a graph $G$ and a subgraph $G^{\prime} \subseteq G$ (not necessarily induced). If we delete the vertices of $G^{\prime}$ from $G$, we obtain a number (may be 0) of connected components. A fragment of $G$ with respect to $G^{\prime}$ is one of the following:

1) an edge of $G$ which is not in $G^{\prime}$ but connects two vertices of $G^{\prime}$;
2) a connected component of $G-V\left(G^{\prime}\right)$ together with edges connecting it to $G^{\prime}$ (vertices of attachment from $G^{\prime}$ included).

Now, let $G^{\prime}$ be a plane graph (algorithm usually starts with a cycle). Find all fragments of $G$ with respect to $G^{\prime}$. For each fragment $A$, determine a set of faces $F(A)$ that contain all vertices of attachment. If $F(A)=\emptyset$ for some $A$, then $G$ is not planar. If $|F(A)|=1$ for some $A$, then select $A$ for the next step. If $|F(A)|>1$ for all $A$, then select any fragment $A$.

Next, chose any path connecting two vertices of attachment of the selected fragment $A$. Embed the path inside a face from $F(A)$. Call the resulting plane graph $G^{\prime}$ and repeat the procedure., i.e., find a new set of fragments, for each of them find all admissible faces, and so on. If we arrive to the initial graph $G$, then $G$ is planar. One can prove that the algorithm works correctly, i.e., if $G$ is planar, then it finds a plane embedding, otherwise it stops at some subgraph $G^{\prime} \neq G$.

## Exercises 4.4.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-091.jpg?height=437&width=1071&top_left_y=1232&top_left_x=321)
Figure 4.6.

1. For which values of $m \geq 1$ and $n \geq 3$, graphs $K_{n}, K_{m, n}, W_{n}$ are planar?
2. Count the number of crossings in each of the graphs in Figure 4.6.
3. Which of the graphs in Figure 4.6 is planar and which is not?
4. In Petersen graph, find a subgraph homeomorphic to $K_{3,3}$.
5. What is the minimum number of vertices (edges) that must be deleted from Petersen graph to make it planar?
6. Prove that replacing an edge by multiple edges does not change the planarity of a graph.

Computer Projects 4.4. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a plane graph $G$ and an edge, construct an embedding of $G$ with the edge being on the unbounded face.
2. Given a graph $G$, determine if it is homeomorphic to $K_{5}$.
3. Given a graph $G$, determine if it is homeomorphic to $K_{3,3}$.
4. Given a graph $G$ and $n \geq 4$, determine if $G$ is homeomorphic to $C_{n}$.
5. Given a graph $G$ and $n \geq 4$, determine if $G$ is homeomorphic to $K_{n}$.
6. Given a graph $G$ and $n \geq 4$, determine if $G$ is homeomorphic to $W_{n}$.
7. Given a graph $G$, determine if it is homeomorphic to a cube.
8. Given a graph $G$, determine if it is homeomorphic to a prism.
9. Given a graph $G$, determine if it is planar.

### 4.5. Plane Triangulations and Dual Graphs

Plane triangulations. A simple connected plane graph is called plane triangulation if every its face, including unbounded, represents a triangle (i.e. has size 3). A simple planar (plane) graph is called maximal planar (plane) graph if adding any new edge to it results in a non-planar graph.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-092.jpg?height=363&width=606&top_left_y=1343&top_left_x=581)
Figure 4.7. Plane triangulation.

One can prove that these two concepts are equivalent, namely a graph is a plane triangulation if and only if it is a maximal plane graph. It is easy to determine the number of edges in a plane triangulation:

Theorem 4.5.1 For any plane triangulation, $m=3 n-6$.
Proof. Indeed, if we count the edges around each face, we obtain the equality $3 f=2 m$. Substitution of $f$ from Euler's formula results in $m=3 n-6$. $\square$

Every plane graph is a spanning subgraph of some plane triangulation; the latter can be obtained by adding edges to a given plane graph. Plane triangulations are important because
sometimes it is sufficient to prove results for them to conclude that the results hold for all planar graphs.

An example of a graph $G$ which is a plane triangulation is shown in Figure 4.7. One can see that all faces including unbounded face are triangles. $G$ has $n=5$ vertices and $m=3 n-6=15-6=9$ edges. Thus any plane graph on five vertices is a subgraph of graph $G$.

Dual graphs. For any plane graph $G$ one can construct another plane graph denoted by $G^{*}$ and called the dual of $G$. The rules are the following:

1. In each face of $G$ choose a point which becomes a vertex of $G^{*}$.
2. For each edge of $G$ separating faces $f_{i}$ and $f_{j}$ construct an edge of $G^{*}$ connecting vertices $f_{i}$ and $f_{j}$.

An example of a graph $G$ and its dual $G^{*}$ is shown in Figure 4.8. The edges of $G$ are drawn by solid lines while the edges of $G^{*}$ are drawn by dashed curves. Since $G$ had two faces, $G^{*}$ has two vertices. Every edge of $G$ is crossed by the corresponding edge of $G^{*}$. As one can see, the dual to simple graph $G$ is not a simple graph, in particular, the separating edge of $G$ corresponds to a loop of $G^{*}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-093.jpg?height=531&width=927&top_left_y=1147&top_left_x=469)
Figure 4.8. Plane graph $G$ and its dual $G^{*}$.

It is evident that $n\left(G^{*}\right)=f, m\left(G^{*}\right)=m$ and $f\left(G^{*}\right)=n$. The last follows from the observation that all faces around each vertex in $G$ are consecutively connected by the edges of $G^{*}$ and thus produce a face of $G^{*}$.

Theorem 4.5.2 If $G$ is a plane connected graph, then $\left(G^{*}\right)^{*}$ is isomorphic to $G$.
Proof. Evidently, one can reconstruct graph $G$ from the plane embedding of $G^{*}$ using the same rules. $\square$

One can show however, that different embeddings of the same planar graph $G$ may have non-isomorphic duals.

Exercises 4.5.

1. In $K_{5}$, delete an edge, draw a plane embedding which is a triangulation and construct the dual.
2. In $K_{3,3}$, delete an edge, draw a plane embedding which is a triangulation and construct the dual.
3. Construct the dual to a prism.
4. Construct the dual to a cube.
5. Construct the dual to $W_{n}, n \geq 4$.

Computer Projects 4.5. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a plane graph $G$, draw $G^{*}$.
2. Given a plane graph, complete it to a triangulation.

## Chapter 5

## Graph Coloring

"Warnings: do not use in painting; do not give any preference to any of the colors..."

### 5.1. Preliminary

Coloring theory started with the problem of coloring the countries of a map in such a way that no two countries that have a common border receive the same color. If we denote the countries by points in the plane and connect each pair of points that correspond to countries with a common border by a curve, we obtain a planar graph. The celebrated Four Color Problem asks if every planar graph can be colored with 4 colors. It seems to have been mentioned for the first time in writing in an 1852 letter from A. De Morgan to W.R. Hamilton. Nobody thought at that time that it was the beginning of a new theory. The first "proof" was given by Kempe in 1879. It stood for more than 10 years until Heawood in 1890 found a mistake. Heawood proved that five colors are enough to color any map. The Four Color Problem became one of the most famous problems in discrete mathematics of the 20th century. Besides colorings it stimulated many other areas of graph theory.

Generally, coloring theory is the theory about conflicts: adjacent vertices in a graph always must have distinct colors, i.e. they are in a permanent conflict. If we have a "good" coloring, then we respect all the conflicts. If we have a "bad" coloring, then we have a pair of adjacent vertices colored with the same color. This looks like having a geographic map where some two countries having common border are colored with the same color. Graphs are used to depict "what is in conflict with what", and colors are used to denote the state of a vertex. So, more precisely, coloring theory is the theory of "partitioning the sets having internal unreconcilable conflicts" because we will only count "good" colorings.

In day by day life, perhaps the most common and simple application of coloring is in traffic lights. People who invented traffic lights did not even realize how smart they were: they were first to observe that it was not important what sign (stop, or drive) to put; it was only important that whatever they put should be in different states at any moment of time for two given streets which intersect. Of course, as in many practical applications of math, they borrowed "red" and "green" from maritime rules, added "yellow" for an intermediate state, and put that on the most visible position. But mathematical model only represents the coloring of graph $K_{2}$.

It may look surprising but in graph coloring it does not matter which color is "blue" or which is "red"; it only matters how many different colors are available. Instead of really coloring the vertices of a graph, we just label them by numbers $1,2, \ldots, \lambda$ where $\lambda$ is the number of available colors. In this sense, graph coloring is the most color-blind subject.

In the most general setting, a color of a vertex may be thought of as a "state of a point", or even more generally, a "statement about anything".

### 5.2 Definitions and Examples

Let $G=(X, E)$ be a simple graph and $\{1,2, \ldots, \lambda\}$ be the set of available colors. Any labeling of vertices of graph $G$ by the numbers from $\{1,2, \ldots, \lambda\}$ is called a coloring. Each vertex is assigned precisely one color.

Definition 5.2.1 A coloring is called proper if adjacent vertices have different colors.
Not every coloring is proper. In a proper coloring, vertices of the same color induce an independent set. If we change the color for at least one vertex, we obtain another coloring. It may be proper or not. The number of all proper colorings of a graph $G$ with at most $\lambda$ colors is denoted by $P(G, \lambda)$. We will see that $P(G, \lambda)$ is a polynomial in $\lambda$ and therefore we call it the chromatic polynomial. When we need to underline the number of available colors, we say that we consider a proper $\lambda$-coloring. Notice that the number of really used colors in a proper $\lambda$-coloring may be strictly less than $\lambda$; but it can never be greater than $\lambda$. Often, when we say just "coloring" we mean proper coloring. The minimum number of colors over all proper colorings is called the chromatic number of a graph $G$, denoted by $\chi(G)$. Evidently, the maximum number of colors that can be used in a proper $\lambda$-coloring is $\min \{n(G), \lambda\}$.

Since there are no colorings with less than $\chi(G)$ colors, $P(G, \lambda)=0$ for all integer values of $\lambda$ such that $1 \leq \lambda \leq \chi(G)-1$. Since any coloring with $\chi(G)$ colors is at the same time a proper $\lambda$-coloring for any $\lambda \geq \chi(G)$, we conclude that $P(G, \lambda) \geq 1$ for any integer $\lambda \geq \chi(G)$. Since $\lambda$ is the number of colors, in our discussions it is always an integer variable.

Consider an example. Let $G=(X, E)$ where $X=\{x, y, z\}$, and $E=\{\{x, y\}$, $\{y, z\}\}$, see Figure 5.1. There is no coloring with one color, so $\chi(G)>1$. On the other hand, it is easy to see a coloring with two colors, say 1-2-1, so $\chi(G)=2$. Suppose the set of available colors is $\{1,2,3\}$, consequently, $\lambda=3$. Having totally three colors and keeping in mind that $\chi(G)=2$, we obtain the following possibilities for the number $i$ of really used colors: $i=2$ and $i=3$. If we use only 2 colors, then we have to chose them from $\{1,2,3\}$. Thus we have the choices: colors 1,2 , colors 2,3 , and colors 1,3 . The total number of choices equals $\binom{\lambda}{i}=\binom{3}{2}=3$. For the first choice, the colorings are 1-2-1 and 2-1-2, see the first two colorings in Figure 5.1, column $i=2$. For the second choice, the colorings are 2-3-2 and 3-2-3. For the last choice, the colorings are 1-3-1 and 3-1-3. Notice that in this case the colorings come in pairs, and in each pair, we just permute the colors.

If $i=3$, we observe that any coloring will be proper because all the vertices are of different colors. To construct all colorings, fix color 1 for $x$ and obtain two colorings by permuting colors 2 and 3 on $y$ and $z$ : 1-2-3 and 1-3-2. Do the same for color 2: we have

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-097.jpg?height=624&width=1227&top_left_y=230&top_left_x=269)
Figure 5.1. Graph $G$ and 12 its proper 3-colorings: 6 strict 2-colorings and 6 strict 3-colorings.

colorings 2-1-3, 2-3-1. At last, for color 3 we obtain the colorings 3-1-2 and 3-2-1, see Figure 5.1.

Summarizing all the cases we arrive to the conclusion that $P(G, 3)=12$. What about $P(G, \lambda)$ for an arbitrary value of $\lambda$ ? Should we consider all possibilities by exhaustive search? And what about $P(G, \lambda)$ for any graph? Is there any formula? We will show that there are general procedures for computation of $P(G, \lambda)$ for an arbitrary graph $G$.

Before proceeding to the next section, let us consider one more concept. Let $G=(X, E)$ be a graph, and $i$ be the number of used colors. So, each of $i$ colors is in use. Such proper colorings are called the strict $i$-colorings. Each strict $i$-coloring partitions the vertex set $X$ into $i$ nonempty subsets, called cells where each cell is the set of vertices of the same color. Such partitions are called feasible and cells are called color classes. In other words, in a feasible partition of $X$ into $i$ cells, adjacent vertices belong to different cells and each cell is an independent subset of vertices. Notice that proper colorings and feasible partitions are different concepts: colorings are labelings of vertices, partitions are divisions of $X$ into nonempty subsets. However, they are closely related. They are even more close than it appears.

In contrast with $\lambda$ which has no upper limit, the number $i$ of really used colors satisfies the following inequality: $1 \leq i \leq n(G)$. Let $r_{i}(G)$ be the number of feasible partitions of $G$ into $i$ cells. The vector

$$
R(G)=\left(r_{1}, r_{2}, \ldots, r_{n}\right)
$$

is called the chromatic spectrum of $G$.
Since by definition $\chi(G)$ is the smallest number of colors in a proper coloring, the chromatic spectrum, in fact, always has the following form:

$$
R(G)=\left(0,0, \ldots, 0, r_{\chi}, r_{\chi+1}, \ldots, r_{n}\right) .
$$

In our example, see Figure 5.1, when $i=2$, we have six proper colorings. Each of these colorings is a proper 3-coloring and simultaneously, a strict 2-coloring. For all cases, there is only one feasible partition of $X: X_{1}=\{x, z\}$ (first cell) and $X_{2}=\{y\}$ (second cell). Therefore, $r_{2}(G)=1$.

When $i=3$, we have other six proper colorings. Each of these colorings is a proper 3coloring and simultaneously, a strict 3-coloring. All the colorings generate only one feasible partition with cells $X_{1}=\{x\}, X_{2}=\{y\}$, and $X_{3}=\{z\}$. Hence $r_{3}(G)=1$. Since evidently, $r_{1}(G)=0$, we obtain that the chromatic spectrum of $G$ is:

$$
R(G)=(0,1,1) .
$$

The chromatic spectrum $R(G)$ is called continuous (gap-free) if it does not contain zeroes between positive components. Otherwise it is called broken (has gaps).

Theorem 5.2.1 For any graph $G$, the chromatic spectrum $R(G)$ is continuous.
Proof. As we noticed, $R(G)=\left(0,0, \ldots, 0, r_{\chi}, r_{\chi+1}, \ldots, r_{n}\right)$. By definition, $r_{\chi}>0$. Consider any strict coloring of $G$ with $\chi$ colors and choose any color class which has > 1 vertices. Split it into two non-empty subsets; we obtain another feasible partition using $\chi+1$ cells what implies $r_{\chi+1}>0$. Repeating this procedure further for any other cell having > 1 vertices, conclude that $r_{\chi+2}>0, r_{\chi+3}>0, \ldots$. We cannot continue the splitting when all cells have precisely one vertex each, and that corresponds to $r_{n}=1>0$. $\square$

We will see in Part II that this fundamental property does not hold in a more general case of hypergraph coloring.

There are many results about the bounds on the chromatic number. We end the section with the following observations. The König theorem (Theorem 2.4.1) about bipartite graphs may now be reformulated in terms of colorings:

Theorem 5.2.2 For a graph $G, \chi(G) \leq 2$ if and only if it has no odd cycles.
An important theorem relating maximum degree $\Delta(G)$ and chromatic number $\chi(G)$ of a graph $G$ is

Theorem 5.2.3 (Brooks, 1941) If $G$ is a connected graph different from a clique and an odd cycle, then $\chi(G) \leq \Delta(G)$.

Exercises 5.2.

1. Find the chromatic number of $E_{n}, K_{n}, K_{m, n}$, tree $T_{n}, C_{2 n}, C_{2 n+1}, W_{n}$, prism, cube and Petersen graph.
2. In graph $G$, see Figure 5.1, weakly delete an edge and find all feasible partitions, $P\left(G^{\prime}, 3\right)$ and $R\left(G^{\prime}\right)$.
3. For all graphs from 1. starting with any proper coloring by the minimum number of colors, show that the chromatic spectrum is gap free.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-099.jpg?height=338&width=933&top_left_y=237&top_left_x=406)
Figure 5.2.

4. Figure 5.2 exhibits a graph $G$ and a proper coloring. Find a respective feasible partition and values of $\lambda$ for which the coloring is a proper $\lambda$-coloring. Find a value of $i$ for which the coloring is a strict $i$-coloring.
5. Beginning with the feasible partition into $i=6$ cells for the graph in Figure 5.2, construct a sequence of feasible partitions into $i+1, i+2, \ldots, n=10$ cells.
6. For the graph in Figure 5.2, find a bound on the chromatic number by applying Brooks Theorem.
7. For the graph in Figure 5.2, find the exact value of the chromatic number and the corresponding optimal coloring.
8. For the graph in Figure 5.2, starting with optimal $\chi$-coloring, construct a sequence of feasible partitions into $\chi, \chi+1, \chi+2, \ldots, n=10$ cells.

Computer Projects 5.2. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$ and a coloring, check if the coloring is proper.
2. Given a graph $G$ and a proper coloring, output the respective feasible partition.
3. Given a graph $G$, using a generator of random numbers, generate a proper coloring.

### 5.3. Structure of Colorings

Let us have $\lambda \geq 1$ colors and consider graph $K_{n}$. Evidently, if $\lambda<n$, then there are no proper colorings of $K_{n}$ because all the vertices must be colored pairwise differently. Suppose now $\lambda \geq n$. Any assignment of $n$ different colors to the vertices of $K_{n}$ results in a proper coloring, so $\chi\left(K_{n}\right)=n$. What about $P\left(K_{n}, \lambda\right)$ ?

Let us start coloring $K_{n}$. We have $\lambda$ possibilities to color the first vertex. Then, for the second vertex, we have ( $\lambda-1$ ) possibilities. For the third vertex there are ( $\lambda-2$ ) possibilities. Any color used once, cannot be used again. Because of the symmetry of $K_{n}$, the order of such coloring procedure does not matter. If we continue it until the last vertex is colored, we arrive to the conclusion that

$$
P\left(K_{n}, \lambda\right)=\lambda(\lambda-1)(\lambda-2) \cdots(\lambda-n+1) .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-100.jpg?height=399&width=1093&top_left_y=233&top_left_x=365)
Figure 5.3. Complete graphs $K_{1}, K_{2}, K_{3}, K_{4}$, and their chromatic polynomials.

Figure 5.3 shows examples of the chromatic polynomials of the simplest complete graphs: The product $\lambda(\lambda-1)(\lambda-2) \cdots(\lambda-n+1)$ is denoted by $\lambda^{(n)}$ and sometimes called the falling factorial.

Let us have now a graph $G=(X, E)$ which is not a $K_{n}$. How to compute $P(G, \lambda)$ ? Since $G$ is not $K_{n}$, it has two nonadjacent vertices, say $x$ and $y$. All proper colorings of $G$ with $\lambda$ colors are split into two classes: when $x$ and $y$ have different colors and when $x$ and $y$ have the same color. All proper $\lambda$-colorings of $G$ when $x$ and $y$ have different colors are the proper $\lambda$-colorings of the graph $G_{1}=G \cup\{x, y\}$. All proper $\lambda$-colorings of $G$ when $x$ and $y$ have the same color are the proper $\lambda$-colorings of the graph $G_{2}=G_{1} \cdot\{x, y\}$ (recall that $G \cdot e$ denotes the graph obtained by contraction of an edge $e$, see Section 1.6., Figure 1.25). Therefore,

$$
P(G, \lambda)=P\left(G_{1}, \lambda\right)+P\left(G_{2}, \lambda\right) .
$$

Notice that compared to $G$, graph $G_{1}$ has the same vertices and edges except a newly added edge $\{x, y\}$. In its turn, graph $G_{2}$ has the same edge set and the same vertex set except that $x$ and $y$ are replaced be the new vertex $x y$. Graph $G_{1}$ has more edges, and graph $G_{2}$ has less vertices than $G$. It is important to observe that graph $G_{2}$ may have multiple edges. Namely, if vertices $x$ and $y$ have common neighbors in $G$, then contraction of edge $\{x, y\}$ leads to multiple edges. Since in the definition of proper coloring multiple edges play no role (only adjacency is important), we replace every multiple edge in graph $G_{2}$ by a single edge. So, without any loss of generality for colorings, we can assume that graph $G_{2}$ is also simple.

Figure 5.4 shows how we can depict the equality above as the equality of graph drawings. In this way, graph $G_{1}$ stands for "connection" and graph $G_{2}$ stands for "contraction". The connection-contraction algorithm itself consists in recurrent application of this step to every graph obtained. That means if $G_{1}$ or $G_{2}$ is not a complete graph, then we find another pair of not adjacent vertices and proceed as we did it with $x$ and $y$. If $P\left(G_{1}, \lambda\right)=P\left(G_{3}, \lambda\right)+P\left(G_{4}, \lambda\right)$ and $P\left(G_{2}, \lambda\right)=P\left(G_{5}, \lambda\right)+P\left(G_{6}, \lambda\right)$, then we obtain that $P(G, \lambda)=P\left(G_{3}, \lambda\right)+P\left(G_{4}, \lambda\right)+P\left(G_{5}, \lambda\right)+P\left(G_{6}, \lambda\right)$ and so on. When the procedure stops? It stops when we are not able to apply the connection, i.e. all obtained graphs are complete graphs. Therefore,

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-101.jpg?height=474&width=1103&top_left_y=205&top_left_x=331)
Figure 5.4. Connection-contraction.

$$
P(G, \lambda)=P\left(K_{i_{1}}, \lambda\right)+P\left(K_{i_{2}}, \lambda\right)+\cdots+P\left(K_{i_{s}}, \lambda\right)
$$

for some integer $s \geq 1$.
Since $P\left(K_{i_{j}}, \lambda\right)$ is a polynomial in $\lambda$, and the sum of polynomials is a polynomial, we conclude immediately that $P(G, \lambda)$ is a polynomial in $\lambda$. Moreover, among all complete graphs $K_{i_{1}}, K_{i_{2}}, \ldots, K_{i_{s}}$ only one is isomorphic to $K_{n}$; namely that which is obtained by connections only. All the other complete graphs have $<n$ vertices because they are obtained from $G$ by at least one contraction. Therefore, keeping in mind that $P\left(K_{n}, \lambda\right)=\lambda(\lambda-1)(\lambda- 2) \cdots(\lambda-n+1)$, our next conclusion is that the degree of $P(G, \lambda)$ is $n$ and the major coefficient is 1.

However, deeper analysis leads to deeper conclusions. Recall that all vertices of $G$ have their names, i.e. labels. When contracting the edges we concatenated the names and produced new names for new vertices. As the result, the vertices in every complete graph $K_{i}$ have composite names. Only the names of vertices in the unique graph $K_{n}$ are exactly the same as they are in $G$. Notice the following important fact. If the name of a vertex in some $K_{i}$ is $x y z$, for example, then there is a strict $i$-coloring of $G$ where vertices $x, y$, and $z$ are colored with the same color. In other words, every complete graph $K_{i}$ corresponds to some strict $i$-coloring of $G$, each vertex of $K_{i}$ corresponds to some color, and the composite name corresponds to all vertices of $G$ colored with that color.

There are no identical complete graphs with the same number of vertices if we compare the composite names of vertices. It is so because each $K_{i}$ was obtained by a unique way from $G$. Therefore, the number of all complete graphs having $i$ vertices equals the number of all feasible partitions of $G$ into $i$ cells, $r_{i}(G)$.

Collecting now all complete graphs on the same number of vertices and doing that for all possible values we obtain the following equality:

$$
\begin{gathered}
P(G, \lambda)=P\left(K_{i_{1}}, \lambda\right)+P\left(K_{i_{2}}, \lambda\right)+\cdots+P\left(K_{i_{s}}, \lambda\right)= \\
r_{1}(G) P\left(K_{1}, \lambda\right)+r_{2}(G) P\left(K_{2}, \lambda\right)+\cdots+r_{n}(G) P\left(K_{n}, \lambda\right)=
\end{gathered}
$$

$$
\sum_{i=1}^{n} r_{i}(G) P\left(K_{i}, \lambda\right) .
$$

Since $r_{1}=r_{2}=\cdots=r_{\chi-1}=0$ and $P\left(K_{i}, \lambda\right)=\lambda^{(i)}$, we arrive at last to the final fundamental equality:

$$
P(G, \lambda)=\sum_{i=\chi}^{n} r_{i}(G) \lambda^{(i)}
$$

Equality (5.3) explicitly shows the structure of proper colorings and their relation to feasible partitions: fix any feasible partition into $i$ cells, then count all the colorings that can be obtained from this partition by permutation of the colors $\left(\lambda^{(i)}\right)$, then do that for all feasible partitions $\left(r_{i}(G) \lambda^{(i)}\right)$, and at last count that for all $i$ (obtain $\sum_{i=\mathrm{x}}^{n} r_{i}(G) \lambda^{(i)}$ ). Connectioncontraction algorithm not only shows this structure, it also shows the way how to obtain $P(G, \lambda)$ for any graph $G$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-102.jpg?height=368&width=1082&top_left_y=984&top_left_x=365)
Figure 5.5. Connection-contraction for $G$.

Consider an example, see Figure 5.5. Let $G=(X, E)$ be the same graph as in Figure 5.1. Apply connection-contraction and immediately obtain

$$
\begin{gathered}
P(G, \lambda)=P\left(K_{3}, \lambda\right)+P\left(K_{2}, \lambda\right)=\lambda^{(3)}+\lambda^{(2)}= \\
\lambda(\lambda-1)(\lambda-2)+\lambda(\lambda-1)=\lambda(\lambda-1)^{2}
\end{gathered}
$$

Now without any exhaustive search for the colorings, we obtain, for example, that $P(G, 3)=3(3-1)^{2}=12$. Moreover, since $P(G, \lambda)=P\left(K_{3}, \lambda\right)+P\left(K_{2}, \lambda\right)=0 \cdot P\left(K_{1}, \lambda\right)+$ $1 \cdot P\left(K_{2}, \lambda\right)+1 \cdot P\left(K_{3}, \lambda\right)$, we conclude that the chromatic spectrum $R(G)=(0,1,1)$. The structure of the colorings can also be seen in Figure 5.5: when $i=3$, all the colorings are obtained from permutations of the colors; when $i=2$, all the colorings are obtained by permutations of two colors when vertex $y$ is colored with one color and vertices $x$ and $z$ with the other color.

The connection-contraction algorithm is good for small graphs but it is not efficient for large $n$. Since every graph produces two new graphs, the number of graphs is doubling at each step and is power of 2 . The whole procedure can be depicted itself as a graph, which is a directed tree, see Figure 5.6. Each arc shows which graph is obtained from which; left directed arcs denote connection, right directed arcs denote contraction. Graph $G$ is located on the zero level, graphs $G_{1}$ and $G_{2}$ on the first level, graphs $G_{3}, G_{4}, G_{5}$, and $G_{6}$ on the

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-103.jpg?height=686&width=1227&top_left_y=238&top_left_x=269)
Figure 5.6. Connection-contraction tree.

second level and so on down. Not all of the graphs $K_{i_{j}}$ are on the last level. Some of them may appear on higher levels.

Since the chromatic polynomial is unique for any graph $G$, there is a unique expansion of $G$ into combination of complete graphs as described in equality (5.2). This observation leads us to the conclusion that the order in which the connection-contraction is implemented is not important.

An implementation of the connection-contraction algorithm for cycle $C_{4}$ is shown in Figure 5.7 in full. Edges to be added at the next level and then contracted are shown by dashed lines. Multiple edges which appear after contraction are not shown. All four feasible partitions of $C_{4}$ can be found from the names of vertices of complete graphs. One can conclude that

$$
\begin{gathered}
P\left(C_{4}, \lambda\right)=0 \cdot P\left(K_{1}, \lambda\right)+1 \cdot P\left(K_{2}, \lambda\right)+2 \cdot P\left(K_{3}, \lambda\right)+1 \cdot P\left(K_{4}, \lambda\right)= \\
\lambda^{(2)}+2 \lambda^{(3)}+\lambda^{(4)}=\lambda(\lambda-1)+2 \lambda(\lambda-1)(\lambda-2)+\lambda(\lambda-1)(\lambda-2)(\lambda-3)= \\
\lambda(\lambda-1)[1+2(\lambda-2)+(\lambda-2)(\lambda-3)]=\lambda(\lambda-1)\left(\lambda^{2}-3 \lambda+3\right)= \\
\lambda^{4}-4 \lambda^{3}+6 \lambda^{2}-3 \lambda .
\end{gathered}
$$

and

$$
R\left(C_{4}\right)=(0,1,2,1) .
$$

If for example, 10 colors are available, then the number of all proper 10-colorings is $P\left(C_{4}, 10\right)=10 \cdot 9 \cdot\left(10^{2}-3 \cdot 10+3\right)=6570$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-104.jpg?height=1236&width=1160&top_left_y=202&top_left_x=241)
Figure 5.7. Connection-contraction for $C_{4}$.

Exercises 5.3.

1. Apply the connection-contraction algorithm to find the chromatic polynomial of the following graphs: $E_{4}, E_{5}, C_{5}, C_{6}, W_{4}, W_{5}, P_{4}, P_{5}, P_{6}$ and $P_{n}$ for every $n \geq 6$.
2. Apply the connection-contraction algorithm to find all feasible partitions for $P_{4}, P_{5}, P_{6}, C_{5}$ and $W_{5}$.
3. Apply the connection-contraction algorithm to find all feasible partitions and the chromatic spectrum for the graphs in Figure 5.8.
4. A manager needs to arrange five people A, B, C, D and E in the offices. Person A is in conflict with B and E; person B is in conflict with A and C; person C is in conflict with B and D; person D is in conflict with A, B, C, E; person E is in conflict with A and D. What is the minimum number of offices and in how many ways the people can be arranged in such a way that there is no conflict inside any office? Find all the assignments to the offices.
5. There are five cell phone towers A, B, C, D, and E. When transmitting a signal using the same frequency, tower A interferes with B and E; tower B interferes with A and C; tower C

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-105.jpg?height=233&width=1071&top_left_y=216&top_left_x=321)
Figure 5.8.

interferes with B and D; tower D interferes with A, B, C, E; tower E interferes with A and D. What is the minimum number of frequencies necessary to avoid interference at any moment of time? Find all possible optimal assignments of frequencies to the towers.

6. Which of the graphs in Figure 5.8 is the model for the problems 4 and 5 above?

Computer Projects 5.3. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, using a generator of random numbers, find several feasible partitions.
2. Given a graph $G$, using a generator of random numbers, find the lower bound on the chromatic spectrum.
3. Apply the connection-contraction algorithm to find all feasible partitions, chromatic polynomial and the chromatic spectrum for: a) cube; b) Petersen graph.

### 5.4. Chromatic Polynomial

Proposition 5.4.1 Suppose $G$ is not a connected graph, and let $G_{1}, G_{2}, \ldots, G_{k}$ be the connected components, $k \geq 2$. Then

$$
P(G, \lambda)=P\left(G_{1}, \lambda\right) P\left(G_{2}, \lambda\right) \cdots P\left(G_{k}, \lambda\right) .
$$

Proof. Indeed, each component can be colored independently; since $G_{1}$ has $P\left(G_{1}, \lambda\right)$ proper colorings, $G_{2}$ has $P\left(G_{2}, \lambda\right)$ proper colorings, and so on, the total number of proper colorings of $G$ is the product of these numbers. $\square$

The equality (5.5) can be immediately applied to graph $E_{n}$ : since $E_{n}=n K_{1}$, and $P\left(K_{1}, \lambda\right)=\lambda$, we obtain

$$
P\left(E_{n}, \lambda\right)=\lambda \cdot \lambda \cdot \ldots \cdot \lambda=\lambda^{n} .
$$

On the other hand, if we apply connection-contraction algorithm to $E_{n}$, we obtain the following equality:

$$
\lambda^{n}=S(n, 1) \lambda^{(1)}+S(n, 2) \lambda^{(2)}+\ldots+S(n, n) \lambda^{(n)}
$$

where $S(n, i)=r_{i}\left(E_{n}\right)$ are some numbers; in other words, $S(n, i)$ equals the number of partitions of a set of $n$ elements into $i$ subsets. These numbers are known as the so called

Stirling numbers of the second kind. Therefore, the chromatic spectrum of $E_{n}$ is nothing else than

$$
R\left(E_{n}\right)=(S(n, 1), S(n, 2), \ldots, S(n, n)) .
$$

One can check, for example, that $R\left(E_{1}\right)=(1), R\left(E_{2}\right)=(1,1), R\left(E_{3}\right)=(1,3,1)$, $R\left(E_{4}\right)=(1,7,6,1)$ and so on.

In turn, if we expand the expression for $\lambda^{(n)}$, then we obtain some polynomial with coefficients:

$$
\lambda^{(n)}=s(n, 1) \lambda+s(n, 2) \lambda^{2}+\ldots+s(n, n) \lambda^{n}
$$

which are called the Stirling numbers of the first kind. For example, $\lambda^{(4)}=-6 \lambda+11 \lambda^{2}-$ $6 \lambda^{3}+\lambda^{4}$, and therefore $s(4,1)=-6, s(4,2)=11, s(4,3)=-6$, and $s(4,4)=1$.

Generally, Stirling numbers serve as the coefficients to express $\lambda^{n}$ (or, equivalently, $E_{n}$ ) in terms of $\lambda^{(i)}$ (or, equivalently, $K_{i}$ ) and $\lambda^{(n)}$ in terms of $\lambda^{i}, i=1,2, \ldots, n$. The latter in a more general setting can be expressed as the disconnection-contraction algorithm.

The idea of it consists in the following. Recall that in the connection-contraction we had the equality (5.1):

$$
P(G, \lambda)=P\left(G_{1}, \lambda\right)+P\left(G_{2}, \lambda\right)
$$

where $G_{1}$ is obtained from $G$ by connection, and $G_{2}$ by contraction. We re-write this equality as

$$
P\left(G_{1}, \lambda\right)=P(G, \lambda)-P\left(G_{2}, \lambda\right) .
$$

We now look as if $G_{1}$ is an original graph, and $G$ is obtained from $G_{1}$ by deletion of an edge, i.e. disconnection, and $G_{2}$ is obtained from $G_{1}$ by the contraction of that edge. Applying this operation recurrently to each of the graphs obtained as many times as possible, we stop when all graphs on the right side of the equation above are the empty graphs. If the connection-contraction algorithm leads to a combination of complete graphs, the disconnection-contraction algorithm leads to a combination of empty graphs.

An example of disconnection-contraction algorithm applied to the very same graph $G$, see Figure 5.5, is shown in Figure 5.9. One can see that the same chromatic polynomial may be obtained in two different ways.

The next theorem describes the behavior of the coefficients of the chromatic polynomial.
Theorem 5.4.1 (Whitney, 1933) The chromatic polynomial $P(G, \lambda)$ is of degree $n(G)$, with integer coefficients alternating in sign and beginning with $1,-m(G), \ldots$.

Proof. We prove by induction on the number of edges $m(G)$. The theorem holds for $m=0$ because in this case $G=E_{n}$ and $P(G, \lambda)=\lambda^{n}$. Assume now that the theorem is true for all graphs with ; $m$ edges and let $G$ be an $n$-vertex graph with $m>1$ edges. Consider arbitrary edge $e$ of $G$. Graphs $G-e$ and $G \cdot e$ have fewer edges than $G$ each. In addition, $G \cdot e$ has $n-1$ vertices. By the induction hypothesis, there exist nonnegative integer numbers $\left\{a_{i}\right\}$ and $\left\{b_{i}\right\}$ such that

$$
P(G-e, \lambda)=\sum_{i=0}^{n}(-1)^{i} a_{i} \lambda^{n-i}
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-107.jpg?height=790&width=1175&top_left_y=236&top_left_x=269)
Figure 5.9. Disconnection-contraction for $G$.

and

$$
P(G \cdot e, \lambda)=\Sigma_{i=0}^{n-1}(-1)^{i} b_{i} \lambda^{n-1-i}
$$

Applying one step of disconnection-contraction to $G$ we obtain the equality which proves the theorem:

$$
\begin{gathered}
P(G, \lambda)=P(G-e, \lambda)-P(G \cdot e, \lambda) \\
=\lambda^{n}-(m-1) \lambda^{n-1}+a_{2} \lambda^{n-2}-\cdots+(-1)^{i} a_{i} \lambda^{n-i} \cdots \\
-\left(\lambda^{n-1}-b_{1} \lambda^{n-2}+b_{2} \lambda^{n-2}-\cdots+(-1)^{i} b_{i-1} \lambda^{n-i} \cdots\right) \\
=\lambda^{n}-m(G) \lambda^{n-1}+\left(a_{2}+b_{1}\right) \lambda^{n-2} \cdots(-1)^{i}\left(a_{i}+b_{i-1}\right) \lambda^{n-i} \cdots
\end{gathered}
$$ $\square$

Lemma 5.4.1 If a graph $G$ contains a clique of size $k$, then the set of all proper colorings of $G$ can be partitioned into $\lambda^{(k)}$ classes having $P(G, \lambda) / \lambda^{(k)}$ colorings each.

Proof. Let $G=(X, E)$ be a connected graph with some $S \subseteq X$ inducing a clique of size $k$. Let us have $\lambda$ available colors. Fix a proper coloring of $S$ with $\lambda$ colors and consider all proper $\lambda$-colorings of $G$ that can be obtained by the extension of the coloring of $S$. Suppose that the number of such colorings is $N_{1}$. Fix now another proper coloring of $S$ with $\lambda$ colors and consider all proper $\lambda$-colorings of $G$ that can be obtained by the extension of this new coloring of $S$. Denote the number of such colorings by $N_{2}$. We claim that $N_{1}=N_{2}$. Indeed, every coloring from the second set of colorings can be obtained from a coloring from the first set (and vice versa) by a permutation of colors. Permutation of colors $i$ and $j$ means that all vertices colored $i$ get color $j$ and all vertices colored $j$ get color $i$. Since $S$ induces a
clique, all colors are different, and any two colorings of $S$ can be obtained from each other by a permutation of colors.

Let $t=P\left(G_{S}, \lambda\right)=P\left(K_{k}, \lambda\right)=\lambda^{(k)}$. Repeating the reasoning above for each of $t$ colorings of $S$, we arrive to the conclusion that $N_{1}=N_{2}=N_{3}=\cdots=N_{t}$. Hence the set of all $P(G, \lambda)$ colorings of $G$ is partitioned into $t$ equal classes. This implies that the number of colorings in each class is $P(G, \lambda) / \lambda^{(k)}$. $\square$

Observe that the statement of the lemma does not hold if $S$ does not induce a clique. If $S$ has $k$ vertices and is not a clique, then it has at least two nonadjacent vertices. The subgraph induced by $S$ has two different colorings, one with $k$ colors and another with $k-1$ colors. These colorings cannot be obtained from each other by a permutation of colors. When $S$ induces a clique, it has the same unique feasible partition for every coloring of $G$.

Theorem 5.4.2 Let $G=(X, E)$ be a connected graph having a separator $S$ which is a clique of size $k$. Suppose $G_{1}=G_{X_{1} \cup S}$ and $G_{2}=G_{X_{2} \cup S}$ are the two derived subgraphs with respect to $S$. Then

$$
P(G, \lambda)=\frac{P\left(G_{1}, \lambda\right) P\left(G_{2}, \lambda\right)}{\lambda^{(k)}} .
$$

Proof. Since $G_{S}$ is a clique of size $k$ in $G_{X_{1} \cup S}$, by Lemma 5.4.1 the set of all $P\left(G_{X_{1} \cup S}, \lambda\right)$ colorings can be partitioned into $P\left(G_{S}, \lambda\right)=\lambda^{(k)}$ equal classes. Each class contains $P\left(G_{X_{1} \cup S}, \lambda\right) / \lambda^{(k)}$ colorings. Similarly, the $P\left(G_{X_{2} \cup S}, \lambda\right)$ colorings of $G_{X_{2} \cup S}$ can be partitioned into $\lambda^{(k)}$ equal classes, and each such class contains exactly $P\left(G_{X_{2} \cup S}, \lambda\right) / \lambda^{(k)}$ colorings.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-108.jpg?height=378&width=1196&top_left_y=1315&top_left_x=285)
Figure 5.10. Separation and the chromatic polynomial.

Combining every coloring from each class of $G_{X_{1} \cup S}$ with every coloring from the corresponding class of $G_{X_{2} \cup S}$ gives a coloring of $G$, see Figure 5.10. Therefore, the total number of colorings of $G$ is

$$
\begin{gathered}
P(G, \lambda)=\frac{P\left(G_{X_{1} \cup S}, \lambda\right)}{\lambda^{(k)}} \frac{P\left(G_{X_{2} \cup S}, \lambda\right)}{\lambda^{(k)}} \lambda^{(k)}= \\
\frac{P\left(G_{X_{1} \cup S}, \lambda\right) P\left(G_{X_{2} \cup S}, \lambda\right)}{\lambda^{(k)}} .
\end{gathered}
$$ $\square$

Corollary 5.4.1 Let $G=(X, E)$ be a connected graph having a separator $S$ which is a clique of size $k$. Suppose $G_{1}, G_{2}, \ldots G_{l}$ are the derived subgraphs with respect to the separator $S$. Then

$$
P(G, \lambda)=\frac{P\left(G_{1}, \lambda\right) P\left(G_{2}, \lambda\right) \cdots P\left(G_{l}, \lambda\right)}{\left[\lambda^{(k)}\right]^{l-1}} .
$$

Proof. Indeed, since $S$ belongs to every graph, we can repeat the same reasoning for each $G_{i}, i=1,2, \ldots, l$. The colorings of graphs all combine in every class of colorings generated by any single coloring of $S$. Since the number of classes is $\lambda^{(k)}$, the formula follows. $\square$

The formula (5.5) may be regarded as a special case of the formula above if for a moment we accept the point of view that disconnected graph is like "connected" graph having a separator which is an empty set, and define $P(\emptyset, \lambda)=1$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-109.jpg?height=557&width=1085&top_left_y=816&top_left_x=313)
Figure 5.11. Separation.

An example to the theorem above is shown in Figure 5.11. Since $G_{1}=C_{4}, G_{2}=K_{3}$ and $|S|=2$, we use the formula (5.4) for $P\left(C_{4}, \lambda\right)$ and $P\left(K_{3}, \lambda\right)=\lambda(\lambda-1)(\lambda-2)$ to compute the chromatic polynomial of the graph $G$ :

$$
\begin{gathered}
P(G, \lambda)=\frac{P\left(G_{1}, \lambda\right) P\left(G_{2}, \lambda\right)}{\lambda(2)}= \\
\frac{\left[\lambda(\lambda-1)\left(\lambda^{2}-3 \lambda+3\right)\right][\lambda(\lambda-1)(\lambda-2)]}{\lambda(\lambda-1)}= \\
\lambda(\lambda-1)(\lambda-2)\left(\lambda^{2}-3 \lambda+3\right)
\end{gathered}
$$

Corollary 5.4.2 If a connected graph $G$ has a simplicial vertex $x$ of degree $k$, then

$$
P(G, \lambda)=(\lambda-k) P(G-x, \lambda) .
$$

Proof. Suppose $G$ is not a complete graph. Then the neighborhood $N(x)$ is a complete separator, i.e. a separator induced by a clique on $k$ vertices. In this case $X_{2}=\{x\}$, see Figure 5.10. Applying formula (5.8) with $G_{1}=G-x, G_{2}=K_{k+1}$, and $G_{S}=K_{k}$ we obtain:

$$
P(G, \lambda)=\frac{P\left(G_{1}, \lambda\right) P\left(K_{k+1}, \lambda\right)}{\lambda^{(k)}}=
$$

$$
\frac{P(G-x, \lambda) \lambda^{(k+1)}}{\lambda^{(k)}}=(\lambda-k) P(G-x, \lambda) .
$$

If $G$ is a complete graph, then $G=K_{k+1}, G-x=K_{k}$ and the formula follows directly. $\square$

We can apply formula (5.10) to graph $G$ in Figure 5.11 and, since $x$ is a simplicial vertex and $G_{1}=G-x=C_{4}$, compute the chromatic polynomial of $G$ directly:

$$
P(G, \lambda)=(\lambda-2) P(G-x, \lambda)=\lambda(\lambda-1)(\lambda-2)\left(\lambda^{2}-3 \lambda+3\right) .
$$

Theorem 5.4.3 If a graph $G$ has a simplicial vertex $x$ of degree $k$, then

$$
r_{i}(G)=(i-k) r_{i}(G-x)+r_{i-1}(G-x) .
$$

Proof. Recall that $r_{i}(G)$ is the number of feasible partitions of graph $G$ into $i$ cells; it coincides with the number of strict $i$-colorings of $G$ if we do not count the permutations of colors.

If vertex $x$ is colored with one of the colors already used in $G-x$, then, because all colors in the neighborhood of $x$ are different, we have $(i-k) r_{i}(G-x)$ such possibilities. If vertex $x$ is colored with the color not used in $G-x$, then there are $r_{i-1}(G-x)$ possibilities. Hence the formula follows. $\square$

Corollary 5.4.3 If $S(n, i)$ is the Stirling number of the second kind, then

$$
S(n, i)=i S(n-1, i)+S(n-1, i-1) .
$$

Proof. Apply the theorem above to graph $E_{n}: r_{i}\left(E_{n}\right)=S(n, i)$ and each vertex may be regarded as a simplicial vertex of degree 0. $\square$

Since trivially $r_{1}\left(E_{1}\right)=S(1,1)=1$, the first five rows and columns of Stirling numbers are:

|  | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 | 0 |
| 3 | 1 | 3 | 1 | 0 | 0 |
| 4 | 1 | 7 | 6 | 1 | 0 |
| 5 | 1 | 15 | 25 | 10 | 1 |

One can see, for example, that

$$
S(5,3)=25=3 \cdot S(4,3)+S(4,2)=3 \cdot 6+7=25 .
$$

Exercises 5.4.

1. Apply the disconnection-contraction algorithm to compute the chromatic polynomial of $P_{3}, P_{4}, P_{5}, P_{n}$ for $n \geq 6$, for $C_{4}, C_{5}, C_{6}, C_{7}$, and for $W_{4}, W_{5}, W_{6}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-111.jpg?height=414&width=1075&top_left_y=214&top_left_x=319)
Figure 5.12.

2. Compute the Stirling numbers of the second kind corresponding to $E_{6}, E_{7}$, and $E_{8}$, and of the first kind corresponding to $K_{3}, K_{4}, K_{5}$, and $K_{6}$.
3. For each graph in Figure 5.12, by finding a simplicial vertex or a complete separator compute the chromatic polynomial.

Computer Projects 5.4. Write a program for the following algorithmic problems.

1. For any positive integers $n$ and $i \leq n$, compute $S(n, i)$.
2. Find a complete separator in a graph.
3. Program the disconnection-contraction algorithm for: a) the cube; b) Petersen graph.

### 5.5. Coloring Chordal Graphs

Chordal graphs have a very special place in graph coloring because the roots of their chromatic polynomials have nice properties. Recall that if $G$ is a chordal graph, then it has a simplicial elimination ordering, i.e. it can be decomposed by sequential elimination of simplicial vertices.

Let $G_{1}=(X, E),|X|=n$, be a chordal graph, and $\boldsymbol{\sigma}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ be a simplicial elimination ordering. Let $G_{2}=G_{1}-x_{1}, G_{3}=G_{2}-x_{2}, \ldots, G_{n}=G_{n-1}-x_{n-1}=\left\{x_{n}\right\}$, such that $G_{n+1}=G_{n}-x_{n}=\emptyset$. It means that vertex $x_{i}$ is a simplicial vertex of degree, say, $k_{i}$, in the graph $G_{i}, i=1, \ldots, n$. Apply sequentially formula (5.10) to each of the graphs in this order:

$$
\begin{gathered}
P\left(G_{1}, \lambda\right)=\left(\lambda-k_{1}\right) P\left(G_{2}, \lambda\right)=\left(\lambda-k_{1}\right)\left(\lambda-k_{2}\right) P\left(G_{3}, \lambda\right) \cdots= \\
\left(\lambda-k_{1}\right)\left(\lambda-k_{2}\right)\left(\lambda-k_{3}\right) \cdots\left(\lambda-k_{n}\right)
\end{gathered}
$$

We see that all the roots of $P\left(G_{1}, \lambda\right)$ are integer numbers equal to the degrees of the respective simplicial vertices. Since $G_{n}$ consists only of one vertex $x_{n}$, conclude that $k_{n}=0$ and we fix the first root $\lambda=0$. If $G_{1}$ is disconnected, then in each component there will be a last vertex of degree 0 ; thus the multiplicity of the root $\lambda=0$ equals the number of connected components of the graph $G_{1}$.

By the definition of clique number, $G_{1}$ contains a complete subgraph on $\omega\left(G_{1}\right)$ vertices, so maximum among all $k_{i}$ 's is $\omega\left(G_{1}\right)-1$. We now fix the second root of the chromatic polynomial, namely, $\lambda=\omega\left(G_{1}\right)-1$. Recall that $\omega\left(G_{1}\right) \leq \chi\left(G_{1}\right)$ what implies that there is no coloring using less than $\omega$ colors. Consequently, every integer on the closed interval $[0, \omega-1]$ is a root of $P\left(G_{1}, \lambda\right)$. Therefore, all roots $k_{i}$ are the integer numbers from the interval $[0, \omega-1]$, some of them may coincide (have multiplicity) but there are no gaps in these integers.

Finally, let us show that $\chi\left(G_{1}\right)=\omega\left(G_{1}\right)$ by coloring the vertices in the order inverse to $\boldsymbol{\sigma}$, i.e. $x_{n}, x_{n-1}, x_{n-2}, \ldots, x_{2}, x_{1}$. In general case this procedure is called online coloring because the vertices of a graph can imaginably be put on the real line and colored from left to right (or from right to left). The main point is to color the vertices sequentially to obtain a proper coloring of a graph.

To do that, color vertex $x_{n}$ with color 1 . Then, if $x_{n-1}$ is not possible to color with 1 (i.e., $x_{n}$ and $x_{n-1}$ are adjacent), color it with color 2. For $x_{n-2}$ try to use color 1, if not possible, try to use color 2, if not possible use the color 3. Continue this procedure each time trying to use the smallest possible color. If none of the used colors fits, use the new color. This is why sometimes the online coloring is called a greedy coloring. Since the maximum degree among $k_{i}$ 's is equal to $\omega-1$, we eventually obtain a coloring of $G_{1}$ with $\omega$ colors. Hence, the conclusion is that $\omega(G)=\chi(G)$. All these facts can be summarized in the next theorem.

Theorem 5.5.1 If $G$ is a chordal graph, then the chromatic polynomial has the following form:

$$
P(G, \lambda)=\lambda^{S_{0}}(\lambda-1)^{S_{1}}(\lambda-2)^{S_{2}} \cdots(\lambda-\chi(G)+1)^{S_{\chi-1}}
$$

where $s_{i} \geq 1(i=0,1, \ldots, \chi-1)$ is the number of simplicial vertices of degree $i$ in the simplicial elimination ordering of $G$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-112.jpg?height=316&width=935&top_left_y=1473&top_left_x=362)
Figure 5.13.

Consider now how this theorem works on the same example of a chordal graph shown in Figure 3.3, see Figure 5.13. As we have seen, $G_{1}$ has a simplicial elimination ordering $\boldsymbol{\sigma}=(1,2,3,4,5,6,7,8)$. The degrees of simplicial vertices in elimination $\boldsymbol{\sigma}$ are: 2, 2, 3, 2, $2,2,1,0$. These are the roots of the chromatic polynomial, they all are from the interval [0, 3]. Therefore, the chromatic polynomial

$$
\begin{gathered}
P\left(G_{1}, \lambda\right)=(\lambda-2)(\lambda-2)(\lambda-3)(\lambda-2)(\lambda-2)(\lambda-2)(\lambda-1)(\lambda-0)= \\
\lambda(\lambda-1)(\lambda-2)^{5}(\lambda-3) .
\end{gathered}
$$

Vertices 3, 6, 7 and 8 form the unique maximum clique, so $\omega\left(G_{1}\right)=\chi\left(G_{1}\right)=4$. Online coloring in the order 8, 7, 6, 5, 4, 3, 2, 1 (inverse to $\sigma$ ) produces a proper coloring using four colors, see Figure 5.14 (now the numbers are colors). There are other colorings with four colors; the total number of 4-colorings, for example, is:

$$
P\left(G_{1}, 4\right)=4(4-1)(4-2)^{5}(4-3)=384 .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-113.jpg?height=316&width=935&top_left_y=536&top_left_x=362)
Figure 5.14. Online coloring of chordal graph.

It would be difficult to find this number of colorings manually by exhaustive search, or even using connection-contraction algorithm developed for all graphs; structure of chordal graphs provides an efficient algorithm for computing the number of proper colorings for any number of available colors. But nice coloring properties of chordal graph go much beyond this. The rest of the section is devoted to such facts that are unimaginable for general graphs. We begin with

Corollary 5.5.1 If $T_{n}$ is a tree on $n$ vertices, then

$$
P\left(T_{n}, \lambda\right)=\lambda(\lambda-1)^{n-1}
$$

Proof. Trees are special case of chordal graphs, and pendant vertices are the special case of simplicial vertices. Decompose $T_{n}$ by sequential elimination of pendant vertices and apply formula (5.11). We obtain $n-1$ vertices of degree 1 and the last vertex of degree 0 , i.e. $k_{1}=k_{2}=\cdots=k_{n-1}=1, k_{n}=0$. $\square$

Lemma 5.5.1 For every cycle $C_{n}, n \geq 1$

$$
P\left(C_{n}, \lambda\right)=(\lambda-1)^{n}+(-1)^{n}(\lambda-1) .
$$

Proof. Induction on the number of vertices $n$. For $n=1,2,3$ verify directly (though $C_{1}$ and $C_{2}$ are not simple graphs, the formula holds). Assume the formula holds for any cycle on $<n$ vertices. Choose any edge of $C_{n}$ and apply disconnection-contraction:

$$
P\left(C_{n}, \lambda\right)=P\left(T_{n}, \lambda\right)-P\left(C_{n-1}, \lambda\right)=
$$

\{apply formula (5.13) and the induction hypothesis\} =

$$
\begin{gathered}
\lambda(\lambda-1)^{n-1}-\left[(\lambda-1)^{n-1}+(-1)^{n-1}(\lambda-1)\right]= \\
(\lambda-1)^{n}+(-1)^{n}(\lambda-1)
\end{gathered}
$$ $\square$

We now are able to state the following criterion for chordal graphs:

Theorem 5.5.2 A graph $G$ is chordal if and only if for any induced subgraph $G^{\prime}$ (including $G$ itself) the chromatic polynomial has the following form:

$$
P\left(G^{\prime}, \lambda\right)=\lambda^{s_{0}^{\prime}}(\lambda-1)^{s_{1}^{\prime}} \ldots\left(\lambda-\chi^{\prime}+1\right)^{s_{\chi^{\prime}-1}^{\prime}}
$$

where $\chi^{\prime}=\chi\left(G^{\prime}\right)$, and $s_{i}^{\prime} \geq 1\left(i=0,1, \ldots, \chi^{\prime}-1\right)$ is the number of simplicial vertices of degree $i$ in the simplicial elimination ordering of $G^{\prime}$.

Proof. ⇒ Every induced subgraph of a chordal graph is chordal as well. Apply Theorem 5.5.1.

⇐ If $G$ is not a chordal graph, then it contains a cycle $C_{k}, k \geq 4$ as an induced subgraph. It is easy to see that $\chi\left(C_{k}\right)=2$ if $k$ is even and $\chi\left(C_{k}\right)=3$ if $k$ is odd. Hence all the roots of $P\left(C_{k}, \lambda\right)$ should be from the set $\{0,1,2\}$. But by Lemma 5.5.1 $P\left(C_{k}, \lambda\right)=(\lambda-1)^{k}+$ $(-1)^{k}(\lambda-1)$. One can prove that $P\left(C_{k}, \lambda\right)$ being a polynomial of degree $k \geq 4$ has at least one complex root; a contradiction. $\square$

Let $G=(X, E)$ be a graph, $A \subset X$ be an arbitrary separator, $G_{1}^{*}=\left(X_{1}, E_{1}\right), G_{2}^{*}=$ $\left(X_{2}, E_{2}\right), \ldots, G_{k}^{*}=\left(X_{k}, E_{k}\right), k \geq 2$, be the connected components obtained after removing vertex set $A$ together with all incident edges from $G$. If $G$ is a disconnected graph having $l$ connected components, then we assume that $k>l$. So, we have $X_{1} \cup X_{2} \cup \ldots \cup X_{k} \cup A=X$, $X_{i} \cap X_{j}=\emptyset, i \neq j$. As usually, denote the derived induced subgraphs in the following way:

$$
G_{X_{1} \cup A}=G_{1}, G_{X_{2} \cup A}=G_{2}, \ldots, G_{X_{k} \cup A}=G_{k}, G_{A}=G_{0} .
$$

Theorem 5.5.3 A graph $G=(X, E)$ is chordal if and only if, for any induced subgraph $G^{\prime}=\left(X^{\prime}, E^{\prime}\right)$ (including $G$ itself) and any separator $A^{\prime} \subset X^{\prime}$ of $G^{\prime}$,

$$
P\left(G^{\prime}, \lambda\right)=\frac{P\left(G_{1}^{\prime}, \lambda\right) P\left(G_{2}^{\prime}, \lambda\right) \ldots P\left(G_{k}^{\prime}, \lambda\right)}{P\left(G_{0}^{\prime}, \lambda\right)^{k-1}} .
$$

Proof. ⇒ Since every induced subgraph of a chordal graph is chordal too, we prove the statement for $G^{\prime}=G$. We proceed by induction on $|X|=n$. The cases $n=2,3,4$, can be verified directly. Let the statement be true for all chordal graphs with fewer than $n$ vertices where $n>4$. Let $n(G)=n$, and $x_{0} \in X$ be a simplicial vertex of degree $p$ in $G$. There are two possible cases.

Case 1. $x_{0} \notin A$. Suppose that $x_{0} \in X_{1}$. Since $A$ is a separator and $x_{0}$ is a simplicial vertex, the neighborhood $N\left(x_{0}\right) \subseteq X_{1} \cup A$. Therefore, $x_{0}$ is a simplicial vertex in $G_{1}$. Applying formula (5.10) to $G_{1}$, we obtain:

$$
P\left(G_{1}, \lambda\right)=(\lambda-p) P\left(G_{1}-x_{0}, \lambda\right) .
$$

Applying the same formula to $G$, we have:

$$
P(G, \lambda)=(\lambda-p) P\left(G-x_{0}, \lambda\right) .
$$

Notice that $A$ is a separator in $G-x_{0}$ with the same number of derived subgraphs. Since $n\left(G-x_{0}\right)<n$ by the induction hypothesis,

$$
P\left(G-x_{0}, \lambda\right)=\frac{P\left(G_{1}-x_{0}, \lambda\right) P\left(G_{2}, \lambda\right) \ldots P\left(G_{k}, \lambda\right)}{P\left(G_{0}, \lambda\right)^{k-1}} .
$$

Multiplying both sides of (5.16) with the factor ( $\lambda-p$ ), we obtain

$$
P(G, \lambda)=\frac{P\left(G_{1}, \lambda\right) P\left(G_{2}, \lambda\right) \ldots P\left(G_{k}, \lambda\right)}{P\left(G_{0}, \lambda\right)^{k-1}} .
$$

Case 2. $x_{0} \in A$, see Figure 5.15. Let $\left|N\left(x_{0}\right) \cap A\right|=p_{1}$. Since $N\left(x_{0}\right)$ induces a complete graph, the remaining $p-p_{1}=p_{2}$ vertices from $N\left(x_{0}\right)$ belong to at most one, say $X_{1}$, of the sets $X_{i}, 1 \leq i \leq n$. Then

$$
\left\{x_{0}\right\} \cup N\left(x_{0}\right) \subseteq X_{1} \cup A, N\left(x_{0}\right) \cap A \subseteq X_{i} \cup A, 1 \leq i \leq k .
$$

One can see that the vertex $x_{0}$ is simplicial in $G_{1}$ with degree $p$ and in all subgraphs $G_{i}, i=$ $0,2,3, \ldots, k$ with degree $p_{1}$. Apply formula (5.10) to $G$ :

$$
P(G, \lambda)=(\lambda-p) P\left(G-x_{0}, \lambda\right) .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-115.jpg?height=782&width=999&top_left_y=917&top_left_x=383)
Figure 5.15.

Notice that set $A-x_{0}$ is a separator in $G-x_{0}$ with the same number of derived subgraphs. Since $n\left(G-x_{0}\right)<n$, by the induction hypothesis we have

$$
P\left(G-x_{0}, \lambda\right)=\frac{P\left(G_{1}^{\prime}, \lambda\right) P\left(G_{2}^{\prime}, \lambda\right) \ldots P\left(G_{k}^{\prime}, \lambda\right)}{P\left(G_{0}^{\prime}, \lambda\right)^{k-1}},
$$

where the graphs $G_{i}^{\prime}$ are obtained from $G_{i}$ by deletion of vertex $x_{0}, i=0,1, \ldots, k$.
On the other hand,

$$
P\left(G_{1}, \lambda\right)=(\lambda-p) P\left(G_{1}^{\prime}, \lambda\right), \text { and } P\left(G_{i}, \lambda\right)=\left(\lambda-p_{1}\right) P\left(G_{i}^{\prime}, \lambda\right)
$$

for $i=0,2, \ldots, k$.

It immediately follows again that

$$
P(G, \lambda)=\frac{P\left(G_{1}, \lambda\right) P\left(G_{2}, \lambda\right) \ldots P\left(G_{k}, \lambda\right)}{P\left(G_{0}, \lambda\right)^{k-1}} .
$$

⇐ For a contradiction, suppose $G$ is not chordal. Then it contains a cycle $C_{k}, k \geq 4$, as an induced subgraph. Let $x$ be a vertex of $C_{k}$. Since $N(x)$ is a separator, by formula (5.15), we obtain

$$
P\left(C_{k}, \lambda\right)=\lambda(\lambda-1)^{2} \lambda(\lambda-1)^{k-2} \lambda^{-2}=(\lambda-1)^{k} \neq P\left(C_{k}, \lambda\right),
$$

a contradiction. $\square$

As we have seen, formula (5.15) is known to be true for arbitrary graphs provided a separator induces a complete graph, see formula (5.9). The main feature of Theorem 5.5.3 is that in chordal graphs it holds for any separator. One can see that (5.15) holds for disconnected $G$ and $G_{A}$ (provided the number of connected components increases) or even for the empty separator. If we accept $P(\emptyset, \lambda)=1$, then (5.15) turns into the formula for the chromatic polynomial of a disconnected graph $G$ with connected components $G_{1}, \ldots, G_{k}$ (case $A=\emptyset$ ).

From this point of view, chordal graphs have so nice structure of colorings that they mysteriously look like "complete graphs having separators". However, (5.15) has an additional final important consequence. Namely, it implies the universal formula for computing the chromatic polynomial of a chordal graph using an arbitrary elimination ordering what is impossible for general graphs.

For a graph $G$, define the function

$$
W(G, \lambda)=\frac{\lambda P(G, \lambda-1)}{P(G, \lambda)} .
$$

Theorem 5.5.4 (universal formula) A graph $G=(X, E)$ is chordal if and only if in every connected induced subgraph $G^{\prime}=\left(X^{\prime}, E^{\prime}\right)$ for any vertex $x \in X^{\prime}$ the following equality holds:

$$
P\left(G^{\prime}, \lambda\right)=P\left(G^{\prime}-x, \lambda\right) W\left(G_{N(x)}^{\prime}, \lambda\right) .
$$

Proof. ⇒ Suppose $G$ is a chordal graph. Since every induced subgraph of a chordal graph is chordal, we prove the necessity for $G^{\prime}=G$. Hence, assume that $G=(X, E)$ is a connected chordal graph and $x \in X$ is an arbitrary vertex.

Case 1. $X=\{x\} \cup N(x)$. Since in any coloring of $G$ with $\lambda$ colors vertex $x$ requires a separate color,

$$
\begin{gathered}
P(G, \lambda)=\lambda P(G-x, \lambda-1)=\frac{P(G-x, \lambda)}{P(G-x, \lambda)} \lambda P(G-x, \lambda-1)= \\
P(G-x, \lambda) W\left(G_{N(x)}, \lambda\right)
\end{gathered}
$$

Case 2. $X \neq\{x\} \cup N(x)$. Since $G$ is connected, the subgraph $G_{N(x)}$ is a separator. Apply equality (5.15):

$$
P(G, \lambda)=\frac{P(G-x, \lambda) P\left(G_{\{x\} \cup N(x)}, \lambda\right)}{P\left(G_{N(x)}, \lambda\right)}=
$$

$$
P(G-x, \lambda) \frac{\lambda P\left(G_{N(x)}, \lambda-1\right)}{P\left(G_{N(x)}, \lambda\right)}=P(G-x, \lambda) W\left(G_{N(x)}, \lambda\right) .
$$

⇐ Suppose $G$ is not chordal and the formula (5.18) holds for any connected induced subgraph. Then it contains an induced cycle $C_{k}, k \geq 4$. Let $x$ be a vertex of $C_{k}$ which is denoted by just $C$. Observe that $C-x$ is a tree on $k-1$ vertices, and $C_{N(x)}=E_{2}$. We see that $P(C-x, \lambda)=\lambda(\lambda-1)^{k-2}, W\left(C_{N(x)}, \lambda\right)=\lambda^{-1}(\lambda-1)^{2}$, and by the formula

$$
P(C, \lambda)=P(C-x, \lambda) W\left(C_{N(x)}, \lambda\right)=(\lambda-1)^{k} \neq P(C, \lambda),
$$

a contradiction. $\square$

Corollary 5.5.2 If $x$ is a simplicial vertex of degree $k \geq 0$ in a chordal graph $G$, then

$$
P(G, \lambda)=(\lambda-k) P(G-x, \lambda) .
$$

Proof. Indeed, $N(x)=K_{k}$, so

$$
W\left(G_{N(x)}, \lambda\right)=W\left(K_{k}, \lambda\right)=\frac{\lambda(\lambda-1)^{(k)}}{\lambda^{(k)}}=(\lambda-k) .
$$

Applying universal formula (5.18) we obtain

$$
P(G, \lambda)=P(G-x, \lambda) W\left(G_{N(x)}, \lambda\right)=(\lambda-k) P(G-x, \lambda) .
$$ $\square$

So, decomposition of chordal graphs using a simplicial elimination ordering is a special case of a general procedure of decomposition by eliminating vertices in an arbitrary order and applying the universal formula (5.18).

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-117.jpg?height=316&width=924&top_left_y=1372&top_left_x=370)
Figure 5.16. Application of the universal formula.

Let us consider how the last theorems work on the example of graph $G$, see Figure 5.16. Suppose we delete non-simplicial vertex 4 and obtain graph $G_{1}$. To compute the chromatic polynomial $P(G, \lambda)$ from $G_{1}$, by the universal formula we need to multiply $P\left(G_{1}, \lambda\right)$ by the function $W\left(G_{N(4)}, \lambda\right)$. Since $N(4)=\{1,5,6\}$, the induced subgraph is a tree on three vertices (encircled by a dotted curve in the figure). Hence

$$
W\left(G_{N(4)}, \lambda\right)=\frac{\lambda P\left(T_{3}, \lambda-1\right)}{P\left(T_{3}, \lambda\right)}=\frac{\lambda(\lambda-1)(\lambda-2)^{2}}{\lambda(\lambda-1)^{2}}=\frac{(\lambda-2)^{2}}{\lambda-1} .
$$

If we decompose $G_{1}$ by simplicial elimination in ordering 1, 5, 6, 7, 8, 3, 2, the degrees of simplicial vertices respectively are: 1, 2, 3, 2, 2, 1, 0. We compute

$$
P\left(G_{1}, \lambda\right)=\lambda(\lambda-1)^{2}(\lambda-2)^{3}(\lambda-3) .
$$

Now

$$
\begin{gathered}
P\left(G_{1}, \lambda\right) W\left(G_{N(4)}, \lambda\right)=\lambda(\lambda-1)^{2}(\lambda-2)^{3}(\lambda-3) \frac{(\lambda-2)^{2}}{\lambda-1}= \\
\lambda(\lambda-1)(\lambda-2)^{5}(\lambda-3)=P(G, \lambda)
\end{gathered}
$$

as it was found in formula (5.12).
Exercises 5.5.

1. For graph $G$ in Figure 5.16, compute the chromatic polynomial using separator $\{5,6,7,8\}$ and respective derived subgraphs.
2. For graph $G$ in Figure 5.16, apply the universal formula for vertex 7.
3. Construct an example of a chordal graph and an ordering of vertices such that online coloring in that order does not give the minimum number of colors.

Computer Projects 5.5. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, recognize if $G$ is chordal.
2. Given a graph $G$, recognize if $G$ is chordal, and if yes, compute the chromatic polynomial.
3. Given a graph $G$, recognize if $G$ is chordal, and if yes, construct an optimal coloring.

### 5.6. Coloring Planar Graphs

Recall that for a graph $G=(X, E)$, the Szekeres-Wilf number is

$$
M(G)=\max _{X^{\prime} \subseteq X} \min _{x \in G^{\prime}} d(x)
$$

where $d(x)$ is the degree of vertex $x$ in a subgraph $G^{\prime}$ induced by the subset of vertices $X^{\prime}$. As we mentioned at the beginning of Section 3.3., this number can easily be found by sequential elimination of vertices of minimum degrees; the maximum degree obtained in this procedure is $M(G)$.

Theorem 5.6.1 For any graph $G, \chi(G) \leq M(G)+1$.
Proof. Decompose $G$ by a sequential elimination of vertices of minimum degree. We obtain a sequence of graphs $G_{1}=G, G_{2}, G_{3}, \ldots, G_{n}$ and corresponding sequence of vertices $x_{1}, x_{2}, \ldots, x_{n}$ such that each vertex $x_{i}$ is a vertex of minimum degree in a graph $G_{i}, i=1, \ldots, n$. We now apply online coloring to $G$ by reconstructing it in ordering $x_{n}, x_{n-1}, \ldots, x_{2}, x_{1}$. That means we color the vertices in order $x_{n}, x_{n-1}, \ldots, x_{2}, x_{1}$ each time using the smallest suitable color. In this sequence, the maximum number of colored neighbors for vertex $x_{i}$ is $M(G)$, see Figure 5.17. The worst case occurs when all $M(G)$ neighbors of $x_{i}$ have distinct colors (otherwise, we just assign to $x_{i}$ the first missing color). We then assign $(M(G)+1)$ th color to $x_{i}$ and continue online coloring. Even if the worst case occurs several times, the total number of colors used in the obtained proper coloring does not exceed $M(G)+1$. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-119.jpg?height=469&width=911&top_left_y=205&top_left_x=430)
Figure 5.17. $G_{i+1}$ is colored, $x_{i}$ is not.

Corollary 5.6.1 If $G$ is a planar graph, then $\chi(G) \leq 6$.
Proof. Recall that by Corollary 4.2.3, $G$ contains a vertex of degree at most 5. Any subgraph of $G$ is a planar graph. Therefore, in any decomposition of $G$ by vertices of minimum degrees, the degrees do not exceed 5. Hence $M(G) \leq 5$. Applying Theorem 5.6.1 results in $\chi(G) \leq 6$. $\square$

Theorem 5.6.2 (Five Color Theorem, Heawood, 1890) If $G=(X, E)$ is a planar graph, then $\chi(G) \leq 5$.

Proof. We prove the theorem by induction on $n(G)=n$. Evidently, all planar graphs having $\leq 5$ vertices are 5-colorable (color all vertices differently).

Assume now that all planar graphs having $<n$ vertices are 5 -colorable. We will prove that under this assumption, $\chi(G) \leq 5$. By Corollary 4.2.3, $G$ contains a vertex $x$ of degree $d(x) \leq 5$. By the induction hypothesis, $\chi(G-x) \leq 5$. Consider a proper 5-coloring of $G-x$. By this, all the vertices of $N(x)$ get some colors. We will show that there is always a way to assign a color to vertex $x$ such that $G$ is 5-colorable.

Case 1: the number of colors used in $N(x)$ is $\leq 4$. We assign the 5 th color to $x$ and obtain a 5-coloring of $G$.

Case 2: the number of colors used in $N(x)$ is 5. It means that $d(x)=5$. The main idea of the rest of the theorem is to show that we can construct another proper 5-coloring of $G-x$ which uses only 4 colors in the neighborhood $N(x)$.

The situation is equivalent to that shown in Figure 5.17 for $G_{i}=G$, but now it can be depicted more specifically in Figure 5.18. Without loss of generality, denote $N(x)=$ \{a,b,c,d,e\} and respective colors by 1, 2, 3, 4 and 5.

Subcase 2.1: in the 5 -coloring of $G-x$, there exists an $(a, c)$-path $P$ with vertices colored by alternating colors 1 and 3 as shown in Figure 5.18 (numbers are the colors). Path $P$ along with edges $a x$ and $x c$ form a cycle $C$ in the plane with all vertices colored 1 and 3, and vertex $x$ uncolored. Switch the colors 2 and 4 on vertices located in the plane

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-120.jpg?height=681&width=1144&top_left_y=238&top_left_x=295)
Figure 5.18.

inside cycle $C$; such re-coloring does not affect vertices colored 2 and 4 which are outside $C$. Therefore, vertex $d$ preserves color 4. We obtain another proper 5-coloring of $G-x$ where vertices $d$ and $b$ are colored with color 4. In this new coloring, color 2 is missing in $N(x)$; assign color 2 to vertex $x$ and obtain a proper 5-coloring of $G$.

Subcase 2.2: in the 5 -coloring of $G-x$, there is no $(a, c)$-path with vertices colored by alternating colors 1 and 3. Let $G_{13}$ be a subgraph of $G-x$ induced by the vertices colored with colors 1 and 3. $G_{13}$ is a disconnected graph and vertices $a$ and $c$ are in different components. Switch the colors 1 and 3 in the component containing vertex $a$. We obtain a proper 5-coloring of $G-x$ where color 1 is missing in $N(x)$. Assign color 1 to vertex $x$ and obtain a proper 5-coloring of $G$, what proves the theorem. $\square$

Theorem 5.6.3 (Four Color Theorem, Appel, Haken, Koch, 1977) If $G$ is a planar graph, then $\chi(G) \leq 4$.

Kempe's proof, 1879, the most famous error in the history of Graph Theory. We "prove" the theorem by induction on $n(G)=n$. Since $K_{5}$ is not a planar graph, all planar graphs having $\leq 5$ vertices are 4-colorable.

Assume now that all planar graphs having $<n$ vertices are 4 -colorable. We will "prove" that under this assumption, $\chi(G) \leq 4$. Observe that any plane graph can be complete to a triangulation, i.e. a plane graph with all faces being triangles by just adding some edges. If we prove that any triangulation is 4-colorable, it will imply that any plane graph is 4-colorable, too. Therefore, without loss of generality we assume that $G$ is a triangulation.

By Corollary 4.2.3, $G$ contains a vertex $x$ of degree $d(x) \leq 5$. By the induction hypothesis, $\chi(G-x) \leq 4$. Consider a proper 4-coloring of $G-x$. By this, all the vertices of $N(x)$ get some colors. We "will show" that there is always a way to assign a color to vertex $x$ such that $G$ is 4-colorable.

Case 1: the number of colors used in $N(x)$ is $\leq 3$. We assign the 4th color to $x$ and obtain a 4-coloring of $G$.

Case 2: the number of colors used in $N(x)$ is 4. It means that $d(x)=4$ or $d(x)=5$.
Subcase 2.1: $d(x)=4$. Apply the reasoning from Theorem 5.6.2 for $G^{\prime}=G-e$ (in fact, vertex $e$ and color 5 was never used in that proof).

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-121.jpg?height=779&width=1116&top_left_y=539&top_left_x=324)
Figure 5.19. Kempe's "proof".

Subcase 2.2: $d(x)=5$. Since the number of colors used in $N(x)$ is 4, two vertices get the same color. Denote $N(x)=\{a, b, c, d, e\}$ and respective colors by 1, 2, 3, and 4. Since we assumed that $G$ is a triangulation, the vertices of the same color cannot be consecutive in the order $a, b, c, d, e$. Assume that the colors are distributed as shown in Figure 5.19. Let $G_{i j}$ denote the subgraph induced by vertices colored $i$ and $j$, and $P_{i j}$ denote any path having all vertices colored with alternating (along the path) colors $i$ and $j$.

Subcase 2.2.1: in the 4-coloring of $G-x$, there is no $(a, c)$-path $P_{13}$ or there is no $(a, d)$-path $P_{14}$. For example, assume there is no $(a, c)$-path $P_{13}$. Then the subgraph $G_{13}$ is disconnected, and vertices $a$ and $c$ are in different components. Switching the colors 1 and 3 in the component containing vertex $a$ eliminates color 1 from $N(x)$; we then assign color 1 to $x$ and obtain a proper 4-coloring of $G$. Similar reasoning applies if there is no $(a, d)$-path $P_{14}$.

Subcase 2.2.2: in the 4-coloring of $G-x$, both $(a, c)$-path $P_{13}$ and $(a, d)$-path $P_{14}$ exist, see Figure 5.19. Observe that the component $G^{\prime}$ of $G_{24}$ containing vertex $b$ is separated from vertices $d$ and $e$ by the cycle completed by $(a, c)$-path $P_{13}$ and edges $a x$ and $x c$. Similarly, the component $G^{\prime \prime}$ of $G_{23}$ containing vertex $e$ is separated from vertices $b$ and $c$ by the cycle
completed by $(a, d)$-path $P_{14}$ and edges $a x$ and $x d$. We now permute color 2 with 4 in $G^{\prime}$ and color 2 with 3 in $G^{\prime \prime}$. This recoloring eliminates color 2 from $N(x)$. Assign color 2 to vertex $x$ and obtain a proper 4-coloring of $G$, what "proves" the theorem. $\square$

Where is the trap in this reasoning by Kempe? The answer to this question is depicted in Figure 5.20. The problem is that in Subcase 2.2.2, $(a, c)$-path $P_{13}$ and $(a, d)$-path $P_{14}$ may intersect at a vertex of color 1. Then the permutation of color 2 with 4 in $G^{\prime}$ and of color 2 with 3 in $G^{\prime \prime}$ leads to a pair of adjacent vertices colored with color 2 (marked by "?"), i.e. to a non proper coloring of $G$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-122.jpg?height=1025&width=1116&top_left_y=676&top_left_x=324)
Figure 5.20. The most famous error in the history of Graph Theory.

The proof above was published by Kempe in 1879, and the error is very instructive. On one hand, it shows an excellent example how drawings may be used in Graph Theory proofs. On the other hand, it explicitly exhibits the limits of drawings. Since the result was considered proven until 1890, it also demonstrated the fact that mathematicians of those times liked writing papers more than reading them. But on the top of all that, nobody could even imagine what a dramatic history was ahead.

Formulated first in 1852 by Francis Guthrie (a student (!) of de Morgan), "proved" in 1879 by Kempe, refuted in 1890 by Heawood, the Four Color Problem became one of the most famous problems in Discrete Mathematics in 20th century before in 1977 it became the Four Color Theorem by Appel, Haken, and Koch. Besides many erroneous proofs, it
generated many new directions in Graph Theory. For example, only one sub-direction of chromatic polynomials introduced by Birkhoff in 1912 with the aim to solve the problem by algebraic methods counts more than five hundred research papers.

The main idea of the final proof is quite simple - by induction on the number of vertices; but the number of cases is huge. Though the Kempe's proof was erroneous, his idea of alternating paths and further re-coloring of the respective subgraphs was used in the final proof. A path on which two colors alternate is called a Kempe chain. In a plane triangulation, a configuration is a derived subgraph with respect to a separating cycle; it is a subgraph induced by the cycle and all the vertices which are inside the cycle in the plane. For example, in Figure 5.20, the subgraph induced by vertices $a, b, c, d, e$ and $x$ is a configuration. It is basically the same idea that was used in chordal graphs, or more generally, any graphs having separators, see Figures 1.34, 5.8, 5.17. In chordal graphs, separators were cliques, in triangulations, separators are cycles.

In a plane triangulation, a configuration is reducible if any 4-coloring of the cycle can be extended to a 4-coloring of the entire triangulation. There were the following two basic steps in the proof:

1. Proof that any plane triangulation contains a configuration from a list of unavoidable configurations.
2. Proof that each unavoidable configuration is reducible.

In 1976, Appel, Haken, and Koch, using 1,200 hours of computer time, found 1936 (!) unavoidable configurations and proved that all they are reducible. Historically, it was the first time when a famous mathematical problem was solved by extensive use of computers. The final accord in this one-century drama was when the result was widely announced, the paper was published in 1977, and the University of Illinois even announced it by postage meter stamp of "four colors suffice", a few errors were found in the original proof. Fortunately for the authors, they have been fixed. For the first time, regardless the fact that there is no human being who would check the entire proof (because it contains steps that most likely can never be verified by humans), the problem is considered completely solved.

In 1996, Robertson, Sanders, Seymour and Thomas improved the proof by finding the set of only (!) 633 reducible configurations. Computers, Kempe chains, and some other techniques were used in both proofs.

The three consecutive theorems - Corollary 5.6.1 (six colors), Theorem 5.6.2 (five colors) and Theorem 5.6.3 (four colors) show the main feature of graph coloring: there is a very simple proof for six colors, a relatively simple proof for five colors and an incredible difficult and complex proof for four colors. The Four Color Problem, formulated by a student, was first "solved" by a lawyer, and really solved with many contributions of the very prominent mathematicians of the century.

So we can conclude that every geographic map can be colored with at most four colors. Sometimes one can use less colors. What about the map of USA? Four Color Theorem implies that it can be colored with four colors. But can it be colored with 3 colors? The answer is no. Indeed, take for example the state of Nevada and five its neighbors: Idaho, Utah, Arizona, California and Oregon. One can easily check, see Figure 5.21, that their adjacency forms the wheel $W_{6}$ for which $\chi\left(W_{6}\right)=4$. West Virginia and Kentucky are also in

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-124.jpg?height=437&width=674&top_left_y=237&top_left_x=554)
Figure 5.21.

the center of $W_{6}$ and $W_{8}$ respectively. Hence a planar graph corresponding to the entire map of USA contains subgraphs which need four colors each anyway. It means that precisely four colors is the minimum for the entire map of USA.

Exercises 5.6.

1. Compute $M(G)$ where $G$ is: $P_{n}, K_{n}, K_{m, n}, C_{n}, W_{n}, m, n \geq 4$, tree, Petersen graph, cube and prism, find the bound on the chromatic number and the respective coloring.
2. Arbitrarily draw any number of straight lines in the plane. Use mathematical induction to prove that the obtained regions can be colored with two colors in such a way that no two of them with a common segment of line have the same color.
3. Color the map of USA with four colors.
4. Construct a planar graph $G$ with no subgraphs isomorphic to $W_{n}, n \geq 4$, such that $\chi(G)=4$.

Computer Projects 5.6. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, find $M(G)$, bound on the chromatic number, and the respective coloring.
2. Given a planar graph $G$, find an optimal coloring.
3. Given a plane graph $G$ and a proper coloring. Find the longest Kempe chain.

### 5.7. Perfect Graphs

Any graph $G$ contains a maximum clique which by definition has $\omega(G)$ vertices. Since its vertices are pairwise adjacent, any proper coloring of $G$ requires at least $\omega$ colors, i.e.

$$
\chi(G) \geq \omega(G) .
$$

There are graphs with $\chi(G)=\omega(G)$, and there are graphs for which $\chi(G)>\omega(G)$. For example, $\chi\left(C_{4}\right)=\omega\left(C_{4}\right)=2$ but $\chi\left(C_{5}\right)=3>\omega\left(C_{5}\right)=2$. How large can be the difference $\chi(G)-\omega(G)$ ? The answer is: it can be arbitrary large.

Consider the so called Mycielski's construction. Two vertices are called copies of each other if they have the same neighborhoods and are not adjacent. Respectively, copying a vertex means adding a new vertex adjacent to all neighbors of a given vertex. A vertex is called universal if it is adjacent to all other vertices of a graph. In a complete graph all vertices are universal. Generally, adding a new vertex to a graph and making it universal increases the size of maximum clique by 1. It also increases the chromatic number by 1 because the universal vertex requires a new color.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-125.jpg?height=311&width=930&top_left_y=621&top_left_x=417)
Figure 5.22.

Start with graph $K_{2}$. Copy the vertices, see Figure 5.22, encircled. Then add a new vertex adjacent to all the copies. The last vertex is "universal" to the copies but its addition does not create triangles and therefore does not increase the clique number. However, it increases the chromatic number. This is the main trick of the construction. Notice that the graph obtained is $C_{5}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-125.jpg?height=531&width=627&top_left_y=1362&top_left_x=570)
Figure 5.23.

Now repeat the procedure for $C_{5}$ : copy each vertex and add a new vertex adjacent to all of the copies. It is convenient to draw the copies and the "universal" vertex inside the cycle, see Figure 5.23. This graph is called the Grötzsch graph. For it $\chi=4$, and evidently, $\omega=2$. One can prove that if we repeat the procedure $k$ times, we obtain a graph with $\boldsymbol{\chi}-\boldsymbol{\omega}=k$. It means that from theoretical point of view, there exist graphs with arbitrary large difference $\boldsymbol{\chi}-\boldsymbol{\omega}$ which are triangle-free. If $\boldsymbol{\omega}(G)$ is the lower bound for $\boldsymbol{\chi}(G)$, then what are the graphs for which $\chi(G)=\omega(G)$ ?

In Graph Theory, when we have some property for a graph, it is convenient to require this property to hold for each induced subgraph. The main motivation is that in such case we can apply mathematical induction by the number of vertices and prove many results.

Definition 5.7.1 A graph $G$ is perfect if $\chi\left(G^{\prime}\right)=\omega\left(G^{\prime}\right)$ for any induced subgraph $G^{\prime}$ including $G$ itself.

It appears that perfection of graphs is related to the complements of graphs. Recall that the clique cover number $\theta(G)$ of a graph $G$ is the minimum number of cliques in graph $G$ such that each vertex belongs to precisely one clique. We say that the cliques "cover" the vertex set of $G$. Since every clique in $G$ induces an independent set in complement $\bar{G}$, we conclude that every coloring of $G$ is equivalent to a clique covering of $\bar{G}$, and thus $\chi(G)=\theta(\bar{G})$. Therefore, if $\bar{G}$ is a perfect graph, then $\theta\left(G^{\prime}\right)=\alpha\left(G^{\prime}\right)$ holds for any induced subgraph $G^{\prime}$ of $G$ including $G$ itself.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-126.jpg?height=557&width=1116&top_left_y=909&top_left_x=318)
Figure 5.24. Perfect graphs.

For example, a graph $G$ in Figure 5.24 has $\chi(G)=3, \omega(G)=3$, and $\alpha(G)=2$ and $\theta(G)=2$. A proper 3-coloring is shown by numbers, and clique covering is shown by dotted ellipses. Respectively, for its complement $\bar{G}$, we have $\chi(G)=2, \omega(G)=2, \alpha(G)=3$ and $\theta(G)=3$. One can easily see that clique covering of $G$ by two cliques corresponds to a proper 2-coloring of $\bar{G}$ and so on. It is also easy to check that $G$ and $\bar{G}$ both are perfect graphs. An example of an imperfect graph is $C_{5}: \chi\left(C_{5}\right)=3, \omega\left(C_{5}\right)=2, \alpha\left(C_{5}\right)=2$ and $\theta\left(C_{5}\right)=3$ (recall that $C_{5}$ is isomorphic to $\overline{C_{5}}$ ). In these examples graphs and their complements behave similarly with respect to graph perfection. Is this the rule?

May we have the equality $\chi\left(G^{\prime}\right)=\omega\left(G^{\prime}\right)$ for all induced subgraphs $G^{\prime}$ and inequality $\theta\left(G^{\prime}\right) \neq \alpha\left(G^{\prime}\right)$ for at least one induced subgraph? In other words, may we have a perfect graph $G$ such that $\bar{G}$ is not perfect? The answer is no. This fact was first stated as the Weak Perfect Graph Conjecture by Berge in 1960 and proved by Lovász in 1972 (the first proof used hypergraph approach).

Theorem 5.7.1 (Weak Perfect Graph Theorem, Lovász, 1972) A graph $G$ is perfect if and only if its complement $\bar{G}$ is perfect.

Chordal graphs were the first proved to be perfect:
Theorem 5.7.2 If $G$ is a chordal graph, then it is perfect.
Proof. Let $G$ be a chordal graph. Since any induced subgraph $G^{\prime}$ is chordal, it is sufficient to prove that $\chi(G)=\omega(G)$. Since $G$ is chordal, it has a simplicial elimination ordering. Apply online (greedy) coloring to $G$ by coloring vertices in inverse ordering as we did it in Section 5.5. Recall that the maximum vertex degree is $\omega(G)-1$. Hence, $\chi(G)=\omega(G)$ and $G$ is perfect. $\square$

Theorem 5.7.3 If $G$ is a quasi-triangulated graph, then it is perfect.
Proof. Let $G$ be a quasi-triangulated graph. Then by definition, see Section 3.5., it has a decomposition by sequential elimination of vertices that at each step, are simplicial or co-simplicial (simplicial in the complement). For any induced subgraph $G^{\prime}$, this ordering of vertices induces an ordering of vertices of $G^{\prime}$ with the same properties. Therefore $G^{\prime}$ has a decomposition by sequential elimination of vertices that at each step, are simplicial or co-simplicial. It means that $G^{\prime}$ is also a quasi-triangulated graph. Hence, as for chordal graphs, without loss of generality it is sufficient to prove that $\chi(G)=\omega(G)$.

Prove by induction on the number of vertices $n(G)$. The equality $\chi(G)=\omega(G)$ is true for $n=3,4,5$. Let it be true for all quasi-triangulated graphs on $<n$ vertices and $n(G)=n$. By definition, $G$ has a vertex $x$ which is simplicial in $G$ or in $\bar{G}$.

Case 1: $x$ is a simplicial vertex in $G$. Consider a proper coloring of $G-x$ by $\chi(G-x)=$ $\omega(G-x)$ colors. If $\omega(G)=\omega(G-x)$, then $|N(x)| \leq \omega(G-x)-1$ and we can use a color missing in $N(x)$ to color vertex $x$. If $\omega(G)=\omega(G-x)+1$, then $|N(x)|=\omega(G-x)$ and we must use a new color for $\chi$. In both cases we obtain a proper coloring of $G$ with $\chi(G)=\omega(G)$ colors. Therefore, $G$ is perfect.

Case 2: $x$ is a simplicial vertex in $\bar{G}$. Again, graph $G-x$ is quasi-triangulated, has $<n$ vertices, and by the induction hypothesis is perfect. By Theorem 5.7.1, graph $\overline{G-x}$ is perfect quasi-triangulated graph. $\bar{G}$ is obtained from $\overline{G-x}$ by adding simplicial vertex $x$. By Case 1, $\bar{G}$ is perfect. By Theorem 5.7.1, $G$ is perfect. $\square$

There are many classes of perfect graphs. Among them are bipartite graphs, weakly chordal graphs (containing no induced cycles of length $\geq 5$ in $G$ and in $\bar{G}$ ), strongly perfect (every induced subgraph has an independent set intersecting all maximal cliques), Meyniel graphs (each odd cycle of length $\geq 5$ has at least two chords), Berge graphs (no induced odd cycles of length $\geq 5$ in graph and its complement). Examples and theorem above give rise to the idea that odd cycles of length $\geq 5$ in graph and its complement prevent a graph from being perfect. Stated as the Strong Perfect Graph Conjecture by Berge in 1960, it became one of the most important results in graph theory of our time:

Theorem 5.7.4 (Strong Perfect Graph Theorem, Chudnovsky, Robertson, Seymour, Thomas, 2003) A graph $G$ is perfect if and only if it contains no induced $C_{2 k+1}$ and $\bar{C}_{2 k+1}$, $k \geq 2$.

One of the fundamental properties of perfect graphs is that they, in contrast to general graphs, allow polynomial time algorithm (see Section 12.2.) for such optimization problem
as finding the chromatic number, and consequently, the minimum clique covering, maximum independent set, and the maximum clique.

Exercises 5.7.

1. Determine if Petersen graph and its complement are perfect.
2. Determine which wheels are perfect and which are not.
3. Apply one step of Mycielski's construction starting with $P_{5}, C_{4}, C_{6}, K_{4}$, prism.
4. Prove that $\theta\left(C_{7}\right)>\alpha\left(C_{7}\right)$.
5. Are cube and prism perfect graphs?

Computer Projects 5.7. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, determine if it contains induced $C_{5}$.
2. Given a quasi-triangulated graph $G$, find an optimal coloring.
3. Given a quasi-triangulated graph $G$, find the clique cover number $\Theta(G)$ and the respective clique covering.

### 5.8. Edge Coloring and Vizing's Theorem

In Graph Coloring, we can also color the edges of a graph. In such colorings, parallel (multiple) edges will make a difference, but loops create inconveniences. Therefore the loops are ignored. Let $G=(X, E)$ be a graph with possible parallel edges but without loops, and $\lambda \geq 0$ be the number of available colors.

Definition 5.8.1 $A$ proper edge $\lambda$-coloring of $G$ is an assignment of a color from set $\{1,2, \ldots, \lambda\}$ to every edge of $G$ is such a way that all edges incident to every vertex have distinct colors. A graph is edge $k$-colorable if it has a proper edge coloring with at most $k$ colors.

Since the maximum number of colors that can be used equals $|E|$, we are interested in the minimum number of colors. In order not to confuse with the chromatic number, the minimum number of colors over all proper edge colorings is called the chromatic index of $G$ and denoted by $\chi^{\prime}(G)$.

In any proper edge coloring of $G=(X, E)$, edges of the same color represent some matchings. Thus the coloring itself is the partition of the edge set $E$ into a number of matchings. The chromatic index $\chi^{\prime}(G)$ is the minimum number of distinct matchings over all such partitions.

Edge colorings of $G$ can be expressed as vertex colorings of an auxiliary graph with vertices representing the edges of $G$. For graph $G=(X, E)$, construct a simple graph $G^{\prime}=$ $\left(X^{\prime}, E^{\prime}\right)$ such that $X^{\prime}=E$ and $E^{\prime}$ is formed in the following way: two vertices in $G^{\prime}$ are adjacent if and only if the respective edges have a common vertex in $G$. Graph $G^{\prime}$ is called the line graph of $G$ and is denoted by $L(G)$. Not every graph can be a line graph.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-129.jpg?height=751&width=1038&top_left_y=243&top_left_x=365)
Figure 5.25.

An example of a graph $G$, its line graph $L(G)$, proper edge 4-coloring of $G$ and proper vertex 4-coloring of $G^{\prime}=L(G)$ is shown in Figure 5.25. One can see that every proper edge coloring of $G$ corresponds to a proper vertex coloring of $G^{\prime}$ and vice versa. For this example $L(G)$ is a chordal graph, so for edge colorings of $G$ we can even compute the chromatic polynomial $P(L(G), \lambda)=\lambda(\lambda-1)(\lambda-2)^{2}(\lambda-3)$ as it follows from the respective simplicial decomposition. Notice that every non pendant vertex of $G$ forms a clique in $L(G)$ but not vice versa: clique $\{b, c, d, e\}$ in $L(G)$ does not have a corresponding vertex in $G$. At last, observe that $\chi^{\prime}(G)=4=\chi(L(G))$, and moreover, the equality $\chi^{\prime}(G)=\chi(L(G))$ holds for any graph $G$ without loops.

As usually, let $\Delta(G)$ denote the maximum vertex degree of $G$. Evidently, $\chi^{\prime}(G) \geq \Delta(G)$. Maximum degree $\Delta$ plays a similar role for the chromatic index $\chi^{\prime}$ as the clique number $\omega$ plays for the chromatic number $\boldsymbol{\chi}$ in vertex coloring where $\boldsymbol{\chi} \geq \boldsymbol{\omega}$. But how far may be the value $\chi^{\prime}(G)$ from $\Delta(G)$ ? Surprisingly, it must be very close.

Theorem 5.8.1 (Vizing, 1964) If $G$ is a simple graph, then either

$$
\chi^{\prime}(G)=\Delta(G), \text { or } \chi^{\prime}(G)=\Delta(G)+1 \text {. }
$$

Proof. Simple examples (like $C_{2 k}$ and $C_{2 k+1}$ ) show that there are graphs with both values of $\chi^{\prime}$. We will show that any graph can be edge colored with $\Delta+1$ colors.

Let $G$ be a simple graph. Take $\Delta+1$ colors and properly color as many edges as possible. If all edges are colored, we are done. Otherwise, we obtain some partial edge coloring. Suppose an edge connecting vertices $x$ and $y_{0}$ and denoted by just $x y_{0}$, is uncolored. We will recolor edges in such a way that $x y_{0}$ becomes colored and the number of colors remains the same. After repeating the procedure as many times as necessary, a complete proper edge coloring of $G$ will be obtained. Since we use $\Delta+1$ colors and $\Delta$ is the maximum degree,
at each vertex at least one color is missing. A feature of this proof is that the reasoning is constructed in terms of such missing colors.

The best case: a color $c$ is missing at both vertices $x$ and $y_{0}$. Color edge $x y_{0}$ with $c$.
The good case: there is no color missing at both $x$ and $y_{0}$ simultaneously. Let a color $c_{0}$ be missing at $x$ and color $c_{1}$ be missing at $y_{0}$. If there is an edge $x y_{k}$ colored $c_{1}$ with both ends missing a color $c_{i}$, then re-color $x y_{k}$ with $c_{i}$ and color $x y_{0}$ with $c_{1}$.

The bad case: there is no edge $x y_{k}$ colored $c_{1}$ with both ends missing a color. Edge $x y_{1}$ is colored $c_{1}$; a color $c_{2}$ is missing at $y_{1}$. Edge $x y_{2}$ is colored $c_{2}$, a color $c_{3}$ is missing at $y_{2}$. Edge $x y_{3}$ is colored $c_{3}$, a color $c_{4}$ is missing at $y_{3}$, and so on, see Figure 5.26 (missing colors are denoted by $\bar{c}_{i}$ ). Suppose this sequence continues until a color $c_{l+1}$ is missing at both vertex $x$ and $y_{l}$. Then we re-color each edge $x y_{i}$ from $c_{i}$ to $c_{i+1}, i=1,2, \ldots, l$. Call this re-coloring downshifting from $y_{l}$. We arrive to a situation when color $c_{1}$ is missing at $x$. Since it is missing at $y_{0}$, too, color edge $x y_{0}$ with $c_{1}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-130.jpg?height=1049&width=1080&top_left_y=852&top_left_x=318)
Figure 5.26.

The worst case: we never reach the situation when some color is missing at both ends of an edge. Then in the sequence of colors $c_{1}, c_{2}, c_{3}, \ldots$, sooner or later, some color $c_{l+1}$ repeats (i.e., we have a loop) because the number of colors is finite. Let $c_{l+1}=c_{k}$ be the first such coincidence of the colors, $1 \leq k \leq l$. Observe that color $c_{0}$ is present at all colored neighbors of $x$ and it is missing at $x$. Consider now the Kempe path $P$ consisting of edges of
two alternating colors $c_{0}$ and $c_{k}$ and beginning at vertex $y_{l}$. Since we color the edges, each vertex may have at most two edges colored with $c_{0}$ and $c_{k}$; therefore, there is the only such path.

Subcase 1: $P$ reaches vertex $y_{k}$ and therefore ends at $x$. Switch colors $c_{0}$ and $c_{k}$ along $P$. We obtain edge $x y_{k}$ with color $c_{k}$ missing at both ends. Downshifting from $y_{k}$ results in release of color $c_{1}$ to be used for $x y_{0}$.

Subcase 2: $P$ reaches vertex $y_{k-1}$ and therefore ends at $y_{k-1}$. Again, switch colors $c_{0}$ and $c_{k}$ along $P$. As a result, color $c_{0}$ is missing at $y_{k-1}$. Since it is also missing at $x$, we obtain edge $x y_{k-1}$ with color $c_{0}$ missing at both ends. Perform downshifting from $y_{k-1}$ and again, release color $c_{1}$ to color edge $x y_{0}$.

Subcase 3: $P$ never reaches $y_{k}$ or $y_{k-1}$. Since $c_{k}$ is present at $x, P$ never reaches vertex $x$. Switch the colors $c_{0}$ and $c_{k}$ along $P$; color $c_{0}$ becomes missing at $y_{l}$. Perform downshifting from $y_{l}$ and release color $c_{1}$ to color edge $x y_{0}$. $\square$

The theorem above partitions all simple graphs into two classes: Class 1 if $\chi^{\prime}(G)=$ $\Delta(G)$ and Class 2 if $\chi^{\prime}(G)=\Delta(G)+1$. Determining whether a simple graph is Class 1 or Class 2 is a hard problem.

If a graph $G$ has multiple (parallel) edges (but not loops), the multiplicity of $G$, denoted by $\mu(G)$, is the maximum number of parallel edges connecting a pair of vertices. Theorem 5.8.1 allows then the following generalization:

Theorem 5.8.2 (Vizing, 1964) If $G$ is a loop-less multigraph with multiplicity $\mu(G)$, then $\Delta(G) \leq \chi^{\prime}(G) \leq \Delta(G)+\mu(G)$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-131.jpg?height=408&width=801&top_left_y=1323&top_left_x=616)
Figure 5.27. "Fat triangle" requires $\Delta+\mu$ colors.

The "worst" example when the upper bound is achieved (i.e. $\chi^{\prime}(G)=\Delta(G)+\mu(G)$ ) is represented by the so called "fat triangle", see Figure 5.27. Theorem 5.8.2 is a direct generalization of Theorem 5.8.1 because for simple graphs $\mu=1$.

We conclude with
Theorem 5.8.3 (König, 1916) If $G$ is a bipartite graph, then $\chi^{\prime}(G)=\Delta(G)$.

Exercises 5.8.

1. Find the chromatic index and an optimal edge coloring of: $K_{n}, C_{n}, W_{n}, K_{m, n}$, where $m, n \geq 3$.
2. Find the chromatic index, chromatic class and an optimal edge coloring of cube, prism and their complements.
3. Prove that for the Petersen graph $\chi^{\prime}=4$.
4. In the Petersen graph, replace each edge by three parallel edges and find the chromatic index and respective edge coloring.

Computer Projects 5.8. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a tree, find the chromatic index and an optimal edge coloring.
2. Given a graph $G$, at random generate an edge coloring and test if it is proper.
3. Given a multigraph $G$, generate a proper edge coloring using a vertex ordering.

### 5.9. Upper Chromatic Index

In this section we show how replacing the definition of proper edge coloring with the opposite version (the requirement "all of different colors" is replaced by "at least two of the same color") leads to the concept of the upper chromatic index and a formula for it.

Let $G=(X, E)$ be an arbitrary multigraph without loops and, as usually, $\{1,2, \ldots, \lambda\}$ be the set of available colors.

Definition 5.9.1 A proper edge $\lambda$-coloring of multigraph $G$ is an assignment of a color from set $\{1,2, \ldots, \lambda\}$ to every edge of $G$ in such a way that every non-pendant vertex of $G$ is incident to at least two edges of the same color.

Following this new definition, we can color all edges with one color and it will be a proper coloring; however, we cannot use $|E|$ colors unless $G$ is just a matching. Let us agree that if $k$ colors are really used in a proper edge coloring, $k \leq \lambda$, then the coloring is called strict edge $\boldsymbol{k}$-coloring, or just $\boldsymbol{k}$-coloring.

Definition 5.9.2 The maximum number $k$ for which there exists a proper edge $k$-coloring of multigraph $G$ is called the upper chromatic index and denoted by $\bar{\chi}^{\prime}(G)$.

An example of a multigraph $G$ and its edge 3-coloring is shown in Figure 5.28. We will show that it uses the maximum number of colors, i.e., $\bar{\chi}^{\prime}(G)=3$.

Theorem 5.9.1 For a connected multigraph $G$, the upper chromatic index $\bar{\chi}^{\prime}(G)=1$ if and only if the maximum degree $\Delta(G) \leq 2$.

Proof. ⇒ Let $\bar{\chi}^{\prime}(G)=1$. For a contradiction, suppose $\Delta(G) \geq 3$. If $G$ contains a cycle, then color the edges of the cycle with color 1 , and all the other edges with color 2 . If $G$ is a tree, color any maximal path with color 1 and all other edges with color 2. In both cases we obtain a proper edge 2-coloring, a contradiction.

⇐ The converse is evident since $\Delta(G) \leq 2$ implies that $G$ is either a cycle or a path. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-133.jpg?height=287&width=489&top_left_y=285&top_left_x=665)
Figure 5.28.

For a connected multigraph $G$, theorem 5.9.1 immediately implies that $\bar{\chi}^{\prime}(G) \geq 2$ if and only if $\Delta(G) \geq 3$.

Consider a proper edge $k$-coloring of $G=(X, E)$; it partitions $E$ into $k$ color classes $\left\{C_{1}, C_{2}, \ldots, C_{k}\right\}$ where each $C_{i}$ is a set of edges colored with color $i$. We denote such partition and the respective edge coloring by $f$.

Let $G_{i}=\left(X_{i}, C_{i}\right)$ be the subgraph of $G$ with a set of vertices $X_{i}$ determined by endpoints of the edges of $C_{i}$. Notice that subgraphs $G_{i}$ are not necessarily connected multigraphs and may have common vertices with each other; however, they do not have common edges.

A vertex $x$ of a subgraph $G_{i}$ is said to be satisfied by subgraph $G_{i}$ if it is not a pendant vertex in $G_{i}$.

Let us discuss some properties of edge colorings that use $\bar{\chi}^{\prime}(G)$ colors.
Theorem 5.9.2 If $f$ is a coloring of $G$ using $\bar{\chi}^{\prime}(G)$ colors, then

$$
\bar{\chi}^{\prime}\left(G_{i}\right)=1, i=1, \ldots, \bar{\chi}^{\prime}(G) .
$$

Proof. In coloring $f$, every pendant vertex of $G_{i}$ is satisfied by some other subgraph. Therefore any proper coloring of $G_{i}$ with at least two colors leads to a proper $\left(\bar{\chi}^{\prime}(G)+1\right)$ coloring of $G$, a contradiction. $\square$

Corollary 5.9.1 Let $f$ be a coloring of $G$ using $\bar{\chi}^{\prime}(G)$ colors. Then each $G_{i}$, where $1 \leq i \leq$ $\bar{\chi}^{\prime}(G)$, is either a cycle or a path.

Proof. Indeed, in $f$, every $G_{i}$ must be connected because otherwise we could increase the number of colors. Any connected multigraph with $\bar{\chi}^{\prime}(G)=1$ is either a cycle or a path (Theorem 5.9.1). $\square$

Theorem 5.9.3 Let $f$ be a coloring of $G$ using $\bar{\chi}^{\prime}(G)$ colors. Then for every vertex $x$ of $G$ the following implications hold:

1) if $x$ is satisfied by a cycle, then $x$ is satisfied by no path;
2) if $x$ is satisfied by two cycles, say $G_{i}$ and $G_{j}$, then $x$ is the only common vertex for $G_{i}$ and $G_{j}$.

Proof. In 1), otherwise, we could break the path in two paths and increase the number of colors.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-134.jpg?height=344&width=997&top_left_y=254&top_left_x=386)
Figure 5.29.

In 2), otherwise, we could split two cycles $G_{i}$ and $G_{j}$ into one cycle and two paths, see Figure 5.29, assign colors $i$ and $j$ to the paths and a new color to the new cycle, and again, increase the number of colors. $\square$

Corollary 5.9.2 Let $f$ be a coloring of $G$ using $\bar{\chi}^{\prime}(G)$ colors. If a vertex $x$ of $G$ is satisfied by more than one $G_{k}$, then all $G_{l} s$ which satisfy $x$, are all cycles with one vertex in common.

Given a $\bar{\chi}^{\prime}(G)$-coloring of an arbitrary multigraph $G$, we now partition the subgraphs $G_{i}$ of $G$ into the following three classes.

Class A: contains all $G_{i}$ forming the maximum number of (vertex) disjoint cycles in $f$. Clearly, the number $c^{\prime}$ of subgraphs in A satisfies $c^{\prime} \leq c$ where $c$ is the maximum number of disjoint cycles in $G$.

Class B: contains the remaining cycles and paths with length at least two each.
Class C: contains $G_{i}$ which represent a separate edge each.
Observe that all non-pendant vertices of $G$ are satisfied by subgraphs from classes A and B, and none is satisfied by any edge from part C; in addition, no pendant vertex is satisfied.

If class B contains cycles, then given the maximum number of disjoint cycles in A, and by Theorem 5.9.2, each of these cycles has a single vertex in common with only one of the cycles in A. The cycles in B may be considered as paths whose endpoints coincide. Notice that the number of edges in each such cycle or path equals the number of internal vertices plus 1.

The next theorem determines the formula for the upper chromatic index. It may be seen as the opposite to Vizing's theorem in the sense that finding the minimum number of colors is replaced with finding the maximum number of colors. At this point, proper vertex coloring defined in Section 5.2., proper edge coloring defined in Section 5.8. and proper edge coloring defined in this section look unrelated; we will see however in Part II, that all they represent special cases of one unifying concept called "mixed hypergraph coloring".

Theorem 5.9.4 (M.Gionfriddo, Milazzo, Voloshin, 2001) If $G=(X, E)$ is an arbitrary multigraph with $|X|=n,|E|=m$, the number of pendant vertices $p$, and the maximum number of disjoint cycles $c$, then

$$
\bar{\chi}^{\prime}(G)=c+m-n+p .
$$

Proof. We prove first that $\bar{\chi}^{\prime}(G) \leq c+m-n+p$. By Corollary 5.9.1, if a coloring $f$ uses $\bar{\chi}^{\prime}(G)$ colors, then subgraphs $G_{i}, 1 \leq i \leq \bar{\chi}^{\prime}(G)$, are either cycles or paths, while Corollary 5.9.2 states that if a vertex $x$ is satisfied by more than one graph $G_{i}$, then all these graphs have precisely one vertex in common.

Let $c^{\prime}$ be the number of subgraphs, and $v^{\prime}$ be the number of satisfied vertices in class A. Clearly, $v^{\prime}$ coincides with the number of edges in A because all cycles in A are vertex disjoint. Let $x$ be a satisfied vertex in $G$. If $x$ is satisfied by some $G_{l}$ from class A, then it is possible to look at all the other $G_{k} \mathrm{~s}$ which satisfy $x$, like paths with endpoints $x$.

If $x$ is not satisfied by any subgraph from class A, then it is satisfied by a subgraph from class B; therefore it is possible to consider one such subgraph $G_{k}$ as a cycle and all others as paths with endpoints $x$.

Let $r$ be the number of $G_{i}$ s in class B. Since pendant vertices are not satisfied, the number of vertices that are satisfied by subgraphs from B equals $n-v^{\prime}-p$. They are the internal vertices for the paths or the internal vertices for the cycles which are considered as paths with coinciding endpoints. Since the number of edges in each of them equals the number of internal vertices plus 1 , and the number of all such subgraphs equals $r$, the total number of edges in B equals

$$
n-v^{\prime}-p+r .
$$

Let $m^{\prime}$ be the number of edges in classes A and B combined. Then we obtain:

$$
m^{\prime}=v^{\prime}+\left(n-v^{\prime}-p+r\right)=n-p+r .
$$

Since class C contains $m-m^{\prime}$ edges, the number of colors in $f$ is:

$$
\bar{\chi}^{\prime}(G)=c^{\prime}+r+\left(m-m^{\prime}\right)=c^{\prime}+m-n+p,
$$

and therefore we obtain

$$
\bar{\chi}^{\prime}(G)=c^{\prime}+m-n+p \leq c+m-n+p .
$$

Next we prove that $\bar{\chi}^{\prime}(G) \geq c+m-n+p$. Let us choose $c$ vertex disjoint cycles $C_{1}, \ldots, C_{c}$ and denote the subgraph with vertex set $X$ and edges of these cycles by $A_{0}$. Color the edges of the cycles properly with the colors $1, \ldots, c$. Since the number of edges $m\left(A_{0}\right)=$ $n\left(A_{0}\right)$, and the number of pendant vertices $p\left(A_{0}\right)=0$, we obtain a proper coloring of $A_{0}$ using $c+m\left(A_{0}\right)-n\left(A_{0}\right)+p\left(A_{0}\right)$ colors. Therefore, $\bar{\chi}^{\prime}\left(A_{0}\right) \geq c+m\left(A_{0}\right)-n\left(A_{0}\right)+p\left(A_{0}\right)$, and the inequality holds.

Now we implement the following coloring augmenting procedure. Choose any satisfied vertex, say $x$, incident to an uncolored edge and construct a path along uncolored edges until the first satisfied vertex $y$ is reached or we get stuck at a pendant vertex $y$. Since $A_{0}$ constitutes the maximum number of disjoint cycles, the new vertices and edges represent either a cycle or a path (if they form a cycle, then $x=y$ ).

Add these new vertices and edges to $A_{0}$ and denote the obtained subgraph by $A_{1}$. Color the added edges with a new color and declare respective vertices satisfied.

If $y$ is pendant, then the numbers of newly added vertices and edges coincide. If $y$ is not pendant, then the number of added edges equals the number of added vertices plus 1. So, in either case,

$$
\bar{\chi}^{\prime}\left(A_{1}\right) \geq \bar{\chi}^{\prime}\left(A_{0}\right)+1 \geq c+m\left(A_{1}\right)-n\left(A_{1}\right)+p\left(A_{1}\right),
$$

and therefore the inequality holds. We repeat this coloring procedure by constructing subgraphs $A_{2}, A_{3}, \ldots$ until all the edges of $G$ are colored and all non-pendant vertices satisfied. Since at each coloring step the inequality holds, we obtain that $\bar{\chi}^{\prime}(G) \geq c+m-n+p$. Hence the theorem follows. $\square$

For our example, see Figure 5.28, it is easy to see that $c=1, m=5, n=4$ and $p=1$, and the formula gives:

$$
\bar{\chi}^{\prime}(G)=c+m-n+p=1+5-4+1=3,
$$

so the coloring in the Figure is maximal, i.e., using the maximum number of colors. As there are several largest sets of vertex disjoint cycles, there are several maximal colorings. Notice that any two parallel edges form cycle $C_{2}$ and may contribute to the value of $c$.

Theorem 5.9.4 allows finding the upper chromatic index for particular classes of multigraphs.

Theorem 5.9.5 If $G$ is a tree, then

$$
\bar{\chi}^{\prime}(G)=p-1 .
$$

Proof. Indeed, for any tree $c=0$ and $m=n-1$. $\square$

Exercises 5.9.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-136.jpg?height=393&width=626&top_left_y=1323&top_left_x=517)
Figure 5.30.

1. For graph $G$, see Figure 5.30, find a maximal edge coloring by hand.
2. For graph $G$, see Figure 5.30, find the largest set of vertex disjoint cycles and determine $\bar{\chi}^{\prime}(G)=c+m-n+p$ and respective edge coloring.
3. For graph $G$, see Figure 5.30, find another largest set of vertex disjoint cycles, calculate $\bar{\chi}^{\prime}(G)$ and show respective edge coloring.
4. For graph $G$, see Figure 5.30, show that coloring the edges of $C_{5}$ with one color does not produce maximal coloring.

5. Find the upper chromatic index and a maximal edge coloring of: $C_{n}, W_{n}, K_{n}, K_{m, n}$, where $m, n \geq 2$.
6. Find the upper chromatic index and a maximal edge coloring of Petersen graph, cube and prism and their complements.
7. In Petersen graph, replace each edge by three parallel edges and find the upper chromatic index and respective edge coloring.
8. In $C_{n}, W_{n}, K_{n}, K_{m, n}$, where $m, n \geq 2$, replace each edge by two parallel edges and find the upper chromatic index and respective edge coloring.

Computer Projects 5.9. Write a program for the following algorithmic problems.

1. Given a graph $G$, find a number of vertex disjoint cycles and an estimate on $\bar{\chi}^{\prime}(G)$.
2. Given a graph $G$ and a number of properly colored vertex disjoint cycles, implement the edge coloring procedure as described in the proof of Theorem 5.9.4 to augment the coloring.
3. Generate an edge coloring at random and verify if it is proper.
4. Generate a maximal edge coloring of complete graph $K_{n}, n \geq 5$.
5. Given a tree $T_{n}$, construct a maximal edge coloring.

## Chapter 6

## Traversals and Flows

### 6.1. Eulerian Graphs

In a graph $G$, a walk is an alternating sequence of vertices and edges where every edge connects preceding and succeeding vertices in the sequence. A walk starts at a vertex, end at a vertex and has the following form: $x_{0}, e_{1}, x_{1}, e_{2}, \ldots, e_{k}, x_{k}$. There are no restrictions on repetitions of vertices and edges. The number of edges in a walk is its length. So, a walk beginning at $x_{0}$ and ending at $x_{k}$ has the length $k$; it is a $\left(x_{0}, x_{k}\right)$-walk. A walk with $x_{0}=x_{k}$ is called closed. If no edge is repeating, then a walk is called a $\left(x_{0}, x_{k}\right)$-trail. A trail with no repeating vertices clearly is a path; a path with $x_{0}=x_{k}$ clearly is a cycle. Thus we recognize the well known concepts as the special cases of a walk and trail.

A connected graph $G$ is called Eulerian if it has a closed trail containing all edges of $G$; such a trail is then called an Eulerian trail. Since trails do not repeat edges, Eulerian trail passes through each edge once.

Lemma 6.1.1 If in a graph $G$ the degree of every vertex is at least 2 , then $G$ contains a cycle.

Proof. If $G$ contains loops or multiple edges, then the statement is evident. Therefore, assume $G$ is a simple graph. Consider a path $P$ of maximal length with an endpoint $x$. Observe that all neighbors of $x$ line on $P$ because otherwise we could extend $P$. Since $G$ is simple and the degree of $x$ is at leats 2, vertex $x$ has at least two distinct neighbors on $P$. Thus vertex $x$, the two its neighbors on $P$ and the segment of $P$ between them form a cycle of length at least 3. $\square$

Theorem 6.1.1 (Euler, 1736) A connected graph $G$ is Eulerian if and only if the degree of every vertex is even.

Proof. ⇒ Let $T$ be an Eulerian trail in $G$.Each time $T$ passes through a vertex, it uses two edges. Since $T$ is closed and uses all edges, every vertex has an even degree.

⇐ Induction on the number of edges of $G$ : assume the statement is true for all graphs with less than $m(G)$ edges. Since the degree of every vertex in $G$ is even and $G$ is connected, the degree each vertex is at least 2. Therefore, by Lemma 6.1.1, $G$ contains a cycle $C$, see

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-140.jpg?height=531&width=1024&top_left_y=239&top_left_x=371)
Figure 6.1.

Figure 6.1 (take any cycle as $C$ ). Delete the edges of $C$ from $G$ and obtain a graph $G^{\prime}$ in which all vertices have even degrees. Graph $G^{\prime}$ may be disconnected but since $G$ is connected, cycle $C$ passes through each component of $G^{\prime}$. Since $m\left(G^{\prime}\right)<m(G)$, by the induction hypothesis, every connected component of $G^{\prime}$ has an Eulerian trail. Now we combine cycle $C$ with an Eulerian trail of each connected component of $G^{\prime}$ in the following way: traverse $C$ and make a detour at the very first vertex of each component. Since every detour ends at the same vertex where it started, an Eulerian trail of $G$ is constructed. $\square$

The theorem above implies that every graph $G=(X, E)$ having all vertices of even degree may be decomposed into cycles, i.e., edge set $E$ may be partitioned into subsets where each subset forms a cycle.

The proof of the theorem above explicitly suggests the idea how to construct an Eulerian trail in a given Eulerian graph: choose a closed trail and then recurrently extend it until the initial graph is obtained.

Exercises 6.1.

1. Which of the graphs $K_{n}, K_{m, n}, W_{n}$, cube, prism, the Petersen graph, a tree are Eulerian?
2. The degree equality $\Sigma_{i=1}^{n} d\left(x_{i}\right)=2 m$ (See Proposition 1.1.1) implies that in any graph $G$, the number of vertices of odd degree is even. How this fact can be used to make any graph Eulerian?
3. Show that if a connected graph $G$ contains $k$ vertices of odd degree, then the minimum number of trails that partition the edges is $k / 2$.
4. Show that if a connected graph $G$ contains $k$ vertices of odd degree, then $k / 2$ continuous pen-strokes are sufficient to draw $G$ in the plane.
5. What is the minimum number of trails that partition the edge set of the Petersen graph?

Computer Projects 6.1. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$, recognize if it is Eulerian, and if yes, then construct an Eulerian trail.

### 6.2. Hamiltonian Graphs

In contrast to Eulerian graphs, one may ask if in a graph $G$, there exists a closed trail passing exactly one time through every vertex of $G$. Clearly, such a trail is a spanning cycle which is then called a Hamiltonian cycle. If $G$ contains a Hamiltonian cycle, then it is called a Hamiltonian graph.

In contrast (one more) to Eulerian graphs, the problem of recognizing Hamiltonian graphs is very difficult. Until now there are no criteria for characterization of Hamiltonian graphs. Typical results about Hamiltonian graphs require significant number of edges in a graph. However, there are Hamiltonian graphs (like cycles etc.) with small number of edges. Recall that $d(x)$ is the degree of a vertex $x$.

Theorem 6.2.1 (Ore, 1960) If in a simple graph $G=(X, E)$, with $|X|=n \geq 3$, for every pair $x$ and $y$ of disjoint vertices

$$
d(x)+d(y) \geq n,
$$

then $G$ is a Hamiltonian graph.
Proof. By contradiction, assume that $G$ is not Hamiltonian. Hence it is not a complete graph and we can sequentially add edges to $G$ as long as possible before it becomes Hamiltonian. The addition of edges preserves the inequality on vertex degrees. Therefore, without loss of generality, we can assume that $G$ is maximal "non-Hamiltonian" graph. Hence it contains a path $P$ passing (in order from left to right) through all the vertices $x_{1}, x_{2}, \ldots, x_{n}$,

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-141.jpg?height=533&width=1033&top_left_y=1315&top_left_x=365)
Figure 6.2.

see Figure 6.2. Since $G$ is not Hamiltonian, vertices $x_{1}$ and $x_{n}$ are disjoint what implies $d\left(x_{1}\right)+d\left(x_{n}\right) \geq n$. On the other hand, since $x_{1}$ and $x_{n}$ are disjoint, $d\left(x_{1}\right) \leq n-2$ and $d\left(x_{n}\right) \leq$ $n-2$. Consider all $n-3$ internal edges of path $P$. If for each of them the left end is not adjacent to $x_{n}$ or the right end is not adjacent to $x_{1}$, then in total sum of degrees for $x_{1}$ and $x_{n}$ at least $n-3$ edges are missing. Therefore

$$
d\left(x_{1}\right)+d\left(x_{n}\right) \leq(n-2)+(n-2)-(n-3)=n-1
$$

what contradicts the condition of theorem. The last implies that among $n-3$ internal edges of $P$ there exists one, say, $\left(x_{i}, x_{i+1}\right)$ with $x_{i}$ adjacent to $x_{n}$ and $x_{i+1}$ adjacent to $x_{1}$.

Thus the cycle

$$
x_{1}, x_{i+1}, x_{i+2}, \ldots, x_{n}, x_{i}, x_{i-1}, \ldots, x_{1}
$$

is Hamiltonian what completes the proof. $\square$

Corollary 6.2.1 (Dirac, 1952) If in a simple graph $G=(X, E)$, with $|X|=n \geq 3$, the degree of each vertex is at least $n / 2$, then $G$ is Hamiltonian.

Proof. The statement follows directly from the theorem above since $d(x)+d(y) \geq n$ holds for every pair of vertices in $G$. $\square$

In both the theorem and corollary we include the condition $n \geq 3$ to avoid graph $K_{2}$ which is not Hamiltonian but satisfies the degree inequality.

Exercises 6.2.

1. For which values of $n$ and $m$ graphs $K_{n}, K_{m, n}, W_{n}$ are Hamiltonian?
2. Are the prism, cube, and the Petersen graph Hamiltonian?
3. Is the Grözsch graph Hamiltonian (see Figure 5.23)?
4. Which of the complement of prism, cube, Petersen and Grözsch graphs are Hamiltonian?
5. Which of the graphs $\overline{C_{7}}$ and $\overline{C_{8}}$ are Hamiltonian?
6. Construct a list of all Hamiltonian cycles of $K_{4}$ and $K_{5}$.

Computer Projects 6.2. Using an appropriate graph representation, write a program for the following algorithmic problems.

1. Given a graph $G$ with the degree condition as in Theorem 6.2.1, and a path with disjoint ends passing through all the vertices. For the path, find an edge extension to construct a cycle as in Theorem 6.2.1.
2. Given a graph $G$ and a set of edges, verify if the set of edges forms a cycle.
3. Given a graph $G$ and a cycle, find the procedure of extending the cycle as much as possible.
4. Given a complete graph $K_{n}$, generate all Hamiltonian cycles.
5. Given a graph $G$, generate $n$ edges at random and check if they form a cycle.
6. Given a 3-regular graph on 10 vertices, check if it is Hamiltonian.

### 6.3. Network Flows

Networks are anywhere: in traffic, communications, internet, even in our body. It appears that graph theory provides an important mathematica model that allows to find optimal flows in networks.

Recall that a graph in which all edges are ordered pairs (and therefore are called arcs) is called a digraph. A digraph $N=(X, A)$ is called a network, if $X$ is a set of vertices (sometimes called nodes), $A$ is a set of arcs, and to each arc $a \in A$ a non-negative real number $c(a)$ is assigned which is called the capacity of arc $a$. For any vertex $y \in X$, any arc of type $(x, y)$ is called incoming, and every arc of type $(y, z)$ is called outcoming. In $N$, there are two special vertices: $u \in X$, which is not incident to any incoming arc and is called the source, and $v \in X$, which is not incident to any outcoming arc and is called the sink.

A network flow $F$ is an assignment to each arc $a \in A$ a non-negative real number $f(a)$ (called the flow in $a$ ) such that:

1. $f(a) \leq c(a)$;
2. for any vertex $x \in X$, except $u$ and $v$, the following flow conservation law holds: the sum of flows of all incoming arcs equals the sum of flows of all outcoming arcs.

An arc $a \in A$ for which $f(a)=c(a)$ is called saturated; if $f(a)<c(a)$, then arc $a$ is called unsaturated. The value of the network flow is the sum of all flows in arcs of type $(u, x)$; the flow conservation law implies that it equals the sum of all flows in arcs of type $(x, v)$.

Given a network $N=(X, A)$, how can we find a maximum flow? Observe that there is no such concept as the conservation law for the capacities: otherwise we could run the maximum flow right from the source. The answer to this question is closely related to the concept of a cut which is a subset of arcs $S \subseteq A$ that separates the source from the sink. It means that every path from the source $u$ to the sink $v$ contains at least one arc from $S$. The capacity of the cut $S$ is the sum of the capacities of all arcs from $S$. Different cuts have different capacities, and evidently, no flow can exceed the smallest capacity over all cuts. Any cut having the smallest capacity is called the minimum cut.

Theorem 6.3.1 (Max-flow min-cut theorem, Ford and Fulkerson, 1956)
In each network, the value of maximum flow equals the capacity of minimum cut.
Proof. Since the value of maximum flow does not exceed the capacity of minimum cut, we prove that for any given maximum flow there exists a minimum cut having the capacity equal to the value of the flow.

Let $N=(X, A)$ be a network with a maximum flow. Consider a sequence of vertices $u=x_{0} \rightarrow x_{1} \rightarrow x_{2} \rightarrow \cdots \rightarrow x_{k}$ such that either $\left(x_{i}, x_{i+1}\right)$ is an unsaturated arc, or $\left(x_{i+1}, x_{i}\right)$ is an arc with a non-zero flow, $i=0,1, \ldots, k-1$. Denote the set of all such vertices in all such sequences by $Y$. Source $u$ does not have incoming arcs; if all outcoming arcs are saturated, then we are done. If at least one outcoming arc from the source is unsaturated, then we have at least one such sequence and $u \in Y$. Let $Z=X \backslash Y$. We claim that the sink $v \in Z$.

By contradiction, assume $v \in Y$. It means that there exists a sequence $u=x_{0} \rightarrow x_{1} \rightarrow$ $x_{2} \rightarrow \cdots \rightarrow x_{k}=v$ with the property above. Choose a number $\delta>0$ which does not exceed
the value needed to saturate any unsaturated arc of type ( $x_{i}, x_{i+1}$ ) and does not exceed the flow in any arc of the type $\left(x_{i+1}, x_{i}\right)$. We now increase the flow in all arcs of the first type and decrease it in all arcs of the second type by the same value $\delta$. It is clear that the flow conservation law holds, and no capacity is exceeded. Therefore we obtain a flow which is greater than the maximum flow, a contradiction.

Now, let $S$ be the set of all arcs with initial vertex in $Y$ and terminal vertex in $Z$. Evidently, $S$ is a cut. Every arc from $S$ is saturated because otherwise we could move a respective terminal vertex from $Z$ to $Y$. Each arc from $Z$ to $Y$ has the zero flow because otherwise we could move a respective initial vertex from $Z$ to $Y$. This implies that the capacity of cut $S$ equals the value of the given maximum flow what completes the proof. $\square$

The idea of the proof in the theorem above is used in the Ford-Fulkerson algorithm for finding maximum flow in a network. It is illustrated by the example of a network and flow shown in Figure 6.3 with continuation in Figure 6.4.

The pair of numbers $(0,3)$ attached to arc $\left(u, x_{1}\right)$ in the initial flow $F_{0}$ means that the flow in arc $\left(u, x_{1}\right)$ is 0, and the capacity is 3. The same "(flow, capacity)" rule holds for every arc in each flow. As one can see, the initial flow $F_{0}$ is obtained by running one unit of flow along the path

$$
u \rightarrow x_{4} \rightarrow x_{3} \rightarrow x_{1} \rightarrow x_{2} \rightarrow v
$$

and assigning flow 0 in all remaining arcs. It immediately saturates the arc $\left(x_{3}, x_{1}\right)$ as the pair $(1,1)$ shows.

Flow $F_{1}$ is obtained from the flow $F_{0}$ by adding one unit in arc ( $u, x_{1}$ ), subtracting it in backward arc $\left(x_{1}, x_{3}\right)$, and adding it in arc the $\left(x_{3}, v\right)$.

Flow $F_{2}$ is obtained from the flow $F_{1}$ by adding two units along the path

$$
u \rightarrow x_{1} \rightarrow x_{2} \rightarrow v .
$$

Flow $F_{3}$ (see the next figure) is obtained from the flow $F_{2}$ by adding one unit along the path

$$
u \rightarrow x_{4} \rightarrow x_{3} \rightarrow v .
$$

At last maximum flow $F_{4}$ is obtained from the flow $F_{3}$ by adding one unit along the path

$$
u \rightarrow x_{4} \rightarrow x_{3} \rightarrow x_{1} \rightarrow x_{2} \rightarrow v .
$$

We conclude that the flow value equals 6, it is maximum because the arcs $\left(u, x_{1}\right),\left(x_{3}, x_{1}\right)$ and $\left(x_{3}, v\right)$ form a cut with the capacity 6, so it is the minimum cut. At each step we augmented the flow. One can easily see that there is no further flow-augmenting path at this point.

Generally, there are many ways to search for the flow augmenting paths.
Exercises 6.3.

1. In the example in Figure 6.3, add arc ( $x_{4}, x_{2}$ ) with capacity 2 and find the maximum flow.
2. In the example in Figure 6.3, change the capacity of some arcs and find the maximum flow.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-145.jpg?height=1719&width=1018&top_left_y=233&top_left_x=316)
Figure 6.3.

3. In the example in Figure 6.3, change the direction of an arc and find the maximum flow.
4. Given a network with several sources and sinks, suggest a way to reduce the problem

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-146.jpg?height=1212&width=1015&top_left_y=249&top_left_x=316)
Figure 6.4.

to the one with one source and one sink.
5. Given a cube, prism, wheel $W_{7}$, assign direction to every edge (making them arcs) in a way to obtain a network with one source and one sink, assign the capacity to each arc, and find the maximum flow.

Computer Projects 6.3. Write a program for the following algorithmic problems.

1. Given a network, find a flow augmenting path.
2. Transform Petersen graph into a network with one source and one sink and find a maximum flow.
3. Given a network with a flow, determine if the flow is maximum.

## Part II

## Hypergraphs

"There is no Mathematics without generalizations...

Mathematics itself is a pure generalization of the world..."

## Chapter 7

## Basic Hypergraph Concepts

"First was the idea..."

### 7.1. Preliminary Definitions

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-151.jpg?height=596&width=650&top_left_y=1043&top_left_x=554)
Figure 7.1. This is a hypergraph.

An example of a hypergraph is shown in Figure 7.1. The basic idea of the hypergraph concept is to consider such a generalization of a graph in which any subset of a given set may be an edge rather than two-element subsets. In drawing hypergraphs, vertices are points in the plane, edges of size 2 are curves connecting respective vertices (as in graph drawing), and edges of size different from 2 are closed curves separating a respective subset from the rest of vertices, see Figure 7.1.

In what follows we provide basic hypergraph definitions which generalize the respective graph concepts ([6]). Let $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ be a finite set, and let $\mathcal{D}=\left\{D_{1}, D_{2}, \ldots, D_{m}\right\}$ be a family of subsets of $X$. The pair $\mathcal{H}=(X, \mathcal{D})$ is called a hypergraph with vertex set $X$ also denoted by $V(\mathcal{H})$, and with edge set $\mathcal{D}$ also denoted by $\mathcal{D}(\mathcal{H})$. Sometimes, the hypergraph $\mathcal{H}=(X, \mathcal{D})$ is called a set-system.
$|X|=n$ is called the order of the hypergraph, written also as $n$, or $n(\mathcal{H})$. The elements $x_{1}, x_{2}, \ldots, x_{n}$ are called the vertices and the sets $D_{1}, D_{2}, \ldots, D_{m}$ are called the edges (hyperedges). The number of edges is usually denoted by $m$ or $m(\mathcal{H})$. Sometimes we will omit the indices when denoting the vertices and edges if this evidently does not lead to misunderstanding. To include the most general case (it may happen in some algorithms), we assume that the set of vertices $X$ and/or the family $\mathcal{D}$ may be empty. A hypergraph which contains no vertices and no edges is called the empty set. Some edges may also be empty sets. Some edges may be the subsets of some other edges; in this case they are called included. In some cases some edges may coincide; they are then called multiple. A hypergraph is called simple if it contains no included edges. Hence simple hypergraphs do not have empty and multiple edges. Simple hypergraphs are also known as Sperner families.

In a hypergraph, two vertices are said to be adjacent if there is an edge $D \in \mathcal{D}$ that contains both vertices. The adjacent vertices are sometimes called neighbor to each other, and all the neighbors for a given vertex $x$ are called the neighborhood of $x$ in a graph or hypergraph. The neighborhood of $x$ is denoted by $N(x)$. Two edges are said to be adjacent if their intersection is not empty. If a vertex $x_{i} \in X$ belongs to an edge $D_{j} \in \mathcal{D}$, then we say that they are incident to each other. As one can see, as in graph theory, the adjacency is referred to the elements of the same kind (vertices vs vertices, or edges vs edges), while the incidence is referred to the elements of different kind (vertices vs edges).
$\mathcal{D}(x), x \in X$, will denote all the edges containing the vertex $x$. The number $|\mathcal{D}(x)|$ is called the degree of the vertex $x$, the number $\left|D_{i}\right|$ is called the degree (size, cardinality) of the edge $D_{i}$. The maximum degree of the hypergraph $\mathcal{H}$ is denoted by

$$
\Delta(\mathcal{H})=\max _{x \in X}|\mathcal{D}(x)| .
$$

A hypergraph in which all vertices have the same degree $k \geq 0$ is called $k$-regular. A hypergraph in which all edges have the same degree $r \geq 0$ is called $r$-uniform. The rank of a hypergraph $\mathcal{H}$ is

$$
r(\mathcal{H})=\max _{D \in \mathcal{D}}|D| .
$$

An edge of a hypergraph which contains no vertices is called an empty edge. The degree of an empty edge is trivially 0. A vertex of a hypergraph which is incident to no edges is called an isolated vertex. The degree of an isolated vertex is trivially 0. An edge of cardinality 1 is called a singleton (loop), a vertex of degree 1 is called a pendant vertex.

A simple hypergraph $\mathcal{H}$ with $\left|D_{i}\right|=2$ for each $D_{i} \in \mathcal{D}$ is thus a simple graph, maybe with isolated vertices.

Two simple hypergraphs $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ are called isomorphic if there exists a one-to-one correspondence between their vertex sets such that any subset of vertices form an edge in $\mathcal{H}_{1}$ if and only if the corresponding subset of vertices forms an edge in $\mathcal{H}_{2}$.

Hypergraph modeling examples. Hypergraphs can model concepts in different sciences in a much more general setting than graphs do. In addition, they help to find optimal solutions for many new optimization problems. While vertices represent elements of a set, the hyperedges represent properties of different subsets, or, even more generally, arbitrary statements about arbitrary subsets. Let us mention just a few examples.

Mathematics:

- the vertices are natural numbers from 1 to 100; the hyperedges are the subsets of numbers having a common divisor greater than 1 , one subset for each common divisor;
- the vertices are a finite set of points on the real line; the edges are some subsets of the points which form intervals in the ordering of the points, one hyperedge for one such subset;
- the vertices are vertices of a graph; the edges are the subsets forming closed neighborhoods, i. e., one neighborhood plus the vertex itself for each vertex;
- the vertices are vertices of a 3-dimensional polyhedron; each face of the polyhedron forms a hyperedge;
- the vertices are points of a finite geometry; each line of the geometry forms a hyperedge;
- the vertices are points of a block design; each block forms a hyperedge.

Computer science:

- the vertices are computers in a network; the edges are the subsets of computers with devices from different manufacturers, one subset for every manufacturer;
- the vertices are all possible inputs for a chip; the edges are the subsets of inputs which determine some internal defects, one subset for each defect;
- the vertices are files in a data base; the edges are files needed to open for a query, one subset for every query;
- the vertices are records in a relational data base; the edges are the subsets of records for which the values of some attributes are "true", one subset for each attribute.

Genetics:

- the vertices are the elements (A, T, G and C) of a specific DNA sequence; the edges are the subsets of elements representing genes, one edge for a gene;
- the vertices are species; the edges are the subsets of species having common hereditary properties, one edge for a property.

Physics/Chemistry:

- the vertices are the atoms in a molecule; hyperedges of degree 2 correspond to simple covalent bonds, and hyperedges of degree greater than 2 correspond to polycentric bonds;

- the vertices are chemical compounds produced by a chemical factory; every subset of compounds that might explode if combined forms a hyperedge (compare this model with its special case discussed in detail at the beginning of Section 1.2.).

Sociology:

- the vertices are employees in a company; the edges are the subsets of people who have some common interest, one subset for each interest;
- the vertices are all the interests of employees in a company; the edges are the subsets of interests which specific employees have, one edge for every employee.

Healthcare:

- the vertices are illnesses; the edges are the subsets of illnesses which can be treated by some medicines, one hyperedge for each medicine;
- the vertices are medicines; the edges are the subsets of medicines which treat some illnesses, one hyperedge for every illness;
- the vertices are illnesses; the edges are the subsets of illnesses which have some specific symptoms, one hyperedge for each symptom;
- the vertices are symptoms; the edges are the subsets of symptoms characteristic to some illnesses, one hyperedge for each illness.

Broadcasting:

- the vertices are the radio transmitters in a region; the edges are the subsets of transmitters which transmit on the same frequency right now, one subset for each frequency.

Geographical maps:

- the vertices are cities; the edges are the cities which are on the same highway;
- the vertices are street crossings in the city map; the edges are the subsets corresponding to the bus routes, one edge for each bus route.

Exercises 7.1.
For each of the hypergraphs in Figure 7.2:

1. Find the order and the number of edges;
2. Find included edges (if any).
3. Find multiple edges (if any).
4. Is the hypergraph simple?

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-155.jpg?height=388&width=1074&top_left_y=243&top_left_x=409)
Figure 7.2.

5. For each pair of vertices, determine if they are adjacent.
6. For every vertex, find the degree and neighborhood.
7. For each pair of edges, determine if they are adjacent.
8. For each edge, find the size.
9. Find the maximum degree.
10. Is the hypergraph regular?
11. Is the hypergraph uniform?
12. Find the rank.
13. Find isolated and pendant vertices (if any).
14. Find a singleton or an empty edge (if any).
15. Name the vertices and edges, re-draw the hypergraph differently and show an isomorphism.

### 7.2. Incidence and Duality

"Duality of hypergraphs: a look from the inside out..."
The incidence matrix of a hypergraph $\mathcal{H}=(X, \mathcal{D})$ is a matrix $I(\mathcal{H})$ with $n$ rows that represent the vertices and $m$ columns that represent the edges of $\mathcal{H}$ such that

$$
(i, j) \text {-entry }= \begin{cases}1 & \text { if } x_{i} \in D_{j}, \\ 0 & \text { if } x_{i} \notin D_{j} .\end{cases}
$$

An example of the incidence matrix is shown in Figure 7.3. As one can see, in contrast to graphs, any (0,1)-matrix is the incidence matrix of a hypergraph. From this point of view,
the hypergraph theory is the theory of (0,1)-matrices. It also follows that empty edges mean zero columns and isolated vertices mean zero rows in the incidence matrix. Let us agree that if the vertex set of a hypergraph is empty, then the incidence matrix consists only of the row containing the names of the edges; similarly, if the edge set of a hypergraph is empty, then the incidence matrix consists only of the column containing the names of the vertices. If all the vertices are isolated and all the edges are empty sets, then the incidence matrix is totally zeros.

Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph with $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ and $\mathcal{D}=\left\{D_{1}, D_{2}, \ldots\right.$, $\left.D_{m}\right\}$. The dual of the hypergraph $\mathcal{H}$ is a hypergraph $\mathcal{H}^{*}=(Y, Z)$ whose vertex set is $Y=\left\{d_{1}, d_{2}, \ldots, d_{m}\right\}$, and the edge set is defined as follows:

$$
\begin{gathered}
\mathcal{Z}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}, \\
X_{i}=\left\{d_{j}: x_{i} \in D_{j} \text { in } \mathcal{H}\right\} .
\end{gathered}
$$

An example of the dual hypergraph is shown in Figure 7.3. It follows that isolated vertices become empty edges in the dual hypergraph and vice versa. Since we allow isolated vertices and empty edges, the dual hypergraph may be constructed for any hypergraph. Observe that the incidence matrix $I\left(\mathcal{H}^{*}\right)$ is the transpose $I^{*}$ of the incidence matrix $I(\mathcal{H})$. So, the alternative definition of the dual is the following: a hypergraph $\mathcal{H}^{*}$ is the dual of the hypergraph $\mathcal{H}$ if $I\left(\mathcal{H}^{*}\right)=I^{*}(\mathcal{H})$. Evidently, if we transpose a matrix twice, we receive the same matrix, therefore $\left(\mathcal{H}^{*}\right)^{*}=\mathcal{H}$. Following the agreement above this holds even in the case when $X$ or/and $\mathcal{D}$ are empty: the column becomes a row and vice versa. Notice that $\Delta(\mathcal{H})=r\left(\mathcal{H}^{*}\right)$ and the dual of a $k$-regular hypergraph is $k$-uniform. The definition above implies that drawing dual hypergraph is a simple procedure: begin with a drawing of $\mathcal{H}$ ⇒ construct incidence matrix $I(\mathcal{H}) \Rightarrow$ transpose it to obtain $I^{*}(\mathcal{H}) \Rightarrow$ draw dual $\mathcal{H}^{*}$.

For a hypergraph $\mathcal{H}=(X, \mathcal{D})$, we define the bipartite representation of $\mathcal{H}$ to be the bipartite graph $B(\mathcal{H})=(X, \mathcal{D} ; E)$ with the vertex set $X \cup \mathcal{D}$, where $X$ is the left part, $\mathcal{D}$ is the right part, and $E$ is the edge set; vertex $x \in X$ is adjacent to vertex $D \in \mathcal{D}$ in $B(\mathcal{H})$ if and only if vertex $x \in X$ is incident to edge $D \in \mathcal{D}$ in $\mathcal{H}$. In this way, any bipartite graph is a bipartite representation of a hypergraph.

It is seen that $B\left(\mathcal{H}^{*}\right)$ is obtained from $B(\mathcal{H})$ simply by interchanging the right part and the left part while preserving all edges.

The very same hypergraph $\mathcal{H}$, see Figure 7.1, its incidence matrix $I(\mathcal{H})$, dual hypergraph $\mathcal{H}^{*}$ and bipartite representation $B(\mathcal{H})$ are shown in Figure 7.3:

$$
\begin{gathered}
\mathcal{H}=(X, \mathcal{D}), X=\{1,2,3,4,5,6\}, \mathcal{D}=\left\{D_{1}, D_{2}, D_{3}, D_{4}, D_{5}\right\}, \\
D_{1}=\{1\}, D_{2}=\{1,2\}, D_{3}=\{1,2,4\} \\
D_{4}=\{2,3,5\}, D_{5}=\{3,4,5\} .
\end{gathered}
$$

Notice that edge $D_{1}$ with $\left|D_{1}\right|=1$ (singleton) is drawn as the circle containing only vertex $x_{1}$. So, loops from graph theory become singletons and are drawn differently. An empty edge is drawn as a circle containing no vertices. These rules are used throughout the book unless stated otherwise. In $\mathcal{H}$, edge $D_{1}$ is a singleton, vertex 6 is isolated, vertices 3 and 5 are incident to the same edges, edge $D_{2}$ is included in edge $D_{3}$; in $I(\mathcal{H})$, column $D_{1}$ contains one 1, row 6 is a zero row, rows 3 and 5 are identical; in $\mathcal{H}^{*}$, vertex $d_{1}$ is of degree

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-157.jpg?height=1328&width=1212&top_left_y=269&top_left_x=293)
Figure 7.3. Example of a hypergraph $\mathcal{H}$, its incidence matrix $I(\mathcal{H})$, dual $\mathcal{H}^{*}$ and bipartite representation $B(\mathcal{H})([6])$.

1, edge 6 is empty, edges 3 and 5 are multiple; in $B(\mathcal{H})$, vertex $D_{1}$ is pendant, vertex 6 is isolated, vertices 3 and 5 have the same neighbors and so on. One can see how the names, degrees, adjacency and incidence, etc. in $\mathcal{H}$ are looking in incidence matrix $I(\mathcal{H})$, dual hypergraph $\mathcal{H}^{*}$ and bipartite representation $B(\mathcal{H})$.

Every picture of a hypergraph is already an isomorphism between the incidence matrix and the points and curves in the plane. In this sense, Figure 7.3 contains four different pictures of the same structure defined as the hypergraph $\mathcal{H}$. One can easily check that incidence matrix of $\mathcal{H}^{*}$ is the transpose of the incidence matrix of $\mathcal{H}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-158.jpg?height=381&width=1134&top_left_y=246&top_left_x=331)
Figure 7.4.

Proposition 7.2.1 (Degree equality) For a hypergraph $\mathcal{H}=(X, \mathcal{D})$, the sum of all vertex degrees equals the sum of all edge cardinalities, i.e.,

$$
\sum_{i=1}^{n}\left|\mathcal{D}\left(x_{i}\right)\right|=\sum_{j=1}^{m}\left|D_{j}\right| .
$$

Proof. Consider the bipartite representation of $\mathcal{H}$, i.e. the bipartite graph $B(\mathcal{H})=$ $(X, \mathcal{D} ; E)$. If we sum the degrees of vertices in the first part, we obtain the left side of the equality; if we sum the degrees of vertices in the second part, we obtain the right side of the equality. Evidently, they coincide because both are equal to the number of edges in $B(\mathcal{H})$. $\square$

As one can see, formula (7.1) is a direct generalization of formula (1.1) which was obtained for graphs. For example in Figure 7.3 it gives:

$$
3+3+2+2+2+0=12=1+2+3+3+3 .
$$

It is important to mention that any graph as a special case of hypergraphs, has its dual, which is not necessarily a graph. As we shall see, the duality of hypergraphs is a powerful tool; we are not able to use it if we are restricted by graphs only.

Figure 7.4 shows an example of a graph $G$ such that the dual $G^{*}$ is a hypergraph. Notice that pendant vertex 3 in $G$ becomes loop 3 in $G^{*}$, vertex 2 of degree 3 becomes edge 2 of cardinality 3 and vice versa. In fact, these two different drawings represent two different pictures of the same structure taken from different points of view. Points, lines and curves in the plane are just simplest tools to visualize it.

Thus, drawings, (0-1)-matrices and bipartite graphs may be used to identify hypergraphs. However, it would be wrong to study only the matrices and bipartite graphs instead of hypergraphs. To see this, the reader should try to formulate the notion of the chromatic number of a graph (a simple special case of a hypergraph) in the language of matrices or bipartite graphs. It depends on the problem however, and for simplicity it is sometimes convenient to use matrices and/or bipartite graphs.

Edge lists. Besides incidence matrices and any structure suitable for bipartite graphs, there is one more simple and convenient way to store hypergraphs in computer memory. It represents the list of all edges and therefore is called the edge list. For hypergraph $\mathcal{H}$ in

Figure 7.3, the edge list is:

$$
L=\{\{1\},\{1,2\},\{1,2,4\},\{2,3,5\},\{3,4,5\}\} .
$$

The edge list should be accompanied by the indication if there are isolated vertices; otherwise they might be lost. In the example above, vertex 6 is isolated.

In computer memory, the edge list is usually represented by a one-dimensional array (the list itself) and one additional two-dimensional array indicating the beginning and the end for each edge.

Adjacency matrix. An $n \times n$ matrix $A=\left(a_{i j}\right)$ is an adjacency matrix of a hypergraph $\mathcal{H}$, denoted by $A(\mathcal{H})$, if

$$
a_{i j}= \begin{cases}1 & \text { if } \mathcal{D}\left(x_{i}\right) \cap \mathcal{D}\left(x_{j}\right) \neq \emptyset \\ 0 & \text { otherwise. }\end{cases}
$$

This definition is the same as for graphs, see Section 1.3. However, in contrast to graphs, it is not possible to draw a hypergraph from its adjacency matrix in a unique way. In other words, there is no one-to-one correspondence between hypergraphs and their adjacency matrices. That is why the adjacency matrices have a limited use in hypergraph theory.

Exercises 7.2.

1. For hypergraphs $\mathcal{H}$ and $\mathcal{H}^{*}$ in Figure 7.3, find the neighborhood of each vertex.
2. For hypergraphs $\mathcal{H}$ and $\mathcal{H}^{*}$ in Figure 7.3, find the degree of each vertex and the cardinality of each edge.
3. Find the rank of $\mathcal{H}$ and $\mathcal{H}^{*}$ in Figure 7.3.
4. Write down an arbitrary $(0,1)$-matrix and draw the respective hypergraph and its dual.
5. Write down an arbitrary edge list and draw the respective hypergraph and its dual.
6. Apply degree equality (7.1) to graph $G$ and its dual $G^{*}$ in Figure 7.4.
7. Construct the edge list for graph $G$ and its dual $G^{*}$ in Figure 7.4.
8. Construct bipartite representations $B(B(\mathcal{H}))$ (Figure 7.3), and $B(G)$ (Figure 7.4).
9. Construct the dual of: $E_{n}, K_{n}, P_{n}, C_{n}$, and $W_{n}, n=3,4,5,6,7$.
10. Construct the dual of cube, prism and Petersen graph.

Computer Projects 7.2. Using an appropriate hypergraph representation, write a program for the following algorithmic problems.

1. Given the incidence matrix of a hypergraph, construct the edge list.
2. Given the incidence matrix of a hypergraph, draw the hypergraph on the screen.

3. Given the incidence matrix of a hypergraph, construct the adjacency matrix.
4. Given the edge list of a hypergraph, construct the adjacency matrix.
5. Given the edge list of a hypergraph, construct the edge list of the dual.
6. Given a hypergraph $\mathcal{H}$, find its rank.
7. Given a hypergraph $\mathcal{H}$, construct bipartite representation $B(\mathcal{H})$.

### 7.3. Basic Hypergraph Classes

Complete hypergraphs. For $0 \leq r \leq n$, we define the complete $r$-uniform hypergraph to be the simple hypergraph $K_{n}^{r}=(X, \mathcal{D})$ such that $|X|=n$ and $\mathcal{D}\left(K_{n}^{r}\right)$ coincides with all the $r$-subsets of $X$. Thus a complete graph on $n$ vertices is a complete 2-uniform hypergraph $K_{n}^{2}$ also denoted by $K_{n}$. The complete $r$-uniform hypergraph and the family of its edges both are denoted by $K_{n}^{r}$, i.e. $K_{n}^{r}=\left(X, K_{n}^{r}\right)$, where $|X|=n$.

All five complete hypergraphs on four vertices are shown in Figure 7.5. For $K_{4}^{0}$, we draw an empty edge to emphasize the empty set. As one can see, the total number of all edges is $1+4+6+4+1=16=2^{4}=2^{n}$ what is the number of all subsets on the set of four vertices. This holds for any $n \geq 0$ and all $r$ such that $0 \leq r \leq n$. It is important to notice that the number of edges in $K_{n}^{r}$ is:

$$
\left|\mathcal{D}\left(K_{n}^{r}\right)\right|=\binom{n}{r}=\frac{n!}{r!(n-r)!}=\frac{n(n-1)(n-2) \cdots(n-r+1)}{r!} .
$$

For example, in $K_{4}^{3}$ we have

$$
\left|\mathcal{D}\left(K_{4}^{3}\right)\right|=\binom{4}{3}=\frac{4 \cdot 3 \cdot 2}{1 \cdot 2 \cdot 3}=4 .
$$

Among all complete hypergraphs on four vertices, only $K_{4}^{2}$ is a simple graph. At last, observe that all complete hypergraphs are $r$-uniform and $\binom{n-1}{r-1}$-regular hypergraphs.

Paths and Cycles. In a hypergraph $\mathcal{H}=(X, \mathcal{D})$, an alternating sequence

$$
\mu=x_{0} D_{0} x_{1} D_{1} x_{2} \ldots x_{t-1} D_{t-1} x_{t}
$$

of distinct vertices $x_{0}, x_{1}, x_{2}, \ldots, x_{t-1}$ and distinct edges $D_{0}, D_{1}, D_{2}, \ldots, D_{t-1}$ satisfying $x_{i}, x_{i+1} \in D_{i}, i=0,1, \ldots, t-1$, is called a path connecting the vertices $x_{0}$ and $x_{t}$, or, equivalently, $\left(x_{0}, x_{t}\right)$-path; it is called a cycle if $x_{t}=x_{0}$. The value of $t$ is called the length of the path/cycle respectively.

For example, in Figure 7.3, the sequence $\mu_{1}=1 D_{2} 2 D_{4} 3 D_{5} 5$ is a (1,5)-path of length 3, and the sequence $\mu_{2}=1 D_{2} 2 D_{4} 3 D_{5} 4 D_{3} 1$ is a cycle of length 4.

Connected hypergraphs. The hypergraph $\mathcal{H}=(X, \mathcal{D})$ is called connected if for any pair of its vertices there is a path connecting them. If $\mathcal{H}$ is not connected, then it consists of two or more connected components each of which is a connected hypergraph. An isolated vertex, a vertex incident to loops only and an empty edge are also considered connected components. Therefore, $\mathcal{H}, \mathcal{H}^{*}$ and $B(\mathcal{H})$ have the same number of connected components.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-161.jpg?height=919&width=1126&top_left_y=256&top_left_x=308)
Figure 7.5. All complete hypergraphs on four vertices.

In Figure 7.5, the hypergraph $K_{4}^{0}$ has 5 connected components, $K_{4}^{1}$ has 4 connected components, $K_{4}^{2}, K_{4}^{3}$ and $K_{4}^{4}$ are connected. If we look at Figure 7.5 as one hypergraph, then it is a disconnected hypergraph having 12 connected components.

Bipartite hypergraphs. A hypergraph $\mathcal{H}=(X, \mathcal{D})$ is called bipartite if its vertex set $X$ can be partitioned into two disjoint sets $X_{1}$ and $X_{2}$ (called parts) in such a way that each hyperedge of cardinality $\geq 2$ contains vertices from both parts. It means that there is no such hyperedge inside $X_{1}$ and there is no such hyperedge inside $X_{2}$. In other words, the vertices of a bipartite hypergraph can be colored with two colors in such a way that no hyperedge of size $\geq 2$ is monochromatic. Bipartite hypergraphs are also called bi-chromatic or 2-colorable hypergraphs. As it follows from the definition, singletons and empty edges play no role in bipartition; they are usually ignored when discussing the properties of 2-colorable hypergraphs.

A complete $r$-partite hypergraph is an $r$-uniform hypergraph $\mathcal{H}=(X, \mathcal{D})$ such that set $X$ can be partitioned into $r$ non-empty parts, each edge contains precisely one vertex from each part, and all such subsets form $\mathcal{D}$. The complete $r$-partite hypergraphs are usually denoted by $K_{n_{1}, n_{2}, \ldots, n_{r}}^{r}$ where $n_{i}$ is the number of vertices in part $X_{i}$. Bipartite hypergraphs generalize bipartite graphs.

Isomorphic hypergraphs. Two (not necessarily simple) hypergraphs $\mathcal{H}=(X, \mathcal{D})$ and $\mathcal{H}^{\prime}=\left(X^{\prime}, \mathcal{D}^{\prime}\right)$ are called isomorphic, written $\mathcal{H} \cong \mathcal{H}^{\prime}$, if there is a one-to-one correspondence between the sets $X$ and $X^{\prime}$ and a one-to-one correspondence between the sets $\mathcal{D}$ and $\mathcal{D}^{\prime}$ such that for every vertex $x \in X$ and for every edge $D \in \mathcal{D}$ we have that $x \in D$ if and only
if for the corresponding vertex $x^{\prime} \in X^{\prime}$ and the corresponding edge $D^{\prime} \in \mathcal{D}^{\prime}$ the inclusion $x^{\prime} \in D^{\prime}$ holds. Using graph terminology, one could say that two hypergraphs are isomorphic if and only if their bipartite representations are isomorphic as graphs (preserving respective bipartition).

Exercises 7.3.

1. Draw all complete hypergraphs on 0, 1, 2, 3, 5, 6 and 7 vertices.
2. Draw the duals to all complete hypergraphs on four vertices, Figure 7.5.
3. Write down the incidence matrix of: $K_{4}^{3}, K_{5}^{3}, K_{5}^{1}, K_{6}^{5}$, and $K_{7}^{4}$.
4. Write down the edge list of $K_{4}^{3}, K_{5}^{3}, K_{5}^{1}, K_{6}^{5}$, and $K_{7}^{4}$.
5. Draw $K_{1,2,3}^{3}$ and write down the incidence matrix.
6. Explain when isomorphic hypergraphs have identical incidence matrix.

Computer Projects 7.3. Using an appropriate hypergraph representation, write a program for the following algorithmic problems.

1. Given a hypergraph $\mathcal{H}$, determine if it is a complete $r$-uniform hypergraph.
2. For $n_{1}, n_{2}, n_{3} \geq 1$, generate an edge list of $K_{n_{1}, n_{2}, n_{3}}^{3}$.
3. Given a hypergraph $\mathcal{H}$, determine if it is connected.
4. Given a bipartite graph $B(\mathcal{H})$, draw $\mathcal{H}$ and construct the incidence matrix.
5. \* Given a 3 -uniform hypergraph, recognize if it is bipartite.

### 7.4. Basic Hypergraph Operations

As in graph theory, there are a few basic operations which allow to obtain one hypergraph from another. They are helpful in proofs of many theorems and useful in many algorithms for solving optimization problems on hypergraphs.

Strong deletion of a vertex. Let us have a hypergraph $\mathcal{H}=(X, \mathcal{D})$ and a vertex $x \in X$, see Figure 7.6. A strong deletion of $x$ from $\mathcal{H}$ is the removing of all the edges containing $x$ from $\mathcal{D}$ and removing of $x$ from $X$.

Recall that $\mathcal{D}(x)$ denotes the set of edges containing vertex $x$ in hypergraph $\mathcal{H}$. If $X_{1}=X-\{x\}$, and $\mathcal{D}_{1}=\mathcal{D}-\mathcal{D}(x)$, then strong deletion of $x$ from $\mathcal{D}$ results in obtaining the hypergraph $\mathcal{H}_{1}=\left(X_{1}, \mathcal{D}_{1}\right)$. We write this operation as $\mathcal{H}_{1}=\mathcal{H}-x$. In $\mathcal{H}_{1}$, we can choose and strongly delete another vertex to obtain a hypergraph $\mathcal{H}_{2}$ and so on; sequential strong deletion of vertices results in a sequence of hypergraphs. As in graphs, this approach is common and very helpful in developing of many algorithms and proving of a series of theorems by using mathematical induction.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-163.jpg?height=370&width=1012&top_left_y=238&top_left_x=391)
Figure 7.6. Strong deletion of $x$ from $\mathcal{H}$.

Sometimes there is a need to strongly delete an entire subset of vertices; it is equivalent to a sequential strong deletion of the respective vertices in any order. We will see that hypergraphs obtained by strong deletions of vertices play a crucial role in the theory. Such deletions of vertices are called "strong" because the vertices are removed from a hypergraph along with all incident edges.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-163.jpg?height=373&width=1023&top_left_y=1046&top_left_x=391)
Figure 7.7. Weak deletion of $x$ from $\mathcal{H}$.

Weak deletion of a vertex. As in the previous case, let us have a hypergraph $\mathcal{H}=$ $(X, \mathcal{D})$ and a vertex $x \in X$. A weak deletion of $x$ from $\mathcal{H}$ is the removing of $x$ from set $X$ and from each hyperedge of $\mathcal{D}(x)$. If the very same vertex $x$ is weakly deleted from $\mathcal{H}$, see Figure 7.7, we obtain a different hypergraph $\mathcal{H}_{1}$. We also write this operation as $\mathcal{H}_{1}=\mathcal{H}-x$ with understanding that the meaning of deletion "weak".

In our example, see Figure 7.7, the loop at $x$ becomes an empty edge, the edge of size 2 incident to $x$ becomes a loop, and the edge of size 3 becomes an edge of size 2 connecting the remaining two vertices. Recall that in hypergraph theory, it is common to draw edges of size two as line segments and not as closed curves.

In graph theory, loops were curves connecting vertex to itself; in hypergraph theory, the loops become singletons drawn as circles; this reflects the basic idea of hypergraphs as collections of sets rather than lines and curves.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-164.jpg?height=451&width=1072&top_left_y=228&top_left_x=352)
Figure 7.8. Strong deletion of hyperedge $D$ from $\mathcal{H}$.

Strong deletion of a hyperedge. It is removing of a hyperedge from the list of edges and then weak deletion of all of its vertices from the vertex set. Strong deletion of the edge $D$ is shown in Figure 7.8. In such case we write $\mathcal{H}_{1}=\mathcal{H}-D$ and indicate that the deletion is strong.

Weak deletion of a hyperedge. It is the simplest operation of deletion in a hypergraph: we just remove a hyperedge from the list of edges. All the rest remains unchanged. Weak deletion of an empty edge is called clearing. In many algorithms clearings usually accompany weak deletions of the vertices. Figure 7.9 shows an example of weak deletion of the same edge $D$ from the same hypergraph $\mathcal{H}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-164.jpg?height=451&width=1181&top_left_y=1271&top_left_x=303)
Figure 7.9 Weak deletion of hyperedge $D$ from $\mathcal{H}$.

Important observation. Let us compare the deletions. In the incidence matrix, strong deletion of a vertex corresponds to removing of the respective row and further removing of all columns that have 1 at intersection with the row. In turn, the weak deletion of a vertex corresponds to just removing of the respective row. As we know, transposition of the incidence matrix results in the incidence matrix of the dual hypergraph. Rows become the columns and columns become the rows. Respectively, vertices become the edges, and edges become the vertices. So, removing of rows corresponds to removing of the columns in the transposed matrix, or, equivalently, deletion of vertices corresponds to the deletions of edges in the dual. In other words, the strong (weak) deletion of any vertex in a hypergraph is nothing else than the strong (weak) deletion of the respective edge in the dual. Comparing weak and strong deletions, notice that only for isolated vertices, as for empty edges, strong
and weak deletions are equivalent.
The hypergraph $\mathcal{H}$, see Figures 7.6 and 7.7, and hypergraph $\mathcal{H}$, see Figures 7.8 and 7.9, are dual to each other. Observe now that strong deletion of vertex $x$ in Figure 7.6 is the same as the strong deletion of the edge $D$ in Figure 7.8. Similarly, weak deletion of the vertex $x$ in Figure 7.7 is nothing else than the weak deletion of the hyperedge $D$ in Figure 7.9. Consequently, the hypergraph $\mathcal{H}_{1}$ in Figure 7.6 and hypergraph $\mathcal{H}_{1}$ in Figure 7.8 are dual to each other. In the same way, $\mathcal{H}_{1}$ in Figure 7.7 and $\mathcal{H}_{1}$ in Figure 7.9 are dual to each other, too.

In graph theory, such fundamental concept as duality is missing because dual graphs are not properly graphs, they are hypergraphs. This is the first (but not last) case when the duality helps in understanding, simplifying and unifying many combinatorial relations.

Contraction of a hyperedge. Let $D$ be an edge in a hypergraph $\mathcal{H}=(X, \mathcal{D})$. A contraction of the edge $D$ consists in the following two steps, see an example in Figure 7.10:

1. weakly delete $D$ from $\mathcal{H}$;
2. replace all vertices of $D$ by one vertex belonging to each $D^{\prime} \in \mathcal{D}$ such that $D \cap D^{\prime} \neq \emptyset$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-165.jpg?height=451&width=1139&top_left_y=1036&top_left_x=300)
Figure 7.10. Contraction of a hyperedge.

Contraction of an edge may significantly change the structure of a hypergraph. For example, notice that in Figure 7.10, $\mathcal{H}_{1}$ is isomorphic to its dual $\mathcal{H}_{1}^{*}$, while $\mathcal{H}$ is not isomorphic to $\mathcal{H}^{*}$. As in graph theory, sequential application of deletions to decompose a hypergraph and then to reconstruct it in inverse order is widely used in many algorithms.

Exercises 7.4. For hypergraph $\mathcal{H}$ in Figure 7.11, do the following:

1. Find all distinct (1,13)-paths.
2. Find the shortest (1,6)-path.
3. Find the shortest and the longest cycle.
4. Determine if $\mathcal{H}$ is bipartite.
5. Strongly delete vertices 1, 2, 3, and 7.
6. Weakly delete vertices 1, 2, 3, and 7.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-166.jpg?height=1087&width=1113&top_left_y=274&top_left_x=326)
Figure 7.11.

7. Strongly delete edges $\{7,11,12\}$ and $\{3,5,9\}$.
8. Weakly delete edges \{7,11,12\} and \{3,5,9\}.
9. Contract edges $\{7,11,12\}$ and $\{3,5,9\}$.
10. Construct the dual hypergraph $\mathcal{H}^{*}$ and compare it with Petersen graph.
11. Construct the dual hypergraph to every hypergraph obtained in 5, 6, 7, 8, and 9.

Computer Projects 7.4. For hypergraph $\mathcal{H}$ in Figure 7.11, using an appropriate hypergraph representation, write a program for the following algorithmic problems.

1. Sequentially strongly delete vertices in an order determined by a user; draw each intermediate step on the screen.
2. Sequentially weakly delete vertices in an order determined by a user; draw each intermediate step on the screen.

3. Sequentially strongly delete edges in an order determined by a user; draw each intermediate step on the screen.
4. Sequentially weakly delete edges in an order determined by a user; draw each intermediate step on the screen.
5. Sequentially contract hyperedges in an order determined by a user; draw each intermediate step on the screen.

### 7.5. Subhypergraphs

By strong and weak deletions of vertices and edges from a hypergraph one can obtain different types of subhypergraphs. As we shall see, many concepts in this section (as in the others, too) have their original ideas coming from Graph Theory.

Subhypergraphs. Let us have a hypergraph $\mathcal{H}=(X, \mathcal{D})$. Any hypergraph $\mathcal{H}^{\prime}=$ $\left(X^{\prime}, \mathcal{D}^{\prime}\right)$ such that $X^{\prime} \subseteq X$, and $\mathcal{D}^{\prime} \subseteq \mathcal{D}$ is called a subhypergraph of $\mathcal{H}$. In such case, we write $\mathcal{H}^{\prime} \subseteq \mathcal{H}$. Evidently, $\mathcal{H}^{\prime}$ can be obtained from $\mathcal{H}$ by strong deletion of the vertices from set $X-X^{\prime}$ (sequentially in any order, or at once) and further weak deletion of the remaining edges from $\mathcal{D}-\mathcal{D}^{\prime}$ (sequentially in any order, or at once). In Figure 7.12, both $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ are subhypergraphs of $\mathcal{H}: \mathcal{H}_{1}$ is obtained by strong deletion of vertex 5 and 1, and $\mathcal{H}_{2}$ is obtained by strong deletion of vertex 4 and weak deletion of edge \{1,2,5\}. Notice that the order in which the vertices and edges are deleted is not important.

Induced subhypergraphs. A hypergraph $\mathcal{H}^{\prime}=\left(X^{\prime}, \mathcal{D}^{\prime}\right)$ is called an induced subhypergraph of a hypergraph $\mathcal{H}=(X, \mathcal{D})$ if $X^{\prime} \subseteq X$ and all edges of $\mathcal{H}$ completely contained in $X^{\prime}$ form the family $\mathcal{D}^{\prime}$. Sometimes we say that $\mathcal{H}^{\prime}$ is a subhypergraph induced by $X^{\prime}$. Induced subhypergraph $\mathcal{H}^{\prime}$ may be obtained from $\mathcal{H}$ by strong deletion of vertices $X-X^{\prime}$ (sequentially in any order, or at once). Induced subhypergraph is a special case of subhypergraph. A subhypergraph is not induced if at least one hyperedge of $\mathcal{H}$ being a subset of $X^{\prime}$, is missing. In a hypergraph $\mathcal{H}$, it is convenient to denote a subhypergraph induced by a set $Y \subseteq X$ by $\mathcal{H}_{Y}$. In Figure 7.12, if $Y=\{2,3,4\}$, then $\mathcal{H}_{1}=\mathcal{H}_{Y}$.

Partial subhypergraph. For a hypergraph $\mathcal{H}=(X, \mathcal{D})$, any subhypergraph $\mathcal{H}^{\prime} \subseteq \mathcal{H}$ such that $\mathcal{H}^{\prime}=\left(X, \mathcal{D}^{\prime}\right)$ is called a partial subhypergraph. Thus partial subhypergraphs have the same vertex set as the hypergraph itself and may be obtained only by weak deletions of edges. Any spanning subgraph of a graph is a partial subhypergraph.

Stable (independent) sets. Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph. A subset of vertices which contains no edge of $\mathcal{H}$ is called the stable set, or the independent set. Independent set of vertices induces an empty subhypergraph. There are maximal by inclusion and not maximal by inclusion stable sets. The largest size of a stable set over all maximal by inclusion stable sets is called the stability (independence) number, denoted by $\alpha(\mathcal{H})$. For any hypergraph $\mathcal{H}$ with not all vertices singletons, $1 \leq \alpha(\mathcal{H}) \leq|X|$. For a hypergraph $\mathcal{H}$ without singletons, if we weakly delete all vertices of a stable set, then in the obtained subhypergraph no edge is empty.

For hypergraph $\mathcal{H}$, see Figure 7.12, vertices 2 and 5 form a maximal by inclusion stable set, but it is not a maximum stable set. Vertices 1,2 and 3 form a maximum independent set, so $\alpha(\mathcal{H})=3$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-168.jpg?height=414&width=1168&top_left_y=217&top_left_x=295)
Figure 7.12. Hypergraph $\mathcal{H}$, induced subhypergraph $\mathcal{H}_{1}$ and subhypergraph $\mathcal{H}_{2}$.

Strongly independent (stable) sets. For a hypergraph $\mathcal{H}=(X, \mathcal{D})$, a subset of vertices $S \subseteq X$ is called a strongly independent (stable) set if $|S \cap D| \leq 1$ for every hyperedge $D \in$ $\mathcal{D}$. The cardinality of a maximum strongly independent set is denoted by $\bar{\alpha}(\mathcal{H})$. Evidently, for a graph $G, \alpha(G)=\bar{\alpha}(G)$.

Transversals. A set $T \subseteq X$ is called a transversal of a hypergraph $\mathcal{H}=(X, \mathcal{D})$ if $|T \cap D| \geq 1$ for every edge $D \in \mathcal{D}$. The cardinality of a minimum transversal is denoted by $\tau(\mathcal{H})$. Following the definition, every set $S=X-T$ is an independent set. Therefore we have the following equality:

$$
\alpha(\mathcal{H})+\tau(\mathcal{H})=|X| .
$$

In Figure 7.12, vertices 4 and 5 form a minimum transversal, so $\tau=2$. The complementary set of vertices 1, 2, and 3 as we have seen, is an independent set and $\alpha(\mathcal{H})=3$. Evidently, $\alpha(\mathcal{H})+\tau(\mathcal{H})=3+2=5=|X|$.

If we strongly delete from a hypergraph the vertices of a transversal, then we obtain a hypergraph without edges, i.e. an empty hypergraph. Transversals are sometimes called blocking sets, or node-covers.

Matchings. In a hypergraph $\mathcal{H}$, a set of edges which pairwise have no vertices in common is called a matching. A perfect matching is a matching which contains every vertex of a hypergraph. The maximum size of a matching (over all matchings) is denoted by $\mathcal{V}(\mathcal{H})$. Any matching of $\mathcal{H}$ is a strongly independent set of vertices in the dual $\mathcal{H}^{*}$. Therefore, $\nu(\mathcal{H})=\bar{\alpha}\left(\mathcal{H}^{*}\right)$. Since any matching is a set of pairwise non-intersecting edges, any transversal must have at least one vertex from each edge of the matching. This fact implies that for any hypergraph $\mathcal{H}$,

$$
\tau(\mathcal{H}) \geq v(\mathcal{H}) .
$$

We say that $\mathcal{H}$ satisfies the König property if

$$
\tau(\mathcal{H})=v(\mathcal{H}) .
$$

In hypergraph $\mathcal{H}$, see Figure 7.12, edge \{2,3,5\} forms a maximal by inclusion matching; however, edges $\{1,2,5\}$ and $\{3,4\}$ form a perfect matching, so $\mathcal{V}(\mathcal{H})=2$. Any transversal of $\mathcal{H}$ must have at least one vertex from each of the edges \{1,2,5\} and \{3,4\}, so $\tau(\mathcal{H}) \geq 2=v(\mathcal{H})$. Since $\tau(\mathcal{H})=v(\mathcal{H}), \mathcal{H}$ satisfies the König property. Notice that if a
transversal contains $\mathcal{V}(\mathcal{H})$ vertices, then it is a minimum transversal; similarly, if a matching contains $\tau(\mathcal{H})$ hyperedges, then it is a maximum matching. Inequality (7.2) is very important in combinatorial optimization because almost all problems in this area may be re-formulated in terms of $\tau$ or $\nu$ for some hypergraph. The König property for hypergraphs has its roots in Theorem 2.4.3 for bipartite graphs.

Coverings. For a hypergraph $\mathcal{H}=(X, \mathcal{D})$, a subset of edges $\mathcal{D}^{\prime}$ is called a covering if the union of all edges from $\mathcal{D}^{\prime}$ coincides with $X$. We say that $\mathcal{D}^{\prime}$ covers $\mathcal{H}$. The minimum number of edges in a covering is denoted by $\rho(\mathcal{H})$. One can see that each covering of $\mathcal{H}$ is a transversal in $\mathcal{H}^{*}$ and vice versa, therefore

$$
\rho(\mathcal{H})=\tau\left(\mathcal{H}^{*}\right) .
$$

A hypergraph $\mathcal{H}$ has the dual König property if $\rho(\mathcal{H})=\bar{\alpha}(\mathcal{H})$.
For hypergraph $\mathcal{H}$ in Figure 7.12, edges $\{1,2,5\}$ and $\{3,4\}$ form a minimum covering, so $\rho(\mathcal{H})=2$. Vertices 1 and 3 form a maximum strongly independent set, so $\bar{\alpha}(\mathcal{H})=2$. Since $\rho(\mathcal{H})=\bar{\alpha}(\mathcal{H})$, hypergraph $\mathcal{H}$ satisfies the dual König property.

Graph $C_{5}$ is an example of a hypergraph with $\tau=3>2=\nu$ and $\rho=3>\bar{\alpha}=\alpha=2$. Therefore, $C_{5}$ does not satisfy König property, neither it satisfies the dual König property.

Hypergraph minors. A hypergraph $\mathcal{H}^{\prime}$ is a minor of a hypergraph $\mathcal{H}$ if it can be obtained from $\mathcal{H}$ by a sequence of weak or strong vertex or edge deletions, identification of two vertices of a hyperedge and the replacement of a hyperedge by any subset of vertices.

Exercises 7.5. For hypergraph $\mathcal{H}$ in Figure 7.11, do the following:

1. Draw subhypergraph $\mathcal{H}^{\prime}=\left(X^{\prime}, \mathcal{D}^{\prime}\right)$, where $X^{\prime}=\{1,2,3,4,5,7,8\}$ and $\mathcal{D}^{\prime}=$ \{\{1,3,7\}, \{2,4,8\}\}.
2. Draw subhypergraph $\mathcal{H}^{\prime}$ induced by vertex subset $X^{\prime}=\{1,2,3,4,5,7,8\}$.
3. Draw any partial subhypergraph.
4. Find a maximal independent set.
5. Find $\alpha(\mathcal{H})$.
6. Find a maximum strongly independent set.
7. Find a minimal transversal.
8. Find $\tau(\mathcal{H})$.
9. Find a maximal matching.
10. Find $v(\mathcal{H})$.
11. Find a $\rho(\mathcal{H})$ and respective minimum covering.
12. Draw a hypergraph minor of $\mathcal{H}$ on five vertices which is not a subhypergraph of $\mathcal{H}$.

Computer Projects 7.5. For hypergraph $\mathcal{H}$ in Figure 7.11, write a program for the following algorithmic problems.

1. Draw a subhypergraph induced by a set of vertices determined by the user.
2. Generate all maximal independent sets.
3. Generate all minimal transversals.
4. Find $\alpha(\mathcal{H})$.
5. Find $\tau(\mathcal{H})$.
6. Find $\mathcal{v}(\mathcal{H})$.
7. Find $\rho(\mathcal{H})$.
8. Find a minor of $\mathcal{H}$.

### 7.6. Conformality and Helly Property

Many properties of hypergraphs can be modeled and explained using the "language of graphs".

The line graph $L(\mathcal{H})$ of a hypergraph $\mathcal{H}=(X, \mathcal{D})$ (sometimes called the intersection graph of a family $\mathcal{D}$ ) is the graph with set $\mathcal{D}$ as the vertex set and two vertices are adjacent if and only if the respective edges intersect:

$$
L(\mathcal{H})=(\mathcal{D}, \mathcal{E}), \text { where }\left(D_{i}, D_{j}\right) \in \mathcal{E} \Leftrightarrow D_{i} \cap D_{j} \neq \emptyset .
$$

The 2-section $(\mathcal{H})_{2}$ of a hypergraph $\mathcal{H}=(X, \mathcal{D})$ is the graph with the same vertex set $X$, and two vertices are adjacent if and only if they both belong to an edge:

$$
(\mathcal{H})_{2}=(X, \mathcal{E}) \text { where }\left\{x_{i}, x_{j}\right\} \in \mathcal{E} \Leftrightarrow \mathcal{D}\left(x_{i}\right) \cap \mathcal{D}\left(x_{j}\right) \neq \mathbb{O} \text {. }
$$

Theorem 7.6.1 For any hypergraph $\mathcal{H}$,

$$
(\mathcal{H})_{2}=L\left(\mathcal{H}^{*}\right) .
$$

Proof. Indeed, graph $(\mathcal{H})_{2}$ has vertex set $X$ which becomes the edge set in $\mathcal{H}^{*}$, what in turn, becomes the vertex set for $L\left(\mathcal{H}^{*}\right)$; so they have the same vertex set. Two vertices in $(\mathcal{H})_{2}$ are adjacent if and only if they have an edge in common in $\mathcal{H}$, what occurs if and only if the respective edges intersect in the dual hypergraph $\mathcal{H}^{*}$; the last happens if and only if the respective vertices in $L\left(\mathcal{H}^{*}\right)$ are adjacent. $\square$

Corollary 7.6.1 For any hypergraph $\mathcal{H}$,

$$
L(\mathcal{H})=\left(\mathcal{H}^{*}\right)_{2} .
$$

Proof. Apply equality $\left(\mathcal{H}^{*}\right)^{*}=\mathcal{H}$ and Theorem 7.6.1 for hypergraph $\mathcal{H}^{*}$. $\square$

Theorem 7.6.2 For any hypergraph $\mathcal{H}$,

$$
\nu(\mathcal{H})=\alpha(L(\mathcal{H})) \text { and } \nu\left(\mathcal{H}^{*}\right)=\alpha\left((\mathcal{H})_{2}\right) .
$$

Proof. By definition, $\mathcal{V}(\mathcal{H})$ is the maximum number of edges of $\mathcal{H}$ which are pairwise disjoint; by definition of $L(\mathcal{H})$, this is the maximum number of vertices which represent an independent set. Similarly, maximum number of pairwise disjoint edges in $\mathcal{H}^{*}$ equals the maximum number of pairwise non-adjacent vertices in $\mathcal{H}$ what coincides with $\alpha\left((\mathcal{H})_{2}\right) . \square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-171.jpg?height=466&width=1126&top_left_y=590&top_left_x=298)
Figure 7.13.

Figure 7.13 shows a hypergraph $\mathcal{H}$, its dual $\mathcal{H}^{*}$ and the graph which is $(\mathcal{H})_{2}$ and $L\left(\mathcal{H}^{*}\right)$. Edges 1 and 4 in $\mathcal{H}^{*}$ for example, form a maximum matching with $v\left(\mathcal{H}^{*}\right)=2$; respectively, vertices 1 and 4 in graph $L\left(\mathcal{H}^{*}\right)$ represent a maximum independent set with $\alpha\left(L\left(\mathcal{H}^{*}\right)\right)=2$.

One can also check that $L(\mathcal{H})$ and $\left(\mathcal{H}^{*}\right)_{2}$ are isomorphic to the graph obtained from $C_{4}$ on vertices $a, b, c, d$ by adding diagonal $b d$. Edges $a$ and $c$ in $\mathcal{H}$ form a matching with $\mathcal{V}(\mathcal{H})=2$; respectively, vertices $a$ and $c$ in $L(\mathcal{H})$ represent a maximum independent set with $\alpha(L(\mathcal{H}))=2$, and so on. Observe that generally, for a hypergraph $\mathcal{H}$, graphs $L(\mathcal{H})$ and $(\mathcal{H})_{2}$ are different graphs.

A hypergraph $\mathcal{H}$ has the Helly property (is Helly, for short) if for every subfamily of its edges the following implication holds: if every two edges of the subfamily have a nonempty intersection, then the whole subfamily has a nonempty intersection.

A hypergraph $\mathcal{H}$ is called an intersecting family if all of its edges pairwise intersect. It means that $L(\mathcal{H})$ is a complete graph. A hypergraph $\mathcal{H}$ is called a star if there is a vertex which belongs to all hyperedges. Clearly, stars are the special case of intersecting families. In a hypergraph $\mathcal{H}$, the number of edges in a maximum intersecting subfamily equals $\boldsymbol{\omega}(L(\mathcal{H}))$. The simplest example of an intersecting family which is not a star is triangle $K_{3}$ : all three edges pairwise intersect but there is no common vertex. In this terminology, a hypergraph is Helly if every partial subhypergraph representing an intersecting family, is a star.

In multigraphs, the intersecting families are the stars or the triangles with possibly multiple edges. The Helly multigraphs do not contain triangles.

The Helly property plays a crucial role in optimization problems. Let us consider the problem of finding a minimum transversal of a hypergraph $\mathcal{H}$, or, equivalently, a maximum independent set of $\mathcal{H}$. Every clique in graph $L(\mathcal{H})$ represents an intersecting family in $\mathcal{H}$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-172.jpg?height=469&width=1142&top_left_y=217&top_left_x=282)
Figure 7.14.

and vice versa. If $\mathcal{H}$ is Helly, then every such family is a star. Therefore, every transversal of $\mathcal{H}$ represents a set of cliques in $L(\mathcal{H})$ which cover all vertices, i.e, clique covering of $L(\mathcal{H})$. Immediate conclusion is that $\tau(\mathcal{H})=\theta(L(\mathcal{H}))$, and finding a minimum transversal of $\mathcal{H}$ is now reduced to finding a minimum clique covering of $L(\mathcal{H})$. In its turn as we know, the last is equivalent to finding the chromatic number $\chi(\overline{L(\mathcal{H})})$ We can see that there is a relation between transversals of $\mathcal{H}$ and feasible partitions of the complementary graph $\overline{L(\mathcal{H})}$. If $\mathcal{H}$ is not Helly, we do not have this relation and we are not able to use $L(\mathcal{H})$ for finding $\tau(\mathcal{H})$.

Hypergraph $\mathcal{H}$ in Figure 7.13 is not Helly: edges $b, c$, and $d$ form an intersecting family ("triangle") which is not a star. Let us extend edge $d$ and consider a hypergraph $\mathcal{H}$ in Figure 7.14. It becomes Helly with $L(\mathcal{H})$ and $\overline{L(\mathcal{H})}$ as in Figure 7.14. One can see that every clique (not necessarily maximal) in $L(\mathcal{H})$ has a corresponding vertex in $\mathcal{H}$ and one minimum covering by cliques of $L(\mathcal{H})$ is: $\{a, b, d\}$ and $\{c\}$. It means that one minimal transversal of $\mathcal{H}$ is obtained by taking one vertex from intersecting family $\{a, b, d\}$ and one vertex from edge $c$ in $\mathcal{H}$, so $\tau(\mathcal{H})=\theta(L(\mathcal{H}))=2$. Such covering corresponds to a proper coloring of $(\overline{L(\mathcal{H})})$ with $\chi(\overline{L(\mathcal{H})})=2$ colors: vertices $\{a, b, d\}$ with the first color and vertex $c$ with the second. There are several such optimal solutions.

A hypergraph $\mathcal{H}$ is called conformal if all the maximal cliques of the graph $(\mathcal{H})_{2}$ are all the maximal by inclusion edges of $\mathcal{H}$. If $\mathcal{H}$ does not contain included edges, it is conformal if and only if the edges of $\mathcal{H}$ are precisely the maximal cliques of 2-section $(\mathcal{H})_{2}$. In other words, any conformal hypergraph may be obtained from a simple graph by taking the set of maximal cliques as hyperedges and possibly adding a number of included hyperedges. For the simplicity reason, let us agree that in the next lemma and theorems hypergraphs do not contain isolated vertices.

Lemma 7.6.1 A hypergraph $\mathcal{H}=(X, \mathcal{D})$ is conformal if and only if for any $Y \subseteq X$ inducing a clique in $(\mathcal{H})_{2}$ there is an edge $D \in \mathcal{D}$ such that $Y \subseteq D$.

Proof. $\Rightarrow$ Let $\mathcal{H}=(X, \mathcal{D})$ be a conformal hypergraph, $G=(\mathcal{H})_{2}$, and $Y \subseteq X$ be any set of vertices such that $G_{Y}$ is a clique. Since any clique is a subgraph of at least one maximal clique, there exists a set $Z \subseteq X$ such that $Y \subseteq Z$ and $G_{Z}$ is a clique. Then $Z=D$ for some $D \in \mathcal{D}$ because $\mathcal{H}$ is conformal. Hence $Y \subseteq D$.

⇐ Let the condition of Lemma hold, i.e., for any $Y \subseteq X$ inducing a clique in $(\mathcal{H})_{2}$ there is an edge $D \in \mathcal{D}$ such that $Y \subseteq D$. To prove that $\mathcal{H}$ is conformal, we need to prove that the family $\mathcal{D}^{\prime}$ of maximal edges of $\mathcal{H}$ and the family $\mathcal{C}$ of maximal cliques of $G$ coincide, i.e. $\mathcal{D}^{\prime}=\mathcal{C}$.

Case 1: Prove that $\mathcal{D}^{\prime} \subseteq \mathcal{C}$. Let $D \in \mathcal{D}^{\prime}$. By definition of $G$, all vertices of $D$ are pairwise adjacent, i.e. $G_{D}$ is a clique. It is contained in a maximal clique $C \in C$, i.e. $D \subseteq C$. By the condition of Lemma, for $C$ there exists an edge $D^{\prime}$ such that $C \subseteq D^{\prime}$. So we have $D \subseteq C \subseteq D^{\prime}$. But both $D$ and $D^{\prime}$ are maximal what implies that $D=C=D^{\prime}$ and $D \in \mathcal{C}$. Consequently, $\mathcal{D}^{\prime} \subseteq \mathcal{C}$.

Case 2: Prove that $\mathcal{C} \subseteq \mathcal{D}^{\prime}$. Let $C \in \mathcal{C}$ be an arbitrary maximal clique in $G$. The vertices of $C$ are pairwise adjacent. By the condition of Lemma, there exist an edge $D \in \mathcal{D}$ with $C \subseteq D$. In turn, there exists an edge $D^{\prime} \in \mathcal{D}^{\prime}$ such that $D \subseteq D^{\prime}$. Since vertices of $D^{\prime}$ are pairwise adjacent in $G$, there exists a maximal clique $C^{\prime}$ such that $D^{\prime} \subseteq C^{\prime}$. Since both $C$ and $C^{\prime}$ are maximal, and $C \subseteq D^{\prime} \subseteq C^{\prime}$, it follows that $C=D=C^{\prime}$ and $C \in \mathcal{D}^{\prime}$. Consequently, $\mathcal{C} \subseteq \mathcal{D}^{\prime}$. $\square$

Theorem 7.6.3 (Gilmore, 1961) A hypergraph $\mathcal{H}=(X, \mathcal{D})$ is conformal if and only if for any three edges $D_{1}, D_{2}, D_{3}$, there is an edge $D$ such that

$$
\left(D_{1} \cap D_{2}\right) \cup\left(D_{1} \cap D_{3}\right) \cup\left(D_{2} \cap D_{3}\right) \subseteq D \text {. }
$$

Proof. $\Rightarrow$ Let $\mathcal{H}=(X, \mathcal{D})$ be a conformal hypergraph and $D_{1}, D_{2}, D_{3}$ be arbitrary edges. The vertices of $\left(D_{1} \cap D_{2}\right) \cup\left(D_{1} \cap D_{3}\right) \cup\left(D_{2} \cap D_{3}\right)$ are pairwise adjacent and therefore induce a clique. By Lemma 7.6.1, there exists an edge $D$ such that

$$
\left(D_{1} \cap D_{2}\right) \cup\left(D_{1} \cap D_{3}\right) \cup\left(D_{2} \cap D_{3}\right) \subseteq D \text {. }
$$

⇐ Assume that the inclusion 7.4 holds and show that then the condition of Lemma 7.6.1 fulfils. Induction on $|Y|$ where $Y$ is the set of pairwise adjacent vertices of graph $(\mathcal{H})_{2}$. If $|Y|=1$, a vertex is contained in some edge of $\mathcal{H}$ (otherwise it is isolated). If $|Y|=2$, then two vertices of $Y$ are adjacent and by definition of $(\mathcal{H})_{2}$ there is an edge $D$ such that $Y \subseteq D$. Let the condition of Lemma 7.6.1 hold for all $Y$ such that $|Y|<k, k \geq 3$, and let $Y$ be a subset of vertices inducing a clique of size $k$ in $(\mathcal{H})_{2}$.

Since $|Y| \geq 3$, choose vertices $x_{1}, x_{2}, x_{3} \in Y$ and put $Y_{i}=Y-\left\{x_{i}\right\}, i=1,2,3$. Notice that

$$
Y=\left(Y_{1} \cap Y_{2}\right) \cup\left(Y_{1} \cap Y_{3}\right) \cup\left(Y_{2} \cap Y_{3}\right) .
$$

By the induction hypothesis, there exist edges $D_{1}, D_{2}, D_{3}$ such that $Y_{i} \subseteq D_{i}, i=1,2,3$. This implies

$$
Y \subseteq\left(D_{1} \cap D_{2}\right) \cup\left(D_{1} \cap D_{3}\right) \cup\left(D_{2} \cap D_{3}\right) .
$$

Applying relation (7.4), we obtain $Y \subseteq D$ for some $D \in \mathcal{D}$. Thus, any subset of pairwise adjacent vertices of graph $(\mathcal{H})_{2}$ is contained in some edge of $\mathcal{H}$. By Lemma 7.6.1, $\mathcal{H}$ is conformal. $\square$

Theorem 7.6.4 A hypergraph $\mathcal{H}$ is conformal if and only if its dual $\mathcal{H}^{*}$ is Helly.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-174.jpg?height=1266&width=1313&top_left_y=220&top_left_x=249)
Figure 7.15. Conformality and Helly property.

Proof. ⇒ Let $\mathcal{H}=(X, \mathcal{D})$ be a conformal hypergraph. Choose any intersecting subfamily of edges in $\mathcal{H}^{*}$, say $X_{1}, X_{2}, \ldots, X_{k}$. In $\mathcal{H}$, they correspond to pairwise adjacent vertices $x_{1}, x_{2}, \ldots, x_{k}$. Since $\mathcal{H}$ is conformal, by Lemma 7.6.1 there is an edge $D$ such that $x_{1}, x_{2}, \ldots, x_{k} \in D$. It means that in $\mathcal{H}^{*}$, there is a vertex $d$ such that $d \in X_{1}, d \in X_{2}, \ldots$, $d \in X_{k}$, or, equivalently, $d \in X_{1} \cap X_{2} \cap \cdots \cap X_{k}$. Consequently, every intersecting subfamily of $\mathcal{H}^{*}$ is a star, i.e. $\mathcal{H}^{*}$ is Helly.

⇐ Assume now that $\mathcal{H}^{*}$ is a Helly hypergraph. Then any intersecting family of $\mathcal{H}^{*}$ is a star. Equivalently, in $\mathcal{H}$, any set of pairwise adjacent vertices is contained in an edge. By Lemma 7.6.1, $\mathcal{H}$ is a conformal hypergraph. $\square$

The simplest example to show the relation between Helly property and conformality is the triangle $K_{3}$, see Figure 7.15. Apparently, $K_{3}$ itself is neither Helly, nor a conformal hypergraph. Indeed, it is an intersecting family but not a star; it is a clique but not contained
in any hyperedge. If we add an edge containing all vertices, then it becomes a conformal hypergraph $\mathcal{H}_{1}$. Otherwise, if we add a vertex incident to all three edges, we obtain a Helly hypergraph $\mathcal{H}_{2}$. One can easily check that $\mathcal{H}_{2} \cong \mathcal{H}_{1}^{*}$. At last, if we add to $\mathcal{H}_{2}$ an edge containing all vertices, we obtain a hypergraph $\mathcal{H}_{3}$ which is both Helly and conformal.

A hypergraph is called self-dual if $\mathcal{H} \cong \mathcal{H}^{*}$; evidently, the incidence matrix of a selfdual hypergraph is square and symmetric about main diagonal. A hypergraph $\mathcal{H}$ is called bi-conformal if both $\mathcal{H}$ and $\mathcal{H}^{*}$ are conformal. Consequently, if $\mathcal{H}$ is a bi-conformal hypergraph, then both $\mathcal{H}$ and $\mathcal{H}^{*}$ are Helly hypergraphs.

Notice that hypergraph $\mathcal{H}_{3}$ in Figure 7.15 is bi-conformal and self-dual, i.e. $\mathcal{H}_{3} \cong \mathcal{H}_{3}^{*}$.

## Exercises 7.6.

1. Construct line graph $L(\mathcal{H})$ for hypergraph $\mathcal{H}$, see Figure 7.11 and show that it is isomorphic to Petersen graph.
2. Construct 2-section $(\mathcal{H})_{2}$ for hypergraph $\mathcal{H}$, see Figure 7.11.
3. Prove that any bipartite graph is Helly.
4. Prove that Petersen graph is a Helly hypergraph.
5. For which $n, p, q, r \geq 1$, the graphs $P_{n}, C_{n}, W_{n}, E_{n}, K_{n}, K_{p, q, r}^{3}$ are or are not Helly ?
6. For which $n, r \geq 1$ complete hypergraph $K_{n}^{r}$ is Helly?
7. Prove that cube is and prism is not a Helly hypergraph.

Computer Projects 7.6. Write a program for the following algorithmic problems.

1. Given a hypergraph $\mathcal{H}$, construct $L(\mathcal{H})$.
2. Given a hypergraph $\mathcal{H}$, construct $(\mathcal{H})_{2}$.
3. Given a hypergraph, recognize if it is Helly.
4. Given a hypergraph, recognize if it is conformal.
5. Given a hypergraph, recognize if it is self-dual.

## Chapter 8

## Hypertrees and Chordal Hypergraphs

"-I see many trees, but where is the forest?..."

### 8.1. Hypertrees and Chordal Conformal Hypergraphs

Trees do not have cycles and represent the simplest class of graphs. We know the definition of a cycle in a hypergraph and it might seem that a direct generalization would be the best one for introducing and studying hypertrees. However, basic properties of trees hold for much more general structures than just hypergraphs without cycles.

A host graph for a hypergraph is a connected graph on the same vertex set, such that every hyperedge induces a connected subgraph of the host graph.

Definition 8.1.1 A hypergraph $\mathcal{H}=(X, \mathcal{D})$ is called a hypertree if there exists a host tree $T=(X, E)$ such that each edge $D \in \mathcal{D}$ induces a subtree in $T$.

In other words, any hypertree is isomorphic to some family of subtrees of a tree. Respectively, $\mathcal{H}$ is not a hypertree if for any tree on the same vertex set, at least one hyperedge of $\mathcal{H}$ induces a disconnected subgraph, i.e. a forest. Any tree is a hypertree because it is a host tree for itself. In contrast, a cycle cannot be a hypertree because there is always an edge inducing a forest. This is shown in Figure 8.1: a tree $T$ can be re-drawn in such a way that the edges become ellipses. We will always draw the host trees by dashed lines. In our example, a host tree coincides with $T$ itself. If we do the same for the cycle $C_{4}$, on the host tree at least one edge (lower edge in the figure) of $C_{4}$ induces a disconnected subgraph. One can try different trees on four vertices of $C_{4}$ to be the host tree: however, there will always be at least one disconnected subgraph of the host tree induced by an edge of $C_{4}$. Since the same reasoning applies to any cycle, no graph with cycles is a hypertree.

An example how the definition of a hypertree works in general hypergraphs is shown in Figure 8.2. One can see that hypergraph $\mathcal{H}_{1}$ is a hypertree, but in drawing of $\mathcal{H}_{2}$ there is an edge inducing a forest isomorphic to the empty graph $E_{3}$ in the host tree. May be another tree on the same vertex set can serve as a host tree? The first problem that arises in hypertrees is how to recognize them: given a hypergraph $\mathcal{H}$, how can we find a host tree if

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-178.jpg?height=746&width=1245&top_left_y=256&top_left_x=267)
Figure 8.1.

it exists? Alternatively, if $\mathcal{H}$ is not a hypertree, how that can be proven? We need a few new definitions and theorems to develop an algorithm for recognizing of hypertrees and finding solutions to some other optimization problems as well.

Lemma 8.1.1 (Buneman, 1974, Gavril, 1974, Walter, 1972) The line graph of a hypertree is chordal.

Proof. Let $\mathcal{H}=(X, \mathcal{D})$ be a hypertree and let $T=(X, E)$ be a host tree. We use induction on the number of vertices of $T$; when there is only one, the line graph is a clique and is chordal. When $T$ is larger, let $x$ be a pendant vertex of $T$. Let $L^{\prime}$ be the line graph of the hypergraph $\mathcal{H}^{\prime}$ obtained from $\mathcal{H}$ by weak deletion of $x$; if $\{x\}$ is a subtree itself, we remove it from the family of edges. Since the host tree for $\mathcal{H}^{\prime}$ is $T-x$, the hypergraph $\mathcal{H}^{\prime}$ is a hypertree too, and the induction hypothesis implies that $L^{\prime}$ is chordal.

If no hyperedge of $\mathcal{H}$ coincides with $\{x\}$, then $L^{\prime}=L$, and $L$ is chordal. If $\{x\}$ occurs by itself as a subtree, then the neighbors of this vertex in $L$ form a clique, since as subtrees they all contain $x$. Thus $L$ is obtained from $L^{\prime}$ by adding a simplicial vertex which cannot introduce a chordless cycle. Hence $L$ is chordal. $\square$

Lemma 8.1.2 (Berge, 1973) Every hypertree is a Helly hypergraph.
Proof. The usual proof is by induction; we present a short argument by Lehel (1972). Let $\mathcal{H}=(X, \mathcal{D})$ be a hypertree and $T=(X, E)$ be a host tree. To show that every intersecting family of $\mathcal{H}$ is a star, we prove the contrapositive. Let $\mathcal{F} \subseteq \mathcal{D}$ be an intersecting family which is not a star. Then each $x \in X$ misses some $D \in \mathcal{F}$. Mark the edge of $T$ that is the first on the path from $x$ to $D$. Since we place $n(T)=|X|$ marks on $n(T)-1$ edges, some edge is marked twice. This edge belongs to a path in $T$ between some members $D_{i}$ and $D_{j}$ of $\mathcal{F}$, which therefore do not intersect. Hence, $\mathcal{F}$ is not an intersecting family, a contradiction. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-179.jpg?height=502&width=1126&top_left_y=246&top_left_x=347)
Figure 8.2.

Definition 8.1.2 A hypergraph $\mathcal{H}$ is called chordal if every cycle of length $\geq 4$ has two non-consecutive vertices which are adjacent.

This definition directly extends the definition of chordal graphs. Thus $\mathcal{H}$ is a chordal hypergraph if and only if its 2-section $(\mathcal{H})_{2}$ is a chordal graph. If $x$ is a simplicial vertex in the 2-section $(\mathcal{H})_{2}$, then the neighbors of $x$ are pairwise adjacent in $\mathcal{H}$.

In a hypergraph $\mathcal{H}=(X, \mathcal{D})$, a vertex $x$ is pendant to a vertex $y$ if $\mathcal{D}(x) \subseteq \mathcal{D}(y)$. Sometimes, pendant vertex is called hyper-pendant. Thus, a pendant vertex in a graph is either isolated or pendant to its unique neighbor. Pendant vertices in a hypergraph $\mathcal{H}$ correspond to included edges in the dual hypergraph $\mathcal{H}^{*}$.

Theorem 8.1.1 A hypergraph $\mathcal{H}$ is chordal and conformal if and only if $\mathcal{H}^{*}$ is a hypertree.
Proof. [6] ⇒ Let $\mathcal{H}=(Y, \mathcal{D})$ be a chordal conformal hypergraph. We prove that $\mathcal{H}^{*}$ is a hypertree by induction on $n=n(\mathcal{H})$. For $n \leq 2$, every hypergraph is a hypertree. Now consider $n>2$, and suppose that the claim holds for smaller hypergraphs. The idea of the proof consists in weak deleting of a simplicial vertex of $(\mathcal{H})_{2}$ from $\mathcal{H}$, finding a host tree in the obtained dual hypergraph, and then reconstructing $\mathcal{H}$ by sequential expansions of the edges (operation inverse to weak deleting of the vertex) and constructing a host tree for $\mathcal{H}^{*}$.

Step 1: constructing hypergraph $\mathcal{H}_{0}$ and its 2-section $\left(\mathcal{H}_{0}\right)_{2}$. Since $\mathcal{H}$ is a chordal hypergraph, $(\mathcal{H})_{2}$ is a chordal graph. Therefore, $(\mathcal{H})_{2}$ has a simplicial vertex $x$. The closed neighborhood of $x$ in $(\mathcal{H})_{2}$ (the neighborhood plus $x$ itself) induces a maximal clique in $(\mathcal{H})_{2}$. By the conformality of $\mathcal{H}$, this set forms an edge $D_{0}$ in $\mathcal{H}$. Since $x$ has no additional neighbors, every edge in $\mathcal{H}$ that contains $x$ is a subset of $D_{0}$.

Let $\mathcal{H}_{0}$ be the hypergraph obtained from $\mathcal{H}$ by weakly deleting $x$ (see an example in Figure 8.3); thus, $\mathcal{H}_{0}$ has vertex set $Y-\{x\}$ and edge set $\{D-\{x\}: D \in \mathcal{D}\}$. Since $x$ is simplicial in $(\mathcal{H})_{2}$ and the edge $D_{0}-\{x\}$ in $\mathcal{H}_{0}$ contains all neighbors of $x$ in $\mathcal{H}$, we have $\left(\mathcal{H}_{0}\right)_{2}=(\mathcal{H})_{2}-x$ (strong deletion of $x$ ), and thus $\mathcal{H}_{0}$ is chordal. The maximal cliques in $\left(\mathcal{H}_{0}\right)_{2}$ are the same as those in $(\mathcal{H})_{2}$, except that the clique with vertex set $D_{0}$ is lost, and the
clique with vertex set $D_{0}-\{x\}$ is gained (unless it is not maximal). Since $\mathcal{H}_{0}$ has $D_{0}-\{x\}$ as an edge, $\mathcal{H}_{0}$ is conformal. In the example (Figure 8.3), edge $D$ becomes a singleton, and edge $D_{0}$ becomes an edge of size 2 in $\mathcal{H}_{0}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-180.jpg?height=406&width=1139&top_left_y=388&top_left_x=274)
Figure 8.3.

Step 2: induction hypothesis. Since $\mathcal{H}_{0}$ is chordal and conformal and contains $<n$ vertices, we may apply the induction hypothesis to $\mathcal{H}_{0}$ to conclude that $\mathcal{H}_{0}{ }^{*}$ is a hypertree. Thus there is a host tree $T$ with vertex set $\mathcal{D}^{\prime}=V\left(\mathcal{H}_{0}^{*}\right)$, such that for every $x^{\prime} \in V\left(\mathcal{H}_{0}\right)=$ $\mathcal{D}\left(\mathcal{H}_{0}^{*}\right)$, the elements of $\mathcal{D}^{\prime}$ that contain $x^{\prime}$ comprise a set of vertices of $T$ that induces a subtree.

Step 3: induction step. It remains to show that $\mathcal{H}^{*}$ is also a hypertree. We do this in several steps. First, define a hypergraph $\mathcal{H}_{1}$ by expanding the edge $D_{0}-\{x\}$ to include $x$ and become $D_{0}$. This adds a vertex of degree 1 to $\mathcal{H}_{0}$ and thus a singleton to $\mathcal{H}_{0}{ }^{*}$. Since $D_{0}-\{x\}$ is one vertex in $\mathcal{H}_{0}{ }^{*}$, it is also one vertex in $T$. Adding this vertex $d_{0}$ as a singleton $X$ as a subtree shows that $\mathcal{H}_{1}{ }^{*}$ is a hypertree.

Good case: $d$ is adjacent to $d_{0}$ in host tree $T$. Let $\mathcal{D}_{x}^{\prime}$ be the set of edges in $\mathcal{H}_{0}$, other than $D_{0}-\{x\}$, obtained by deleting $x$ from the edges of $\mathcal{D}(x)$ in $\mathcal{H}$. To obtain $\mathcal{H}$ from $\mathcal{H}_{1}$, we must expand these edges to include $x$. For each vertex $d$ of $T$ that is a neighbor of $d_{0}$ and corresponds to some $D \in \mathcal{D}_{\chi}^{\prime}$, we expand the edge $X$ of $\mathcal{H}_{1}^{*}$ to include $d$. This yields a hypertree $\mathcal{H}_{2}^{*}$ with host tree $T$, in which the edge $X$ corresponding to $x$ is a star with center $d_{0}$. The pendant vertices of this star are vertices in $\mathcal{H}_{2}^{*}$ that correspond to edges in $\mathcal{H}_{2}$ which we have expanded to include $x$.

Figure 8.4 shows the same example in dual form. Edges $D, D_{0}$ and $E$ become vertices $d, d_{0}$ and $e$; similarly, vertices $x, a, b$ and $c$ become edges $X, A, B$, and $C$ in dual $\mathcal{H}_{0}$. Notice that $X$ and $C$ are the singletons. Host tree $T$ is drawn by dashed lines.

Bad case: $d$ is not adjacent to $d_{0}$ in host tree $T$. Let $\mathcal{H}_{3}$ be the hypergraph obtained from $\mathcal{H}_{2}$ by including $x$ in an edge $D \in \mathcal{D}_{x}^{\prime}$ that we have not yet expanded. The edge $D$ of $\mathcal{H}_{2}$ corresponds to a vertex $d$ in $\mathcal{H}_{2}^{*}$ that is pendant to $d_{0}$, because the edges of $\mathcal{H}_{2}^{*}$ containing $d$ or $d_{0}$ are the vertices of $\mathcal{H}_{2}$ contained in $D$ or $D_{0}$, respectively, and we have $D \subset D_{0}$. The vertex $d$ in $\mathcal{H}_{2}^{*}$ occurs as a vertex of $T$ not adjacent to $d_{0}$. Adding the edge $\left(d, d_{0}\right)$ to $T$ creates a unique cycle. Deleting the edge $\left(d, d^{\prime}\right)$ on that cycle (with $d^{\prime} \neq d_{0}$ ) yields a different tree $T_{3}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-181.jpg?height=406&width=1033&top_left_y=207&top_left_x=381)
Figure 8.4.

Since $X$ consists only of $d_{0}$ and neighbors of $d_{0}$, we can now extend $X$ to include $d$; this corresponds to expanding $D$ to include $x$, and the vertices of the extended $X$ still induce a star in $T_{3}$. In order to complete the proof that $\mathcal{H}_{3}^{*}$ is a hypertree, we must show that the other edges of $\mathcal{H}_{3}^{*}$ induce a subtree even when $\left(d, d^{\prime}\right)$ is deleted. Let $X^{\prime}$ be an edge of $\mathcal{H}_{2}^{*}$ that contains $d$ and $d^{\prime}$. In $\mathcal{H}_{2}$, the vertex $x^{\prime}$ belongs to $D$ and $D^{\prime}$. Since $d$ is pendant to $d_{0}$ in $\mathcal{H}_{2}^{*}$, all the edges of $\mathcal{H}_{2}^{*}$ that contained $d$ also contain $d_{0}$. Thus the subtree in $T$ consisting of the vertices of $X^{\prime}$ contains not only $d$ and $d^{\prime}$ but also the path from $d^{\prime}$ to $d_{0}$. This implies that the vertices of $X^{\prime}$ still form a subtree in $T_{3}$.

The operation of changing the host tree $T$ (drawn by dashed lines) and further expansion of edge $X$ is shown in Figure 8.5: vertex $e$ plays the role of $d^{\prime}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-181.jpg?height=406&width=1033&top_left_y=1271&top_left_x=381)
Figure 8.5.

Repeating this procedure of enlarging the remaining edges of $\mathcal{D}_{x}^{\prime}$ yields a sequence of hypertrees $\mathcal{H}_{3}^{*}, \mathcal{H}_{4}^{*}, \ldots$ with host trees $T_{3}, T_{4}, \ldots$. At each step, the conditions are preserved so that the argument made for $\mathcal{H}_{3}^{*}$ holds also for the next step. After all these edges are expanded, the resulting hypertree is $\mathcal{H}^{*}$.

⇐ Let $\mathcal{H}^{*}$ be a hypertree. By Lemma 8.1.1, $L\left(\mathcal{H}^{*}\right)$ is chordal. Since $(\mathcal{H})_{2}=L\left(\mathcal{H}^{*}\right)$, we conclude that $(\mathcal{H})_{2}$ is a chordal graph, and thus $\mathcal{H}$ is a chordal hypergraph.

Let $R$ be a set of pairwise adjacent vertices in $\mathcal{H}$. These become pairwise intersecting edges in $\mathcal{H}^{*}$. By Lemma 8.1.2, $\mathcal{H}^{*}$ is Helly, and hence these edges in $\mathcal{H}^{*}$ have a common vertex. Thus in $\mathcal{H}$ the elements of $R$ lie in a common edge. This shows that the vertices of every clique in $(\mathcal{H})_{2}$ lie in an edge of $\mathcal{H}$, and thus $\mathcal{H}$ is conformal. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-182.jpg?height=404&width=1240&top_left_y=225&top_left_x=267)
Figure 8.6.

Corollary 8.1.1 (Flament, 1978) A hypergraph $\mathcal{H}$ is a hypertree if and only if $\mathcal{H}$ is Helly and $L(\mathcal{H})$ is chordal.

Proof. Theorem 8.1.1 states that $\mathcal{H}$ is a hypertree if and only if $\mathcal{H}^{*}$ is conformal and has a chordal 2-section. The corollary follows because $\mathcal{H}$ has the Helly property if and only if $\mathcal{H}^{*}$ is conformal (Theorem 7.6.4), and because $\left(\mathcal{H}^{*}\right)_{2}=L(\mathcal{H})$ (Corollary 7.6.1). $\square$

The clique hypergraph of a graph $G$ is the hypergraph with vertex set $V(G)$ whose edge set is the family of vertex sets of maximal cliques in graph $G$. Note that the 2-section of the clique hypergraph of a graph $G$ is $G$. Further, by construction every clique hypergraph is conformal. With Theorem 8.1.1, these observations yield:

Corollary 8.1.2 The dual of the clique hypergraph of a chordal graph is a hypertree.
Corollary 8.1.3 The dual of a chordal graph $G$ is a hypertree if and only if $G$ is a tree.
Proof. If $G$ is a tree, then the clique hypergraph of $G$ is $G$, and Corollary 8.1.2 yields the result. If $G^{*}$ is a hypertree, then $G$ as a hypergraph is conformal. Since all edges of $G$ have size 2, conformality requires that $G$ has no clique of size greater than 2, and thus $G$ is a tree. $\square$

Corollary 8.1.4 (Gavril, 1974) A graph $G$ is chordal if and only if it is the line graph of a hypertree.

Proof. If $G$ is chordal, then Corollary 8.1.2 says that the dual of its clique hypergraph is a hypertree. The vertices of the hypertree are the maximal cliques of $G$, and the cliques containing a particular vertex of $G$ form a subtree of the host tree. Furthermore, vertices of $G$ are adjacent if and only if they appear together in a maximal clique, meaning that the subtrees containing them have a common vertex in the host tree. The converse is Lemma 8.1.1. $\square$

A simple example to illustrate these statements is the triangle $K_{3}$ which is chordal but not a conformal hypergraph, nor it is a hypertree, see Figure 7.15. Adding an edge containing all the vertices makes it conformal, while adding a vertex contained in all the edges
makes it a hypertree; they are dual to each other. Another example, see Figure 8.6, shows how to find a tree representation, i.e., a hypertree, for a chordal graph $G$ : construct a clique hypergraph $\mathcal{H}$ of $G$, take the dual $\mathcal{H}^{*}$ and construct a respective tree. The host tree $T$ on vertices $x, y$ and $z$ is shown by dashed lines. Vertices $a, b, c, d$, and $e$ in $G$ and $\mathcal{H}$ become hyperedges $A, B, C, D$, and $E$ in $\mathcal{H}^{*}$ and each induce a subtree in $T$. One can easily see that $G=L\left(\mathcal{H}^{*}\right)$. Drawings of $\mathcal{H}$ and $\mathcal{H}^{*}$ are simply two different drawings of a (0,1)-matrix (namely, the incidence matrix of $\mathcal{H}$ ) and its transpose.

Chordal conformal hypergraphs are also known as $\alpha$-acyclic hypergraphs. In [2], hypertrees are called "arboreal hypergraphs" and chordal conformal hypergraphs are called "co-arboreal hypergraphs".

Exercises 8.1.
![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-183.jpg?height=269&width=1186&top_left_y=841&top_left_x=272)

Figure 8.7.

1. For each of the hypergraphs in Figure 8.7, construct the line graph.
2. Which of the hypergraphs in Figure 8.7 are Helly hypergraphs?
3. Which of the hypergraphs in Figure 8.7 are hypertrees?
4. Which of the hypergraphs in Figure 8.7 are chordal?
5. Which of the hypergraphs in Figure 8.7 are chordal and conformal?
6. For each of the hypergraphs in Figure 8.7, construct the dual.
7. For each of the hypergraphs in Figure 8.7, verify that $L(\mathcal{H})=\left(\mathcal{H}^{*}\right)_{2}$.
8. Which of the dual hypergraphs to every hypergraph in Figure 8.7 is a hypertree?

Computer Projects 8.1. Write a program for the following algorithmic problems.

1. Given a graph $G$, construct the clique hypergraph of $G$.
2. Given a hypertree, construct the line graph.
3. Given a chordal conformal hypergraph, construct the 2-section.
4. Given a chordal graph $G$, construct a hypertree $\mathcal{H}$ such that $G=L(\mathcal{H})$.
5. Given a hypergraph, determine if it is chordal.

### 8.2. Algorithms on Hypertrees

In a hypergraph $\mathcal{H}=(X, \mathcal{D})$, a vertex $x \in X$ is called a transversal vertex if there exist an edge $D \in \mathcal{D}$ such that $D=\{x\}$ (i.e., $D$ is a singleton). It means that $x$ belongs to every transversal of $\mathcal{H}$, including minimum ones. Transversal vertex in $\mathcal{H}$ becomes an edge $X$ in $\mathcal{H}^{*}$ which contains a vertex $d$ belonging only to $X$.

Recall that in a hypergraph $\mathcal{H}=(X, \mathcal{D})$, a vertex $x \in X$ is called pendant (hyperpendant) if there exist a vertex $y \in X, y \neq x$, such that $\mathcal{D}(x) \subseteq \mathcal{D}(y)$. Such a vertex $y$ is then called a twin vertex of $x$. In dual hypergraph $\mathcal{H}^{*}$, hyper-pendant vertex $x$ becomes an edge $X$ which is contained as a subset in an edge $Y$ corresponding to the twin $y$, i.e. it is an included edge. If $\mathcal{H}$ contains at least two vertices, then any isolated vertex is hyperpendant because $\mathcal{D}(x)=\emptyset$ for any isolated vertex $x$. Any pendant vertex in a graph is hyper-pendant. Hyper-pendant vertex cannot be transversal, and transversal vertex cannot be hyper-pendant.

Theorem 8.2.1 If $x \in X$ is a hyper-pendant vertex in a hypergraph $\mathcal{H}=(X, \mathcal{D})$, and hypergraph $\mathcal{H}_{1}$ is obtained from $\mathcal{H}$ by weak deletion of $x$, then:

1. there exists a maximum independent set $S \subseteq X$ such that $x \in S$;
2. $\mathrm{T}(\mathcal{H})=\mathrm{T}\left(\mathcal{H}_{1}\right)$;
3. $\alpha(\mathcal{H})=\alpha\left(\mathcal{H}_{1}\right)+1$;
4. $v(\mathcal{H})=v\left(\mathcal{H}_{1}\right)$;
5. if $\mathcal{H}$ is a hypertree, then $\mathcal{H}_{1}$ is a hypertree.

Proof. 1. By definition of hyper-pendant vertex, there exists a twin vertex $y$ such that $\mathcal{D}(x) \subseteq \mathcal{D}(y)$. Consider two cases.

Case a): $y$ belongs to a minimum transversal $T \subseteq X$. Then $x \notin T$ because otherwise the set $T_{1}=T-\{X\}$ is a transversal with $\left|T_{1}\right|=|T|-1=\tau(\mathcal{H})-1$, a contradiction. Therefore, $x \in X-T=S$ where $S$ is a maximum independent set.

Case b): $y$ belongs to no minimum transversal of $\mathcal{H}$. If there exists a minimum transversal $T_{1}$ such that $x \in T_{1}$, then set $T_{2}=\left(T_{1}-\{x\}\right) \cup\{y\}$ is a minimum transversal what contradicts the condition of the case. Hence again, there exists a maximum independent set $S \subseteq X$ such that $x \in S$.
2. Weak deletion of a vertex from a hypergraph cannot decrease the size of a minimum transversal, so $\tau(\mathcal{H}) \leq \tau\left(\mathcal{H}_{1}\right)$. On the other hand, 1. implies that in $\mathcal{H}$ there is a minimum transversal not containing $x$; weak deletion of $x$ cannot increase it, so $\tau(\mathcal{H}) \geq \tau\left(\mathcal{H}_{1}\right)$. Therefore, $\tau(\mathcal{H})=\tau\left(\mathcal{H}_{1}\right)$.
3. Since $\alpha(\mathcal{H})+\tau(\mathcal{H})=|X|, \alpha\left(\mathcal{H}_{1}\right)+\tau\left(\mathcal{H}_{1}\right)=|X|-1$, and $\tau(\mathcal{H})=\tau\left(\mathcal{H}_{1}\right)$, conclude that $\boldsymbol{\alpha}(\boldsymbol{\mathcal { H }})=\boldsymbol{\alpha}\left(\mathcal{H}_{1}\right)+1$.
4. Any maximum matching of $\mathcal{H}$ is a matching in $\mathcal{H}_{1}$, so $\mathcal{V}(\mathcal{H}) \leq \mathcal{v}\left(\mathcal{H}_{1}\right)$. On the other hand, in $\mathcal{H}_{1}$ no matching contains two edges from $\mathcal{D}(x)$ because $x$ is hyper-pendant. This implies that every matching in $\mathcal{H}_{1}$ is a matching in $\mathcal{H}$, i.e., $\mathcal{V}(\mathcal{H}) \geq \mathcal{V}\left(\mathcal{H}_{1}\right)$.
5. By Corollary 8.1.1, $\mathcal{H}$ is a hypertree if and only if it is Helly and $L(\mathcal{H})$ is a chordal graph. Since $x$ is hyper-pendant, $\mathcal{H}_{1}$ is a Helly hypergraph, too, and, moreover, $L(\mathcal{H})=$ $L\left(\mathcal{H}_{1}\right)$. Consequently, $\mathcal{H}_{1}$ is a hypertree. $\square$

Theorem 8.2.2 If $x \in X$ is a transversal vertex in a hypergraph $\mathcal{H}=(X, \mathcal{D})$, and hypergraph $\mathcal{H}_{1}$ is obtained from $\mathcal{H}$ by strong deletion of $x$, then:

1. $x$ belongs to any transversal of $\mathcal{H}$;
2. $\tau(\mathcal{H})=\tau\left(\mathcal{H}_{1}\right)+1$;
3. $\alpha(\mathcal{H})=\alpha\left(\mathcal{H}_{1}\right)$;
4. $v(\mathcal{H})=v\left(\mathcal{H}_{1}\right)+1$;
5. if $\mathcal{H}$ is a hypertree, then $\mathcal{H}_{1}$ is a hypertree.

Proof. 1. It follows from the definition of transversal and the fact that $\{x\} \in \mathcal{D}$.
2. Let $T_{1} \subset X_{1}=X-\{x\}$ be a minimum transversal of $\mathcal{H}_{1}$. Then set $T_{2}=T_{1} \cup\{x\} \subset X$ is a transversal of $\mathcal{H}$, what implies $\tau(\mathcal{H}) \leq \tau\left(\mathcal{H}_{1}\right)+1$. On the other hand, if $T$ is a minimum transversal of $\mathcal{H}$, then $T_{0}=T-\{x\}$ is a transversal of $\mathcal{H}_{1}$, what implies $\tau(\mathcal{H}) \geq \tau\left(\mathcal{H}_{1}\right)+1$.
3. Since $\alpha(\mathcal{H})+\tau(\mathcal{H})=|X|, \alpha\left(\mathcal{H}_{1}\right)+\tau\left(\mathcal{H}_{1}\right)=|X|-1$, and $\tau(\mathcal{H})=\tau\left(\mathcal{H}_{1}\right)+1$, conclude that $\alpha(\mathcal{H})=\alpha\left(\mathcal{H}_{1}\right)$.
4. Since $x$ is a transversal vertex, for any maximum matching $\mathcal{F}$ of $\mathcal{H}_{1}$ the family $\mathcal{F} \cup\{x\}$ is a matching of $\mathcal{H}$, what implies $\mathcal{V}(\mathcal{H}) \geq \mathcal{V}\left(\mathcal{H}_{1}\right)+1$.

Strong deletion of a vertex from a hypergraph cannot decrease the size of a maximum matching by more than 1 ; hence $\mathcal{V}(\mathcal{H})-1 \leq \mathcal{V}\left(\mathcal{H}_{1}\right)$ what implies the required equality.
5. Any induced subhypergraph of a hypertree is also a hypertree; even if $\mathcal{H}_{1}$ is a disconnected hypergraph, each connected component is a hypertree, and the host tree for the entire $\mathcal{H}_{1}$ can be obtained by sequential connecting of the respective host trees by edges. $\square$

Proposition 8.2.1 If $\mathcal{H}=(X, \mathcal{D}),|X| \geq 2$, is a hypertree, then it contains at least two vertices such that each of them is either transversal or hyper-pendant.

Proof. Indeed, since $\mathcal{H}$ is a hypertree, there exists a tree $T$ which is a host graph. Tree $T$ has at least two pendant vertices. Evidently, each of these vertices is either hyper-pendant, or transversal. $\square$

Theorem 8.2.3 If $\mathcal{H}$ is a hypertree, then it satisfies the König property, i.e.

$$
\tau(\mathcal{H})=\nu(\mathcal{H}) .
$$

Proof. Since $\mathcal{H}$ is a hypertree, by Proposition 8.2.1 it contains either a hyper-pendant vertex, or a transversal vertex. We can decompose $\mathcal{H}$ sequentially by weak deleting of a hyper-pendant vertex or strong deleting of a transversal vertex. Theorems 8.2.1 and 8.2.2 assure that in such decomposition we obtain a sequence of hypertrees, and, moreover, the cardinality of the minimum transversal $\tau$ changes or does not change simultaneously with the cardinality of maximum matching $\nu$. At the very end of decomposition we obtain a
one-vertex hypergraph; either it is a hyper-pendant (isolated) vertex, then $\tau=\nu=0$, or a transversal vertex, then $\tau=v=1$. In all steps we have the equality, so $\tau(\mathcal{H})=v(\mathcal{H})$. $\square$

The statement above could be seen in a different way. Recall that Theorem 5.7.1 states that graph $G$ is perfect if and only if its complement $\bar{G}$ is perfect. Theorem 5.7.2 states that any chordal graph is perfect. Hence for chordal graphs $\chi=\omega$ and $\theta=\alpha$. We know that if $\mathcal{H}$ is a hypertree, then $L(\mathcal{H})$ is chordal. Therefore $\theta(L(\mathcal{H}))=\alpha(L(\mathcal{H}))$. Because $\mathcal{H}$ is Helly, the cardinality of minimum transversal $\tau(\mathcal{H})=\theta(L(\mathcal{H}))$. By definition of $L(\mathcal{H})$, the size of maximum matching $\nu(\mathcal{H})=\alpha(L(\mathcal{H}))$. So in total, we have the same equality $\tau(\mathcal{H})=\mathcal{V}(\mathcal{H})$. Moreover, it holds for every partial subhypergraph $\mathcal{H}^{\prime} \subseteq \mathcal{H}$ and for every induced subgraph of $L(\mathcal{H})$ as well.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-186.jpg?height=1170&width=1201&top_left_y=720&top_left_x=251)
Figure 8.8. Recognition of a hypertree.

Next we propose an algorithm for recognizing hypertrees. It is based on Proposition 8.2.1 and weak deletions of vertices and edges.

Algorithm 8.2.1 Recognition of a hypertree.
INPUT: An arbitrary hypergraph $\mathcal{H}=(X, \mathcal{D})$.
OUTPUT: A host tree $T$ if $\mathcal{H}$ is a hypertree, or answer "No" otherwise.

1. Find a hyper-pendant vertex or such a transversal vertex that becomes hyper-pendant after weak deleting of all incident singletons. If there are no such vertices, output "No" and end.
2. Delete weakly the hyper-pendant vertex and fix the twin vertex. Continue steps 1 and 2 until one vertex remains.
3. Starting with one vertex construct the host tree $T$ by adding vertices in inverse order; each time add the vertex and connect it with its twin.
4. Output tree T.

An example how the algorithm works is shown in Figure 8.8. The arrow with 1-2 on it means that hyper-pendant vertex 1 is weakly deleted from $\mathcal{H}$, its twin vertex 2 is fixed and $\mathcal{H}_{2}$ is the hypergraph obtained. Hypergraph $\mathcal{H}_{2}$ does not contain hyper-pendant vertices, however, vertex 3, for example, becomes hyper-pendant with the twin 2 after weak deletion of the singleton $\{3\}$. Similarly, vertex 2 in $\mathcal{H}_{3}$ becomes hyper-pendant with the twin 4 after weak deletion of the singleton $\{2\}$. At last, hypergraph $\mathcal{H}_{4}$ has the only vertex. So, the ordering of vertices is: 1, 3, 2, 4. At this point we start constructing the host tree beginning with $T_{4}$. Sequentially adding vertices in inverse order 4, 2, 3, 1 and connecting them to their twins, finally, we arrive to tree $T$ which is the host tree for $\mathcal{H}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-187.jpg?height=456&width=1087&top_left_y=1222&top_left_x=311)
Figure 8.9. Hyper-pendant vertices $x$ and $y$.

Applying Algorithm 8.2.1 to hypergraph $\mathcal{H}_{2}$, shown in Figure 8.2, see Figure 8.9, we find that vertex $x$ is hyper-pendant with twin $y$; after weak deletion of $x$ we obtain the triangle which contains neither transversal nor hyper-pendant vertices. Algorithm stops with the output "No".

It is important to notice that the output of Algorithm 8.2.1 does not depend on the order in which vertices and edges are deleted. Another observation is that in the incidence matrix of a hypergraph, a hyper-pendant vertex can be recognized by the following: its row contains 1 in the same columns as the row of respective twin.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-188.jpg?height=803&width=1258&top_left_y=217&top_left_x=264)
Figure 8.10.

Algorithm 8.2.2 Finding minimum transversal and maximum matching in a hypertree.
INPUT: Hypertree $\mathcal{H}=(X, \mathcal{D})$.
OUTPUT: minimum transversal $T \subseteq X$ and maximum matching $\mathcal{F} \subseteq \mathcal{D}$.

1. Put $T=\emptyset, \mathcal{F}=\emptyset$.
2. Find a hyper-pendant or transversal vertex.
3. If the vertex is hyper-pendant, delete it weakly.
4. If the vertex is transversal, include it in $T$, the incident singleton in $\mathcal{F}$, and delete the vertex strongly.
5. Repeat steps 2-4 as many times as possible.
6. Output $T, \mathcal{F}$.

Theoretical base for Algorithm 8.2.2 is provided by Theorems 8.2.1 and 8.2.2. It only remains to notice that in practical realization of the algorithm one needs to keep track about all changes in the edges; including a singleton in the maximum matching really means including an original edge from which the singleton was obtained by all previous deletions.

A remarkable instructive feature of Algorithm 8.2.2, however, is that it works for much more general hypergraphs than just hypertrees. A clue to this fact is that strong deletions of the vertices may change the structural properties of a hypergraph in such a way that it becomes "like hypertree" not being hypertree at all in the beginning. An example of such
a case is demonstrated in Figure 8.10. Graph $G$ is not a hypertree; it has the only hyperpendant (=pendant) vertex 6. After weak deletion of it, vertex 1 becomes transversal. Strong deletion of vertex 1 produces a graph with two pendant vertices, 2 and 5. Weak deletion of vertex 2 makes vertex 3 transversal in the next graph. Strong deletion of vertex 3 and further weak deletion of vertex 4 results in one transversal vertex 5 . The output of algorithm is the minimum transversal $T=\{1,3,5\}$ and maximum matching $\mathcal{F}=\{\{1,6\},\{2,3\},\{4,5\}\}$, so $\tau(G)=\mathcal{V}(G)$. Maximum matching $\mathcal{F}$ is shown by double lines in the second drawing of $G$. One can compare graph $G$ with cycle $C_{5}$ where $\tau\left(C_{5}\right)=3>2=v\left(C_{5}\right)$.

## Exercises 8.2.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-189.jpg?height=479&width=1113&top_left_y=751&top_left_x=342)
Figure 8.11.

1. Find all pendant and transversal vertices in Figure 8.11.
2. Apply Algorithm 8.2.1 to each hypergraph in Figure 8.11.
3. Compute $\tau, \alpha$ and $\nu$ and find a minimum transversal, maximum independent set and maximum matching for each hypergraph in Figure 8.11.
4. For each of the hypergraphs in Figure 8.11, construct the dual hypergraph and solve the problems 1-3 above.

Computer Projects 8.2. Write a program for the following algorithmic problems.

1. Given a hypergraph $\mathcal{H}$, recognize if it is a hypertree.
2. Given a hypertree $\mathcal{H}$, find minimum transversal, maximum independent set and maximum matching.
3. Given a hypergraph $\mathcal{H}$ that can be decomposed by weak deletions of hyper-pendant and strong deletions of transversal vertices. Find $\tau(\mathcal{H}), \alpha(\mathcal{H})$ and $\nu(\mathcal{H})$.
4. Given a chordal conformal hypergraph $\mathcal{H}$, find a minimum covering $\rho(\mathcal{H})$.

### 8.3. Cyclomatic Number of a Hypergraph

Cycles in graphs and hypergraphs represent the main cause of complexity for optimization problems. Therefore it is important to know how many cycles are in a given graph or hypergraph, or how they are structured, i.e. what additional properties they have. Recall (see Section 2.1.) that for a simple connected graph $G$, the cyclomatic number $\wedge(G)=$ $m-n+1$. The same formula generalizes to multigraphs if we add to $G$ any number of loops or multiple edges; each such addition forms a unique cycle with respect to a chosen spanning tree and increases the number of edges $m=m(G)$. Any additional edge, even loop, is considered as a "chord", or "diagonal" of the spanning tree. In this way the cyclomatic number is a measure of "how far" the multigraph is from a tree. We now show that the cyclomatic number can be generalized to hypergraphs, and hypertrees play a role similar to that what trees play for multigraphs.

Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph. A multigraph $G=(X, E)$ is called the generalized 2-section of $\mathcal{H}$, denoted by $[\mathcal{H}]_{2}$, if it is obtained from $\mathcal{H}$ in the following way:

1. all loops and edges of size 2 of $\mathcal{H}$ are included in $E$;
2. every hyperedge of size $\geq 3$ of $\mathcal{H}$ is replaced by a complete graph on the same vertices and all edges of the complete graph are included in $E$.

Hence, $(\mathcal{H})_{2}=[\mathcal{H}]_{2}$ if and only if $\mathcal{H}$ itself is a simple graph. Further, let us call any multigraph without cycles of length $\geq 3$ a multi-forest. The weight of a multi-forest $T$, denoted by $w(T)$, is the number of edges of size 2 in $T$; the loops have weight 0 . If $T$ is a multi-forest, then $\bar{T}$ denotes a forest obtained from $T$ by weak deletion of all loops and replacing each set of parallel edges by an edge connecting the same pair of vertices. Thus $\bar{T}=(T)_{2}$. A vertex $x$ is called pendant in a multi-forest $T$ if it is pendant in $\bar{T}$.

Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph and $T=(X, E)$ be a spanning multi-forest of the multigraph $[\mathcal{H}]_{2}$. For brevity, throughout this section call every such a spanning multiforest by just "forest".

Proposition 8.3.1 For any forest $T$ of a multigraph $[\mathcal{H}]_{2}$

$$
w(T) \leq \sum_{D \in \mathcal{D}}(|D|-1) .
$$

Proof. By definition of $T$, any single edge $D \in \mathcal{D}$ may provide to $T$ maximum $|D|-1$ edges of size 2. $\square$

Any singleton in a hypergraph, or, equivalently, any loop in a multigraph is considered as a cycle of length 1 (by default we assume that hypergraphs do not contain empty edges). Let $l(\mathcal{H}, T)$ denote the number of singletons (loops) of a hypergraph $\mathcal{H}$ which are not included in a forest $T$. It is convenient to consider them as "chords" of $T$.

Definition 8.3.1 Generalized cyclomatic number of a hypergraph $\mathcal{H}$ with respect to forest $T$ is the value

$$
\wedge(\mathcal{H}, T)=\sum_{D \in \mathcal{D}}(|D|-1)-w(T)+l(\mathcal{H}, T) .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-191.jpg?height=927&width=1227&top_left_y=197&top_left_x=269)
Figure 8.12. Forests $T$ and $\bar{T}$.

Let $\mathcal{H}$ be a connected multigraph (with loops and multiple edges); then $[\mathcal{H}]_{2}=\mathcal{H}$. If we take any spanning tree (clearly without loops and multiple edges) as a forest $T$, then $w(T)=|X|-1=n-1$. Since all loops of $\mathcal{H}$ will contribute to $l(\mathcal{H}, T)$, we obtain:

$$
\begin{gathered}
\wedge(\mathcal{H}, T)=\sum_{|D|=2}(|D|-1)-w(T)+l(\mathcal{H}, T) \\
=|\mathcal{D}|-(|X|-1)=m-n+1 .
\end{gathered}
$$

This equality shows that $\Lambda(\mathcal{H}, T)$ generalizes usual cyclomatic number of a multigraph.
An example of a hypergraph $\mathcal{H}$, its generalized 2-section $[\mathcal{H}]_{2}$, a forest $T$ and a forest $\bar{T}$ is shown in Figure 8.12. Forest $T$ contains three edges of size 2, an isolated vertex and only one of the two loops of $\mathcal{H}$, so $w(T)=3$. One can compute:

$$
\begin{gathered}
\Lambda(\mathcal{H}, T)=\sum_{D \in \mathcal{D}}(|D|-1)-w(T)+l(\mathcal{H}, T) \\
=2+2+0+0-3+1=2 .
\end{gathered}
$$

From the definition of $[\mathcal{H}]_{2}$ it follows that for a fixed forest $T=(X, E)$, edges of a complete graph generated by an edge $D$ are split into two subsets: those which belong to $T$ ("lie on $T$ ") and those which do not (the remaining edges). Evidently, if $|D|-1$ edges of size 2 belong to $T$ (possible maximum), then the subgraph that they induce on $T$ is connected. If less than $|D|-1$ edges belong to $T$, then those edges induce a disconnected subgraph,
i.e. a forest. Let $E_{D}$ be the set of edges of size 2 which are generated by the 2-section of $D$ and lie on $T$, and $c(T, D)$ be the number of connected components in such a subgraph.

Theorem 8.3.1

$$
\wedge(\mathcal{H}, T)=\sum_{D \in \mathcal{D}}(c(T, D)-1)+l(\mathcal{H}, T) .
$$

Proof. First, notice that for every edge $D$ such that $|D| \geq 2$, the following equality holds :

$$
c(T, D)=|D|-\left|E_{D}\right| .
$$

Second, recall that by definition,

$$
w(T)=\sum_{|D| \geq 2}\left|E_{D}\right| .
$$

Further, since for any singleton $D$, evidently $c(T, D)=1$, we obtain:

$$
\begin{gathered}
\wedge(\mathcal{H}, T)=\sum_{D \in \mathcal{D}}(|D|-1)-w(T)+l(\mathcal{H}, T) \\
=\{\text { ignore the singletons }\}=\sum_{|D| \geq 2}(|D|-1)-w(T)+l(\mathcal{H}, T) \\
=\{\text { insert the weight of the forest }\} \\
=\sum_{|D| \geq 2}(|D|-1)-\sum_{|D| \geq 2}\left|E_{D}\right|+l(\mathcal{H}, T) \\
=\{\text { unite the sum }\}=\sum_{|D| \geq 2}\left(|D|-\left|E_{D}\right|-1\right)+l(\mathcal{H}, T) \\
=\{\text { use (8.5) }\}=\sum_{|D| \geq 2}(c(T, D)-1)+l(\mathcal{H}, T) \\
=\{\text { bring in singletons back }\}=\sum_{D \in \mathcal{D}}(c(T, D)-1)+l(\mathcal{H}, T) .
\end{gathered}
$$ $\square$

For the example in Figure 8.12, formula (8.4) gives:

$$
\wedge(\mathcal{H}, T)=(2-1)+(1-1)+(1-1)+1=2 .
$$

Proposition 8.3.2 For any hypergraph $\mathcal{H}$ and forest $T, \Lambda(\mathcal{H}, T) \geq 0$.
Proof. Apply inequalities (8.2) and $l(\mathcal{H}, T) \geq 0$. $\square$

Theorem 8.3.2 (Acharya, Las Vergnas, 1982) For a connected hypergraph $\mathcal{H}$, $\Lambda(\mathcal{H}, T)=0$ if and only if $\mathcal{H}$ is a hypertree and $T$ is a multi-tree of maximum weight containing all loops of $\mathcal{H}$.

Proof. ⇒ Assume $\Lambda(\mathcal{H}, T)=0$. Formula (8.4) implies $c(T, D)=1$ for any edge $D \in$ $\mathcal{D}$, and, in addition, $l(\mathcal{H}, T)=0$. It means that 2-section of any edge $D \in \mathcal{D}$ induces a connected subgraph in $T$, and all possible loops of $\mathcal{H}$ are in $T$. In other words, since $\mathcal{H}$ is connected there exists a tree $\bar{T}$ (obtained from $T$ by replacing multiple edges with single edges and removing singletons) such that every edge of $\mathcal{H}$ induces a subtree of $\bar{T}$. Hence $\bar{T}$ is a host tree and $\mathcal{H}$ is a hypertree.

Further, since $c(T, D)=1$, inequality (8.2) becomes equality

$$
w(T)=\sum_{D \in \mathcal{D}}(|D|-1) .
$$

Therefore $T$ is the multi-tree of maximum weight. Since it contains all loops of $\mathcal{H}$, the theorem follows.

⇐ Immediately we have $l(\mathcal{H}, T)=0$. Since $T$ is a multi-tree of maximum weight, $w(T)=\sum_{D \in \mathcal{D}}(|D|-1)$, and by (8.3) equality $\wedge(\mathcal{H}, T)=0$ holds. $\square$

Theorem 8.3.3 (Voloshin, 1987) Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph, $x \in X$ a hyper-pendant vertex, $\mathcal{D}(x) \subseteq \mathcal{D}(y)$ for some $y \in X$, and $T$ be a forest of $[\mathcal{H}]_{2}$. Then in $[\mathcal{H}]_{2}$ there exists a forest $T_{1}$ such that

1. $x$ is adjacent to $y$ and pendant in $\overline{T_{1}}$;
2. $w\left(T_{1}\right)=w(T)$.

Theorem 8.3.4 (Voloshin, 1987) Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph, $x \in X, T$ be a forest in $[\mathcal{H}]_{2}, \mathcal{D}_{T}(x)$ denote the set of edges of $T$ incident to $x$, and $m_{2}$ be the number of edges of size 2 from $\mathcal{H}$ not included in $T$. If hypergraph $\mathcal{H}_{1}$ is obtained from $\mathcal{H}$ by weak deletion of $x$, and forest $T_{1}$ is obtained from $T$ by strong deletion of $x$, then:

$$
\wedge(\mathcal{H}, T)=\wedge\left(\mathcal{H}_{1}, T_{1}\right)+|\mathcal{D}(x)|-\left|\mathcal{D}_{T}(x)\right|-m_{2} .
$$

Corollary 8.3.1 Let the conditions of Theorem 8.3.4 hold. Then

$$
\wedge(\mathcal{H}, T)=\wedge\left(\mathcal{H}_{1}, T_{1}\right) \text { if and only if }|\mathcal{D}(x)|=\left|\mathcal{D}_{T}(x)\right|+m_{2} .
$$

An example of a hypergraph $\mathcal{H}$ with a vertex $x$, and a forest $T$ is shown in Figure 8.13. According to the definition,

$$
\wedge(\mathcal{H}, T)=2+2+1+0+0-3+1=3 .
$$

If we weakly delete $x$ from $\mathcal{H}$ and strongly delete $x$ from $T$, we obtain respectively a hypergraph $\mathcal{H}-x$ and a forest $T-x$. Again, according to the definition,

$$
\wedge(\mathcal{H}-x, T-x)=2+1+0+0-2+1=2 .
$$

Now notice that $|\mathcal{D}(x)|=3,\left|\mathcal{D}_{T}(x)\right|=1$, and $m_{2}=1$. Hence,

$$
\wedge(\mathcal{H}-x, T-x)+|\mathcal{D}(x)|-\left|\mathcal{D}_{T}(x)\right|-m_{2}=2+3-1-1=3=\wedge(\mathcal{H}, T) .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-194.jpg?height=945&width=1194&top_left_y=197&top_left_x=277)
Figure 8.13.

Theorem 8.3.5 Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph, $T$ be a forest of maximum weight in $[\mathcal{H}]_{2}, x \in X$ be a vertex pendant and adjacent to $y$ in $\bar{T}$. If hypergraph $\mathcal{H}_{1}$ is obtained from $\mathcal{H}$ and forest $T_{1}$ is obtained from $T$ by weak deletion of $x$, then $T_{1}$ is a forest of maximum weight in $\left[\mathcal{H}_{1}\right]_{2}$, and moreover,

$$
w\left(T_{1}\right)=w(T)-\left|\mathcal{D}_{T}(x)\right| .
$$

Proof. Assume there is another forest, say, $T_{1}^{\prime}$ which is of maximum weight in $\left[\mathcal{H}_{1}\right]_{2}$. Evidently, $w\left(T_{1}^{\prime}\right) \geq w\left(T_{1}\right)$. If $T_{1}$ is not a forest of maximum weight, then $w\left(T_{1}^{\prime}\right) \geq w\left(T_{1}\right)+1$. Consider forest $T_{1}^{\prime}$ in $[\mathcal{H}]_{2}$. To make it spanning add vertex $x$ and connect it with $y$ by $\left|\mathcal{D}_{T}(x)\right|$ edges. Denote the obtained forest by $T^{\prime}$. Then

$$
w\left(T^{\prime}\right)=w\left(T_{1}\right)+\left|\mathcal{D}_{T}(x)\right| \geq w\left(T_{1}\right)+1+\left|\mathcal{D}_{T}(x)\right|=w(T)+1
$$

what contradicts the maximality of $T$. Therefore, $w\left(T_{1}^{\prime}\right)=w\left(T_{1}\right)$ and the theorem follows. $\square$

Generalized cyclomatic number $\Lambda(\mathcal{H}, T)$ depends on the weight of the forest $T$ which can be chosen in many ways from multigraph $[\mathcal{H}]_{2}$. How can we get rid of that dependence? The answer is suggested by Theorem 8.3.2: one need to consider forests of the maximum weight and include all the loops. For a hypergraph $\mathcal{H}$, let

$$
w(\mathcal{H})=\max _{T} w(T) .
$$

Definition 8.3.2 The cyclomatic number of a hypergraph $\mathcal{H}$ is called the value

$$
\wedge(\mathcal{H})=\min _{T} \wedge(\mathcal{H}, T)=\sum_{D \in \mathcal{D}}(|D|-1)-w(\mathcal{H}) .
$$

Theorem 8.3.6 Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph with hyper-pendant vertex $x \in X$, and hypergraph $\mathcal{H}_{1}$ be obtained from $\mathcal{H}$ by weak deletion of $x$. Then

$$
\wedge(\mathcal{H})=\wedge\left(\mathcal{H}_{1}\right) .
$$

Proof. Let $y \in X$ be a twin vertex for $x$. By Theorem 8.3.3, there exists a forest $T$ of maximum weight in $[\mathcal{H}]_{2}$ such that $x$ is pendant and adjacent to $y$ in $\bar{T}$. If $x$ is incident to edges of size 2 in $\mathcal{H}$, then all such edges connect $x$ with $y$ because $x$ is the hyperpendant vertex. Since $T$ is the forest of maximum weight, all such edges belong to $T$. We are able now to apply Theorem 8.3.4 (or, equivalently, Corollary 8.3.1): $m_{2}=0$ and $|\mathcal{D}(x)|=\left|\mathcal{D}_{T}(x)\right|$, and therefore

$$
\wedge(\mathcal{H})=\wedge(\mathcal{H}, T)=\wedge\left(\mathcal{H}_{1}, T_{1}\right) .
$$

By Theorem 8.3.5, forest $T_{1}$ is the forest of maximum weight in $\left[\mathcal{H}_{1}\right]_{2}$ what implies $\Lambda\left(\mathcal{H}_{1}, T_{1}\right)=\Lambda\left(\mathcal{H}_{1}\right)$. Hence, $\Lambda(\mathcal{H})=\Lambda\left(\mathcal{H}_{1}\right)$. $\square$

Theorem 8.3.7 For a hypergraph $\mathcal{H}$, the following statements are equivalent:

1. $\mathcal{H}$ can be decomposed by sequential weak deletions of hyper-pendant vertices and singletons;
2. $\wedge(\mathcal{H})=0$;
3. $\mathcal{H}$ is a hypertree.

Proof. $1 \Rightarrow 2$ : Apply Theorem 8.3.6 and evident fact that singletons do not contribute to $\Lambda(\mathcal{H})$.
$2 \Rightarrow 3$ : Apply Theorem 8.3.2.
$3 \Rightarrow 1$ : Apply Theorem 8.2.1. $\square$

We now conclude by presenting an algorithm for computing $\wedge(\mathcal{H})$.

Algorithm 8.3.1 Computation of $\wedge(\mathcal{H})$
INPUT: A hypergraph $\mathcal{H}$.
OUTPUT: $\wedge(\mathcal{H})$.

1. Construct 2-section $[\mathcal{H}]_{2}$.
2. In $[\mathcal{H}]_{2}$, delete all loops and replace multiple edges with single edges having weight equal to the multiplicity. Obtain a weighted graph $G$.

3. In $G$, find a spanning tree $T$ of maximum weight $w(\mathcal{H})$.
4. Compute $\Lambda(\mathcal{H})=\sum_{D \in \mathcal{D}}(|D|-1)-w(\mathcal{H})$.
5. Output $\wedge(\mathcal{H})$.

Step 3 of the algorithm may use Kruskal's Algorithm 2.3.1 for maximum spanning tree, see Section 2.3.

Exercises 8.3.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-196.jpg?height=432&width=1129&top_left_y=792&top_left_x=321)
Figure 8.14.

1. For each of the hypergraphs in Figure 8.14, construct the generalized 2-section, choose a (multi)-forest and compute its weight. Verify the inequality (8.2).
2. Compute the generalized cyclomatic number with respect to forest chosen in 1.
3. In each case of 2., verify the equality (8.4).
4. In each of the hypergraphs in Figure 8.14, weakly delete a vertex and verify the equality (8.6).
5. For each of the hypergraphs in Figure 8.14, compute the cyclomatic number.

Computer Projects 8.3. Write a program for the following algorithmic problems.

1. Given a hypergraph $\mathcal{H}$, apply Algorithm 8.3.1 to compute cyclomatic number $\wedge(\mathcal{H})$.
2. Given a hypergraph $\mathcal{H}$, find a set of edges which after weak deletion leaves a hypertree.

## Chapter 9

## Some Other Remarkable Hypergraph Classes

"Beauty is in the eyes of the beholder..."

There are several classes of hypergraphs which have nice structural properties. Most of them have been introduced as generalizations of bipartite graphs and therefore are related to colorings. In this section, we consider a few of them; proper hypergraph colorings will be discussed in the next chapter.

### 9.1. Balanced Hypergraphs

Let us recall that in a hypergraph $\mathcal{H}=(X, \mathcal{D})$, an alternating sequence

$$
\mu=x_{0} D_{0} x_{1} D_{1} x_{2} \ldots x_{t-1} D_{t-1} x_{t}
$$

of distinct vertices $x_{0}, x_{1}, x_{2}, \ldots, x_{t-1}$ and distinct edges $D_{0}, D_{1}, D_{2}, \ldots D_{t-1}$ satisfying $x_{i}, x_{i+1} \in D_{i}, i=0,1, \ldots, t-1$, is called a cycle if $x_{t}=x_{0}$. The value of $t$ is called the length of the cycle. A cycle is called odd or even if its length is odd or even respectively. As one can see, in cycles vertices and edges play a similar role: every edge of a cycle contains two consecutive vertices, and every vertex is contained in two consecutive edges. This fact is widely used in duality of hypergraphs.

A hypergraph $\mathcal{H}$ is called balanced if every odd cycle of length $\geq 3$ has an edge containing three vertices of the cycle; it is called totally balanced if every cycle of length $\geq 3$ has an edge containing three vertices of the cycle. A cycle itself is called balanced if it contains an edge having three vertices of the cycle. Evidently, the totally balanced hypergraph is balanced.

An example of a balanced cycle is shown in Figure 9.1. Notice that hypergraph itself is not balanced.

Since cycles represent partial subhypergraphs (with possible isolated vertices), every partial subhypergraph of a (totally) balanced hypergraph is (totally) balanced.

Proposition 9.1.1 The dual of a (totally) balanced hypergraph is (totally) balanced.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-198.jpg?height=624&width=743&top_left_y=212&top_left_x=505)
Figure 9.1. Balanced cycle.

Proof. Indeed, if an edge contains three vertices of the cycle, it means that one vertex is contained in three edges of the cycle. When taking dual hypergraph, cycles become cycles of the same length, so the assertion follows. $\square$

Theorem 9.1.1 (Berge) A hypergraph $\mathcal{H}$ is balanced if and only if every subhypergraph $\mathcal{H}^{\prime}$ obtained from $\mathcal{H}$ by weak deletions of vertices is 2-colorable.

The hypergraph shown in Figure 9.1 is not balanced because weak deletion of all pendant vertices and one lower vertex results in a graph having a triangle.

Theorem 9.1.2 (Berge, Las Vergnas, 1970) A hypergraph is balanced if and only if every partial subhypergraph has the König property.

Since balanced hypergraphs are invariant with respect to duality, they also posses the dual König property.

Corollary 9.1.1 (Berge) Every balanced hypergraph has the Helly property and is conformal.

Proof. Let $\mathcal{H}$ be a balanced hypergraph and let $\mathcal{H}^{\prime} \subseteq \mathcal{H}$ be an intersecting family. By Theorem 9.1.2, $\tau\left(\mathcal{H}^{\prime}\right)=v\left(\mathcal{H}^{\prime}\right)$. But $v\left(\mathcal{H}^{\prime}\right)=1$ because any matching contains maximum one edge from every intersecting family. Thus, $\tau\left(\mathcal{H}^{\prime}\right)=1$ what means there exists a vertex common to all the edges of $\mathcal{H}^{\prime}$, i.e. $\mathcal{H}^{\prime}$ is a star. Therefore $\mathcal{H}$ is a Helly hypergraph. Since the dual of a balanced hypergraph is balanced, we conclude that $\mathcal{H}$ is conformal. $\square$

Corollary 9.1.2 Every totally balanced hypergraph is a hypertree.
Proof. Let $\mathcal{H}$ be a totally balanced hypergraph. Since every cycle of length $>3$ has an edge incident to three vertices of the cycle, the line graph $L(\mathcal{H})$ is a chordal graph. Since $\mathcal{H}$ is balanced, it is a Helly hypergraph. Corollary 8.1.1 implies that $\mathcal{H}$ is a hypertree. $\square$

Corollary 9.1.3 Every totally balanced hypergraph is a chordal conformal hypergraph.
Proof. Let $\mathcal{H}$ be a totally balanced hypergraph. Since every cycle of length $>3$ has an edge incident to three vertices of the cycle, the 2-section $(\mathcal{H})_{2}$ is a chordal graph and $\mathcal{H}$ is a chordal hypergraph. Since $\mathcal{H}$ is balanced, it is a conformal hypergraph. Hence $\mathcal{H}$ is a chordal conformal hypergraph. $\square$

Exercises 9.1.

1. Which of the graphs $K_{n},, K_{m, n}, W_{n}$, prism, cube and Petersen graph are balanced hypergraphs?
2. Which graphs are totally balanced hypergraphs?
3. Give an example of a hypertree which is not a totally balanced hypergraph.
4. Give an example of a chordal conformal hypergraph which is not a totally balanced hypergraph.

### 9.2. Interval Hypergraphs

A hypergraph $\mathcal{H}=(X, \mathcal{D})$ is called an interval hypergraph if there exists a linear ordering of the vertices $x_{1}, x_{2}, \ldots, x_{n}$ such that every $D \in \mathcal{D}$ induces an interval in this ordering. In other words, the vertices of $X$ can be placed on the real line such that every hyperedge is an interval, see Figure 9.2.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-199.jpg?height=316&width=1230&top_left_y=1465&top_left_x=277)
Figure 9.2. Interval hypergraph.

Theorem 9.2.1 If $\mathcal{H}$ is an interval hypergraph, then it is Helly and graph $L(\mathcal{H})$ is chordal.
Proof. Any interval hypergraph $\mathcal{H}$ is a hypertree because in this case a host graph is a simple path. Apply Corollary 8.1.1. $\square$

Theorem 9.2.2 If $\mathcal{H}$ is an interval hypergraph without included edges, then the dual $\mathcal{H}^{*}$ is an interval hypergraph, too.

Proof. Indeed, suppose the vertices of $\mathcal{H}$ are placed on the real line in such an ordering that each edge is an interval. Order the edges of $\mathcal{H}$ by the very left vertex in each edge. Since there are no included edges, every vertex is the very left vertex for at most one edge. So, we have uniquely determined linear ordering of the edges. Now observe that for each vertex all incident edges appear in this ordering. That means the dual hypergraph $\mathcal{H}^{*}$ is an interval hypergraph. $\square$

Figure 9.2 shows two interval hypergraphs which are dual to each other.
Theorem 9.2.3 Every interval hypergraph is totally balanced.
Proof. Suppose $\mathcal{H}$ is an interval hypergraph and the vertices are points on the real line in order from left to right. Consider any cycle of length $\geq 3$. The very left edge of the cycle intersects with the second edge, the second with the third and so on around the cycle. Sooner or later the last edge must intersect the very first edge; it means it contains at least three vertices of the cycle. Hence $\mathcal{H}$ is totally balanced. $\square$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-200.jpg?height=507&width=1124&top_left_y=981&top_left_x=300)
Figure 9.3.

There are totally balanced hypergraphs which are not the interval hypergraphs, and there are hypertrees which are not balanced, see Figure 9.3, $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ respectively.

Exercises 9.2.

1. Which graphs are interval hypergraphs?
2. Explain why cycle $C_{n}, n \geq 3$ is not an interval hypergraph.
3. Construct an example of a hypertree on $\geq 4$ vertices which is not an interval hypergraph.
4. Construct an example of a totally balanced hypergraph on $\geq 4$ vertices which is not an interval hypergraph.
5. A graph $G$ is called an interval graph if there exists an interval hypergraph $\mathcal{H}$ such that $G=L(\mathcal{H})$. Evidently, any interval graph is chordal. Construct an example of a chordal graph which is not an interval graph.

### 9.3. Normal Hypergraphs

Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph. The chromatic index of $\mathcal{H}$ is the minimum number of colors needed to color the edges of $\mathcal{H}$ such that no two intersecting edges have the same color. As for graphs, we denote it by $\chi^{\prime}(\mathcal{H})$. Clearly, $\chi^{\prime}(\mathcal{H})=\chi(L(\mathcal{H}))$. Now we have the following relation:

$$
\chi^{\prime}(\mathcal{H}) \geq \omega(L(\mathcal{H})) \geq \Delta(\mathcal{H}) .
$$

We state that hypergraph $\mathcal{H}$ has the edge-coloring property if $\chi^{\prime}(\mathcal{H})=\Delta(\mathcal{H})$. The edge-coloring property means that if we take dual hypergraph $\mathcal{H}^{*}$, then $\chi\left(\left(\mathcal{H}^{*}\right)_{2}\right)=$ $\omega\left(\left(\mathcal{H}^{*}\right)_{2}\right)$.

At last, a hypergraph $\mathcal{H}$ is called normal if every partial hypergraph $\mathcal{H}^{\prime} \subseteq \mathcal{H}$ has the edge-coloring property, i.e.

$$
\chi^{\prime}\left(\mathcal{H}^{\prime}\right)=\Delta\left(\mathcal{H}^{\prime}\right) .
$$

One can prove that any balanced hypergraph is normal and therefore has edge-coloring property. The example of hypergraph $\mathcal{H}_{2}$ in Figure 9.3 shows that the converse is not true: $\mathcal{H}_{2}$ is a normal hypergraph but it is not balanced.

Theorem 9.3.1 Any hypertree is a normal hypergraph.
Proof. Indeed, every partial hypergraph of a hypertree is a hypertree; in addition, it is Helly and the line graph is a chordal graph which is perfect. Therefore for a hypertree $\mathcal{H}$ itself and for any partial hypergraph we have the required equality:

$$
\chi^{\prime}(\mathcal{H})=\chi(L(\mathcal{H}))=\omega(L(\mathcal{H}))=\Delta(\mathcal{H}) .
$$ $\square$

Theorem 9.3.2 (Fournier, Las Vergnas, 1972) Every normal hypergraph is 2-colorable.
Theorem 9.3.3 (Lovász, 1972) For any hypergraph $\mathcal{H}$, the following conditions are equivalent:

1. $\mathcal{H}$ is normal;
2. every partial hypergraph $\mathcal{H}^{\prime} \subseteq \mathcal{H}$ has the König property.

Corollary 9.3.1 A hypergraph $\mathcal{H}$ is normal if and only if $\mathcal{H}$ satisfies the Helly property and $L(\mathcal{H})$ is a perfect graph.

Proof. ⇒ Let $\mathcal{H}$ be a normal hypergraph. By Theorem 9.3.3 every partial hypergraph $\mathcal{H}^{\prime} \subseteq \mathcal{H}$ has the König property. In particular, if $\mathcal{H}^{\prime}$ is an intersection family, then $\tau\left(\mathcal{H}^{\prime}\right)=\mathcal{V}\left(\mathcal{H}^{\prime}\right)=1$ what implies that $\mathcal{H}$ is a Helly hypergraph. The last means that $\mathcal{H}^{*}$ is conformal. Further, $\chi^{\prime}(\mathcal{H})=\Delta\left(\mathcal{H}^{\prime}\right)$ means $\chi\left(\left(\mathcal{H}^{*}\right)_{2}\right)=\omega\left(\left(\mathcal{H}^{*}\right)_{2}\right)$, and this equality holds for every induced subgraph of $\left(\mathcal{H}^{*}\right)_{2}$, i.e. graph $\left(\mathcal{H}^{*}\right)_{2}$ is perfect. Since $L(\mathcal{H})=\left(\mathcal{H}^{*}\right)_{2}$, the implication follows.

⇐ Assume that $\mathcal{H}$ satisfies the Helly property and $L(\mathcal{H})$ is a perfect graph. Then in dual hypergraph $\mathcal{H}^{*}$ the maximal edges are the maximal cliques of graph $\left(\mathcal{H}^{*}\right)_{2}=L(\mathcal{H})$. Observe that $\chi\left(\left(\mathcal{H}^{*}\right)_{2}\right)=\omega\left(\left(\mathcal{H}^{*}\right)_{2}\right)$ because $L(\mathcal{H})$ is perfect; this means that $\chi^{\prime}(\mathcal{H})=$
$\Delta(\mathcal{H})$. Since by the same reason the last equality holds for every $\mathcal{H}^{\prime} \subseteq \mathcal{H}$, the hypergraph $\mathcal{H}$ is normal. $\square$

In fact, normal hypergraphs have been introduced by Lovász in 1972 as Helly hypergraphs having a perfect line graph. They represent a remarkable example when an outstanding graph-theoretic problem was first solved using hypergraph approach. The Berge's weak perfect graph conjecture that graph is perfect if and only if its complement is perfect (see Theorem 5.7.1), was first proved via normal hypergraphs. Namely, it followed from Theorem 9.3.3 by establishing such a fundamental fact that in normal hypergraphs every partial hypergraph has the König property. After that, a pure graph-theoretic proof was found. This is not a unique case when a problem was first solved using hypergraphs and then the solution was re-phrased using a different terminology.

## Exercises 9.3.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-202.jpg?height=507&width=1126&top_left_y=948&top_left_x=321)
Figure 9.4.

1. Which of the graphs $K_{n}, K_{m, n}, C_{n}, W_{n}$, cube, prism and Petersen graph are normal hypergraphs?
2. Which of the hypergraphs in Figure 9.4 is normal or not and why?
3. Which of the hypergraphs in Figure 9.4 satisfies the König property?
4. For each of the hypergraphs in Figure 9.4 find the chromatic index and respective edge coloring.
5. Which of the hypergraphs in Figure 9.4 has the edge-coloring property?

### 9.4. Planar Hypergraphs

Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph. Recall that a bipartite representation of $\mathcal{H}$ is the bipartite graph $B(\mathcal{H})$ with vertex set $X \cup \mathcal{D}$. The vertex $x \in X$ is adjacent to the vertex $d \in \mathcal{D}$ in $B(\mathcal{H})$ if and only if $x \in D$ in $\mathcal{H}$. A hypergraph $\mathcal{H}$ is called planar if and only if $B(\mathcal{H})$ is a planar graph.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-203.jpg?height=1515&width=1134&top_left_y=562&top_left_x=316)
Figure 9.5. Planar hypergraph $\mathcal{H}$.

Thus, planar graphs are the special case of planar hypergraphs in which all edges have size 2. As one may see, a planar hypergraph admits an embedding in the plane in such a way that each vertex corresponds to a point in the plane, and every edge corresponds to a closed region homeomorphic to a disk. The region contains (in its boundary) the points corresponding to the vertices of the edge, and does not contain the points corresponding to the other vertices. Furthermore, two such regions intersect exactly in the points that correspond to the vertices in the intersection of the corresponding edges. In this way, the connected regions of the plane which do not correspond to the edges form the faces of the embedding of the planar hypergraph. As for graphs, the size of a face (region) is the number of vertices on the boundary.

An example of a planar hypergraph $\mathcal{H}$ is shown in Figure 9.5. First, we may draw edges of size two as ellipses containing the respective vertices and vice versa, see the top of the figure. Each time we draw edges of size two, we keep in mind this understanding. Further, if a hypergraph is planar, we show how the usual drawing of edges of $\mathcal{H}$ (namely, edges $D_{1}$ and $D_{2}$ ) can be re-drawn in such a way that hyperedges intersect only at the neighborhoods of common vertices. In this way, the regions corresponding to the two faces $f_{1}$ and $f_{2}$ appear. One can see that in the plane embedding of $\mathcal{H}$ face $f_{1}$ is an interior face of size 2 while $f_{2}$ is an unbounded face of size 4. If for every edge we put a vertex "at the center" and connect it with the original vertices of the very same edge, we obtain a plane embedding of the bipartite representation $B(\mathcal{H})$. The figure also shows two drawings of $B(\mathcal{H})$, with original vertices $1,2,3$, and 4 , and the vertices corresponding to edges $D_{1}$ and $D_{2}$.

Using properties of bipartite representation $B(\mathcal{H})$, one can derive many properties of a plane embedding of the hypergraph $\mathcal{H}$.

Proposition 9.4.1 A hypergraph $\mathcal{H}$ is planar if and only if dual hypergraph $\mathcal{H}^{*}$ is planar.
Proof. If $\mathcal{H}$ is planar hypergraph, then bipartite representation $B(\mathcal{H})$ is a planar graph. Bipartite representation of $B\left(\mathcal{H}^{*}\right)$ is obtained from $B(\mathcal{H})$ by simply interchanging the roles of parts. Hence $B\left(\mathcal{H}^{*}\right)$ is planar, and therefore $\mathcal{H}^{*}$ is planar. $\square$

In contrast to graphs, in plane embeddings of hypergraphs the singletons are drawn as circles and not as loops. Therefore the singletons, if added to a hypergraph do not form new faces. With this agreement the plane embedding of the dual hypergraph $\mathcal{H}^{*}$ is also shown in Figure 9.5.

Recalling that the degree of a vertex $x \in X$ in $\mathcal{H}$ is $|\mathcal{D}(x)|$ we obtain the following generalization of Euler's formula for hypergraphs:

Theorem 9.4.1 (Euler's formula) Let $\mathcal{H}=(X, \mathcal{D}),|X|=n,|\mathcal{D}|=m$, be a planar hypergraph embedded in the plane with $f$ faces. Then

$$
n-\sum_{i=1}^{m}\left(\left|E_{i}\right|-1\right)+f=m-\sum_{j=1}^{n}\left(\left|\mathcal{D}\left(x_{j}\right)\right|-1\right)+f=2 .
$$

Proof. [6] Construct the planar embedding of the bipartite graph $B(\mathcal{H})$. It contains $n^{\prime}=$ $n+m$ vertices,

$$
m^{\prime}=\sum_{j=1}^{m}\left|D_{j}\right|=\sum_{i=1}^{n}\left|\mathcal{D}\left(x_{i}\right)\right|
$$

edges and $f^{\prime}=f$ faces. Since $B(\mathcal{H})$ is a planar graph, by Theorem 4.2.1, Euler's formula gives:

$$
n^{\prime}-m^{\prime}+f^{\prime}=2
$$

Therefore, using the first equality of (9.1), we have

$$
n-\sum_{i=1}^{m}\left(\left|D_{i}\right|-1\right)+f=2
$$

and, using the second equality of (9.1), we obtain

$$
m-\sum_{j=1}^{n}\left(\left|\mathcal{D}\left(x_{j}\right)\right|-1\right)+f=2
$$ $\square$

For example, for the plane embedding of $\mathcal{H}$ in Figure 9.5 we have:

$$
n-\sum_{i=1}^{m}\left(\left|E_{i}\right|-1\right)+f=4-(2+2)+2=2
$$

and

$$
\left.m-\sum_{j=1}^{n}\left(\left|\mathcal{D}\left(x_{j}\right)\right|-1\right)+f=2-(0+1+0+1)+2\right)=2 .
$$

A planar hypergraph is called maximal if it is simple (i.e., does not contain included edges) and adding any new edge of size $\geq 2$ makes it non planar. Consequently, an embedding of a planar hypergraph is called maximal if and only if every face has size 2, or equivalently, if and only if in the corresponding embedding of $B(\mathcal{H})$ every face has size 4.

This maximality is relative in the sense that in every such face one can insert an additional edge of size 2. However, if a planar hypergraph $\mathcal{H}$ is not maximal, then there is at least one face of size at least 3, and therefore one can insert an additional edge of size at least 3 in that face.

If we draw the faces of a maximal planar hypergraph as curves connecting the respective two vertices, then we obtain a plane graph whose faces correspond to the edges of the initial hypergraph. In this way, a plane graph corresponds to a planar embedding of a maximal hypergraph such that the faces of the graph correspond to the edges of the hypergraph.

Notice that this "face-hyperedge" duality is different from both the hypergraph duality ("vertices - hyperedges") and the classic planar graph duality ("vertices - faces", see Section 4.5.).

An example of maximal embedding of a planar hypergraph is shown in Figure 9.6. It is complete 3-uniform hypergraph $K_{4}^{3}$. Regions representing faces are denoted by $f_{1}, f_{2}, f_{3}, f_{4}, f_{5}$ and $f_{6}$. Notice that all the faces have size 2, and face $f_{6}$ is unbounded. Faces $f_{1}, \ldots, f_{6}$ can be seen as the edges of size 2 connecting the respective pairs of vertices: face $f_{1}$ "connects" vertices 1 and 2, face $f_{2}$ "connects" vertices 1 and 4 and so on. Unbounded face $f_{6}$ "connects" vertices 1 and 3 . In this way the figure turns into a plane embedding of the simple complete graph $K_{4}$ which is drawn below.

There are six edges in the plane embedding of $K_{4}$, and each corresponds to a face from the plane embedding of $K_{4}^{3}$ and vice versa. There are four faces in the plane embedding of

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-206.jpg?height=1623&width=1054&top_left_y=236&top_left_x=347)
Figure 9.6. Maximal planar hypergraph $K_{4}^{3}$ and its "face-hyperedge" dual $K_{4}$.

$K_{4}$, and each corresponds to a hyperedge from the plane embedding of $K_{4}^{3}$ and vice versa. In this way the duality "face-hyperedge" is observed directly and it is different from the hypergraph duality and the classic planar graph duality of $K_{4}^{3}$ and $K_{4}$ respectively.

## Exercises 9.4.

1. For each hypergraph $\mathcal{H}$ in Figure 9.7, construct its dual $\mathcal{H}^{*}$, bipartite representation $B(\mathcal{H})$ and $B\left(\mathcal{H}^{*}\right)$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-207.jpg?height=507&width=1121&top_left_y=422&top_left_x=324)
Figure 9.7.
2. Determine which of the hypergraphs in Figure 9.7 is planar and draw both a plane embedding of $\mathcal{H}$ and $\mathcal{H}^{*}$. In both cases, verify the Euler's formula.
3. For planar hypergraph in Figure 9.7, add a hyperedge of size 3 to make its embedding maximal.
4. For a non-planar hypergraph in Figure 9.7, weakly (strongly) delete an edge/a vertex and find a plane embedding (if it exists) of an obtained hypergraph and its dual.

Computer Projects 9.4. Write a program for the following algorithmic problems.

1. Given a hypergraph $\mathcal{H}$, construct bipartite representation $B(\mathcal{H})$.
2. Given a planar hypergraph $\mathcal{H}$, construct its plane embedding.
3. Given a plane embedding of a hypergraph $\mathcal{H}$, determine if it is maximal.
4. Given a hypergraph $\mathcal{H}$, determine if it is planar, and if yes, construct a plane embedding.
5. Given a plane embedding of a hypergraph $\mathcal{H}$, and a face $f$, construct such a plane embedding of $\mathcal{H}$ that $f$ is an unbounded face.

## Chapter 10

## Hypergraph Coloring

"Graph coloring unfolding: unforeseen features of unforeseen generalizations..."

### 10.1. Basic Kinds of Classic Hypergraph Coloring

In this chapter we use some parts adapted and updated from research monograph [6]. As in graph coloring, let $\{1,2, \ldots, \lambda\}$ be the set of available colors. A proper $\lambda$-coloring of a hypergraph $\mathcal{H}=(X, \mathcal{D})$ is a labeling of its vertices $X$ with the colors from set $\{1,2, \ldots, \lambda\}$ in such a way that every edge $D \in \mathcal{D}$ such that $|D| \geq 2$ has at least two vertices colored differently. In other words, in any proper coloring no edge of size $\geq 2$ is monochromatic. We do not necessarily have to use all $\lambda$ colors. When considering the colorings we ignore the edges of size $\leq 1$, which is equivalent to the preliminary weak deletion of all such elements from the family $\mathcal{D}$. A proper $\lambda$-coloring sometimes is called a weak coloring of a hypergraph. The minimum $\lambda$ for which there exists a proper $\lambda$-coloring is called the chromatic number of $\mathcal{H}$ and is denoted by $\chi(\mathcal{H})$. Since every vertex gets one color, the maximum number of different colors that may actually be used in any $\lambda$-coloring is at most $n(\mathcal{H})$. If $\lambda>n$, then in every $\lambda$-coloring at least one color remains unused. Proper $\lambda$-colorings exist for every finite $\lambda \geq n$.

If $\mathcal{H}$ is a simple hypergraph with all edges of size two, then it is a simple graph and we obtain a usual classic graph coloring as studied in Chapter 5. Since in a proper coloring of a graph no edge is monochromatic, this requirement directly generalizes to any hyperedge of size $\geq 2$. As the loops are ignored in graph coloring, the singletons are ignored in hypergraph coloring. An important point, however, is that graph coloring, as we shall see, may have many different generalizations.

A $\lambda$-coloring of $\mathcal{H}=(X, \mathcal{D})$ which uses precisely $k \leq \lambda$ colors defines a feasible partition of $X$ into $k$ stable sets $S_{1}, S_{2}, \ldots, S_{k}$ called color classes. Each color class $S_{i}$ represents a set of vertices colored with color $i$. Therefore there is no edge inside any of $S_{i}$. Thus we have the following:

$$
X=\cup_{i=1}^{k} S_{i}, \quad S_{i} \neq \emptyset, \quad S_{i} \cap S_{j}=\emptyset, i \neq j .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-210.jpg?height=598&width=709&top_left_y=259&top_left_x=531)
Figure 10.1.

Proposition 10.1.1 Let $\mathcal{H}$ be a hypergraph of order $n$ with stability number $\alpha(\mathcal{H})$, transversal number $\tau(\mathcal{H})$ and chromatic number $\chi(\mathcal{H})$. Then the following inequalities hold:

$$
\begin{gathered}
\alpha(\mathcal{H}) \chi(\mathcal{H}) \geq n ; \\
\chi(\mathcal{H}) \leq \tau(\mathcal{H})+1=n-\alpha(\mathcal{H})+1 .
\end{gathered}
$$

Proof. The first inequality follows from equality (10.1) because in an optimal proper coloring of $\mathcal{H}$ with $\chi(\mathcal{H})$ colors, $\left|S_{i}\right| \leq \alpha(\mathcal{H})$.

The second inequality is obtained by the following reasoning: choose a minimum transversal of $\mathcal{H}$ and color it with $\tau(\mathcal{H})$ colors; then color the remaining vertices of $\mathcal{H}$ with a new color. Since we obtain a proper coloring of $\mathcal{H}$ and use $\tau+1$ colors, the chromatic number $\chi$ cannot be greater than $\tau+1=n-\alpha+1$. $\square$

An example of a hypergraph $\mathcal{H}$ and a proper 3-coloring is shown in Figure 10.1. As one can easily see, $\tau(\mathcal{H})=2$, respectively $\alpha(\mathcal{H})=3$, and $\chi(\mathcal{H})=2$. The coloring produces a feasible partition of the vertex set into three color classes. Vertices of color 1 and 2 represent a minimum transversal, and vertices of color 3 represent a maximum independent set. The inequality $\alpha(\mathcal{H}) \chi(\mathcal{H}) \geq n$ turns into $3 \cdot 2 \geq 5$, and $\chi(\mathcal{H}) \leq \tau(\mathcal{H})+1$ into $2 \leq 2+1$.

There are some restrictive types of hypergraph coloring that are regularly encountered in the literature, see for example [1, 2].

Strong colorings. A strong $\lambda$-coloring of $\mathcal{H}$ is a coloring of the vertices using at most $\lambda$ colors in such a way that every edge $D \in \mathcal{D}$ is polychromatic, i.e. has all vertices colored differently. The strong chromatic number $\gamma(\mathcal{H})$ is the smallest $\lambda$ for which there exists a strong $\lambda$-coloring of $\mathcal{H}$. It follows that $\gamma(\mathcal{H}) \geq \chi(\mathcal{H})$ because every strong coloring is also a weak coloring. Evidently the strong and weak colorings coincide when $\mathcal{H}$ is a graph. In addition, strong coloring is nothing else than a proper $\lambda$-coloring of the graph $(\mathcal{H})_{2}$, the 2-section of $\mathcal{H}$. Since any graph, as a special case of a hypergraph, is a 2-section of itself, strong colorings do not add anything new to coloring theory.

Equitable colorings. An equitable $\lambda$-coloring of $\mathcal{H}=(X, \mathcal{D})$ is a partition of $X$ into $\lambda$ stable sets $S_{i}, i=1,2, \ldots, \lambda$, such that for every $D \in \mathcal{D}$, and for every $i$ the following inequalities hold:

$$
\left\lfloor\frac{|D|}{\lambda}\right\rfloor \leq\left|D \cap S_{i}\right| \leq\left\lceil\frac{|D|}{\lambda}\right\rceil,
$$

where $\lfloor r\rfloor$ is the largest integer not greater than $r$, and $\lceil r\rceil$ is the smallest integer not smaller than $r$.

Good colorings. A good $\lambda$-coloring of $\mathcal{H}$ is a partition of $X$ into $\lambda$ stable sets $S_{i}$, $i=1,2, \ldots, \lambda$, such that each $D \in \mathcal{D}$ has

$$
\min \{|D|, \lambda\}
$$

colors. If

$$
\lambda \leq \min _{D \in \mathcal{D}}|D|,
$$

then every $S_{i}$ forms a transversal of $\mathcal{H}$. If $\lambda \geq \max _{D \in \mathcal{D}}|D|$, then a good $\lambda$-coloring is a strong $\lambda$-coloring. Finally, for every $\lambda$, any equitable $\lambda$-coloring is also a good $\lambda$-coloring.

Uniform colorings. For a hypergraph $\mathcal{H}$ of order $n$, a proper $\lambda$-coloring $\left(S_{1}, S_{2}, \ldots, S_{\lambda}\right)$ is uniform if the number of vertices of the same color is always the same (to within one), i.e.

$$
\left\lfloor\frac{n}{\lambda}\right\rfloor \leq\left|S_{i}\right| \leq\left\lceil\frac{n}{\lambda}\right\rceil .
$$

The problem of the existence of uniform colorings arises in numerous scheduling problems.
I-regular colorings. For every edge $D_{j} \in \mathcal{D}$ of size at least two in $\mathcal{H}$, let there be two corresponding integers $a_{j}, b_{j}$ such that

$$
0 \leq a_{j} \leq b_{j} \leq\left|D_{j}\right| .
$$

An I-regular $\lambda$-coloring of $\mathcal{H}$ is a partition of $X$ into $\lambda$ stable sets $S_{i}, i=1,2, \ldots, \lambda$, in such a way that for every $D_{j} \in \mathcal{D}$, and every $i=1,2, \ldots, \lambda$ we have

$$
a_{j} \leq\left|D_{j} \cap S_{i}\right| \leq b_{j} .
$$

Notice that each weak coloring is an I-regular coloring if $a_{j}=0$ and $b_{j}=\max \left\{1,\left|D_{j}\right|-1\right\}$; every strong coloring is an I-regular coloring with $a_{j}=0$ and $b_{j}=1$; an arbitrary equitable coloring is an I-regular coloring with $a_{j}=\left\lfloor\frac{\left|D_{j}\right|}{\lambda}\right\rfloor$ and $b_{j}=\left\lceil\frac{\left|D_{j}\right|}{\lambda}\right\rceil$.

Remark. On one hand, I-regular colorings seem to be the most general. On the other hand, it is not so. Suppose we want to express that for such colorings some $D_{j}$ must have at least two vertices of the same color. Hence $D_{j}$ may be monochromatic. If it is monochromatic and we use at least two colors, then some color is missing and some color uses all the vertices of $D_{j}$. Therefore, in the language of I-regular colorings, we must put $a_{j}=0$, $b_{j}=\left|D_{j}\right|$. The last is equivalent to having no constraint on the coloring of $D_{j}$, i.e. it is equivalent to considering all I-regular colorings of $\mathcal{H}$ without $D_{j}$. To express the condition above it is necessary to require the following: in every coloring there exists an $i$ such that $\left|S_{i} \cap D_{j}\right| \geq 2$. The point of this remark is that all graph generalizations of colorings described above miss a case.

As in graphs, cycles play an important role in hypergraph colorings. Recall that $\Lambda(\mathcal{H})$ denotes the cyclomatic number of a hypergraph, see Section 8.3.

Theorem 10.1.1 For any hypergraph $\mathcal{H}=(X, \mathcal{D})$,

$$
\chi(\mathcal{H}) \leq \wedge(\mathcal{H})+2 .
$$

Proof. We use Algorithm 8.3.1 that computes the cyclomatic number of $\mathcal{H}$. Let $T=$ $(X, E)$ be the spanning tree in the weighted graph $G$ constructed in Step 2. Starting at any vertex, color the vertices of $T$ with two colors by alternating the colors along the tree. Those edges of $\mathcal{H}$ which have two adjacent vertices in $T$ are colored properly. The number of remaining edges is at most $\Lambda(\mathcal{H})$. Using a new color for each of them, we obtain a proper coloring of $\mathcal{H}$ with $\wedge(\mathcal{H})+2$ colors. $\square$

Next, we cite some significant results in this direction. For details we refer the reader to [2, 8].

Theorem 10.1.2 (Erdös, Hajnal, 1966) For any natural numbers $h, k, l$, all $\geq 2$, there exists an h-uniform hypergraph $\mathcal{H}=(X, \mathcal{D})$ such that $\chi(\mathcal{H})=k$ and $\mathcal{H}$ contains no cycles of length $<l$.

A hypergraph $\mathcal{H}$ is edge-critical if it contains no isolated vertices, $\chi(\mathcal{H})=k, k \geq 3$, and weak deletion of any edge results in a hypergraph $\mathcal{H}^{\prime}$ with $\chi\left(\mathcal{H}^{\prime}\right)=k-1$.

Lemma 10.1.1 (Zykov, 1974) Any hypergraph $\mathcal{H}$ with $\chi(\mathcal{H}) \geq 3$ can be transformed into an edge-critical hypergraph by weak deletion of edges and vertices of degree $\leq 1$.

The intersections of edges in cycles appear to be also important:
Theorem 10.1.3 (Zykov, 1974) In each edge-critical hypergraph $\mathcal{H}$ with $\chi(\mathcal{H})=3$ there exists an odd cycle such that no three of its edges share a common vertex.

Corollary 10.1.1 (Fournier, Las Vergnas, 1972) If in a hypergraph $\mathcal{H}$ every odd cycle has three edges that share a common vertex, then $\chi(\mathcal{H})=2$.

Numerous papers study the smallest number of edges (or the largest number of edges) which an $r$-uniform hypergraph on $n$ vertices can have if $\chi(\mathcal{H})>k(\chi(\mathcal{H}) \leq k)$; these are often referred to as "extremal problems related to the chromatic number of a hypergraph". In most papers the results are obtained by probabilistic methods.

Nevertheless, one of the well developed direction in classic hypergraph coloring is the investigation of bi-chromatic hypergraphs, i.e. hypergraphs with $\chi(\mathcal{H})=2$, as generalizations of bipartite graphs. A detailed exposition of this topics can be found in the last chapter of [2].

## Exercises 10.1.

1. For hypergraph $\mathcal{H}$ in Figure 10.2, find the chromatic number $\chi(\mathcal{H})$, a respective proper coloring and a feasible partition.
2. For hypergraph $\mathcal{H}$ in Figure 10.2, determine $\alpha(\mathcal{H}), \tau(\mathcal{H})$ and verify the inequalities of Proposition 10.1.1

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-213.jpg?height=458&width=924&top_left_y=225&top_left_x=417)
Figure 10.2.

3. For hypergraph $\mathcal{H}$ in Figure 10.2, find the strong chromatic number $\gamma(\mathcal{H})$, a respective strong proper coloring and a feasible partition.
4. For hypergraph $\mathcal{H}$ in Figure 10.2, construct examples of equitable, good, uniform, and $I$-regular colorings, if they exist.
5. For hypergraph $\mathcal{H}$ in Figure 10.2, compute the cyclomatic number $\Lambda(\mathcal{H})$ and verify the inequality of Theorem 10.1.1.
6. Is hypergraph $\mathcal{H}$ in Figure 10.2 edge-critical?

Computer Projects 10.1. Write a program for the following algorithmic problems.

1. Given a hypergraph $\mathcal{H}$, a random coloring of the vertices and a number $\lambda \geq 1$. Determine if the coloring is a proper $\lambda$-coloring.
2. Given a hypergraph $\mathcal{H}$, find an upper bound on the chromatic number by generating colorings at random.

### 10.2. Greedy Algorithm for the Lower Chromatic Number

Let $\mathcal{H}=(X, \mathcal{D})$ be a hypergraph, and, as usually, let $\mathcal{D}(x)$ be the set of edges containing $x \in X$. A star in $\mathcal{H}$ which has a unique center is called a monostar. A vertex $x$ can be a center for many stars or even monostars; we are interested in the largest number of edges in a monostar with $x$ as the center.

Definition 10.2.1 The mono-degree $m(x, \mathcal{H})$ of a vertex $x \in X$ in a hypergraph $\mathcal{H}=(X, \mathcal{D})$ is the maximum cardinality of a subfamily $\mathcal{D}_{1}(x) \subseteq \mathcal{D}(x)$ such that:

$$
D_{i}, D_{j} \in \mathcal{D}_{1}(x) \Rightarrow D_{i} \cap D_{j}=\{x\} .
$$

In other words, the mono-degree of a vertex $x$ is the maximum number of edges of a monostar with vertex $x$ as the center. If $\mathcal{H}$ is a graph without loops, then mono-degree coincides with the usual degree of a vertex.

Consider the value

$$
M(\mathcal{H})=\max _{Y \subseteq X} \min _{x \in Y} m\left(x, \mathcal{H}_{Y}\right) .
$$

It can be computed by considering all induced subhypergraphs of $\mathcal{H}$, choosing a vertex of minimum mono-degree in each of them and then taking the maximum mono-degree over all induced subhypergraphs.

If applied to graphs, $M(\mathcal{H})$ equals the Szekeres-Wilf number of a graph, see Section 3.3. Recall that $\boldsymbol{\omega}$ denotes the maximum cardinality of a clique, and the Szekeres-Wilf number is at least $\omega-1$, see Proposition 3.3.1. We have seen in Theorem 3.3.1 that when considered for graphs the value $M(G)$ is closely related to chordal graphs.

Next we consider a greedy hypergraph coloring algorithm which is related to the value $M(\mathcal{H})$. The idea is to find a good ordering of the vertices by first decomposing $\mathcal{H}$ using the mono-degrees of the vertices. Then greedily color $\mathcal{H}$ successively, by adding vertices in reverse ordering. At each step we use the first suitable color in the set of colors. In the worst case we can't use any color from the set of colors. Then we assign a new color to the next vertex and add the color to the set of colors. Since we are looking for the minimum number of colors, at each worst case we lose one color. In detail, the algorithm looks as follows. We use the notation $c(x)$ for the color of a vertex $x \in X$ and the vector $c=\left(c\left(x_{1}\right), c\left(x_{2}\right), \ldots, c\left(x_{n}\right)\right)$ for a coloring of $\mathcal{H} ; c(x)=0$ means that $x$ is not colored.

Algorithm 10.2.1 (greedy hypergraph coloring)
INPUT: An arbitrary hypergraph $\mathcal{H}=(X, \mathcal{D}), X=\{1,2, \ldots, n\}$.
OUTPUT: A proper coloring $c=(c(1), c(2), \ldots, c(n))$ of $\mathcal{H}$.

1. Set $C=(0,0, \ldots, 0), i=n, \mathcal{H}_{n}=\mathcal{H}$. Find a vertex of minimum mono-degree in $\mathcal{H}_{n}$ and label it $x_{n}$.
2. Put $i:=i-1$; if $i=0$, then go to step 5.
3. Strongly delete the vertex $x_{i+1}$ and form an induced subhypergraph $\mathcal{H}_{i}=\mathcal{H}_{i+1}-x_{i+1}$.
4. Find a vertex of minimum mono-degree in $\mathcal{H}_{i}$ and label it $x_{i}$; go to step 2.
5. Color $x_{1}$ with the first color: $c\left(x_{1}\right)=1, i=1$.
6. Put $i:=i+1$; if $i=n+1$, then go to step 8.
7. Color $x_{i}$ in $\mathcal{H}_{i}$ with the smallest suitable color from $\{1,2, \ldots, n\}$; go to step 6.
8. Output $c=(c(1), c(2), \ldots, c(n))$. End.

Remark. It is important to observe that the algorithm is greedy in the sense that it never requires re-coloring (backtracking) of vertices that have been colored. The worst case results in a new color and at any step a proper coloring is obtained. Though simple, the algorithm has one complex point, namely that of determining a vertex of minimum
mono-degree (step 4). Let us suppose that $x$ is an arbitrary vertex in an arbitrary hypergraph. Determining its mono-degree is equivalent to finding the maximum monostar with $x$ as the central vertex. The latter is equivalent to finding the maximum matching in the hypergraph obtained by weak deletion of $x$ from the subhypergraph induced by the neighborhood of $x$. This leads to the problem of finding a maximum stable set in the 2-section of the dual hypergraph, which is generally difficult to do. However, if the degrees of the vertices are bounded by a constant, for example if $\Delta(\mathcal{H})$ is bounded, then some polynomial bounds may be derived for the complexity. In practice some modifications might be made to avoid exhaustive searching at the cost of accuracy depending on the structural properties of hypergraphs.

Theorem 10.2.1 The maximum value of the minimum mono-degree generated by steps 1-4 of the greedy hypergraph coloring algorithm equals $M(\mathcal{H})$.

Proof. Let $t$ be the maximum value of the minimum mono-degree over all the vertices in the ordering generated by steps 1-4. It is clear that $t \leq M(\mathcal{H})$. We must show that $t \geq M(\mathcal{H})$ also holds. There is an induced subhypergraph $\mathcal{H}_{Y}$ and a vertex $y \in Y$ such that

$$
m\left(y, \mathcal{H}_{Y}\right)=\min _{z} m\left(z, \mathcal{H}_{Y}\right)=M(\mathcal{H}) .
$$

Let $k$ be the step when the first vertex from the set $Y$ was deleted. Hence $\mathcal{H}_{Y}$ is an induced subhypergraph of $\mathcal{H}_{k}$. Therefore

$$
M(\mathcal{H})=m\left(y, \mathcal{H}_{Y}\right) \leq m\left(x_{k}, \mathcal{H}_{k}\right) \leq t .
$$

Consequently, $t=M(\mathcal{H})$. $\square$

Corollary 10.2.1 For any hypergraph $\mathcal{H}=(X, \mathcal{D})$

$$
\chi(\mathcal{H}) \leq M(\mathcal{H})+1 .
$$

Proof. From the algorithm and Theorem 10.2.1 it follows that the maximum value of the mono-degree obtained by the algorithm coincides with $M(\mathcal{H})$. The maximum number of colors which we are not allowed to use to color the vertex $x_{i}$ at step 7 is not greater than $M(\mathcal{H})$. Indeed, if we cannot use the colors $1,2, \ldots, t$ it means that we have the edges, say $D_{1}, D_{2}, \ldots, D_{t}$ in $\mathcal{H}_{i}$, which are mono-colored (except the vertex $x_{i}$ ) with the respective colors $1,2, \ldots, t$. These colors are different, therefore the edges $D_{1}, D_{2}, \ldots, D_{t}$ have a unique common vertex $x_{i}$ and represent a monostar. Since we use the next color for $x_{i}$, the theorem follows. $\square$

Notice that Theorem 10.2.1 is a direct generalization of the procedure for computing $M(G)$ described at the beginning of Section 3.3., and Corollary 10.2.1 is a direct generalization of Theorem 5.6.1

Figure 10.3 shows the application of Algorithm 10.2.1 to the hypergraph in Figure 10.1. At the very beginning, $\mathcal{H}_{5}=\mathcal{H}$ and $X=\{1,2,3,4,5\}$. In $\mathcal{H}$, the mono-degrees of vertices are:

$$
m(1, \mathcal{H})=2, m(2, \mathcal{H})=2, m(3, \mathcal{H})=2, m(4, \mathcal{H})=1, m(5, \mathcal{H})=1 .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-216.jpg?height=1323&width=1230&top_left_y=194&top_left_x=267)
Figure 10.3.

Since $\min \{2,2,2,1,1\}=1$, either vertex 4 or vertex 5 can be deleted to obtain hypergraph $\mathcal{H}_{4}$. Choose vertex 5 : $\mathcal{H}_{4}=\mathcal{H}_{5}-5$. In $\mathcal{H}_{4}$, vertex 4 has the minimum mono-degree 1 . Continuing decomposition of the original hypergraph $\mathcal{H}$ we obtain the sequence of hypergraphs $\mathcal{H}_{5}, \mathcal{H}_{4}, \mathcal{H}_{3}, \mathcal{H}_{2}$ and $\mathcal{H}_{1}=(\{2\}, \emptyset)$ which corresponds to the ordering of vertices

$$
5,4,1,3,2 .
$$

At this point the algorithm starts coloring the hypergraph $\mathcal{H}_{1}$ by assigning color 1 to vertex 2 at Step 5. Next it reconstructs the original hypergraph by adding vertices in inverse ordering

$$
2,3,1,4,5,
$$

and coloring each of them by the smallest suitable color. At this segment of work the numbers in the Figure mean the colors. Algorithm ends with the output of the following proper coloring of the original hypergraph $\mathcal{H}$ :

$$
c=(2,1,2,1,1) .
$$

Maximum among all minimal mono-degrees found by Algorithm is 2. Hence by Theorem 10.2.1, $M(\mathcal{H})=2$. At last, one can easily see that $\chi(\mathcal{H})=2 \leq M(\mathcal{H})+1=3$.

Exercises 10.2.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-217.jpg?height=523&width=974&top_left_y=492&top_left_x=365)
Figure 10.4.

1. In hypergraph $\mathcal{H}$ in Figure 10.4, find the mono-degree of each vertex.
2. Apply Algorithm 10.2.1 to hypergraph $\mathcal{H}$ in Figure 10.4 to find a proper coloring, $M(\mathcal{H})$ and an upper bound on the chromatic number $\chi(\mathcal{H})$.
3. For hypergraph $\mathcal{H}$ in Figure 10.4, find the exact value of $\chi(\mathcal{H})$.

Computer Projects 10.2. Write a program for the following algorithmic problems.

1. Given a hypergraph $\mathcal{H}$ and a vertex, find the mono-degree of the vertex and a respective mono-star.
2. Given a hypergraph $\mathcal{H}$, find $M(\mathcal{H})$.
3. Given a hypergraph $\mathcal{H}$, apply Algorithm 10.2.1 to find an upper bound on the chromatic number $\chi(\mathcal{H})$ and a respective proper coloring.

### 10.3. Basic Definitions of Mixed Hypergraph Coloring

Until now, we discussed the classic graph and hypergraph coloring. The basic problem was to find the chromatic number, i.e. the minimum number of colors, of a graph or a hypergraph and the corresponding optimal coloring. Since for proper coloring the maximum number of colors is $n$ if we consider strict colorings, or is $\lambda$ if we consider all proper colorings, the problem of finding the largest number of colors over all proper colorings never occurred. In this section we introduce the basic concepts of mixed hypergraph coloring where, in contrast, problems on both the minimum and maximum number of colors occur [6].

Let $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}, n \geq 1$, be a finite set, and let $\mathcal{C}=\left\{C_{1}, C_{2}, \ldots, C_{l}\right\}$ and $\mathcal{D}=$ $\left\{D_{1}, D_{2}, \ldots, D_{m}\right\}$ be two families of subsets of $X$ such that the size of every member of $\mathcal{C} \cup \mathcal{D}$ is at least 2. Each of $\mathcal{C}, \mathcal{D}$ may be empty, and any subset of vertices may be contained in both $\mathcal{C}$ and $\mathcal{D}$. If $\mathcal{C} \neq \boldsymbol{\emptyset}$, then denote $I=\{1,2, \ldots, l\}$, and if $\mathcal{D} \neq \emptyset$, then denote $J=\{1,2, \ldots, m\}$.

Definition 10.3.1 A mixed hypergraph is a triple $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ where $X$ is called the vertex set, also denoted by $V(\mathcal{H}), \mathcal{C}$ is the family of subsets called $\mathcal{C}$-edges, also denoted by $\mathcal{C}(\mathcal{H})$, and $\mathcal{D}$ is the family of subsets called $\mathcal{D}$-edges, also denoted by $\mathcal{D}(\mathcal{H})$.

As in graphs and hypergraphs, let us call $\lambda \geq 1$ natural numbers $\{1,2, \ldots, \lambda\}$ the set of colors. Any labeling of elements of $X$ by colors is called a coloring. More formally, we will call any coloring a mapping $c$ from the vertex set $X$ into the set of colors and denote it by

$$
c: X \rightarrow\{1,2, \ldots, \lambda\} .
$$

In such a mapping, the number $c(x), x \in X$, is called the color of vertex $x$.
Definition 10.3.2 A proper $\lambda$-coloring of a mixed hypergraph $\mathcal{H}=(X, C, \mathcal{D})$ is a mapping $c: X \rightarrow\{1,2, \ldots, \lambda\}$ such that the following two conditions hold:

1) every $C \in \mathcal{C}$ has at least two vertices of a Common color;
2) every $D \in \mathcal{D}$ has at least two vertices of Different colors.

Again, as in graphs, we also use the terms "proper coloring", or just "coloring", if the value of $\lambda$ is not important and this does not lead to misunderstanding. Note that Definition 10.3.2 of a proper coloring generalizes all those contained in Chapter 5 and Sections 10.1. and 10.2. that correspond to the case $\mathcal{C}=\emptyset$. In contrast to graphs and hypergraphs, however, not every mixed hypergraph is colorable:

Definition 10.3.3 A mixed hypergraph $\mathcal{H}$ is called colorable if it admits at least one proper coloring; otherwise $\mathcal{H}$ is called uncolorable.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-218.jpg?height=194&width=523&top_left_y=1686&top_left_x=621)
Figure 10.5. The smallest uncolorable mixed hypergraph.

The example of the smallest uncolorable mixed hypergraph is shown in Figure 10.5: $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ where $X=\{1,2\}, \mathcal{C}=\{\{1,2\}\}$, and $\mathcal{D}=\{\{1,2\}\}$. Indeed, according to Definition 10.3.2, $\mathcal{C}$-edge $C=\{1,2\}$ requires the vertices 1 and 2 to be of a common color; however, $\mathcal{D}$-edge $D=\{1,2\}$ requires the vertices 1 and 2 to be of different colors. This contradiction cannot be reconciled with any set of available colors $\{1,2, \ldots, \lambda\}$.

In what follows we assume that mixed hypergraphs are colorable unless stated otherwise.

Definition 10.3.4 The minimum $\lambda$ for which there exists a proper $\lambda$-coloring of a mixed hypergraph $\mathcal{H}$ is called the lower chromatic number of $\mathcal{H}$, denoted by $\chi(\mathcal{H})$.

The chromatic number of a graph or hypergraph as defined in Chapter 5 and Sections 10.1. and 10.2. simply becomes the lower chromatic number of a mixed hypergraph with $\mathcal{C}=\emptyset$.

Two proper colorings $c_{1}, c_{2}$ of a mixed hypergraph $\mathcal{H}$ are said to be different, if there exists at least one vertex $x \in X$ that changes the color, i.e. $c_{1}(x) \neq c_{2}(x)$. Hence any permutation of colors results in a new proper coloring since it represents a different mapping. Let $P(\mathcal{H}, \lambda)$ be the number of different proper $\lambda$-colorings of a mixed hypergraph $\mathcal{H}$. As in graphs, we need to identify proper colorings which use all the colors; in this case we use $i$ for the number of colors.

Definition 10.3.5 A proper $i$-coloring of a mixed hypergraph $\mathcal{H}$ is called a strict $i$ coloring, if each of the $i$ colors is used.

Strict $i$-colorings exist only for $1 \leq i \leq n$. Note that a proper $\chi(\mathcal{H})$-coloring is necessarily a strict coloring since $\chi(\mathcal{H})$ is the minimum number of colors over all proper colorings. The maximum number of colors may now be specified as follows:

Definition 10.3.6 The maximum i for which there exists a strict i-coloring of a mixed hypergraph $\mathcal{H}$ is called the upper chromatic number of $\mathcal{H}$, denoted by $\bar{\chi}(\mathcal{H})$.

In a coloring of a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, a subset of vertices $Y \subseteq X$ is called monochromatic if all the colors $c(y), y \in Y$, have the same value, and it is called polychromatic if all the colors $c(y), y \in Y$, are pairwise different. In a proper coloring of a mixed hypergraph, $\mathcal{D}$-edges are non-monochromatic subsets, while the $\mathcal{C}$-edges are non-polychromatic subsets of vertices.

Any strict $i$-coloring of $\mathcal{H}$ induces a partition of the vertex set $X$ into $i$ nonempty monochromatic subsets called color classes. Therefore we can interpret strict colorings using the language of partitions:

Definition 10.3.7 In a mixed hypergraph $\mathcal{H}$, a partition of $X$ into $i$ nonempty sets $X_{1}, X_{2}$, $\ldots, X_{i}$ is called a feasible partition of $\mathcal{H}$ if every $\mathcal{C}$-edge has at least two vertices in a Common set and every $\mathcal{D}$-edge has at least two vertices in $\mathcal{D}$ ifferent sets of the partition.

Sometimes we will write the feasible partition or strict $i$-coloring $c$ as $c=X_{1} \cup X_{2} \cup \ldots \cup X_{i}$. Let $r_{i}(\mathcal{H})=r_{i}, 1 \leq i \leq n$, denote the number of feasible partitions of a mixed hypergraph $\mathcal{H}$ into $i$ sets.

Definition 10.3.8 The integer vector

$$
R(\mathcal{H})=\left(r_{1}, r_{2}, \ldots, r_{n}\right)
$$

is called the chromatic spectrum of the mixed hypergraph $\mathcal{H}$.

In fact, since we have lower and upper chromatic numbers for every colorable mixed hypergraph $\mathcal{H}$, there are no feasible partitions into less than $\mathcal{X}$ color classes, and there no feasible partitions into more than $\bar{\chi}$ color classes. Therefore, chromatic spectrum generally has the following form:

$$
R(\mathcal{H})=\left(0, \ldots, 0, r_{\chi}, \ldots, r_{\bar{\chi}}, 0, \ldots, 0\right) .
$$

Further, each feasible partition into $i$ color classes determines $i$ ! strict $i$-colorings obtained from each other by a permutation of colors. Hence the number of strict $i$-colorings equals $r_{i} i!$. In general, if we have $\lambda \geq i$ colors, then to count proper $\lambda$-colorings we have $\binom{\lambda}{i}$ ways to choose the subset of $i$ colors. Consequently the number of proper $\lambda$-colorings generated by all feasible partitions into $i$ subsets is $\binom{\lambda}{i} r_{i} i!=r_{i} \lambda(\lambda-1) \ldots(\lambda-i+1)=$ $r_{i} \lambda^{(i)}$. To obtain the number of all proper $\lambda$-coloring it is sufficient then to add all these numbers for every $\chi(\mathcal{H}) \leq i \leq \bar{\chi}(\mathcal{H})$. Thus we arrive to the following conclusion:

Proposition 10.3.1 The number of proper $\lambda$-colorings $P(\mathcal{H}, \lambda)$ of a colorable mixed hypergraph $\mathcal{H}$ is a polynomial in $\lambda$ and has the following formula:

$$
P(\mathcal{H}, \lambda)=\sum_{i=\chi(\mathcal{H})}^{\bar{\chi}(\mathcal{H})} r_{i}(\mathcal{H}) \lambda^{(i)} .
$$

Therefore we call $P(\mathcal{H}, \lambda)$ the chromatic polynomial of the mixed hypergraph $\mathcal{H}$. Chromatic polynomials of graphs, see Section 5.3., represent an important special case, and equality (10.2) directly generalizes the fundamental equality (5.3). Therefore we will call it the fundamental equality in mixed hypergraph coloring.

Corollary 10.3.1 For any colorable mixed hypergraph $\mathcal{H}$, the degree of the chromatic polynomial equals $\bar{\chi}$, and the leading coefficient equals $r_{\bar{\chi}}$.

Proof. Indeed, the major term in equality (10.2) equals

$$
r_{\bar{\chi}} \lambda(\lambda-1)(\lambda-2) \cdots(\lambda-\bar{\chi}+1)
$$

what proves the statement. $\square$

Definition 10.3.9 For an uncolorable mixed hypergraph $\mathcal{H}$ we set

$$
\chi(\mathcal{H})=\bar{\chi}(\mathcal{H})=0, \quad R(\mathcal{H})=(0,0, \ldots, 0), \quad P(\mathcal{H}, \lambda)=0 .
$$

For a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, the partial mixed subhypergraph $\mathcal{H}=(X, \mathcal{C}, \emptyset)$, also denoted by $\mathcal{H}_{\mathcal{C}}=(X, \mathcal{C})$, is called a $\mathcal{C}$-hypergraph, and the partial mixed subhypergraph $\mathcal{H}=(X, \emptyset, \mathcal{D})$, also denoted by $\mathcal{H}_{\mathcal{D}}=(X, \mathcal{D})$, is called a $\mathcal{D}$-hypergraph.

Remark. We will use the prefixes $\mathcal{C}$ - and $\mathcal{D}$ - when discussing different coloring and structural properties of $\mathcal{H}_{\mathcal{C}}$ and $\mathcal{H}_{\mathcal{D}}$ respectively. For example, a $\mathcal{D}$-graph is a $\mathcal{D}$ hypergraph with all the $\mathcal{D}$-edges of size 2, i.e. it is a classic graph. It is also convenient to use the term "edge" for any element from $\mathcal{C} \cup \mathcal{D}$. Thus the prefixes express the type of coloring of a subset of vertices.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-221.jpg?height=507&width=689&top_left_y=217&top_left_x=528)
Figure 10.6. Mixed hypergraph $\mathcal{H}$.

In this framework, the colorings of classic hypergraphs are the colorings of $\mathcal{D}$-hypergraphs; the chromatic number of a hypergraph becomes the lower chromatic number of $\mathcal{H}_{\mathcal{D}}$. Their opposites are the colorings of $\mathcal{C}$-hypergraphs; the main problem here will be to find $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)$. Notice that, for any mixed hypergraph $\mathcal{H}$ (colorable or not), the partial hypergraphs $\mathcal{H}_{C}$ and $\mathcal{H}_{\mathcal{D}}$ are both colorable, trivially with one color and $n(\mathcal{H})$ colors respectively. Obviously, $\chi\left(\mathcal{H}_{\mathcal{C}}\right)=1, r_{1}\left(\mathcal{H}_{\mathcal{C}}\right)=1$, and $\bar{\chi}\left(\mathcal{H}_{\mathcal{D}}\right)=n(\mathcal{H}), r_{n}\left(\mathcal{H}_{\mathcal{D}}\right)=1$. Generally, for a colorable mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, the following evident inequalities hold:

$$
1 \leq \chi\left(\mathcal{H}_{\mathcal{D}}\right) \leq \chi(\mathcal{H}) \leq \bar{\chi}(\mathcal{H}) \leq \bar{\chi}\left(\mathcal{H}_{C}\right) \leq n .
$$

Figure 10.6 shows an example of a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ with $X=\{1,2,3,4,5\}, \quad \mathcal{C}=\left\{C_{1}, C_{2}\right\}=\{\{1,4,5\},\{1,3,4\}\}$, and $\mathcal{D}=\left\{D_{1}, D_{2}\right\}=$ \{\{1,3,4\}\{1,2,3\}\}. The $\mathcal{C}$-edges are drawn by dashed (closed) curves; we will follow this rule unless stated otherwise. One can easily find that $\chi(\mathcal{H})=2$, while $\bar{\chi}(\mathcal{H})=4$. Notice that $C_{2}=D_{1}=\{1,3,4\}$ what means that in any proper coloring the subset of vertices \{1,3,4\} can be neither monochromatic nor polychromatic; since it has three elements, precisely two colors must be used. A coloring which uses the minimum number of colors is $c_{1}=(1,2,2,1,1)$; a strict coloring which uses the maximum number of colors is $c_{2}=(1,2,3,1,4)$. There are also other proper colorings. The $\mathcal{C}$-hypergraph $\mathcal{H}_{C}$ is obtained from $\mathcal{H}$ be weak deletion of all $\mathcal{D}$-edges; the $\mathcal{D}$-hypergraph $\mathcal{H}_{\mathcal{D}}$ is obtained from $\mathcal{H}$ be weak deletion of all $\mathcal{C}$-edges. Thus the inequalities (10.3) turn into the following:

$$
1 \leq \chi\left(\mathcal{H}_{\mathcal{D}}\right)=2 \leq \chi(\mathcal{H})=2 \leq \bar{\chi}(\mathcal{H})=4 \leq \bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)=4 \leq n=5 .
$$

It is easy to construct uncolorable mixed hypergraphs. Both $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$, see Figure 10.7, are uncolorable mixed hypergraphs. $\mathcal{H}_{1}$ contains $\mathcal{D}$-graph $K_{3}$ which requires three different colors; however, the unique $\mathcal{C}$-edge containing the same three vertices requires two vertices to be of the same color what cannot be satisfied. Generally, any $\mathcal{C}$-edge with all the vertices inducing a complete $\mathcal{D}$-graph will be called an evidently uncolorable $\mathcal{C}$-edge.

Mixed hypergraph $\mathcal{H}_{2}$ contains a tree consisting of $\mathcal{C}$-edges. This implies that all four vertices must have the same color. However, the unique $\mathcal{D}$-edge being the set of all vertices requires at least two different colors. Again, we have a contradiction that leads to the

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-222.jpg?height=482&width=1023&top_left_y=199&top_left_x=360)
Figure 10.7. Evidently uncolorable $\mathcal{C}$ - and $\mathcal{D}$-edges.

uncolorability. Generally, any $\mathcal{D}$-edge with each pair of the vertices connected by a $\mathcal{C}$-path consisting of $\mathcal{C}$-edges of size 2, will be called an evidently uncolorable $\mathcal{D}$-edge. Notice that such $\mathcal{C}$-paths may not be inside the $\mathcal{D}$-edge.

Evidently, any mixed hypergraph containing an evidently uncolorable edge of any type is uncolorable. Recall that in mixed hypergraph coloring, by default, we do not consider edges of size $\leq 1$ of any kind.

One more direct observation is that any mixed hypergraph with $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)<\chi\left(\mathcal{H}_{\mathcal{D}}\right)$ is uncolorable. We will discuss uncolorable mixed hypergraphs in Section 10.6.

In a mixed hypergraph, if a subset of vertices is a $\mathcal{C}$-edge and a $\mathcal{D}$-edge at the same time, then it is a bi-edge. For example, in Figure 10.6, the subset of vertices $\{1,3,4\}$ is a $\mathcal{C}$-edge and a $\mathcal{D}$-edge at the same time, i.e. it is a bi-edge. A mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is a bihypergraph if $\mathcal{C}=\mathcal{D}$.

Let us denote the underlying families of $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ by $\mathcal{E}=\mathcal{C} \cup \mathcal{D}$. We say that $\mathcal{H}^{\prime}=(X, \mathcal{E})$ is the underlying hypergraph of $\mathcal{H}$. Using underlying hypergraphs, many general structural concepts and agreements (such as drawing rules, basic operations, etc.) introduced for hypergraphs will be applied to mixed hypergraphs. For example, any path in the underlying hypergraph $\mathcal{H}^{\prime}$ is a mixed path in $\mathcal{H}$, and it is a $\mathcal{C}$-path ( $\mathcal{D}$-path) in $\mathcal{H}$ if it is a path in $\mathcal{H}_{C}\left(\mathcal{H}_{\mathcal{D}}\right)$, respectively. $\mathcal{H}$ is an $r$-uniform mixed hypergraph if $\mathcal{H}^{\prime}$ is an $r$-uniform hypergraph. $\mathcal{H}$ is connected if $\mathcal{H}^{\prime}$ is connected; otherwise $\mathcal{H}$ is disconnected. For any subset $Y \subseteq X$, a mixed hypergraph $\mathcal{H}_{Y}=\left(Y, \mathcal{C}^{\prime}, \mathcal{D}^{\prime}\right)$ is the induced subhypergraph of $\mathcal{H}$ if the underlying hypergraph of $\mathcal{H}_{Y}$ is the induced subhypergraph in $\mathcal{H}^{\prime}$; this means that $\mathcal{C}^{\prime}$ and $\mathcal{D}^{\prime}$ consist of all those members of $\mathcal{C}$ and of $\mathcal{D}$, respectively, which are entirely contained in $Y$. Clearly, any induced subhypergraph of a mixed hypergraph can be obtained by strong deletions of the respective vertices.

In a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, a set of vertices $S \subseteq X$ is $\mathcal{C}$-stable or $\mathcal{C}$ -independent ( $\mathcal{D}$-stable, $\mathcal{D}$-independent) if it contains no $\mathcal{C}$-edge (no $\mathcal{D}$-edge) as a subset.

## Exercises 10.3.

1. For mixed hypergraph $\mathcal{H}$ in Figure 10.8, find a few proper colorings and respective feasible partitions; estimate the chromatic spectrum $R(\mathcal{H})$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-223.jpg?height=536&width=917&top_left_y=236&top_left_x=365)
Figure 10.8.

2. For mixed hypergraph $\mathcal{H}$ in Figure 10.8, find the lower and upper chromatic numbers, respective strict colorings and respective feasible partitions.
3. What is the degree of the chromatic polynomial $P(\mathcal{H}, \lambda)$ ?
4. For mixed hypergraph $\mathcal{H}$ in Figure 10.8, draw $\mathcal{H}_{C}$ and $\mathcal{H}_{\mathcal{D}}$. Find their lower and upper chromatic numbers.
5. For mixed hypergraph $\mathcal{H}$ in Figure 10.8, verify inequalities (10.3).
6. For mixed hypergraph $\mathcal{H}$ in Figure 10.8, draw a few induced and partial subhypergraphs.

Computer Projects 10.3. Write a program for the following algorithmic problems.

1. Given a mixed hypergraph $\mathcal{H}$, randomly generate a series of proper colorings and find an estimate on the chromatic spectrum $R(\mathcal{H})$.

### 10.4. Greedy Algorithm for the Upper Chromatic Number

In this section we discuss a greedy algorithm for the upper chromatic number as the opposite to the greedy algorithm for the lower chromatic number described in Section 10.2.

Let $\mathcal{H}=(X, \mathcal{C}, \emptyset)$ be a $\mathcal{C}$-hypergraph, abbreviated simply by $\mathcal{H}=(X, \mathcal{C})$ and let $\mathcal{C}(x)$ denote the set of $\mathcal{C}$-edges containing vertex $x \in X$. Two vertices $x$ and $y$ are adjacent if and only if $\mathcal{C}(x) \bigcap \mathcal{C}(y) \neq \emptyset$. Call the set $\mathcal{C}(x) \cap \mathcal{C}(y)$ a bistar of the vertex $x \in X$ with respect to the vertex $y$. So, every vertex $y$ that is adjacent to $x$ defines a bistar. Some bistars of a given vertex may coincide. Furthermore, call the value

$$
b(x, \mathcal{H})=\max _{y}\{|\mathcal{C}(x) \cap \mathcal{C}(y)|: y \in X, y \neq x\}
$$

the bidegree of vertex $x$. In this way, the bidegree of a vertex is formed by a maximum bistar. We will see that the bidegree in $\mathcal{C}$-hypergraphs in some sense plays the role of the monodegree in $\mathcal{D}$-hypergraphs as defined in Definition 10.2.1.

Call the value

$$
o(x, \mathcal{H})=|\mathcal{C}(x)|-b(x, \mathcal{H}) \geq 0
$$

the originality of a vertex $x$ in the $\mathcal{C}$-hypergraph $\mathcal{H}$.
Thus $o(x, \mathcal{H})=0$ implies that there is another vertex $y \in X$ which is contained in all $\mathcal{C}$-edges containing $x$. The term "originality" is justified as follows. If the vertices of a hypergraph represent different objects in real life, and the $\mathcal{C}$-edges correspond to sets of objects that have a common property (each property is one $\mathcal{C}$-edge), then all the properties of the object $x$ are $\mathcal{C}(x)$. The object $x$ with $o(x, \mathcal{H})=0$ is "not original" because there exists at least one other object with the same properties. So, the originality of a vertex is a measure of "similarity with its neighbors". The higher the originality, the less similar a vertex is to its neighbors. The upper limit here is $|\mathcal{C}(x)|-1$ if $x$ is the center of a monostar.

Definition 10.4.1 The value

$$
O(\mathcal{H})=\max _{Y \subseteq X} \min _{x \in Y} o\left(x, \mathcal{H}_{Y}\right)
$$

is called the resistance of a hypergraph $\mathcal{H}$.
We will see that $O(\mathcal{H})$ plays the role which is similar to the role of $M(\mathcal{H})$.
Definition 10.4.2 In a coloring of a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, a set $M \subseteq X$ of vertices is called a monochromatic component of a vertex $x \in M$, and is denoted by $M C(x)$, if all the vertices of $M$ have the same color as $x$ and are reachable from $x$ by $\mathcal{C}$-paths.

Now, in order to find a lower bound for the upper chromatic number, we propose a quasigreedy algorithm for an arbitrary $\mathcal{H}=(X, \mathcal{C})$. As for the lower chromatic number, the idea is to find a good ordering of the vertices and greedily color $\mathcal{H}$ successively, maximally using the local information. But this time, at each step we use a new color for the next vertex and verify if the coloring obtained is proper. If the coloring is wrong (i.e. there are polychromatic $\mathcal{C}$-edges), then we re-color a monochromatic component starting at the neighborhood of the given vertex in order to guarantee the correctness of the new coloring and minimize the losses of used colors. The unavoidable backtracking in this approach justifies the more precise term "quasi-greedy".

Algorithm 10.4.1 (quasi-greedy $\mathcal{C}$-hypergraph coloring)
INPUT: An arbitrary $\mathcal{C}$-hypergraph $\mathcal{H}=(X, \mathcal{C}),|X|=n$.
OUTPUT: A strict coloring of $\mathcal{H}$ in a number of colors.

1. Set $i=n, \mathcal{H}_{n}=\mathcal{H}$; find a vertex of minimum originality and label it $x_{n}$.
2. Put $i:=i-1$; if $i=0$, then go to step 5.
3. Strongly delete the vertex $x_{i+1}$ and form an induced $\mathcal{C}$-hypergraph $\mathcal{H}_{i}=\mathcal{H}_{i+1}-x_{i+1}$.
4. Find a vertex of minimum originality in $\mathcal{H}_{i}$ and label it $x_{i}$; go to step 2.
5. Set the list of used colors $U=\{1\}$, color the vertex $x_{1}$ with the color 1; set $i=$ 1 ,new = 2.
6. Put $i:=i+1$; if $i=n$, then go to step 10; color the vertex $x_{i}$ of $\mathcal{H}_{i}$ with color new; put $U:=U \cup\{$ new $\}$, new $:=$ new +1 .
7. Verify the correctness of the coloring of $\mathcal{H}_{i}$; if there are no polychromatic $\mathcal{C}$-edges, then go to step 6.
8. In $\mathcal{H}_{i}$, choose a neighbor $y$ of the vertex $x_{i}$, which generates a largest bistar of $x_{i}$ with all the $\mathcal{C}$-edges polychromatic. If $x_{i}$ was not yet re-colored in $\mathcal{H}_{i}$, then re-color $x_{i}$ with the color of $y$, put $U:=U-\{$ new $\}$, new $:=$ new -1 , and go to step 7 .
9. Re-color all the vertices from the monochromatic component $M C(y)$ with the color of $x_{i}$ and go to step 7.
10. Renumber the colors of $U$ in increasing order; end.

Remark. The monochromatic component re-coloring used in the algorithm is the opposite to the bi-chromatic chain re-coloring by Kempe, see Section 5.6.

Complexity. Let us suppose that the hypergraph $\mathcal{H}=(X, \mathcal{C})$, with $|X|=n,|\mathcal{C}|=k$, is represented by its incidence matrix $I(\mathcal{H})$ of the size $n \times k$. Since finding the originality of a vertex requires $O(n k)$ steps, finding the minimum originality requires $O\left(n^{2} k\right)$ steps. Hence, steps 1-4 may be implemented, in the worst case, in $O\left(n^{3} k\right)$ steps.

To check if the coloring is proper, it is necessary to look through every column, so the complexity of step 7 is $O(n k)$. Simultaneously, one can label the wrongly colored $\mathcal{C}$ -edges. Finding the neighborhood of $x_{i}$ and simultaneously identifying the vertex $y$ takes $O(n k)$ steps. Finding and re-coloring the monochromatic component $M C(y)$ can also be implemented in $O(n k)$ steps. Since, in the worst case, all the vertices from the neighborhood may require re-coloring, the complexity of steps 7-9 is $O\left(n^{2} k\right)$. Steps 7-9 are repeated $n$ times; consequently, the complexity of the second part and of the whole algorithm does not exceed $O\left(n^{3} k\right)$. One can improve this bound by using special data structures and techniques.

Example 10.4.1 Consider the $\mathcal{C}$-hypergraph $\mathcal{H}=(X, \mathcal{C})$ (see Figure 10.9) such that $X=$ $\{1,2,3,4,5\}, C=\left\{C_{1}, C_{2}, C_{3}, C_{4}, C_{5}\right\}, C_{1}=\{1,2,3\}, C_{2}=\{2,3,4\}, C_{3}=\{3,4,5\}$, $C_{4}=\{4,5,1\}$, and $C_{5}=\{5,1,2\}$. Set $\mathcal{H}_{5}=\mathcal{H}$. All the vertices have the same originality 1 , therefore, let us start with the first vertex: $x_{5}=1$.

Form the induced $\mathcal{C}$-hypergraph $\mathcal{H}_{4}=\left(X_{4}, \mathcal{C}_{4}\right)$ with $X_{4}=\{2,3,4,5\}, \mathcal{C}_{4}=\left\{C_{2}, C_{3}\right\}$. The first vertex with minimum originality is $x_{4}=2$.

Form the induced $\mathcal{C}$-hypergraph $\mathcal{H}_{3}=\left(X_{3}, \mathcal{C}_{3}\right)$ with $X_{3}=\{3,4,5\}, \mathcal{C}_{3}=\left\{C_{3}\right\}$. The first vertex with minimum originality is $x_{3}=3$.

Form the induced $\mathcal{C}$-hypergraph $\mathcal{H}_{2}=\left(X_{2}, \mathcal{C}_{2}\right)$ with $X_{2}=\{4,5\}, \mathcal{C}_{2}=\{\emptyset\}$. The first vertex with minimum originality is $x_{2}=4$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-226.jpg?height=779&width=898&top_left_y=241&top_left_x=412)
Figure 10.9. $\mathcal{C}$-hypergraph $\mathcal{H}=(X, \mathcal{C})$ of Example 10.4.1.

Form the induced $\mathcal{C}$-hypergraph $\mathcal{H}_{1}=\left(X_{1}, \mathcal{C}_{1}\right)$ with $X_{1}=\{5\}, \mathcal{C}_{1}=\{\emptyset\}$. The last vertex is $x_{1}=5$.

These are the results of steps 1-4. As usual, let $c(i)$ be the color of vertex $i, c(i)=0$ means the vertex is not colored, $i=1, \ldots, 5$.

Set $c=(c(1), c(2), c(3), c(4), c(5))=(0,0,0,0,0)$. Start coloring. Step 5: $c=$ (0, 0, 0, 0, 1). Step 6: $c=(0,0,0,2,1)$. Step 7: there are no polychromatic $\mathcal{C}$-edges in $\mathcal{C}$-hypergraph $\mathcal{H}_{2}$.

Step 6: $c=(0,0,3,2,1)$. Step 7: $\mathcal{C}$-edge $C_{3}$ is polychromatic.
Step 8: re-coloring: $c=(0,0,2,2,1)$.
Step 7: there are no polychromatic $\mathcal{C}$-edges in the $\mathcal{C}$-hypergraph $\mathcal{H}_{3}$.
Step 6: $c=(0,3,2,2,1)$.
Step 7: there are no polychromatic $\mathcal{C}$-edges in the $\mathcal{C}$-hypergraph $\mathcal{H}_{4}$.
Step 6: $c=(4,3,2,2,1)$.
Step 7: the $\mathcal{C}$-edges $C_{1}, C_{4}, C_{5}$ are each polychromatic in the $\mathcal{C}$-hypergraph $\mathcal{H}_{5}$.
Step 8: vertices 2 and 5 in the $\mathcal{C}$-hypergraph $\mathcal{H}_{5}$ generate the largest bi-stars of vertex 1 with all the $\mathcal{C}$-edges polychromatic; choose vertex 5; vertex 1 was not yet re-colored; re-color it with the color $c(5)=1: c=(1,3,2,2,1)$.

Step 7: the $\mathcal{C}$-edge $C_{1}$ is still polychromatic.
Step 8: vertices 2 and 3 in the $\mathcal{C}$-hypergraph $\mathcal{H}_{5}$ are contained in one polychromatic $\mathcal{C}$-edge; choose vertex 3.

Step 9: re-color the monochromatic component $M C(3)=\{3,4\}: c=(1,3,1,1,1)$.
Step 7: $\mathcal{H}_{1}=\mathcal{H}$ is colored properly.

Step 10: renumber the colors in increasing order: $c=(1,2,1,1,1)$. End.
Remark. Note that in the process of coloring, when $\mathcal{H}_{5}=\mathcal{H}$ is reconstructed and the coloring $C=(4,3,2,2,1)$ is obtained, for vertex $x_{5}=1$ none from the available colors $1,2,3,4,5 \ldots$ is appropriate. At this point we reach a deadlock, i.e. the situation when none of the available colors can be used to color the next vertex in a $\mathcal{C}$-hypergraph. Since $\mathcal{H}$ is evidently colorable, the re-coloring becomes unavoidable.

Theorem 10.4.1 The maximum value of the minimum originality generated by steps 1-4 of the Algorithm 10.4.1 equals $O(\mathcal{H})$.

Proof. Let $t$ be the maximum value of minimum originality over all the vertices in the order generated by steps 1-4. It is clear that $t \leq O(\mathcal{H})$.

Suppose that $t \leq O(\mathcal{H})-1$. Hence in an induced subhypergraph $\mathcal{H}^{\prime} \subseteq \mathcal{H}$ there is a vertex $y$ such that

$$
o\left(y, \mathcal{H}^{\prime}\right)=\min _{z} o\left(z, \mathcal{H}^{\prime}\right)=O(\mathcal{H}) \geq t+1 .
$$

It is easy to see that the originality of any vertex is a monotone function with respect to the induced subhypergraph inclusion. This implies that the first vertex of $\mathcal{H}^{\prime}$ that was deleted by the algorithm had originality $\geq t+1$, a contradiction. Consequently, $t=O(\mathcal{H})$. $\square$

In some sense, Theorem 10.4.1 is similar to Theorem 10.2.1.
Theorem 10.4.2 The number of colors that may be lost at steps 6-10 of Algorithm 10.4.1 does not exceed the value $O(\mathcal{H})+1$.

Proof. Let us suppose that we have the worst case at step 8; i.e., all the $\mathcal{C}$-edges containing $x_{i}$ in $\mathcal{H}_{i}$ have all their vertices polychromatic. Recall that in $\mathcal{H}_{i}$, for the vertex $x_{i}$, there is a neighbor $y$ forming the largest bistar of $x_{i}$. If we re-color vertex $x_{i}$ with $c(y)$, then we are losing one color (new) and at the same time are properly coloring $b\left(x_{i}, \mathcal{H}_{i}\right) \mathcal{C}$-edges. Hence, in the worst case, there remain at most $o\left(x_{i}, \mathcal{H}_{i}\right)=\left|\mathcal{C}\left(x_{i}\right)\right|-b\left(x_{i}, \mathcal{H}_{i}\right) \mathcal{C}$-edges that are still colored improperly. Every such $\mathcal{C}$-edge may form a separate bistar of $x_{i}$. Therefore, when re-coloring one monochromatic component for each of these $\mathcal{C}$-edges, we are again losing at most $o\left(x_{i}, \mathcal{H}_{i}\right)$ colors. Consequently, the total number of colors lost is not greater than $o\left(x_{i}, \mathcal{H}_{i}\right)+1$. Since for any $i, 1 \leq i \leq n$,

$$
o\left(x_{i}, \mathcal{H}_{i},\right) \leq O(\mathcal{H})=\max _{Y \subseteq X} \min _{x \in Y} o(x, \mathcal{H} / Y,)
$$

the theorem follows. $\square$

Corollary 10.4.1 If $O(\mathcal{H})=0$, then there exists an ordering of the vertex set $X$ such that Algorithm 10.4.1 may be implemented without re-colorings of monochromatic components.

Proof. Indeed, the vertices of originality 0 are pendant to some neighbors, and the algorithm uses the color of the neighbor. $\square$

Corollary 10.4.2 In Algorithm 10.4.1, if $|U|=p$, then $\bar{\chi}(\mathcal{H}) \geq p$.

We described Algorithm 10.4.1 which is a consecutive quasi-greedy coloring algorithm searching for $\bar{\chi}(\mathcal{H})$ and a corresponding coloring for an arbitrary $\mathcal{C}$-hypergraph $\mathcal{H}$. Let us compare it to the classical greedy coloring Algorithm 10.2.1 for the lower chromatic number of a $\mathcal{D}$-hypergraph. Both use the same information and are consecutive; i.e., we decompose the $\mathcal{D}$-hypergraph or $\mathcal{C}$-hypergraph first by deleting the vertices following some greedy rules. Then we reconstruct the initial $\mathcal{D}$-hypergraph or $\mathcal{C}$-hypergraph by adding vertices in reverse order and coloring them using the neighborhoods. Each time, we assign the first free color if we have a $\mathcal{D}$-hypergraph and a new color if we have a $\mathcal{C}$-hypergraph. However, the results are different. The greedy algorithm needs no re-coloring; in the worst case, we simply assign a new color to the next vertex. The quasi-greedy algorithm, in the worst case, encounters the deadlock and requires re-coloring of vertices which are already colored. The greedy algorithm gives a possibility to obtain an upper bound for the lower chromatic number directly. It is not the case with Algorithm 10.4.1. We must implement it, obtain a number of colors, and only then write a trivial inequality. One can consider Algorithm 10.2.1 as opposite to Algorithm 10.4.1.

The comparison above explicitly shows that if for finding the maximum number of colors we apply the same approach as for the minimum, we obtain much less.

The value $O(\mathcal{H})$ was called the "resistance" of a $\mathcal{C}$-hypergraph because it shows how the structure of a $\mathcal{C}$-hypergraph may resist the quasi-greedy coloring algorithm. Smaller resistance indicates that fewer colors are lost in the worst case when re-coloring. So from this view point, hypergraphs with $O(\mathcal{H})=0$ deserve special attention.

Theorem 10.4.3 If $\mathcal{H}=(X, \mathcal{C})$ is a hypertree, then $O(\mathcal{H})=0$.
Proof. Induction on $|X|=n$. For $n=2,3$ the assertion is trivial. Assume it holds for all hypertrees on $<n$ vertices. Consider a vertex $x$ that is pendant in the host tree. Since any $\mathcal{C}$-edge of $\mathcal{H}$ has cardinality at least 2, $o(x, \mathcal{H})=0$. From this and $O\left(\mathcal{H}_{Y}\right)=0$ for any $Y \subset X$ (by the induction hypothesis since $\mathcal{H}_{Y}$ is also a hypertree), it follows that $O(\mathcal{H})=0$. $\square$

Corollary 10.4.3 If $\mathcal{H}=(X, \mathcal{C})$ is a hypertree, then Algorithm 10.4.1 requires no recoloring of monochromatic components.

Proof. Apply Theorem 10.4.3 and Corollary 10.4.1. $\square$

Thus, hypertrees are the first class of hypergraphs that play a special role in sequential $\mathcal{C}$-hypergraph coloring.

Exercises 10.4.

1. For $\mathcal{C}$-hypergraph $\mathcal{H}$ in Figure 10.10, find bidegree and originality of each vertex.
2. For $\mathcal{C}$-hypergraph $\mathcal{H}$ in Figure 10.10, find the resistance $O(\mathcal{H})$.
3. For $\mathcal{C}$-hypergraph $\mathcal{H}$ in Figure 10.10, apply Algorithm 10.4.1 to find a proper coloring and a lower bound on the upper chromatic number.
4. For $\mathcal{C}$-hypergraph $\mathcal{H}$ in Figure 10.10, find the upper chromatic number $\overline{\mathrm{X}}(\mathcal{H})$, the respective proper coloring and feasible partition.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-229.jpg?height=466&width=1030&top_left_y=223&top_left_x=368)
Figure 10.10.

5. For $\mathcal{C}$-hypergraph $\mathcal{H}$ in Figure 10.10, explain why Algorithm 10.4.1 requires no recoloring of monochromatic components.

Computer Projects 10.4. Write a program for the following algorithmic problems.

1. Given a $\mathcal{C}$-hypergraph $\mathcal{H}$ and a random coloring, determine if the coloring is proper.
2. Given a $\mathcal{C}$-hypergraph $\mathcal{H}$, implement Algorithm 10.4.1.

### 10.5. Splitting-Contraction Algorithm

Recall that we use the following notation. For a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, the vertex set $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}, n \geq 1$, the edge families $\mathcal{C}=\left\{C_{1}, C_{2}, \ldots, C_{l}\right\}$ and $\mathcal{D}=$ $\left\{D_{1}, D_{2}, \ldots, D_{m}\right\}$; if $\mathcal{C} \neq \emptyset$, then $I=\{1,2, \ldots, l\}$, and if $\mathcal{D} \neq \emptyset$, then $J=\{1,2, \ldots, m\}$. An edge containing another edge as a subset is called including; an edge which is contained as a subset in another edge is called included.

Now, in order to compute $P(\mathcal{H}, \lambda)$ and $R(\mathcal{H})$ for an arbitrary mixed hypergraph $\mathcal{H}=$ $(X, \mathcal{C}, \mathcal{D})$, we provide the following 5 rules.

1. If $\mathcal{H}$ contains an evidently uncolorable edge of any type, then it is uncolorable and can be removed from further considerations (elimination).
2. If $C_{i} \subseteq C_{j}$, then $P(\mathcal{H}, \lambda)=P\left(\mathcal{H}-C_{j}, \lambda\right), R(\mathcal{H})=R\left(\mathcal{H}-C_{j}\right), i, j \in I$; it means that including edge $C_{j}$ can be weakly deleted because the respective coloring constraints are satisfied in the included edge $C_{i}$ ( $\mathcal{C}$-clearing).
3. If $D_{i} \subseteq D_{j}$, then $P(\mathcal{H}, \lambda)=P\left(\mathcal{H}-D_{j}, \lambda\right), R(\mathcal{H})=R\left(\mathcal{H}-D_{j}\right), i, j \in J$; it means that including edge $D_{j}$ can be weakly deleted because the respective coloring constraints are satisfied in the included edge $D_{i}$ ( $\mathcal{D}$-clearing).

4. If $\left\{x_{k}, x_{l}\right\} \notin \mathcal{D}$ and $\left\{x_{k}, x_{l}\right\} \notin \mathcal{C}$, then
$$
P(\mathcal{H}, \lambda)=P\left(\mathcal{H}_{1}, \lambda\right)+P\left(\mathcal{H}_{2}, \lambda\right), \quad R(\mathcal{H})=R\left(\mathcal{H}_{1}\right)+R\left(\mathcal{H}_{2}\right),
$$
where
$$
\begin{gathered}
\mathcal{H}_{1}=\left(X, \mathcal{C}, \mathcal{D}_{1}\right), \mathcal{D}_{1}=\mathcal{D} \cup\left\{x_{k}, x_{l}\right\}, \\
\mathcal{H}_{2}=\left(X, \mathcal{C}_{1}, \mathcal{D}\right), \mathcal{C}_{1}=\mathcal{C} \cup\left\{x_{k}, x_{l}\right\} \text { (splitting). }
\end{gathered}
$$
In other words, we can split the colorings of $\mathcal{H}$ into the colorings of $\mathcal{H}_{1}$ and the colorings of $\mathcal{H}_{2}$; in $\mathcal{H}_{1}$ vertices $x_{k}$ and $x_{l}$ have different colors, and in $\mathcal{H}_{2}$ vertices $x_{k}$ and $x_{l}$ have the same color.
5. If $C_{t}=\left\{x_{k}, x_{l}\right\}$, for some $t \in I$ and $x_{k}, x_{l} \in X$, such that $C_{t} \neq D_{s}$ for any $s \in J$, then
$$
P(\mathcal{H}, \lambda)=P\left(\mathcal{H}_{1}, \lambda\right), \quad R(\mathcal{H})=R\left(\mathcal{H}_{1}\right), \text { where }
$$
$\mathcal{H}_{1}=\left(X_{1}, \mathcal{C}^{1}, \mathcal{D}^{1}\right), X_{1}=\left(X \backslash\left\{x_{k}, x_{l}\right\}\right) \cup\{y\}, \quad y$ is a new vertex;
if $x_{k} \in D_{j}$, or $x_{l} \in D_{j}, j \in J$, then $D_{j}^{1}=\left(D_{j} \backslash\left\{x_{k}, x_{l}\right\}\right) \cup\{y\}$, otherwise $D_{j}^{1}=D_{j}$;
if $x_{k} \in C_{i}$, or $x_{l} \in C_{i}, i \in I, i \neq t$, then $C_{i}^{1}=\left(C_{i} \backslash\left\{x_{k}, x_{l}\right\}\right) \cup\{y\}$, otherwise $C_{i}^{1}=C_{i}$;
$$
\mathcal{C}_{1}=\mathcal{C}-C_{t} \text { (contraction). }
$$
Any $\mathcal{C}$-edge of size 2 can be contracted unless it coincides with a $\mathcal{D}$-edge of size 2 .

Remark. In 5., $n(\mathcal{H})=n\left(\mathcal{H}_{1}\right)+1$ and the equality $R(\mathcal{H})=R\left(\mathcal{H}_{1}\right)$ means that $r_{i}(\mathcal{H})=r_{i}\left(\mathcal{H}_{1}\right)$ for $i=1,2, \ldots, n-1$ and $r_{n}(\mathcal{H})=0$ since $\mathcal{H}$ contains one $\mathcal{C}$-edge $C_{t}$ of size 2. We will use the equalities of chromatic spectra in this sense when discussing different operations on mixed hypergraphs.

The algorithm that allows us to compute $P(\mathcal{H}, \lambda)$ and $R(\mathcal{H})$ for any mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is a generalization of the connection-contraction algorithm for graphs (see Section 5.3.) which was first explicitly suggested by Zykov in 1949. The "embryos" of connection-contraction may be seen in the papers by Birkhoff and Lewis (1946), by Whitney (1932), and even by Birkhoff (1912) where the chromatic polynomials were introduced (in the language of maps!).

Our idea is to find a pair of vertices that is neither a $\mathcal{C}$-edge nor a $\mathcal{D}$-edge, and to split all the colorings of $\mathcal{H}$ into two classes with respect to this pair of vertices. Further, by implementing elimination, $\mathcal{C}$-clearing, $\mathcal{D}$-clearing and contraction (the order is important) the initial problem is reduced to the same problem for the new pair of "simpler" mixed hypergraphs (in the sense that one of them has fewer vertices and the other has more $\mathcal{D}$ -edges of cardinality 2). Next we obtain a list of complete graphs with labeled vertices and finally form a list of all strict colorings. We call this algorithm the "splitting-contraction algorithm" and present it in the following form:

## Algorithm 10.5.1 (splitting-contraction)

INPUT: An arbitrary mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ with $X$ labeled $1,2, \ldots, n$.
OUTPUT: A list $L$ of all strict colorings, the chromatic spectrum $R(\mathcal{H})$, the chromatic polynomial $P(\mathcal{H}, \lambda)$, the chromatic numbers $\chi(\mathcal{H})$ and $\bar{\chi}(\mathcal{H})$.

1. Set lists $L=Z=Y=\emptyset, R(\mathcal{H})=(0,0, \ldots, 0), P(\mathcal{H}, \lambda)=0, \chi(\mathcal{H})=\bar{\chi}(\mathcal{H})=0$. Add $\mathcal{H}$ to $Y$.
2. Verify the condition of elimination for each element from $Y$; delete evidently uncolorable mixed hypergraphs from $Y$.
3. Perform $\mathcal{C}$-clearing and $\mathcal{D}$-clearing where possible in $Y$.
4. Perform contraction where possible in $Y$; when contracting, amalgamate the labels of the respective vertices.
5. Perform one splitting in each element of $Y$ where possible; move complete $\mathcal{D}$-graphs from $Y$ to $Z$; if splitting is performed at least once then go to step 2.
6. Form a list $L$ of all strict colorings using the labels of vertices of complete $\mathcal{D}$-graphs from $Z$.
7. Compute the chromatic spectrum $R(\mathcal{H})$ by counting the numbers of complete $\mathcal{D}$ graphs in $Z$ having exactly $i$ vertices, $i=1,2, \ldots, n$.
8. Compute the chromatic polynomial $P(\mathcal{H}, \lambda)$ using fundamental equality (10.2).
9. Determine $\chi(\mathcal{H}), \bar{\chi}(\mathcal{H})$ using $R(\mathcal{H})$.
10. OUTPUT: list $L$, vector $R(\mathcal{H})$, polynomial $P(\mathcal{H}, \lambda)$, numbers $\chi(\mathcal{H}), \bar{\chi}(\mathcal{H})$. End.

Proposition 10.5.1 For any mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, Algorithm 10.5.1 is correct.

Sketch of Proof. Correctness of the algorithm follows from the evident rules of elimination, clearing, splitting and contraction, and from the fact that every labeled vertex of any complete graph in the list $Z$ corresponds to the monochromatic subset of the respective vertices in precisely one feasible partition of $\mathcal{H}$. The last means that any feasible partition is reachable from $\mathcal{H}$ by the splitting-contraction algorithm. $\square$

Example 10.5.1 The example in Figure 10.11 illustrates the splitting-contraction algorithm and some of the new properties of colorings as well. The $\mathcal{C}$-edges are shown by dashed ellipse and lines. We have here a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, where $X=\{1,2$, $3,4\}, \mathcal{C}=\{C\}=\{\{1,2,3,4\}\}, \mathcal{D}=\left\{D_{1}, D_{2}, D_{3}, D_{4}\right\}=\{\{1,2\},\{2,3\},\{3,4\},\{4,1\}\}$. As the result of splitting-contraction, we obtain

$$
\begin{gathered}
Z=\left\{K_{3}, K_{3}, K_{2}\right\}, R(\mathcal{H})=(0,1,2,0), \\
P(\mathcal{H}, \lambda)=2 \lambda^{(3)}+\lambda^{(2)}=2 \lambda^{3}-5 \lambda^{2}+3 \lambda,
\end{gathered}
$$

$\chi=2, \bar{\chi}=3$, and the corresponding list $L$ of three strict colorings in the form $(c(1), c(2), c(3), c(4))$ is the following (now the numbers are colors):

$$
L=\{(1,2,3,2),(1,2,1,3),(1,2,1,2)\} .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-232.jpg?height=1709&width=1165&top_left_y=249&top_left_x=313)
Figure 10.11. Splitting-contraction algorithm.

The running time of Algorithm 10.5.1 is exponential (see Section 12.2.). It shows that there exists a common unified procedure different from the exhaustive search which enables us to compute all strict colorings and to solve the problems on the minimum and maximum
number of colors simultaneously. Using special properties of mixed hypergraphs, more efficient procedures for the same goals may be found in some cases. One can see that $\mathcal{C}$ -edges were present implicitly in the classic connection-contraction algorithm (namely at the point of contraction) and in this way were implicitly used since 1912. Finally, for an uncolorable mixed hypergraph, the output contains the empty list and zeros.

We can see that the class of polynomials that may be chromatic for mixed hypergraphs is much larger than the class for usual graphs and hypergraphs because of the interactions between $\mathcal{C}$-edges and $\mathcal{D}$-edges.

Example 10.5.2 Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, where $X=\{1,2,3,4,5\}, \quad \mathcal{C}=\{\{1,2,3\},\{1,3,4\}$, $\{1,4,5\},\{1,5,2\}\}, \quad \mathcal{D}=\{\{3,5\}\}$; we have that $\bar{\chi}(\mathcal{H})=3$ and, after adding the $\mathcal{D}$-edge $\{2,4\}$, we obtain the new mixed hypergraph $\mathcal{H}_{1}$ for which $\bar{\chi}\left(\mathcal{H}_{1}\right)=2$. It is easy to see that, in general, adding one $\mathcal{C}$-edge to $\mathcal{H}$ can increase $\chi(\mathcal{H})$ and adding one $\mathcal{D}$-edge can decrease $\bar{\chi}(\mathcal{H})$.

There is one more unusual property of mixed hypergraph colorings, which is impossible in $\mathcal{D}$-hypergraphs. As we have seen, clearing operations eliminate the edges which contain other edges of the same type, while the chromatic spectrum and the chromatic polynomial remain unchanged. In mixed hypergraphs however, some edges not containing other edges of the same type may also be eliminated with the same effect.

Definition 10.5.1 In a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, a $\mathcal{C}$-edge $C \in \mathcal{C}(\mathcal{D}$-edge $D \in$ $\mathcal{D}$ ) is called redundant if it does not contain any other $\mathcal{C}$-edge ( $\mathcal{D}$-edge) as a subset, and

$$
R(\mathcal{H})=R(\mathcal{H}-C)(R(\mathcal{H})=R(\mathcal{H}-D)) .
$$

Example 10.5.3 Let $\mathcal{H}=(X, \mathcal{C}, \emptyset)$, where $X=\{1,2,3,4\}$ and $\mathcal{C}=\{\{1,2,3\}$, $\{1,3,4\},\{1,2,4\},\{2,3,4\}\}$, see Figure 10.12. One can see that any $\mathcal{C}$-edge in $\mathcal{H}$ is redundant because any three $\mathcal{C}$-edges provide that at most two colors are used for the missing triple. Therefore,

$$
R(\mathcal{H})=R\left(\mathcal{H}-C_{j}\right)=(1,7,0,0), j=1,2,3,4 .
$$

Moreover, if we add to $\mathcal{H}$ the family

$$
\mathcal{D}=\{\{1,2\},\{2,3\},\{3,4\},\{4,1\}\}
$$

forming a simple cycle, then in the mixed hypergraph $\mathcal{H}^{\prime}=(X, \mathcal{C}, \mathcal{D})$, any $\mathcal{D}$-edge is also redundant because three other $\mathcal{D}$-edges guarantee different colors at the ends of a missing $\mathcal{D}$-edge.

Proposition 10.5.2 If $\mathcal{H}$ is a disconnected mixed hypergraph and $\mathcal{H}_{1}, \mathcal{H}_{2}, \ldots, \mathcal{H}_{k} k \geq 2$, are the connected components, then

$$
\begin{gathered}
\chi(\mathcal{H})=\max \left\{\chi\left(\mathcal{H}_{1}\right), \chi\left(\mathcal{H}_{2}\right), \ldots, \chi\left(\mathcal{H}_{k}\right)\right\}, \\
\bar{\chi}(\mathcal{H})=\bar{\chi}\left(\mathcal{H}_{1}\right)+\bar{\chi}\left(\mathcal{H}_{2}\right)+\ldots+\bar{\chi}\left(\mathcal{H}_{k}\right), \\
P(\mathcal{H}, \lambda)=P\left(\mathcal{H}_{1}, \lambda\right) P\left(\mathcal{H}_{2}, \lambda\right) \ldots P\left(\mathcal{H}_{k}, \lambda\right) .
\end{gathered}
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-234.jpg?height=1163&width=1163&top_left_y=205&top_left_x=295)
Figure 10.12.

Proof. The formulas follow from the possibility to color the components independently. $\square$

Definition 10.5.2 A mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is called reduced if no edge is a subset of any other edge of the same type and the size of each $\mathcal{C}$-edge is at least 3.

Remark 10.5.1 As follows from the splitting-contraction algorithm, $\mathcal{C}$-clearing, $\mathcal{D}$ -clearing and contractions of $\mathcal{C}$-edges of size two do not change anything; the coloring properties of a mixed hypergraph can be derived from the respective reduced mixed hypergraph. Hence, without loss of generality, $\mathcal{C}$-edges of size 2 and edges containing other edges of the same type may be ignored, i.e. we only may consider reduced mixed hypergraphs.

Exercises 10.5.

1. For mixed hypergraphs $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ in Figure 10.13, apply splitting-contraction Algorithm 10.5.1 to compute both the chromatic polynomials and the chromatic spectra. Find all feasible partitions.

2. Apply the splitting-contraction algorithm to $\mathcal{H}_{1}=\left(\{1,2,3,4\}, K_{4}^{3}, \emptyset\right)$ and $\mathcal{H}_{2}=$ $\left(\{1,2,3,4\}, \emptyset, K_{4}^{3}\right)$ to find the feasible partitions, chromatic polynomials, and chromatic spectra.

Computer Projects 10.5. Write a program for the following algorithmic problems.

1. Given a mixed hypergraph $\mathcal{H}$ and a random coloring, determine if the coloring is proper.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-235.jpg?height=495&width=1100&top_left_y=608&top_left_x=311)
Figure 10.13.
2. Given a mixed hypergraph $\mathcal{H}$, determine if it is reduced.
3. For mixed hypergraphs $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ in Figure 10.13, by generating colorings at random, find an estimate on the chromatic spectrum, the chromatic polynomial, and compare with the exact values.
4. Given a mixed hypergraph $\mathcal{H}$, by generating colorings at random, find an estimate on the chromatic spectrum $R(\mathcal{H})$ and the chromatic polynomial $P(\mathcal{H}, \lambda)$.

### 10.6. Uncolorability

Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be a mixed hypergraph and $\mathcal{C}=\left\{C_{1}, C_{2}, \ldots, C_{l}\right\}$ and $\mathcal{D}=\left\{D_{1}, D_{2}\right.$, $\left.\ldots, D_{m}\right\}$ be two nonempty families of edges. As usual, denote $I=\{1,2, \ldots, l\}$ and $J=$ $\{1,2, \ldots, m\}$. In this section we assume that mixed hypergraph $\mathcal{H}$ is simple, i.e. no edge is contained in any other edge of the same type.

Recall that a mixed hypergraph is called uncolorable if it admits no proper coloring; otherwise, it is called colorable. Next we formulate the colorability problem:

Definition 10.6.1 Given a mixed hypergraph $\mathcal{H}=(X, C, \mathcal{D})$, the problem of deciding whether there exists at least one proper coloring of $\mathcal{H}$ is called the colorability problem.

The colorability problem represents a new type of problem in coloring theory. It contains, as a special case, the problem of deciding whether a classic hypergraph admits a proper coloring with a given number of colors. Namely, to any $\mathcal{D}$-hypergraph, we can
add $\mathcal{C}$-edges of the complete hypergraph $K_{n}^{k+1}$. Then a $\mathcal{D}$-hypergraph $\mathcal{H}=(X, \mathcal{D})$, is $k$ colorable if and only if the mixed hypergraph $\mathcal{H}^{\prime}=\left(X,\binom{X}{k+1}, \mathcal{D}\right)$ is colorable.

Minimal uncolorable mixed hypergraphs. In this subsection we show that quite different methods are required to determine the conditions for colorability in different classes of mixed hypergraphs. Evidently, if a mixed hypergraph contains an uncolorable subhypergraph of any kind (induced or partial), it is uncolorable as well. Therefore, one of the basic goals is to find the list of all minimal uncolorable mixed hypergraphs from a given class and describe the colorability in terms of forbidden subhypergraphs.

In particular, we prove that there are uncolorable mixed hypergraphs $\mathcal{H}$ with arbitrary difference between the upper chromatic number of the partial $\mathcal{C}$-hypergraph $\mathcal{H}_{C}$ and the lower chromatic number of the partial $\mathcal{D}$-hypergraph $\mathcal{H}_{\mathcal{D}}$.

Definition 10.6.2 An uncolorable mixed hypergraph is called (inclusion-wise) minimal uncolorable if it is connected and becomes colorable after the weak removal of any $\mathcal{C}$-edge or any $\mathcal{D}$-edge.

Notice that minimal uncolorable mixed hypergraphs do not contain isolated vertices. If two vertices $x_{1}, x_{2}$ form a bi-edge, then $\mathcal{H}$ is uncolorable, by the evident conflict of constraints on $\left\{x_{1}, x_{2}\right\}$. Thus, minimal uncolorability in this situation immediately implies that in $\mathcal{H}$ there are no further vertices, $\mathcal{C}$-edges, or $\mathcal{D}$-edges. Evidently, a minimal uncolorable mixed hypergraph becomes colorable if we strongly delete any vertex.

Theorem 10.6.1 Every uncolorable mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ contains an inclusion-wise minimal uncolorable (induced, partial) subhypergraph.

Proof. One can sequentially delete vertices (strongly), $\mathcal{C}$-edges (weakly) and $\mathcal{D}$-edges (weakly) until we get a colorable subhypergraph; then restore the last element removed and delete other elements, and so on. Since $\mathcal{H}$ is finite, the assertion follows. $\square$

Definition 10.6.3 Given an uncolorable mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, a partial subhypergraph $\mathcal{H}^{\prime}$ (induced subhypergraph $\mathcal{H}^{\prime}$ ) is called a maximal partial colorable subhypergraph (maximal induced colorable subhypergraph) of $\mathcal{H}$ if adding any $\mathcal{C}$-edge or $\mathcal{D}$-edge (or any vertex with all the incident edges of both types) of $\mathcal{H}$ to $\mathcal{H}^{\prime}$ makes $\mathcal{H}^{\prime}$ uncolorable.

So, minimal uncolorable subhypergraphs and maximal colorable subhypergraphs of uncolorable mixed hypergraphs determine a critical border of colorability. The interaction of $\mathcal{C}$ and $\mathcal{D}$ on the same vertex set $X$ is not simple: $\mathcal{H}_{\mathcal{C}}$ and $\mathcal{H}_{\mathcal{D}}$ may be very easy to color separately, while the whole $\mathcal{H}$ is uncolorable.

To show that, let us consider the following problem: For every integer $k \geq 0$, let $v(k)$ denote the smallest natural number $n$ such that there exists an inclusion-wise minimal uncolorable mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D}),|X|=n$, for which $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)-\chi\left(\mathcal{H}_{\mathcal{D}}\right)=k$. What are the values of $v(k)$ for $k=0,1,2, \ldots$ ?

Observe first that if minimality is not required, then one can easily construct an uncolorable mixed hypergraph $\mathcal{H}$ with large $\bar{\chi}\left(\mathcal{H}_{C}\right)-\chi\left(\mathcal{H}_{\mathcal{D}}\right)$ by taking just one bi-edge of size 2 together with $n-2=k+1$ isolated vertices; then the lower chromatic number of $\mathcal{H}_{\mathcal{D}}$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-237.jpg?height=466&width=466&top_left_y=269&top_left_x=647)
Figure 10.14. The "most uncolorable" mixed hypergraph on four vertices $\mathcal{U}_{4}$.

is 2 and the upper chromatic number of $\mathcal{H}_{C}$ is $n-1$. Second, if $k$ is negative, then every mixed hypergraph is evidently uncolorable. For every $n=|X| \geq 2$, the "most uncolorable" example (if minimality is not required) is the mixed hypergraph $\mathcal{U}_{n}=\left(X,\binom{X}{2},\binom{X}{2}\right.$ ) which is uncolorable together with each of its induced subhypergraphs of order $\geq 2$. In $\mathcal{U}_{n}$, each pair of vertices is a $\mathcal{C}$-edge and a $\mathcal{D}$-edge at the same time. Figure 10.14 shows the most uncolorable mixed hypergraph on four vertices $\mathcal{U}{ }_{4}$.

For nonnegative $k$, the theorem below gives the characterization of the numbers $v(k)$.
Theorem 10.6.2 (Tuza, Voloshin 2000) For every $k \geq 0$,

$$
v(k)=k+4 .
$$

Proof. Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be an inclusion-wise minimal uncolorable mixed hypergraph such that $|X|=n=v(k)$, and $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)-\chi\left(\mathcal{H}_{\mathcal{D}}\right)=k$. We have to prove that $n=v(k)=k+4$.

We show first that $n \geq k+4$. For a contradiction, suppose that $n<k+4$. Since $\mathcal{H}$ is uncolorable, $\chi\left(\mathcal{H}_{\mathcal{D}}\right) \geq 2$. If $\chi\left(\mathcal{H}_{\mathcal{D}}\right) \geq 3$, then $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right) \geq k+3$, which implies $n=k+3$, $\chi\left(\mathcal{H}_{\mathcal{C}}\right)=n$; therefore, $\mathcal{H}$ contains no $\mathcal{C}$-edges and thus it is colorable, a contradiction.

Hence, $\chi\left(\mathcal{H}_{\mathcal{D}}\right)=2$. Then we have only two possibilities for the number of vertices: $n=k+2$ or $n=k+3$.

Similarly to the previous case, for $n=k+2$ and $\bar{\chi}\left(\mathcal{H}_{C}\right)=k+2$ it follows that the mixed hypergraph $\mathcal{H}$ contains no $\mathcal{C}$-edges, and therefore is not uncolorable. Hence, consider the last case $n=k+3$. Since $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)=k+2=n-1$, the partial $\mathcal{C}$-hypergraph $\mathcal{H}_{\mathcal{C}}=$ $(X, \mathcal{C})$ is a bistar, i.e., a $\mathcal{C}$-hypergraph having two vertices, say $x_{1}$ and $x_{2}$, that belong to all $\mathcal{C}$-edges. If this pair $\left\{x_{1}, x_{2}\right\}$ were not a $\mathcal{D}$-edge in $\mathcal{H}_{\mathcal{D}}$, then we could color $x_{1}, x_{2}$ with the first color and the remaining vertices all differently, which again contradicts the uncolorability of $\mathcal{H}$. Consequently, the pair $\left\{x_{1}, x_{2}\right\}$ is a $\mathcal{D}$-edge in $\mathcal{H}$. Since $\mathcal{H}$ is an uncolorable hypergraph minimal under inclusion, no $\mathcal{C}$-edge may coincide with $\left\{x_{1}, x_{2}\right\}$, and therefore the cardinality of each $\mathcal{C}$-edge is at least 3.

Consider an arbitrary proper 2-coloring of $\mathcal{H}_{\mathcal{D}}=(X, \mathcal{D})$. It is, at the same time, a coloring of the initial mixed hypergraph $\mathcal{H}$, because each $\mathcal{C}$-edge contains at least three

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-238.jpg?height=893&width=1121&top_left_y=241&top_left_x=321)
Figure 10.15. Minimal by inclusion uncolorable mixed hypergraph, $k=3$.

vertices. Thus, again, we obtain that $\mathcal{H}$ is colorable. This contradiction implies that $v(k)=$ $n \geq k+4$.

Now, in order to prove the converse inequality $v(k) \leq k+4$, we construct a series of examples of minimal uncolorable mixed hypergraphs with $\bar{\chi}\left(\mathcal{H}_{C}\right)-\chi\left(\mathcal{H}_{\mathcal{D}}\right)=k$ and $n=$ $k+4, k=0,1,2, \ldots$. The construction will depend on the parity of $k$; we first describe the particular cases $k=0,1$ that can be verified directly.
$k=0$.
Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, where $X=\{1,2,3,4\}, \mathcal{C}=\{\{1,2,3\},\{1,2,4\}\}, \mathcal{D}=\{\{1,2\}$, $\{2,3\},\{2,4\},\{3,4\}\}$.
$k=1$.
Consider $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, where $X=\{1,2,3,4,5\}, \mathcal{C}=\{\{1,2,3\},\{1,2,4\},\{1,2,5\}\}$, $\mathcal{D}=\{\{1,2\},\{3,4\},\{4,5\},\{3,5\}\}$.
$k=2 l, l \geq 1$.
Construct the mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, where $X=\{1,2,3, \ldots, k+4\}, \mathcal{C}=$ $\{\{1,2, i\}: 3 \leq i \leq k+4\}$, and $\mathcal{D}=\{\{i, i+1\}: 1 \leq i \leq k+3\} \cup\{k+4,2\}$.

In other words, $\mathcal{H}_{\mathcal{C}}=(X, \mathcal{C})$ represents a 3-uniform bistar in which vertices 1,2 belong to all $\mathcal{C}$-edges, and therefore $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)=n-1=k+3$. Moreover, $\mathcal{H}_{\mathcal{D}}=(X, \mathcal{D})$ is the odd cycle $(2,3,4, \ldots, k+4,2)$ with the pendant $\mathcal{D}$-edge $\{1,2\}$, so that $\chi\left(\mathcal{H}_{\mathcal{D}}\right)=3$.

Let us try to construct a proper coloring $c$ of $\mathcal{H}$. As usual, $c(i)$ means the color of vertex $i, i=1,2, \ldots, n$. In any possible coloring of $\mathcal{H}$, vertices 1 and 2 have to be colored differently, say $c(1)=1, c(2)=2$. Since $\{2,3\}$ is a $\mathcal{D}$-edge, we have $c(3) \neq c(2)$ and, because of the $\mathcal{C}$-edge $\{1,2,3\}$, the unique possibility for vertex 3 to get colored is $c(3)=$ $c(1)=1$. In the same way, $c(4) \neq c(3)$ and, because of the $\mathcal{C}$-edge $\{1,2,4\}$, the unique possibility for vertex 4 to be colored is $c(4)=c(2)=2$.

It is now clear that the colors have to alternate on the cycle $(2,3,4, \ldots, k+4)$. Since $c(k+3)=1$ and $c(2)=2$, we can color vertex $k+4$ neither with color 1 nor with color 2. However, any other color $c(k+4)$ is infeasible because of the $\mathcal{C}$-edge $\{1,2, k+4\}$. Consequently, $\mathcal{H}$ is uncolorable. One can easily check that it is minimal under inclusion. $k=2 l+1, l \geq 1$.

Construct the mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, where $X=\{1,2,3, \ldots, k+4\}, \mathcal{C}=$ $\{\{1,2, i\}: 3 \leq i \leq k+4\}$, and $\mathcal{D}=\{1,2\} \cup\{\{i, i+1\}: 3 \leq i \leq k+3\} \cup\{k+4,3\}$.

Again, $\mathcal{H}_{\mathcal{C}}=(X, \mathcal{C})$ represents a 3-uniform bistar with vertices 1,2 shared by all $\mathcal{C}$ edges, so that $\bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)=n-1=k+3$. In the present case, $\mathcal{H}_{\mathcal{D}}=(X, \mathcal{D})$ is a disconnected graph having $\mathcal{D}$-edge $\{1,2\}$ as the first component and the odd cycle $(3,4, \ldots, k+4,3)$ as the second component, yielding again $\chi\left(\mathcal{H}_{\mathcal{D}}\right)=3$. Case $k=3$ is shown in Figure 10.15.

Let $c(1)=1, c(2)=2$. For $c(3)$ there are only two possibilities: $c(3)=1$, or $c(3)=2$. By symmetry, we may assume $c(3)=1$. Then, similarly to the argument above, we obtain $c(4)=2, c(5)=1, c(6)=2$, and so on; i.e., the colors have to alternate along the odd cycle. Since vertex $k+4$ cannot be colored with any color (because of the $\mathcal{C}$-edge $\{1,2, k+4\}$ and the $\mathcal{D}$-edges $\{k+3, k+4\}$ and $\{k+4,3\}$ ), we conclude that $\mathcal{H}$ is uncolorable. Minimality is also easily seen. Hence, the theorem follows. $\square$

Complete uncolorable mixed hypergraphs. For $2 \leq l, m \leq n=|X|$, let

$$
\mathcal{K}(n, l, m)=(X, \mathcal{C}, \mathcal{D})=\left(X,\binom{X}{l},\binom{X}{m}\right) .
$$

Hence, $|\mathcal{C}|=\binom{n}{l}$ and $|\mathcal{D}|=\binom{n}{m}$. Call $\mathcal{K}(n, l, m)$ the complete $(l, m)$-uniform mixed hypergraph of order $n$. In other words, in $\mathcal{K}(n, l, m)$ every $l$ vertices form a $\mathcal{C}$-edge, and every $m$ vertices form a $\mathcal{D}$-edge. Evidently, for given $n, l, m$ there exists exactly one (up to isomorphism) $\mathcal{K}(n, l, m)$. Complete (4,2)-uniform mixed hypergraph $\mathcal{K}(4,4,2)$ is shown in Figure 10.16.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-239.jpg?height=362&width=368&top_left_y=1828&top_left_x=699)
Figure 10.16. $\mathcal{K}(4,4,2)$.

Theorem 10.6.3 (Tuza, Voloshin, 2000) $\mathcal{K}(n, l, m)$ is uncolorable if and only if

$$
n \geq(l-1)(m-1)+1 .
$$

Proof. ⇒ Let $n \leq(l-1)(m-1)$. We color $m-1$ vertices with the first color, the next $m-1$ vertices with the second color, etc. Since $n \leq(l-1)(m-1)$, this procedure requires at most $l-1$ colors, and a proper coloring of $\mathcal{K}(n, l, m)$ is obtained; i.e., the hypergraph is colorable.
⇐ Let $n \geq(l-1)(m-1)+1$. Suppose there exists a proper coloring of $\mathcal{K}(n, l, m)$. Since each $m$-tuple is a $\mathcal{D}$-edge and each $l$-tuple is a $\mathcal{C}$-edge, the number of vertices in any one color class does not exceed $m-1$ and the total number of colors does not exceed $l-1$. Since $n \geq(l-1)(m-1)+1$, there is at least one $\mathcal{C}$-edge or $\mathcal{D}$-edge colored improperly, a contradiction. $\square$

If we fix $l$ and $m$, and let $n$ approach the infinity, then we have the fixed number (namely, $(l-1)(m-1))$ of colorable mixed hypergraphs $\mathcal{K}(n, l, m)$ and any number of uncolorable $\mathcal{K}(n, l, m)$. In other words, when $n$ is growing, the share of colorable $\mathcal{K}(n, l, m)$ becomes smaller and smaller. This can be stated as the following corollary.

Corollary 10.6.1 (Tuza, Voloshin 2000) For fixed $(l, m)$, almost all $\mathcal{K}(n, l, m)$ are uncolorable.

A completely different conclusion is obtained, however, if we do not fix the values $l$ and $m$. In the analysis below it will turn out that the proportion of uncolorable complete mixed hypergraphs of order $n$ tends to zero as $n$ gets large.

Theorem 10.6.4 (Tuza, Voloshin, 2000) For unrestricted $(l, m)$, almost all $\mathcal{K}(n, l, m)$ are colorable.

Proof. In order to simplify the formulas, let us calculate for mixed hypergraphs of order $n+1$ instead of $n$. Since $l=1$ and $m=1$ are excluded by definition, we have $n^{2}$ possibilities to choose the pair $(l, m)$ in the range $2 \leq l \leq n+1,2 \leq m \leq n+1$. Applying Theorem 10.6.3, we obtain that $\mathcal{K}(n, l, m+1)$ is uncolorable if and only if

$$
(l-1)(m-1) \leq n .
$$

Here the smallest possible value of $m-1$ is 1 . Thus, for each $l \geq 2$, there are precisely $\left\lfloor\frac{n}{l-1}\right\rfloor$ uncolorable complete mixed hypergraphs of order $n+1$. Consequently, the total number $N_{n}$ of complete uncolorable mixed hypergraphs on $n+1$ vertices equals

$$
N_{n}=\sum_{k=1}^{n}\left\lfloor\frac{n}{k}\right\rfloor \simeq n \log n
$$

where the asymptotic equation is meant as $n$ tends to infinity (here and next we use simple calculus formulas). Thus, the proportion of uncolorable complete mixed hypergraphs equals

$$
\lim _{n \rightarrow \infty} \frac{N_{n}}{n^{2}}=\lim _{n \rightarrow \infty} \frac{\log n}{n}=0,
$$

implying that almost all large complete mixed hypergraphs are colorable. $\square$

| $l \ m$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2 | - | - | - | - | - | - | - |
| 3 | - | - | - | + | + | + | + |
| 4 | - | - | + | + | + | + | + |
| 5 | - | + | + | + | + | + | + |
| 6 | - | + | + | + | + | + | + |
| 7 | - | + | + | + | + | + | + |
| 8 | - | + | + | + | + | + | + |

Figure 10.17. The uncolorability of $\mathcal{K}(8, l, m)$.

Example 10.6.1 The behavior of the uncolorability of $\mathcal{K}(8, l, m)$ is shown in Figure 10.17. The signs "+" and "_" mean that for given $l, m$, the mixed hypergraph $\mathcal{K}(8, l, m)$ is colorable or uncolorable, respectively. The statements above may be commented on in the following way. When $n$ tends to infinity, and if $l, m$ are fixed, then the uncolorability zone sooner or later reaches any $\mathcal{K}(n, l, m)$; however, if $l, m$ are not fixed, then the ratio of the uncolorability zone in the entire "big square" tends to zero. The table in Figure 10.17 contains 16 cases of uncolorability and 33 cases of colorability; therefore the ratio of uncolorability is 16/49.

Colorability of mixed hypertrees. A mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is called a mixed hypertree if there exists a host tree $T=(X, E)$ such that every $C \in \mathcal{C}$ and every $D \in \mathcal{D}$ induces a subtree in $T$. Clearly, it is a direct generalization of the hypertree concept studied in Chapter 8 which now corresponds to the case $\mathcal{C}=\emptyset$.

Recall that in a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, a $\mathcal{D}$-edge $D \in \mathcal{D}$, is called evidently uncolorable if each pair of vertices $x, y \in D$ is connected by a $\mathcal{C}$-path of $\mathcal{H}$ consisting of $\mathcal{C}$-edges of size 2.

Theorem 10.6.5 (Tuza, Voloshin 2000) A mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is uncolorable if and only if it contains an evidently uncolorable $\mathcal{D}$-edge.

Proof. ⇒ Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be an uncolorable mixed hypertree. By contradiction, suppose it does not contain evidently uncolorable $\mathcal{D}$-edges. Observe that if it contains no $\mathcal{C}$-edges of size 2, then it is colorable. Indeed, consider the corresponding host tree $T$ and color it as usual, starting at any vertex and alternating colors 1 and 2 along the tree. The coloring obtained is, at the same time, a proper coloring of $\mathcal{H}$. If $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ contains $\mathcal{C}$-edges of size 2, then each of them coincides with an edge of $T$. Now we repeat the previous procedure with the following exception: if we encounter a $\mathcal{C}$-edge of size 2, then we do not change color along this edge of $T$ (i.e., an edge of $T$ becomes properly colored if and only if it is not a $\mathcal{C}$-edge in $\mathcal{H}$ ). Since there are no evidently uncolorable $\mathcal{D}$-edges in $\mathcal{H}$, we again obtain a proper coloring of $\mathcal{H}$. Therefore, $\mathcal{H}$ is colorable, a contradiction

⇐ Obvious. $\square$

We end the section with the following evident
Corollary 10.6.2 Every reduced mixed hypertree is a colorable mixed hypergraph.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-242.jpg?height=440&width=958&top_left_y=269&top_left_x=394)
Figure 10.18. Uncolorable mixed hypertree.

Corollary 10.6.3 If $\mathcal{H}$ is a colorable mixed hypertree, then $\chi(\mathcal{H}) \leq 2$.
An example of uncolorable mixed hypertree is shown in Figure 10.18. As usual, $\mathcal{C}$ edges are drawn by dashed curves, and $\mathcal{D}$-edges are drawn by solid curves; the host tree is not shown.

Exercises 10.6.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-242.jpg?height=518&width=836&top_left_y=1282&top_left_x=414)
Figure 10.19.

1. For mixed hypergraph $\mathcal{H}$ in Figure 10.19, find the lower chromatic number of $\mathcal{H}_{\mathcal{D}}$ and the upper chromatic number of $\mathcal{H}_{\mathcal{C}}$.
2. Prove that mixed hypergraph $\mathcal{H}$ in Figure 10.19 is uncolorable.
3. For mixed hypergraph $\mathcal{H}$ in Figure 10.19, find a minimal uncolorable subhypergraph.
4. For mixed hypergraph $\mathcal{H}$ in Figure 10.19, find a maximal colorable subhypergraph.

Computer Projects 10.6. Write a program for the following algorithmic problems.

1. Given a mixed hypergraph $\mathcal{H}$, by generating colorings at random, determine if it is colorable.
2. Given an uncolorable mixed hypergraph $\mathcal{H}$, by generating colorings at random, find a maximal colorable (induced / partial) subhypergraph.

### 10.7. Unique Colorability

Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be an arbitrary mixed hypergraph and no edge is included, i.e. contained in any other edge of the same type.

Definition 10.7.1 A mixed hypergraph $\mathcal{H}$ is called uniquely colorable (uc hypergraph or uc for short) if it has precisely one strict coloring apart from permutation of colors. The class of uniquely colorable mixed hypergraphs is denoted by $\mathcal{U C}$.

Equivalently, $\mathcal{H}$ is uc if it allows exactly one feasible partition of the vertex set $X$ into color classes. Let us agree that the expression "unique coloring" means "unique partition" into the corresponding number of color classes. This means that we ignore the permutation of colors unless stated otherwise. The term "uniquely colorable" is inherited from graph coloring; the meaning of it is "uniquely partitionable".

Evidently, if $\mathcal{H}$ is a uc hypergraph, then

$$
\chi(\mathcal{H})=\bar{\chi}(\mathcal{H})=\chi, r_{\chi}(\mathcal{H})=1,
$$

and

$$
R(\mathcal{H})=(0, \ldots, 0,1,0, \ldots, 0) .
$$

Therefore,

$$
P(\mathcal{H}, \lambda)=\lambda(\lambda-1)(\lambda-2) \cdots(\lambda-\chi+1)=\lambda^{(\chi)} .
$$

A classic graph $G$ as a $\mathcal{D}$-graph, is uniquely colorable if and only if $G$ is a complete graph $K_{n}$ (this is true for all $\mathcal{D}$-hypergraphs). In other words, the uc mixed hypergraphs represent merely generalizations of cliques. As we know, the complete $r$-uniform hypergraph $K_{n}^{r}$ is a generalization of $K_{n}$; however, the coloring properties of $K_{n}^{r}$ are far to be as nice as those of uc mixed hypergraphs. This reflects the fact that $K_{n}^{r}$ is uc if and only if $r=2$.

Proposition 10.7.1 Given a uc mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ with a unique strict coloring $c$, then the union of any two color classes contains a $\mathcal{D}$-edge; any partition of any color class encounters a $\mathcal{C}$-edge having exactly two vertices in common with this color class and at most one vertex in common with any other color class.

Proof. This follows directly from the definition of a proper coloring of a mixed hypergraph. $\square$

Definition 10.7.2 In a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, a sequence of vertices $x=$ $x_{0}, x_{1}, \ldots, x_{k}=y, k \geq 1$, is called an $(x, y)$-invertor if and only if $x_{i} \neq x_{i+1}$ and $\left(x_{i}, x_{i+1}\right) \in \mathcal{D}$ for every $i=0,1, \ldots, k-1$, and, moreover, the following implication holds:

$$
x_{j} \neq x_{j+1} \neq x_{j+2} \neq x_{j} \Rightarrow\left\{x_{j}, x_{j+1}, x_{j+2}\right\} \in \mathcal{C}, j=0,1, \ldots, k-2 .
$$

The $(x, y)$-invertor is called odd or even if $k$ is odd or even, respectively; it is called cyclic if $x=y$; and if $k \geq 2$, then $x_{1}, \ldots, x_{k-1}$ are termed internal vertices.

If a mixed hypergraph has an even $(x, y)$-invertor, then in every proper coloring, the vertices $x$ and $y$ have the same color; in this case, the $(x, y)$-invertor "transports" the color of vertex $x$ to vertex $y$. In contrast, if there is an odd $(x, y)$-invertor, then in every coloring, the vertices $x$ and $y$ have different colors; in this case, the $(x, y)$-invertor "excludes" the color of vertex $y$ to be the color of vertex $x$. Notice that invertors may be induced or partial subhypergraphs, and induce either a uc subhypergraph or an uncolorable one.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-244.jpg?height=386&width=1139&top_left_y=919&top_left_x=280)
Figure 10.20. Invertors.

Two examples of invertors are shown in Figure 10.20. $\mathcal{H}_{1}$ is an odd invertor $x_{0}, x_{1}$, $x_{2}, x_{3}$, while $\mathcal{H}_{2}$ is an even invertor $x_{0}, x_{1}, x_{2}, x_{3}, x_{4}$. The colors are shown by numbers 1 and 2. While in $\mathcal{H}_{1}$, the $\mathcal{D}$-edges represent a simple path connecting $x_{0}$ and $x_{3}$, in $\mathcal{H}_{2}$, the $\left(x_{0}, x_{4}\right)$-path uses edge $\left\{x_{1}, x_{2}\right\}$ twice, i.e. it is not a simple path. The important feature however, is that every three different consecutive vertices in such path form a $\mathcal{C}$-edge. Both $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ are uc mixed hypergraphs with the unique strict coloring shown in the figure. In every proper coloring of $\mathcal{H}_{1}$, the vertices $x_{0}$ and $x_{3}$ have different colors. In contrast, in any proper coloring of $\mathcal{H}_{2}$, the vertices $x_{0}$ and $x_{4}$ have the same color. We say that $\mathcal{H}_{1}$ excludes vertex $x_{3}$ from having the color of vertex $x_{0}$; and, $\mathcal{H}_{2}$ "transports" the color of vertex $x_{0}$ to vertex $x_{4}$. One can easily see that for both invertors $\chi=\bar{\chi}=2$, and, moreover

$$
R\left(\mathcal{H}_{1}\right)=R\left(\mathcal{H}_{2}\right)=(0,1,0,0), P\left(\mathcal{H}_{1}, \lambda\right)=P\left(\mathcal{H}_{2}, \lambda\right)=\lambda(\lambda-1) .
$$

The latter means that from coloring point of view, the invertors simply extend the properties of complete graph $K_{2}$.

Embeddings into uc mixed hypergraphs. In $\mathcal{D}$-hypergraphs, for each $n$ we have the only uc graph $K_{n}$; the fundamental property is that any induced subgraph of $K_{n}$ is a uc graph as well. There is a very different situation in mixed hypergraphs. In this subsection,
we show that every mixed hypergraph having at least one coloring may be an induced subhypergraph of a uniquely colorable mixed hypergraph. Namely, we embed a mixed hypergraph $\mathcal{H}$ into a mixed hypergraph $\mathcal{H}^{\prime}$ such that $\mathcal{H}^{\prime}$ has a unique strict coloring. More precisely:

Theorem 10.7.1 (Tuza, Voloshin, Zhou 2002) Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be a colorable mixed hypergraph and $c=X_{1} \cup \cdots \cup X_{t}$ be a strict $t$-coloring. Then there exists a uc mixed hypergraph $\mathcal{H}^{\prime}=\left(X^{\prime}, \mathcal{C}^{\prime}, \mathcal{D}^{\prime}\right)$ with the following properties:

1. $\mathcal{H}$ is an induced subhypergraph of $\mathcal{H}^{\prime}$;
2. $\chi\left(\mathcal{H}^{\prime}\right)=\bar{\chi}\left(\mathcal{H}^{\prime}\right)=t$ and an extension of $c$ is the unique strict coloring of $\mathcal{H}^{\prime}$.

Proof. To extend $\mathcal{H}$ into some $\mathcal{H}^{\prime}$ in the required way, we first choose a dummy spanning tree $T_{i}$ inside each partition class $X_{i}$ of $c$. For every edge $x y$ of $T_{i}$ we put an even $(x, y)$-invertor with internal vertices not in $X$. Different even invertors should be internally disjoint. These invertors ensure that vertices from $X_{i}$ will always have the same color.

At this point, the internal vertices of the invertors may get new colors; hence, the number of possible colors for $\mathcal{H}^{\prime}$ may increase. In order to avoid this, we insert one $\mathcal{C}$-edge of size 3, $\left\{x=x_{1}, x_{2}, z\right\}$, for each even $(x, y)$-invertor, where $z$ is any vertex such that $x$ and $z$ belong to distinct color classes $X_{i}$ under $c$. These $\mathcal{C}$-edges imply that no new color will occur outside $X$.

Next, for each pair $(i, j)$ such that $X_{i}$ and $X_{j}$ are two distinct classes of $c$, we choose two vertices $x_{i} \in X_{i}$ and $x_{j} \in X_{j}$, and build an odd $\left(x_{i}, x_{j}\right)$-invertor on them. Then any two vertices belonging to distinct classes of $c$ are assigned distinct colors. Again, the newly added intermediate vertices in odd invertors should be distinct for the distinct vertex pairs of $\mathcal{H}$, and should not be in $X$. Since colors on invertors alternate, the colors on an odd invertor are all the same as the two colors at the endpoints. Hence, no new colors outside $X$ can occur on internal vertices of newly created invertors.

It is clear that such extension of $c$ is the unique strict coloring of $\mathcal{H}^{\prime}$ with precisely $t$ color classes because each class of $c$ is monochromatic (due to the presence of even invertors) and no pair of vertices belonging to distinct color classes of $c$ can get the same color (by the odd invertors). $\square$

Uniquely colorable mixed hypertrees. In a mixed hypergraph $\mathcal{H}$, for two vertices $x, y$ there may be many $(x, y)$-invertors (a subhypergraph induced by an $(x, y)$-invertor is also termed an ( $x, y$ )-invertor). Two ( $x, y$ )-invertors are different if they represent two different sequences of vertices. The shortest $(x, y)$-invertor contains the minimum number of vertices. Recall that an $(x, y)$-invertor with $x=y$ is called a cyclic invertor. We show here that invertors play an important role in uniquely colorable mixed hypertrees. Also recall that reduced mixed hypertrees are colorable (Corollary 10.6.2).

Definition 10.7.3 In a mixed hypertree, a cyclic invertor is called simple if all $\mathcal{C}$-edges are different, any $\mathcal{D}$-edge is used along the invertor precisely two times, and the repetition is sequential.

Let $\mu=\left(z_{0}, z_{1}, \ldots, z_{k}=z_{0}\right), k \geq 6$ be a simple cyclic invertor in a mixed hypertree. Without loss of generality, assume that $z_{0} \neq z_{1} \neq z_{2} \neq z_{0}$. From the definition of a simple cyclic invertor, it follows that $z_{0} \neq z_{2} \neq \ldots \neq z_{k-2}$ and $z_{1}=z_{3}=\ldots=z_{k-1}=y$, where $y$ is the center of a star in the host tree $T$.

Theorem 10.7.2 If $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is a reduced mixed hypertree with $|\mathcal{D}| \leq n-2$, then $r_{2}(\mathcal{H}) \geq 2$.

Proof. Let $T=(X, \mathcal{E})$ be a host tree of the mixed hypertree $\mathcal{H}$. Since $|\mathcal{D}| \leq n-2$, in $T$ there exists an edge $e=\{x, y\} \notin \mathcal{D}$. Starting with vertices $x, y$, we can construct two different colorings with colors 1 and 2 generating two different partitions. First, put $c(x)=c(y)=1$ and color all the other vertices alternatively along the tree $T$ with the colors $2,1,2, \ldots$. Second, apply the same procedure starting with $c(x)=1$ and $c(y)=2$. $\square$

Theorem 10.7.3 (Niculitsa, Voloshin, 2000) A reduced mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is uniquely colorable if and only if for every two vertices $x, y \in X$ there exists an $(x, y)$-invertor.

Proof. ⇒ Let $c$ be the unique feasible partition of the mixed hypertree $\mathcal{H}$. Recall that $c(x)$ denotes the color class of vertex $x$ in the partition, or, equivalently, the color of vertex $x$. We show that for any two vertices $x, y \in X$ there exists an $(x, y)$-invertor.

Suppose $\mathcal{H}$ has two vertices $u, v \in X$ such that there is no $(u, v)$-invertor in $\mathcal{H}$. Consider the unique $(u, v)$-path in the host tree T of $\mathcal{H}$. The assumption implies that either, in $\mathcal{H}$, there is no $\mathcal{D}$-path connecting $u$ and $v$ or, in the sequence $u=x_{1}, x_{2}, \ldots, x_{p}=v$, there exists a triple of pairwise different vertices $x_{j}, x_{j+1}, x_{j+2}$ not belonging to $\mathcal{C}$. If there is no $\mathcal{D}$-path connecting $u$ and $v$, then, by Theorem 10.7.2, $\mathcal{H}$ has two different feasible partitions, a contradiction.

Assume now that in the sequence $u=x_{1}, x_{2}, \ldots, x_{p}=v$, each pair of consecutive vertices is a $\mathcal{D}$-edge, and there is a triple of pairwise different vertices $x_{j}, x_{j+1}, x_{j+2}$ such that $\left\{x_{j}, x_{j+1}, x_{j+2}\right\} \notin \mathcal{C}$. Evidently, $x_{j+1}$ is not pendant in $T$. Let $T_{1}$ and $T_{2}$ be two connected components obtained after deletion of vertex $x_{j+1}$ from the host tree $T$. There are two cases.

1) $c\left(x_{j}\right)=c\left(x_{j+2}\right)$. Evidently, the number of color classes in the unique partition $c$ of $\mathcal{H}$ is 2 . Re-color the vertex $x_{j+2}$ and all vertices of even distance from $x_{j+2}$ in the component $T_{2}$ with the new color. The obtained coloring is a proper coloring of $\mathcal{H}$ inducing a feasible partition different from $c$, a contradiction.
2) $c\left(x_{j}\right) \neq c\left(x_{j+2}\right)$. Since $\left\{x_{j}, x_{j+1}\right\},\left\{x_{j+1}, x_{j+2}\right\} \in \mathcal{D}, c\left(x_{j}\right) \neq c\left(x_{j+1}\right) \neq c\left(x_{j+2}\right)$. Consequently, $\mathcal{H}$ is colored with at least three colors. But every mixed hypertree can also be colored with two colors, and we again have two different feasible partitions, a contradiction.

⇐ Assume that any two vertices $x, y \in X$ are joined by an $(x, y)$-invertor. Suppose $\mathcal{H}$ has at least two distinct feasible partitions $c_{1}$ and $c_{2}$. Then there are two vertices, say $x^{\prime}, y^{\prime}$, such that $c_{1}\left(x^{\prime}\right)=c_{1}\left(y^{\prime}\right)$ but $c_{2}\left(x^{\prime}\right) \neq c_{2}\left(y^{\prime}\right)$. Without loss of generality, consider an $\left(x^{\prime}, y^{\prime}\right)$ - invertor $x^{\prime}=x_{0}, x_{1}, \ldots x_{k}=y^{\prime}$. From the definition of an invertor, it follows that, if $k$ is even, then in all possible colorings the vertices $x^{\prime}$ and $y^{\prime}$ have the same color; if $k$ is odd, then in all possible colorings the vertices $x^{\prime}$ and $y^{\prime}$ have distinct colors. Therefore, in all colorings, either $c\left(x^{\prime}\right)=c\left(y^{\prime}\right)$ or $c\left(x^{\prime}\right) \neq c\left(y^{\prime}\right)$, a contradiction. $\square$

Corollary 10.7.1 If $\mathcal{H}=(X, C, \mathcal{D})$ is a reduced uniquely colorable mixed hypertree with the host tree $T=(X, \mathcal{E})$, then $\mathcal{D}=\mathcal{E}$.

Recall that in a mixed hypergraph $\mathcal{H}$, the $\mathcal{C}$-edge $C \in \mathcal{C}$ is called redundant if $R(\mathcal{H})=$ $R(\mathcal{H}-C)$.

Corollary 10.7.2 If $\mathcal{H}=(X, C, \mathcal{D})$ is a reduced uniquely colorable mixed hypertree, then no $\mathcal{D}$-edge is redundant.

Corollary 10.7.3 In a reduced uniquely colorable mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, any $\mathcal{C}$-edge of size $\geq 4$ is redundant.

Proof. No invertor contains such a $\mathcal{C}$-edge. $\square$

Theorem 10.7.4 In a reduced uniquely colorable mixed hypertree $\mathcal{H}=(X, C, \mathcal{D})$, a $\mathcal{C}$ -edge $C$ of size 3 is redundant if and only if there exists a simple cyclic invertor containing $C$.

Proof. $\Rightarrow$ Let $C=\left\{x_{1}, x_{2}, x_{3}\right\}$ be the redundant $\mathcal{C}$-edge. By definition $\mathcal{H}^{\prime}=\left(X, \mathcal{C}^{\prime}, \mathcal{D}\right)$ where $\mathcal{C}^{\prime}=\mathcal{C} \backslash\{C\}$ is a uniquely colorable mixed hypertree. Then for the vertices $x_{1}$ and $x_{3}$ in $\mathcal{H}^{\prime}$ there exists an $\left(x_{1}, x_{3}\right)$-invertor: $x_{1}=z_{0}, z_{1}, \ldots, z_{k}=x_{3}$. Construct the $\left(x_{1}, x_{1}\right)$-invertor in the following way: $x_{1}=z_{0}, z_{1}, \ldots, z_{k}=x_{3}, x_{2}, x_{1}$. This invertor is a simple cyclic invertor of $\mathcal{H}$ containing $C$.

⇐ Conversely, suppose that the $\mathcal{C}$-edge $C=\left\{x_{1}, x_{2}, x_{3}\right\}$ is contained in a simple cyclic invertor $x_{1}=z_{0}, z_{1}, \ldots, z_{k}=x_{3}, x_{2}, x_{1}$. Then the vertices $x_{1}$ and $x_{3}$ are joined by two different $\left(x_{1}, x_{3}\right)$-invertors: $\left\{x_{1}, x_{2}, x_{3}\right\}=C$ and $x_{1}=z_{0}, z_{1}, \ldots, z_{k}=x_{3}=\left(x_{1}, x_{3}\right)^{\prime}$-invertor. In each $(x, y)$-invertor containing $C$, replace this $\mathcal{C}$-edge by the $\left(x_{1}, x_{3}\right)^{\prime}$-invertor. Thus, $\mathcal{H}^{\prime}=(X, \mathcal{C} \backslash$ $\{C\}, \mathcal{D})$ is uniquely colorable; i.e., the $\mathcal{C}$-edge $C$ is redundant. $\square$

Consider a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$. Let $X=X_{1} \cup X_{2} \cup \ldots \cup X_{i}$ be a proper $i$-coloring of $\mathcal{H}, \chi(\mathcal{H}) \leq i \leq \bar{\chi}(\mathcal{H})$ and choose any $X_{j}$.

Definition 10.7.4 The touching graph of a color class $X_{j}$ is the graph $L_{j}=\left(X_{j}, E_{j}\right)$ where the edge set $E_{j}$ is defined in the following way: $\{x, y\} \in E_{j}$ if and only if some $C \in C$ satisfies $C \cap X_{j}=\{x, y\}$, and $\left|C \cap X_{k}\right| \leq 1$ for any $k \neq j$.

Theorem 10.7.5 Given a mixed hypergraph $\mathcal{H}$ and an arbitrary $\bar{\chi}$-coloring of $\mathcal{H}$, then all $\bar{\chi}$ touching graphs are connected.

Proof. If at least one touching graph is disconnected, then we can construct a new strict coloring of $\mathcal{H}$ with $\bar{\chi}+1$ colors by assigning a new color to the vertices of one component. $\square$

Notice that the connectedness of a touching graph for a color class means that we can't split the color class into two smaller ones.

Corollary 10.7.4 Given a uniquely colorable mixed hypergraph $\mathcal{H}$ and the unique partition $c$, then all $\bar{\chi}(\mathcal{H})$ touching graphs are connected.

Corollary 10.7.5 If a reduced mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is uniquely colorable, then in its 2-coloring, the touching graphs $L_{1}$ and $L_{2}$ are connected.

Theorem 10.7.6 Given any uniquely colorable mixed hypergraph $\mathcal{H}=(X, C, \mathcal{D})$, then

$$
|C| \geq n-\chi .
$$

Proof. Let $\mathcal{H}$ be a uniquely colorable mixed hypergraph, $\chi(\mathcal{H})=\chi$. Consider a unique $\chi$-coloring $X=X_{1} \cup X_{2} \cup \ldots \cup X_{\chi}$ and construct the touching graphs

$$
L_{1}=\left(X_{1}, E_{1}\right), L_{2}=\left(X_{2}, E_{2}\right), \ldots, L_{\chi}=\left(X_{\chi}, E_{\chi}\right) .
$$

The minimum number of edges in $L_{i}$ required for $L_{i}$ to be connected is $\left|X_{i}\right|-1$, and, in this case, each $L_{i}$ is a tree, $i=1,2, \ldots, \chi$. Since every edge in $L_{i}$ corresponds to some $\mathcal{C}$-edge of $\mathcal{H}$, we obtain that the minimum number of $\mathcal{C}$-edges is:

$$
\left|X_{1}\right|-1+\left|X_{2}\right|-1+\ldots+\left|X_{\chi}\right|-1=|X|-\chi .
$$ $\square$

Corollary 10.7.6 A mixed hypergraph $\mathcal{H}$ with $|\mathcal{C}|<n-\chi(\mathcal{H})$ is not uc.
Corollary 10.7.7 The minimum number of $\mathcal{C}$-edges in any reduced uniquely colorable mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is $n-2$.

Corollary 10.7.8 In a reduced uniquely colorable mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, the number of redundant $\mathcal{C}$-edges is $|\mathcal{C}|-n+2$.

Proof. Indeed, for each touching graph $L_{i}$, construct a spanning tree $T_{i}, i=1,2$. Each elementary cycle in $L_{i}$ generates some simple cyclic invertor in $\mathcal{H}$. Therefore, every $\mathcal{C}$ edge of $\mathcal{H}$ is redundant if it has size $\geq 4$, or corresponds to some edge of $L_{i}$ which is a chord with respect to $T_{i}$. $\square$

Remark. A redundant $\mathcal{C}$-edge may become irredundant after deleting some other redundant $\mathcal{C}$-edges from $\mathcal{C}$.

Definition 10.7.5 A reduced mixed hypertree $\mathcal{H}=(X, C, \mathcal{D})$ is called complete if every edge of the host tree $T$ forms a $\mathcal{D}$-edge, and every path on three vertices of $T$ forms a $\mathcal{C}$-edge in $\mathcal{H}$.

Therefore, having the host tree $T=(X, \mathcal{E})$ for the complete mixed hypertree $\mathcal{H}=$ $(X, \mathcal{C}, \mathcal{D})$, we see that $\mathcal{D}=\mathcal{E}$. As in graphs and hypergraphs, here completeness means that we can't add any additional $\mathcal{C}$ - or $\mathcal{D}$-edges and preserve $\mathcal{H}$ being reduced.

Denote by $M$ the number of $\mathcal{C}$-edges of a complete mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$. Then

$$
M=\sum_{\substack{x \in T \\ d(x) \geq 2}}\binom{d(x)}{2},
$$

where $d(x)$ is the degree of vertex $x$ in the host tree $T$. Examples show that for any $k>1$, one can construct a mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ with $|\mathcal{D}|=n-1, \quad n-2 \leq|\mathcal{C}| \leq M$ and $\bar{\chi}(\mathcal{H})=k$. Therefore, these bounds on $|\mathcal{D}|$ and $|\mathcal{C}|$ are not sufficient for a mixed hypertree to be uniquely colorable.

Theorem 10.7.7 (Niculitsa, Voloshin, 2000) Let $\mathcal{H}=(X, C, \mathcal{D})$ be a reduced uniquely colorable mixed hypertree with the minimum number of $\mathcal{C}$-edges, $T=(X, \mathcal{E})$ be a host tree, $T_{1}$ and $T_{2}$ be touching graphs which are trees. Then there exists a vertex $x \in X$, simultaneously pendant in $T$ and in $T_{1}$ or $T_{2}$, such that $\mathcal{H}-x$, obtained by strong deletion of $x$ from $\mathcal{H}$, is a uc mixed hypertree.

Proof. Let us first suppose that every pendant vertex of the host tree $T$ is not pendant in either $T_{1}$ or $T_{2}$. This means that every such vertex belongs to at least two $\mathcal{C}$-edges. Then, it is possible to start at any such vertex and construct a cyclic invertor (since $T$ is finite). This implies that one $T_{i}$ contains a cycle; i.e., $\mathcal{H}$ is not a uc mixed hypertree with the minimum number of $\mathcal{C}$-edges, a contradiction. Hence, there exists a vertex $x \in X$ which is pendant in $T$ and in, say $T_{1}$. Then $x$ belongs to precisely one $\mathcal{C}$-edge $C=\{x, y, z\}$. Evidently, $\{x, y\},\{y, z\} \in \mathcal{D}$. Consequently, $c(x)=c(z)$ in the unique partition $c$ of $\mathcal{H}$. Strongly delete $x$ from $\mathcal{H}$, thus obtaining $\mathcal{H}-x$. Clearly, $\mathcal{H}-x$ is a mixed hypertree, $|\mathcal{C}(\mathcal{H}-x)|=|\mathcal{C}(\mathcal{H})|-1$. If it is not uc, then it admits at least two strict colorings. In any extension of a proper coloring of $\mathcal{H}-x$ to a proper coloring of $\mathcal{H}$, we always have $c(x)=c(z)$. Therefore both colorings of $\mathcal{H}-x$ induce different strict colorings of the initial mixed hypertree $\mathcal{H}$, a contradiction. $\square$

Definition 10.7.6 A mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is called uc-orderable if there exists an ordering $\boldsymbol{\sigma}=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ of the vertex set $X$ such that every mixed subhypergraph $\mathcal{H}_{i}$, induced by vertices

$$
\left\{x_{1}, x_{2}, \ldots, x_{i}\right\}, i=1,2, \ldots, n
$$

is uniquely colorable.
It is easy to see that if we add vertices in the order $\boldsymbol{\sigma}$ and color them successively, then each time, there is precisely one possibility to color the next vertex. Equivalently, we can decompose $\mathcal{H}$ by elimination of vertices in order inverse to $\sigma$, i.e. $\left(x_{n}, x_{n-1}, \ldots, x_{1}\right)$, and at each step we obtain a uc mixed hypergraph. Notice that not every uc mixed hypergraph is uc-orderable, but any uc-orderable mixed hypergraph is uc.

From Theorem 10.7.7, we conclude that a uc-orderable mixed hypertree $\mathcal{H}$ can be recognized by consecutive elimination of pendant vertices of the $\mathcal{D}$-graph $\mathcal{H}_{\mathcal{D}}$ in a special ordering, by applying the following:

Algorithm 10.7.1 (uc-ordering)

- INPUT: A reduced mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D}), \sigma$ (n-dimensional empty vector).
- OUTPUT: A uc-ordering $\sigma$ of $\mathcal{H}$ or an indication that $\mathcal{H}$ is not uc.
- Idea: Simultaneous decomposition of $\mathcal{H}_{\mathcal{D}}$, spanning trees $T_{1}$ and $T_{2}$ of touching graphs $L_{1}, L_{2}$, respectively, by pendant vertices.

Iterations:

1. If there is a vertex $x \in X$ not belonging to a $\mathcal{C}$-edge of size 3 or a $\mathcal{D}$-edge of size 2, then return NON uc. Otherwise, remove from $\mathcal{C}$ all elements of size $\geq 4$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-250.jpg?height=606&width=1121&top_left_y=205&top_left_x=329)
Figure 10.21. Uniquely colorable mixed hypertree.

2. Color $\mathcal{D}$-graph $\mathcal{H}_{\mathcal{D}}$ with two colors.
3. Construct touching graphs $L_{1}$ and $L_{2}$.
4. If $L_{i}, i=1,2$, is not connected, then return NON uc.
5. For $L_{i}$, construct spanning tree $T_{i}, i=1,2$.
6. $i:=1$.
7. While in $T_{i}$ there exists a vertex $x$ pendant in both $T_{i}$ and $\mathcal{H}_{\mathcal{D}}$, delete it from $T_{i}$ and $\mathcal{H}_{\mathcal{D}}$, and include $x$ in $\sigma$.
8. If at least one of $T_{1}$ and $T_{2}$ is not empty, assign $i:=3-i$ and go to 7; otherwise, return uc, $\sigma=$ uc-ordering.

Remark. All chords of the graph $L_{i}$, with respect to the spanning tree $T_{i}, i=1,2$, correspond to redundant $\mathcal{C}$-edges in $\mathcal{H}$. The trees $T_{1}$ and $T_{2}$ provide the existence of a unique $(x, y)$-invertor for any $x, y \in X$. Theorem 10.7.7 ensures, at any step of the algorithm, the existence of a vertex, say $x$, pendant in both $\mathcal{H}_{\mathcal{D}}$ and one of $T_{1}$ or $T_{2}$. Notice that not every elimination of pendant vertices in $\mathcal{H}_{\mathcal{D}}$ generates a uc-ordering in $\mathcal{H}$.

An example of a uc mixed hypertree $\mathcal{H}$ and respective touching graphs $L_{1}$ and $L_{2}$ is shown in Figure 10.21. Graph $L_{1}$ is a tree, so $T_{1}=L_{1}$. Graph $L_{2}$ is not a tree; it means that $\mathcal{H}$ has a redundant $\mathcal{C}$-edge. Any of three $\mathcal{C}$-edges $\left\{x_{1}, x_{3}, x_{4}\right\},\left\{x_{4}, x_{3}, x_{5}\right\},\left\{x_{2}, x_{3}, x_{5}\right\}$ is redundant. In graph $L_{2}$, choose edge $\left\{x_{2}, x_{5}\right\}$ to be a chord of spanning tree $T_{2}$. At the beginning, vertex $x_{1}$ is pendant in both $\mathcal{H}_{\mathcal{D}}$ and $L_{1}$. After deleting of $x_{1}$, graph $L_{1}$ contains the only vertex $x_{3}$. However, $x_{3}$ is not pendant in $\mathcal{H}_{\mathcal{D}}$. Therefore, Algorithm 10.7.1 switches spanning tree $T_{1}$ to $T_{2}$. Now vertex $x_{2}$ is pendant in both $\mathcal{H}_{\mathcal{D}}$ and $L_{2}$, so it is deleted next, and so on. Thus the algorithm decomposes $\mathcal{H}$ in the ordering $x_{1}, x_{2}, x_{4}, x_{3}$, and $x_{5}$. Hence the uc-ordering is:

$$
\boldsymbol{\sigma}=\left(x_{5}, x_{3}, x_{4}, x_{2}, x_{1}\right) .
$$

From Theorem 10.7.7 and Algorithm 10.7.1 we have
Corollary 10.7.9 A reduced mixed hypertree is uniquely colorable if and only if it is ucorderable.

Therefore, combining Theorems 10.7.3, 10.7.9 and the relation between the chromatic polynomial and chromatic spectrum, we obtain the following:

Corollary 10.7.10 Let $\mathcal{H}=(X, C, \mathcal{D})$ be a reduced mixed hypertree. Then the following five statements are equivalent:

(1) $R(\mathcal{H})=(0,1,0, \ldots, 0)$;
(2) $P(\mathcal{H}, \lambda)=\lambda(\lambda-1)$;
(3) $\mathcal{H}$ is uniquely colorable;
(4) Every two vertices $x, y \in X$ are joined by an $(x, y)$-invertor;
(5) $\mathcal{H}$ is uc-orderable.

Exercises 10.7.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-251.jpg?height=492&width=1170&top_left_y=1129&top_left_x=311)
Figure 10.22.

1. Show that mixed hypergraph $\mathcal{H}_{1}$ in Figure 10.22 is not uc.
2. Embed mixed hypergraph $\mathcal{H}_{1}$ (Figure 10.22) into a uc-mixed hypergraph.
3. For mixed hypergraph $\mathcal{H}_{2}$ in Figure 10.22, find a proper coloring and construct touching graphs for every color.
4. Determine if mixed hypergraphs in Figure 10.22 are mixed hypertrees.
5. Apply Algorithm 10.7.1 to mixed hypergraph $\mathcal{H}_{2}$ in Figure 10.22, to determine if $\mathcal{H}_{2}$ is uniquely colorable. If yes, find a uc-ordering.
6. For mixed hypergraph $\mathcal{H}_{2}$ in Figure 10.22, verify the conditions of Corollary 10.7.10.

Computer Projects 10.7. Write a program for the following algorithmic problems.

1. Given a mixed hypertree $\mathcal{H}$, apply Algorithm 10.7.1 to determine if $\mathcal{H}$ is uniquely colorable.

### 10.8. Perfection

In graph coloring theory, perfect graphs (see Section 5.7.) provide an important theoretic and algorithmic topic of research. In the language of mixed hypergraphs, a $\mathcal{D}$-graph $G$ is called perfect if, for every one of its induced subgraphs $G^{\prime}$ (including $G$ itself), the lower chromatic number equals the size of its largest clique, i.e. $\chi\left(G^{\prime}\right)=\omega\left(G^{\prime}\right)$.

The notion of graph perfection is difficult to extend to general $\mathcal{D}$-hypergraphs because, from the point of view of colorings, there is no natural and simple analogue of complete graphs (cliques). For example, the $\mathcal{D}$-hypergraph $\mathcal{K}_{n}^{r}, r \geq 3$, being a hypergraph generalization of the clique $K_{n}$ and considered as a mixed hypergraph $\mathcal{H}=\left(X, \emptyset,\binom{X}{r}\right)$, has many proper colorings and its properties are not so nice as those of the clique $\mathcal{H}=\left(X, \emptyset,\binom{X}{2}\right)$.

In contrast, we find a natural notion of perfection of an arbitrary mixed hypergraph with respect to the upper chromatic number. Hence, when talking about graph perfection we mean perfection with respect to the lower chromatic number, while talking about hypergraph perfection we mean perfection with respect to the upper chromatic number.

Recall that by definition in a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ a set $S \subseteq X$ is said to be $\mathcal{C}$-stable ( $\mathcal{C}$-independent) if it contains no $\mathcal{C}$-edge $C \in \mathcal{C}$.

Definition 10.8.1 The cardinality of a maximum $\mathcal{C}$-stable set in $\mathcal{H}$ is called the $\mathcal{C}$-stability ( $\mathcal{C}$-independence) number $\alpha_{c}(\mathcal{H})$.

It follows from this definition that a maximum $\mathcal{C}$-stable set is the largest set that could possibly be polychromatic over all proper colorings. One can compare it with the notion of a maximum $\mathcal{D}$-stable set which in turn is the largest set that could possibly be monochromatic over all proper colorings.

Proposition 10.8.1 For every mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$,

$$
\bar{\chi}(\mathcal{H}) \leq \alpha_{c}(\mathcal{H}) .
$$

Proof. Consider a strict $\bar{\chi}$-coloring of $\mathcal{H}$ and choose one vertex from each color class to form a set $S$. Since $S$ is a polychromatic set, it does not contain any $\mathcal{C}$-edge. It means that $S$ is a $\mathcal{C}$-stable set. The cardinality of a maximum $\mathcal{C}$-stable set cannot be smaller; hence the inequality follows. $\square$

Mixed hypergraphs with $\bar{\chi}(\mathcal{H})=\alpha_{c}(\mathcal{H})$ may be constructed easily, and it is now seen that $\alpha_{c}(\mathcal{H})$ plays a role for $\bar{\chi}(\mathcal{H})$ analogous to that played by the maximum clique number $\omega$ for the chromatic number $\chi$ in a classic graph $G$. Namely, it is opposite, in some sense, to the inequality $\chi(G) \geq \omega(G)$, see Section 5.7. The significant difference, however, is that the latter holds only for graphs, i.e. 2-uniform $\mathcal{D}$-hypergraphs, while the inequality (10.4) holds for any mixed hypergraph.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-253.jpg?height=549&width=645&top_left_y=241&top_left_x=567)
Figure 10.23.

We know from Mycielski's construction (Section 5.7.) that there are graphs (even without triangles) such that the difference $\chi(G)-\omega(G)$ is arbitrarily large. Something similar can be stated with respect to the upper chromatic number and the $\mathcal{C}$-stability number, even for $\mathcal{C}$-hypergraphs.

Theorem 10.8.1 For any $k \geq 0$ and $\bar{\chi} \geq k+1$, there exists a 3-uniform $\mathcal{C}$-hypergraph $\mathcal{H}$ such that

$$
\boldsymbol{\alpha}_{c}(\mathcal{H})-\overline{\boldsymbol{\chi}}(\mathcal{H})>k .
$$

Proof. Let $\mathcal{H}=(X, \mathcal{C})$ be a 3-uniform $\mathcal{C}$-hypergraph with $X=\{1,2, \ldots, 2 k+5\}$, and $C_{1}=\{1,2,3\}, C_{2}=\{1,4,5\}, \ldots, C_{k+2}=\{1,2 k+4,2 k+5\}$ such that

$$
C_{i} \cap C_{j}=\{1\}, \quad i, j \in I=\{1,2, \ldots k+2\}, \quad i \neq j .
$$

In other words, $\mathcal{H}$ is a 3-uniform monostar having vertex 1 as the unique center, see Figure 10.23. Vertex 1 represents the minimum transversal, therefore all other vertices form a stable set. Hence $\alpha_{c}(\mathcal{H})=2 k+4$. Further, since no two edges have two vertices in common, in every proper coloring we must repeat one color in each edge. Since the number of edges is $k+2$, the number of colors in any proper coloring is at most $2 k+5-(k+2)=$ $k+3$, i.e. $\bar{\chi}(\mathcal{H})=k+3$. Hence, $\alpha_{c}(\mathcal{H})-\bar{\chi}(\mathcal{H})=2 k+4-(k+3)=k+1>k$. $\square$

Compare Figure 10.23 with Figure 5.23: they both show that the lower and upper chromatic numbers can be arbitrarily far from their respective bounds.

Definition 10.8.2 A colorable mixed hypergraph $\mathcal{H}=(X, C, \mathcal{D})$ is called perfect if for every induced subhypergraph $\mathcal{H}^{\prime}$ (including $\mathcal{H}$ itself) the following equality holds:

$$
\bar{\chi}\left(\mathcal{H}^{\prime}\right)=\alpha_{c}\left(\mathcal{H}^{\prime}\right) .
$$

Example 10.8.1 Every colorable mixed hypergraph $\mathcal{H}=\left(X,\binom{X}{r}, \mathcal{D}\right), r \geq 2$, is perfect. Indeed, $\bar{\chi}\left(\mathcal{H}_{Y}\right)=r-1=\alpha_{c}\left(\mathcal{H}_{Y}\right)$ for each $|Y| \geq r$, and $\bar{\chi}\left(\mathcal{H}_{Y}\right)=|Y|=\alpha_{c}\left(\mathcal{H}_{Y}\right)$ for each $|Y|<r$.

A mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ with $\mathcal{C} \neq \boldsymbol{\emptyset}$ is called a $\mathcal{C}$-bistar if there are two vertices (called the center) common to all $\mathcal{C}$-edges.

Theorem 10.8.2 Every $\mathcal{C}$-bistar $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is a perfect mixed hypergraph.
Proof. Obviously, we can color the center with one color and the remaining vertices with all different colors, so $\bar{\chi}(\mathcal{H})=n-1=\alpha_{\mathcal{C}}(\mathcal{H})$. Consider any $Y \subseteq X$. If $\mathcal{H}_{Y}$ contains at least one $\mathcal{C}$-edge, then $\bar{\chi}\left(\mathcal{H}_{Y}\right)=|Y|-1=\alpha_{\mathcal{C}}\left(\mathcal{H}_{Y}\right)$. Otherwise, $\bar{\chi}\left(\mathcal{H}_{Y}\right)=|Y|=\alpha_{\mathcal{C}}\left(\mathcal{H}_{Y}\right)$. $\square$

Minimal non-perfect mixed hypergraphs. Recall that we denote by $\tau\left(\mathcal{H}_{C}\right)$ the transversal number of $\mathcal{H}_{\mathcal{C}}$, i.e., the cardinality of the smallest subset of vertices that contains at least one vertex from every $\mathcal{C}$-edge of a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$. Let $\tau_{2}\left(\mathcal{H}_{\mathcal{C}}\right)$ denote the bitransversal number of $\mathcal{H}_{C}$ which is the cardinality of the smallest subset of vertices that contains at least two vertices from every $\mathcal{C}$-edge of a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$.

A $\mathcal{C}$-monostar is a mixed hypergraph which has exactly one vertex in common with all of its $\mathcal{C}$-edges. That vertex is called the center. Therefore, if $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is a $\mathcal{C}$ -monostar, then $\tau\left(\mathcal{H}_{\mathcal{C}}\right)=1$, and $\tau_{2}\left(\mathcal{H}_{\mathcal{C}}\right) \geq 3$. However, if $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is a $\mathcal{C}$-bistar, then it has two vertices in common with all the $\mathcal{C}$-edges, what implies $\tau\left(\mathcal{H}_{\mathcal{C}}\right)=1$, and $\tau_{2}\left(\mathcal{H}_{\mathcal{C}}\right)=2$. The classes of $\mathcal{C}$-monostars and $\mathcal{C}$-bistars have an empty intersection.

Theorem 10.8.3 A $\mathcal{C}$-monostar $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is not a perfect mixed hypergraph.
Proof. It follows from the definition of $\mathcal{C}$-monostar that $\alpha_{c}(\mathcal{H})=|X|-1$. Since also by definition $\mathcal{H}$ contains at least two $\mathcal{C}$-edges, in any proper coloring either we have three vertices including the center colored with the same color, or we have one color repeated in one $\mathcal{C}$-edge and another color repeated in another $\mathcal{C}$-edge. In both cases the maximum number of colors is not greater than $|X|-2$. This implies that $\bar{\chi}(\mathcal{H}) \leq|X|-2$, so $\bar{\chi}(\mathcal{H}) \neq$ $\boldsymbol{\alpha}_{c}(\mathcal{H})$. $\square$

Every subhypergraph of a $\mathcal{C}$-monostar $\mathcal{H}$ which itself is a $\mathcal{C}$-monostar (i.e., it contains at least two $\mathcal{C}$-edges of $\mathcal{H}$ ) is not a perfect mixed hypergraph. It means that the minimal not perfect subhypergraph that becomes perfect after strong deletion of a vertex represents just two $\mathcal{C}$-edges sharing precisely one vertex.

Definition 10.8.3 An $r$-uniform $\mathcal{C}$-hypergraph $\mathcal{H}=(X, \mathcal{C}),|X|=n \geq 3, r \geq 2$, is called $a$ cycloid and denoted by $C_{n}^{r}$ if $X=\{0,1, \ldots, n-1\}$ and $\mathcal{C}=\{\{i, i+1(\bmod n), \ldots, i+r-$ $1(\bmod n)\}: i=0,1, \ldots, n-1\}$.

In other words, one can say that for a cycloid there exists a host graph $C_{n}=(X, E)$ representing a simple cycle without chords, such that $\mathcal{C}$ coincides with the family of all paths of length $r-1$ on $C_{n}$. Thus, the usual cycle $C_{n}$ (considered as a $\mathcal{C}$-hypergraph) is $C_{n}^{2}$ for any $n \geq 3$. Note that the example given for Algorithm 10.4.1, see Figure 10.9, is the cycloid $C_{5}^{3}$ considered as the mixed hypergraph $\left(X, C_{5}^{3}, \emptyset\right)$.

Theorem 10.8.4 A cycloid $C_{n}^{r}=(X, \mathcal{C}), 3 \leq r \leq n$, is perfect if and only if $2 r \geq n+2$.

Proof.
Case 1: $2 r \geq n+2$. Since for $r=n$ the theorem is evident, let $r \leq n-1$. Hence, $\left|C_{i} \cap C_{j}\right| \geq 2, i, j \in I$. Let $x_{1}$ be a neighbor of $x_{2}, x_{3}$ be a neighbor of $x_{4}$, and the pair $\left\{x_{1}, x_{2}\right\}$ be opposite to the pair $\left\{x_{3}, x_{4}\right\}$ on the host cycle of $C_{n}^{r}$. The inequality $2 r \geq n+2$ implies that for any $C_{i} \in \mathcal{C}$ either $\left|C_{i} \cap\left\{x_{1}, x_{2}\right\}\right| \geq 2$ or $\left|C_{i} \cap\left\{x_{3}, x_{4}\right\}\right| \geq 2$. Thus, $C_{n}^{r}$ is the union of two $\mathcal{C}$-bistars with disjoint centers. From $r \leq n-1$, we conclude that there are no two vertices belonging to all $\mathcal{C}$-edges, so $\bar{\chi}\left(C_{n}^{r}\right)<n-1$. On the other hand, we can color $x_{1}, x_{2}$ with the first color, $x_{3}, x_{4}$ with the second color and all the remaining $n-4$ vertices with all different colors. Therefore, $\bar{\chi}\left(C_{n}^{r}\right)=n-2$. Since $C_{n}^{r}$ is not a $\mathcal{C}$-monostar, and vertices $x_{1}$ and $x_{3}$ form a minimum transversal, $\tau\left(C_{n}^{r}\right)=2$. It implies $\alpha\left(C_{n}^{r}\right)=n-2=\bar{\chi}\left(C_{n}^{r}\right)$. At last, every induced subhypergraph of $C_{n}^{r}$ is a $\mathcal{C}$-bistar and, by Theorem 10.8.2, is perfect. Hence, $C_{n}^{r}$ is perfect.

Case 2: $2 r=n+1$. Observe that $C_{n}^{r}$ does not contain any $\mathcal{C}$-monostar as an induced subhypergraph. For $r=3,4$, it can be verified directly that $C_{n}^{r}$ is not $\mathcal{C}$-perfect. Hence, let $r \geq 5$. Since $\tau\left(C_{n}^{r}\right)=2$, it follows that $\alpha\left(C_{n}^{r}\right)=n-2$. We show that $\bar{\chi}\left(C_{n}^{r}\right)<n-2$. For a contradiction, assume that $\bar{\chi}\left(C_{n}^{r}\right)=n-2$. Consider a strict coloring using $\bar{\chi}$ colors. There are two possibilities: either one pair of vertices is colored with one color and another pair of vertices is colored with another color and all other $n-4$ vertices colored differently, or, there are three vertices colored with one color and all the remaining $n-3$ vertices colored differently. We consider this as the following two subcases.

Subcase 1: pair $x_{1}, x_{2}$ is colored with one color and pair $x_{3}, x_{4}$ is colored with another color. Then $C_{n}^{r}$ is the union of two $\mathcal{C}$-bistars with centers that do not intersect. Assume that $x_{1}, x_{2} \in X$ represent a center of the first $\mathcal{C}$-bistar, and $x_{3}, x_{4}$ a center of the second $\mathcal{C}$ -bistar, and, moreover, $x_{1}, x_{2}, x_{3}, x_{4}$ are placed on $C_{n}^{r}$ clockwise in this order. Let $n_{i j}$ be the number of vertices between $x_{i}$ and $x_{j}, i, j=1,2,3,4$. If $n_{12}=0$ and $n_{34}=0$, then a $\mathcal{C}$-edge $C \in \mathcal{C}$ may be found easily such that $\left|C \cap\left\{x_{1}, x_{2}\right\}\right| \leq 1$ and $\left|C \cap\left\{x_{3}, x_{4}\right\}\right| \leq 1$; so, assume that $n_{12}+n_{34} \geq 1$. We have $n_{12}+n_{23}+n_{34}+n_{41}+4=n=2 r-1$. Since any $\mathcal{C}$-edge must contain either $\left\{x_{1}, x_{2}\right\}$ or $\left\{x_{3}, x_{4}\right\}$, it follows that

$$
\begin{aligned}
& n_{12}+n_{23}+n_{34}+2<r, \\
& n_{12}+n_{14}+n_{34}+2<r .
\end{aligned}
$$

By summing the above two inequalities, we have $2 r-1+n_{12}+n_{34}<2 r$ which gives the contradiction $r<r$.

If the vertices $x_{1}, x_{2}, x_{3}, x_{4}$ are placed on $C_{n}^{r}$ in any other order, then a $\mathcal{C}$-edge $C \in \mathcal{C}$ may easily be found such that $\left|C \cap\left\{x_{1}, x_{2}\right\}\right| \leq 1$ and $\left|C \cap\left\{x_{3}, x_{4}\right\}\right| \leq 1$. Consequently, $C_{2 r-1}^{r}$ cannot be the union of two $\mathcal{C}$-bistars with disjoint centers for any $r \geq 3$.

Subcase 2: vertices $x_{1}, x_{2}$, and $x_{3}$ are colored with the same color and placed on $C_{n}^{r}$ clockwise in this order. Then $x_{1}, x_{2}, x_{3}$ is a minimum $\mathcal{C}$-bitransversal. Let $n_{i j}$ be the number of vertices between $x_{i}$ and $x_{j}, i, j=1,2,3$. We have $n_{12}+n_{23}+n_{31}+3=n=2 r-1$. Since any $\mathcal{C}$-edge must contain two vertices among $x_{1}, x_{2}$ and $x_{3}$, it follows that

$$
\begin{aligned}
& n_{12}+1+n_{23}<r, \\
& n_{23}+1+n_{31}<r,
\end{aligned}
$$

$$
n_{31}+1+n_{12}<r .
$$

Summing these inequalities implies $r<5$, a contradiction. Consequently, $C_{2 r-1}^{r}$ cannot be colored with $n-2$ colors in such a way that three vertices have the same color and all the other vertices have different colors. This holds for any $r \geq 3$ and Subcase 2 is proved.

Case 3: $2 r \leq n$. In this case, all $\mathcal{C}$-edges containing a fixed vertex form an induced subhypergraph which is a $\mathcal{C}$-monostar, and hence, $C_{n}^{r}$ is not perfect. $\square$

Next we provide a description of one more example of minimal non perfect $\mathcal{C}$ -hypergraph found by Král'. Let $r \geq 3$ be a fixed integer. We define a $\mathcal{C}$-hypergraph $\mathcal{H}^{r}=(X, \mathcal{C})$ in the following way. Let

$$
X=\{1,2,3, \ldots, 2 r\},
$$

and the vertices be drawn in the plane in cyclic clockwise order. The edge family has $2 r+2$ edges,

$$
\mathcal{C}=\left\{C_{1}, C_{2}, \ldots, C_{2 r}, C_{o}, C_{e}\right\}
$$

such that

$$
C_{1}=\{1,2,4,6,8, \ldots, 2 r-2\} .
$$

Thus $C_{1}$ contains consecutive vertices 1 and 2, skips vertex 3 and contains all (except $2 r$ ) even vertices thereafter, $r$ vertices in total. Further, edge $C_{2}$ is obtained when shifting (=rotating) $C_{1}$ by 1 clockwise around the cycle, edge $C_{3}$ is obtained when shifting $C_{2}$ by 1 in the same direction around the cycle, and so on, ..., edge $C_{2 r}$ is obtained when shifting $C_{2 r-1}$ by 1 around the cycle. In other words, edges $C_{2}, C_{3}, \ldots, C_{2 r}$ are all copies of $C_{1}$ obtained by shifting around the cycle. At last, edge $C_{o}$ contains all odd vertices, and edge $C_{e}$ contains all even vertices. Clearly, $\mathcal{H}^{r}$ is an $r$-uniform ( $r+1$ )-regular $\mathcal{C}$-hypergraph on $2 r$ vertices.

For $r=3$ the example is shown in Figure 10.24. To avoid confusion, edges $C_{2}, \ldots, C_{6}$ are not shown, and edges $C_{o}$ and $C_{e}$ are shown separately.

Theorem 10.8.5 (Král', 2003) The $\mathcal{C}$-hypergraph $\mathcal{H}^{r}$ contains no cycloid on $2 r-1$ vertices and no monostar as induced subhypergraphs; moreover

$$
\bar{\chi}\left(\mathcal{H}^{r}\right)=2 r-4<2 r-3=\alpha_{\mathcal{C}}\left(\mathcal{H}^{r}\right) .
$$

Perfection of mixed hypertrees. A hypergraph $\mathcal{H}$ is called bi-Helly if for any subfamily of edges the following implication holds: if every two edges of the subfamily have intersection of cardinality at least two, then the whole subfamily has intersection of cardinality at least two.

A mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is called an eclipse if the intersection of all $\mathcal{C}$ -edges induces a complete $\mathcal{D}$-graph. Evidently, any eclipse has at least one $\mathcal{C}$-edge; if it has exactly one $\mathcal{C}$-edge, then it is uncolorable. Any $\mathcal{C}$-monostar is a special case of an eclipse. Every $\mathcal{C}$-bistar where each center is a $\mathcal{D}$-edge of size 2 is an eclipse. An example of a $\mathcal{C}$-bistar and an eclipse which is obtained from that $\mathcal{C}$-bistar is shown in Figure 10.25.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-257.jpg?height=640&width=1098&top_left_y=233&top_left_x=321)
Figure 10.24. Král's construction.

Theorem 10.8.6 Every eclipse $\mathcal{H}$ is not a perfect mixed hypergraph.
Proof. Indeed, since the intersection of all $\mathcal{C}$-edges is not empty, $\tau\left(\mathcal{H}_{\mathcal{C}}\right)=1$, hence $\alpha\left(\mathcal{H}_{\mathcal{C}}\right)=n-1$. If $\mathcal{H}$ contains only one $\mathcal{C}$-edge, then it is uncolorable and $\bar{\chi}(\mathcal{H})=$ 0 . If $\mathcal{H}$ has more than one $\mathcal{C}$-edges, then, in any proper coloring, the intersection of all $\mathcal{C}$-edges must be polychromatic. This implies that no two $\mathcal{C}$-edges may repeat the same color, therefore no coloring with $n-1$ colors exist. In all cases $\bar{\chi}(\mathcal{H}) \neq$ $n-1$. $\square$

Clearly, if an eclipse is a hypertree, or any subhypergraph of a hypertree, then it is either a $\mathcal{C}$-monostar or a $\mathcal{C}$-bistar having $\mathcal{D}$-graph $K_{2}$ as the unique center.

Theorem 10.8.7 If a mixed hypertree $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ contains no eclipse then it is perfect.
Proof. Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be a colorable mixed hypertree without eclipses. Since every induced subhypergraph of a mixed hypertree is also a mixed hypertree, it is sufficient to show that we can color $\mathcal{H}$ with $\alpha_{C}(\mathcal{H})$ colors.

By Theorem 8.1.2 the hypertree $\mathcal{H}_{\mathcal{C}}=(X, \mathcal{C}, \emptyset)$ satisfies the Helly property; i.e., for any subfamily $\mathcal{C}_{1} \subseteq \mathcal{C}$ with $C \cap C^{\prime} \neq \emptyset$ for each pair $C, C^{\prime} \in \mathcal{C}_{1}$, it follows that

$$
\bigcap_{C \in \mathcal{C}_{1}} C \neq \emptyset .
$$

In fact, for every such subfamily $\left|\bigcap_{C \in \mathcal{C}_{1}}\right| \geq 2$ because otherwise $\mathcal{C}_{1}$ forms an eclipse. Thus $\mathcal{H}_{C}$ is a bi-Helly hypergraph, and moreover, $C \cap C^{\prime} \neq \emptyset$ implies $\left|C \cap C^{\prime}\right| \geq 2$ for any $C, C^{\prime} \in C$.

Consider the problem of finding a minimum transversal of $\mathcal{H}_{C}$. For this, construct the line graph of $\mathcal{H}_{C}$, that is the graph $L\left(\mathcal{H}_{C}\right)=(\mathcal{C}, \mathcal{E})$, where $\left(C, C^{\prime}\right) \in \mathcal{E} \Leftrightarrow C \cap C^{\prime} \neq \emptyset$ in $\mathcal{H}$. Because of the Helly property, minimum covering of $L$ by cliques corresponds to a minimum transversal of $\mathcal{H}_{C}$. Let $K_{1}, K_{2}, \ldots, K_{t}$ be the cliques of such a minimum covering of $L$. Thus $\tau\left(\mathcal{H}_{\mathcal{C}}\right)=t$ and $\alpha_{\mathcal{C}}(\mathcal{H})=|X|-t$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-258.jpg?height=557&width=1175&top_left_y=267&top_left_x=295)
Figure 10.25. $\mathcal{C}$-bistar and eclipse.

Because of the bi-Helly property, every clique of the graph $L$ forms a $\mathcal{C}$-bistar as a partial subhypergraph in $\mathcal{H}$ with at least one center ( $\mathcal{C}$-bitransversal). Since by the condition of the theorem $\mathcal{H}$ contains no eclipses, every such $\mathcal{C}$-bistar has at least one center that is not a $\mathcal{D}$-edge.

Let the pair $\left\{x_{i}, y_{i}\right\}$ be the $\mathcal{C}$-bitransversal corresponding to the clique $K_{i}, i=1,2, \ldots, t$ such that $\left\{x_{i}, y_{i}\right\} \notin \mathcal{D}$. They all are different because $K_{i} \neq K_{j}$ implies that $\left\{x_{i}, y_{i}\right\} \cap\left\{x_{j}, y_{j}\right\}=$ $\emptyset$. Color the vertices $x_{1}, y_{1}$ with the first color, $x_{2}, y_{2}$ with the second color, $\ldots, x_{t}, y_{t}$ with the $t$ th color; after that, color all the remaining vertices each with a different color from $t+1, t+2, \ldots,|X|-t$. Thus, we obtain a proper coloring of $\mathcal{H}$ with $|X|-t=\alpha_{C}(\mathcal{H})$ colors, and the theorem follows. $\square$

Corollary 10.8.1 If $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ is a perfect mixed hypertree, $\mathrm{v}\left(\mathcal{H}_{C}\right)$ and $\tau\left(\mathcal{H}_{C}\right)$ are the maximum cardinality of a matching and the minimum cardinality of a transversal of $\mathcal{H}_{C}$ respectively, then

$$
\bar{\chi}(\mathcal{H})=\alpha_{C}(\mathcal{H})=|X|-\tau\left(\mathcal{H}_{C}\right)=|X|-\nu\left(\mathcal{H}_{C}\right) .
$$

Proof. Since $\mathcal{H}_{C}$ is also a hypertree, it fulfills the well known König property, see Theorem 8.2.3, saying that

$$
\nu\left(\mathcal{H}_{C}\right)=\tau\left(\mathcal{H}_{C}\right) .
$$

Hence, the assertion follows. $\square$

Remark. The presence or absence of monostars in $\mathcal{C}$-hypergraphs does not determine perfection directly. Consider, for example, the $\mathcal{C}$-hypergraph $\mathcal{H}=(X, \mathcal{C})$ where $X=\{1,2,3,4,5\}, C=\left\{C_{1}, C_{2}, C_{3}\right\}, C_{1}=\{1,2,3\}, C_{2}=\{2,3,4,5\}, C_{3}=\{1,4,5\}$. We see that $C_{1} \cap C_{3}=\{1\}$ and we have a monostar as a partial subhypergraph. However, $\mathcal{H}$ is perfect with $\bar{\chi}(\mathcal{H})=\alpha_{C}(\mathcal{H})=3$. On the other hand, the cycloid $C_{5}^{3}$ contains monostars as
partial subhypergraphs, does not contain them as induced subhypergraphs and, at the same time, is not perfect (Theorem 10.8.4).

We end the section with explicit description of six known examples of minimal non perfect 3-uniform $\mathcal{C}$-hypergraphs:

$$
\begin{aligned}
& V_{1}=(\{1,2,3,4\},\{\{1,2,3\},\{1,3,4\},\{1,2,4\}\}) \text { (monostar); } \\
& V_{2}=(\{1,2,3,4,5\},\{\{1,2,3\},\{1,4,5\}\}) \text { (monostar); } \\
& V_{3}=(\{1,2,3,4,5\},\{\{1,2,3\},\{1,3,4\},\{1,4,5\}\}) \text { (monostar); } \\
& V_{4}=(\{1,2,3,4,5\},\{\{1,2,3\},\{1,3,4\},\{1,4,5\},\{1,2,5\}\}) \text { (monostar); } \\
& \left.V_{5}=(\{1,2,3,4,5\},\{\{1,2,3\},\{2,3,4\},\{3,4,5\},\{4,5,1\},\{5,1,2\}\}) \text { (cycloid } C_{5}^{3}\right) ; \\
& K_{1}=(\{1,2,3,4,5,6\},\{\{1,2,4\},\{2,3,5\},\{3,4,6\}, \quad\{4,5,1\}, \quad\{5,6, \quad 2\}, \quad\{6,1,3\}, \\
& 3,5\},\{2,4,6\}\}) \text { (Král's example). }
\end{aligned}
$$

As one can see, the perfection of hypergraphs is much more complex than the perfection of graphs discussed in Section 5.7.

## Exercises 10.8.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-259.jpg?height=484&width=1139&top_left_y=986&top_left_x=295)
Figure 10.26.

1. For each of mixed hypergraphs $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ in Figure 10.26, find $\mathcal{C}$-stability number $\alpha_{C}(\mathcal{H})$ and upper chromatic number $\bar{\chi}(\mathcal{H})$. Verify inequality (10.4).
2. Which of the mixed hypergraphs $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ in Figure 10.26 is perfect and which is not, and why?
3. For each of mixed hypergraphs $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ in Figure 10.26, find bi-transversal number $\tau_{2}\left(\mathcal{H}_{1}\right)$ and $\tau_{2}\left(\mathcal{H}_{2}\right)$.

Computer Projects 10.8. Write a program for the following algorithmic problems.

1. Given a $\mathcal{C}$-hypergraph $\mathcal{H}$, recognize if $\mathcal{H}$ is a monostar, a cycloid, or the Král's hypergraph.
2. Given a mixed hypergraph $\mathcal{H}$, recognize if $\mathcal{H}$ is a $\mathcal{C}$-bistar, or an eclipse.
3. Given a mixed hypergraph $\mathcal{H}$, find all monostars.

### 10.9. Chromatic Spectrum

Every strict $i$-coloring of a mixed hypergraph $\mathcal{H}$ induces a feasible partition of the vertex set into $i$ nonempty color classes. By definition, the numbers of all feasible partitions into $i$ color classes, $1 \leq i \leq n$, form the chromatic spectrum. The positive components of the chromatic spectrum begin with the number of feasible partitions into the lower chromatic number of classes and end with the number of feasible partitions into the upper chromatic number of classes. It is easy to see that for any $\mathcal{C}$-hypergraph or for any $\mathcal{D}$-hypergraph this segment of the chromatic spectrum contains no gaps, i.e. no zeroes between positive numbers. However, the chromatic spectra of mixed hypergraphs may have gaps. This means that if we know the lower and upper chromatic numbers, we don't know if there are colorings using any intermediate number of colors. In a more formal language these properties are explained as follows.

The set of values $k$ such that $\mathcal{H}$ has a strict $k$-coloring is called the feasible set of $\mathcal{H}$, denoted by $S(\mathcal{H})$. In other words, $S(\mathcal{H})$ is the set of indices $k$ such that $r_{k}(\mathcal{H})>0$.

Definition 10.9.1 A mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ has a gap at $k$ if $S(\mathcal{H})$ contains elements larger and smaller than $k$, but omits $k$. The chromatic spectrum $R(\mathcal{H})$ is called continuous (gap-free) if $S(\mathcal{H})$ has no gaps. Otherwise, it is called broken.

Proposition 10.9.1 For any mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$, both $\mathcal{H}_{\mathcal{C}}=(X, \mathcal{C})$ and $\mathcal{H}_{\mathcal{D}}=(X, \mathcal{D})$ have continuous chromatic spectra.

Proof. Indeed, for $\mathcal{H}_{\mathcal{C}}$, start with any strict $\bar{\chi}$-coloring and sequentially as long as possible unite any two color classes; we end when there is only one color class. Since at each step a proper coloring is obtained, the chromatic spectrum of $\mathcal{H}_{C}$ is gap-free.

For $\mathcal{H}_{\mathcal{D}}$, start with any strict $\chi$-coloring and sequentially as long as possible split any color class having at least two vertices; we end when there are $|X|$ color classes of cardinality 1 each. At every step a proper coloring is obtained, hence the chromatic spectrum of $\mathcal{H}_{\mathcal{D}}$ is continuous. $\square$

Notice that the last part of the statement above is a direct generalization of Theorem 5.2.1 about the chromatic spectrum of graphs.

The simplest example. One of the simplest ways to construct a mixed hypergraph with a gap in the chromatic spectrum is the following. First, define an operation called the "inflation" of a $\mathcal{D}$-edge. Let us have a $\mathcal{D}$-edge $\{a, b\}$, see Figure 10.27. We double the vertices, i.e. replace vertices $a, b$ with the pairs $a, a^{\prime}$ and $b, b^{\prime}$ respectively. Thus, $\mathcal{D}$-edge $\{a, b\}$ becomes a quadruple, i.e. $\mathcal{D}$-edge $\left\{a, a^{\prime}, b, b^{\prime}\right\}$.

Next, we add all triples on vertices $a, a^{\prime}, b, b^{\prime}$ as $\mathcal{C}$-edges. If $\mathcal{H}$ denotes the mixed hypergraph obtained, then simply $\mathcal{H}=\left(X, K_{4}^{3}, K_{4}^{4}\right)$ where $X=\left\{a, a^{\prime}, b, b^{\prime}\right\}$. The inflation consists in the replacing of $\mathcal{D}$-edge $\{a, b\}$ by $\mathcal{H}$. One can easily see that

$$
R(\mathcal{H})=(0,7,0,0)
$$

and all seven feasible partitions are induced by the following seven strict 2-colorings (in order $a, a^{\prime}, b, b^{\prime}$ ):
1122,1112,1121,1222,2122,1212,1221.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-261.jpg?height=834&width=1059&top_left_y=220&top_left_x=324)
Figure 10.27. Inflation of edge $\{a, b\}$.

Observe that among all seven colorings there is only one coloring, namely, the first one, when vertex $a$ has the same color as $a^{\prime}$ (color 1), and vertex $b$ has the same color as $b^{\prime}$ (color 2). This fact is the key to the gap in the chromatic spectrum.

The final step in constructing the example is the following: take a complete $\mathcal{D}$-graph $K_{4}$ on vertices $a, b, c, d$ and by doubling the vertices inflate all of its six $\mathcal{D}$-edges, see Figure 10.28. To avoid any confusion, the $\mathcal{C}$-edges are not shown. Denote the mixed hypergraph obtained by $\mathcal{H}$.

Consider now the proper colorings of $\mathcal{H}$. It has four pairs of vertices, namely, $\left\{a, a^{\prime}\right\}$, $\left\{b, b^{\prime}\right\},\left\{c, c^{\prime}\right\}$, and $\left\{d, d^{\prime}\right\}$. In any proper coloring of $\mathcal{H}$, if there is a pair, say $\left\{a, a^{\prime}\right\}$, colored with different colors, say, 1 and 2, then each of the remaining vertices is colored with one of the colors 1 or 2. This occurs because any new color, say 3, at any of the vertices, say $c$, immediately results in a polychromatic triple $\left\{a, a^{\prime}, c\right\}$ which is a $\mathcal{C}$-edge. So, it remains to consider the proper colorings when each pair is monochromatic. Surprisingly, there is only one coloring of such type (if we do not count the permutations of colors):
11223344.

Indeed, no two pairs of vertices may have the same color because each "pair of pairs" is a $\mathcal{D}$-edge, see Figure 10.28. The fundamental conclusion at this point is that $\mathcal{H}$ has several strict 2-colorings ( $r_{2} \geq 2$ ), a strict 4-coloring ( $r_{4}=1$ ) and no strict 3-coloring ( $r_{3}=0$ ), i.e. there is a gap in the chromatic spectrum. Since by the reasoning above there are no strict 5-,6-,7- and 8-colorings, the chromatic spectrum has then the following form:

$$
R(\mathcal{H})=\left(0, r_{2}, 0,1,0,0,0,0\right) .
$$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-262.jpg?height=844&width=1041&top_left_y=230&top_left_x=316)
Figure 10.28. Inflation of $K_{4}$.

The mixed hypergraph $\mathcal{H}$ is not the minimal one. One can observe that the gap may be obtained by starting with the same $\mathcal{D}$-graph $K_{4}$ and doubling only vertices $c$ and $d$ (i.e. inflating $\mathcal{D}$-edge $\{c, d\}$ ) and adding triples $\left\{a, c, c^{\prime}\right\},\left\{a, d, d^{\prime}\right\},\left\{b, c, c^{\prime}\right\},\left\{b, d, d^{\prime}\right\}$ as $\mathcal{C}$ edges. Thus these triples become bi-edges. In addition, recall that in $\mathcal{C}$-hypergraph $K_{4}^{3}$ any edge is redundant, see Figure 10.12; it means that one $\mathcal{C}$-edge can be removed from the inflation of edge $\{c, d\}$, and we still have the gap. Later on this smallest example will be denoted by $\mathcal{H}_{2,4}$ where index means $S(\mathcal{H})=\{2,4\}$.

Developing this idea further, the construction of minimal examples of mixed hypergraphs with the gaps in their chromatic spectrum in a more general setting is considered next.

The smallest mixed hypergraphs with gaps. Let $s, t$ be two integer numbers such that $2 \leq s \leq t-2$. In this subsection we construct a mixed hypergraph $\mathcal{H}_{s, t}$ with feasible set $S\left(\mathcal{H}_{s, t}\right)=\{s, t\}$ and prove that $\mathcal{H}_{s, t}$ has the fewest vertices among all $s$-colorable mixed hypergraphs with a gap at $t-1$; this minimum number of vertices is $2 t-s$.

We begin with an explicit construction of a mixed hypergraph with $2 t-2$ vertices and feasible set $\{2, t\}$. As usual, $K_{n}$ is viewed as the mixed hypergraph $\left(X, \emptyset,\binom{X}{2}\right)$; trivially, $S\left(K_{n}\right)=\{n\}$. First, we describe the construction informally. Beginning with $K_{t}$, expand $t-$ 2 of the vertices into pairs, leaving two special vertices unexpanded. The $\mathcal{D}$-edge consisting of the two special vertices remains, and the other $\mathcal{D}$-edges expand into $\mathcal{D}$-edges of size 3 or 4 (special vertex plus pair, or union of two pairs). Add, as $\mathcal{C}$-edges, all triples consisting of three vertices arising from two original vertices (special vertex plus pair, or three vertices from two pairs).

This describes the construction completely, but we present it more formally to facilitate the proofs. The smallest instance is for $t=4$; from $K_{4}$, a 6-vertex mixed hypergraph with spectrum $\{2,4\}$ is produced. Let $[m]=\{1, \ldots, m\}$.

Construction 1. Define a hypergraph $\mathcal{H}_{2, t}$ with vertex set

$$
\left\{x_{1}, x_{2}, a_{1}, \ldots, a_{t-2}, b_{1}, \ldots, b_{t-2}\right\} .
$$

Let $T$ be the set of triples of the form $x_{r} a_{i} b_{i}$, for $r \in\{1,2\}$ and $i \in[t-2]$. Let $U$ be the set of quadruples of the form $a_{i} b_{i} a_{j} b_{j}$ for $i, j \in[t-2]$. Let $W$ be the union, over $i, j \in[t-2]$, of the sets of four triples contained in $\left\{a_{i}, b_{i}, a_{j}, b_{j}\right\}$. The $\mathcal{C}$-edges in $\mathcal{H}_{2, t}$ are $T \cup W$. The $\mathcal{D}$-edges are $T \cup U \cup\left\{x_{1} x_{2}\right\}$.

Lemma 10.9.1 $S\left(\mathcal{H}_{2, t}\right)=\{2, t\}$.
Proof. Let $c$ be an arbitrary coloring of $\mathcal{H}_{2, t}$. If $c\left(a_{i}\right) \neq c\left(b_{i}\right)$ for some $i \in[t-2]$, then the $\mathcal{C}$-edges in $T$ and $W$ that contain $a_{i}$ and $b_{i}$ force all other vertices to have the same color as $a_{i}$ or $b_{i}$. Thus, in this case there are at most two colors. The existence of $\mathcal{D}$-edges prevents a proper 1-coloring, and setting all $c\left(a_{i}\right)=c\left(x_{1}\right)=1$ and $c\left(b_{i}\right)=c\left(x_{2}\right)=2$ completes a proper 2-coloring.

Hence, we may assume that $c\left(a_{i}\right)=c\left(b_{i}\right)$ for all $i \in[t-2]$. Now the $\mathcal{D}$-edges in $U$ force these colors to be distinct for all $i$, and the $\mathcal{D}$-edges in $T$ along with $\left\{x_{1} x_{2}\right\}$ require additional colors for $x_{1}$ and $x_{2}$. This completely forces the coloring, which uses $t$ colors and is proper. $\square$

In order to extend this construction to the lower chromatic number $s$, we use a simple lemma about combining feasible sets. The join of two mixed hypergraphs $\left(X_{1}, \mathcal{C}_{1}, \mathcal{D}_{1}\right)$ and $\left(X_{2}, \mathcal{C}_{2}, \mathcal{D}_{2}\right)$ with disjoint vertex sets is the mixed hypergraph $(X, C, \mathcal{D})$ defined by $X=X_{1} \cup X_{2}, \mathcal{C}=\mathcal{C}_{1} \cup \mathcal{C}_{2}$, and $\mathcal{D}=\mathcal{D}_{1} \cup \mathcal{D}_{2} \cup R$, where $R$ is the set of all pairs consisting of one vertex from $X_{1}$ and one from $X_{2}$.

Lemma 10.9.2 If $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ are mixed hypergraphs, then the feasible set of the join of $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ is $\left\{i+j: i \in S\left(\mathcal{H}_{1}\right), j \in S\left(\mathcal{H}_{2}\right)\right\}$.

Proof. The $\mathcal{D}$-edges added between the vertex sets of $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ prohibit colors from appearing in both sets. Thus, every proper coloring of the join consists of proper colorings of $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ using disjoint sets of colors. $\square$

Call the join $\mathcal{H}^{\prime}$ of an arbitrary mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ with one new vertex $z \notin X$ an elementary shifting of the chromatic spectrum of $\mathcal{H}$. Evidently, elementary shifting results in the chromatic spectrum being shifted to the right by one position for all positive components and adding one zero in the very left position. That is, if $R(\mathcal{H})=$ $\left(r_{1}, r_{2}, \ldots, r_{n}\right)$, then $R\left(\mathcal{H}^{\prime}\right)=\left(0, r_{1}, r_{2}, \ldots, r_{n}\right)$. Joining with the complete graph $K_{i}$ results in $i$ elementary shiftings.

Theorem 10.9.1 If $\mathcal{H}$ is an $s$-colorable mixed hypergraph with a gap at $t-1$, then $n \geq$ $2 t-s$, and this is sharp.

Proof. Consider a proper coloring of $\mathcal{H}$ using $k$ colors, where $k$ is the smallest element of the feasible set larger than $t-1$. If $n<2 t-s$, then using at least $t$ colors requires having at least $s+1$ color classes of size 1 . Two such color classes can be combined to obtain a proper coloring using $k-1$ colors unless they form a $\mathcal{D}$-edge of size 2 . Since $k-1$ is not in the feasible set, $\mathcal{H}$ contains $K_{s+1}$. Now $\mathcal{H}$ is not $s$-colorable; the contradiction yields $n \geq 2 t-s$.

For $s=2$, Lemma 10.9.1 shows that Construction 10.9. achieves the bound. For $s>2$, define $\mathcal{H}_{s, t}$ to be the join of $K_{s-2}$ and $\mathcal{H}_{2, t-s+2}$. By Lemma 10.9.2, the feasible set of $\mathcal{H}_{s, t}$ is $\{s-2\}+\{2, t-s+2\}=\{s, t\}$. The number of vertices in $\mathcal{H}_{s, t}$ is $s-2+2(t-s+2)-2=$ $2 t-s$. $\square$

Corollary 10.9.1 The minimum number of vertices in a mixed hypergraph with a gap in its feasible set is 6, achieved by $\mathcal{H}_{2,4}$.

Proof. Every mixed hypergraph with a gap in its feasible set is s-colorable with a gap at $t-1$, for some $s, t$ with $t-1>s \geq 2$ (notice that $s \geq 2$, otherwise there are no gaps). Thus $t \geq 4$ and $t-s \geq 2$. By Theorem 10.9.1, $n \geq t+(t-s) \geq 6$. $\square$

As we mentioned earlier, closer analysis allows one $\mathcal{C}$-edge in the 6-vertex example to be dropped without changing the spectrum. Thus, $7 \mathcal{C}$-edges and $6 \mathcal{D}$-edges suffice. The mixed hypergraph $\mathcal{H}_{2,4}$ has the following structure: $X=\{1,2,3,4,5,6\}, C=\{\{1,2,3\}$, $\{1,4,5\},\{6,2,3\},\{6,4,5\},\{2,3,4\},\{3,4,5\},\{2,4,5\}\}, \mathcal{D}=\{\{1,6\},\{1,2,3\},\{1,4,5\}$, \{6,2,3\}, \{6,4,5\}, \{2,3, 4,5\}\}. Subsets \{1,2,3\}, \{1,4,5\},\{6,2,3\}, \{6,4,5\} are the biedges. In Figure 10.29, the bi-edges are drawn by doubled curves. One can easily check that the four strict 2-colorings in order of vertices 1,2,3,4,5,6 are 112122, 112212, 212121, 212211, the unique strict 4-coloring is 122334, hence the chromatic spectrum

$$
R\left(\mathcal{H}_{2,4}\right)=(0,4,0,1,0,0),
$$

and the chromatic polynomial

$$
P(\mathcal{H}, \lambda)=\lambda(\lambda-1)\left(\lambda^{2}-5 \lambda+10\right) .
$$

$\mathcal{H}_{2,4}$ is the minimal mixed hypergraph with a gap in the following sense: any deletion of a vertex or an edge of any type eliminates the gap. As Corollary 10.9.1 states, there are no gaps if a mixed hypergraph has less than six vertices. However, we will see that even $\mathcal{H}_{2,4}$ is not the smallest one if the total number of edges is considered.

Feasible sets and doubling-shifting algorithm. The gaps in the chromatic spectrum raise the question regarding which sets of positive integers are feasible sets of mixed hypergraphs. In this subsection we characterize all feasible sets and suggest a conceptual algorithm for constructing a mixed hypergraph realizing a given feasible set.

The $n$-vertex trivial mixed hypergraph ( $X, \emptyset, \emptyset$ ) has, evidently, feasible set $\{1, \ldots, n\}$. We construct mixed hypergraphs realizing all other feasible sets using the trivial mixed hypergraphs, the join operation of Lemma 10.9.2, and one additional operation. This operation is similar to the construction of $\mathcal{H}_{2, t}$ from $K_{t}$. In Construction 10.9., expanding two of the vertices was avoided in order to create few vertices. Here the construction is huge, so we prefer the simplicity gained by expanding all vertices into pairs.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-265.jpg?height=818&width=1111&top_left_y=210&top_left_x=334)
Figure 10.29. The minimal mixed hypergraph with a gap $\mathcal{H}_{2,4}$.

Construction 2. Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be a mixed hypergraph. We construct a mixed hypergraph $\mathcal{H}^{\prime}=\left(X^{\prime}, \mathcal{C}^{\prime}, \mathcal{D}^{\prime}\right)$ with $X^{\prime}=\bigcup_{v \in X}\left\{v^{-}, v^{+}\right\}$. For each edge $D \in \mathcal{D}$, we add $D^{\prime}=\bigcup_{v \in D}\left\{v^{-}, v^{+}\right\}$to $\mathcal{D}^{\prime}$. For each edge $C \in \mathcal{C}$, we add $C^{\prime}=\left\{v^{-}: v \in C\right\}$ to $\mathcal{C}^{\prime}$. Finally, for each ordered pair $u, v \in X$, we add the triples $\left\{v^{-}, v^{+}, u^{-}\right\}$and $\left\{v^{-}, v^{+}, u^{+}\right\}$to $\mathcal{C}^{\prime}$.

The application of Construction 2 may be called doubling. It has the effect of appending element 2 to the feasible set. This is what Construction 1 did to $K_{t}$, and the analysis here generalizes Lemma 10.9.1.

Lemma 10.9.3 Let $\mathcal{H}$ be a mixed hypergraph with feasible set $S$. If $\chi(\mathcal{H}) \geq 2$, then the mixed hypergraph $\mathcal{H}^{\prime}$ obtained from $\mathcal{H}$ via Construction 2 has feasible set $S \cup\{2\}$.

Proof. Let $c$ be a proper coloring of $\mathcal{H}^{\prime}$. If $c\left(v^{-}\right) \neq c\left(v^{+}\right)$for a vertex $v$ of $\mathcal{H}$, then the $\mathcal{C}$-edges that are triples containing $v^{-}, v^{+}$force all other vertices to have color $c\left(v^{-}\right)$or $c\left(v^{+}\right)$. Thus, such a coloring uses exactly two colors. We obtain a strict 2-coloring by setting $c\left(u^{-}\right)=c\left(v^{-}\right)$and $c\left(u^{+}\right)=c\left(v^{+}\right)$for all $u$. Since each member of $\mathcal{D}^{\prime}$ consists of full pairs, the constraints on $\mathcal{D}$-edges are satisfied. Also, each member of $\mathcal{C}^{\prime}$ contains two vertices with superscripts of the same type.

It remains to consider proper colorings with $c\left(v^{-}\right)=c\left(v^{+}\right)$for each vertex $v$ of $\mathcal{H}$. Let $\tilde{c}$ be the coloring of $\mathcal{H}$ defined by $\tilde{c}(v)=c\left(v^{-}\right)$. For each member of $\mathcal{D}^{\prime}$, the coloring constraint is satisfied by $c$ if and only if $\tilde{c}$ satisfies the constraint for the corresponding member of $\mathcal{D}$. The same statement holds for members of $\mathcal{C}^{\prime}$ that arise from members of $\mathcal{C}$. By construction, the new triples in $\mathcal{C}^{\prime}$ are automatically satisfied. Thus, $c$ is a proper coloring of $\mathcal{H}^{\prime}$ if and only if $\tilde{c}$ is a proper coloring of $\mathcal{H}$. Note that $\tilde{c}$ uses the same number of colors as $c$.

Similarly, we can extend each proper coloring of $\mathcal{H}$ to a proper coloring of $\mathcal{H}^{\prime}$ using the same number of colors, by copying the color of each vertex onto both of its copies. This implies that every integer greater than 2 is feasible for $\mathcal{H}$ if and only if it is feasible for $\mathcal{H}^{\prime}$. $\square$

Corollary 10.9.2 Let $\mathcal{H}$ and $\mathcal{H}^{\prime}$ be as above, and

$$
R(\mathcal{H})=\left(0, \ldots, 0, r_{\chi}, \ldots, r_{\bar{\chi}}, 0, \ldots, 0\right) .
$$

Then

$$
R\left(\mathcal{H}^{\prime}\right)=\left(0, r_{2}\left(\mathcal{H}^{\prime}\right), 0 \ldots, 0, r_{\chi}, \ldots, r_{\bar{\chi}}, 0, \ldots, 0\right) .
$$

Proof. Indeed, the proof of Lemma 10.9.3 establishes a bijection between strict colorings of $\mathcal{H}$ with at least three colors and strict colorings of $\mathcal{H}^{\prime}$ with at least three colors. The number of 0s on the right part of the chromatic spectrum of $R\left(\mathcal{H}^{\prime}\right)$ is greater by $n(\mathcal{H})$ since $n\left(\mathcal{H}^{\prime}\right)=2 n(\mathcal{H})$. $\square$

Using shiftings (joins with cliques) and doublings, one can produce all feasible sets.
Theorem 10.9.2 (Jiang et al., 2002) A finite set of positive integers is the feasible set for a mixed hypergraph if and only if it omits the number 1 or is an interval containing 1.

Proof. It remains only to consider the sets not containing 1 . We produce a mixed hypergraph $\mathcal{H}(T)$ with feasible set $T$. We use induction on the size of set $T$, and within each size, we use induction on the smallest element $t$ of $T$. For $T=\{t\}$, we set $\mathcal{H}(T)=K_{t}$.

For $|T|>1$ and $t=2$, we let $\mathcal{H}(T)$ be the mixed hypergraph obtained by applying Construction 2 to $\mathcal{H}(T-\{2\})$. Lemma 10.9.3 implies that this works.

For $|T|>1$ and $t>2$, we let $\mathcal{H}(T)$ be the join of $K_{t-2}$ with the mixed hypergraph $\mathcal{H}\left(T^{\prime}\right)$, where $T^{\prime}$ is obtained from $T$ by subtracting $t-2$ from each element. Lemma 10.9.2 implies that this works. $\square$

Next we present a conceptual algorithm which, for an arbitrary increasing sequence of integer numbers, constructs a mixed hypergraph having the respective feasible set.

Algorithm 10.9.1 (doubling-shifting algorithm)
INPUT: A set $S=\left\{n_{1}, n_{2}, \ldots, n_{p}\right\}$ of increasing integer numbers, $n_{1} \geq 2$.
OUTPUT: A mixed hypergraph $\mathcal{H}$ with the feasible set $S$.
Initialization: $i=n_{p}-1 ; \mathcal{H}=K_{3}$.
Iteration: while $i \neq 1$, do:

1. If $i \in S$, do doubling.
2. If $i \notin S$, do elementary shifting.
3. $i=i-1$.

End.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-267.jpg?height=702&width=1152&top_left_y=207&top_left_x=303)
Figure 10.30. The smallest 3-uniform bihypergraph with a gap.

Uniform bihypergraphs. All examples discussed so far represented mixed hypergraphs with $\mathcal{C}$-edges and $\mathcal{D}$-edges of different sizes, i.e. not uniform. As next theorem shows the uniform bihypergraphs may also have gaps in their chromatic spectra.

Theorem 10.9.3 (L. Gionfriddo, Voloshin, 2002) The minimum number of vertices over all 3-uniform bihypergraphs with a gap in the chromatic spectrum is 7; the minimum number of edges over all 3-uniform bihypergraphs on 7 vertices with a gap in the chromatic spectrum is 9.

Proof. We first prove that there is no 3-uniform bihypergraph on 6 vertices with a broken chromatic spectrum.

Let $\mathcal{H}=(X, \mathcal{E})$ be a colorable 3-uniform bihypergraph with $X=\{1,2, \ldots, 6\}$, with all the elements of $\mathcal{E}$ being triples (bi-edges of size 3), and $R(\mathcal{H})=\left(r_{1}, r_{2}, \ldots, r_{6}\right)$. For a contradiction, suppose that $R(\mathcal{H})$ is broken.

Evidently, $r_{1}=0, r_{6}=0$. If $r_{5} \neq 0$, then in a strict 5-coloring of $\mathcal{H}$, all bi-edges contain a fixed monochromatic pair of vertices, say 1,2 , and all the other color classes are singletons. These color classes can easily be combined, so $r_{4} \neq 0, r_{3} \neq 0, r_{2} \neq 0$, a contradiction. Hence $r_{5}=0$. If $r_{4} \neq 0$, then in a strict 4-coloring of $\mathcal{H}$, there are at least two singleton color classes which implies $r_{3} \neq 0$, a contradiction. Hence, there are no gaps in $R(\mathcal{H})$.

We now show that there exists a 3 -uniform bihypergraph on 7 vertices with a broken chromatic spectrum. Let $\mathcal{H}=(X, \mathcal{E})$ be a 3-uniform bihypergraph defined as follows (see Figure 10.30, bi-edges are drawn as classic hyperedges): $X=\{1,2, \ldots, 7\}, \mathcal{E}=\{\{1,2,3\}$, $\{1,2,5\},\{1,2,6\},\{1,2,7\},\{3,4,2\},\{3,4,5\},\{3,4,6\},\{3,4,7\},\{5,6,7\}\}$. In every proper coloring, there are two possibilities for vertices 1 and 2: either $c(1) \neq c(2)$ or $c(1)=$ $c(2)$. Let $\{A, B, C, D, \ldots\}$ be the set of colors. If $c(1)=A, c(2)=B$, then all the remaining
vertices are colored with the colors from $\{A, B\}$; i.e., all the colorings are 2-colorings. If $c(1)=c(2)=A$, then $c(3)=c(4)=B$, and consequently, $c(5), c(6), c(7) \in\{C, D\}$; i.e., we have a strict 4-coloring. Therefore, no strict 3-coloring exists; thus, $S(\mathcal{H})=\{2,4\}$ (closer analysis shows that $\left.R(\mathcal{H})=(0,12,0,3,0,0,0), P(\mathcal{H}, \lambda)=3 \lambda(\lambda-1)\left(\lambda^{2}-5 \lambda+10\right)\right)$.

Finally, we prove that 9 is the minimum number of edges for a 3-uniform bihypergraph with a gap in the chromatic spectrum over all 3-uniform bihypergraphs on 7 vertices. Let $\mathcal{H}=(X, \mathcal{E})$ be a 3-uniform bihypergraph with $X=\{1,2, \ldots, 7\}$ and $|\mathcal{E}| \leq 8$. For a contradiction, suppose that $R(\mathcal{H})=\left(r_{1}, r_{2}, \ldots, r_{7}\right)$ has at least one gap. We immediately have $r_{1}=r_{7}=0$. If $r_{6} \neq 0$ (respectively $r_{6}=0, r_{5} \neq 0$ ), then at least 3 color classes are singletons which can easily be combined to obtain a strict coloring with 3, 4 and 5 (respectively 3 and 4) colors, so $R(\mathcal{H})$ contains no gaps, a contradiction.

Therefore, suppose $r_{7}=r_{6}=r_{5}=0, r_{4} \neq 0$. In a strict 4-coloring, if the number of singleton color classes $\geq 2$, then $r_{3} \neq 0$, a contradiction. Hence, the only type of a 4coloring to examine is

$$
(A, A, B, B, C, C, D) .
$$

If $\{1,2,7\} \notin \mathcal{E}$ (respectively $\{3,4,7\} \notin \mathcal{E},\{5,6,7\} \notin \mathcal{E}$ ), then there exists a 3-coloring $(A, A, B, B, C, C, A)$ (respectively $(A, A, B, B, C, C, B),(A, A, B, B, C, C, C)$ ) and thus $r_{3} \neq 0$, a contradiction. So, we have that in any case

$$
\{1,2,7\},\{3,4,7\},\{5,6,7\} \in \mathcal{E} .
$$

Observe further that the remaining, at most, 5 triples of $\mathcal{H}$ belong to the following family:

$$
\begin{array}{lll}
123 & 341 & 561 \\
124 & 342 & 562 \\
125 & 345 & 563 \\
126 & 346 & 564 .
\end{array}
$$

Since it consists of 3 columns, there is one column which contains, at most, one triple of $\mathcal{H}$. Choose the first column and let $\{1,2,3\} \notin \mathcal{E},\{1,2,4\} \notin \mathcal{E},\{1,2,5\} \notin \mathcal{E}$. If $\{3,4,1\},\{3,4,2\} \notin \mathcal{E}$, then the following 3-coloring exists: (A,A,A,A,B,B,C), a contradiction. Therefore $\{3,4,1\} \in \mathcal{E}$, or $\{3,4,2\} \in \mathcal{E}$. If $\{3,4,5\},\{3,4,6\} \notin \mathcal{E}$ then the following 3-coloring exists: (A,A,A,B,C,C,B), a contradiction. Hence $\{3,4,5\} \in \mathcal{E}$ or $\{3,4,6\} \in \mathcal{E}$. If $\{5,6,1\} \notin \mathcal{E}$ (respectively, $\{5,6,2\} \notin \mathcal{E}$ ), then the following 3-coloring exists: (B,A,C,C,B,B,A)(respectively (A,B,C,C,B,B,A)), a contradiction. Therefore \{5,6,1\}, $\{5,6,2\} \in \mathcal{E}$. If $\{1,2,6\} \in \mathcal{D}$ then all 8 bi-edges of $\mathcal{H}$ are exhausted and the 3-coloring (A,A,B,B,A,C,C) completes the proof.

Suppose $\{1,2,6\} \notin \mathcal{E}$. If $\{3,4,1\} \notin \mathcal{E}$ (respectively $\{3,4,2\} \notin \mathcal{E}$ ), then the following 3-coloring exists: (A,B,A,A,C,C,B) (respectively (B,A,A,A,C,C,B)), a contradiction. Therefore both $\{3,4,1\},\{3,4,2\} \in \mathcal{E}$. Hence all 8 bi-edges of $\mathcal{H}$ are exhausted, and the 3-coloring (A,B,C,C,A,B,B) completes the proof. $\square$

We conclude the section with the following important results:
Theorem 10.9.4 (Král' et al., 2000) If $\mathcal{H}$ is a mixed hypertree, then the chromatic spectrum is continuous.

Theorem 10.9.5 (Král' et al., 2003) If $\mathcal{H}$ is a mixed hypergraph with each vertex of degree 2, then the chromatic spectrum is continuous.

If we take dual to the mixed hypergraph from the theorem above, then the dual is a multigraph with two types of vertices: $\mathcal{C}$-vertices and $\mathcal{D}$-vertices. A proper coloring of $\mathcal{H}$ becomes a coloring of the edges of the respective multigraph in such a way that each $\mathcal{C}$ -vertex has two edges of the same color and each $\mathcal{D}$-vertex has two edges of different colors. Let us call such a multigraph a mixed multigraph. Thus the theorem above leads to the following important conclusion:

Corollary 10.9.3 (Král' et al., 2003) The chromatic spectrum in edge coloring of any mixed multigraph is continuous.

Notice that in such colorings there are lower and upper chromatic indexes; the special case gives the formula for the upper chromatic index $\bar{\chi}^{\prime}(G)=c+m-n+p$, see Part I, Section 5.9.

## Exercises 10.9.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-269.jpg?height=541&width=1020&top_left_y=1059&top_left_x=365)
Figure 10.31.

1. For mixed hypergraph $\mathcal{H}$ in Figure 10.31, find feasible sets $S\left(\mathcal{H}_{\mathcal{C}}\right)$ and $S\left(\mathcal{H}_{\mathcal{D}}\right)$.
2. For mixed hypergraph $\mathcal{H}$ in Figure 10.31, find feasible set $S(\mathcal{H})$ and prove that the chromatic spectrum is gap-free.
3. Given set of integers $S=\{2,3,5\}$, apply Algorithm 10.9.1 to construct a mixed hypergraph $\mathcal{H}$ with $S(\mathcal{H})=S$.

Computer Projects 10.9. Write a program for the following algorithmic problems.

1. Given a mixed hypergraph $\mathcal{H}$, by generating colorings at random, find an estimate on feasible set $S(\mathcal{H})$.
2. Implement Algorithm 10.9.1.

### 10.10. Coloring Planar Hypergraphs

Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be a mixed hypergraph. Denote the underlying family of edges of $\mathcal{H}$ by $\mathcal{E}=\mathcal{C} \cup \mathcal{D}$. Let us agree that if a subset of vertices is a bi-edge, then it appears in $\mathcal{E}$ only once. Recall that hypergraph $\mathcal{H}^{\prime}=(X, \mathcal{E})$ is the underlying hypergraph of $\mathcal{H}$. As we know from Section 9.4., a hypergraph $\mathcal{H}^{\prime}$ is planar if and only if bipartite representation $B\left(\mathcal{H}^{\prime}\right)$ is a planar graph.

Definition 10.10.1 A mixed hypergraph $\mathcal{H}=(X, C, \mathcal{D})$ is called planar if the underlying hypergraph $\mathcal{H}^{\prime}=(X, \mathcal{E})$ is planar.

This can be viewed as follows: we can embed $\mathcal{H}^{\prime}$ in the plane and label all hyperedges with $B, C$ or $D$ appropriately, according to whether they are bi-edges, $\mathcal{C}$-edges or $\mathcal{D}$-edges. Note that in the plane, $\mathcal{C}$-edges of size 2 can be contracted as described in the splittingcontraction Algorithm 10.5.1, and bi-edges of size 2 lead to uncolorability; so, in general, it suffices to only consider reduced mixed hypergraphs.

A first discussion on the coloring of planar hypergraphs can be found in a paper by Zykov [8]. The main results discussed there may be reformulated in the language of mixed hypergraphs as follows.

Theorem 10.10.1 (Bulitco [8]) The four color theorems for planar $\mathcal{D}$-graphs and for planar $\mathcal{D}$-hypergraphs are equivalent.

Theorem 10.10.2 (Burshtein, Kostochka [8]) If a planar $\mathcal{D}$-hypergraph contains at most one $\mathcal{D}$-edge of size 2, then $\chi(\mathcal{H}) \leq 2$.

There are uncolorable planar mixed hypergraphs. A planar embedding of the smallest non-trivial (reduced) uncolorable planar mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})=\left(X,\binom{X}{3},\binom{X}{2}\right)$ is shown in Figure 10.32: $X=\{1,2,3\}, \mathcal{C}=\{C\}=\{\{1,2,3\}\}, \mathcal{D}=\left\{D_{1}, D_{2}, D_{3}\right\}=$ $\{\{1,2\},\{2,3\},\{1,3\}\}$, the four faces are $f_{1}, f_{2}, f_{3}, f_{4}$. It is not difficult to extend this example to an infinite family of uncolorable planar mixed hypergraphs.

The general structure of uncolorable planar mixed hypergraphs is unknown. However, if a planar mixed hypergraph is colorable, then naturally the problem of determining the lower and upper chromatic number arises. Finding the lower chromatic number is difficult since if we allow $\mathcal{D}$-edges of cardinality 2 , it contains the four color problem as a special case, see Section 5.6. As to the upper chromatic number, the simplest interesting case is that of 3-uniform $\mathcal{C}$-hypergraphs. This case could be viewed as an analogue to the four color problem in the sense that we consider the maximum number of colors rather than the minimum. The situation, however, is different than the four color problem since the upper chromatic number of a 3-uniform $\mathcal{C}$-hypergraph must depend on the number of vertices $n$.

Therefore, we next consider an important simple case of planar mixed hypergraphs, namely, maximal 3-uniform planar bihypergraphs.

Since every face of a maximal planar hypergraph is of size 2, we can associate a graph $G(\mathcal{H})$ on the same vertex set with $\mathcal{H}$ : replace every face in $\mathcal{H}$ by an edge in $G$, so that every edge in $\mathcal{H}$ becomes a face of $G$. $\mathcal{H}$ is maximal 3-uniform, so $G$ must be a triangulation in the usual sense, see Section 4.5. We use $\mathcal{H}$ and $G$ interchangeably, and since every edge of $\mathcal{H}$ is a bi-edge, we will refer to them as bitriangulations.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-271.jpg?height=544&width=702&top_left_y=199&top_left_x=531)
Figure 10.32. The smallest reduced uncolorable planar mixed hypergraph.

We now study the colorings of bitriangulations; we want to color the vertices of triangulation $G$ so that every face has exactly two vertices of the same color.

Let us define that a coloring $c_{1}$ is a refinement of a coloring $c_{2}$ if every color class of $c_{1}$ is contained in a color class of $c_{2}$. If for every color class of the coloring $c_{2}$ we construct a touching graph (see Section 10.7., Definition 10.7.4), then the connected components of the touching graph represent the possibility of all further refinements of $c_{2}$. We say that a color class of a coloring $c$ is non-partitionable if it is a color class in every refinement of $c$; i.e., its touching graph is connected. In other words, there is no way to split the vertices of the color class and obtain another proper coloring. If every color class of $c$ is non-partitionable, then $c$ is said to be a maximal coloring. Notice that the number of colors used in a maximal coloring is not necessarily $\bar{\chi}$.

Lemma 10.10.1 A color class in a coloring of a bitriangulation is non-partitionable if and only if it induces a connected subgraph.

Proof. In a triangulation two vertices are together in a face if and only if they are adjacent. Therefore, a non-partitionable color class must induce a connected subgraph, since otherwise we can simply re-color one of the components. Conversely, a connected color class can not be refined further, since re-coloring some of its vertices results in two adjacent vertices from the old color class receiving distinct new colors. Since all faces are of size 3, this leads to a polychromatic face. $\square$

The duality of planar graphs in the following theorems refers to the classic planar duality "vertices - faces" (see Section 4.5.). In fact, starting with a maximal planar 3-uniform mixed bihypergraph $\mathcal{H}$ (a bitriangulation), we consider its corresponding "hyperedges - faces" dual which is the graph $G$ (also called a bitriangulation), and then we proceed to the dual "vertices - faces" graph $G^{*}$. In this way, a proper coloring of the original maximal planar 3-uniform bihypergraph $\mathcal{H}$ becomes a coloring of the vertices of the graph $G$ in such a way that each face has two vertices of the same color, which, in turn, becomes a coloring of the faces of the graph $G^{*}$ in such a way that each vertex belongs to two faces of the same color.

Theorem 10.10.3 (Kündgen et al., 2002) There is a 1-1 correspondence between the kcolorings of a bitriangulation $G$ and the $k$-face-colorings of the 2-factors in the dual $G^{*}$. In this correspondence, a coloring $c_{1}$ of $G$ is a refinement of a coloring $c_{2}$ if and only if the corresponding 2-factors are identical and the face-coloring associated with $c_{1}$ is a refinement of the face-coloring associated with $c_{2}$.

Proof. The main idea of the proof is accredited to Penaud (1975), who essentially showed that there is a 1-1 correspondence between 2-colorings of $G$ and 2-factors of $G^{*}$ (see Corollary 10.10.2).

A 2-factor of $G^{*}$ is simply a collection of closed Jordan curves; it partitions the plane into regions, inducing a partition of $V(G)$ into non-empty sets. Thus, every proper facecoloring of this 2-factor with $k$ colors corresponds to a $k$-coloring of $V(G)$. Such a coloring is in fact a $k$-coloring of the bitriangulation $G$, since it follows from the face-coloring being proper that every face of $G$ is colored with precisely two colors.

Conversely, given a $k$-coloring, we can recover the 2 -factor and its face-coloring. Since in every face of $G$ there are exactly two vertices of the same color, we get a 2-regular spanning subgraph, i.e. a 2-factor of $G^{*}$, by taking the dual edge of every edge in $G$ that is incident to vertices of different colors. Now, if two vertices are in the same region (generated by the 2-factor), then there is a curve connecting them, that passes only through vertices in this region. But then consecutive vertices on this curve must be on the same face and therefore adjacent. The edge joining these vertices can not be the dual of an edge in the 2-factor, since otherwise it would follow from the Jordan Curve Theorem 4.1.1 that they are in different regions. By the definition of the 2-factor, it thus follows that consecutive vertices on this curve must be of the same color, and that therefore every vertex in a given region has the same color. Since every region of the 2-factor must contain at least one vertex, we can therefore uniquely define the coloring of the regions, and this $k$-coloring is a proper coloring, since faces are separated by dual edges and thus adjacent faces contain adjacent vertices of different colors.

For the second part of the proof, observe that a refinement of the face-coloring of the dual graph clearly leads to a refinement of the coloring of the bitriangulation. For the converse, suppose that $c_{1}$ is a refinement of $c_{2}$. Following the construction of the dual 2-factor, it follows that the 2-factor for $c_{1}$ must contain the 2-factor for $c_{2}$, from which it follows that they are identical. Finally, the face-coloring corresponding to $c_{1}$ must be a refinement of the coloring corresponding to $c_{2}$. $\square$

As in Section 5.4., let $S(n, k)$ denote the Stirling numbers of the second kind, i.e. the number of ways of partitioning a set of $n$ elements into exactly $k$ sets. Also define $f_{k}\left(G^{*}\right)$ to be the number of 2-factors of $G^{*}$ that consist of exactly $k$ components (i.e, $k$ vertex disjoint cycles), and let $f\left(G^{*}\right)=\sum_{i \geq 1} f_{i}\left(G^{*}\right)$ be the total number of 2-factors of $G^{*}$.

Corollary 10.10.1 Every coloring of a bitriangulation $G$ can be refined to a unique maximal coloring and there are exactly $f_{k-1}\left(G^{*}\right)$ maximal $k$-colorings of $G$.

Proof. By the Jordan Curve Theorem 4.1.1, a given 2-factor consisting of $k-1$ disjoint cycles divides the plane into $k$ regions and, by Lemma 10.10.1, the coloring that assigns a different color to each face must be the unique maximal coloring for this 2-factor, since (as
shown in the proof above) the vertices in every region induce a connected subgraph. The second statement follows immediately. All refinements of a given coloring correspond to the same 2-factor, so that the first statement also follows. $\square$

Corollary 10.10.2 Every bitriangulation $G$ has exactly $f\left(G^{*}\right)$ strict 2-colorings. In general, the components of the chromatic spectrum $R(G)$ are defined by

$$
r_{k}(G)=\sum_{i \geq 1} S(i, k-1) f_{i}\left(G^{*}\right), 1 \leq k \leq n(G),
$$

and the chromatic polynomial is given by

$$
P(\mathcal{H}, \lambda)=\sum_{i \geq 1} f_{i}\left(G^{*}\right) \lambda(\lambda-1)^{i} .
$$

Proof. The first statement follows from both summation formulas, by setting $k=2$ or $\lambda=2$ respectively. For the first formula, it suffices, by Theorem 10.10.3, to show that every 2-factor consisting of $i$ cycles can be $k$-face-colored in exactly $S(i, k-1)$ ways. To see this, create a graph whose vertices are the faces in the dual of the 2-factor, and two vertices are adjacent if and only if the corresponding faces are separated by a 2-factor. This graph is connected and has $i$ edges. By the Jordan curve theorem, it has exactly $i+1$ vertices and must therefore form a tree $T$. Let $r_{k}(T)$ be the number of proper $k$-colorings of $T$. To see that $r_{k}(T)=S(e(T), k-1)$, observe that $r_{1}\left(K_{1}\right)=1$ and $r_{k}\left(K_{1}\right)=0$ for $k \geq 2$. By removing a pendant vertex $x$, we can see that $r_{k}(T)=(k-1) r_{k}(T-x)+r_{k-1}(T-x)$, the usual recursion for the Stirling numbers, as shown by Theorem 5.4.3 and Corollary 5.4.3. For the second formula, recall that the chromatic polynomial for a tree on $i+1$ vertices is $\lambda(\lambda-1)^{i}$ (Theorem 5.5.1). $\square$

Corollary 10.10.3 The chromatic spectrum of every bitriangulation $G$ is continuous, $\chi(G)=2$ and $\bar{\chi}(G)=1+\max \left\{k: f_{k}\left(G^{*}\right) \geq 1\right\}$.

Proof. Since $G^{*}$ is a 3-regular bridgeless graph it follows from Petersen's theorem (see e.g. [7, p.124]) that it has a 2-factor. So, by Corollary 10.10.2, every bitriangulation is 2-colorable, and therefore must have lower chromatic number 2. A coloring achieving the upper chromatic number must be maximal, so that the value of $\bar{\chi}(G)$ follows from Corollary 10.10.1. If $k=\bar{\chi}(G)$, then $f_{k-1}\left(G^{*}\right) \geq 1$; so, since $S(k-1, i-1) \geq 1$ for every $2 \leq i \leq k$, we get that $r_{i}(G) \geq 1$ in this range and that the chromatic spectrum is continuous. Furthermore, an $i$-coloring can be obtained from an $i$-coloring of the tree. $\square$

Corollary 10.10.4 Every planar mixed hypergraph without edges of size 2 is 2-colorable.
Proof. We may assume that the mixed hypergraph is a maximal bihypergraph, since adding $\mathcal{C}$ - or $\mathcal{D}$-edges only decreases the number of 2-colorings. Similarly, if $G$ contains any faces of size larger than 3, then they can be divided into faces of size 3 by adding graph edges to obtain a bitriangulation. The result now follows from Corollary 10.10.3. $\square$

Corollary 10.10.5 Every uniquely colorable planar mixed hypergraph must have an edge of size 2.

Proof. Suppose that $G$ is uniquely colorable and free of edges of size 2. Again, we may assume that $G$ is a bitriangulation. By Corollary 10.10.3, $\bar{\chi}(G)=2$; then, by Corollary 10.10.2, $G^{*}$ has a unique 2-factor that must be a Hamiltonian cycle. But this contradicts Theorem 10.10.4 below. $\square$

Theorem 10.10.4 (Thomason, 1978, Tutte, 1946, "Smith's Theorem")
The number of Hamiltonian cycles containing a given edge of a cubic graph is even.
Proof. We sketch the elegant proof of Thomason. Let $u v$ be the given edge. Consider the graph whose vertices are the Hamiltonian paths starting at $u$ with edge $u v$. Two such paths are adjacent if one can be obtained from the other by adding an edge at the end of the path and deleting a different edge. Now, vertices of degree 1 in this graph correspond to Hamiltonian cycles containing $u v$, and all other vertices have degree 2. Thus, the number of Hamiltonian cycles containing $u v$ is even. $\square$

As with the class of uncolorable planar mixed hypergraphs, there are infinitely many uniquely colorable planar mixed hypergraphs. One can easily see this, for example, by constructing a planar embedding of an $(x, y)$-invertor of arbitrary length (see Section 10.7.) which represents a uniquely colorable mixed hypergraph.

Theorem 10.10.3 and the corollaries above can be illustrated by the following example.
Example 10.10.1 Let $\mathcal{H}$ be a maximal planar 3-uniform bihypergraph, i.e. a bitriangulation, such that

$$
\mathcal{H}=\left(X,\binom{X}{3},\binom{X}{3}\right)
$$

where

$$
X=\{1,2,3,4\}, \mathcal{C}=\mathcal{D}=\{\{1,2,3\},\{2,3,4\},\{3,4,1\},\{4,1,2\}\} ;
$$

the drawing of $\mathcal{H}$ and its "hyperedges - faces" dual which is $K_{4}$ is shown in Section 9.4., Figure 9.6.

The drawing of $K_{4}$ in Figure 10.33 is the continuation of Figure 9.6. In the plane embedding of $K_{4}$ there are four faces denoted by $a, b, c$, and $d$. The dual "vertices - faces" is drawn by dotted curves and then redrawn as $K_{4}^{*}$. Graph $K_{4}^{*}$ has three 2-factors which all have one component (i.e., are hamiltonian) and shown next. Edges "not participating" in 2-factors are drawn by dashed curves. In the first 2-factor, faces 1 and 4 are outside the cycle and colored with color $A$; faces 2 and 3 are inside the cycle and colored with color $B$. In the second 2-factor, faces 1 and 3 are inside the cycle and colored with color $A$; faces 2 and 4 are outside the cycle and colored with color $B$. At last, in the third 2-factor, faces 1 and 2 are inside the cycle and colored with color $A$; faces 3 and 4 are outside the cycle and colored with color $B$.

This leads to the conclusion that there are only three strict colorings of the vertices of $K_{4}$ and $\mathcal{H}$, and all they are the following (in order of vertices 1,2,3,4): $A B B A, A B A B$, and $A A B B$. Thus, $\chi(\mathcal{H})=\bar{\chi}(\mathcal{H})=2$, the chromatic spectrum $R(\mathcal{H})=(0,3,0,0)$, and the chromatic polynomial $P(\mathcal{H}, \lambda)=3 \lambda(\lambda-1)$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-275.jpg?height=1631&width=1201&top_left_y=233&top_left_x=300)
Figure 10.33. Continuation of Figure 9.6.

Gap in the chromatic spectrum. Planar mixed hypergraphs with a gap in their chromatic spectrum were first constructed by Kobler and Kündgen:

Lemma 10.10.2 (Kobler, Kündgen, 2001) Let $\mathcal{H}_{2,4}^{\prime}=(X, \mathcal{C}, \mathcal{D})$ be the mixed hypergraph with $X=\{1,2, \ldots, 6\}, \mathcal{C}=\left\{C_{1}, \ldots, C_{4}\right\}=\{\{1,2,3\},\{2,3,4\},\{2,4,5\},\{4,5,6\}\}$, and $\mathcal{D}=\left\{D_{1}, \ldots, D_{6}\right\}=\{\{1,2\},\{1,5\},\{1,6\},\{2,4\},\{3,6\},\{4,6\}\}$. $\mathcal{H}_{2,4}^{\prime}$ is planar and has
feasible set $S\left(\mathcal{H}_{2,4}^{\prime}\right)=\{2,4\}$.
Proof. Figure 10.34 shows an embedding of $\mathcal{H}_{2,4}^{\prime}$ in the plane. The $\mathcal{D}$-edges are drawn as line segments and a curve, the $\mathcal{C}$-edges as regions having size 3, and the faces are not indicated. Let $c$ be a strict coloring of $\mathcal{H}_{2,4}^{\prime}$. If $c(2) \neq c(3)$, then the remaining colors are forced and we have the 2-coloring $\{1,3,4\} \cup\{2,5,6\}$. If $c(2)=c(3)$, then $c(4)=c(5)$ and $c(2) \neq c(4)$, which results in the strict 4-coloring $\{1\} \cup\{2,3\} \cup\{4,5\} \cup\{6\}$. One can see that these feasible partitions are unique. $\square$

Consequently, the chromatic spectrum

$$
R\left(\mathcal{H}_{2,4}^{\prime}\right)=(0,1,0,1,0,0),
$$

and the chromatic polynomial

$$
P\left(\mathcal{H}_{2,4}^{\prime}, \lambda\right)=\lambda(\lambda-1)\left(\lambda^{2}-5 \lambda+7\right)
$$

(compare to $\mathcal{H}_{2,4}$ in Figure 10.29 and to the bihypergraph in Figure 10.30).

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-276.jpg?height=917&width=1219&top_left_y=999&top_left_x=272)
Figure 10.34. Planar mixed hypergraph with a gap, $\mathcal{H}_{2,4}^{\prime}$.

Theorem 10.10.5 (Kobler, Kündgen, 2001) A non-empty set of positive integers $S$ is the feasible set of some planar mixed hypergraph if and only if $S$ is an interval $\{s, s+1, \ldots, t\}$ with $1 \leq s \leq 4$ or of the form $\{2,4,5, \ldots, t\}$.

Proof. Let $G=(X, \mathcal{D})$ be a $t$-vertex planar $\mathcal{D}$-graph. The feasible set $S(G)=\{\chi(G)$, $\chi(G)+1, \ldots, t\}$, where $\chi(G) \leq 4$. This shows the sufficiency of the condition when $S$ is
an interval. When $S$ has a gap at 3, consider the mixed hypergraph obtained from $\mathcal{H}_{2,4}^{\prime}$ by taking the vertices $\{7, \ldots, t+2\}$ and placing them in the region containing vertices 2 and 3. Then include the $\mathcal{C}$-edges $\{\{2,3,7\},\{2,3,8\}, \ldots,\{2,3, t+2\}\}$. If we have a 2 -coloring on $\mathcal{H}_{2,4}^{\prime}$, then this only extends to a 2-coloring of the larger graph, whereas from the 4-coloring, we obtain all other values in the feasible set.

It remains to prove the necessity of the condition. So, consider a planar mixed hypergraph $\mathcal{H}$, with feasible set $S \neq \emptyset$. If $1 \in S$, then $S$ trivially forms an interval. Let $c$ be a strict $t$-coloring of $\mathcal{H}$, where $t$ is the largest value in $S$. We will construct a planar mixed hypergraph $\mathcal{H}^{\prime}$ with $\{4,5, \ldots, t\} \subset S\left(\mathcal{H}^{\prime}\right) \subset S$. So, by the choice of $t$, it follows that $S$ is of the required form.
$\mathcal{H}^{\prime}$ will have the same vertex set as $\mathcal{H}$. We will keep every edge of size 2 , and since $\mathcal{H}$ is colorable this must be either a $\mathcal{C}$-edge or a $\mathcal{D}$-edge. Now consider all edges containing $\geq 3$ vertices. If the corresponding region is a $\mathcal{C}$-edge, then it contains vertices $u, v$ with $c(u)=c(v)$. We replace the region by a $\mathcal{C}$-edge $\{u, v\}$. If the region is a $\mathcal{D}$-edge, then it contains vertices $u, v$ with $c(u) \neq c(v)$. We replace the region by a $\mathcal{D}$-edge $\{u, v\}$. If the region is a bi-edge, then it contains vertices $u, v, w$ with $c(u)=c(v) \neq c(w)$. We replace the region by a $\mathcal{C}$-edge $\{u, v\}$ and a $\mathcal{D}$-edge $\{v, w\}$. The mixed hypergraph $\mathcal{H}^{\prime}$ we obtain is planar and still has $c$ as a strict $t$-coloring. Furthermore, in obtaining $\mathcal{H}^{\prime}$ from $\mathcal{H}$ no coloring constraints are lost, so that every coloring of $\mathcal{H}^{\prime}$ is a coloring of $\mathcal{H}$.

We now have a planar mixed hypergraph with all edges ( $\mathcal{C}$ - or $\mathcal{D}$-) of size 2 . Contract every $\mathcal{C}$-edge and obtain a loopless planar $\mathcal{D}$-graph $G$. There is a 1-1 correspondence between strict colorings of $G$ and strict colorings of $\mathcal{H}^{\prime}$. Since the feasible set $S(G)=$ $\{\chi(G), \chi(G)+1, \ldots, t\}$, we see that $\{4,5, \ldots, t\} \subset S\left(\mathcal{H}^{\prime}\right)$. $\square$

The importance of the theorem above is that the gaps in the chromatic spectrum of planar mixed hypergraphs may occur only at 3.

Exercises 10.10.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-277.jpg?height=430&width=707&top_left_y=1491&top_left_x=528)
Figure 10.35.

1. Let $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ be a bi-triangulation such that its "hyperedges - faces" dual is graph $G$ in Figure 10.35. Construct vertices-faces dual graph $G^{*}$, find all 2-factors of $G^{*}$, and the chromatic spectrum $R(\mathcal{H})$ and the chromatic polynomial $P(\mathcal{H}, \lambda)$.
2. Determine if mixed hypergraph $\mathcal{H}_{2,4}^{\prime}$ in Figure 10.34 is perfect.

Computer Projects 10.10. Write a program for the following algorithmic problems.

1. Given a mixed hypergraph $\mathcal{H}$, determine if $\mathcal{H}$ is planar.
2. Given a planar mixed hypergraph $\mathcal{H}$, determine if its chromatic spectrum is broken.

## Chapter 11

## Modeling with Hypergraphs

### 11.1. List Colorings without Lists

For cellular telephones, the frequencies are assigned by zones. Every zone is assigned a list of frequencies that can be used in the zone. If two zones interfere, they cannot use the same frequency at any time. Suppose we have three zones in a region, say $Z_{1}, Z_{2}$ and $Z_{3}$. Zone $Z_{1}$ must use frequencies $a$ or $c$, zone $Z_{2}$ must use frequencies $a$ or $b$, and zone $Z_{3}$ must use frequencies $b$ or $c$. Zones $Z_{1}$ and $Z_{2}$ interfere, zones $Z_{2}$ and $Z_{3}$ interfere, and zones $Z_{1}$ and $Z_{3}$ do not interfere.

In how many ways and in which ways can we assign frequencies to the zones? Construct a graph $G$ with three vertices $Z_{1}, Z_{2}$ and $Z_{3}$, see Figure 11.1; two vertices are adjacent if the respective zones interfere. The list of admissible colors $\{a, c\}$ is assigned to vertex $Z_{1}$, the list of admissible colors $\{a, b\}$ is assigned to vertex $Z_{2}$, and the list of admissible colors \{ $b, c\}$ is assigned to vertex $Z_{3}$. Now the original problem can be formulated as follows: in how many ways and in which ways can we color the vertices of graph $G$ such that adjacent vertices have different colors and each vertex is colored with the color from its list? Such graph colorings are called the list colorings. We show that in turn, the list colorings can be modeled by the mixed hypergraph colorings without any lists.

Construct a mixed hypergraph $\mathcal{H}=(X, \mathcal{C}, \mathcal{D})$ in the following way, see Figure 11.1. Since we have three colors $a, b, c$ in total, add three new vertices $a, b$, and $c$ and put $X=$ $\left\{Z_{1}, Z_{2}, Z_{3}, a, b, c\right\}$. Set $\mathcal{D}$ to include all edges of $G$ plus all edges forming complete graph on vertices $a, b$ and $c$. At last, set $\mathcal{C}=\left\{\left\{Z_{1}, a, c\right\},\left\{Z_{2}, a, b\right\},\left\{Z_{3}, b, c\right\}\right\}$.

One can easily see that every list coloring of $G$ corresponds to a proper coloring of the mixed hypergraph $\mathcal{H}$, and vice versa. Indeed, since the first $\mathcal{C}$-edge $\left\{Z_{1}, a, c\right\}$ must have at least two vertices of the same color, and vertices corresponding to colors form a complete graph, in any proper coloring of $\mathcal{H}$, vertex $Z_{1}$ will be colored either with a color of vertex $a$ or with a color of vertex $c$. The similar is true for all $\mathcal{C}$-edges.

As a consequence, graph $G$ admits at least one list coloring if and only if mixed hypergraph $\mathcal{H}$ is colorable. Clearly, the names of colors (=the values of frequencies) do not matter; the things that matter are the structure of graph $G$ (=interferencies between the zones in the region), the lists of colors with assignments, and the total number of colors (frequencies).

For our simple example in Figure 11.1, one can manually find that $\chi(\mathcal{H})=\bar{\chi}(\mathcal{H})=$

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-280.jpg?height=1142&width=914&top_left_y=228&top_left_x=427)
Figure 11.1. List colorings without lists.

3, chromatic spectrum $R(\mathcal{H})=(0,0,3,0,0,0)$, chromatic polynomial $P(\mathcal{H}, \lambda)=3 \lambda(\lambda-$ $1)(\lambda-2)$, and moreover, the three list colorings of $G$ in order $\left(Z_{1}, Z_{2}, Z_{3}\right)$ are as follows: $(a, b, c),(c, b, c),(c, a, c)$.

### 11.2. Resource Allocation

Consider the following example. Let us have $n=4$ elementary jobs $X=\left\{x_{1}, x_{2}, x_{3}\right.$, $\left.x_{4}\right\}$ which are to be executed by allocating $m=5$ available resources $Y=\left\{y_{1}, y_{2}, y_{3}\right.$, $\left.y_{4}, y_{5}\right\}$. Suppose that time is discrete and each of these elementary jobs can be executed during one unit of time. A set of resources $S\left(x_{i}\right) \subseteq Y$ must be available for job $x_{i} \in X$ to be performed. For execution, job $x_{1}$ requires resource $S_{1}=\left\{y_{1}\right\}$, job $x_{2}$ requires resources $S_{2}=\left\{y_{1}, y_{2}, y_{3}\right\}$, job $x_{3}$ requires resources $S_{3}=\left\{y_{3}, y_{4}\right\}$, job $x_{4}$ requires resources $S_{4}=\left\{y_{2}, y_{4}, y_{5}\right\}$. For any resource used by at least two jobs simultaneously, a penalty must be paid.

Management requirements are: jobs $x_{1}, x_{2}, x_{3}$ must be performed for at most two units of time, and jobs $x_{1}, x_{2}, x_{4}$ must also be performed for a maximum two units of time without

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-281.jpg?height=1116&width=981&top_left_y=233&top_left_x=318)
Figure 11.2. Bipartite graph $G$ and mixed hypergraph $\mathcal{H}$ for resource allocation.

penalty. Is there a resource allocation for all the jobs without any penalty?
Construct a bipartite graph "jobs - resources" $G$, see Figure 11.2, and then construct a mixed hypergraph $\mathcal{H}$ as follows. Since $S_{1} \cap S_{2} \neq \emptyset$, construct the first $\mathcal{D}$-edge $D_{1}=$ $\left\{x_{1}, x_{2}\right\}$. Since $S_{2} \cap S_{3} \neq \emptyset$, construct the second $\mathcal{D}$-edge $D_{2}=\left\{x_{2}, x_{3}\right\}$. Since $S_{2} \cap S_{4} \neq \emptyset$, construct the third $\mathcal{D}$-edge $D_{3}=\left\{x_{2}, x_{4}\right\}$. Since $S_{3} \cap S_{4} \neq \emptyset$, construct the fourth $\mathcal{D}$-edge $D_{4}=\left\{x_{3}, x_{4}\right\}$. Since $S_{1} \cap S_{3}=\emptyset$ and $S_{1} \cap S_{4}=\emptyset$, no other $\mathcal{D}$-edge can be added to $\mathcal{H}$.

Management requirements give us the following two $\mathcal{C}$-edges: $C_{1}=\left\{x_{1}, x_{2}, x_{3}\right\}, C_{2}=$ $\left\{x_{1}, x_{2}, x_{4}\right\}$. Put $\mathcal{C}=\left\{C_{1}, C_{2}\right\}, \mathcal{D}=\left\{D_{1}, D_{2}, D_{3}, D_{4}\right\}$. Thus, the mixed hypergraph $\mathcal{H}=$ $(X, C, \mathcal{D})$ is obtained.

One can easily see that $\mathcal{H}$ is uncolorable. This means that no allocation of resources, without any penalty is possible. However, if we violate, for example, the constraint expressed by the $\mathcal{C}$-edge $C_{1}$, then we can color the vertices $x_{1}, x_{2}, x_{3}, x_{4}$ respectively with the colors 1,2,3,1. Therefore, in this case, the minimum number of time units is 3, and the maximum number of time units is also 3, for all the jobs to be performed. In any case, one penalty must be paid. If we are interested in the performance without any penalty, then one might ignore, for example, job $x_{3}$. This gives the minimum and maximum time of 2 units
for the remaining jobs to be executed, etc.
In general case, every proper coloring of $\mathcal{H}$ represents an allocation of resources without penalty and vice versa; i.e., the resource allocation problem is an instance of a colorability problem. Respectively, the minimum and maximum time for executing all the jobs without penalty correspond to the lower and upper chromatic numbers. The maximization of the number of jobs or the minimization of penalties represent the respective optimization problems on coloring the mixed hypergraph $\mathcal{H}$. Also, the information about the chromatic spectrum $R(\mathcal{H})$ and all the strict colorings will answer the question if there exists an allocation such that each resource is used continuously. Notice that constraints expressed by $\mathcal{C}$-edges may generally increase the minimum duration in resource allocation. In addition, the possibility of gaps in the chromatic spectrum gives no guarantee that resource allocation is possible for each of the intermediate values between $\chi(\mathcal{H})$ and $\bar{\chi}(\mathcal{H})$.

In computer science applications, the jobs could be, for example, the computational problems, and the resources could be the processors in parallel computations. Or, the jobs could be the queries, and the resources could be the files in a data base, and so on.

## Chapter 12

## Appendix

"What did you like most during the study at the university?

- Great school, great professors...

What did you hate most?

- Mathematical induction..."

### 12.1. What Is Mathematical Induction

One of the most popular methods of proof in graph theory is the proof by mathematical induction. The idea is simple. Suppose we want to prove a statement $P_{n}$ depending on $n$ where $n=1,2,3, \ldots$. This is equivalent to prove an infinite list of statements $P_{1}, P_{2}, \ldots$ to be true. Instead of proving the infinite list of theorems, we prove just the following two:

1. Prove $P_{1}$.
2. For any $k \geq 1$, prove that if $P_{k}$ is true, then $P_{k+1}$ is true.

It is easy to see that this is sufficient to conclude that $P_{n}$ is true for all $n=1,2, \ldots$, or, equivalently, all statements $P_{1}, P_{2}, \ldots$ are true.

Step 1. is called the basis of induction, see Fig. 12.1. Step 2. is called the induction step. It can be abbreviated as $P_{k} \rightarrow P_{k+1}$ and called an implication. In step 2., the statement $P_{k}$ is called the induction hypothesis. In notation $P_{n}, n$ is called the induction parameter.

Mathematical induction is a bright example how generalizations work in mathematics: instead of proving $P_{1} \rightarrow P_{2}$, then $P_{2} \rightarrow P_{3}$, and so on (up to infinity!), one just prove the general case $P_{k} \rightarrow P_{k+1}$. In this way, the induction step replaces infinitely many proofs. To have a complete proof, we only need an initial condition which is the induction basis. Evidently, any positive integer greater than 1 may serve as the induction basis.

Summarizing these arguments, one can describe the following sequence of steps in writing the proofs by mathematical induction in Graph Theory:

1. Write down the statement $P_{n}$, i. e. the theorem to be proved.
2. Induction basis: write down and prove the statement $P_{n_{0}}$, where property $P_{n_{0}}$ is directly observed; usually, $n$ is the number of vertices, and $n_{0}=3$, or $n_{0}=4$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-284.jpg?height=580&width=1098&top_left_y=230&top_left_x=334)
Figure 12.1. Mathematical induction.

3. Write down the statement $P_{k}$.
4. Write down the statement $P_{k+1}$.
5. Induction step: prove that if $P_{k}$ is true, then $P_{k+1}$ is true. In the proof, the assumption that $P_{k}$ is true, must be used. To prove $P_{k+1}$, one consider a graph on $k+1$ vertices. Then apply to it an operation such as removing a vertex or contraction an edge to obtain a graph having $k$ vertices. At this point it is very important to assure that property $P_{k}$ (for a graph on $k$ vertices) holds. Finally, considering the inverse operation one prove that property $P_{k+1}$ (for a graph on $k+1$ vertices) fulfills.
6. Conclude that $P_{n}$ is true for all $n \geq n_{0}$.

![](https://cdn.mathpix.com/cropped/cde1d261-30b2-451d-a9dd-108d5796775a-284.jpg?height=577&width=1119&top_left_y=1551&top_left_x=318)
Figure 12.2. Strong mathematical induction.

There is another form of this method which is called the strong mathematical induction. The difference is in the induction step. Namely, instead of proving $P_{k} \rightarrow P_{k+1}$, the
strong mathematical induction requires the following: prove that if $P_{1}$ is true, and if $P_{2}$ is true, and if $P_{3}$ is true, and so on, and if $P_{k}$ is true, then $P_{k+1}$ is true. This can be abbreviated as $P_{1}, P_{2}, \ldots, P_{k} \rightarrow P_{k+1}$. Implicitly it is clear that if we started at $P_{1}$ and arrived to $P_{k}$, then all intermediate statements $P_{2}, P_{3}, \ldots, P_{k-1}$ must be true. In some complicated cases we need all these values to prove $P_{k+1}$, and that is exactly the motivation of applying the strong mathematical induction. The idea is depicted in Figure 12.2. As in simple mathematical induction, evidently, any positive integer greater than 1 may serve as the induction basis.

In Graph Theory proofs, sometimes index $k$ is omitted or hidden; the assumption is "let $P$ hold for all graphs on $<n$ vertices" and then one prove $P$ for a graph on $n$ vertices.

### 12.2. Graph Theory Algorithms and Their Complexity

Generally, an algorithm is a finite set of precise instructions for solving a problem. In graph theory, algorithms consist of sequences of numbered steps (with possible repetitions and checking logical conditions) describing what to do to solve a problem for a graph or hypergraph. In all cases, a graph or a hypergraph is in the input, and a number or a special subgraph in many cases is in the output. An algorithm can be programmed and the program can be run on the computer. If we try the same program for different graphs, then we find that time for computations depends on the number of vertices $n$, i.e., it is some function $f(n)$. If we have another algorithm for the same problem, then the running time is another function of $n$, say, $g(n)$. How to compare the algorithms? The first algorithm is better if $f(n) \leq g(n)$ beginning with some fixed number of vertices, say $n \geq N_{1}$. If the first algorithm is run on a computer which is $c_{1}$ times faster, and the second algorithm is run on a computer which is $c_{2}$ times faster, then the first is better when $f(n) / c_{1} \leq g(n) / c_{2}$ holds for all $n \geq N_{2}$ where $N_{2}$ is some other natural number. This is equivalent to $f(n) \leq C g(n)$ for some constant $C=c_{1} / c_{2}$. Evidently, it holds for any other constant $C^{\prime} \geq C$ and any other $N \geq N_{2}$. In other words, no matter how fast the new computers would be, if the inequality $f(n) \leq C g(n)$ holds for some sufficiently large constant $C$ and all $n \geq N$, then the first algorithm is better. This reasoning explains the meaning of the following notation in comparison of the complexity of algorithms.

We say that $f(n)$ is $O(g(n)$ ) (read " $f(n)$ is big-oh of $g(n)$ ", sometimes denoted by $f(n)$ $=O(g(n)))$ if there are constant $C$ and a number $N$ such that

$$
f(n) \leq C g(n)
$$

for all $n \geq N$. The basic idea of this definition is that time is the measure of the complexity of algorithms, and that time should not depend on the speed of a computer. The comparison of algorithms is asymptotical, i.e., what occurs beginning with some $N$ on, or, as we say, when $n$, the number of vertices, approaches infinity.

In practice, when estimating algorithms, one compute the number of elementary operations (addition, multiplication, comparison, etc.) as a function of $n$ in the worst case at every step of the algorithm. That is an upper bound for the complexity. One then say that the complexity of the algorithm is $O(g(n))$ where $g(n)$ is that very same upper bound.

If $g(n)=n$, then the algorithm is called linear-time and its complexity is denoted by $O(n)$. Generally, if $g(n)$ is a polynomial of degree $k$ on $n$, then the algorithm is called
polynomial-time and complexity is denoted by $O\left(n^{k}\right)$. If $g(n)$ is an exponential function, then the algorithm is called exponential-time and complexity is denoted by $O\left(a^{n}\right)$ where $a>1$. There is also a constant complexity denoted by $O(1)$, logarithmic complexity denoted by $O(\log n)$ and even factorial complexity denoted by $O(n!)$.

For example, let a graph $G$ be given by its adjacency matrix $A(G)$ of size $n \times n$ and the problem is to find the vertex degrees. Since the matrix is symmetric, it is sufficient to check every entry of the lower triangle if it is 0 or 1 . The number of such checks is $\left(n^{2}-n\right) / 2$ which is the polynomial of $n$. Therefore the complexity of such procedure is $O\left(n^{2}\right)$.

However, many problems in graph theory are much more complex. The best known algorithms for finding the chromatic number of a general graph, or determine if two graphs are isomorphic, for example, are exponential-time.

For hypergraphs, the complexity usually is expressed as a function of the sum of all edge cardinalities, not just $n$. For example, if we need to find vertex degrees of a hypergraph on $n$ vertices and $m$ edges given by its incidence matrix, then we need to check every of $m n$ entries if it is 0 or 1 . So the total time is $O(m n)$. However, if the hypergraph is given by its edge list, then we may scan the lists and determine the degree of every vertex. In this case, the total time is $O$ (the sum of all edge cardinalities). As one can see, the complexity of many algorithms depends on the graph or hypergraph representation in computer memory.

In general, a problem that can be solved by polynomial-time algorithm is called tractable, otherwise it is called intractable. Tractable problems form the so called class P of problems. There are many problems that no polynomial-time algorithm can solve them, but a solution (if known) can be checked in polynomial time. Such problems form the so called class NP. At last, there is a class of problems with the property that if any of these problems can be solved in polynomial time, then all of them can be solved in polynomial time because there is a polynomial-time transformation from each other. They form the so called class of NP-complete problems.

### 12.3. Answers and Hints to Selected Exercises

Chapter 1
Section 1.1

1. $n\left(G_{1}\right)=4, m\left(G_{1}\right)=3, n\left(G_{2}\right)=5, m\left(G_{2}\right)=7, n\left(G_{3}\right)=8, m\left(G_{3}\right)=12$. 5. Degree sequences: $G_{1}:(1,1,1,3), G_{2}:(2,2,2,4,4), G_{3}:(2,2,3,3,3,3,4,4)$.

Section 1.2

1. $L\left(G_{1}\right)=\{\{2\},\{1,3,4\},\{2,4\},\{2,3\}\}$.
2. 

$$
A\left(G_{1}\right)=\left(\begin{array}{llll}
0 & 1 & 0 & 0 \\
1 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
0 & 1 & 1 & 0
\end{array}\right)
$$

3. 

$$
I\left(G_{1}\right)=\left(\begin{array}{llll}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 1 \\
0 & 1 & 1 & 0 \\
0 & 0 & 1 & 1
\end{array}\right)
$$

4. $J\left(G_{1}\right)=\{\{1,2\},\{2,3\},\{3,4\},\{2,4\}\}$.

Section 1.4
5. $G_{5}, G_{6}, G_{7}, G_{8}, G_{9}$. 7. Because $K_{s, r}$ is obtained from $K_{r, s}$ by just interchanging the parts. 8. $G_{1} \cong G_{2}, G_{3} \cong G_{4}, G_{7} \cong G_{8} \cong G_{9}$. 9. When the names and order of vertices correspond to the given isomorphism. 10. When the names and order of vertices correspond to any isomorphism.

Section 1.5
6. $\eta(T)=2, \eta\left(C_{5}\right)=3, \eta\left(W_{5}\right)=4, \eta\left(K_{2,3}=3\right.$. 10. If we reverse the order in degree sequence of $G$ and add it with the degree sequence of $\bar{G}$ as two vectors, then we obtain a vector with all components equal to $n-1$.

Section 1.6
11. In $K_{4,4}: C_{4}, C_{8}$, in cube: $C_{4}, C_{8}$, in Petersen graph: $C_{5}, C_{9}$. 13. For graphs in Figure 1.21: $\omega\left(G_{1}\right)=\omega\left(G_{2}\right)=\omega\left(G_{3}\right)=\omega\left(G_{4}\right)=3, \omega\left(G_{5}\right)=\omega\left(G_{6}\right)=\omega\left(G_{7}\right)=\omega\left(G_{8}\right)=\omega\left(G_{9}\right)=2$.
14. For graphs in Figure 1.21: $\alpha\left(G_{1}\right)=\alpha\left(G_{2}\right)=\alpha\left(G_{3}\right)=\alpha\left(G_{4}\right)=2, \alpha\left(G_{5}\right)=\alpha\left(G_{6}\right)=4$, $\boldsymbol{\alpha}\left(G_{7}\right)=\boldsymbol{\alpha}\left(G_{8}\right)=\boldsymbol{\alpha}\left(G_{9}\right)=3$. 15. For graphs in Figure 1.21: $\boldsymbol{\tau}\left(G_{1}\right)=\boldsymbol{\tau}\left(G_{2}\right)=2, \boldsymbol{\tau}\left(G_{3}\right)=$ $\tau\left(G_{4}\right)=3, \tau\left(G_{5}\right)=\tau\left(G_{6}\right)=4, \tau\left(G_{7}\right)=\tau\left(G_{8}\right)=\tau\left(G_{9}\right)=2$. 16. For graphs in Figure 1.21: $\nu\left(G_{1}\right)=\nu\left(G_{2}\right)=\nu\left(G_{3}\right)=\nu\left(G_{4}\right)=2, \nu\left(G_{5}\right)=\nu\left(G_{6}\right)=4, \nu\left(G_{7}\right)=\nu\left(G_{8}\right)=\nu\left(G_{9}\right)=2$.
17. If $n$ is even: $\alpha\left(C_{n}\right)=\tau\left(C_{n}\right)=\nu\left(C_{n}\right)=n / 2$, if $n$ is odd: $\alpha\left(C_{n}\right)=\nu\left(C_{n}\right)=(n-1) / 2$, $\tau\left(C_{n}\right)=(n+1) / 2$, for all $n: \omega\left(C_{n}\right)=2$.

Section 1.7
3. $\mathrm{K}(G)=2$. 4. $k \geq 2$. 12. 2.

Chapter 2
Section 2.1

1. $\Lambda\left(E_{n}\right)=0, \Lambda\left(C_{n}\right)=1, \Lambda\left(K_{n}\right)=(n-1)(n-2) / 2, \Lambda\left(W_{n}\right)=n-1$.

Section 2.2

1. $\operatorname{diam}(T)=9$, radius $=5$.

Section 2.3
2. Minimum weight $=28$. 3. Maximum weight $=49$. 4. $n^{n-2}$.

Section 2.4
2. $m=n$. 4. $\tau\left(K_{m, n}\right)=\nu\left(K_{m, n}\right)=\min \{m, n\}$. 6. $\tau=\nu=13$.

## Chapter 3

Section 3.2
2. $G_{1}$ and $G_{3}$ are chordal; $G_{2}$ is not chordal. 3. $G_{2}$. 7. $\Theta\left(G_{1}\right)=\alpha\left(G_{1}\right)=3, \Theta\left(G_{2}\right)=$ $\boldsymbol{\alpha}\left(G_{2}\right)=5, \boldsymbol{\theta}\left(G_{3}\right)=\boldsymbol{\alpha}\left(G_{3}\right)=3$. 8. For cube: 6. 9. From cube: 5.
Section 3.3

1. $M\left(G_{1}\right)=3, \omega\left(G_{1}\right)-1=2 ; M\left(G_{2}\right)=4, \omega\left(G_{2}\right)-1=2 ; M\left(G_{3}\right)=2, \omega\left(G_{3}\right)-1=2.2$. $G_{1}, G_{2}$ are not chordal; $G_{3}$ is chordal. 3. $M\left(C_{n}\right)=2, M\left(K_{n}\right)=n-1, M\left(W_{n}\right)=3$; for cube, prism and Petersen graph: $M(G)=3$. 4. Take empty graph $E_{n}$ with sufficient large $n$; add a vertex and make it adjacent to all the vertices of $E_{n}$; repeat the procedure. Observe that $\omega=2$ for all obtained graphs, and $M(G)$ is increasing by 1 every step until it reaches $n$. Evidently, the graph obtained is $K_{n, n}$. 5. Delete vertices by minimum degree; since graph is $k$-regular, at any step except the first, there is a vertex of degree $\leq k-1$.

Section 3.4
2. $\operatorname{diam}(G)=6$, radius = 3.

Section 3.5

1. $G_{1}$ and $G_{2}$ are quasi-triangulated, $G_{3}$ is not. 2. $C_{5}$ in $G_{3}$. 5. Quasi-triangulated graphs: $C_{n}$ for $n=3,4, K_{n}$ for $n \geq 3, W_{n}$ for $n=4,5$.

Chapter 4
Section 4.1

1. $G_{1}: 5 ; G_{2}: 7$. 3. Yes.

Section 4.2

1. See Figure 1.30 for prism and Figure 1.17 for cube.

Section 4.3

1. For $K_{3,3}: 0,1,2,3$; for $K_{5}: 0,1,2,3,4$. 6.1 .

Section 4.4

1. $K_{n}: n=3,4 ; K_{m, n}: m=1, n \geq 3$, or $m=2, n \geq 3 ; W_{n}: n \geq 4$. 3. $G_{1}$ is not planar; $G_{2}$ is planar.

Chapter 5
Section 5.2

1. $\chi\left(E_{n}\right)=1, \chi\left(K_{n}\right)=n, \chi\left(K_{m, n}\right)=2, \chi\left(T_{n}\right)=2, \chi\left(C_{2 n}\right)=2, \chi\left(C_{2 n+1}\right)=3, \chi\left(W_{2 n}\right)=4$, $\chi\left(W_{2 n+1}\right)=3$. 4. $\lambda \geq 136$. 6. $\chi(G) \leq 6$. 7. $\chi(G)=5$.

Section 5.3

1. $P\left(E_{4}, \lambda\right)=\lambda^{4} ; P\left(C_{5}, \lambda\right)=(\lambda-1)^{5}-(\lambda-1) ; P\left(W_{4}, \lambda\right)=\lambda^{(4)} ; P\left(P_{n}, \lambda\right)=\lambda(\lambda-1)^{n-1}$.
2. The last one.

Section 5.4
2. $S(7,1)=1, S(7,2)=63, S(7,3)=301, S(7,4)=350, S(7,5)=140, S(7,6)=21$, $S(7,7)=1 ; s(3,1)=2, s(3,2)=-3, s(3,3)=1$. 3. $P\left(G_{1}, \lambda\right)=\lambda(\lambda-1)^{3}(\lambda-2)^{2}\left(\lambda^{2}-\right.$ $3 \lambda+3)^{2} ; P\left(G_{2}, \lambda\right)=\lambda(\lambda-1)(\lambda-2)^{4} ; P\left(G_{3}, \lambda\right)=\lambda(\lambda-1)(\lambda-2)^{4}\left(\lambda^{2}-3 \lambda+3\right)$.

Section 5.5
3. Graph $G=(X, E)$ with $X=\{1,2,3,4,5\}$ and adjacency list $L(G)=\{\{2,4\}$, $\{1,3,4,5\},\{2,5\},\{1,2,5\},\{2,3,4\}\}$; the order of online coloring: $1,2,3,4,5$.

Section 5.6

1. For Petersen graph: $M=3$, therefore $\chi \leq 4$. 2. Idea: switch the colors in the regions on one side of a newly added line.

Section 5.7

1. None of them is perfect because each contains induced $C_{5}$. 2. $W_{2 k-1}$ are perfect, $W_{2 k}$ are not, $k \geq 3$.

Section 5.8

1. $\chi^{\prime}\left(K_{n}\right)=n$ if $n \geq 3$ is odd, $\chi^{\prime}\left(K_{n}\right)=n-1$ if $n \geq 2$ is even. $\chi^{\prime}\left(C_{n}\right)=3$ if $n \geq 3$ is odd, $\chi^{\prime}\left(C_{n}\right)=2$ if $n \geq 2$ is even. $\chi^{\prime}\left(W_{n}\right)=n-1$ for all $n \geq 4 . \chi^{\prime}\left(K_{m, n}\right)=\max \{m, n\}$.

Section 5.9
2. $\bar{\chi}^{\prime}(G)=8$. 5. $\bar{\chi}^{\prime}\left(C_{n}\right)=1, \bar{\chi}^{\prime}\left(W_{n}\right)=n-1$. 6. For Petersen graph $\bar{\chi}^{\prime}=7$, for cube $\bar{\chi}^{\prime}=6$, and for prism $\bar{\chi}^{\prime}=5$.

Chapter 6
Section 6.1
2. Connect each pair of such vertices by an edge.

Section 6.2

1. $K_{n}: n \geq 3 ; K_{m, n}: m=n ; W_{n}: n \geq 4$. 2. Prism and cube - yes; Petersen graph - not. 3. Yes.

Section 6.3

1. 8. 4. Add a new source and connect it with outcoming arcs to all sources; add a new sink and connect it with incoming arcs from all sinks.

Chapter 7
Section 7.1

1. $n\left(\mathcal{H}_{1}\right)=6, m\left(\mathcal{H}_{1}\right)=5 ; n\left(\mathcal{H}_{2}\right)=6, m\left(\mathcal{H}_{2}\right)=11$. 2. Two in $\mathcal{H}_{1}$, seven in $\mathcal{H}_{2}$. 3. None. 4. None. 9. $\Delta\left(\mathcal{H}_{1}\right)=3, \Delta\left(\mathcal{H}_{2}\right)=5$. 10. None. 11. None. 12. $r\left(\mathcal{H}_{1}\right)=3 ; r\left(\mathcal{H}_{2}\right)=4$. 13. $\mathcal{H}_{1}$ : one isolated vertex, no pendant vertices; $\mathcal{H}_{2}$ : no isolated and no pendant vertices. 14. $\mathcal{H}_{1}$ : one singleton, no empty edges; $\mathcal{H}_{2}$ : no singletons and no empty edges.

Section 7.2

1. In $\mathcal{H}: N(1)=\{2,4\}, N(2)=\{1,3,4,5\}, N(3)=\{2,4,5\}, N(4)=\{1,2,3,5\}$, $N(5)=\{2,3,4\}, N(6)=\emptyset$; in $\mathcal{H}^{*}: N\left(d_{1}\right)=\left\{d_{2}, d_{3}\right\}, N\left(d_{2}\right)=\left\{d_{1}, d_{3}, d_{4}\right\}, N\left(d_{3}\right)=$ $\left\{d_{1}, d_{2}, d_{4}, d_{5}\right\}, N\left(d_{4}\right)=\left\{d_{2}, d_{3}, d_{5}\right\}, N\left(d_{5}\right)=\left\{d_{3}, d_{4}\right\}$. 3. $r(\mathcal{H})=r\left(\mathcal{H}^{*}\right)=3.7 . L(G)=$ $\{\{1,5\},\{1,2\},\{2,3\},\{2,4\},\{4,5\}\} ; L\left(G^{*}\right)=\{\{a, b\},\{b, c, d\},\{c\},\{d, e\},\{a, e\}\} .9 . E_{n}^{*}$ consists of $n$ empty edges.

Section 7.3
4. $L\left(K_{4}^{3}\right)=\{\{1,2,3\},\{1,3,4\},\{2,3,4\},\{1,2,4\}\}$. 6. When order of the vertices is the same under the isomorphism.

Section 7.4
2. $1 \rightarrow 7 \rightarrow 11 \rightarrow 6$. 10. $\mathcal{H}^{*}$ is the Petersen graph.

Section 7.5
4. For example, $S=\{3,4,5,6,7,8,10,11,13,14\}$. 5. $\alpha(\mathcal{H})=10$. 7. For example, $T=\{1,2,9,12,15\}$. 8. $\tau(\mathcal{H})=5$. 9. For example, $\mathcal{D}^{\prime}=\{\{6,11,15\}$, $\{9,13,14\},\{1,3,7\},\{2,8,4\}\} . \mathbf{1 0} . \boldsymbol{v}(\mathcal{H})=4$. 11. $\boldsymbol{\rho}(\mathcal{H})=6$.

Section 7.6
3. Since bipartite graphs do not contain triangles, every intersecting family is a star. 4. Petersen graph does not have triangles. 7. Cube does not have triangles, while prism does.

Chapter 8
Section 8.1
2. 3rd, 4th and 5th. 3. 3rd, 4th and 5th. 4. 2nd, 3rd, 4th and 5th. 5. 3rd, 4th and 5th. 8. 3rd, 4th and 5th.

Section 8.2
3. $\tau\left(\mathcal{H}_{1}\right)=2, \alpha\left(\mathcal{H}_{1}\right)=4, \nu\left(\mathcal{H}_{1}\right)=2 ; \tau\left(\mathcal{H}_{2}\right)=3, \alpha\left(\mathcal{H}_{2}\right)=5, \nu\left(\mathcal{H}_{2}\right)=3$.

Section 8.3
5. $\wedge\left(\mathcal{H}_{1}\right)=1, \wedge\left(\mathcal{H}_{2}\right)=0$.

Chapter 9
Section 9.1

1. $K_{n}: n=1,2 ; K_{m, n}: m, n \geq 1 ; W_{n}$ : none; prism: no; cube: yes; Petersen graph: no. 2. Graphs without cycles of length $\geq 3$. 3. $\mathcal{H}=(X, \mathcal{D})$ with $X=\{1,2,3,4\}$ and $\mathcal{D}=\{\{1,2,3\},\{1,2,4\},\{2,3,4\}\}$. 4. $\mathcal{H}=(X, \mathcal{D})$ with $X=\{1,2,3\}$ and $\mathcal{D}=\{\{1,2,3\}$, $\{1,2\},\{2,3\},\{1,3\}\}$.

Section 9.2

1. Paths $P_{n}, n \geq 1$. 2. In any linear ordering of the vertices of $C_{n}, n \geq 3$, there is always an edge which is not an interval in the ordering. 3. $\mathcal{H}=(X, \mathcal{D})$ with $X=\{1,2,3,4\}, \mathcal{D}=$ $\{\{1,4\},\{2,4\},\{3,4\}\}$. 4. $\mathcal{H}=(X, \mathcal{D})$ with $X=\{1,2,3,4\}, \mathcal{D}=\{\{1,4\},\{2,4\},\{3,4\}\}$. 5. $\mathcal{H}=(X, \mathcal{D})$ with $X=\{1,2,3,4\}, \mathcal{D}=\{\{1,4\},\{2,4\},\{3,4\}\}$.

Section 9.3
2. $\mathcal{H}_{1}$ : not because it is not Helly; $\mathcal{H}_{2}$ : not because $L\left(\mathcal{H}_{2}\right)=C_{5}$ which is not perfect. 3. None. 4. $\chi^{\prime}\left(\mathcal{H}_{1}\right)=3 ; \chi^{\prime}\left(\mathcal{H}_{2}\right)=3$. 5. None.

Section 9.4
2. $\mathcal{H}_{1}$.

Chapter 10
Section 10.1

1. $\chi(\mathcal{H})=2$. 2. $\alpha(\mathcal{H})=6 ; \tau(\mathcal{H})=2$. 3. $\gamma(\mathcal{H})=4.5$. $\wedge(\mathcal{H})=0$. 6. No.

Section 10.2
2. $M(\mathcal{H})=2, \chi(\mathcal{H}) \geq 3$. 2. $\chi(\mathcal{H})=3$.

Section 10.3
2. $\chi(\mathcal{H})=2, \bar{\chi}(\mathcal{H})=3$. 3. 3. 4. $\chi\left(\mathcal{H}_{\mathcal{C}}\right)=1, \bar{\chi}\left(\mathcal{H}_{\mathcal{C}}\right)=3 ; \chi\left(\mathcal{H}_{\mathcal{D}}\right)=2, \bar{\chi}\left(\mathcal{H}_{\mathcal{D}}\right)=5$.

Section 10.4
2. 0. 3. $\bar{\chi}(\mathcal{H}) \geq 3$. 4. $\bar{\chi}(\mathcal{H})=3$. 5. Because the resistance $O(\mathcal{H})=0$.

Section 10.5

1. $P\left(\mathcal{H}_{1}, \lambda\right)=3 \lambda^{(3)}+6 \lambda^{(2)}, R\left(\mathcal{H}_{1}\right)=(0,6,3,0) ; P\left(\mathcal{H}_{2}, \lambda\right)=\lambda^{(2)}, R\left(\mathcal{H}_{2}\right)=(0,1,0,0)$.

Section 10.6

1. $\chi\left(\mathcal{H}_{\mathcal{D}}\right)=3, \bar{\chi}\left(\mathcal{H}_{C}\right)=3$.

Section 10.7
4. Yes. 5. Yes.

Section 10.8

1. $\alpha_{\mathcal{C}}\left(\mathcal{H}_{1}\right)=3, \bar{\chi}\left(\mathcal{H}_{1}\right)=3 ; \alpha_{\mathcal{C}}\left(\mathcal{H}_{2}\right)=3, \bar{\chi}\left(\mathcal{H}_{2}\right)=3$. 2. $\mathcal{H}_{1}$ is perfect, $\mathcal{H}_{2}$ is not. 3. $\tau_{2}\left(\mathcal{H}_{1}\right)=2, \tau_{2}\left(\mathcal{H}_{2}\right)=3$.

Section 10.9

1. $S\left(\mathcal{H}_{\mathcal{C}}\right)=\{1,2,3,4,5,6\}, S\left(\mathcal{H}_{\mathcal{D}}\right)=\{2,3,4,5,6,7,8\}$. 3. $S(\mathcal{H})=\{2,3,4,5\}$.

Section 10.10
2. No.

### 12.4. Glossary of Additional Concepts

This glossary contains informal definitions of additional concepts that are most often used in the literature.

- Acyclic graph: graph without cycles
- Acyclic orientation: replacing edges by arcs which produces no directed cycles
- Almost always true: a property which has asymptotic (as $n \rightarrow \infty$ ) probability 1

- Antihole: a subgraph induced by $\overline{C_{k}}$
- Automorphism: a permutation of the vertices that keeps the adjacency
- Binary tree: a tree with a root in which every non-pendant vertex has at most two neighbors further from the root
- Bipartite Ramsey number: given a bipartite graph $G$, the minimum $n$ such that any 2-coloring of the edges of $K_{n, n}$ produces a monochromatic copy of $G$
- Block: maximal 2-connected subgraph
- Block designs: also known as BIBDs (Balanced Incomplete Block Designs), are the $k$-uniform hypergraphs with vertices called points, edges called blocks, such that every point is contained in exactly r blocks, any subset of points of a given size is contained in exactly $\lambda$ blocks
- Cactus: graph in which no two cycles share an edge
- Chinese Postman Problem: to find a shortest closed walk passing through each edge of a weighted graph
- $k$-choosable graph: when for any lists of colors of length $k$ assigned to vertices, there exists a proper list coloring
- Claw: graph $K_{1,3}$
- Cograph: graph with no induced path $P_{4}$
- Color-critical: a graph for which every proper subgraph has the smaller chromatic number (index)
- $(n, k, \lambda)$-configuration: a $k$-uniform hypergraph of order $n$ such that every pair of vertices is contained in precisely $\lambda$ edges
- Density: ratio $m(G) / n(G)$
- Dominating set: a subset $S$ of vertices in a graph such that every vertex not in $S$ has a neighbor from $S$
- Domination number: the size of a smallest dominating set
- Eigenvalue of a graph: eigenvalue of the adjacency matrix
- Extremal combinatorics: study of the smallest (largest) number of edges which an $r$-uniform hypergraph of order $n$ can have provided that some given property holds
- Fano plane: Steiner Triple System STS(7), or Steiner System S(2,3,7)
- Finite projective plane of rank $r$ : a hypergraph $\mathcal{H}=(X, \mathcal{D})$ with $|X|=|\mathcal{D}|=r^{2}-r+$ 1, vertices called points, edges called planes, such that every point belongs to exactly $r$ lines, every line contains exactly $r$ points, any two distinct points are on precisely one line, and any two distinct lines have precisely one point in common

- Genus of a graph: the minimum genus of a surface on which the graph can be embedded without crossings of edges
- Genus of a surface: the number of handles added to the sphere
- Girth: the length of a shortest cycle
- Greedy algorithm: an algorithm for finding an optimal solution of a problem that takes the best possible choice at each step; it does not guarantee the optimal solution for the whole problem
- Hereditary class: a class of graphs such that any induced subgraph of any graph from the class is also in the class
- Hole: induced subgraph isomorphic to $C_{k}, k \geq 4$
- Homomorphism: a map $f: V\left(G_{1}\right) \rightarrow V\left(G_{2}\right)$ that keeps adjacency
- Hypergraph removal lemma: for a given $r$-uniform hypergraph $\mathcal{H}$, in any larger $r$ uniform hypergraph containing a bounded number of copies of $\mathcal{H}$, one can remove bounded number of edges to construct a hypergraph with no copy of $\mathcal{H}$
- List coloring: proper vertex coloring of a graph in which every vertex has a list of admissible colors
- Matroid: discrete hereditary structure generalizing linear independence in vector spaces; it has many equivalent formulations; for example, graphic matroid for a graph $G$ consists of edges as "elements" and subsets of edges not forming any cycle as "bases"
- Non-orientable surface: a surface which does not have two different sides, for example like Möbius strip
- Orientable surface: a surface with two different sides, for example like sphere or torus
- Outerplanar graph: a planar graph that can be embedded in the plane with all the vertices on the unbounded face
- Partition of a set: dividing a set into a number of nonempty subsets
- Pigeonhole principle: if $n$ items are put into $m$ pigeonholes and $n>m$, then at least one pigeonhole contains more than one item; or, if $n$ vertices are colored with $m$ colors and $n>m$, then there are at least two vertices of the same color
- Probabilistic graph theory: the study of existence of graphs with some properties using probability theory; usually, the graphs are not constructed, but one prove that with positive probability they exist
- Ramsey number $R(p, q)$ : the minimum $n$ such that any 2-coloring of the edges of $K_{n}$ produces either a monochromatic copy of $K_{p}$ or a monochromatic copy of $K_{q}$; for example, $R(3,3)=6$

- Random graph: a graph in which every pair of vertices forms an edge with probability p
- Regularity Lemma (also known as Szemerédi regularity lemma): every graph having sufficiently many vertices and edges can be approximated by some composition of almost regular parts; in other words, the vertex set can be partitioned into a number of almost equal in size subsets having special properties with sufficiently small set of leftover vertices; it has a generalization to $r$-uniform hypergraphs
- Satisfiability problem: the problem of finding truth values for logical variables such that some logical formula becomes true
- Spectrum of a graph: the set of eigenvalues with their multiplicity
- Steiner Quadruple System $S Q S(v)$ : Steiner System $S(3,4, v)$
- Steiner System $S(t, k, v)$ : a $k$-uniform hypergraph $\mathcal{H}=(X, \mathcal{B})$ with $|X|=v$, hyperedges called blocks, such that any $t$ distinct vertices appear together in precisely one block
- Steiner Triple System STS(v): Steiner System S(2,3,v)
- System of distinct representatives: for a collection of sets, a choice of one element from each set such that all chosen elements are distinct
- Thickness of a graph $G$ : minimum number of planar graphs into which $G$ can be split
- Topological graph theory: the study of graph drawings on different surfaces
- Torus: the orientable surface of genus 1; equivalently, a sphere with added handle
- Total coloring: coloring of both vertices and edges so that no adjacent and no incident elements have the same color
- Tournament: digraph obtained from $K_{n}$ by replacing edges with arcs (orientation)
- Transitive digraph: if there are arcs $(x, y)$ and $(y, z)$, then there is arc $(x, z)$
- Transversal hypergraph $\operatorname{Tr} \mathcal{H}$ : for a given hypergraph $\mathcal{H}=(X, \mathcal{E}), \operatorname{Tr} \mathcal{H}=(X, \mathcal{D})$ where $\mathcal{D}$ is the family of all minimal transversals of $\mathcal{H}$
- Traveling Salesman Problem: to find a shortest spanning cycle in a weighted graph
- Traversal: visiting all the vertices or edges of a graph in a special way
- Turán graph: the complete multipartite graph with all parts of almost the same size (different by at most 1)
- Turán number $T(n, p, r)$ : the smallest number of edges in an $r$-uniform hypergraph on $n$ vertices such that every set of vertices of cardinality $p$ contains at least one edge
- Turán's theorem: for a given $n$, the Tuŕan $r$-partite graph contains the maximum number of edges and does not contain $K_{r+1}$

## References

[1] C. Berge. Graphs and Hypergraphs. North-Holland, 1973.
[2] C. Berge. Hypergraphs: combinatorics of finite sets. North-Holland, 1989.
[3] J.A. Bondy and U.S.R Murty. Graph Theory. Springer, 2008.
[4] G. Chartrand and P. Zhang. Introduction to Graph Theory. Walter Rudin Student Series in Advanced Mathematics, 2004.
[5] R. Diestel. Graph Theory. Springer, 2006.
[6] V. Voloshin. Coloring Mixed Hypergraphs: theory, allgorithms and applications. AMS, Providence, 2002.
[7] D. B. West. Introduction to Graph Theory. Prentice Hall, 2001.
[8] A. A. Zykov. Hypergraphs. Uspekhi Mat. Nauk 29 (1974), 89-154 (in Russian).

## Index

$(x, y)$-invertor, 228
$(x, y)$-path, 18, 144
$(x, y)$-separator, 34
$(\mathcal{H})_{2}$, 2-section, 154
$B(\mathcal{H})$, bipartite representation, 140
$E(G)$, edge set, 7
$E(x)$, set of edges containing vertex $x, 7$
$G$, graph, 6
$L(G)$, line graph, 112
$L(\mathcal{H})$, line graph, 154
$N_{\infty}(x)$, farthest set of vertices, 41
$O(g(n))$, big-oh, 269
$P(G, \lambda)$, chromatic polynomial, 80
$P(\mathcal{H}, \lambda)$, chromatic polynomial of a hypergraph, 204
$R(G)$, chromatic spectrum, 81
$R(\mathcal{H})$, chromatic spectrum, 203
$V(G)$, vertex set, 7
$V(\mathcal{H})$, vertex set, 135
$[\mathcal{H}]_{2}$, generalized 2-section, 174
$\Delta(G)$, maximum degree, 6, 113
$\Delta(\mathcal{H})$, maximum degree of hypergraph, 136
$\Lambda(G)$, cyclomatic number, 40
$\Lambda(\mathcal{H}, T)$, generalized cyclomatic number, 174
$\Lambda(\mathcal{H})$, cyclomatic number of a hypergraph, 179
$\alpha(G)$, stability number, 31
$\alpha(\mathcal{H})$, stability (independence) number, 151
$\boldsymbol{\alpha}_{c}(\mathcal{H}), \mathcal{C}$-stability number, 236
$\bar{\chi}(\mathcal{H})$, upper chromatic number, 203
$\bar{\chi}^{\prime}(G)$, upper chromatic index, 116
$\chi^{\prime}(G)$, chromatic index, 112
$\chi^{\prime}(\mathcal{H})$, chromatic index, 185
$\chi(G)$, chromatic number, 80
$\chi(\mathcal{H})$, lower chromatic number, 203
$\chi(\mathcal{H})$, chromatic number, 193
$\kappa(G)$, connectivity, 34
$\lambda^{(n)}$, falling factorial, 84
$\mu(G)$, multiplicity of a graph, 115
$\nu(G)$, maximum size of a matching, 32
$\omega(G)$, clique number, 31
$\tau(G)$, transversal number, 31
$\tau_{2}\left(\mathcal{H}_{C}\right)$, bitransversal number, 238
$\theta(G)$, clique cover number, 56
$k$-connected graph, 34
k-factor, 32
$k$-factorization, 32
$k$-regular graph, 21
$k$-regular hypergraph, 136
$l(\mathcal{H}, T)$, number of loops of $\mathcal{H}$ not in forest $T, 174$
$m=m(\mathcal{H})$, the number of edges, 136
$n=n(\mathcal{H})$, order of $\mathcal{H}$, the number of vertices, 136
$r$-uniform hypergraph, 136, 206
$r_{i}(G)$, number of feasible partitions, 81
$r_{i}(\mathcal{H})$, number of feasible partitions, 203
$w(T)$, weight of a tree, 43
$\mathcal{C}$-bistar, 238
$\mathcal{C}$-clearing, 213
$\mathcal{C}$-hypergraph, 204
$\mathcal{C}$-monostar, 238
$\mathcal{C}$-perfection, perfection, 237
$\mathcal{C}$-stability number, $\alpha_{c}(\mathcal{H}), 236$
$\mathcal{C}$-stable set, 206
$\mathcal{D}$-clearing, 213
$\mathcal{D}$-graph, 204
$\mathcal{D}$-hypergraph, 204
$\mathcal{D}(\mathcal{H})$, edge set, 135
$\mathcal{D}(x)$, set of edges containing vertex $x$, 136
$\mathcal{H}$, hypergraph, 135
$\mathcal{H}^{*}$, dual hypergraph, 140
$\mathcal{H}_{Y}$, subhypergraph induced by $Y$, 151
2-colorable hypergraph, 145
2-section, $(\mathcal{H})_{2}, 154$
acyclic graph, 275
acyclic orientation, 275
adjacency list, 12
adjacency matrix, 13, 143
adjacent edges, 7
adjacent edges in hypergraph, 136
adjacent vertices, 6
adjacent vertices in hypergraph, 136
algorithm, 269
almost always, 275
antihole, 276
applications, 8, 17, 137, 263, 264
arc, 16
automorphism, 276
back edge, 46
backtracking, 46
balanced cycle, 181
balanced hypergraph, 181
Berge graph, 111
bi-chromatic hypergraph, 145
bi-conformal hypergraph, 159
bi-edge, 206
bi-Helly hypergraph, 240
bidegree, 208
bihypergraph, 206
binary Ramsey number, 276
binary tree, 276
bipartite graph, 21
bipartite hypergraph, 145
bipartite representation, $B(\mathcal{H})$, 140
bistar, 207, 221
bitransversal number, $\mathbf{\tau}_{2}\left(\mathcal{H}_{C}\right), 238$
bitriangulation, 254
block, 276
block design, 276
blocking set, 152
breadth-first search algorithm, 45
bridge, 36
broken chromatic spectrum, 82, 244
Brooks' theorem, 82
cactus, 276
capacity of a cut, 127
capacity of an arc, 127
cardinality of edge, 136
cell, 81
center, 41
Chinese Postman Problem, 276
choosable graph, 276
chord of a cycle, 51
chord with respect to the spanning tree, 40
chordal graph, 51
chordal hypergraph, 163
chromatic index, $\chi^{\prime}(\mathcal{H}), 185$
chromatic index, $\chi^{\prime}(G)$, 112
chromatic number, $\chi(G), 80$
chromatic number, $\chi(\mathcal{H}), 193$
chromatic polynomial of a hypergraph, $P(\mathcal{H}, \lambda), 204$
chromatic polynomial, $P(G, \lambda), 80$
chromatic spectrum, $R(\mathcal{H})$, 203
chromatic spectrum, $R(G)$, 81
class 1 graphs, 115
class 2 graphs, 115
class NP, 270
class P, 270
clearing, 148
clique, 30
clique cover number, $\theta(G)$, 56
clique covering, 56
clique hypergraph, 166
clique number, $\omega(G)$, 30
closed Jordan curve, 67
closed walk, 123
co-simplicial vertex, 62
cograph, 276
color class, 81, 193, 203
color-critical graph, 276
colorability problem, 219
colorable mixed hypergraph, 202
coloring, 80, 202
complement of a graph, 28
complete $(l, m)$-uniform mixed hypergraph, 223
complete $r$-partite hypergraph, 145
complete $r$-uniform hypergraph, 144
complete bipartite graph, 21
complete graph, 20
complete hypergraph, 144
complete mixed hypertree, 232
complexity, 269
computation of cyclomatic number, algorithm, 179
configuration, 107, 276
conformal hypergraph, 156
connected component, 19, 144
connected graph, 18
connected hypergraph, 144
connected mixed hypergraph, 206
connected region, 67
connection-contraction algorithm, 84
connectivity, $\mathrm{K}(G)$, 34
constant complexity, 270
continuous chromatic spectrum, 82, 244
contractible graph, 28
contraction, 214
contraction of a hyperedge, 149
contraction of an edge, 27
copy of a vertex, 109
covering, 153
crossing, 67
crossing number, 68
cube, 12, 22
cubic graph, 21
cut, 127
cycle, 19, 30
cycle in hypergraph, 144
cycloid, 238
cyclomatic number of a hypergraph, $\Lambda(\mathcal{H}), 179$
cyclomatic number, $\Lambda(G)$, 40
deadlock, 211
degree of a vertex, 6
degree of edge, 136
degree sequence, 7
deletion of a vertex, 25
deletion of an edge, 26
density, 276
depth-first algorithm, 46
derived subgraph, 35
diagonal of a cycle, 51
diameter, 41
diametral path, 41
different proper colorings, 203
digraph, 16
directed graph, 16
disconnected graph, 18
disconnection-contraction algorithm, 90
disjoint edges, 7
disjoint vertices, 6
distance, 41
dominating set, 276
domination number, 276
doubling, 249
drawing dual hypergraph, 140
dual graph to a plane graph, 77
dual hypergraph, $\mathcal{H}^{*}$, 140
dual König property, 153
eccentricity , 41
eclipse, 240
edge, 5
edge $k$-colorable graph, 112
edge coloring, 112, 116
edge list, 14, 142
edge-coloring property, 185
edge-critical hypergraph, 196
edge-cut, 36
edge-intersection in the plane, 67
edge-separator, 36
eigenvalue of a graph, 276
elementary cycle, 40
elementary shifting, 247
elimination, 213
embedding of hypergraph, 188
empty edge, 136
empty graph, 18
equitable coloring, 195
Euler's formula for hypergraphs, 188
Eulerian graph, 123

Eulerian trail, 123
even cycle, 19
evidently uncolorable $\mathcal{C}$-edge, 205
evidently uncolorable $\mathcal{D}$-edge, 206
exponential-time, 270
extremal combinatorics, 276
face, 188
face of a plane graph, 67
factor, 32
factorial complexity, 270
falling factorial, $\lambda^{(n)}$, 84
family, 6
Fano plane, 276
feasible partition, 81, 193, 203
feasible set, 244
finding maximum stable set in chordal graph, algorithm, 55
finding minimum transversal and maximum matching in a hypertree, algorithm, 172
finite projective plane, 276
flow conservation law, 127
flow in an arc, 127
forest, 21
four color problem, 79
fragment, 75
friendship graph, 12
fundamental equality, 204
fundamental relation, 86
gap in chromatic spectrum, 244
gap-free chromatic spectrum, 82
generalized 2-section, $[\mathcal{H}]_{2}, 174$
generalized cyclomatic number, $\Lambda(\mathcal{H}, T), 174$
genus of a graph, 277
genus of a surface, 277
girth, 277
good coloring, 195
Grötzsch graph, 109
graph, 6
graph applications, 8, 17
graph minor, 32
graph perfection vs hypergraph perfection, 236
greedy $\mathcal{C}$-hypergraph coloring, algorithm, 208
greedy algorithm, 277
greedy coloring, 96
greedy hypergraph coloring, 198
Hadwiger number, 28
Hall's theorem, 47
Hamiltonian cycle, 125
Hamiltonian graph, 125
Helly property, 155
hereditary class, 277
hole, 277
homeomorphic graphs, 73
homomorphism, 277
host graph, 161
hyper-pendant vertex, 163, 168
hyperedge, 136
hypergraph, 135
hypergraph applications, 136, 263, 264
hypergraph minor, 153
hypergraph removal lemma, 277
hypertree, 161
hypertree recognition algorithm, 170
I-regular coloring, 195
incidence matrix, 14, 139
incident vertices and edges, 7, 136
included hyperedge, 136, 213
including hyperedge, 213
incoming arc, 127
independent (stable) set, 31
induced subgraph, 30
induced subhypergraph, 151, 206
induction, 267
inflation, 244
initial vertex, 16
intersecting family, 155
intersection graph, 154
interval graph, 11, 184
interval hypergraph, 183
intractable problem, 270
isolated vertex, 15, 136
isomorphic graphs, 23
isomorphic hypergraphs, 136, 145
isomorphism, 23
join, 247
Jordan curve, 67
König property, 152
König's theorem, 45, 48
Kempe chain, 107, 209
Kempe's proof, 104
Kruskal's algorithm for minimum spanning tree, 43
Kuratowski's theorem, 74
latticed graph, 62
leaf, 41
length of a path, 18
length of the cycle, 19
length of the path/cycle, 144
line graph, $L(\mathcal{H})$, 154
line graph, $L(G)$, 112
linear-time, 270
list coloring, 263, 277
logarithmic complexity, 270
loop, 15
loop in hypergraph, 136
lower chromatic number, $\chi(\mathcal{H})$, 203
matching, 32, 152
matching covering, 47
matroid, 277
maximal (minimal) versus maximum (minimum), 31
maximal by inclusion complete subgraph, 30
maximal clique, 30
maximal colorable subhypergraph, 220
maximal coloring, 120
maximal embedding, 189
maximal planar graph, 76
maximum degree of hypergraph, $\Delta(\mathcal{H})$, 136
maximum degree, $\Delta, 6$
Menger's theorem, 37
Meyniel graph, 111
minimal separator, 34
minimal uncolorable mixed hypergraph, 220
minimum (maximum) spanning tree problem, 43
minimum cut, 127
mixed hypergraph, 202
mixed hypertree, 225
mixed multigraph, 253
monochromatic component, 208
monochromatic subset, 203
monodegree, 197
monostar, 197
multi-forest, 174
multigraph, 15
multiple edges, 15
multiple hyperedge, 136
multiplicity, 15
multiplicity of a graph, $\mu(G)$, 115
Mycielski's construction, 109
neighbor, 7
neighborhood, 7
neighborhood in hypergraph, 136
neighborhood of a subset, 46
network, 127
network flow, 127
node, 127
non-orientable surface, 277
normal hypergraph, 185
NP-complete problems, 270
odd cycle, 19
online coloring, 96
orientable surface, 277
originality of vertex, 208
outcoming arc, 127
outerplanar graph, 277
parallel edges, 15
partial subhypergraph, 151
partition, 277
path, 18
pendant vertex, 41, 136, 163, 174
perfect elimination ordering, 54
perfect graph, 110
perfect matching, 32, 152
Petersen graph, 22
pigeonhole principle, 277
planar graph, 67
planar hypergraph, 187
planar mixed hypergraph, 254
planarity testing algorithm, 74
plane embedding, 67
plane graph, 67
plane triangulation, 76
polychromatic subset, 203
polynomial-time, 270
prism, 22
probabilistic graph theory, 277
proper $\lambda$-coloring, 80, 193
proper coloring, 80, 202
proper edge $\lambda$-coloring, 112
quasi-triangulated graph, 62
radius, 41
Ramsey number, 277
random graph, 278
rank of hypergraph, $r(\mathcal{H})$, 136
reduced mixed hypergraph, 218
reducible configuration, 107
redundant edge, 217
refinement, 255
regular graph, 21
regular hypergraph, 136
regularity lemma, 278
resistance of $\mathcal{C}$-hypergraph, 208
root in a tree, 46
satisfiability problem, 278
satisfied vertex, 117
saturated arc, 127
self-dual hypergraph, 159
separator, 34
set-system, 135
simple cycle, 30
simple graph, 16
simple hypergraph, 136
simple invertor, 229
simplicial decomposition, 54
simplicial elimination ordering, 54
simplicial vertex, 51
singleton, 136
sink, 127
size of a face, 67
size of edge, 136
size of face, 188
source, 127
spanning subgraph, 31
spanning tree, 32
spectrum of a graph, 278
Sperner family, 136
splitting, 214
splitting-contraction algorithm, 214
stability (independence) number, $\alpha(\mathcal{H})$, 151
stability (independence) number, $\alpha(G)$, 31
stable (independent) set, 31, 151
star, 155
Steiner Quadruple System, 278
Steiner System, 278
Steiner Triple System, 278
stereographic projection, 70
Stirling numbers of the first kind, 90
Stirling numbers of the second kind, 90
strict $i$-coloring, 81, 203
strict edge coloring, 116
strong chromatic number, 194
strong coloring, 194
strong deletion of a hyperedge, 148
strong deletion of a vertex, 26
strong deletion of an edge, 26
strong deletion of vertex, 146
strong perfect graph conjecture, 111
strongly independent (stable) set, 152
strongly perfect graph, 111
subgraph, 29
subhypergraph, 151
symmetric matrix, 13
System of distinct representatives, 278
Szekeres-Wilf number, 57
Szemerédi regularity lemma, 278
terminal vertex, 16
thickness of a graph, 278
topological graph theory, 278
torus, 278
total coloring, 278
totally balanced hypergraph, 181
touching graph, 231
tournament, 278
tractable problem, 270
trail, 123
transitive graph, 278
transposition of a matrix, 13
transversal, 31, 152
transversal hypergraph, 278
transversal number, $\tau(G), 31$
transversal vertex, 168
Traveling Salesman Problem, 278
traversal, 123, 125, 278
tree, 20
triangle, 19
trivial graph, 41
Turán graph, 278
Turán number, 278
Turán's theorem, 278
twin vertex, 168
uc, 227
uc-orderable mixed hypergraph, 233
uc-ordering algorithm, 233
unavoidable configuration, 107
unbounded face, 67
uncolorable mixed hypergraph, 202
underlying hypergraph, 206
undirected graph, 16
uniform coloring, 195
uniform hypergraph, 136
uniquely colorable mixed hypergraph, 227
universal vertex, 109
unsaturated arc, 127
upper chromatic index, $\bar{\chi}^{\prime}(G), 116$
upper chromatic number, $\bar{\chi}(\mathcal{H})$, 203
value of the network flow, 127
vertex, 5, 136
vertex cover, 31
vertex cut, 34
Vizing's theorem, 113
walk, 123
weak coloring, 193
weak deletion of a hyperedge, 148
weak deletion of a vertex, 26
weak deletion of vertex, 147
weak perfect graph conjecture, 110
weakly chordal graph, 111
weakly cyclic vertex, 62
weight of a multi-forest, $w(T)$, 174
weight of a tree, $w(T), 43$
weight of an edge, 43
weighted graph, 43
wheel, 20
Whitney's theorem, 90


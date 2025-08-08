# A constructive Characterisation of Interval Graphs

This repository stores the Python modules accompanying a forthcoming paper titled *"A constructive characterisation of interval graphs"*.

In that work, we propose an iterative procedure for constructing interval graphs. As a byproduct, we derived various results. The purpose of this repository is to provide computational implementations for testing and illustrating those results. 

Each module in [main/src](https://github.com/n-chikh/A-constructive-characterisation-of-interval-graphs/tree/main/src) corresponds to a specific a definition or result in the paper:

| Module      | Definition/result | Description |
| ----------- | ----------- | ----------- |
| proposition1.py      | Proposition 1       | 1. The function `N_construction` construct an interval graph using its dominance list. <br> 2. `dominance_lists` generates a list of all dominance lists of lenght $n$. |
| proposition3.py   | Proposition 3       | `nbr_cc` returns: the number of connected components of an interval graph; and the the index of the leftmost vertex in each connected component. |
| definition7_proposition4.py   | Definition 7 <br> Proposition 4       | 1. `i_transpose` returns the $(i-1,i)$-transpose of a dominance list. <br> 2. `check_itranspose` checks if two dominance lists are $(i-1,i)$-transposes of each other. <br> 3. `iso_transpose` checks if any two dominance lists are $(i-1,i)$-transposes corresponding to two isomorphic graphs. |
| proposition5.py   | Proposition 5       | `chromatic_poly` computes the chromatic polynomial of an interval graph.|
| corollary1_corollary2.py   | Corallary 1 <br> Corollary 2       | The functions `p` and `t` compute the numbers $p_{n,m}$ and $t_{n,m}$ respectively. | 
| proposition7.py   | Proposition 7       | 1. `phi` maps a dominance list to its corresponding permutation; `inv_phi` does the inverse mapping. <br> 2. `cyclic` returns the cyclic form of a permutation. | 
| table2.py   | Table 2      | 1. `gen_Nconstructions` generates all $\mathcal{N}$-constructions with $n$ vertices and $m$ edges. <br> 2. `iso_Nconstructions` generates all (non isomorphic) interval graphs with $n$ vertices and $m$ edges. <br> 3. `list_iso_Nconstructions` retrun the list of numbers $\widetilde{p}_{n,m}$, with fixed $n$. |

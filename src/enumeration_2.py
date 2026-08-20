'''Calculation of non isomorphic interval graphs in Concluding remarks'''


import networkx as nx
from src.N_procedure import *


'''The second function generates a list containing every (non isomorphic) 
    interval graph $G_{n}$ or $G_{n,m}$ 
'''
def iso_Nconstructions(n, L=None, m=None, C=False):
    '''Input: the number of vertices n and the number of edges m (optional).
       Output: a list that contains all interval graphs $G_{n}$
               or (if m is given) $G_{n,m}$'''    
    if L == None:
        L = gen_Nconstructions(n, m, c=C)
        
    L_distinct = [L[0]]
    for H in L[1:]:
        all_checked = 0
        for G in L_distinct:
            if (nx.vf2pp_is_isomorphic(G,H) == True):
                break
            else:
                all_checked += 1
        if (all_checked == len(L_distinct)):
            L_distinct.append(H)
    return L_distinct
    

'''This function gives a list that contains the numbers $p_{n,m}$,
    for a fixed $n$ 
'''
def list_iso_p(n):
    '''Input: the number of vertices n 
       Output: a list containing all $p_{n,m}$'''
    nbrs = [len(iso_Nconstructions(n, m=k)) for k in range(int(n*(n-1)/2)+1)]
    return nbrs

 
'''Module execution

'''
if __name__ == "__main__":
    import sys
    inp = int(sys.argv[1])
    print(list_iso_p(inp))

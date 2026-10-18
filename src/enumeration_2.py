'''Calculation of non isomorphic interval graphs discussed in the Concluding remarks

    Functions:
    iso_Nconstructions() -- Extract interval graphs from a list of N-constructions with n vertices
    and optionnally m edges; or from a any personalised list of N-constructions
'''

import networkx as nx
from src.N_procedure import *


def iso_Nconstructions(n, L=None, m=None, C=False):
    '''
    Args: 
        n: Number of vertices.
        m: Number of edges (optional).
        L: A list of N-constuctrions (optional); if None the list of all N-constructions
        with n vertices (and optionally m edges) is used.
    Returns: 
        A list of non isomorphic interval graphs of n vertices and, if precised, m edges.
    '''
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
    

def list_iso_p(n):
    '''
    Args: 
        n: Number of vertices.
    Returns: 
        A list of the numbers interval graphs with n vertices and m edges, m spanning from
        0 to n(n-1)/2.
    '''
    nbrs = [len(iso_Nconstructions(n, m=k)) for k in range(int(n*(n-1)/2)+1)]
    return nbrs

 
'''Module execution

'''
if __name__ == "__main__":
    import sys
    inp = int(sys.argv[1])
    print(list_iso_p(inp))

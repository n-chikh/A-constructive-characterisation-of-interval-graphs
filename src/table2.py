'''Calculation of p_{n,m} for a fixed n given in Table 2'''


import networkx as nx

'''The first function generates a list containing all the N-constructions
   $G_{n}$ or $G_{n,m}$ 
'''
def gen_Nconstructions(n,m=None):
    '''Input: the number of vertices n and (optionnaly) the number of edges m.
       Output: a list that contains all the N-constructions $G_{n}$
               or (if m is given) $G_{n,m}$'''
    dom_list = []
    dom = dominance_lists(n)
    g = []
    if m==None:
        for d in dom:
            G = N_graphe(d)
            g.append(G)
    else:
        for d in dom:
            if sum(d)==m:
                G = N_graphe(d)    
                g.append(G)           
    return g    


'''The second function generates a list containing every (non isomorphic) 
    interval graph $G_{n}$ or $G_{n,m}$ 
'''
def iso_Nconstructions(n, m=None):
    '''Input: the number of vertices n and (optionnaly) the number of edges m.
       Output: a list that contains all interval graphs $G_{n}$
               or (if m is given) $G_{n,m}$'''    
    L = gen_Nconstructions(n, m)
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
    

'''The thrid function gives a list that contains the numbers $p_{n,m}$,
    for a fixed $n$ 
'''
def list_iso_p(n):
    '''Input: the number of vertices n 
       Output: a list containing all $p_{n,m}$'''
    nbrs = [len(iso_Nconstructions(n, m=k)) for k in range(int(n*(n-1)/2)+1)]
    return nbrs
    

'''Duplicate of the homonymic function in proposition1.py
'''
def N_graphe(ld):
    G = nx.Graph()
    ik = 1
    for j in ld:
        G.add_node(ik)
        if j >= 1:
            for v in range(ik-1,ik-j-1,-1):
                G.add_edge(ik,v)
        ik = ik +1
    return G


'''Duplicate of the homonymic function in proposition1.py
'''
def dominance_lists(n):
    dom_list = []
    gd = [0 for k in range(n)]
    def gen_dominance_list(n,init=1):
        i = init
        if init<n:
            for j in range(i+1):
                gd[i]=j
                gen_dominance_list(n,i+1)
        else:
            dom_list.append(list(gd))
    gen_dominance_list(n)
    return dom_list
    
 
'''Module execution

'''
if __name__ == "__main__":
    import sys
    inp = int(sys.argv[1])
    print(list_iso_p(inp))

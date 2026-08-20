'''Implementation of the N-procedure'''


''' This first function implements the N-construction that constructs the
so-called N-constructions, that are constructed interval graphs (that are not non
isomorphic)
'''
import networkx as nx
import matplotlib.pyplot as plt

from src.connected_components import *


def N_construction(ld):
    '''Input: the dominance list of a constructed interval graph (N-construction) 
       Output: the corresponding networkx's graph'''
    G = nx.Graph()
    ik = 1
    for j in ld:
        G.add_node(ik)
        if j >= 1:
            for v in range(ik-1,ik-j-1,-1):
                G.add_edge(ik,v)
        ik = ik +1
    return G


''' The second function generates every dominance list of some lenght, 
i.e. the number of vertices of its corresponding N-construction.
'''
def dominance_lists(n, cc=False):
    '''Input: the number of vertices n
       Output: a list that stores the dominance list of every 
               constructed interval graph (N-construction) with n vertices'''
    dom_list = []
    gd = [0 for k in range(n)]
    
    '''That is the inner function that actually generates the dominance list
    The encapsulating function is meant to return the dominance lists'''
    def gen_dominance_list(n,init=1):
        i = init
        if init<n:
            for j in range(i+1):
                gd[i]=j
                gen_dominance_list(n,i+1)
        else:
            if cc == True: 
                if indices_cc(gd) == [0]:
                    dom_list.append(list(gd))
            else:
                dom_list.append(list(gd))
    gen_dominance_list(n)
    return dom_list


'''The third function generates a list containing all the N-constructions
   $G_{n}$ or $G_{n,m}$ 
'''
def gen_Nconstructions(n, L=None, m=None, c = False):
    '''Input: the number of vertices n and (optionnaly) the number of edges m.
       Output: a list that contains all the N-constructions $G_{n}$
               or (if m is given) $G_{n,m}$'''
    dom_list = []
    if L == None:
        dom = dominance_lists(n, cc=c)
    else:
        dom = L
    g = []
    if m==None:
        for d in dom:
            G = N_construction(d)
            g.append(G)
    else:
        for d in dom:
            if sum(d)==m:
                G = N_construction(d)    
                g.append(G)           
    return g    




'''Module execution
   (generate an image of the corresponding N-construction)
'''
if __name__ == "__main__":
    import sys
    inp = sys.argv[1]
    form_inp = map(int, inp.strip('[]').split(','))
    nx.draw(N_graphe(form_inp), with_labels=True)
    namegraph = 'interval graph ' + inp + '.png'
    plt.savefig(namegraph, dpi=400, format='png')

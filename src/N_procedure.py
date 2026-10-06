'''Implementation of the N-procedure.

Functions:
    N_construction() -- Constructs the N-construction corresponding to a dominance list.
    dominance_lists() -- Generates all the dominances lists of a given lenght.
    gen_Nconstructions -- Generates all the N-constructions of a given order.

'''
import networkx as nx
import matplotlib.pyplot as plt

from src.connected_components import *


def N_construction(ld):
    '''
    Args: 
        ld: Dominance list given as a list or array.
    Returns: 
        N-construction of ld as a networkx graph. 
    '''
    G = nx.Graph()
    ik = 1
    for j in ld:
        G.add_node(ik)
        if j >= 1:
            for v in range(ik-1,ik-j-1,-1):
                G.add_edge(ik,v)
        ik = ik +1
    return G


def dominance_lists(n, cc=False):
     '''
    Args: 
        n: An integer respresing the number of vertices.
    Returns: 
        List of all dominance lists with lenght n. 
    '''
    dom_list = []
    gd = [0 for k in range(n)]
    def gen_dominance_list(n,init=1):
    '''Inner function that actually generates the graphs'''
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


def gen_Nconstructions(n, L=None, m=None, c = False):
        '''
    Args: 
        n: Number of vertices of the graphs.
        L (optional): A list or array containing dominance lists.
        m (optional) Number of edges of the graphs
    Returns: 
        List of all N-constructions with n vertices. 
    '''
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

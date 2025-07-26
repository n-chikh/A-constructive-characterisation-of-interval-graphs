'''Implementation of Proposition 1'''


''' This first function implements the N-construction that constructs the
so-called N-constructions, that are constructed interval graphs (that are not non
isomorphic)
'''
import networkx as nx
import matplotlib.pyplot as plt
def N_graphe(ld):
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
i.e. the number of vertices of its corresponding graph.
'''
def dominance_lists(n):
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
            dom_list.append(list(gd))
    gen_dominance_list(N)
    return dom_list


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

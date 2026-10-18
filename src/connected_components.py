'''Implementation of the sufficient and necessary condition of connectedness

Functions:
    condition_dec() -- For a given vertex's index i, returns TRUE if the successive vertex is
    the first vertex of some connected compenent.
'''

def condition_dec(ld, i):
     '''
    Args: 
        ld: Dominance list given as a list or array.
        i: A vertex's index.
    Returns: 
        An ordered pair (True/False, i+1); True if the vertex v_{i} disconnects
        the graph, and False otherwise.
    '''
    ldt = list(ld[i:])
    n = len(ldt)
    exh = 0 
    cc = False
    isolating_vertex = 0   
    if (i !=0):
        for j in range(n):
            if ldt[j]<=j:
                exh += 1
        if exh==n:
            cc = True
            isolating_vertex = i+1
    else:
        for j in range(1,n):
            if ldt[j]<j:
                exh += 1
        if exh==n-1:
            cc = True
            isolating_vertex = i+1
    return cc, isolating_vertex
    

def indices_cc(ld):
    ''' Args:
            ld: dominance list given as a list or array.
        Returns:
            A list of the indices of vertexes that disconnect the graph, i.e. which are 
            the last vertex of every connected component.
    '''
    composantes = [0] + [ condition_dec(ld, k)[1] 
                        for k in range(len(ld)) 
                        if condition_dec(ld, k)[0] == True ]
    return composantes


def nbr_cc(LD):
    '''
    Args: 
        LD: Dominance list given as a list or array.
    Returns: 
        An ordered pair which contains the number of connected components and a list of the indices
        of the leading vertices of each connected component.
    '''
    components = 1
    listv = []
    for i in range(len(LD)):
        if condition_dec(LD,i)[1] != 0:
            components += condition_dec(LD,i)[0]
            listv.append(condition_dec(LD,i)[1])
    return components, listv


'''Module execution
'''
if __name__ == "__main__":
    import sys
    inp = map(int, sys.argv[1].strip('[]').split(','))
    print(nbr_cc(list(inp)))

'''Implementation of the sufficient and necessary condition of connectedness

Functions:
    condition_dec() -- For a given vertex's index i, return TRUE if the successive vertex is
    the first vertex of some connected compenent.
'''
def condition_dec(ld, i):
     '''
    Args: 
        ld: Dominance list given as a list or array.
        i: A vertex's index.
    Returns: 
        Return the ordered pair (True/False, i+1); True if the vertex v_{i} disconnects
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
    
''' This function gives a list of the first vertex of every connected component.
'''
def indices_cc(ld):
    composantes = [0] + [ condition_dec(ld, k)[1] 
                        for k in range(len(ld)) 
                        if condition_dec(ld, k)[0] == True ]
    return composantes

    
''' The main function
'''    
def nbr_cc(LD):
    '''Input: Dominance list "ld".
       Output: components counts the number of connected components.
               listv is a list of indices refering to the leading vertices of each connected component
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

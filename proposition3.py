'''Implementation of Proposition 3'''



''' This function check the necessary condition for a given index 
    It is meant to be used in the main function.
'''
def condition_dec(ld, i):
    '''Input: Dominance list "ld" and the index "i+1".
       Output: cc:=1 if the necessary condition holds.
               isolating_vertex:= the index i+1 of the first vertex of the connected component being identified.
     '''
    ldt = list(ld[i:])
    n = len(ldt)
    exh = 0 
    cc = 0
    isolating_vertex = 0   
    if (i !=0):
        for j in range(n):
            if ldt[j]<=j:
                exh += 1
            if exh==n:
                cc += 1
                isolating_vertex = i+1
    else:
        for j in range(1,n):
            if ldt[j]<j:
                exh += 1
            if exh==n-1:
                isolating_vertex = i+1
    return cc, isolating_vertex
    
    
    
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

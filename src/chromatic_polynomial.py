'''Computation of chromatic polynomial of an N-construction

Functions:
    chromatic_poly() -- Compute the chromatic polynomial given a dominance list
'''

import sympy as sp

def chromatic_poly(ld):
    '''
    Args: 
        ld: Dominance list given as a list or array.
    Returns: 
        The chromatic polynomial of the corresponding N-construction. 
    '''
    x = sp.Symbol('λ')
    p = sp.Function("P")(x)
    p = 1    #initialisation
    ik = 0 ; seo =[]
    for j in range(len(ld)):
        seo.append(0)
        for i in range(j+1, len(ld)):
            if ld[i] >= i-j:
                seo[j]=seo[j]+1
    for j in range(len(seo)):
        p = p * (x - seo[j])
    return p        
 
'''Module execution
   (gives the chromatic polynomial)
'''
if __name__ == "__main__":
    import sys
    #print("Transposition's position, then the dominance list")
    inp = sys.argv[1]
    form_inp = list(map(int, inp.strip('[]').split(',')))
    #print("P(G,λ) = {}".format(chromatic_poly(form_inp)))
    sp.pprint(chromatic_poly(form_inp))

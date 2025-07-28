'''Implementation of Proposition 5'''


'''This function gives the chromatic polynomial of an N-construction
'''
import sympy as sp
def chromatic_poly(ld):
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
   (generate an image of the corresponding N-construction)
'''
if __name__ == "__main__":
    import sys
    #print("Transposition's position, then the dominance list")
    inp = sys.argv[1]
    form_inp = list(map(int, inp.strip('[]').split(',')))
    #print("P(G,λ) = {}".format(chromatic_poly(form_inp)))
    sp.pprint(chromatic_poly(form_inp))

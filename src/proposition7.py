'''Implementation of Proposition 7 (Algorithm 1 and Algorithm 2)'''


'''This function implements Algorithm 1, which gives the permutation
   corresponding to a dominance list
'''
def phi(d):
    dl = list(d)
    '''Input: a dominance list d.
       Output: the permutation sigma = phi(d)
    '''
    #La transposition et déplacement à droite
    def Rshift(l, p, deg):
        for k in range(0,deg):
            t = l[p-k-1]
            l[p-k-1] = l[p-(k+1)-1]
            l[p-(k+1)-1] = t
        return l
        
    sb = [k for k in range(1,len(dl)+1)]
    for i in range(1,len(dl)+1):
        Rshift(sb, i, dl[i-1])
    return sb


'''This function implements Algorithm 1, which gives the permutation
   corresponding to a dominance list
'''
def phi_inv(s):
    sl = list(s)
    '''Input: a permutation sigma.
       Output: the dominance list d = phi^{-1}(sigma)
    '''
    #La transposition et déplacement à gauche
    def Lshift(l, p, deg):
        for k in range(0,deg-p-1):
            t = l[p+k]
            l[p+k] = l[p+k+1]
            l[p+k+1] = t
        return l
    #----------------------------------------
    db = [0 for k in range(1,len(sl)+1)]
    for i in range(len(db),1,-1):
        db[i-1] = i-(sl.index(i)+1)
        Lshift(sl, sl.index(i), i)
    return db
     
     
'''This function gives the cycles-representation of a permutation
'''
def cyclic(L):
    destack = [(k+1) for k in range(len(L))]
    init = True
    i = 1
    cycles = []
    while (destack != []):
        if init == True:
            cycle = [destack[0]]
            #print(cycle)
            destack.remove(i)
        if (L[i-1] == cycle[0]):
            tc = tuple(cycle)
            #print(tc)
            cycles.append(tc)
            if (destack != []):
                cycle = []
                i = destack[0]
                init = True
        else:
            i=L[i-1]
            cycle.append(i)
            destack.remove(i)
            init = False
            if (destack == []):
                tc = tuple(cycle)
                cycles.append(tc)
    return cycles 
 
 
'''Module execution
   (Gives the corresponding distance list, if the second argument is 'd'
    Gives the corresponding permutation, if the second argument is 'p' 
    --both in word- and cycles-representation--)
'''
if __name__ == "__main__":
    import sys
    inp = sys.argv[1]
    ques = sys.argv[2]
    form_inp = list(map(int, inp.strip('[]').split(',')))
    if ques == 'p':
        print(phi(form_inp),' = ', cyclic(phi(form_inp)))
    elif ques == 'd':
        print(phi_inv(form_inp))
    else:
        print(None)

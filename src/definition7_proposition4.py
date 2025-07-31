'''Implementation of Definition 7 and Proposition 4'''


'''The first function returns the (i-1,i)-transposition of a dominance list
'''
def i_transpose(i, dl):
    '''Input: the transposition's position i
              the dominance list to be stransposed 
       Output: the (i-1,i)-transposition'''
    if (i<=1 or i>len(dl) or dl[i-1]<=0):
        print("This is not a (i-1, i)-transposition")
    else:        
        dlp = list(dl)
        dlp[i-1]=dl[i-2]+1
        dlp[i-2]=dl[i-1]-1
        return dlp
        
        
''' The second function check if two dominance lists are the 
        (i-1,i)-transposes of each other
'''
def check_itranspose(dl,tdl):
    '''Input: two dominance lists
       Output: (True, the transposition's position), if dl and tdl are 
               (i-1,i)-transposes of each-other;
               or (False, 0), elsewhere.
    '''
    itranspose = False
    if len(dl) == len(tdl):
        i = 1
        #Sub-function returns True if, for an index i, tdl[i+1:] == dl[i+1:] 
        def tau_trans(i):
            if (tdl[i] == dl[i-1] + 1) and (tdl[i-1] == dl[i] - 1) and (tdl[i+1:] == dl[i+1:]):
                return True
            else: return False
    #------------------------------------------------------------------------
        while (itranspose == False) and (i < len(dl)):
            if tau_trans(i) == True:
                itranspose = True
            else:
                i += 1
    return itranspose, (None if (itranspose == False) else i)


''' The third function check if two (i-1,i)-transposes are isomorphic
'''   
def iso_transpose(dl, tdl):
    '''Input: two dominance lists
       Output: "Not (i-1,i)-tranposes" if there is no (i-1,i)-transposition
               True, if the (i-1,i)-tranposes are isomorphic; False elsewise
    '''
    #Sub-function that check isomorphism condition
    def check_iso(d):
        #nonlocal i
        test = True
        if (d[i-1], d[i]) != (d[i-1], d[i-1]+1):            
            for k in range(i+1,len(d)):
                if d[k] == k - i:
                    test = False
                    break
        return test
    #------------------------------------------------
    if not check_itranspose(dl,tdl)[0]:
        return 'Not (i-1,i)-tranposes'
    else:
        i = check_itranspose(dl,tdl)[1]
        return check_iso(dl)


'''Module execution
  (input: a dominance list and a index i,
   output: its (i-1,i)-transpose)
'''
if __name__ == "__main__":
    import sys
    #print("Transposition's position, then the dominance list")
    inp = sys.argv[1]
    inp2 = int(sys.argv[2])
    form_inp = list(map(int, inp.strip('[]').split(',')))
    td = i_transpose(inp2, form_inp)
    if td != None: print("τ(d) = {}".format(td))

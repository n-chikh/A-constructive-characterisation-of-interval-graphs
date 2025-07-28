'''Implementation of Corollary 1 & Corollary 2'''


'''This function counts the number of N-constructions 
   with n vertices and m edges
'''
from functools import lru_cache
@lru_cache(maxsize = None)
def p(n,m):
    part = 0
    if (m<0) or (n<=0):
        return 0
    elif (m==0):
        return 1
    else:
        for k in range(0,n):
            part += p(n-1,m-k)
        return part
 

'''This function counts the number of threshold graphs
   with n vertices and m edges
'''
from functools import lru_cache
@lru_cache(maxsize = None)
def t(n,m):
    if (m<0) or (n<=0):
        return 0
    elif (m==0):
        return 1
    else:
        return t(n-1,m) + t(n-1,m-n+1)
 
'''Module execution
   (computes p(n,m) and t(n,m), 
    depending on the third argument: 'p' or 't')
'''
if __name__ == "__main__":
    import sys
    #print("Transposition's position, then the dominance list")
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    inp = int(sys.argv[3])
    if inp == 'p':
        print(p(n,m))
    elif inp == 't':
        print(t(n,m))
    else:
        print(None)

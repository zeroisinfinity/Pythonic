def scanner(A):
     
    n = len(A)
    L = []
    for r in range(1,n+1,1):

        
        for j in range(1,n+1,1):
         
          i = j-r
          s = A[i:j]
          
          if r<=j and " " not in list(s)[0] and " " not in list(s)[-1]: #and " " not in list(s):
           L.append(s)
            
    return L
    
    
#n = input()
#print(scanner(n))
            
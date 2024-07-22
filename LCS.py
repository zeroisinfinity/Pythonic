#pylint:disable=W0621
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=C0303

#TAKING INPUT SUPERSTRING
opt = input("Enter superstring - ")


#MAKING LIST OF SUPERSTRING
opt_list = list(opt)


#EMPTY LISTS
L = []
L2 = []
L3 = []












#WHILE LOOP FOR IDENTIFYING BLANK SPACES
while " " in opt_list:
            
            
            
            #SLICING LIST 0 TO FIRST BLANK AND  ADDING IT TO L
            
            L.append(opt_list[:opt_list.index(" ")+1])
            
            
            
            
            #NOTING LENGTH OF BLANK's POSITION
            
            L2.append(len(L[L.index(opt_list[:opt_list.index(" ")+1])]))
            
            
            
            
            #NOTING SUM 
            
            L3.append(sum(L2[:])-1)
          
           
           
           
           
           #DEL OPT LIST BY INTERVALS OF BLANK SPACES
           
            del opt_list[:opt_list.index(" ")+1]
          
          
          
          
          
          
          
   
          
                 
                               
#1ST N LAST ITEMS OF LIST          
L4_1 = [opt[:L3[0]]]
L4_last = [opt[L3[-1]+1:]]




#LIST COMPHRENSION TO MIDDLE PART OF FINAL SORTED LIST
L4 = [opt[(L3[L3.index(i)]+1):L3[L3.index(i)+1]] for i in L3 if (len(L3)-1)>L3.index(i)>=0]




#FINAL SORTED LIST
L4_final = L4_1+L4+L4_last



while '' in L4_final:
     L4_final.remove('')


numofstr = len(L4_final)

           
           
           
           
           

#FUNCTION WHICH GIVES YOU EVERY PERMUTATION OF WORD    
def scanner(A):
    
    n = len(A)
    L = []
    for r in range(1,n+1,1): #r = dragging var
        
        for j in range(1,n+1,1):
         
          i = j-r    #i,j = end,front of slot
          s = A[i:j] #s = slot
          
          if r<=j and " " not in list(s)[0] and " " not in list(s)[-1] and " " not in list(s):
           L.append(s)
            
    return L
    






#LAST LOOP
container = []
for i in range(1,len(L4_final),1):
    
    set5 = set(scanner(L4_final[0])) & set(scanner(L4_final[i]))
    set_list = list(set5)
    set_list.sort(key=len)
   
    if len(set_list)!=0:
        
       container.append(set_list[-1])
       

#print(L4_final)    

    
container.sort(key=len)
#print(container)


    
if len(container) == (len(L4_final)-1):
    LCS = container[0]
    print(f"Largest common string is - {LCS}")
else:
    print("No common substring.")
            
   


    



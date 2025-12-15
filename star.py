n=int (input("entr the number :"))
for i in range(1,n+1):
    if(i==1 or i==n):
     print("*"* n,end="")
    else:
        
       print("*", end="")
       print(" "*(n-2),end="")
       print("*",end="")
    
     
     #print(" "* (n-i), end=" ")#space the number n-i
   # print("*"*  (2*i-1), end="")#print the star pattaern 
    #print(" ")#new line the space next line ke liye the 
   # print("*"* i,end="")
   
    print("")
#code
import numpy as np
t=int(input())
while(t>0):
    R = int(input()) 
    C=R
    entries = list(map(int, input().split())) 
    matrix = np.array(entries).reshape(R, C)              #converting the elements into matrix of rxc
    f=[]                                                
    n=[]
    for i in range(R):                                    #iterrating outer for loop
        for j in range(C):                                #iterating innner for loop
            x=i
            m=j 
            l=[]                                          #intializing an empty list
            while((x,m) not in n and x<=(R-1) and m>=0):  #checking for given pairs present in list or not
                l.append(matrix[x][m])                    #append elements m[x][m]
                n.append((x,m))
                x+=1
                m-=1
            f.append(l) 
    for i in range(f.count([])):                           #removing all unnecessary empty lists
        f.remove([])
    print(f)                                               #printing left diagnols

    print('\r')
    t-=1
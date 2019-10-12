# Z-algorithm (O(N))
# https://deve68.hatenadiary.org/entry/20120201/1328109890
def Z(s):
    n=len(s)
    z=[0]*n
    z[0]=n
    L,R=0,0
    for i in range(1,n):
        if(i>=R): # 過去の結果が全く使えない
            L=R=i
            while(R<n and s[R-L]==s[R]): R+=1
            z[i]=R-L
        elif(z[i-L]<R-i): # 過去の結果が全て使える
            z[i]=z[i-L]
        else: # 過去の結果が一部使える
            L=i
            while(R<n and s[R-L]==s[R]): R+=1
            z[i]=R-L
    return z

# example
print(Z("abaaabaabb")) # [10,0,1,1,4,0,1,2,0,0]

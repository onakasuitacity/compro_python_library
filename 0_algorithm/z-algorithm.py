# Z-algorithm (O(N))
# https://deve68.hatenadiary.org/entry/20120201/1328109890
def Z(s):
    """
    s: str
    return list of int with length len(s)
    """
    # initialization
    n=len(s)
    z=[0]*n
    z[0]=n
    # construct
    L,R=0,0
    for i in range(1,n):
        if i>R: # 過去の結果が全く使えない
            L=R=i
            while(R<n and s[R-L]==s[R]): R+=1
            z[i]=R-L
            R-=1 # 0-indexedでiと比較するため
        elif z[i-L]<R-i+1:
            z[i]=z[i-L]
        else:
            L=i
            R+=1 # Rまでは確定しているので、R+1から確認
            while(R<n and s[R-L]==s[R]): R+=1
            z[i]=R-L
            R-=1
    return z

print(Z("abaaabaabb")) # [10,0,1,1,4,0,1,2,0,0]

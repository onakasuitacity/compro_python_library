# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def bisection(l,r,f,left=True,discrete=True):
    eps=1 if(discrete) else 10**-8
    if((not left)^f(r)): return r if(left) else r+1
    elif(left^f(l)): return l-1 if(left) else l
    while(r-l>eps):
        h=(l+r)//2 if(discrete) else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if(not discrete) else l if(left) else r

def resolve():
    n,q=map(int,input().split())
    S=input()
    TD=[input().split() for _ in range(q)]

    def checkleft(i):
        for t,d in TD:
            if(S[i]==t and d=='L'):
                i-=1
            elif(S[i]==t and d=='R'):
                i+=1
            if(i<0):
                return False
            elif(i>n-1):
                return True
        return True

    def checkright(i):
        for t,d in TD:
            if(S[i]==t and d=='L'):
                i-=1
            elif(S[i]==t and d=='R'):
                i+=1
            if(i<0):
                return True
            elif(i>n-1):
                return False
        return True

    i=bisection(0,n-1,checkleft,left=False)
    j=bisection(0,n-1,checkright,left=True)
    print(max(j-i+1,0))
resolve()

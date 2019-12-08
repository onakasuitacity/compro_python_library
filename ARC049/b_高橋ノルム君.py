# https://atcoder.jp/contests/arc049/tasks/arc049_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def trisection(l,r,f,convex=True,discrete=True):
    eps=2 if(discrete) else 10**-8
    while(r-l>eps):
        d=(r-l)//3 if(discrete) else (r-l)/3
        h1=l+d; h2=r-d
        if((f(h1)>=f(h2))^convex): r=h2
        else: l=h1
    if(not discrete): return f((l+r)/2)
    elif(convex): return min([(f(l),l),(f(l+1),l+1),(f(r),r)])[1]
    else: return max([(f(l),l),(f(l+1),l+1),(f(r),r)])[1]

def resolve():
    n=int(input())
    XYC=[tuple(map(int,input().split())) for _ in range(n)]

    def check1(X):
        res=-INF
        for x,y,c in XYC:
            res=max(res,c*abs(x-X))
        return res

    def check2(Y):
        res=-INF
        for x,y,c in XYC:
            res=max(res,c*abs(y-Y))
        return res

    s=trisection(-10**6,10**6,check1,discrete=False)
    t=trisection(-10**6,10**6,check2,discrete=False)
    print(max(s,t))
resolve()

# https://atcoder.jp/contests/abc093/tasks/arc094_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

def trisection(l,r,f,convex=True,discrete=True):
    eps=2 if(discrete) else 10**-12
    while(r-l>eps):
        d=(r-l)//3 if(discrete) else (r-l)/3
        h1=l+d; h2=r-d
        if((f(h1)>=f(h2))^convex): r=h2
        else: l=h1
    if(not discrete): return (l+r)/2
    elif(convex): return min([(f(l),l),(f(l+1),l+1),(f(r),r)])[1]
    else: return max([(f(l),l),(f(l+1),l+1),(f(r),r)])[1]

def resolve():
    for _ in range(int(input())):
        a,b=map(int,input().split())
        l=0; r=a+b
        while(r-l>1):
            h=(l+r)//2
            f=lambda x:(x+(x>=a))*(h-x+1+(h-x+1>=b))
            x=trisection(1,h,f,convex=False,discrete=True)
            if(f(x)<a*b): l=h
            else: r=h
        print(l)
resolve()

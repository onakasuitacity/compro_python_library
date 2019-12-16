# https://atcoder.jp/contests/arc042/tasks/arc042_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def area(a,b):
    return abs(a.real*b.imag-a.imag*b.real)/2

def resolve():
    x,y=map(int,input().split())
    c0=x+y*1j
    n=int(input())
    C=[None]*n
    for i in range(n):
        x,y=map(int,input().split())
        C[i]=x+y*1j
    C.append(C[0])

    ans=INF
    for i in range(n):
        c1=C[i]; c2=C[i+1]
        c1-=c0; c2-=c0
        s=area(c1,c2)
        l=abs(c1-c2)
        ans=min(ans,2*s/l)
    print(ans)
resolve()

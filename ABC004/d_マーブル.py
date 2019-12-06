# https://atcoder.jp/contests/abc004/tasks/abc004_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def cost(c,l,r):
    l-=c; r-=c
    if(l<=0<=r):
        l=abs(l)
        return l*(l+1)//2+r*(r+1)//2
    if(l<=r<0): l,r=abs(r),abs(l)
    assert(0<=l<=r)
    return r*(r+1)//2-l*(l-1)//2

def resolve():
    R,G,B=map(int,input().split())
    ans=INF
    for l in range(-500,500):
        score=0
        r=l+G-1
        score+=cost(0,l,r)
        # 青について
        if(r<100-(B-1)//2):
            score+=cost(100,100-(B-1)//2,100+B//2)
        else:
            score+=cost(100,r+1,r+B)
        # 赤について
        if(-100+(R-1)//2<l):
            score+=cost(-100,-100-R//2,-100+(R-1)//2)
        else:
            score+=cost(-100,l-R,l-1)
        ans=min(ans,score)
    print(ans)
resolve()

# https://atcoder.jp/contests/agc008/tasks/agc008_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    aI,aO,aT,aJ,aL,aS,aZ=map(int,input().split())
    ans=aO

    if(aI>=1 and aJ>=1 and aL>=1 and (aI%2+aJ%2+aL%2)==2):
        ans+=3
        aI-=1; aJ-=1; aL-=1

    ans+=(aI//2)*2
    ans+=(aJ//2)*2
    ans+=(aL//2)*2
    if(aI&1 and aJ&1 and aL&1):
        ans+=3

    print(ans)
resolve()

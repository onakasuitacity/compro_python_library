# https://atcoder.jp/contests/abc071/tasks/arc081_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

from collections import Counter
def resolve():
    int(input())
    C=Counter(map(int,input().split()))
    C=[(k,v) for k,v in C.items()]
    C.sort(reverse=1)
    ans=0
    for k,v in C:
        if(v>=4):
            ans=k*k
            break

    a=0; b=0
    for i in range(len(C)):
        k,v=C[i]
        if(v>=2):
            a=k
            C[i]=(0,0)
            break

    for i in range(len(C)):
        k,v=C[i]
        if(v>=2):
            b=k
            C[i]=(0,0)
            break

    print(max(ans,a*b))
resolve()

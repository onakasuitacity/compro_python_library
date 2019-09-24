# https://atcoder.jp/contests/arc081/tasks/arc081_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=map(int,input().split())
    from collections import Counter
    c=Counter(A)
    ans=0
    first=0
    second=0
    for k,v in c.items():
        if v>=4: ans=max(ans,k*k)
        if v>=2:
            if k>first:
                first,second=k,first
            elif k>second:
                second=k
    print(max(ans,first*second))
resolve()

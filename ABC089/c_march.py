# https://atcoder.jp/contests/abc089/tasks/abc089_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    s="MARCH"
    n=int(input())
    k=[0]*5
    for _ in range(n):
        t=input()[0]
        if t in s: k[s.index(t)]+=1
    from itertools import combinations
    A=combinations(range(5),3)
    ans=0
    for a,b,c in A:
        ans+=k[a]*k[b]*k[c]
    print(ans)
resolve()

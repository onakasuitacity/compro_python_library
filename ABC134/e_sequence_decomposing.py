# https://atcoder.jp/contests/abc134/tasks/abc134_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect
    n=int(input())
    A=[-int(input()) for _ in range(n)]
    B=[]
    for a in A:
        i=bisect(B,a)
        if(i==len(B)): B.append(a)
        else: B[i]=a
    print(len(B))
resolve()

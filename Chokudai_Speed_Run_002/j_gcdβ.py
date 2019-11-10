# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_j
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from fractions import gcd
    n=int(input())
    A,B=map(int,input().split())
    for _ in range(n-1):
        a,b=map(int,input().split())
        A=max(gcd(A,a),gcd(A,b))
        B=max(gcd(B,a),gcd(B,b))
    print(max(A,B))
resolve()

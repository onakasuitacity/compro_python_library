# https://atcoder.jp/contests/abc145/tasks/abc145_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    if(n&1):
        print("No")
        return
    S=input()
    a=S[:n//2]
    b=S[n//2:]
    print("Yes" if(a==b) else "No")
resolve()

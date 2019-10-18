import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    if n%2==0: print(0.5)
    else: print((n//2+1)/n)
resolve()

# https://atcoder.jp/contests/abc068/tasks/arc079_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    k=int(input())
    n=50
    q=k//n
    r=k%n
    A=[q+n-r+1+i for i in range(r)]+[q+i for i in range(n-r)]
    print(n)
    print(*A)
resolve()

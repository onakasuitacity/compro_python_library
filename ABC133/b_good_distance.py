# https://atcoder.jp/contests/abc133/tasks/abc133_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    def check(i,j):
        if(i>=j): return False
        d=sum((X[i][k]-X[j][k])**2 for k in range(D))**.5
        return d==int(d)

    n,D=map(int,input().split())
    X=[list(map(int,input().split())) for _ in range(n)]
    from itertools import product
    print(sum(check(i,j) for i,j in product(range(n),repeat=2)))
resolve()

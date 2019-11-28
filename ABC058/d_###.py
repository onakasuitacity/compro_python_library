# https://atcoder.jp/contests/abc058/tasks/arc071_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    X=list(map(int,input().split()))
    Y=list(map(int,input().split()))
    X.sort()
    Y.sort()
    I=0
    J=0
    coef=-(n-1)
    for x in X:
        I+=coef*x
        I%=MOD
        coef+=2
    coef=-(m-1)
    for y in Y:
        J+=coef*y
        J%=MOD
        coef+=2
    print(I*J%MOD)
resolve()

# https://atcoder.jp/contests/abc142/tasks/abc142_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def prime_factorization(n):
    factor=[]
    sqrt=int(n**.5)
    for d in range(2,sqrt+1):
        while(n%d==0):
            n//=d
            factor.append(d)
    if n!=1: factor.append(n)
    return factor

def resolve():
    a,b=map(int,input().split())
    from fractions import gcd
    g=gcd(a,b)
    factor=prime_factorization(g)
    print(len(set(factor))+1)
resolve()

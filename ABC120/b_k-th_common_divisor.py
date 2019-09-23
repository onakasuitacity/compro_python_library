# https://atcoder.jp/contests/abc120/tasks/abc120_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]

def resolve():
    a,b,k=map(int,input().split())
    from fractions import gcd
    g=gcd(a,b)
    A=divisors(g)
    print(A[-k])
resolve()

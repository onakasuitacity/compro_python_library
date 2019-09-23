# https://atcoder.jp/contests/arc017/tasks/arc017_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def prime(n,is_prime=True):
    """
    n: positive integer
    if is_prime: return n is prime
    else: return list of prime <= n
    """
    if n<=1: return False if is_prime else []
    S=[1]*(n+1)
    S[0]=0; S[1]=0
    for i in range(2,n):
        if S[i]==0: continue
        for j in range(2*i,n+1,i):
            S[j]=0
    if is_prime: return bool(S[n])
    else: return [p for p in range(n+1) if S[p]]
def resolve():
    print("YES" if prime(int(input())) else "NO")
resolve()

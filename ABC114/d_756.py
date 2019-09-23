# https://atcoder.jp/contests/abc114/tasks/abc114_d
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
    """
    p^74,p^24q^2,p^14q^4,p^4q^4r^2
    """
    n=int(input())
    P=prime(n,False)
    bin=[0]*48
    for p in P:
        if p>47: continue # p<=47
        q=p
        while(q<=n):
            bin[p]+=n//q
            q*=p
    c2=len([0 for i in bin if i>=2])
    c4=len([0 for i in bin if i>=4])
    c14=len([0 for i in bin if i>=14])
    c24=len([0 for i in bin if i>=24])
    c74=len([0 for i in bin if i>=74])
    ans=0
    ans+=c74
    ans+=c24*(c2-1)
    ans+=c14*(c4-1)
    ans+=c4*(c4-1)//2*(c2-2)
    print(ans)
resolve()

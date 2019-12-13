# https://atcoder.jp/contests/agc008/tasks/agc008_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    B=[max(a,0) for a in A] # 正の部分だけ取れる
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]

    T=[0]*(n+1)
    for i in range(n):
        T[i+1]=T[i]+B[i]

    # A[:i] までは任意、A[i:i+k]は塗るか塗らないかの2択、A[i+k:]からは任意
    ans=0
    for i in range(n-k+1):
        score=T[i]+max(0,S[i+k]-S[i])+(T[n]-T[i+k])
        ans=max(ans,score)

    print(ans)
resolve()

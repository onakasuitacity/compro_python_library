# https://atcoder.jp/contests/abc102/tasks/arc100_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left as bisect
    n=int(input())
    A=list(map(int,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]

    ans=INF
    for j in range(1,n):
        i=bisect(S,S[j]/2)
        k=bisect(S,(S[j]+S[-1])/2)
        ans=min(ans,max(S[i],S[j]-S[i],S[k]-S[j],S[-1]-S[k])-min(S[i],S[j]-S[i],S[k]-S[j],S[-1]-S[k]))
        ans=min(ans,max(S[i],S[j]-S[i],S[k-1]-S[j],S[-1]-S[k-1])-min(S[i],S[j]-S[i],S[k-1]-S[j],S[-1]-S[k-1]))
        ans=min(ans,max(S[i-1],S[j]-S[i-1],S[k]-S[j],S[-1]-S[k])-min(S[i-1],S[j]-S[i-1],S[k]-S[j],S[-1]-S[k]))
        ans=min(ans,max(S[i-1],S[j]-S[i-1],S[k-1]-S[j],S[-1]-S[k-1])-min(S[i-1],S[j]-S[i-1],S[k-1]-S[j],S[-1]-S[k-1]))
    print(ans)
resolve()

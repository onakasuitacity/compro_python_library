# https://atcoder.jp/contests/arc103/tasks/arc103_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=[None]+list(map(int,input()))
    n=len(S)-1

    # check
    if(not (S[1]==1 and S[n-1]==1)):
        print(-1)
        return
    if(S[n]==1):
        print(-1)
        return
    if(any(S[i]!=S[n-i] for i in range(1,n-1))):
        print(-1)
        return

    v=1
    nv=2
    for i in range(n-1,0,-1):
        print(v,nv)
        nv+=1
        if(S[i]==1): v=nv-1
resolve()

# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    S=[-INF]*n
    S[0]=A[0]
    for i in range(n-1):
        S[i+1]=max(S[i],A[i+1])
    print(1+sum(1 for i in range(n-1) if(A[i+1]>S[i])))
resolve()

# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))

    # A,Bそれぞれについて、隣接している値が異なる -> その山の値は確定
    C=[None]*n
    C[0]=A[0]
    for i in range(1,n):
        if(A[i]!=A[i-1]):
            C[i]=A[i]

    for i in range(n):
        if(C[i] and B[i]<C[i]):
            print(0)
            return

    D=[None]*n
    D[-1]=B[-1]
    for i in range(n-2,-1,-1):
        if(B[i]!=B[i+1]):
            D[i]=B[i]

    for i in range(n):
        if(D[i] and A[i]<D[i]):
            print(0)
            return

    ans=1
    for i in range(n):
        if(C[i] or D[i]): continue
        ans*=min(A[i],B[i])
        ans%=MOD

    print(ans)
resolve()

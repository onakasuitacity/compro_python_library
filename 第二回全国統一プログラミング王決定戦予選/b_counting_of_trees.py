# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=998244353
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    D=list(map(int,input().split()))
    M=max(D)

    if(D[0]!=0):
        print(0)
        return

    C=[0]*(M+1)
    for d in D:
        C[d]+=1

    if(C[0]!=1):
        print(0)
        return

    if(any(C[i]==0 for i in range(M+1))):
        print(0)
        return

    ans=1
    for i in range(1,M+1):
        ans*=pow(C[i-1],C[i],MOD)
        ans%=MOD
    print(ans)
resolve()

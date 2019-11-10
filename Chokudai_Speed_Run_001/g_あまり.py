# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_g
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    ans=A[0]
    for i in range(1,n):
        ans=ans*pow(10,len(str(A[i])),MOD)+A[i]
        ans%=MOD
    print(ans)
resolve()

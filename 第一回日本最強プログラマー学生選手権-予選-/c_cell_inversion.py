# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    S=input()
    A=[((S[i]=='B') is (i&1==1))+0 for i in range(2*n)]

    # pair が偏る場合は不可能
    if(sum(A)!=n):
        print(0)
        return

    cnt=0
    ans=1
    for a in A:
        if(a==0):
            cnt+=1
        else:
            ans*=cnt
            ans%=MOD
            cnt-=1

    # factorial(n) を掛ける
    for i in range(1,n+1):
        ans*=i
        ans%=MOD
    print(ans)
resolve()

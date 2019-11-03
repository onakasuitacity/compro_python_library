# https://atcoder.jp/contests/abc134/tasks/abc134_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=['$']+list(map(int,input().split())) # 1-index
    ans=[0]*(n+1)
    for i in range(n,0,-1): # iを確定させたい
        parity=A[i]
        for j in range(2,n//i+1): # iの倍数のうち、i以外のものを全てみる
            parity+=ans[i*j]
        if(parity%2): ans[i]=1
    s=sum(1 for i in range(1,n+1) if ans[i])
    print(s)
    if(s):
        print(*(i for i in range(1,n+1) if ans[i]))
resolve()

# https://atcoder.jp/contests/abc076/tasks/abc076_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    T=[0]+list(map(int,input().split()))
    for i in range(n): T[i+1]+=T[i]
    V=list(map(int,input().split()))

    def f(t):
        res=INF
        res=min(res,t)
        res=min(res,-t+T[-1])
        for i in range(1,n+1):
            if(t<T[i-1]): res=min(res,-t+T[i-1]+V[i-1])
            elif(t<=T[i]): res=min(res,V[i-1])
            else: res=min(res,t-T[i]+V[i-1])
        return res

    ans=0
    for t in range(2*T[-1]): # 0.5刻みで計算
        ans+=(f(t/2)+f((t+1)/2))/4
    print(ans)
resolve()

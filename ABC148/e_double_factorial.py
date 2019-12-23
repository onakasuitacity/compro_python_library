# https://atcoder.jp/contests/abc148/tasks/abc148_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def df(n):
    if(n<2): return 1
    return n*df(n-2)

def resolve():
    n=int(input())

    # 奇数のときは 0
    if(n&1):
        print(0)
        return

    # n が小さいときは愚直にやる
    if(n<=100):
        x=df(n)
        ans=0
        while(x%10==0):
            ans+=1
            x//=10
        print(ans)
        return

    # そうでなければ n 偶数に対して 10 の倍数を調べる
    ans=0
    while(n):
        ans+=n//10
        n//=5
    print(ans)

resolve()

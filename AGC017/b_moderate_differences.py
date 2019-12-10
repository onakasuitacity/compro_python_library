# https://atcoder.jp/contests/agc017/tasks/agc017_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,a,b,c,d=map(int,input().split())
    for k in range(n): # k 右に行った回数
        L=a+k*c-(n-k-1)*d
        R=a+k*d-(n-k-1)*c
        if(L<=b<=R):
            print("YES")
            return
    print("NO")
resolve()

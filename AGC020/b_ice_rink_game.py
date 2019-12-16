# https://atcoder.jp/contests/agc020/tasks/agc020_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    k=int(input())
    A=list(map(int,input().split()))
    l=2; r=2
    for a in A[::-1]:
        # l 以上の a の倍数
        l=((l-1)//a+1)*a
        # r 以下の a の倍数 + (a-1)
        r=(r//a)*a+(a-1)
        if(l>r or r<2):
            print(-1)
            return
    print(l,r)
resolve()

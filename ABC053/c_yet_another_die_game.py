# https://atcoder.jp/contests/abc053/tasks/arc068_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x=int(input())
    ans=2*(x//11)
    x%=11
    if(x==0):
        print(ans)
    elif(x<7):
        print(ans+1)
    else:
        print(ans+2)
resolve()

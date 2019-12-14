# https://atcoder.jp/contests/arc046/tasks/arc046_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    a,b=map(int,input().split())

    if(a>b):
        print("Takahashi")
        return

    elif(a<b):
        if(n<=a): print("Takahashi")
        else: print("Aoki")

    else:
        if(n%(a+1)==0): print("Aoki")
        else: print("Takahashi")
resolve()

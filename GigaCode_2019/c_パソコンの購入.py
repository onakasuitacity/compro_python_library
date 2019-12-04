# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    d=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    now=0
    ans=INF
    for a,b in zip(A,B):
        now+=a
        if(now>=b):
            ans=min(ans,b)
    if(ans==INF): ans=-1
    print(ans)
resolve()

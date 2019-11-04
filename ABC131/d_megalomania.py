# https://atcoder.jp/contests/abc131/tasks/abc131_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    J=[tuple(map(int,input().split())) for _ in range(n)]
    J.sort(lambda x:x[1])
    now=0
    for a,b in J:
        now+=a
        if(now>b):
            print("No")
            return
    print("Yes")
resolve()

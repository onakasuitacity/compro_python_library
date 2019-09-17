# https://atcoder.jp/contests/abc080/tasks/abc080_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    run=[int(input().replace(' ',''),2) for _ in range(n)]
    profit=[tuple(map(int,input().split())) for _ in range(n)]
    print(max(sum(profit[j][bin(run[j]&i).count('1')] for j in range(n)) for i in range(1,1<<10)))
resolve()

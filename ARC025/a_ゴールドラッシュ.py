# https://atcoder.jp/contests/arc025/tasks/arc025_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    D=list(map(int,input().split()))
    J=list(map(int,input().split()))
    print(sum(max(D[i],J[i]) for i in range(7)))
resolve()

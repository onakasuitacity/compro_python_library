# https://atcoder.jp/contests/abc144/tasks/abc144_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    s=set()
    for i in range(1,10):
        for j in range(1,10):
            s.add(i*j)
    n=int(input())
    print("Yes" if n in s else "No")
resolve()

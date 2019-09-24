# https://atcoder.jp/contests/abc109/tasks/abc109_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    W=[input() for _ in range(n)]
    for i in range(n):
        w=W.pop()
        if w in W:
            print("No")
            return
        if W:
            if not w[0]==W[-1][-1]:
                print("No")
                return
    print("Yes")
resolve()

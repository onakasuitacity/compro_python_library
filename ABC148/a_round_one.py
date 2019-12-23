# https://atcoder.jp/contests/abc148/tasks/abc148_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    A=list(range(1,4))
    A.remove(int(input()))
    A.remove(int(input()))
    print(A[0])
resolve()

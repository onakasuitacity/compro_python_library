# https://atcoder.jp/contests/abc019/tasks/abc019_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.buffer.readline().rstrip()
def resolve():
    n=int(input())
    A=map(int,input().split())
    A={a//(a&(-a)) for a in A}
    print(len(A))
resolve()

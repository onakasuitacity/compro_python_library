# https://atcoder.jp/contests/abc063/tasks/arc075_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    S=[int(input()) for _ in range(n)]
    S.sort()
    res=sum(S)
    if(res%10):
        print(res)
        return
    for s in S:
        if(s%10):
            print(res-s)
            return
    print(0)
resolve()

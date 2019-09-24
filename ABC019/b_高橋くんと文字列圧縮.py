# https://atcoder.jp/contests/abc019/tasks/abc019_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import groupby
    G=groupby(input())
    ans=''
    for s,it in G:
        ans+=s+str(len(list(it)))
    print(ans)
resolve()

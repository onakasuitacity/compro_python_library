# https://atcoder.jp/contests/agc029/tasks/agc029_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    ans=0
    b=0
    for s in S:
        if s=="B": b+=1
        else: ans+=b
    print(ans)
resolve()

# https://atcoder.jp/contests/arc014/tasks/arc014_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    n=int(input())
    S=input()
    ans=0
    for key,val in Counter(S).items():
        ans+=val%2
    print(ans)
resolve()

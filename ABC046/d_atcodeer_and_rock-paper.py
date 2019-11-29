# https://atcoder.jp/contests/abc046/tasks/arc062_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    S=input()
    C=Counter(S)
    g=C['g']; p=C['p']
    n=g+p
    print(g-(n+1)//2)
resolve()

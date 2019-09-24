# https://atcoder.jp/contests/abc110/tasks/abc110_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from collections import Counter
    s=Counter(input()).most_common()
    t=Counter(input()).most_common()
    n=len(s)
    print("Yes" if all(s[i][1]==t[i][1] for i in range(n)) else "No")
resolve()

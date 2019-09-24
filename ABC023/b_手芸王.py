# https://atcoder.jp/contests/abc023/tasks/abc023_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    s=input()
    n=n//2
    import re
    if n%3==0:
        res=re.match("^(bca)*b$",s)
    elif n%3==1:
        res=re.match("^(abc)+$",s)
    else:
        res=re.match("^(cab)+ca$",s)
    print(n if res else -1)
resolve()

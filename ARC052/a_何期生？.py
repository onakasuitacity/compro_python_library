# https://atcoder.jp/contests/arc052/tasks/arc052_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    ans=''
    for s in S:
        if not (65<=ord(s)<=90 or 97<=ord(s)<=122):
            ans=ans+s
    print(ans)
resolve()

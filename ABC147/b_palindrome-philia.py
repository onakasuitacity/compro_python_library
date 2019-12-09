# https://atcoder.jp/contests/abc147/tasks/abc147_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=input()
    n=len(S)
    pre=S[:n//2]
    suf=S[n-n//2::]
    suf=suf[::-1]
    ans=0
    for p,s in zip(pre,suf):
        ans+=(p!=s)
    print(ans)
resolve()

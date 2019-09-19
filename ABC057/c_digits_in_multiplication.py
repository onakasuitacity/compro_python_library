# https://atcoder.jp/contests/abc057/tasks/abc057_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    ans=INF
    for i in range(1,int(n**.5)+1):
        if n%i: continue
        ans=min(ans,max(len(str(i)),len(str(n//i))))
    print(ans)
resolve()

# https://atcoder.jp/contests/abc138/tasks/abc138_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    T=input()
    if(set(T)-set(S)):
        print(-1)
        return
    n=len(S)
    C=[[] for _ in range(26)]
    for i,s in enumerate(S*2): C[ord(s)-97].append(i)
    from bisect import bisect_left
    ans=0
    for s in T:
        j=bisect_left(C[ord(s)-97],ans%n)
        ans+=C[ord(s)-97][j]-ans%n+1
    print(ans)
resolve()

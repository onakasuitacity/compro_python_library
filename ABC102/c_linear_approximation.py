# https://atcoder.jp/contests/abc102/tasks/arc100_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=map(int,input().split())
    B=[a-i for i,a in enumerate(A)]
    if n==1:
        print(0)
        return
    B.sort()
    f=lambda x:sum(abs(x-b) for b in B)
    ans=min(f(B[n//2]),f(B[n//2+1]))
    print(ans)
resolve()

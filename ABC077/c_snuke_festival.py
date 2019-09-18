# https://atcoder.jp/contests/abc077/tasks/arc084_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    import bisect
    n=int(input())
    A=sorted(list(map(int,input().split())))
    B=sorted(list(map(int,input().split())))
    C=sorted(list(map(int,input().split())))
    ans=0
    for b in B:
        i=bisect.bisect_left(A,b)
        j=bisect.bisect_right(C,b)
        ans+=i*(n-j)
    print(ans)
resolve()

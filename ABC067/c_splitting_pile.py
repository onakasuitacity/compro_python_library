# https://atcoder.jp/contests/abc067/tasks/arc078_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    s=sum(A)
    for i in range(n-1):
        A[i+1]+=A[i]
    res=INF
    for x in A[:-1]:
        res=min(res,abs(s-2*x))
    print(res)
resolve()

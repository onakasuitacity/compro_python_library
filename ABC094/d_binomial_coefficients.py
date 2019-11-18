# https://atcoder.jp/contests/abc094/tasks/arc095_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    A.sort()
    m=A[-1]

    score=INF
    a=-1
    for i in range(n-1):
        if(score>abs(A[i]-m/2)):
            score=abs(A[i]-m/2)
            a=A[i]
    print(m,a)
resolve()

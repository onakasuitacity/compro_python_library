# https://atcoder.jp/contests/abc004/tasks/abc004_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    n%=30
    A=['1','2','3','4','5','6']
    for i in range(n):
        A[i%5],A[i%5+1]=A[i%5+1],A[i%5]
    print(''.join(A))
resolve()

# https://atcoder.jp/contests/abc127/tasks/abc127_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    r,d,x=map(int,input().split())
    A=[0]*11
    A[0]=x
    for i in range(10):
        A[i+1]=r*A[i]-d
    for i in range(1,11):
        print(A[i])
resolve()

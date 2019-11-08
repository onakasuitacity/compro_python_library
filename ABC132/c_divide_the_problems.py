# https://atcoder.jp/contests/abc132/tasks/abc132_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    if(n%2):
        print(0)
        return
    A.sort()
    print(A[n//2]-A[n//2-1])
resolve()

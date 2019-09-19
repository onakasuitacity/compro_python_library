# https://atcoder.jp/contests/abc124/tasks/abc124_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    if n==1:
        print(1)
        return
    H=list(map(int,input().split()))
    M=[0]*n
    M[1]=H[0]
    for i in range(2,n):
        M[i]=max(M[i-1],H[i-1])
    print(sum(1 for i in range(n) if H[i]>=M[i]))
resolve()

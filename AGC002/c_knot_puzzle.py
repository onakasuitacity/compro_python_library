# https://atcoder.jp/contests/agc002/tasks/agc002_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,L=map(int,input().split())
    A=list(map(int,input().split()))

    for i in range(n-1):
        if(A[i]+A[i+1]>=L):
            print("Possible")
            break
    else:
        print("Impossible")
        return

    for j in range(1,i+1):
        print(j)
    for j in range(n-1,i,-1):
        print(j)
resolve()

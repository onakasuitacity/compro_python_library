# https://atcoder.jp/contests/abc134/tasks/abc134_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[int(input()) for _ in range(n)]
    Left=[0]*n
    Left[0]=A[0]
    Right=[0]*n
    Right[-1]=A[-1]

    for i in range(1,n):
        Left[i]=max(A[i],Left[i-1])
    for i in range(n-2,-1,-1):
        Right[i]=max(A[i],Right[i+1])

    for i in range(n):
        if(i==0):
            print(Right[1])
        elif(i==n-1):
            print(Left[n-2])
        else:
            print(max(Left[i-1],Right[i+1]))
resolve()

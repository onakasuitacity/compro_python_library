# https://atcoder.jp/contests/abc135/tasks/abc135_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    score=0
    for i in range(n):
        k=min(A[i],B[i])
        score+=k
        A[i]-=k
        B[i]-=k
        if(B[i]>0):
            k=min(A[i+1],B[i])
            score+=k
            A[i+1]-=k
            B[i]-=k
    print(score)
resolve()

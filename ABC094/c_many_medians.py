# https://atcoder.jp/contests/abc094/tasks/arc095_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[0]*n
    for i,x in enumerate(map(int,input().split())):
        A[i]=[x,i]
    A.sort()

    l=A[n//2-1][0]
    h=A[n//2][0]
    for i in range(n//2):
        A[i][0]=h
    for i in range(n//2):
        A[n//2+i][0]=l

    A.sort(lambda x:x[1])
    for i in range(n):
        print(A[i][0])
resolve()

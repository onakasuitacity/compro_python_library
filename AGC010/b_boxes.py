# https://atcoder.jp/contests/agc010/tasks/agc010_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    N=n*(n+1)//2

    if(sum(A)%N):
        print("NO")
        return

    k=sum(A)//N
    for i in range(n):
        q,r=divmod(k-(A[(i+1)%n]-A[i]),n)
        if(q<0 or r):
            print("NO")
            return

    print("YES")
resolve()

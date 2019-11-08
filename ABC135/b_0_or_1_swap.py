# https://atcoder.jp/contests/abc135/tasks/abc135_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    score=0
    for i,a in enumerate(A):
        score+=i+1!=a
    if(score<=2):
        print("YES")
    else:
        print("NO")
resolve()

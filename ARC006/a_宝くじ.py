# https://atcoder.jp/contests/arc006/tasks/arc006_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    A=set(map(int,input().split()))
    b=int(input())
    C=set(map(int,input().split()))
    k=len(A&C)
    if k==6:
        print(1)
    elif k==5 and (b in C):
        print(2)
    elif k==5 and (b not in C):
        print(3)
    elif k==4:
        print(4)
    elif k==3:
        print(5)
    else:
        print(0)
resolve()

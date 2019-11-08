# https://atcoder.jp/contests/abc121/tasks/abc121_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    # f(A,B)=f(0,B)^f(0,A-1)
    # f(0,x)はmod 4の値で場合分けでき、
    # x=0: f(0,x)=x
    # x=1: f(0,x)=1
    # x=2: f(0,x)=x+1
    # x=3: f(0,x)=0

    A,B=map(int,input().split())

    if(B%4==0):
        SB=B
    elif(B%4==1):
        SB=1
    elif(B%4==2):
        SB=B+1
    else:
        SB=0

    A-=1
    if(A<0):
        SA=0
    elif(A%4==0):
        SA=A
    elif(A%4==1):
        SA=1
    elif(A%4==2):
        SA=A+1
    else:
        SA=0

    print(SA^SB)
resolve()

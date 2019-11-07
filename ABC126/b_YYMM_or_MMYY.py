# https://atcoder.jp/contests/abc126/tasks/abc126_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    # YY は 00から99
    # MM は 01から12
    S=input()
    u=int(S)//100
    d=int(S[2:])
    if(1<=u<=12 and 1<=d<=12):
        print('AMBIGUOUS')
    elif(1<=u<=12 and (d==0 or d>12)):
        print('MMYY')
    elif((not 1<=u<=12) and 1<=d<=12):
        print('YYMM')
    else:
        print('NA')
resolve()

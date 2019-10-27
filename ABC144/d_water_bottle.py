# https://atcoder.jp/contests/abc144/submissions/8183946
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import pi,atan
    a,b,x=map(int,input().split())
    if(2*x<=a*a*b):
        # b*b/tany*1/2*a=x
        # tany=a*b*b/(2*x)
        print(atan(a*b*b/(2*x))*180/pi)
    else:
        # (b+(b-a*tany))*1/2*a*a=x
        # 2*b-a*tany=2*x/(a*a)
        # tany=(2*(b-x/(a*a)))/a
        print(atan((2*(b-x/(a*a)))/a)*180/pi)
resolve()

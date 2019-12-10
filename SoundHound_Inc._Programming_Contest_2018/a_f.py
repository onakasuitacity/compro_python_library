# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    if(a+b==15):
        print('+')
    elif(a*b==15):
        print('*')
    else:
        print('x')
resolve()

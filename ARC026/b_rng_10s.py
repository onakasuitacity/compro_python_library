# https://atcoder.jp/contests/agc026/tasks/agc026_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from fractions import gcd
def resolve():
    for _ in range(int(input())):
        a,b,c,d=map(int,input().split())
        if(a<b):
            print("No")
            continue
        if(b>d):
            print("No")
            continue
        if(c>=b):
            print("Yes")
            continue

        g=gcd(b,d)
        a%=g
        a-=g
        u=(c-a)//g+1
        if(a+u*g>=b):
            print("Yes")
        else:
            print("No")
resolve()

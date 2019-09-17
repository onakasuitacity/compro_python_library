# https://atcoder.jp/contests/abc034/tasks/abc034_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
from math import factorial
def resolve():
    w,h=map(lambda x:int(x)-1,input().split())
    def modinv(a,m=MOD):
        b,u,v=m,1,0
        while(b):
            t=a//b
            a-=t*b; a,b=b,a
            u-=t*v; u,v=v,u
        u%=m
        if u<0: u+=m
        return u
    print(factorial(w+h)%MOD*modinv(factorial(w))%MOD*modinv(factorial(h))%MOD)
resolve()

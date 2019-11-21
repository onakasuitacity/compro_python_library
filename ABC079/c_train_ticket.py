# https://atcoder.jp/contests/abc079/tasks/abc079_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c,d=input()
    from itertools import product
    for i,j,k in product(['+','-'],repeat=3):
        s=a+i+b+j+c+k+d
        if(eval(s)==7):
            print(s+'=7')
            return
resolve()

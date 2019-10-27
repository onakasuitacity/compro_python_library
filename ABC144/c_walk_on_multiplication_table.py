# https://atcoder.jp/contests/abc144/tasks/abc144_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    a,b=0,0
    for d in range(1,int(1+n**.5)):
        if(n%d==0):
            a,b=d,n//d
    print(a-1+b-1)
resolve()

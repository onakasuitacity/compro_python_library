# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    b=w=0
    for _ in range(n):
        s=input()[0]
        if(s=='b'): b+=1
        else: w+=1

    print("black" if(b>w) else "white")
resolve()

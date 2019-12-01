# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    for i in range(1,50001):
        k=int(i*1.08)
        if(n==k):
            print(i)
            return
        elif(n<k):
            print(":(")
            return
resolve()

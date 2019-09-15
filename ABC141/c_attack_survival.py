# https://atcoder.jp/contests/abc141/tasks/abc141_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,k,q=map(int,input().split())
    S=[0]*n
    for _ in range(q):
        S[int(input())-1]+=1
    for i in range(n):
        print('Yes' if k>q-S[i] else 'No') 
resolve()

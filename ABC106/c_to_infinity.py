# https://atcoder.jp/contests/abc106/tasks/abc106_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    s=input()
    k=int(input())
    for i in range(k):
        if(s[i]!='1'):
            print(int(s[i]))
            return
    print(1)
resolve()

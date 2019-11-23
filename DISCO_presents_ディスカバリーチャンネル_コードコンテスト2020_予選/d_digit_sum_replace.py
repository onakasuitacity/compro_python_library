# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    m=int(input())
    D=[0]*m;C=[0]*m
    for i in range(m):
        D[i],C[i]=map(int,input().split())

    digit=sum(D[i]*C[i] for i in range(m))
    print(sum(C)+(digit-1)//9-1)
resolve()

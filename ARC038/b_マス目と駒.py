# https://atcoder.jp/contests/arc038/tasks/arc038_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    h,w=map(int,input().split())
    G=[['#']*(w+2)]+[['#']+list(input())+['#'] for _ in range(h)]+[['#']*(w+2)]

    # grundy数 0 のマスを確定させる
    for i,j in product(range(1,h+1),range(1,w+1)):
        if(G[i][j]=='#'): continue
        if(G[i+1][j]=='#' and G[i][j+1]=='#' and G[i+1][j+1]=='#'):
            G[i][j]=0

    # 0 に遷移できれば 1、そうでなければ0を右下から確定させる
    for i,j in product(range(h,0,-1),range(w,0,-1)):
        if(G[i][j]!='.'): continue
        if(G[i+1][j]==0 or G[i][j+1]==0 or G[i+1][j+1]==0): G[i][j]=1
        else: G[i][j]=0

    print("First" if(G[1][1]) else "Second")
resolve()

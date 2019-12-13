# https://atcoder.jp/contests/arc040/tasks/arc040_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    G=[list(input()) for _ in range(n)]

    ans=0
    for i in range(n):
        if(not '.' in G[i]): continue # 行になければ何もしなくて良い
        ans+=1
        for j in range(n-1,-1,-1): # 塗られていない行の右端を取る
            if(G[i][j]=='.'): break
        # この行は塗ったとして、下の行を塗る
        if(i+1<n):
            for k in range(j,n):
                G[i+1][k]='o'

    print(ans)
resolve()

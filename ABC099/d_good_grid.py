# https://atcoder.jp/contests/abc099/tasks/abc099_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,c=map(int,input().split())
    D=[list(map(int,input().split())) for _ in range(c)]
    grid=[list(map(lambda x:int(x)-1,input().split())) for _ in range(n)]
    C=[[0]*c for _ in range(3)]

    # grid の色の集計をしておく (O(n^2))
    from itertools import product
    for i,j in product(range(n),repeat=2):
        col=grid[i][j]
        C[(i+j)%3][col]+=1

    # 3つそれぞれをどの色に変更するかを決めてスコアを計算する (O(c^4))
    ans=INF
    for u,v,w in product(range(c),repeat=3):
        if(u==v or v==w or w==u): continue
        score=0
        for col in range(c):
            score+=C[0][col]*D[col][u]
            score+=C[1][col]*D[col][v]
            score+=C[2][col]*D[col][w]
        ans=min(ans,score)

    print(ans)
resolve()

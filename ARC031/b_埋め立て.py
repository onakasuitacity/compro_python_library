# https://atcoder.jp/contests/arc031/tasks/arc031_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    G=[list(input()) for _ in range(10)]

    D=[(-1,0),(1,0),(0,-1),(0,1)]
    def connect():
        used=[[0]*10 for _ in range(10)]
        flag=False
        for i,j in product(range(10),repeat=2):
            if(G[i][j]=='x'): continue
            if(G[i][j]=='o' and (not flag)): # DFS
                Q=[(i,j)]
                used[i][j]=1
                while(Q):
                    i,j=Q.pop()
                    for di,dj in D:
                        ni=i+di; nj=j+dj
                        if(0<=ni<10 and 0<=nj<10):
                            if(used[ni][nj]==1): continue
                            if(G[ni][nj]=='o'):
                                used[ni][nj]=1
                                Q.append((ni,nj))
                flag=True
            if(G[i][j]=='o' and flag and (not used[i][j])):
                return False
        return True

    if(connect()):
        print("YES")
        return

    for i,j in product(range(10),repeat=2):
        if(G[i][j]=='o'): continue
        G[i][j]='o'
        if(connect()):
            print("YES")
            return
        G[i][j]='x'

    print("NO")
resolve()

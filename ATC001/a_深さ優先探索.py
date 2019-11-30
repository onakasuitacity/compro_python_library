# https://atc001.contest.atcoder.jp/tasks/dfs_a
### PyPyはTLE、PythonはAC ###
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    C=[['#']*(w+2)]+[list('#'+input()+'#') for _ in range(h)]+[['#']*(w+2)]
    # startの位置を確認
    start=[0,0]
    for i in range(1,h+1):
        for j in range(1,w+1):
            if C[i][j]=='s':
                start[0]=i; start[1]=j
                break
    # DFS
    def dfs(i,j):
        C[i][j]='#' # 埋める
        if C[i-1][j]=='g' or C[i+1][j]=='g' or C[i][j-1]=='g' or C[i][j+1]=='g':
            print("Yes")
            exit()
        if C[i-1][j]=='.': dfs(i-1,j)
        if C[i+1][j]=='.': dfs(i+1,j)
        if C[i][j-1]=='.': dfs(i,j-1)
        if C[i][j+1]=='.': dfs(i,j+1)
    dfs(*start)
    print("No")
resolve()

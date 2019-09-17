# https://atcoder.jp/contests/abc039/tasks/abc039_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    h,w=map(int,input().split())
    grid=[0]*(h+2)
    grid[0]=['#']*(w+2)
    grid[h+1]=['#']*(w+2)
    for i in range(h):
        grid[i+1]=['#']+list(input())+['#']
    from copy import deepcopy
    grid2=deepcopy(grid)
    from itertools import product
    for i,j in product(range(1,h+1),range(1,w+1)):
        if grid[i][j]=='.':
            grid2[i-1][j-1]='.'
            grid2[i-1][j]='.'
            grid2[i-1][j+1]='.'
            grid2[i][j-1]='.'
            grid2[i][j+1]='.'
            grid2[i+1][j-1]='.'
            grid2[i+1][j]='.'
            grid2[i+1][j+1]='.'
    grid3=deepcopy(grid2)
    for i,j in product(range(1,h+1),range(1,w+1)):
        if grid2[i][j]=='#':
            grid3[i-1][j-1]='#'
            grid3[i-1][j]='#'
            grid3[i-1][j+1]='#'
            grid3[i][j-1]='#'
            grid3[i][j+1]='#'
            grid3[i+1][j-1]='#'
            grid3[i+1][j]='#'
            grid3[i+1][j+1]='#'
    # judge
    flag=True
    for i,j in product(range(1,h+1),range(1,w+1)):
        flag=(grid[i][j]==grid3[i][j]) and flag
    # output
    if not flag:
        print("impossible")
        return
    else:
        print("possible")
        for s in grid2[1:h+1]:
            print(''.join(s[1:w+1]))
resolve()

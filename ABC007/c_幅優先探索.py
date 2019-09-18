# https://atcoder.jp/contests/abc007/tasks/abc007_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    m,n=map(int,input().split())
    start=tuple(map(lambda x:int(x)-1,input().split()))
    goal=tuple(map(lambda x:int(x)-1,input().split()))
    C=[list(input()) for _ in range(m)]
    C[start[0]][start[1]]=0
    from collections import deque
    Q=deque([(start[0],start[1],0)])
    while(Q):
        x,y,d=Q.popleft()
        C[x][y]=d
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            if C[x+dx][y+dy]=='.':
                C[x+dx][y+dy]=d+1
                Q.append((x+dx,y+dy,d+1))
    print(C[goal[0]][goal[1]])
resolve()

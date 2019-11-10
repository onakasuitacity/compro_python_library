# https://atcoder.jp/contests/abc109/tasks/abc109_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(h)]

    ans=[]
    for i in range(h):
        for j in range(w-1):
            if(grid[i][j]%2):
                ans.append((i+1,j+1,i+1,j+2))
                # print(i+1,j+1,i+1,j+2)
                grid[i][j+1]+=1

    for i in range(h-1):
        if(grid[i][w-1]%2):
            ans.append((i+1,w,i+2,w))
            # print(i+1,w,i+2,w)
            grid[i+1][w-1]+=1

    print(len(ans))
    for a in ans:
        print(*a)
resolve()

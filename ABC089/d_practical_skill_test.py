# https://atcoder.jp/contests/abc089/tasks/abc089_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w,d=map(int,input().split())
    grid=[]
    cnt=0
    for i in range(h):
        for j,a in enumerate(map(int,input().split())):
            a-=1
            grid.append((a,(i,j)))
    grid.sort()

    n=h*w
    A=list(map(lambda x:x[1],grid))
    C=[0]*n
    for r in range(d):
        for x in range(r,n-d,d):
            C[x+d]=C[x]+abs(A[x+d][0]-A[x][0])+abs(A[x+d][1]-A[x][1])

    for _ in range(int(input())):
        l,r=map(int,input().split())
        l-=1; r-=1
        print(C[r]-C[l])
resolve()

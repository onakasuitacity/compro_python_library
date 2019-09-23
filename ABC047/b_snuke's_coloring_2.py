# https://atcoder.jp/contests/abc047/tasks/abc047_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    w,h,n=map(int,input().split())
    A=[0,w,0,h] # xl,xh,yl,yh
    for _ in range(n):
        x,y,a=map(int,input().split())
        if a==1: A[0]=max(A[0],x)
        elif a==2: A[1]=min(A[1],x)
        elif a==3: A[2]=max(A[2],y)
        elif a==4: A[3]=min(A[3],y)
    print(max(0,A[1]-A[0])*max(0,A[3]-A[2]))
resolve()

# https://atcoder.jp/contests/abc069/tasks/arc080_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    n=int(input())
    A=[0]*(h*w)
    idx=0
    for i,a in enumerate(map(int,input().split())):
        cnt=0
        while(cnt<a):
            A[idx]=i+1
            cnt+=1
            idx+=1

    idx=0
    for i in range(h):
        G=[0]*w
        for j in range(w):
            G[j]=A[idx]
            idx+=1
        if(i&1): G=G[::-1]
        print(*G)
resolve()

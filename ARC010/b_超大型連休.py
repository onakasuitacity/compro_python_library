# https://atcoder.jp/contests/arc010/submissions/8957336
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import groupby
def resolve():
    H=[0]*367 # 1-indexed
    D=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(12):
        D[i+1]+=D[i]

    # sun,sat を埋める
    for i in range(1,367):
        if(i%7 in [0,1]):
            H[i]=1

    # 祝日を sort する
    n=int(input())
    A=[None]*n
    for i in range(n):
        m,d=map(int,input().split('/'))
        A[i]=d+D[m-1]
    A.sort()

    # 祝日を埋める
    for d in A:
        while(d<366 and H[d]==1): d+=1
        H[d]=1

    # 最長の 1 を求める
    ans=2
    for key,it in groupby(H):
        if(key==1):
            ans=max(ans,len(list(it)))

    print(ans)
resolve()

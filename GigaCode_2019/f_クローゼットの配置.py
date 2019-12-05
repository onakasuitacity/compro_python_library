# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def count_rectangle(Hist,B):
    Hist.append(0)
    res=0
    Q=[(-1,0)]
    for i,h in enumerate(Hist):
        while(Q[-1][1]>h):
            i0,h0=Q.pop()
            if(Q[-1][1]==h0): continue # 左と高さが同じ -> 極大長方形ではない
            if(Q[-1][0]<0): res+=(B[i-1]>0) # 左が-1 -> blockがあるかどうか
            else: res+=(B[i-1]>B[Q[-1][0]])
        if(Q[-1][1]<=h):
            Q.append((i,h))
    return res

from collections import defaultdict
from itertools import product
def resolve():
    h,w=map(int,input().split())
    n=int(input())
    C=[[1]*w for _ in range(h)]
    blocks=defaultdict(list)
    for _ in range(n):
        r,c=map(int,input().split())
        r-=1; c-=1
        C[r][c]=0
        blocks[r].append(c)
    blocks[h]=list(range(w)) # 一番下は全てブロックがあると考える

    # histgram 化しておく
    for i,j in product(range(h-1),range(w)):
        if(C[i+1][j]): C[i+1][j]+=C[i][j]

    ans=0
    for r,block in blocks.items():
        if(r==0): continue
        B=[0]*w
        for b in block: B[b]+=1
        for i in range(w-1): B[i+1]+=B[i] # block を左側から累積和を取る
        ans+=count_rectangle(C[r-1],B) # block とその1つ上の行の histgram から個数を数え上げる
    print(ans)
resolve()

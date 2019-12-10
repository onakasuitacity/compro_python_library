# https://atcoder.jp/contests/agc016/tasks/agc016_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    m=min(A); M=max(A)

    # 種類数が x だとして
    # 自分の色が他にいない -> x-1
    # 自分の色が他にいる -> x
    # よって M-m は1以下
    if(M-m>1):
        print("No")
        return

    # もし全員が同じ数字を言っている場合
    if(m==M):
        if(m==n-1): # 全てが1色ずつならOK
            print("Yes")
            return
        elif(m<=n//2): # 全てが2色以上ずつ用意できるならOK
            print("Yes")
            return
        else:
            print("No")
            return

    # もしズレがある場合
    s=A.count(m) # 自分だけの色を持つ数
    t=A.count(M) # 複数で色を共有する数
    # 色の種類は最小でs+1、最大でs+t//2
    if(s+1<=M<=s+t//2):
        print("Yes")
    else:
        print("No")

resolve()

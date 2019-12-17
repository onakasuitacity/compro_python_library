# https://atcoder.jp/contests/agc033/tasks/agc033_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    h,w,n=map(int,input().split())
    i0,j0=map(int,input().split())
    S=input()
    T=input()

    # 各ターンにおいて、駒が [u,d] x [l,r] にあれば後手の勝ち
    u,d,l,r=1,h,1,w
    for t,s in zip(T[::-1],S[::-1]):
        # 後手は存在範囲を(可能なら)広げられる
        if(t=='U'): d=min(h,d+1)
        elif(t=='D'): u=max(1,u-1)
        elif(t=='L'): r=min(w,r+1)
        elif(t=='R'): l=max(1,l-1)

        # 先手は存在範囲を(必ず)狭められる
        if(s=='U'): u+=1
        elif(s=='D'): d-=1
        elif(s=='L'): l+=1
        elif(s=='R'): r-=1

        # 駒の存在範囲が空集合ならば先手の勝ち
        if(u>d or l>r):
            print("NO")
            return

    # 開始時に駒が範囲にあるかどうかで判定
    print("YES" if(u<=i0<=d and l<=j0<=r) else "NO")
resolve()

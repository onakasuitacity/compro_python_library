# https://atcoder.jp/contests/abc051/tasks/abc051_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    sx,sy,tx,ty=map(int,input().split())
    x,y=tx-sx,ty-sy
    ans=''
    # 1往復目
    ans=ans+'R'*x+'U'*y+'L'*x+'D'*y
    # 2往復目
    ans=ans+'D'+'R'*(x+1)+'U'*(y+1)+'L'+'U'+'L'*(x+1)+'D'*(y+1)+'R'
    print(ans)
resolve()

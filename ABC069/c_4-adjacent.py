# https://atcoder.jp/contests/abc069/tasks/arc080_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    int(input())
    cnt=[0]*3
    for a in map(int,input().split()):
        if(a%4==0): cnt[2]+=1
        elif(a%2==0): cnt[1]+=1
        else: cnt[0]+=1
    if(cnt[1]): cnt[0]+=1
    print("Yes" if(cnt[2]>=cnt[0]-1) else "No")
resolve()

# https://atcoder.jp/contests/abc064/tasks/abc064_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    C=[0]*9
    n=int(input())
    for a in map(int,input().split()):
        s=a//400
        if(s>=8): C[8]+=1
        else: C[s]+=1

    cnt=sum(1 for i in range(8) if(C[i]))
    print(max(1,cnt),cnt+C[-1])
resolve()

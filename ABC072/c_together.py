# https://atcoder.jp/contests/abc072/tasks/arc082_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    M=10**5
    n=int(input())
    C=[0]*M
    for a in map(int,input().split()):
        C[a]+=1
    print(max(*(C[i-1]+C[i]+C[i+1] for i in range(1,M-1))))
resolve()

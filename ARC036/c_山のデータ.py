# https://atcoder.jp/contests/arc036/tasks/arc036_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    H=[int(input()) for _ in range(n)]
    left=[1]*n
    right=[1]*n

    for i in range(n-1):
        if(H[i+1]>H[i]):
            left[i+1]+=left[i]

    for i in range(n-1,0,-1):
        if(H[i-1]>H[i]):
            right[i-1]+=right[i]

    print(max(l+r for l,r in zip(left,right))-1)
resolve()

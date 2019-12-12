# https://atcoder.jp/contests/arc071/tasks/arc071_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    # 全部 A にした時に、差が3の約数なら良さそう
    S=[1 if(s=='A') else 2 for s in input()]
    T=[1 if(s=='A') else 2 for s in input()]

    # cumsum
    m=len(S)
    n=len(T)
    CS=[0]*(m+1)
    for i in range(m):
        CS[i+1]=CS[i]+S[i]

    CT=[0]*(n+1)
    for i in range(n):
        CT[i+1]=CT[i]+T[i]

    # output
    for _ in range(int(input())):
        a,b,c,d=map(int,input().split())
        a-=1; c-=1
        k=abs((CS[b]-CS[a])-(CT[d]-CT[c]))
        print("YES" if(k%3==0) else "NO")
resolve()

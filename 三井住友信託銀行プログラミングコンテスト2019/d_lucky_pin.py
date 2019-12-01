# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from bisect import bisect_left as bisect
def resolve():
    n=int(input())
    S=input()
    C=[[] for _ in range(10)]
    for i,s in enumerate(S):
        C[int(s)].append(i)

    ans=0
    for i in range(1000):
        i=str(i)
        i=i.zfill(3)
        now=0
        flag=True
        for d in i:
            d=int(d)
            j=bisect(C[d],now)
            if(j==len(C[d])):
                flag=False
                break
            now=C[d][j]+1
        ans+=flag
    print(ans)
resolve()

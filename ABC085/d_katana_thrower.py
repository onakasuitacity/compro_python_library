# https://atcoder.jp/contests/abc085/tasks/abc085_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from math import ceil
def resolve():
    n,h=map(int,input().split())
    AB=[tuple(map(int,input().split())) for _ in range(n)]

    # a が最大のうち、bが最小のものを取りだす
    AB.sort(lambda x:(x[0],-x[1]))
    ma,mb=AB.pop()

    # 残りのうち b が大きい順に投げ続ける
    AB.sort(lambda x:-x[1])
    ans=0
    for i in range(n-1):
        a,b=AB[i]
        if(b<=ma): break
        h-=b
        ans+=1
        if(h<=0):
            print(ans)
            return
    ans+=min(ceil(h/ma),ceil((h-mb)/ma)+1)
    print(ans)
resolve()

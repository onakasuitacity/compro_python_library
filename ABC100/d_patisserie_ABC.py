# https://atcoder.jp/contests/abc100/tasks/abc100_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    XYZ=[tuple(map(int,input().split())) for _ in range(n)]
    ans=-INF

    from itertools import product
    for cx,cy,cz in product(range(2),repeat=3):
        XYZ.sort(lambda a:(2*cx-1)*a[0]+(2*cy-1)*a[1]+(2*cz-1)*a[2],reverse=1)
        score=0
        for i in range(m):
            a=XYZ[i]
            score+=(2*cx-1)*a[0]+(2*cy-1)*a[1]+(2*cz-1)*a[2]
        ans=max(ans,score)
    print(ans)
resolve()

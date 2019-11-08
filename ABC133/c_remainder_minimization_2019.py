# https://atcoder.jp/contests/abc133/tasks/abc133_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    L,R=map(int,input().split())
    d=R-L
    L%=2019
    d=min(d,2019)
    from itertools import product
    ans=INF
    for i,j in product(range(d+1),repeat=2):
        if(i>=j): continue
        ans=min(ans,(L+i)*(L+j)%2019)
    print(ans)
resolve()

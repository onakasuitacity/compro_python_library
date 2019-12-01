# https://atcoder.jp/contests/abc029/tasks/abc029_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    n=input()
    
    dp=[[0]*2 for _ in range(11)]
    dp[0][0]=1
    for a in n:
        ndp=[[0]*2 for _ in range(11)]
        a=int(a)
        for i,d,lt in product(range(10),range(10),range(2)):
            nlt=lt
            ni=i+(d==1)
            if((not lt) and a<d): continue
            if(a>d): nlt=1
            ndp[ni][nlt]+=dp[i][lt]
        dp=ndp
    
    ans=0
    for i in range(10):
        ans+=sum(dp[i])*i
    print(ans)
resolve()

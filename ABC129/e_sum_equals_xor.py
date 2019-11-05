# https://atcoder.jp/contests/abc129/tasks/abc129_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import product
    L=input()
    dp=[1,0]
    for d in range(len(L)):
        ndp=[0,0]
        Ld=int(L[d])
        for lt,a,b in product(range(2),repeat=3):
            nlt=lt
            if(a==1 and b==1): continue
            if(lt==0 and (a==1 or b==1) and Ld==0): continue
            if(a==0 and b==0 and Ld==1): nlt=1
            ndp[nlt]+=dp[lt]
            ndp[nlt]%=MOD
        dp=ndp
    print(sum(dp)%MOD)
resolve()

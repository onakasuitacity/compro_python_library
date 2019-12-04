# https://atcoder.jp/contests/abc020/tasks/abc020_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]

def resolve():
    n,k=map(int,input().split())
    D=divisors(k)
    C={}
    for d in D:
        s=d*(n//d) # n 以下で最大の d の倍数
        t=n//d # n 以下の d の倍数の個数
        C[d]=(d+s)*t//2 # 等差数列の和
    
    # 約数包除
    for d in D[::-1]:
        for d1 in D:
            if(d1>d and d1%d==0):
                C[d]-=C[d1]

    ans=0
    for key,val in C.items():
        ans+=(k//key)*val
        ans%=MOD
    print(ans)
resolve()

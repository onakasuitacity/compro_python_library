# https://atcoder.jp/contests/agc039/tasks/agc039_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=998244353
input=lambda :sys.stdin.readline().rstrip()
def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]

def resolve():
    N=int(input())
    x=input()
    y=''.join('1' if c=='0' else '0' for c in x) # xのbit反転
    D=divisors(N)
    C={d:0 for d in D} # x以下の数字のうち、周期2dの個数
    for d in D:
        if (N//d)%2==0: continue # N/dがevenなら0個
        else:
            z=(x[:d]+y[:d])*((N//d-1)//2)+x[:d]
            C[d]=int(x[:d],2)+1-(x<z)
            C[d]%=MOD
    # ここでC[d]を約数包除で最小周期2dの個数に更新
    for d in D:
        for d1 in D:
            if (d%d1==0 and d!=d1):
                C[d]-=C[d1]
    ans=0
    for d in D:
        ans+=2*d*C[d]%MOD
    print(ans%MOD)
resolve()

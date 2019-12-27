# https://atcoder.jp/contests/agc005/tasks/agc005_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    X=input()
    Q=[]
    ans=0
    for c in X:
        if(c=='T' and Q and Q[-1]=='S'): Q.pop()
        else: Q.append(c)
    print(len(Q))
resolve()

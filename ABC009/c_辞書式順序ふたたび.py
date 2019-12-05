# https://atcoder.jp/contests/abc009/tasks/abc009_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    n,k=map(int,input().split())
    S=input()
    C=Counter(S)
    C=[[key,val] for key,val in C.items()]
    C.sort()

    def check(T):
        cnt=sum(1 for s,t in zip(S,T) if(s!=t)) # prefix のズレ
        extra=Counter(S)-Counter(T) # 残りの文字
        extra-=Counter(S[len(T):]) # suffix で相殺できない文字
        cnt+=sum(extra.values())
        return cnt<=k

    ans=''
    for _ in range(n):
        for i in range(len(C)):
            if(C[i][1] and check(ans+C[i][0])):
                ans+=C[i][0]
                C[i][1]-=1
                break

    print(ans)
resolve()

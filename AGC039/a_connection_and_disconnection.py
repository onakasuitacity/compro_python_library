# https://atcoder.jp/contests/agc039/tasks/agc039_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import groupby
    s=input()
    k=int(input())
    t=groupby(s)
    S=[]
    for tup in t: S.append((tup[0],len(list(tup[1]))))
    if len(S)==1:
        print(len(s)*k//2)
        return
    if s[0]==s[-1]:
        p=0 # s自体で変更する数
        for a,b in S[1:-1]:
            p+=b//2
        q=(S[0][1]+S[-1][1])//2
        ans=p*k+q*(k-1)
        ans+=S[0][1]//2+S[-1][1]//2
        print(ans)
    else:
        p=0
        for a,b in S:
            p+=b//2
        ans=p*k
        print(ans)
resolve()

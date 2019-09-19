# https://atcoder.jp/contests/abc035/tasks/abc035_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    t=int(input())
    p=[0,0]
    q=0
    for s in S:
        if s=='L': p[0]-=1
        elif s=='R': p[0]+=1
        elif s=='D': p[1]-=1
        elif s=='U': p[1]+=1
        else: q+=1
    m=abs(p[0])+abs(p[1])
    if t==1:
        print(m+q)
    else:
        if m-q>=0: print(m-q)
        else:
            print(0 if (m+q)%2==0 else 1)
resolve()

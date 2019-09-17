# https://atcoder.jp/contests/abc128/tasks/abc128_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    switch=[0]*n
    for i in reversed(range(m)):
        k,*S=map(int,input().split())
        for s in S:
            switch[s-1]+=1<<i
    p=int(input().replace(' ',''),2)
    # calculate
    ans=0
    for k in range(2**n):
        xor=0
        for i in range(n):
            if k&(1<<i):
                xor^=switch[i]
        if xor==p: ans+=1
    print(ans)
resolve()

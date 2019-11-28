# https://atcoder.jp/contests/abc053/tasks/arc068_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    input()
    C=Counter(map(int,input().split()))
    C=[v for k,v in C.most_common()[::-1]]
    n=len(C)
    for i in range(n):
        if(C[i]==1): continue
        C[i]=1 if(C[i]&1) else 2
        if(i<n-1 and C[i]==2):
            C[i+1]-=1
    print(n-(C[-1]==2))
resolve()

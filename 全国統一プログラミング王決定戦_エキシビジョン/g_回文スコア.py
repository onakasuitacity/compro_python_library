# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_g
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=input()
    C=[0]*26
    for s in S:
        c=ord(s)-ord('a')
        C[c]+=1

    l=0
    for i in range(26):
        l+=C[i]-(C[i]&1)
        C[i]&=1

    if(max(C)==1):
        print((l+1)**2+sum(C)-1)
    else:
        print(l**2+sum(C))
resolve()

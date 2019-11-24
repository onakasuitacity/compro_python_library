# https://atcoder.jp/contests/abc146/tasks/abc146_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    S=list(input())
    S=list(map(ord,S))
    for i in range(len(S)):
        s=S[i]
        S[i]=65+(s+n-65)%26
    S=list(map(chr,S))
    print(''.join(S))
resolve()

# https://atcoder.jp/contests/abc048/tasks/arc064_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    print("First" if((len(S)&1)^(S[0]==S[-1])) else "Second")
resolve()

# https://atcoder.jp/contests/abc132/tasks/abc132_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from collections import Counter
    C=Counter(input())
    if(len(C)!=2):
        print("No")
        return
    for k,v in C.items():
        if(v!=2):
            print("No")
            return
    print("Yes")
resolve()

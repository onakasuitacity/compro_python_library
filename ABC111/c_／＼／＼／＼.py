# https://atcoder.jp/contests/abc111/tasks/arc103_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input()) # even
    V=list(map(int,input().split()))
    # 1種類しかないときはindexの関係上別処理する
    if len(set(V))==1:
        print(n//2)
        return
    from collections import Counter
    E=Counter(V[::2]).most_common() # list of tuple
    O=Counter(V[1::2]).most_common()
    if E[0][0]!=O[0][0]:
        print(n-E[0][1]-O[0][1])
    elif E[0][1]>O[0][1]:
        print(n-E[0][1]-O[1][1])
    elif E[0][1]<O[0][1]:
        print(n-E[1][1]-O[0][1])
    else:
        print(min(n-E[0][1]-O[1][1],n-E[1][1]-O[0][1]))
resolve()

# https://atcoder.jp/contests/abc082/tasks/arc087_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    from collections import Counter
    C=Counter(map(int,input().split()))
    ans=0
    for k,v in C.items():
        ans+=v if v<k else v-k
    print(ans)
resolve()

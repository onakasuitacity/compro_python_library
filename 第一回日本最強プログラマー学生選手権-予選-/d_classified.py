# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    for u in range(n-1):
        ans=[]
        for v in range(u+1,n):
            w=u^v
            for i in range(10):
                if((w>>i)&1):
                    ans.append(i+1)
                    break
        print(*ans)
resolve()

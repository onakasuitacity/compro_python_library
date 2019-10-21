# https://atcoder.jp/contests/abc143/tasks/abc143_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    L=list(map(int,input().split()))
    L.sort()
    ans=0
    for b in range(n):
        c=b+1
        for a in range(b):
            while(1):
                if(c>=n or L[a]+L[b]<=L[c]): break
                c+=1
            ans+=c-(b+1)
    print(ans)
resolve()

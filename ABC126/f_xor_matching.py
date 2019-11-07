# https://atcoder.jp/contests/abc126/tasks/abc126_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    m,k=map(int,input().split())
    if(m==1):
        if(k>=1):
            print(-1)
            return
        else:
            print(0,0,1,1)
            return
    elif(k>=2**m):
        print(-1)
        return
    n=2**m
    ans=[]
    ans+=list(range(k-1,-1,-1))
    ans.append(k)
    ans+=list(range(k))
    ans+=list(range(k+1,n))
    ans.append(k)
    ans+=list(range(n-1,k,-1))
    print(*ans)
resolve()

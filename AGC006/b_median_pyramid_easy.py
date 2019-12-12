# https://atcoder.jp/contests/agc006/tasks/agc006_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def resolve():
    n,x=map(int,input().split())
    if(x!=1 and x!=2*n-1):
        print("Yes")
    else:
        print("No")
        return

    if(n==2):
        print(1,2,3)
        return

    if(x!=2):
        ans=[i for i in range(1,2*n) if(i not in [x-2,x-1,x,x+1])]
        ans=ans[:n-2]+[x-2,x,x+1,x-1]+ans[n-2:]
        print(*ans)
    else:
        ans=[i for i in range(5,2*n)]
        ans=ans[:n-2]+[1,2,4,3]+ans[n-2:]
        print(*ans)
resolve()

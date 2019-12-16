# https://atcoder.jp/contests/arc034/tasks/arc034_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    dsum=lambda x:sum(map(int,str(x)))

    ans=[]
    for x in range(max(0,n-300),n+1):
        if(x+dsum(x)==n):
            ans.append(x)

    print(len(ans))
    if(ans):
        print(*ans,sep='\n')
resolve()

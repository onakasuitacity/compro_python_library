# https://atcoder.jp/contests/abc147/tasks/abc147_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    E=[None]*n
    for i in range(n):
        a=int(input())
        XY=[tuple(map(int,input().split())) for _ in range(a)]
        E[i]=XY

    N=2**n
    ans=0
    for S in range(N):
        flag=True
        for i in range(n):
            if((S>>i)&1)==0: continue # 正直者のみを見る
            for x,y in E[i]:
                x-=1
                if((S>>x)&1)!=y:
                    flag=False
        if(flag):
            ans=max(ans,bin(S).count('1'))
    print(ans)
resolve()

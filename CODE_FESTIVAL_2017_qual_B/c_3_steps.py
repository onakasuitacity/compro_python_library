# https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for i in range(m):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[u].append(v)
        E[v].append(u)

    # bipartite check
    col=[-1]*n
    col[0]=0
    Q=[0]
    while(Q):
        v=Q.pop()
        for nv in E[v]:
            if(col[v]==col[nv]): # 二部グラフではない -> 全部繋げられる
                print(n*(n-1)//2-m)
                return
            elif(col[nv]!=-1 and col[nv]^col[v]): continue
            col[nv]=1-col[v]
            Q.append(nv)

    # 二部グラフ -> 偶数と奇数とが繋げられる
    even=col.count(0)
    odd=col.count(1)
    print(even*odd-m)
resolve()

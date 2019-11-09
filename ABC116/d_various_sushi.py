# https://atcoder.jp/contests/abc116/tasks/abc116_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from heapq import heappop,heappush
    n,k=map(int,input().split())
    A=[0]*n
    for i in range(n):
        t,d=map(int,input().split())
        t-=1
        A[i]=(t,d)
    A.sort(lambda x:-x[1]) # d の降順ソート

    # 各種の中で最大かどうかをわける
    B=[0]*n
    first=[1]*n
    for i,a in enumerate(A):
        t,d=a
        if(first[t]):
            first[t]=0
            B[i]=(d,1)
        else:
            B[i]=(d,0)

    # 初めは貪欲に d の大きい方から k 個取る
    S=[]
    for i in range(k):
        d,f=B[i]
        heappush(S,(f,d))
    x=sum(S[i][1] for i in range(k))
    y=sum(S[i][0] for i in range(k))
    ans=x+y*y

    # 残りの n-k について、Sからf=0で最小のものを捨て、B[k:]からf=1の中で最大のものを加える
    B=B[k:]
    for i in range(n-k):
        d,f=B[i]
        if(f==0): continue
        pf,pd=heappop(S)
        if(pf==1): break
        x+=d-pd
        y+=1
        ans=max(ans,x+y*y)
    print(ans)
resolve()

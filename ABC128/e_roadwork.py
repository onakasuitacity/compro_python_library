# https://atcoder.jp/contests/abc128/tasks/abc128_e
# PyPyだとTLE
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,q=map(int,input().split())
    S,T,X=[0]*n,[0]*n,[0]*n
    D=[0]*q
    for i in range(n):
        S[i],T[i],X[i]=map(int,input().split())
    for j in range(q):
        D[j]=int(input())

    E=[]
    E+=[(s-x,1,x) for s,x in zip(S,X)]
    E+=[(t-x,2,x) for t,x in zip(T,X)]
    E+=[(d,3,i) for i,d in enumerate(D)]
    E.sort()
    from collections import defaultdict
    cnt=defaultdict(int)
    cnt[INF]=1

    from heapq import heappop,heappush
    Q=[INF]
    ans=[-1]*q
    for a,b,c in E:
        if(b==1):
            heappush(Q,c)
            cnt[c]+=1
        elif(b==2): # 本来はここでqからcを削除したいが、できないためb==3で処理する
            cnt[c]-=1
        else:
            while(cnt[Q[0]]==0): # 本来削除されるべき通行止めをここで消す
                heappop(Q)
            x=Q[0]
            if(x!=INF): ans[c]=x
    print(*ans,sep="\n")
resolve()

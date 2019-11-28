# https://atcoder.jp/contests/abc146/tasks/abc146_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

class SWAG(object):
    def __init__(self,dot):
        self.__front=[]; self.__back=[]; self.__dot=dot

    def __bool__(self):
        return bool(self.__front or self.__back)

    def __len__(self):
        return len(self.__front)+len(self.__back)

    def append(self,x):
        back=self.__back
        if(not back): back.append((x,x))
        else: back.append((x,self.__dot(back[-1][1],x)))

    def popleft(self):
        assert(self)
        front=self.__front; back=self.__back
        if(not front):
            front.append((back[-1][0],back[-1][0]))
            back.pop()
            while(back):
                front.append((back[-1][0],self.__dot(back[-1][0],front[-1][1])))
                back.pop()
        return front.pop()[0]

    def sum(self):
        assert(self)
        front=self.__front; back=self.__back
        if(not front): return back[-1][1]
        elif(not back): return front[-1][1]
        else: return self.__dot(front[-1][1],back[-1][1])

def resolve():
    # input
    n,m=map(int,input().split())
    S=list(map(int,input()))

    # dp
    swag=SWAG(min)
    dp=[None]*(n+1)
    dp[n]=0
    for i in range(n-1,-1,-1):
        swag.append(dp[i+1])
        dp[i]=swag.sum()+1 if(S[i]==0) else INF
        if(len(swag)==m): swag.popleft()

    # output
    if(dp[0]==INF):
        print("-1")
        return
    ans=[]
    now=next=0
    while(now<n):
        next+=1
        if(dp[now]>dp[next]):
            ans.append(next-now)
            now=next
    print(*ans)
resolve()

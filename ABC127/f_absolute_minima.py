# https://atcoder.jp/contests/abc127/tasks/abc127_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    k=int(input())
    score=0
    B=0

    from heapq import heappush,heappop
    q=[] # 小さいほうの最大をとる→マイナスにして入れる
    Q=[] # 大きいほうの最小をとる

    for _ in range(k):
        s=input()
        if(s[0]=='1'):
            s,a,b=map(int,s.split())
            heappush(q,-a)
            heappush(Q,a)
            B+=b
            # 大小関係が逆転しているかを判断する
            t=-q[0]; T=Q[0]
            if(t>T):
                score+=t-T
                heappop(q); heappop(Q)
                heappush(q,-T); heappush(Q,t)
        else:
            print(-q[0],score+B)
resolve()

# https://atcoder.jp/contests/arc040/tasks/arc040_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,r=map(int,input().split())
    S=list(input())

    # 何もする必要がないときは例外処理
    if(all(s=='o' for s in S)):
        print(0)
        return

    # 一番右端の '.' を見つける
    e=n-S[::-1].index('.')-1
    # 最後に塗るのは e にギリギリ届く場所
    e=max(0,e-r+1)

    # 自分の足元が塗られていないか、e であるときに塗る
    now=0
    ans=0
    while(1):
        if(S[now]=='.' or now==e):
            for i in range(now,min(now+r,n)):
                S[i]='o'
            ans+=1
        if(now==e):
            break
        now+=1
        ans+=1

    print(ans)
resolve()

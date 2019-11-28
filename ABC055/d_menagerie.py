# https://atcoder.jp/contests/abc055/tasks/arc069_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    S=list(map(lambda x:(x=='o')-0,input()))

    # 4パターン試す
    from itertools import product
    for a,b in product(range(2),repeat=2):
        ans=[None]*n
        ans[0]=a; ans[1]=b

        for i in range(2,n):
            if(S[i-1]==ans[i-1]): ans[i]=ans[i-2]
            else: ans[i]=1-ans[i-2]

        if((S[0]==ans[0])==(ans[1]==ans[-1]) and (S[-1]==ans[-1])==(ans[0]==ans[-2])):
            for s in ans: print('S' if(s) else 'W',end='')
            print()
            return
    print(-1)
resolve()

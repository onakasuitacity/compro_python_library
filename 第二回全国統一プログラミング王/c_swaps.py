# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    X=[(a,b) for a,b in zip(A,B)]
    X.sort(lambda x:x[1])

    # B を先に昇順ソートしておき、それに応じて A の順序を定める
    A=[X[i][0] for i in range(n)]
    B=[X[i][1] for i in range(n)]
    # Aのソート結果のインデックスを保持する
    C=[(a,i) for i,a in enumerate(A)]
    C.sort()

    # 最適な場合でも不可能なときはNo
    if(any(C[i][0]>B[i] for i in range(n))):
        print("No")
        return

    # 自由度が1つ以上あればYes
    if(any(C[i+1][0]<=B[i] for i in range(n-1))):
        print("Yes")
        return

    # この時点で A に値の重複は無いので、A のソートのサイクルを見る
    I=[C[i][1] for i in range(n)]
    x=0
    cnt=0
    while(True):
        cnt+=1
        x=I[x]
        if(x==0): break

    # サイクルが1つの場合は不可能、それ以外は可能
    if(cnt<n):
        print("Yes")
    else:
        print("No")
resolve()

# https://atcoder.jp/contests/abc073/tasks/abc073_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m,r=map(int,input().split())
    R=list(map(lambda x:int(x)-1,input().split()))
    # Adjacency Matrix
    A=[[INF]*n for _ in range(n)]
    for i in range(n): A[i][i]=0
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1
        b-=1
        A[a][b]=c
        A[b][a]=c
    # Warshall-Floyd
    from itertools import product
    for k,i,j in product(range(n),repeat=3):
        A[i][j]=min(A[i][j],A[i][k]+A[k][j])
    # calculate
    from itertools import permutations
    per=permutations(R)
    ans=INF
    for R in per:
        score=0
        for i in range(r-1):
            score+=A[R[i]][R[i+1]]
        ans=min(ans,score)
    print(ans)

resolve()

# https://atcoder.jp/contests/abc012/tasks/abc012_4
def resolve():
    # import
    from itertools import product

    # input
    n,m=map(int,input().split())

    # initialization
    A=[[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n): A[i][i]=0

    # input cost
    for _ in range(m):
        a,b,t=map(int,input().split())
        A[a-1][b-1]=t
        A[b-1][a-1]=t

    # Warshall–Floyd
    for k,i,j in product(range(n),range(n),range(n)):
        A[i][j]=min(A[i][j],A[i][k]+A[k][j])

    print(min(max(a) for a in A))
resolve()

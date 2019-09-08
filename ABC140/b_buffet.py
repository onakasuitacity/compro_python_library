# https://atcoder.jp/contests/abc140/tasks/abc140_b
def resolve():
    n=int(input())
    A=list(map(lambda x:int(x)-1,input().split()))
    ans=sum(map(int,input().split()))
    C=list(map(int,input().split()))

    for i in range(n-1):
        if A[i+1]-A[i]==1: ans+=C[A[i]]

    print(ans)
resolve()

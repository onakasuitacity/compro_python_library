# https://atcoder.jp/contests/abc140/tasks/abc140_c
def resolve():
    n=int(input())
    B=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if i==0: ans+=B[i]
        elif i==n-1: ans+=B[i-1]
        else: ans+=min(B[i-1],B[i])
    print(ans)
resolve()

# https://atcoder.jp/contests/abc087/tasks/arc090_a
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans=max(ans,sum(A[:i+1]+B[i:]))
    print(ans)
resolve()

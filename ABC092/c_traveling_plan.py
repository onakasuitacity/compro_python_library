# https://atcoder.jp/contests/abc092/tasks/arc093_a
def resolve():
    n=int(input())
    A=[int(i) for i in input().split()]
    B=[A[0]]+[A[i+1]-A[i] for i in range(n-1)]+[-A[n-1]]
    abssum=sum(abs(b) for b in B)
    for i in range(n):
        print(abssum-abs(B[i])-abs(B[i+1])+abs(B[i]+B[i+1]))
resolve()

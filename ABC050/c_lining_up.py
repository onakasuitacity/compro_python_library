# https://atcoder.jp/contests/abc050/tasks/arc066_a
def resolve():
    n=int(input())
    A=sorted(list(map(int,input().split())))
    if n%2:
        A.insert(0,0)
        flag=all(A[2*i]==2*i and A[2*i+1]==2*i for i in range(len(A)//2))
    else:
        flag=all(A[2*i]==2*i+1 and A[2*i+1]==2*i+1 for i in range(len(A)//2))
    print(2**(n//2)%(10**9+7) if flag else 0)
resolve()

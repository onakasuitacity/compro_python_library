# https://atcoder.jp/contests/abc098/tasks/arc098_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    s=input()
    A=[0]*n # A[i]: i番目までのWの数
    count=0
    for i in range(n):
        if s[i]=='W': count+=1
        A[i]=count
    ans=INF
    for i in range(n):
        if i==0:
            ans=min(ans,n-1-(A[n-1]-A[0]))
        elif i==n-1:
            ans=min(ans,A[n-2])
        else:
            ans=min(ans,A[i-1]+n-i-1-(A[n-1]-A[i]))
    print(ans)
resolve()

# https://atcoder.jp/contests/abc071/tasks/arc081_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[list(input()) for _ in range(2)]
    ans=1
    i=0
    while(i<n):
        # 縦に置かれているとき
        if(A[0][i]==A[1][i]):
            if(i==0): ans*=3
            elif(A[0][i-1]==A[1][i-1]): ans*=2
            else: pass
            i+=1
        # 横に置かれているとき
        else:
            if(i==0): ans*=6
            elif(A[0][i-1]==A[1][i-1]): ans*=2
            else: ans*=3
            i+=2

    print(ans%MOD)
resolve()

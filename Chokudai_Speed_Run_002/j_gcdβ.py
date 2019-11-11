# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_j
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]

def resolve():
    n=int(input())
    A,B=map(int,input().split())
    A=divisors(A)
    B=divisors(B)
    X=A+B
    AB=[0]*(n-1)
    for i in range(n-1):
        AB[i]=tuple(map(int,input().split()))

    def check(d):
        for a,b in AB:
            if(a%d and b%d):
                return False
        return True

    ans=0
    for d in X:
        if(check(d)): ans=max(ans,d)
    print(ans)
resolve()

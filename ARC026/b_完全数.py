# https://atcoder.jp/contests/arc026/tasks/arc026_2
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
    D=divisors(n)
    s=sum(D)-2*n
    if(s<0):
        print("Deficient")
    elif(s==0):
        print("Perfect")
    else:
        print("Abundant")
resolve()

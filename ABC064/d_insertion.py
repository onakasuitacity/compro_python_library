# https://atcoder.jp/contests/abc064/tasks/abc064_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    S=input()
    a=0
    b=0

    for i in range(n):
        if(S[i]=='('):
            a+=1
        else:
            if(a>0): a-=1
            else: b+=1
    P='('*b

    a=0
    b=0
    for i in range(n-1,-1,-1):
        if(S[i]==')'):
            a+=1
        else:
            if(a>0): a-=1
            else: b+=1
    Q=')'*b
    print(P+S+Q)
resolve()

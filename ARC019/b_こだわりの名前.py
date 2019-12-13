# https://atcoder.jp/contests/arc019/tasks/arc019_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=input()
    n=len(S)
    d=sum(s!=t for s,t in zip(S,S[::-1]))//2

    if(d==0): # 既に回文のとき
        if(n&1):
            print(25*(n-1))
        else:
            print(25*n)

    elif(d==1): # 回文との差が 1 のとき
        print(25*n-2)

    elif(d>=2): # 回文との差が 2 以上のとき
        print(25*n)
resolve()

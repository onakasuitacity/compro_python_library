# https://atcoder.jp/contests/abc146/tasks/abc146_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    if(S=="SUN"):
        print(7)
    elif(S=="MON"):
        print(6)
    elif(S=="TUE"):
        print(5)
    elif(S=="WED"):
        print(4)
    elif(S=="THU"):
        print(3)
    elif(S=="FRI"):
        print(2)
    else:
        print(1)
resolve()

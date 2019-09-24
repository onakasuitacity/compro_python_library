# https://atcoder.jp/contests/arc023/tasks/arc023_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    y,m,d=[int(input()) for _ in range(3)]
    if m in (1,2):
        y-=1
        m+=12
    f=lambda y,m,d:365*y+y//4-y//100+y//400+(306*(m+1))//10+d-429
    print(f(2014,5,17)-f(y,m,d))
resolve()

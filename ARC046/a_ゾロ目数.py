# https://atcoder.jp/contests/arc046/tasks/arc046_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())-1
    p,q=n//9+1,n%9+1
    print(int(str(q)*p))
resolve()

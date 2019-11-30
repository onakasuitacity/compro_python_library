# https://atcoder.jp/contests/abc042/tasks/arc058_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    D=set(map(int,input().split()))
    for i in range(n,100000):
        flag=True
        for s in str(i):
            if(int(s) in D):
                flag=False
        if(flag):
            print(i)
            return
resolve()

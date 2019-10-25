# https://atcoder.jp/contests/abc056/tasks/arc070_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x=int(input())
    ans=0
    while(ans*(ans+1)<2*x): ans+=1
    print(ans)
resolve()

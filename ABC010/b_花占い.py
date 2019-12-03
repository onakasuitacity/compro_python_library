# https://atcoder.jp/contests/abc010/tasks/abc010_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    ans=0
    int(input())
    for a in map(int,input().split()):
        if(a%6==2): ans+=1
        elif(a%6==4): ans+=1
        elif(a%6==5): ans+=2
        elif(a%6==0): ans+=3
    print(ans)
resolve()

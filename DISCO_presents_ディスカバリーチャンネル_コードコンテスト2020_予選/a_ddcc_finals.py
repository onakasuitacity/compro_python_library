# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x,y=map(int,input().split())
    ans=0
    if(x==1):
        ans+=3
    elif(x==2):
        ans+=2
    elif(x==3):
        ans+=1
    if(y==1):
        ans+=3
    elif(y==2):
        ans+=2
    elif(y==3):
        ans+=1
    if(x==1 and y==1):
        ans+=4
    print(ans*100000)
resolve()

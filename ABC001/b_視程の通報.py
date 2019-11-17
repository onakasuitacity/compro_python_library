# https://atcoder.jp/contests/abc001/tasks/abc001_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    m=int(input())
    if(m<100):
        print("00")
    elif(m<=5000):
        m//=100
        m=str(m)
        print(m.zfill(2))
    elif(m<=30000):
        m//=1000
        print(m+50)
    elif(m<=70000):
        m//=1000
        m=(m-30)//5
        print(m+80)
    else:
        print(89)
resolve()

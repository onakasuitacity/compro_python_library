# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    t1,t2=map(int,input().split())
    a1,a2=map(int,input().split())
    b1,b2=map(int,input().split())
    v1=a1-b1
    v2=a2-b2

    # v1とv2が同符号なら0回
    if(v1*v2>0):
        print(0)
        return
    # v1t1+v2t2 が0ならば無限
    if(v1*t1+v2*t2==0):
        print("infinity")
        return
    # abs(v1t1)>abs(v2t2)ならば0回
    if(abs(v1*t1)>abs(v2*t2)):
        print(0)
        return

    # 以下、v1を負の方の大きさ、v2を正の方の大きさとする
    v1=abs(v1); v2=abs(v2)
    d=v2*t2-v1*t1

    ans=-1
    ans-=(v1*t1%d==0)
    k=(v1*t1-1)//d+1+(v1*t1%d==0)
    ans+=2*k
    print(ans)
resolve()

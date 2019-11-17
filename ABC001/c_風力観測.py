# https://atcoder.jp/contests/abc001/tasks/abc001_3
# PyPyだとMLE
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    a*=10
    if(a>=34875 or a<1125):
        d="N"
    elif(a<3375):
        d="NNE"
    elif(a<5625):
        d="NE"
    elif(a<7875):
        d="ENE"
    elif(a<10125):
        d="E"
    elif(a<12375):
        d="ESE"
    elif(a<14625):
        d="SE"
    elif(a<16875):
        d="SSE"
    elif(a<19125):
        d="S"
    elif(a<21375):
        d="SSW"
    elif(a<23625):
        d="SW"
    elif(a<25875):
        d="WSW"
    elif(a<28125):
        d="W"
    elif(a<30375):
        d="WNW"
    elif(a<32625):
        d="NW"
    else:
        d="NNW"

    b=round(b/60+0.001,1)
    if(b<=0.2):
        w=0
    elif(b<=1.5):
        w=1
    elif(b<=3.3):
        w=2
    elif(b<=5.4):
        w=3
    elif(b<=7.9):
        w=4
    elif(b<=10.7):
        w=5
    elif(b<=13.8):
        w=6
    elif(b<=17.1):
        w=7
    elif(b<=20.7):
        w=8
    elif(b<=24.4):
        w=9
    elif(b<=28.4):
        w=10
    elif(b<=32.6):
        w=11
    else:
        w=12

    if(w==0):
        print("C",0)
    else:
        print(d,w)
resolve()

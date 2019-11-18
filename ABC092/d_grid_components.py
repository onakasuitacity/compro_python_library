# https://atcoder.jp/contests/abc092/tasks/arc093_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    a-=1; b-=1
    print(100,98)
    h=99
    print('#'*49+'.'*49)
    while(a>0 or b>0):
        if(a>=24):
            s1='#.'*24+'#'
            a-=24
        else:
            s1='#.'*a+'#'*(49-2*a)
            a=0
        if(b>=24):
            s2='.#'*24+'.'
            b-=24
        else:
            s2='.#'*b+'.'*(49-2*b)
            b=0
        print(s1+s2)
        h-=1

        print('#'*49+'.'*49)
        h-=1

    for i in range(h):
        print('#'*49+'.'*49)

resolve()

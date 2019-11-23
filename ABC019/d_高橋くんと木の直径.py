# https://atcoder.jp/contests/abc019/tasks/abc019_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

prd=True
N=5
d=[
[ 0, 5,14, 6, 8],
[ 5, 0, 9, 1, 3],
[14, 9, 0,10,12],
[ 6, 1,10, 0, 2],
[ 8, 3,12, 2, 0]
]

def ask(u,v):
    print("? {} {}".format(u,v))
    sys.stdout.flush()
    return int(input()) if(prd) else d[u-1][v-1]

def resolve():
    n=int(input()) if(prd) else N
    s=-1
    dmax=0
    for i in range(2,n+1):
        d=ask(1,i)
        if(d>dmax):
            dmax=d
            s=i
    for i in range(1,n+1):
        if(i==s): continue
        d=ask(s,i)
        if(d>dmax):
            dmax=d
    print("! {}".format(dmax))
resolve()

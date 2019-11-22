# https://atcoder.jp/contests/abc074/tasks/arc083_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c,d,e,f=map(int,input().split())
    Water=set()
    Sugar=set()
    for i in range(30):
        for j in range(30):
            w=100*i*a+100*j*b
            if(w>f): break
            Water.add(w)
    Water.remove(0)

    for i in range(b):
        for j in range(1500):
            s=i*c+j*d
            if(s*(100+e)>f*e): break
            Sugar.add(s)

    from itertools import product
    SW=list(product(Water,Sugar))
    SW.sort(lambda x:x[1]/(x[0]+x[1]), reverse=1)
    for w,s in SW:
        if(s+w<=f and s*(100+e)<=e*(s+w)):
            print(s+w,s)
            return
resolve()

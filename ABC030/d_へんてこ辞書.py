# https://atcoder.jp/contests/abc030/tasks/abc030_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,a=map(int,input().split())
    a-=1
    k=input()
    B=list(map(lambda x:int(x)-1,input().split()))

    D=[None]*n
    D[a]=0
    cycle=[a]

    v=a
    while(1):
        nv=B[v]
        if(D[nv] is not None): break
        D[nv]=D[v]+1
        cycle.append(nv)
        v=nv
    path,cycle=cycle[:D[nv]],cycle[D[nv]:]

    # k をintとして扱えるときは普通に計算する
    if(len(k)<=19):
        k=int(k)
        if(k<len(path)):
            print(path[k]+1)
        else:
            k-=len(path)
            print(cycle[k%len(cycle)]+1)
        return

    # そうでないときは k-len(path)のmod len(cycle)の値を桁毎に計算する
    r=0
    m=len(cycle)
    for d in k:
        d=int(d)
        r=(10*r+d)%m
    r=(r-len(path))%m
    print(cycle[r]+1)
resolve()

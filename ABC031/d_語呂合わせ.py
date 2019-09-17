# https://atcoder.jp/contests/abc031/tasks/abc031_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    k,n=map(int,input().split())
    vw=[input().split() for _ in range(n)]
    from itertools import product
    for length in product(range(1,4),repeat=k):
        flag1=True
        goro={i:None for i in range(1,k+1)}
        for v,w in vw:
            flag2=True
            ind=0
            for s in v: # vの各桁の数字を見ている
                s=int(s)
                if ind+length[s-1]>len(w): # index over
                    flag2=False
                    break # for s
                if goro[s] is None:
                    goro[s]=w[ind:ind+length[s-1]]
                else:
                    if goro[s]!=w[ind:ind+length[s-1]]:
                        flag2=False
                        break # for s
                ind+=length[s-1]
            if ind!=len(w):
                flag1=False
                break
            if flag2 is False:
                flag1=False
                break # for v,w
        if flag1:
            for v in goro.values():
                print(v if v else 'a')
            return
        else:
            continue
resolve()

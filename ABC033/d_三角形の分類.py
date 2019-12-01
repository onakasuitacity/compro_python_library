# https://atcoder.jp/contests/abc033/tasks/abc033_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from cmath import pi,phase
from itertools import chain
def resolve():
    n=int(input())
    C=[None]*n
    for i in range(n):
        x,y=map(int,input().split())
        C[i]=x+y*1j

    eps=1e-10
    eq=gt=0
    for i in range(n):
        args=[phase(c-C[i]) for c in chain(C[:i],C[i+1:])]
        args.sort()
        args+=[a+2*pi for a in args]

        # two pointers
        j=k=0 # [i:j]はpi/2未満、[i:k]はpi未満にする
        for a in args[:n-1]:
            while(args[j+1]<a+pi/2-eps): j+=1
            while(args[k+1]<a+pi): k+=1
            if(abs(args[j+1]-(a+pi/2))<eps):
                eq+=1; gt+=k-j-1
            else:
                gt+=k-j

    print(n*(n-1)*(n-2)//6-eq-gt,eq,gt)
resolve()

# https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    # 1/c=(4ab-na-nb)/nab
    from itertools import product
    for a,b in product(range(1,3501),repeat=2):
        if(4*a*b-n*a-n*b<=0): continue
        if(n*a*b%(4*a*b-n*a-n*b)==0):
            c=n*a*b//(4*a*b-n*a-n*b)
            print(a,b,c)
            return
resolve()

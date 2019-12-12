# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    for i in range(1,int(input())+1):
        res=''
        if(i%2==0): res+='a'
        if(i%3==0): res+='b'
        if(i%4==0): res+='c'
        if(i%5==0): res+='d'
        if(i%6==0): res+='e'
        print(res if(res) else i)
resolve()

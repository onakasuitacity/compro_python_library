# https://atcoder.jp/contests/abc117/tasks/abc117_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.buffer.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    m=k.bit_length()
    A=list(map(int,input().split()))
    flag=False # x<=kが確定したかどうか
    x=0
    for d in range(m-1,-1,-1):
        d_sum=sum((a>>d)&1 for a in A)
        if(d_sum<=(n//2)): # xのd桁目を1にしたい
            if(flag or ((k>>d)&1==1)):
                x+=(1<<d)
        else: # xのd桁目を0にする
            if((k>>d)&1==1):
                flag=True
    print(sum(a^x for a in A))
resolve()

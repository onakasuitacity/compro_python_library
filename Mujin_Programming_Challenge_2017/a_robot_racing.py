# https://atcoder.jp/contests/mujin-pc-2017/tasks/mujin_pc_2017_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    imos=[0]*n
    over=0
    for i,x in enumerate(map(int,input().split())):
        imos[over]+=1
        over=max(over,i-(x-1)//2)

    for i in range(n-1):
        imos[i+1]+=imos[i]

    ans=1
    chosen=0
    for c in imos:
        ans*=(c-chosen)
        ans%=MOD
        chosen+=1

    print(ans)
resolve()

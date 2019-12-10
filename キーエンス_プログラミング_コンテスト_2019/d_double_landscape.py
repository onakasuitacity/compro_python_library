# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    N=n*m
    CA=[0]*(N+1)
    CB=[0]*(N+1)
    for a in map(int,input().split()):
        CA[a]+=1
    for b in map(int,input().split()):
        CB[b]+=1
    for i in range(N):
        CA[i+1]+=CA[i]
        CB[i+1]+=CB[i]

    ans=1
    for i in range(N,0,-1):
        # 双方に i の数字があるとき
        if(CA[i]-CA[i-1]==1 and CB[i]-CB[i-1]==1):
            continue # 1通りしかない
        # B にだけあるとき
        elif(CA[i]==CA[i-1] and CB[i]-CB[i-1]==1):
            ans*=CA[-1]-CA[i]
        # A にだけあるとき
        elif(CA[i]-CA[i-1]==1 and CB[i]==CB[i-1]):
            ans*=CB[-1]-CB[i]
        # 双方に i の数字がないとき
        elif(CA[i]==CA[i-1] and CB[i]==CB[i-1]):
            ans*=(CA[-1]-CA[i])*(CB[-1]-CB[i])-(N-i)
        else:
            print(0)
            return
        ans%=MOD

    print(ans)
resolve()

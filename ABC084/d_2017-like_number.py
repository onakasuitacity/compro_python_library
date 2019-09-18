# https://atcoder.jp/contests/abc084/tasks/abc084_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    c=10**5+1
    # S[i]: iがprimeかを指すboolean
    S=[1]*c
    S[0]=0; S[1]=0 # 別に無くてよい
    for i in range(2,c):
        if S[i]==0: continue
        for j in range(2*i,c,i):
            S[j]=0
    # T[i]: iが2017-like primeかを指すboolean
    T=[0]*c
    for i in range(3,c,2):
        if S[i] and S[(i+1)//2]: T[i]=1
    # cumsum
    for i in range(c-1): T[i+1]+=T[i]
    # input
    q=int(input())
    for _ in range(q):
        l,r=map(int,input().split())
        print(T[r]-T[l-1])
resolve()

# https://atcoder.jp/contests/abc143/tasks/abc143_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def bin_sort(A,n_min=None,n_max=None):
    if(n_min is None): n_min=min(A)
    if(n_max is None): n_max=max(A)
    bin=[0]*(n_max-n_min+1)
    for a in A: bin[a-n_min]+=1
    B=[]
    for i in range(n_min,n_max+1): B+=[i]*bin[i-n_min]
    return B

def resolve():
    n=int(input())
    A=[0]*n
    for a in map(int,input().split()): A[a-1]+=1
    A=bin_sort(A,0,n)
    S=[0]*(n+1)
    for i in range(n): S[i+1]=S[i]+A[i]
    # output
    p=n; i=n
    for k in range(1,n+1):
        while(1):
            while(1):
                if(i<=0 or A[i-1]<p): break
                i-=1
            if(S[i]+p*(n-i)>=k*p): break
            p-=1
        print(p)
resolve()

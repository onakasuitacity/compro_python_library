# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import Counter,defaultdict
def resolve():
    n,m=map(int,input().split())
    D=defaultdict(list)
    for a in map(int,input().split()):
        D[a%m].append(a)

    ans=len(D[0])//2
    if(m%2==0): ans+=len(D[m//2])//2

    for i in range(1,(m-1)//2+1):
        A=D[i]; B=D[m-i]
        if(len(A)<len(B)): A,B=B,A # len(A)>=len(B)
        n=len(B)
        ans+=n
        A=Counter(A).most_common()[::-1]
        for i in range(len(A)):
            if(n>0 and A[i][1]&1):
                n-=1
                A[i]=(A[i][0],A[i][1]-1)
        for key,val in A:
            if(n>=val): n-=val
            else:
                val-=n
                n=0
                ans+=val//2
    print(ans)
resolve()

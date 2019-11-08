# https://atcoder.jp/contests/abc119/tasks/abc119_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,a,b,c=map(int,input().split())
    L=[int(input()) for _ in range(n)]
    ans=INF
    from itertools import product
    for I in product(range(4),repeat=n):
        score=0
        I=tuple(I)
        A,B,C=[],[],[]
        for i,k in enumerate(I):
            if(k==0): A.append(L[i])
            elif(k==1): B.append(L[i])
            elif(k==2): C.append(L[i])
        if((not A) or (not B) or (not C)): continue # 1つも竹が無いのはダメ
        score+=(len(A)+len(B)+len(C)-3)*10

        SA=sum(A)
        SB=sum(B)
        SC=sum(C)
        score+=abs(SA-a)
        score+=abs(SB-b)
        score+=abs(SC-c)
        ans=min(ans,score)
    print(ans)
resolve()

# https://atcoder.jp/contests/abc075/tasks/abc075_b
from itertools import product
#%%
def resolve():
    h,w=map(int,input().split())
    A=[list('.'+input()+'.') for _ in range(h)]
    A=[['.']*(w+2)]+A+[['.']*(w+2)]

    for i,j in product(range(1,h+1),range(1,w+1)):
        if A[i][j]=='.':
            A[i][j]=((A[i-1][j-1]=='#')+(A[i-1][j]=='#')+(A[i-1][j+1]=='#')
            +(A[i][j-1]=='#')+(A[i][j+1]=='#')
            +(A[i+1][j-1]=='#')+(A[i+1][j]=='#')+(A[i+1][j+1]=='#'))

    for i in range(1,h+1):
        print(*A[i][1:w+1],sep='')
resolve()

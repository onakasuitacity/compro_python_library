# https://atcoder.jp/contests/abc096/tasks/abc096_c 
#%%
from itertools import product

#%%
def resolve():
    h,w=map(int,input().split())
    A=['.'+input()+'.' for _ in range(h)]
    A=['.'*(w+2)]+A+['.'*(w+2)]
    flag = 1

    for i,j in product(range(1,h+1),range(1,w+1)):
        if A[i][j]=='#':
            flag = min(flag,A[i-1][j]=='#' or A[i+1][j]=='#' or A[i][j-1]=='#' or A[i][j+1]=='#')

    print("Yes" if flag else "No")
resolve()

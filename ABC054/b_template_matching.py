# https://atcoder.jp/contests/abc054/tasks/abc054_b
from itertools import product
#%%
def resolve():
    n,m=map(int,input().split())
    A=[input() for _ in range(n)]
    B=[input() for _ in range(m)]
    flag = any([r[j:j+m] for r in A[i:i+m]]==B for i,j in product(range(n-m+1),range(n-m+1)))
    print("Yes" if flag else "No")
resolve()

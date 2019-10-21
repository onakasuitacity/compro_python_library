# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
# 1-3. しゃくとり法のアイディア・実装

# input
n=12
A=[4,6,7,8,1,2,110,2,4,12,3,9]
x=25

# preparation
from bisect import bisect_right
S=[0]*(n+1)
for i in range(n):
    S[i+1]=S[i]+A[i]
 
# calculate
for l in range(n):
    print(l,bisect_right(S,x+S[l])-1)

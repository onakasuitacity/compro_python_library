# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
# 1-3. しゃくとり法のアイディア・実装

# input
n=12
A=[4,6,7,8,1,2,110,2,4,12,3,9]
x=25

# calculate
r=0
sum=0
for l in range(n):
    # incrementation of r
    while(r<n and sum+A[r]<=x):
        sum+=A[r]
        r+=1
    # r=r(l)
    print(l,r)
    # incrementation of l
    if(r==l): r+=1
    else: sum-=A[l]

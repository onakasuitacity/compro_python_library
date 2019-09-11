from collections import deque

# given
N=5
V=list(range(N))
E=[{1,2,3},{0},{0},{0,4},{3}]

###
# 1   2
#  \ /
#   0   4
#    \ /
#     3

# parameter
root=0

# build
inf=float("inf")
d=[inf if i!=root else 0 for i in G]
Q=deque()
Q.append(root)
while(Q):
    u=Q.popleft()
    for v in E[u]:
        if d[v]>d[u]+1:
            d[v]=d[u]+1
            Q.append(v)

# result
print(d)

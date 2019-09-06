# Dijkstra's algorithm

### input
# node
V=[0,1,2,3,4]
n=len(V)
# adjacency matrix
A = [
[0,50,80,0,0],
[0,0,20,15,0],
[0,0,0,10,15],
[0,0,0,0,30],
[0,0,0,0,0]
]
m=7 # 使わない

### parameter
# start
s=0

### initialize
# distance
d=[float("inf") if i!=s else 0 for i in V]
# previous node
prev=[None for _ in V]

### iterate
Q=set(V)
while(Q):
    # Qの中で距離が最小のものを取得
    i = min((d[q],q) for q in Q)[1]
    Q.remove(i)
    # iの出力辺の先を探索
    for j in range(n):
        if A[i][j]==0: continue
        elif d[j]>d[i]+A[i][j]:
            d[j]=d[i]+A[i][j]
            prev[j]=i

### output
for i in V:
    print("FROM {} TO {}".format(s,i))
    print("distance : {}".format(d[i]))
    p=i
    path=[i]
    while(prev[p]):
        p=prev[p]
        path.append(p)
    print("path : {}".format(path[::-1]),end="\n\n")

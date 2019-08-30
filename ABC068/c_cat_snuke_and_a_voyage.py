# https://atcoder.jp/contests/abc068/tasks/arc079_a
N,M=map(int,input().split())
start,end=set(),set()
for i in range(M):
    a,b=map(int,input().split())
    if a==1: start.add(b)
    if b==N: end.add(a)
print("POSSIBLE" if start&end else "IMPOSSIBLE")

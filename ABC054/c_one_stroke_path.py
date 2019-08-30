# https://atcoder.jp/contests/abc054/tasks/abc054_c
import itertools
N,M=map(int,input().split())
edges = {tuple(map(int,input().split())) for _ in range(M)}
paths = itertools.permutations(range(2,N+1))
ans = 0
for path in paths:
    count = 0
    path = [1]+list(path)
    for edge in zip(path[:-1],path[1:]):
        count += tuple(sorted(edge)) in edges
    ans += count==N-1
print(ans)

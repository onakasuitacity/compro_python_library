# https://atcoder.jp/contests/abc016/tasks/abc016_3
def resolve():
    v,e=map(int,input().split())
    edges=[set() for _ in range(v)]
    for _ in range(e):
        a,b=map(int,input().split())
        edges[a-1].add(b-1)
        edges[b-1].add(a-1)
    for i in range(v):
        print(sum(1 for j in range(v) if (j!=i) and (j not in edges[i]) and (edges[i]&edges[j])))
resolve()

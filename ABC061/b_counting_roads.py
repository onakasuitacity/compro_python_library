# https://atcoder.jp/contests/abc061/tasks/abc061_b
def resolve():
    n,m=map(int,input().split())
    edges=[0 for _ in range(n)]
    for _ in range(m):
        a,b=map(lambda x:int(x)-1,input().split())
        edges[a]+=1
        edges[b]+=1
    print(*edges,sep='\n')
resolve()

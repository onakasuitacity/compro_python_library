# https://atcoder.jp/contests/abc075/tasks/abc075_c
def resolve():
    n,m=map(int,input().split())
    edges=[list(map(lambda x:int(x)-1,input().split())) for _ in range(m)]
    ans=0
    for x in edges:
        C=list(range(n))
        for y in edges:
            if y==x: continue
            C=[C[y[0]] if C[i]==C[y[1]] else C[i] for i in range(n)]
        if len(set(C))!=1: ans+=1
    print(ans)
resolve()

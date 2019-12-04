# https://atcoder.jp/contests/abc013/tasks/abc013_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m,d=map(int,input().split())
    A=list(map(lambda x:int(x)-1,input().split()))
    perm=list(range(n))
    for a in A[::-1]:
        perm[a],perm[a+1]=perm[a+1],perm[a]

    # この perm をサイクル分解する
    cycles=[]
    color=[None]*n
    cnt=0
    def cycle_decomposition(v)->bool:
        if(color[v] is not None): return False
        cycle=[]
        while(color[v] is None):
            color[v]=cnt
            cycle.append(v)
            v=perm[v]
        cycles.append(cycle)
        return True
    for v in range(n):
        cnt+=cycle_decomposition(v)

    ans=[None]*n
    for cycle in cycles:
        p=len(cycle)
        for i in range(p):
            v=cycle[i]
            ans[v]=cycle[(i+d)%p]
    for a in ans:
        print(a+1)
resolve()

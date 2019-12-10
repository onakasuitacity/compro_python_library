# https://atcoder.jp/contests/agc013/tasks/agc013_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        a-=1
        b-=1
        E[a].append(b)
        E[b].append(a)

    # 0 から出発し、2方向にpathを伸ばす
    used=[0]*n
    used[0]=1
    Q=[0]
    front=[0]
    while(Q):
        v=Q.pop()
        for nv in E[v]:
            if(used[nv]): continue
            used[nv]=1
            front.append(nv)
            Q.append(nv)
            break

    back=[]
    Q=[0]
    while(Q):
        v=Q.pop()
        for nv in E[v]:
            if(used[nv]): continue
            used[nv]=1
            back.append(nv)
            Q.append(nv)
            break

    ans=back[::-1]+front
    print(len(ans))
    print(*map(lambda x:x+1,ans))
resolve()

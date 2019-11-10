# https://atcoder.jp/contests/abc111/tasks/arc103_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    XY=[tuple(map(int,input().split())) for _ in range(n)]
    parity=[0]*2
    for x,y in XY:
        parity[(x+y)%2]=1

    # それぞれのパリティの点が存在すると不可能
    if(parity[0] and parity[1]):
        print(-1)
        return

    m=31
    D=[pow(2,i) for i in range(m)]
    # 偶数の場合は奇数に帰着させる
    if(parity[0]):
        XY=[(x-1,y) for x,y in XY]
        D=[1]+D

    U=[x-y for x,y in XY]
    V=[x+y for x,y in XY]

    W=[0]*n
    for j in range(n):
        res=[0]*m
        u=(U[j]+pow(2,m)-1)//2
        v=(V[j]+pow(2,m)-1)//2
        for i in range(m):
            ub=u&1; vb=v&1
            if(ub and vb):
                res[i]='R'
            elif(ub and (not vb)):
                res[i]='D'
            elif((not ub) and vb):
                res[i]='U'
            else:
                res[i]='L'
            u>>=1; v>>=1
        ans=''.join(res)
        W[j]=ans

    m=m+parity[0]
    print(m)
    print(*D)
    for j in range(n):
        ans=W[j] if(parity[1]) else 'R'+W[j]
        print(ans)
resolve()

# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    X=list(zip(A,B))
    X.sort(lambda x:x[1])

    C=[(x[0],i) for i,x in enumerate(X)]
    C.sort()
    perm=[C[i][1] for i in range(n)]

    A.sort()
    B.sort()

    # A <= B を満たしていなければ不可能
    if(any(A[i]>B[i] for i in range(n))):
        print("No")
        return

    # 自由度が1つあれば可能
    if(any(A[i+1]<=B[i] for i in range(n-1))):
        print("Yes")
        return

    # permのYoung図が[n]かどうかで判断
    p=0
    cnt=0
    while(True):
        cnt+=1
        p=perm[p]
        if(p==0): break
    print("Yes" if(cnt<n) else "No")
resolve()

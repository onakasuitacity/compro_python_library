# https://atcoder.jp/contests/agc039/tasks/agc039_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[[int(s) for s in input()] for _ in range(n)]
    B=[a[:] for a in A]
    from itertools import product
    # 対角以外の0をINF
    for i,j in product(range(n),repeat=2):
        if i==j: continue
        if B[i][j]==0: B[i][j]=INF
    # Warshall-Floyd
    for k,i,j in product(range(n),repeat=3):
        B[i][j]=min(B[i][j],B[i][k]+B[k][j])
    # 直径となる始点を1つ取得
    dia=0; p=0
    for i,j in product(range(n),repeat=2):
        if dia<B[i][j]:
            dia=B[i][j]
            p=i
    for i,j in product(range(n),repeat=2):
        if i>=j: continue # i<j
        if A[i][j]:
            if abs(B[i][p]-B[j][p])!=1:
                print(-1)
                return
    print(dia+1)
resolve()

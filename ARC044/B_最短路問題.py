# https://atcoder.jp/contests/arc044/tasks/arc044_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    M=max(A)

    # rootの距離が0でないと矛盾
    if(A[0]!=0):
        print(0)
        return

    # 個数分布を計算
    C=[0]*(M+1)
    for a in A:
        C[a]+=1

    # rootが複数あると矛盾
    if(C[0]!=1):
        print(0)
        return

    # 距離が分断されていたら矛盾
    if(any(C[i]==0 for i in range(M+1))):
        print(0)
        return

    ans=1
    for i in range(1,M+1):
        # depth i-1 と各頂点に対して、少なくとも1本辺を引く
        up=pow(pow(2,C[i-1],MOD)-1,C[i],MOD)
        ans*=up
        ans%=MOD
        # depth i 同士の辺を引く
        mid=pow(2,C[i]*(C[i]-1)//2,MOD)
        ans*=mid
        ans%=MOD
    print(ans)
resolve()

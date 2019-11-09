# https://atcoder.jp/contests/abc113/tasks/abc113_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def check(x):
    n=x.bit_length()
    for i in range(n-1):
        if((x>>i)&1 and (x>>(i+1))&1):
            return False
    return True

def resolve():
    H,W,K=map(int,input().split())
    K-=1
    dp=[0]*W
    dp[0]=1
    for _ in range(H):
        ndp=[0]*W
        # 各 2^(W-1)通りの線の引き方から、dpの遷移先を考える
        for V in range(2**(W-1)):
            if(not check(V)): continue
            for w in range(W):
                if(w<W-1 and (V>>w)&1): # 右に線があるとき
                    ndp[w+1]+=dp[w]
                    ndp[w+1]%=MOD
                elif(w>0 and (V>>(w-1))&1): # 左に線があるとき
                    ndp[w-1]+=dp[w]
                    ndp[w-1]%=MOD
                else: # 双方に線がないとき
                    ndp[w]+=dp[w]
                    ndp[w]%=MOD
        dp=ndp
    print(dp[K])
resolve()

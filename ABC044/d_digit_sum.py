# https://atcoder.jp/contests/abc044/tasks/arc060_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

def f(b,n):
    if(n<b): return n
    return f(b,n//b)+n%b

def resolve():
    n=int(input())
    s=int(input())

    if(s>n):
        print(-1)
        return
    if(s==n):
        print(n+1)
        return

    # 2 <= b <= sqrt(n) を全探索
    k=int(n**.5)
    for b in range(2,k+1):
        if(f(b,n)==s):
            print(b)
            return

    # sqrt(n) < b <= n を考える
    B=[]
    for p in range(1,k+1):
        if((n-s)%p): continue
        b=(n-s)//p+1
        if(b<2): continue
        if(f(b,n)==s):
            B.append(b)

    print(min(B) if(B) else -1)
resolve()

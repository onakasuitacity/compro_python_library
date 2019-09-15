# https://atcoder.jp/contests/abc141/tasks/abc141_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    xor=0
    max_digit=0
    for a in A:
        xor^=a
        max_digit=max(max_digit,a.bit_length())
    # xorのうち、bitが立っていない部分だけでスクリーニング
    for i in range(n): A[i]&=(~xor)
    # このAに対してsweeping
    r=0 # Aのrank
    for d in reversed(range(max_digit)): # digit
        for i in range(r,n):
            if A[i]&(1<<d): # 候補のiをfixする
                for j in range(i+1,n): # sweep(確定してる奴は掃き出さなくてよい)
                    if A[j]&(1<<d): A[j]^=A[i]
                A[i],A[r]=A[r],A[i] # swap
                r+=1
                break
    # sweepしたAに対し、最上位bitから確定させていく
    x=0
    for i in range(r):
        d=A[i].bit_length()
        if not x&(1<<(d-1)):
            x^=A[i]
    print(xor+2*x)
resolve()

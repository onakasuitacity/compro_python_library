# https://atcoder.jp/contests/abc043/tasks/arc059_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    n=len(S)

    # 同じ文字が連続していたらOK
    for i in range(n-1):
        if(S[i]==S[i+1]):
            print(i+1,i+2)
            return

    # 1つ飛ばしで同じならOK
    for i in range(n-2):
        if(S[i]==S[i+2]):
            print(i+1,i+3)
            return

    # そうでなければ存在しない
    print(-1,-1)
resolve()

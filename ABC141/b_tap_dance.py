# https://atcoder.jp/contests/abc141/tasks/abc141_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    s=input()
    flag=True
    for i in range(len(s)):
        if i%2==0 and s[i]=='L':
            flag=False
        elif i%2==1 and s[i]=='R':
            flag=False
    print("Yes" if flag else "No")

resolve()

# https://atcoder.jp/contests/abc076/tasks/abc076_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    s=input().replace('?','.')
    t=input()
    import re
    for i in range(len(s)-len(t),-1,-1):
        if re.match(s[i:i+len(t)],t):
            s=s.replace('.','a')
            print(s[:i]+t+s[i+len(t):])
            return
    print("UNRESTORABLE")
resolve()

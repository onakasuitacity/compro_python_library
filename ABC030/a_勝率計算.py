# https://atcoder.jp/contests/abc030/tasks/abc030_a
a,b,c,d = map(int,input().split())
s,t = b/a,d/c
if s>t: print("TAKAHASHI")
elif s<t: print("AOKI")
else: print("DRAW")

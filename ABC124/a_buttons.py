# https://atcoder.jp/contests/abc124/tasks/abc124_a
a,b=map(int,input().split())
if a==b: print(2*a)
else: print(2*max(a,b)-1)

# https://atcoder.jp/contests/abc093/tasks/abc093_b
a,b,k = map(int,input().split())
s = set(range(a,a+k))
t = set(range(b-k+1,b+1))
u = sorted(s|t)
for i in u:
    if a<=i<=b: print(i)

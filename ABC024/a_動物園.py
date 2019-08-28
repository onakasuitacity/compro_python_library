# https://atcoder.jp/contests/abc024/tasks/abc024_a
a,b,c,k = map(int,input().split())
s,t = map(int,input().split())
print(a*s+b*t-(c*(s+t) if s+t>=k else 0))

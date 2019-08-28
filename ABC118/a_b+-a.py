# https://atcoder.jp/contests/abc118/tasks/abc118_a
a,b = map(int,input().split())
print(a+b) if b%a==0 else print(b-a)

# https://atcoder.jp/contests/abc118/tasks/abc118_b
n,m = map(int,input().split())
a = set(range(1,m+1))
for i in range(n):
    a = a & set(map(int,input()[2:].split()))
print(len(a))

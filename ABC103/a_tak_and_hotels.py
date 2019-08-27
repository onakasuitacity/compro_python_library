# https://atcoder.jp/contests/abc044/tasks/abc044_a
n = int(input())
k = int(input())
x = int(input())
y = int(input())
print(x*min(n,k)+y*max(0,n-k))

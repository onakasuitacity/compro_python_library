# https://atcoder.jp/contests/abc095/tasks/abc095_b
n,x = map(int,input().split())
m = [int(input()) for _ in range(n)]
print(n+(x-sum(m))//(min(m)))

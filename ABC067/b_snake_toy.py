# https://atcoder.jp/contests/abc067/tasks/abc067_b
n,k = map(int,input().split())
print(sum(sorted(list(map(int,input().split())),reverse=1)[:k]))

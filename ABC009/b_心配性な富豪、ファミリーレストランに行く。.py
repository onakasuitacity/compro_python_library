# https://atcoder.jp/contests/abc009/tasks/abc009_2
n = int(input())
print(sorted(list(set(int(input()) for _ in range(n))))[-2])

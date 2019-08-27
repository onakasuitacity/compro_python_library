# https://atcoder.jp/contests/abc091/tasks/abc091_b
n = int(input())
a = [input() for i in range(n)]
m = int(input())
b = [input() for i in range(m)]
score = 0

for i in range(n):
    score = max(score, a.count(a[i])-b.count(a[i]))

print(score)

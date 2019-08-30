# https://atcoder.jp/contests/abc027/tasks/abc027_a
a = set()
for b in list(map(int,input().split())):
    a^={b}
print(*a)

# https://atcoder.jp/contests/abc028/tasks/abc028_b
s = input()
print(*list(s.count(c) for c in "ABCDEF"))

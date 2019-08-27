# https://atcoder.jp/contests/abc013/tasks/abc013_2
a,b = [int(input()) for _ in range(2)]
d = abs(a-b)
print(min(d,10-d))

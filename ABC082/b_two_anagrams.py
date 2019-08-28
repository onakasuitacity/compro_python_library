# https://atcoder.jp/contests/abc082/tasks/abc082_b
s = ''.join(sorted(input()))
t = ''.join(sorted(input(), reverse=True))
print("Yes") if s<t else print("No")

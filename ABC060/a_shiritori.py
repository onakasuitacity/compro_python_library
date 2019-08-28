# https://atcoder.jp/contests/abc060/tasks/abc060_a
a,b,c = input().split()
print("YES" if a[-1]==b[0] and b[-1]==c[0] else "NO")

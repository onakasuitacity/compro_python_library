# https://atcoder.jp/contests/abc053/tasks/abc053_b
a = input()
s = a.index('A')
e = a[::-1].index('Z')
print(len(a)-s-e)

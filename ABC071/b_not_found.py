# https://atcoder.jp/contests/abc071/tasks/abc071_b
a = set("abcdefghijklmnopqrstuvwxyz")
a -= set(input())
if a: print(sorted(list(a))[0])
else: print("None")

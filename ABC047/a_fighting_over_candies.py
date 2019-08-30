# https://atcoder.jp/contests/abc047/tasks/abc047_a
a = sorted(list(map(int,input().split())))
print("Yes" if a.pop()==sum(a) else "No")

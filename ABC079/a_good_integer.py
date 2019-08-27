# https://atcoder.jp/contests/abc079/tasks/abc079_a
N = input()
flag = False

for i in range(len(N)-2):
    if len(set(N[i:i+3]))==1: flag = True

print("Yes" if flag else "No")

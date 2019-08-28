# https://atcoder.jp/contests/abc079/tasks/abc079_b
a,b = 2,1
for _ in range(int(input())):
    a,b = b,a+b
print(a)

# https://atcoder.jp/contests/abc014/tasks/abc014_1
a,b = [int(input()) for _ in range(2)]
print(b*(a%b!=0)-a%b)

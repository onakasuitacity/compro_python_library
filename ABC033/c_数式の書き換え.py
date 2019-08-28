# https://atcoder.jp/contests/abc033/tasks/abc033_c
l = input().split('+')
print(len(list(filter(lambda x: '0' not in x,l))))

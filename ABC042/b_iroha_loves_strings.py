# https://atcoder.jp/contests/abc042/tasks/abc042_b
N,L = map(int,input().split())
strs = sorted([input() for i in range(N)])
print(''.join(strs))

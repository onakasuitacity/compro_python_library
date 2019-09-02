# https://atcoder.jp/contests/abc036/tasks/abc036_b
n = int(input())
A = [list(input()) for _ in range(n)][::-1]
B = list(zip(*A))
for Row in B: print(''.join(Row))

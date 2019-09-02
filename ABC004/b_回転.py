# https://atcoder.jp/contests/abc004/tasks/abc004_2
n = 4
A = [list(input()) for _ in range(n)]
B = list(zip(*A))[::-1]
C = list(zip(*B))[::-1]
for Row in C: print(''.join(Row))

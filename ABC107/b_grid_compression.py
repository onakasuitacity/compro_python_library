# https://atcoder.jp/contests/abc107/tasks/abc107_b
h,w = map(int,input().split())
A = [list(input()) for _ in range(h)]
B = []
C = []
for Row in A:
    if set(Row)!={'.'}: B.append(Row)
B = [Row for Row in zip(*B)]
for Row in B:
    if set(Row)!={'.'}: C.append(Row)
for Row in zip(*C):
    print(''.join(Row))

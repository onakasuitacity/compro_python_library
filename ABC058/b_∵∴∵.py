# https://atcoder.jp/contests/abc058/tasks/abc058_b
O = input()
E = input()

for i in range(len(E)):
    print(O[i]+E[i],end='')

if len(O)!=len(E):
    print(O[-1])

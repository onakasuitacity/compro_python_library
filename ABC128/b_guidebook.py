# https://atcoder.jp/contests/abc128/tasks/abc128_b
n = int(input())
L = [input().split()+[i] for i in range(1,n+1)]
L.sort(key=lambda l:(l[0],-int(l[1])))
for l in L: print(l[2])

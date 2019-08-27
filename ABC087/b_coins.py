# https://atcoder.jp/contests/abc087/tasks/abc087_b
import itertools

A = int(input())
B = int(input())
C = int(input())
X = int(input())//50
count = 0

for i,j,k in itertools.product(range(A+1),range(B+1),range(C+1)):
    if i*10+j*2+k == X:
        count += 1

print(count)

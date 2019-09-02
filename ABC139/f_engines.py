# https://atcoder.jp/contests/abc139/tasks/abc139_f
import cmath
import itertools
n = int(input())
C = sorted([complex(*map(int,input().split())) for _ in range(n)], key=cmath.phase)
score = 0
for i,j in itertools.product(range(n),range(n)):
    if i>j: continue
    score = max((score,abs(sum(C[:i]+C[j:])),abs(sum(C[i:j]))))
print(score)

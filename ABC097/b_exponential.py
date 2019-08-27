# https://atcoder.jp/contests/abc097/tasks/abc097_b
import itertools
x = int(input())
score = 0

# bmax = int(math.sqrt(x)), pmax = len(bin(x))-3
for b,p in itertools.product(range(1,33),range(2,10)):
    if b**p<=x: score = max(score, b**p)

print(score)

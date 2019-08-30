# https://atcoder.jp/contests/abc026/tasks/abc026_b
import math
N = int(input())
l = sorted([int(input())**2 for _ in range(N)],reverse=1)
score = 0

for i in range(N):
    score += l[i] if i%2==0 else -l[i]
    
print(math.pi*score)

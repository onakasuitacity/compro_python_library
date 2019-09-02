# https://atcoder.jp/contests/abc076/tasks/abc076_b
n,k = int(input()),int(input())
score = 1
for _ in range(n):
    if score<k : score*=2
    else: score+=k
print(score)

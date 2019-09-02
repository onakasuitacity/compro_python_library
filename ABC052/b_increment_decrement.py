# https://atcoder.jp/contests/abc052/tasks/abc052_b
n = int(input())
S = input()
score = 0
max_score = 0
for s in S:
    score += -1 + 2*(s=='I')
    max_score=max(max_score,score)
print(max_score)

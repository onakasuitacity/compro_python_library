# https://atcoder.jp/contests/abc114/tasks/abc114_b
s = input()
score = 753
for i in range(len(s)-2):
    score = min(score, abs(753-int(s[i:i+3])))
print(score)

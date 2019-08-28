# https://atcoder.jp/contests/abc122/tasks/abc122_b
s = input()
score = 0
count = 0

for i in range(len(s)):
    if s[i] in "ACGT":
        score += 1
        count = max(count,score)
    else:
        score = 0

print(count)

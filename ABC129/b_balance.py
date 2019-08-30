# https://atcoder.jp/contests/abc129/tasks/abc129_b
n = int(input())
l = list(map(int,input().split()))
score = 10**10
for i in range(n):
    score = min(score,abs(sum(l[:i])-sum(l[i:])))
print(score)

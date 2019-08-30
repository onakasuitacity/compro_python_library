# https://atcoder.jp/contests/abc073/tasks/abc073_c
n = int(input())
l = sorted([input() for _ in range(n)])
x = l[0]
count = 0
score = 0
for s in l[1:]:
    if x==s:
        count+=1
    else:
        score+=count%2==0
        count=0
    x = s
score+=count%2==0
print(score)

# https://atcoder.jp/contests/abc065/tasks/abc065_b
n = int(input())
s = [int(input()) for _ in range(n)]
t = set()
i = 1
count = 0

while(i not in t):
    count += 1
    t.add(i)
    i = s[i-1]
    if i==2:
        print(count)
        break
else:
    print(-1)

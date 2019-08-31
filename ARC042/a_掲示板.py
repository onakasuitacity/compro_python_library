# https://atcoder.jp/contests/arc042/tasks/arc042_a
n,m = map(int,input().split())
l = [int(input()) for _ in range(m)]
a = set()
ans = []
for i in range(m):
    p = l[m-1-i]
    if p not in a: ans.append(p)
    a.add(p)
for i in range(1,n+1):
    if i not in a: ans.append(i)
print(*ans, sep="\n")

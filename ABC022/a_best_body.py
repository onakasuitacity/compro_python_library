# https://atcoder.jp/contests/abc022/tasks/abc022_a
n,s,t = map(int,input().split())
w = int(input())
count = int(s<=w and w<=t)
for _ in range(2,n+1):
    w += int(input())
    count += s<=w and w<=t
print(count)

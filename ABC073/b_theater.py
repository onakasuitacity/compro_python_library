# https://atcoder.jp/contests/abc073/tasks/abc073_b
n = int(input())
count = 0
for _ in range(n):
    l,r = map(int,input().split())
    count += r - l
print(count+n)

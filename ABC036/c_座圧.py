# https://atcoder.jp/contests/abc036/tasks/abc036_c
import bisect
n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(list(set(a)))
for i in a:
    print(bisect.bisect_left(b,i))

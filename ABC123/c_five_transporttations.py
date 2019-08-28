# https://atcoder.jp/contests/abc123/tasks/abc123_c
import math
n = int(input())
d = [int(input()) for _ in range(5)]
print(math.ceil(n/min(d))+4)

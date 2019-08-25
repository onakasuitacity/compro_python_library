# https://atcoder.jp/contests/abc138/tasks/abc138_b
N = int(input())
nums = map(int, input().split())
a = 0
for num in nums:
    a += 1/num
print(1/a)

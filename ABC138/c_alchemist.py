# https://atcoder.jp/contests/abc138/tasks/abc138_c
N = int(input())
nums = list(map(int,input().split()))
nums.sort()
score = nums[0]
for i in range(N-1):
    score = (score + nums[i+1])/2
print(score)

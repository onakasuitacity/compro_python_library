# https://atcoder.jp/contests/abc088/tasks/abc088_b
N = int(input())
nums = sorted(map(int,input().split()),reverse=True)
count = 0

for i in range(N):
    if i%2==0:
        count += nums[i]
    else:
        count -= nums[i]
        
print(count)

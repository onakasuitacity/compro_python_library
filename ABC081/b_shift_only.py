# https://atcoder.jp/contests/abc081/tasks/abc081_b
N = int(input())
nums = list(map(int,input().split()))
flag = True
count = 0

while(True):
    for num in nums:
        flag = flag and (num%2==0)
    if flag:
        count += 1
        nums = list(map(lambda x:x//2, nums))
    else:
        break

print(count)

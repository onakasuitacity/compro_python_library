# https://atcoder.jp/contests/abc139/tasks/abc139_c
n = int(input())
H = list(map(int,input().split()))

count = 0
max_count = 0
for i in range(n-1):
    if H[i]>=H[i+1]: count+=1
    else:
        count=0
    max_count = max(max_count,count)
print(max_count)

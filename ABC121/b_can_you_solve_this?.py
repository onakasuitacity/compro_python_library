# https://atcoder.jp/contests/abc121/tasks/abc121_b
n,m,c = map(int,input().split())
b = list(map(int,input().split()))
count = 0
for i in range(n):
    a = list(map(int,input().split()))
    if sum(i*j for i,j in zip(a,b))+c>0: count+=1
print(count)

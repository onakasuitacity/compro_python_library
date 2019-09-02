# https://atcoder.jp/contests/abc139/tasks/abc139_b
a,b = map(int,input().split())
d = a-1
l = 1
count = 0
while(l<b):
    l+=d
    count+=1
print(count)

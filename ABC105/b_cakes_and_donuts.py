# https://atcoder.jp/contests/abc105/tasks/abc105_b
n = int(input())
for i in range(15):
    if (n-i*7)%4==0 and (n-i*7)>=0:
        print("Yes")
        break
else:
    print("No")

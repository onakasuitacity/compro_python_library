# https://atcoder.jp/contests/abc101/tasks/abc101_b
n = input()
print("Yes" if int(n)%sum(map(int,n))==0 else "No")

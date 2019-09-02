# https://atcoder.jp/contests/abc080/tasks/abc080_b
n = input()
print("Yes" if int(n)%sum(map(int,n))==0 else "No")

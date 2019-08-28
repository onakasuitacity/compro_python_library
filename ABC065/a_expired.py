# https://atcoder.jp/contests/abc065/tasks/abc065_a
x,a,b = map(int,input().split())
print("delicious") if -a+b<=0 else print("safe") if -a+b<=x else print("dangerous")

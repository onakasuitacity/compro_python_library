# https://atcoder.jp/contests/abc097/tasks/abc097_a
a,b,c,d = map(int,input().split())
print("Yes") if abs(a-c)<=d or (abs(a-b)<=d and abs(b-c)<=d) else print("No")

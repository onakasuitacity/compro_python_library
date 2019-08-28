# https://atcoder.jp/contests/arc002/tasks/arc002_1
X = int(input())
print("YES") if X%400==0 or (X%4==0 and X%100!=0) else print("NO") 

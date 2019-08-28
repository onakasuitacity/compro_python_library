# https://atcoder.jp/contests/abc083/tasks/abc083_a
a,b,c,d = map(int,input().split())
l,r=a+b,c+d
print("Left") if l>r else print("Right") if l<r else print("Balanced")

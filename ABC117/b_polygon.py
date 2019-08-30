# https://atcoder.jp/contests/abc117/tasks/abc117_b
n = int(input())
l = sorted(map(int,input().split()), reverse=1)
print("Yes" if l[0]<sum(l[1:]) else "No")

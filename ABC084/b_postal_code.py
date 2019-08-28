# https://atcoder.jp/contests/abc084/tasks/abc084_b
a,b = map(int,input().split())
s = input()
print("Yes" if s[a]=='-' and s.count('-')==1 else "No")

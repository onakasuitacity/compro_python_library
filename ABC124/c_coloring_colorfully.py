# https://atcoder.jp/contests/abc124/tasks/abc124_c
s = input()
n = len(s)
a = "10"*(n//2) + '1'*(n%2)
p = 0

for i in range(n):
    if s[i]!=a[i]: p+=1

print(min(p,n-p))

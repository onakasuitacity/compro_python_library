# https://atcoder.jp/contests/abc066/tasks/abc066_b
s = input()
n = len(s)//2

for i in range(1,n):
    if s[:n-i]==s[n-i:2*(n-i)]:
        print(2*(n-i))
        break

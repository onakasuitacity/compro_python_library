# https://atcoder.jp/contests/abc032/tasks/abc032_b
s = input()
k = int(input())
a = set()
for i in range(len(s)-k+1):
    a.add(s[i:i+k])
print(len(a))

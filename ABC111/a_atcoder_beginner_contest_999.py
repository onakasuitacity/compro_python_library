# https://atcoder.jp/contests/abc111/tasks/abc111_a
n = input()
a = ''
for i in range(len(n)):
    a += '1' if n[i]=='9' else '9'
print(int(a))

# https://atcoder.jp/contests/abc104/tasks/abc104_b
s = input()
flag = True
if s[0]!='A': flag=False
if s[2:-1].count('C')!=1: flag=False
if flag:
    l = list(s[2:-1])
    l.remove('C')
    s = s[1] + ''.join(l) + s[-1]
    if s!=s.lower(): flag=False
print("AC" if flag else "WA")

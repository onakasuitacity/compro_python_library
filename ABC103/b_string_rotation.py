# https://atcoder.jp/contests/abc103/tasks/abc103_b
s,t = [input() for _ in range(2)]
for _ in range(len(s)):
    if s==t:
        print("Yes")
        break
    s = s[1:]+s[0]
else: print("No")

# https://atcoder.jp/contests/abc116/tasks/abc116_b
s = int(input())
t = set()
count = 1

while(s not in t):
    t.add(s)
    count += 1
    s = s//2 if s%2==0 else 3*s+1

print(count)

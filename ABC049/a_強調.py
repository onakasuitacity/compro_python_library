# https://atcoder.jp/contests/arc049/tasks/arc049_a
s = list(input())
n = list(map(int,input().split()))[::-1]
for k in n:
    s.insert(k,'"')
print(''.join(s))

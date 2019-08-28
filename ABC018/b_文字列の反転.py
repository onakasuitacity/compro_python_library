# https://atcoder.jp/contests/abc018/tasks/abc018_2
s = list(input())
n = int(input())
for _ in range(n):
    l,r = map(int,input().split())
    s = s[:l-1] + s[l-1:r][::-1] + s[r:]    
print(''.join(s))

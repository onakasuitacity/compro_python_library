# https://atcoder.jp/contests/abc037/tasks/abc037_b
n,q = map(int,input().split())
a = [0 for i in range(n)]
for i in range(q):
    l,r,t = map(int,input().split())
    for j in range(l,r+1):
        a[j-1]=t

print(*a, sep='\n')

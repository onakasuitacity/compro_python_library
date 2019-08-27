# https://atcoder.jp/contests/abc031/tasks/abc031_b
l,h = map(int,input().split())
n = int(input())
for i in range(n):
    a = int(input())
    print(-1 if a>h else 0 if a>=l else l-a)

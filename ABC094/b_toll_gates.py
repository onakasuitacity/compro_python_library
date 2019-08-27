# https://atcoder.jp/contests/abc094/tasks/abc094_b
n,m,p = map(int,input().split())
a = list(map(int,input().split()))
up = len(list(filter(lambda x:x>p,a)))
down = len(list(filter(lambda x:x<p,a)))
print(min(up,down))

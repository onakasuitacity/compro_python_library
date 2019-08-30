# https://atcoder.jp/contests/abc066/tasks/arc077_a
n = int(input())
l = list(map(int,input().split()))
print(*(l[::-2]+l[n%2::2]))

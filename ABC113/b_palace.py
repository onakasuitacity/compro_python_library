# https://atcoder.jp/contests/abc113/tasks/abc113_b
n = int(input())
t,a = map(int,input().split())
h = list(map(lambda x:abs(t-int(x)*0.006-a),input().split()))
print(h.index(min(h))+1)

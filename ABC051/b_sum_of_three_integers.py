# https://atcoder.jp/contests/abc051/tasks/abc051_b
import itertools
k,s = map(int,input().split())
print(sum([0<=s-x-y<=k for x,y in itertools.product(range(k+1),range(k+1))]))

# https://atcoder.jp/contests/abc122/tasks/abc122_c
import itertools

N,Q = map(int,input().split())
S = input()

b = [0]+[S[i]=='A' and S[i+1]=='C' for i in range(N-1)]
b = list(itertools.accumulate(b))

for _ in range(Q):
    l,r = map(int,input().split())
    print(b[r-1]-b[l-1])

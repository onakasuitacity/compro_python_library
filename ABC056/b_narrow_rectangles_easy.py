# https://atcoder.jp/contests/abc056/tasks/abc056_b
w,a,b=map(int,input().split())
if b-a-w>=0: print(b-a-w)
elif a-b-w>=0: print(a-b-w)
else: print(0)

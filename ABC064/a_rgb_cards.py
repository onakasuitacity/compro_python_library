# https://atcoder.jp/contests/abc064/tasks/abc064_a
r,g,b = map(int,input().split())
print("YES") if (10*g+b)%4==0 else print("NO")

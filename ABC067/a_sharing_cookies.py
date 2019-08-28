# https://atcoder.jp/contests/abc067/tasks/abc067_a
a,b = map(int,input().split())
print("Impossible") if all((a%3,b%3,(a+b)%3)) else print("Possible")

# https://atcoder.jp/contests/abc059/tasks/abc059_b
a,b = [int(input()) for _ in range(2)]
print("GREATER") if a>b else print("LESS") if a<b else print("EQUAL")

# https://atcoder.jp/contests/abc054/tasks/abc054_a
a,b = map(lambda x:int(x)+13*(x=='1'),input().split())
print("Alice") if a>b else print("Bob") if a<b else print("Draw")

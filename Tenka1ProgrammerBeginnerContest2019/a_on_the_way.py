# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_a
a,b,c = map(int,input().split())
print("Yes") if a<=c<=b or b<=c<=a else print("No")

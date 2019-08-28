# https://atcoder.jp/contests/abc015/tasks/abc015_2
n = int(input())
a = list(filter(lambda x:x,list(map(int,input().split()))))
print((sum(a)-1)//len(a)+1)

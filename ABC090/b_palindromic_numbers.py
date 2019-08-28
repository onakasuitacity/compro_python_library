# https://atcoder.jp/contests/abc090/tasks/abc090_b
a,b = map(int,input().split())
count = 0
for i in range(a,b+1):
    s = str(i)
    if s[0]==s[-1] and s[1]==s[-2]: count+=1
print(count)

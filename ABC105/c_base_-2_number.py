# https://atcoder.jp/contests/abc105/tasks/abc105_c
n = int(input())
digit = 1
ex = ""
while(n):
    if n%2==0:
        ex='0'+ex
    else:
        ex='1'+ex
        n-=-1+2*(digit%2)
    n=n//2
    digit+=1
print(ex if ex else "0")

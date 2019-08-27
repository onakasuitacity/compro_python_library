# https://atcoder.jp/contests/abc083/tasks/abc083_b
N,A,B = map(int,input().split())
count = 0

for i in range(N+1):
    s = sum(map(int,list(str(i))))
    if A <= s and s <= B:
        count += i

print(count)

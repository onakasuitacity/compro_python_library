# https://atcoder.jp/contests/abc113/tasks/abc113_c
n,m = map(int,input().split())
C = [[i]+list(map(int,input().split())) for i in range(m)]
C.sort(key=lambda c:c[1:])
prev = 0
count = 0
for c in C:
    if prev==c[1]: count+=1
    else: count=1
    c.append(format(c[1],'0>6')+format(count,'0>6'))
    prev=c[1]

for c in sorted(C, key=lambda c:c[0]):
    print(c[3])

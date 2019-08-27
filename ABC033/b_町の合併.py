# https://atcoder.jp/contests/abc033/tasks/abc033_b
pmax = 0
psum = 0
name = ''
for i in range(int(input())):
    s,p = input().split()
    p = int(p)
    psum += p
    if p > pmax:
        pmax,name = p,s
print(name if 2*pmax>psum else 'atcoder')

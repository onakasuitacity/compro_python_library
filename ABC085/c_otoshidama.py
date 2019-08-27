# https://atcoder.jp/contests/abc085/tasks/abc085_c
N,Y = map(int,input().split())
Y = Y//1000
flag = False

for i in range(N+1):
    for j in range(N+1-i):
        if 10*i+5*j+(N-i-j) == Y:
            print(i,j,N-i-j)
            flag = True
            break
    if flag:
        break

if flag is False:
    print(-1,-1,-1)

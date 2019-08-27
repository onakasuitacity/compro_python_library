# https://atcoder.jp/contests/abs/tasks/arc089_a
N = int(input())
flag = True
t_0,x_0,y_0 = 0,0,0

for i in range(N):
    t_1,x_1,y_1 = map(int,(input().split()))
    dt = t_1 - t_0
    dx = abs(x_1 - x_0)
    dy = abs(y_1 - y_0)
    if dx+dy<=dt and (dx+dy+dt)%2==0:
        t_0,x_0,y_0 = t_1,x_1,y_1
    else:
        flag = False
        break

print("Yes") if flag else print("No")

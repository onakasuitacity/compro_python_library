# https://atcoder.jp/contests/abc119/tasks/abc119_b
jpy,btc=0,0
for _ in range(int(input())):
    x,u = input().split()
    if u=="JPY": jpy+=int(x) 
    else: btc+=float(x)
print(jpy+380000*btc)

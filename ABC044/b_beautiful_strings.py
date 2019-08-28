# https://atcoder.jp/contests/abc044/tasks/abc044_b
w = input()
for s in "abcdefghijklmnopqrstuvwxyz":
    if w.count(s)%2!=0:
        print("No")
        break
else:
    print("Yes") 

# https://atcoder.jp/contests/arc065/tasks/arc065_a
S = input()[::-1]
n = len(S)
count = 0
flag = True

while count<n:
    if S[count:count+5] == "dream"[::-1]:
        count += 5
    elif S[count:count+7] == "dreamer"[::-1]:
        count += 7
    elif S[count:count+5] == "erase"[::-1]:
        count += 5
    elif S[count:count+6] == "eraser"[::-1]:
        count += 6
    else:
        flag = False
        break

print("YES") if flag else print("NO")

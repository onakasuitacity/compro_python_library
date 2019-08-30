# https://atcoder.jp/contests/abc120/tasks/abc120_c
S = input()
stack = []
count = 0
for s in S:
    if (not stack) or stack[-1]==s:
        stack.append(s)
    else:
        stack.pop()
        count += 2
print(count)

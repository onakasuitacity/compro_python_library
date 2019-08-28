# https://atcoder.jp/contests/abc043/tasks/abc043_b
S = input()
ans = []
for s in S:
    if s=='B' and ans:
        ans.pop(-1)
    elif s!='B':
        ans.append(s)
print(''.join(ans))

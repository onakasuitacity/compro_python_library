# https://atcoder.jp/contests/abc098/tasks/abc098_b
N = int(input())
S = input()
count = 0
for i in range(N):
    count = max(len(set(S[:i])&set(S[i:])),count)
print(count)

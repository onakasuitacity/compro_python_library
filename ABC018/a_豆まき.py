# https://atcoder.jp/contests/abc018/tasks/abc018_1
a = [int(input()) for _ in range(3)]
b = sorted(a,reverse=True)
for i in a:
    print(b.index(i)+1)

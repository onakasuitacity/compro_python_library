# https://atcoder.jp/contests/arc001/tasks/arc001_1
n = int(input())
c = input()
l = [c.count(str(i)) for i in range(1,5)]
print(max(l),min(l))

# https://atcoder.jp/contests/abc123/tasks/abc123_b
l = [int(input()) for _ in range(5)]
a = list(map(lambda x:-(-x//10)*10,l))
b = list(map(lambda x:x%10 if x%10 else 10,l))
print(sum(a)-(10-min(b)))

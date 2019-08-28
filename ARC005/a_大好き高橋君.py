# https://atcoder.jp/contests/arc005/tasks/arc005_1
count = 0
input()
for w in input()[:-1].split():
    count += (w in ["TAKAHASHIKUN","Takahashikun","takahashikun"])
print(count)

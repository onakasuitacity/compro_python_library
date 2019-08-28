# https://atcoder.jp/contests/abc038/tasks/abc038_b
h1,w1 = map(int,input().split())
h2,w2 = map(int,input().split())
print("YES") if h1==h2 or h1==w2 or w1==h2 or w1==w2 else print("NO")

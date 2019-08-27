# https://atcoder.jp/contests/abc112/tasks/abc112_b
N,T = map(int,input().split())
score = 1001
for i in range(N):
    c,t = map(int,input().split())
    if t<=T: score = min(score,c)
        
print("TLE" if score==1001 else score)

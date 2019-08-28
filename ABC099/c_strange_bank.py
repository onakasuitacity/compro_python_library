# https://atcoder.jp/contests/abc099/tasks/abc099_c
def nsin(X,n):
    if(int(X/n)):
        return nsin(int(X/n),n)+str(X%n)
    return str(X)
 
N = int(input())
score = N
for i in range(N+1):
    score = min(score,sum(map(int,nsin(i,6)+nsin(N-i,9))))
print(score)

# https://atcoder.jp/contests/abc140/tasks/abc140_d
def resolve():
    n,k=map(int,input().split())
    S=input()
    lr=0
    rl=0
    score=0
    for i in range(n-1):
        score+=(S[i]==S[i+1])
        lr+=(S[i]=="L" and S[i+1]=="R")
        rl+=(S[i]=="R" and S[i+1]=="L")
    print(score+min(k,lr)+min(k,rl))
resolve()

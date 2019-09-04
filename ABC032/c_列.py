# https://atcoder.jp/contests/abc032/tasks/abc032_c
def resolve():
    n,k=map(int,input().split())
    S=[int(input()) for _ in range(n)]
    if 0 in S:
        print(n)
        return

    r=0
    value=1
    score=0
    for l in range(n):
        while(r<n and value*S[r]<=k):
            value*=S[r]
            r+=1
        score=max(score,r-l)
        if l==r: r+=1
        else: value//=S[l]
    print(score)
resolve()

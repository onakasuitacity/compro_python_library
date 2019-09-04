# https://atcoder.jp/contests/abc098/tasks/arc098_b
def resolve():
    n=int(input())
    A=list(map(int,input().split()))

    ans=0
    r=0
    xor=0
    sum=0

    for l in range(n):
        while(r<n and xor^A[r]==sum+A[r]):
            xor^=A[r]
            sum+=A[r]
            r+=1
        if l==r: r+=1 # 起こり得ない
        else:
            ans+=r-l
            xor^=A[l]
            sum-=A[l]
    print(ans)
resolve()

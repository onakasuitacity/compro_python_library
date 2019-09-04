# https://atcoder.jp/contests/arc022/tasks/arc022_2
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    B=set()
    ans=0
    r=0
    for l in range(n):
        while(r<n and A[r] not in B):
            B.add(A[r])
            r+=1
        if l==r: r+=1 # 起こり得ない
        else:
            ans=max(ans,r-l)
            B.remove(A[l])
    print(ans)
resolve()

# https://atcoder.jp/contests/abc038/tasks/abc038_c
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    ans=0
    count=1
    for i in range(n-1):
        if A[i]<A[i+1]:
            count+=1
        else:
            ans+=count*(count+1)//2
            count=1
    ans+=count*(count+1)//2
    print(ans)
resolve()

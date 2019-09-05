# https://atcoder.jp/contests/abc093/tasks/arc094_a
def resolve():
    a,b,c=sorted(list(map(int,input().split())))
    ans=c-b
    a+=c-b
    b=c
    if (c-a)%2==0: print(ans+(c-a)//2)
    else: print(ans+2+(c-a)//2)
resolve()

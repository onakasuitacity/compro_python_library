# https://atcoder.jp/contests/abc062/submissions/7666160
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    if h%3==0 or w%3==0:
        print(0)
        return
    ans=INF
    # hをtrisect, wをbisect
    a=(h//3)*w
    b=(h-h//3)*(w//2)
    c=h*w-a-b
    ans=min(ans,max(a,b,c)-min(a,b,c))
    a=(h//3+1)*w
    b=(h-h//3-1)*(w//2)
    c=h*w-a-b
    ans=min(ans,max(a,b,c)-min(a,b,c))
    # hをbisect, wをtrisect
    a=(w//3)*h
    b=(w-w//3)*(h//2)
    c=h*w-a-b
    ans=min(ans,max(a,b,c)-min(a,b,c))
    a=(w//3+1)*h
    b=(w-w//3-1)*(h//2)
    c=h*w-a-b
    ans=min(ans,max(a,b,c)-min(a,b,c))
    # h,wをtrisect
    print(min(ans,h,w))
resolve()

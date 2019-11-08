# https://atcoder.jp/contests/abc116/tasks/abc116_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    H=list(map(int,input().split()))
    cnt=0
    while(sum(H)):
        flag=False
        for i in range(n):
            if((not flag) and H[i]>0):
                flag=True
            if(flag and H[i]==0):
                break
            if(flag):
                H[i]-=1
        cnt+=1
    print(cnt)
resolve()

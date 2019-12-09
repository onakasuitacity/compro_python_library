# https://atcoder.jp/contests/agc022/tasks/agc022_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    if(n==3):
        print(2,5,63)
        return
    if(n==4):
        print(2,5,20,63)
        return

    q=n//8
    r=n%8
    ans=list(i for i in range(1,12*q+1) if(i%2==0 or i%3==0))
    x=12*q
    if(r==1):
        ans+=[x+6]
    elif(r==2):
        ans+=[x+2,x+4]
    elif(r==3):
        ans+=[x+2,x+4,x+6]
    elif(r==4):
        ans+=[x+2,x+4,x+6,x+12]
    elif(r==5):
        ans+=[x+2,x+3,x+4,x+6,x+9]
    elif(r==6):
        ans+=[x+2,x+3,x+4,x+6,x+9,x+12]
    elif(r==7):
        ans+=[x+2,x+3,x+4,x+6,x+8,x+9,x+10]
    print(*ans)
resolve()

# https://atcoder.jp/contests/abc130/submissions/8300701
import sys
sys.setrecursionlimit(2147483647)
INF=10**9
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    X=[[INF,-INF] for _ in range(3)]
    Y=[[INF,-INF] for _ in range(3)]
    for _ in range(n):
        x,y,d=input().split()
        x=int(x); y=int(y)
        if(d=='R'):
            X[2][0]=min(X[2][0],x)
            X[2][1]=max(X[2][1],x)
            Y[1][0]=min(Y[1][0],y)
            Y[1][1]=max(Y[1][1],y)
        elif(d=='L'):
            X[0][0]=min(X[0][0],x)
            X[0][1]=max(X[0][1],x)
            Y[1][0]=min(Y[1][0],y)
            Y[1][1]=max(Y[1][1],y)
        elif(d=='U'):
            X[1][0]=min(X[1][0],x)
            X[1][1]=max(X[1][1],x)
            Y[2][0]=min(Y[2][0],y)
            Y[2][1]=max(Y[2][1],y)
        elif(d=='D'):
            X[1][0]=min(X[1][0],x)
            X[1][1]=max(X[1][1],x)
            Y[0][0]=min(Y[0][0],y)
            Y[0][1]=max(Y[0][1],y)

    T=[0]
    for i in range(3):
        for j in range(i): # i>j
            t=-(X[i][0]-X[j][0])/(i-j)
            if(t>0): T.append(t)
            t=-(X[i][1]-X[j][1])/(i-j)
            if(t>0): T.append(t)
            t=-(Y[i][0]-Y[j][0])/(i-j)
            if(t>0): T.append(t)
            t=-(Y[i][1]-Y[j][1])/(i-j)
            if(t>0): T.append(t)

    def f(t):
        x_min=min(X[0][0],X[1][0]+t,X[2][0]+2*t)
        x_max=max(X[0][1],X[1][1]+t,X[2][1]+2*t)
        y_min=min(Y[0][0],Y[1][0]+t,Y[2][0]+2*t)
        y_max=max(Y[0][1],Y[1][1]+t,Y[2][1]+2*t)
        return (x_max-x_min)*(y_max-y_min)

    ans=float("inf")
    for t in T:
        ans=min(ans,f(t))
    print(ans)
resolve()

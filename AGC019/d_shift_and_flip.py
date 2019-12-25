# https://atcoder.jp/contests/agc019/tasks/agc019_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    A,B=(list(map(int,input())) for _ in range(2))
    n=len(A)

    # B が全て0のときだけ例外処理
    if(all(b==0 for b in B)):
        if(all(a==0 for a in A)):
            print(0)
        else:
            print(-1)
        return

    def calc():
        L=[INF]*n # L[i]: i 以下で B の bit が立っているもののうち、i-L[i] が最大となるもの
        R=[INF]*n # R[i]: i 以上で B の bit が立っているもののうち、i+R[i] が最小となるもの

        tmp=0
        for i,b in enumerate(2*B):
            if(b==1):
                tmp=i
            if(i>=n):
                L[i-n]=i-tmp

        tmp=0
        for i,b in enumerate(2*B[::-1]):
            if(b==1):
                tmp=i
            if(i>=n):
                R[i-n]=i-tmp
        R.reverse()

        res=INF
        for d in range(n): # トータルの右シフトが d 回
            LR=[]
            cnt=0 # flip する回数
            for i in range(n):
                if(A[i]==B[(i+d)%n]): continue
                cnt+=1
                if(R[i]<=d): continue
                LR.append((L[i],R[i]-d))

            if(not LR): # 左右に余分に移動する必要が無い場合
                res=min(res,cnt+d)
                continue

            LR.sort()
            k=len(LR)
            X,Y=[[None]*k for _ in range(2)]
            for i in range(k):
                X[i],Y[i]=LR[i]
            for i in range(k-1,0,-1):
                Y[i-1]=max(Y[i-1],Y[i])

            score=min(X[-1],Y[0]) # maxX, maxY
            for i in range(k-1):
                score=min(score,X[i]+Y[i+1])
            res=min(res,cnt+d+score*2)
        
        return res

    ans=INF
    ans=min(ans,calc())
    A.reverse()
    B.reverse()
    ans=min(ans,calc())
    print(ans)
resolve()

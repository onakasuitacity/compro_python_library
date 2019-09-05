# https://atcoder.jp/contests/abc059/tasks/arc072_a
def resolve():
    n=int(input())
    A=[int(i) for i in input().split()]
    def check(A,flag): # flag=Trueなら上から、Falseなら下から
        cumsum=0
        ans=0
        for a in A:
            cumsum+=a
            if cumsum<=0 and flag:
                ans+=1-cumsum
                cumsum=1
            elif cumsum>=0 and (not flag):
                ans+=1+cumsum
                cumsum=-1
            flag = (not flag)
        return ans
    print(min(check(A,True),check(A,False)))
resolve()

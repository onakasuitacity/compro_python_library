# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[int(input()) for _ in range(n)]

    # 最初の人には1円で売る
    ans=A[0]-1
    p=2
    # 以降は残りの所持金をp-1にできるようにする
    for a in A[1:]:
        if(a<p): # 状況変化無し
            continue
        elif(a==p): # 所持金が元々 p の場合はどうしようもないので+1する
            p+=1
        else: # 基本 p で売って、最後は残りの所持金を p 以下にするように調整
            ans+=(a-1)//p
    print(ans)
resolve()

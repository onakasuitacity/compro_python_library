# https://atcoder.jp/contests/abc003/tasks/abc003_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=input()
    T=input()
    X=set("atcoder")

    for s,t in zip(S,T):
        if(s==t): continue
        if(s!='@' and t!='@'):
            print("You will lose")
            return
        if(s=='@'):
            if(t not in X):
                print("You will lose")
                return
        if(t=='@'):
            if(s not in X):
                print("You will lose")
                return
    print("You can win")
resolve()

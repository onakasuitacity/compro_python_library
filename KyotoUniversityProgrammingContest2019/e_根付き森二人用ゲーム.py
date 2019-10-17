# https://atcoder.jp/contests/kupc2019/tasks/kupc2019_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def solve_tree(P):
    n=len(P)+1
    E=[[] for _ in range(n)]
    for i,p in enumerate(P,1):
        E[p].append(i)
    even=[0]*n; odd=[0]*n # dp
    def dfs(v): # 有向木だから親の情報要らない
        if(not E[v]): # leafは(0,1)
            odd[v]=1
            return
        e=o=1 # 子たちの最小値
        for nv in E[v]:
            dfs(nv)
            e=min(e,even[nv])
            o=min(o,odd[nv])
        even[v]=e^1
        odd[v]=o^1
    dfs(0)
    return even[0],odd[0]

def resolve():
    n=int(input())
    # (even,odd)
    xx=0 # 先手に選択の自由あり＝入れたら勝ち
    oo=0 # 後手に選択の自由あり＝入れられることはない
    xo=0 # 先手入れ替わらない＝使用してもしなくても関係ない
    ox=0 # 先手入れ替わる
    for _ in range(n):
        input()
        e,o=solve_tree(list(map(lambda x:int(x)-1,input().split())))
        if(e and o): oo+=1
        elif(e and (not o)): ox+=1
        elif((not e) and o): xo+=1
        else: xx+=1
    print("Alice" if(xx or ox&1) else "Bob")
resolve()

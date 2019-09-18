# https://atcoder.jp/contests/abc001/tasks/abc001_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    c=1500 # 24*60=1440
    imos=[0]*c
    for _ in range(n):
        s,e=input().split('-')
        s=int(s[:2])*60+int(s[2])*10+(int(s[3])//5)*5
        e=int(e[:2])*60+int(e[2])*10-((-int(e[3]))//5)*5
        imos[s]+=1
        imos[e+1]-=1
    for i in range(c-1):
        imos[i+1]+=imos[i]
    flag=False
    for i in range(c):
        if (not flag) and imos[i]>0:
            start=i
            start=str(start//60).zfill(2)+str(start%60).zfill(2)
            flag=True
        elif flag and imos[i]==0:
            end=i-1
            end=str(end//60).zfill(2)+str(end%60).zfill(2)
            print(start+'-'+end)
            flag=False
resolve()

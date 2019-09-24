# https://atcoder.jp/contests/abc039/tasks/abc039_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    text="WBWBWWBWBWBW"*2
    pattern=input()[:12]
    i=text.find(pattern)
    print(["Do",'',"Re",'',"Mi","Fa",'',"So",'',"La",'',"Si"][i])
resolve()

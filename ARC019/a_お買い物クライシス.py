# https://atcoder.jp/contests/arc019/tasks/arc019_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    print(input().replace('O','0').replace('D','0').replace('I','1').replace('Z','2').replace('S','5').replace('B','8'))
resolve()

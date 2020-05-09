# Z-algorithm (O(N))
# https://deve68.hatenadiary.org/entry/20120201/1328109890
# https://snuke.hatenablog.com/entry/2014/12/03/214243
def Z(S):
    n = len(S)
    res = [0] * n
    res[0] = n
    l = r = 0
    for i in range(1, n):
        if res[i - l] < r - i: # 過去の結果が全て使える
            res[i] = res[i - l]
        else:
            l = i
            r = max(i, r) # i < r ならば過去の結果が一部使える
            while r < n and S[r - l] == S[r]: r += 1
            res[i] = r - l
    return res

print(Z("abaaabaabb")) # [10, 0, 1, 1, 4, 0, 1, 2, 0, 0]

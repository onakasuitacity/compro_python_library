# https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
class RollingHash(object):
    from random import randint
    __MASK30=(1<<30)-1
    __MASK31=(1<<31)-1
    __MOD=(1<<61)-1
    __base=randint(129,__MASK31)

    def __init__(self,s:str):
        n=len(s)
        H=[0]*(n+1); P=[1]*(n+1)
        for i in range(n):
            H[i+1]=self.__modulo(self.__multiple(H[i],self.__base)+ord(s[i]))
            P[i+1]=self.__modulo(self.__multiple(P[i],self.__base))
        self.__H=H; self.__P=P

    def __multiple(self,a,b):
        au=a>>31
        ad=a&self.__MASK31
        bu=b>>31
        bd=b&self.__MASK31
        m=ad*bu+au*bd
        mu=m>>30
        md=m&self.__MASK30
        return 2*au*bu+mu+(md<<31)+ad*bd

    def __modulo(self,x):
        x=(x&self.__MOD)+(x>>61)
        if(x>self.__MOD): x-=self.__MOD
        return x

    def hash(self,l,r):
        H=self.__H; P=self.__P
        res=H[r]+self.__MOD*3-self.__multiple(H[l],P[r-l])
        if(res<0): return res+self.__MOD
        else: return self.__modulo(res)

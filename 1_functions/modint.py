# modint
# https://qiita.com/wotsushi/items/c936838df992b706084c
class mint(object):
    MOD=998244353

    def __init__(self,x):
        self.__x=x%self.MOD

    def __repr__(self):
        return str(self.__x)

    def __add__(self,other):
        return mint(self.__x+other.__x) if isinstance(other,mint) else mint(self.__x+other)

    def __sub__(self,other):
        return mint(self.__x-other.__x) if isinstance(other,mint) else mint(self.__x-other)

    def __mul__(self,other):
        return mint(self.__x*other.__x) if isinstance(other,mint) else mint(self.__x*other)

    def __truediv__(self,other):
        return mint(self.__x*pow(other.__x,self.MOD-2,self.MOD)) if isinstance(other, mint) else mint(self.__x*pow(other, self.MOD-2,self.MOD))

    def __pow__(self,other):
        return mint(pow(self.__x,other.__x,self.MOD)) if isinstance(other,mint) else mint(pow(self.__x,other,self.MOD))

    __radd__=__add__

    def __rsub__(self,other):
        return mint(other.__x-self.__x) if isinstance(other,mint) else mint(other-self.__x)

    __rmul__=__mul__

    def __rtruediv__(self,other):
        return mint(other.__x*pow(self.__x,self.MOD-2,self.MOD)) if isinstance(other,mint) else mint(other*pow(self.__x,self.MOD-2,self.MOD))

    def __rpow__(self,other):
        return mint(pow(other.__x,self.__x,self.MOD)) if isinstance(other,mint) else mint(pow(other,self.__x,self.MOD))

# https://scrapbox.io/data-structures/Sliding_Window_Aggregation
class SWAG(object):
    def __init__(self,dot):
        self.__front=[]
        self.__back=[]
        self.__dot=dot

    def __bool__(self):
        return True if(self.__front or self.__back) else False

    def __len__(self):
        return len(self.__front)+len(self.__back)

    def sum(self):
        assert(self)
        front=self.__front; back=self.__back
        if(not front): return back[-1][1]
        elif(not back): return front[-1][1]
        else: return self.__dot(front[-1][1],back[-1][1])

    def append(self,x):
        back=self.__back
        if(not back): back.append((x,x))
        else: back.append((x,self.__dot(back[-1][1],x)))

    def popleft(self):
        assert(self)
        front=self.__front; back=self.__back
        if(not front):
            front.append((back[-1][0],back[-1][0]))
            back.pop()
            while(back):
                front.append((back[-1][0],self.__dot(back[-1][0],front[-1][1])))
                back.pop()
        front.pop()

# example
from operator import add
swag=SWAG(add)
swag.append(1)
swag.append(2)
swag.append(3)
swag.popleft()
print(swag.sum())
print(len(swag))

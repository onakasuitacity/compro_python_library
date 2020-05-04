# https://scrapbox.io/data-structures/Sliding_Window_Aggregation
class SWAG(object):
    def __init__(self, dot):
        self.front, self.back, self.dot = [], [], dot

    def __bool__(self):
        return bool(self.front) or bool(self.back)

    def __len__(self):
        return len(self.front) + len(self.back)

    def append(self, val):
        if not self.back: self.back.append((val, val))
        else: self.back.append((val, self.dot(self.back[-1][1], val)))

    def popleft(self):
        if not self.front:
            self.front.append((self.back[-1][0], self.back[-1][0]))
            self.back.pop()
            while self.back:
                self.front.append((self.back[-1][0], self.dot(self.back[-1][0], self.front[-1][1])))
                self.back.pop()
        return self.front.pop()[0]

    def sum(self):
        if not self.front: return self.back[-1][1]
        elif not self.back: return self.front[-1][1]
        else: return self.dot(self.front[-1][1], self.back[-1][1])

# example
from operator import add
swag=SWAG(add)
swag.append(1)
swag.append(2)
swag.append(3)
print(swag.popleft())
print(swag.sum())
print(len(swag))

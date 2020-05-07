# https://scrapbox.io/data-structures/Sliding_Window_Aggregation
class SWAG(object):
    def __init__(self, dot):
        self._front, self._back, self._dot = [], [], dot

    def __bool__(self):
        return bool(self._front) or bool(self._back)

    def __len__(self):
        return len(self._front) + len(self._back)

    def append(self, val):
        if not self._back: self._back.append((val, val))
        else: self._back.append((val, self._dot(self._back[-1][1], val)))

    def popleft(self):
        if not self._front:
            self._front.append((self._back[-1][0], self._back[-1][0]))
            self._back.pop()
            while self._back:
                self._front.append((self._back[-1][0], self._dot(self._back[-1][0], self._front[-1][1])))
                self._back.pop()
        return self._front.pop()[0]

    def sum(self):
        if not self._front: return self._back[-1][1]
        elif not self._back: return self._front[-1][1]
        else: return self._dot(self._front[-1][1], self._back[-1][1])

# example
from operator import add
swag = SWAG(add)
swag.append(1)
swag.append(2)
swag.append(3)
print(swag.popleft())
print(swag.sum())
print(len(swag))

# https://scrapbox.io/data-structures/Sliding_Window_Aggregation
class SWAG(object):
    def __init__(self, dot):
        self._front, self._back, self._dot = [], [], dot

    def __bool__(self):
        return bool(self._front) or bool(self._back)

    def __len__(self):
        return len(self._front) + len(self._back)

    def append(self, val):
        if self._back:
            self._back.append((val, self._dot(self._back[-1][1], val)))
        else:
            self._back.append((val, val))

    def popleft(self):
        assert self
        if not self._front:
            l = self._back.pop()[0]
            self._front.append((l, l))
            while self._back:
                l = self._back.pop()[0]
                self._front.append((l, self._dot(l, self._front[-1][1])))
        return self._front.pop()[0]

    def sum(self):
        assert self
        if not self._back:
            return self._front[-1][1]
        elif not self._front:
            return self._back[-1][1]
        else:
            return self._dot(self._front[-1][1], self._back[-1][1])

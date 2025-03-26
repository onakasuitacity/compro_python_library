# https://scrapbox.io/data-structures/Sliding_Window_Aggregation
# https://qiita.com/Shirotsume/items/4a2837b5895ef9a7aeb1
class SWAG(object):
    def __init__(self, dot):
        self._front, self._back, self._dot = [], [], dot

    def __bool__(self):
        return bool(self._front) or bool(self._back)

    def __len__(self):
        return len(self._front) + len(self._back)

    def __getitem__(self, i):
        if i < len(self._front):
            return self._front[~i][0]
        return self._back[i - len(self._front)][0]

    def __repr__(self):
        return str([self[i] for i in range(len(self))])

    def append(self, val):
        if self._back:
            self._back.append((val, self._dot(self._back[-1][1], val)))
        else:
            self._back.append((val, val))
    
    def appendleft(self, val):
        if self._front:
            self._front.append((val, self._dot(val, self._front[-1][1])))
        else:
            self._front.append((val, val))

    def pop(self):
        if not self._back:
            N = len(self._front)
            if N == 1:
                return self._front.pop()[0]
            N2 = N - 1 >> 1
            front, back, dot = self._front, self._back, self._dot
            prod = front[N2][0]
            back.append((prod, prod))
            for val, _ in front[:N2][::-1]:
                prod = dot(prod, val)
                back.append((val, prod))
            prod = front[N2 + 1][0]
            _front = [(prod, prod)]
            for val, _ in front[N2 + 2:]:
                prod = dot(val, prod)
                _front.append((val, prod))
            self._front = _front
        return self._back.pop()[0]

    def popleft(self):
        if not self._front:
            N = len(self._back)
            if N == 1:
                return self._back.pop()[0]
            N2 = N - 1 >> 1
            front, back, dot = self._front, self._back, self._dot
            prod = back[N2][0]
            front.append((prod, prod))
            for val, _ in back[:N2][::-1]:
                prod = dot(val, prod)
                front.append((val, prod))
            prod = back[N2 + 1][0]
            _back = [(prod, prod)]
            for val, _ in back[N2 + 2:]:
                prod = dot(prod, val)
                _back.append((val, prod))
            self._back = _back
        return self._front.pop()[0]

    def prod(self):
        if not self._back:
            return self._front[-1][1]
        elif not self._front:
            return self._back[-1][1]
        else:
            return self._dot(self._front[-1][1], self._back[-1][1])

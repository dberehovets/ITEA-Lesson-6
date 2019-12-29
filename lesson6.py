class MyIter:

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        pass

    def __next__(self):
        if self._start < self._end:
            self._start += 1
            return self._start
        raise StopIteration()


obj = MyIter(0, 4)

extra_value = "token"
kwargs = {
    "sum": 12,
    "id": 134,
    "comment": "user_comm",
    "token": "123455"
}

d1 = dict(filter(lambda k: k != "token", **kwargs))
print(d1)

"""
Python iterators
- iterators are everywhere in python
- an object can be iterated upon
- an object which will return data, one element at a time
- python iterator object must implement two special methods
__iter__ and __next__ collectively called iterator protocol
- iter function returns an iterator
- when there are no more items remained in an iterator stopIter error is raised
- for loop in python internally uses iterator
"""

class PowTwo:
    def __init__(self, max):
        self.max = 1000

    def __iter__(self):
        self.n = 0
        return self

    def next(self):
        if self.n < self.max:
            res = 2 ** self.n
            self.n +=1
        return res

power = PowTwo(100)
my_iter = iter(power)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
"""
Python generators
- python generators are simple way of creating iterators
- a generator is a function that returns an iterator object which we can iterate over
- if a function contains at least one yield statement, it becomes a generator function in python
- both yield and return will return some value from the function
- whicle a return statement terminates a function entirely yield statement passes the fucntion saveing all
of its states and later conitnues from successive calls
- methods like iter and next are implemented automatically so we can iterate through the items using next
- local variables and theirs state are remembered during successive calls
- once function yields
"""


class PowTwo:
    def __init__(self, max):
        self.max = max

    def generate(self, n):
        for i in range(n):
            if self.max < 2**i:
                raise StopIteration
            yield 2**i


a = PowTwo(50)
for i in a.generate(7):
    print i
"""
python decorators
- used to add functionality to preexisting code
- this is called meta programming
- functions that take other function as arguments are called as higher order functions
- functions and methods are called callable as they can be called
- any object which implement special method __call__() is termed as callable
- decorator is callable that returns a callable
- decorator takes in a function, add some functionality to it, and return it
"""

def make_pretty(function):
    def inner():
        print "I got decorated"
        function()
    return inner

def ordinary():
    print "I am ordinary function"

ordinary()
pretty =  make_pretty(ordinary)
pretty()

print "---------------------------"

ordinary = make_pretty(ordinary)
ordinary()

print "---------------------------"

def make_pretty_(function):
    def inner():
        print "I got decorated"
        function()
    return inner

@make_pretty
def ordinary_():
    print "I am ordinary function"

ordinary()

print "---------------------------"

def check_divide(func):
    def inner(a, b):
        if b == 0:
            print "not applicable"
            return
        else:
            return func(a, b)
    return inner

@check_divide
def divide(a, b):
    return a/b

print divide(4,0)

print "----------chaining decorators----------"

def inner_decorator(func):
    def inner():
        print "inner decorator"
        func()
    return inner

def outer_decorator(func):
    def inner():
        print "outer decorator"
        func()
    return inner

#@outer_decorator
#@inner_decorator

def ordinary_function():
    print "ordinary function"

ordinary_function = outer_decorator(inner_decorator(ordinary_function))
ordinary_function()
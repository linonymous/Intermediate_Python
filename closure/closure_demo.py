"""
- A function inside function is called as nested function
- nested function can access variables of the enclosing scope
- In python these non local variables are read only by default
and we must declare them explicitly as non local in order to modify them.
"""

def print_msg(msg):
    def printer():
        print msg
    return printer

another = print_msg("swap")
another()

def multiplier_of(n):
    def mult(x):
        return x * n
    return mult

three = multiplier_of(3)
five = multiplier_of(5)

print three(5)
print five(7)
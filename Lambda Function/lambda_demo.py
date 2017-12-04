"""
******* Lambda Functions *******

- lambdas are one line functions
- they are also known as anonymous functions
- can be used when we are not using function twice in the code
- these functions are not bound to a name at run time
- lambda does not include a return statement
- it contains an expression that returns something
- this function has no name but can be called through the object is is assigned to
- used when encapsulate specific, non - reusable code without littering my code
with lot of little one line function
- lamda functions is always true in boolean context, it returns any value in case of false
- python support style of programming called functional programming, where you can pass
functions to other functions to do stuff
-lamdas are mainly used with map(),reduce(),filter()
"""

# Example 1
change_case = lambda string : string.lower()
print change_case("SWAPNIL")

# Example 2
greater = lambda a,b : a if a>b else b
print greater(6,10)

# Example 3
def make_incrementor(n):
    return lambda x: x + n

five = make_incrementor(5)
three = make_incrementor(3)

print five(4)
print three(3)

# Map using lambda, can have multiple iterable objects
# Map applies the function to all elements in the sequence it returns a new
# list with the element chnaged by function

bar = lambda x,y: x + y
foo_1 = [2, 1, 3, 5, 6, 8, 10, 11, 12, 13]
foo_2 = [1, 2, 8, 3, 3, 2, 7, 8, 3, 11]
m = map(bar, foo_1, foo_2)
print m

# Filtering using lambda, can have only one iterable object
# provides elegant way to filter out all the elemets of a list
# function filter needs a function f as its first arguement
# f returns boolean value therefore true or false
# only if f returns true, the element will be in the result list

bar = lambda x: x%2
f = filter(bar,foo_1)
print f

m_dict = [{"name":"swap"}, {"name":"somesh","hobby":"kickboxing"},{"name":"somesh","likes":"movie"}]
f = filter(lambda x: x['name'] == 'somesh', m_dict)
print f

# Reduce using lambda
# function returns single value
# continually applies function to the whole sequence
# finding max from list
max = lambda x, y : x if x > y else y
sum = lambda x,y : x + y

print reduce(sum, foo_1)




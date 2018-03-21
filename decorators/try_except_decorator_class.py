"""
     If forgot to add try except in the methods in class, add decorator to do try except stuff and it handles it on its own.
     Decorator is cool!
"""

"""use following in debug mode"""
#import pdb
#pdb.set_trace()

class person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.validate()

    def decorator(function):
        def wrapper(*args, **kargs):
            try:
                function(*args, **kargs)
            except Exception as e:
                print "No Worries! I, decorator, catched the exception.. :)"
        return wrapper

    @staticmethod
    def validate_age(age):
        if age < 0:
            raise Exception

    @staticmethod
    def validate_name(name):
        if len(name) == 0:
            raise Exception

    @decorator
    def validate(self):
        self.validate_age(self.age)
        self.validate_name(self.name)

    def show(self):
        print self.name, self.age

if __name__ == "__main__":
    per = person("swapil", -10)
    per.show()
    per = person("swapil", 21)
    per.show()

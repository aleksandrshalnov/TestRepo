def trace(func):
    def wrapper(*args, **kwargs):
        print("trace")
        _new_tuple = ()
        for one in args:
            _new_tuple += (one.upper(),)
        original_result = func(*_new_tuple, **kwargs)
        return original_result
    return wrapper

def add_1(func):
    def wrapper1(*words, **kwargs):
        new_words = ()
        print("add_1")
        for one in words:
            new_words += (one+"xx",)
        add_1_result = func(*new_words,**kwargs)
        return add_1_result
    return wrapper1



class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

    def test(self, *args, **kwargs):
        print(args)
        print(kwargs)

# John = Person("John", 32)
# John.age = 45
# John.about_me()
#tgggg

#hjhjhjhj
#hjhjhjhj#hjhjhjhj
#hjhjhjhj

# John.test(1,3,4,5, city="kostroma")

@trace
@add_1
def say(name,line):
        return f'{name}: {line}'


jane = say('Jane', 'Hello')
print(jane)

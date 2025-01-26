#Decorators: function that modify the behaviour of another functions or methods. they are applied using the @decorator_name syntax above the target function.
#A decorator wraps the original function or method after adding pre or post-processing steps without changing the function core logic 
#Example 
def decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("after call")
    return wrapper
@decorator 
def say_hello():
    prints("Hello!")
say_hello()


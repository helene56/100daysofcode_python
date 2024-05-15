# Python decorator function
# wrap around a function to give it more functionality
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2) # all the function that uses this decorator will now sleep for 2 sec. before getting executed
        function()
    return wrapper_function

def say_hello():
    print("hello")

def say_bye():
    print("Bye")

def say_greeting():
    print("how are you")

say_hello()
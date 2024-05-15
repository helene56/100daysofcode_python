# Python decorator function
# wrap around a function to give it more functionality
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2) # all the function that uses this decorator will now sleep for 2 sec. before getting executed
        function()
        function()
        # you could add something here that should happen after
    return wrapper_function

@delay_decorator # put in front of the function you want to delay
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("how are you")

decorated_function = delay_decorator(say_greeting) # does the same thing as @delay_decorator
decorated_function()
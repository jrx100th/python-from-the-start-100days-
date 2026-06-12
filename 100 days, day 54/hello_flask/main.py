"""from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)


@app.route('/')                  ## / is the homepage
def hello_world():
    return 'Hello world'

if __name__ == "__main__":
    app.run()
"""














## 392


"""
## Functions can be returned from other functions

def outer_function():
    print("im outer")

    def inner_function():
        print("im inner")

    return inner_function

inner_function = outer_function()
inner_function()

##mimics inner"""













## 393 Decorator function

#basically they are wrappers
"""
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    time.sleep(2)
    print("Hello")

#adding the same thing to multiple functions
@delay_decorator
def say_bye():
    print("bye")

def say_greeting():
    print("stfup")


## just like delay it can do multiple things such as delay by 2secs and also iterate for each and every decorator use from parent decorator function


decorated_function=delay_decorator(say_greeting)
decorated_function()"""


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/bye")
def say_bye():
    return "BYE"
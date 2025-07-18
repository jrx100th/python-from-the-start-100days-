def add(*args):
    print(sum(args))

# add(3,5,4,7,8)

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
# kwargs is a dictionary of the remainder arguments


class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        # .get(item_name) is similar to using square brackets for getting the value in dictionary
        # benefits of using .get is it wont give an not found error like square bracket, instead it will return None
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")    # so even if one of this is not available it will crash
print(my_car.model) # returns none
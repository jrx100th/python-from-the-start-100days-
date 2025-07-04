
"""

class inheritance

process of behaviour and appearance from existing class

inheritance

class Fish(parent_class_name):
    def __init__(self):
        super().__init__()# refers to super class
            # initialize everything that our superclass can do in our fish class


"""

# real code

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    # now fish class can inherit everything that animal class can do/have
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()

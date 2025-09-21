class Animal:
    def __init__(self,name):
        pass

class Human:
    def __init__(self,name,age):
        pass

class Robots(Human,Animal):
    name3 = "charli123"

obj = Robots()
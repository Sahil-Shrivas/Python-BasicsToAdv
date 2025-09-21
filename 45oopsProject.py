class Animal:
    name = "lion" #class attribute
    
    def __init__(self,age):
        self.age = age #instance attribute
    
    def show(self):  #instance method
        print(f"how are you your agger is {self.age}")
    
    @classmethod
    def hello(cls):
        print(f"how are you brother {cls.age}")

    @staticmethod
    def static():
        print("how are you")

    obj = Animal(12)

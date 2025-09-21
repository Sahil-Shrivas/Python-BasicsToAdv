class Animal:
    def show(self):
        print("hello I am akarsh")
    


class Human(Animal):
    def show(self):
        print("how are you")

obj = Human()
obj.show()
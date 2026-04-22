class Animal:
    def __init__(self):
        print("Hello From Animal Class")

    def speak(self):
        print("Animal makes sound")


class Dog(Animal):
    def __init__(self):
        super().__init__()   # correct place

    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def __init__(self):
        super().__init__()   # correct place

    def speak(self):
        print("Cat meows")


dog1 = Dog()
dog1.speak()
from Animals import Animals


class Dog(Animals):
    def __init__(self, bark):
        self.bark = bark

    def eat(self):
        print("The dog is eating")

    def sleep(self):
        print("The dog is sleeping")

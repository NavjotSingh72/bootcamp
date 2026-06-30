class Animal:                         # Parent / Base class
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):                    # Child / Derived class
    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # Call parent __init__
        self.breed = breed

    def fetch(self):                                #new method added in child
        return f"{self.name} fetches the ball!"


d = Dog("Bruno", "Golden Retriever")

print(d.speak())
print(d.fetch())
print(d)
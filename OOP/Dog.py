class Dog():

    # Define the dog
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof woof!")

# Instantiate a dog object
spot = Dog("spot", 2)

spot.bark()

print(spot.name)
print(spot.age)



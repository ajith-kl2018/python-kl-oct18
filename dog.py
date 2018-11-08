# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name="Doggy", age=10):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def testStatic():
        print ("Hey , I am static")

    testStatic = staticmethod(testStatic)


#Static method
Dog.testStatic()


#Instance of a class
john = Dog("John", 25)
print(john.description())
john.testStatic()

#Instance of a class 
kim = Dog(name="Kim")
print(kim.description())

#Instance of a class
doggy = Dog()
print(doggy.description())

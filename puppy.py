class Puppy:
    
    name =""
    color=""

    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def bark(self) :
        print ("I am", self.color, self.name)

    def __str__(self):
        ret = "Puppy Object\n"
        ret += "name:" + self.name + "\n"
        return ret


puppy1 = Puppy("Max", "brown")
puppy1.bark() 

puppy2 = Puppy("Ruby", "black")
puppy2.bark()

print (dir(puppy2))

print(puppy2)




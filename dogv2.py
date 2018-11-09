class DogV2:
    species = 'mammal'
    name =""
    age =0
    def __init__(self,name,age):
        self.name =name
        self.age = age

jake = DogV2("Jake",7)
doug = DogV2("Doug",8)
william = DogV2("William",10)

def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(get_biggest_number(jake.age,doug.age,william.age)))

print(jake.species)



    
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Dogs(Animal):
    
    def __init__(self, color,breed):
        self.color=color
        self.breed=breed
    def dog_info(self):
        print(self.name+" is a "+self.color+" "+self.breed)
    def bark(self):
        print("Wof Wof Woff Woff!")
class Cats(Animal):
    def __init__(self,inoculated):
        self.inoculated=inoculated
    def get_info(self):
        if self.inoculated==True:
            print(self.name+" has inoculated")
        else:
            print(self.name+" has not inoculated")

    def meow(self):
        print("Meoow Meooow!")

myCat=Cats(True)
myCat.age=3
myCat.name="Miyav"
myCat.get_info()
myCat.meow()
myDog=Dogs("Black","Kangal")
myDog.age=5
myDog.name="Yumak"
myDog.dog_info()
myDog.bark()
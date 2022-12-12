import datetime
today = datetime.datetime.now()
hour = today.hour
sunrise = 7
sunset = 21
#hour = 3


class Utility:
    def isDay(self, hour):
        if hour >= sunrise and hour <= sunset:
            return True
        else:
            return False

class Sun(Utility):
    def light(self, hour):
        if Utility.isDay(self, hour):
            print("The Sun is shining")
        else:
            print("The night has come")

class Tree(Utility):
    def photosynthesys(self, hour):
        if Utility.isDay(self, hour):
            print("The tree produces some fresh air")
        else:
            print("The tree is waiting for dark times to end")

class Grass:
    def grow(self, hour):
        if Utility.isDay(self, hour):
            print("The green grass grows")
        else:
            print("The grass stopped growing")

class Air:
    def exist(self, hour):
        if Utility.isDay(self, hour):
            print("There's enough air to breath")
        else:
            print("No fresh air is being produced")

class Frog:
    def __init__(self, name):
        self.name = name
    def sleep(self, hour):
        if Utility.isDay(self, hour):
            print(self.name + " is awake")
        else:
            print(self.name + " is sleeping, tsss")

    def breath(self, hour):
        if Utility.isDay(self, hour):
            print(self.name + " breathes")

    def eat(self, hour):
        if Utility.isDay(self, hour):
            print(self.name + " eats fresh grass")

    def move(self, hour):
        if Utility.isDay(self, hour):
            print(self.name + " travels across the Froggyland")


theSun = Sun()
oak = Tree()
greenGrass = Grass()
freshAir = Air()
froggy = Frog("Froggy")

print("Let's see what happens in Froggyland at this hour")

theSun.light(hour)
froggy.sleep(hour)
oak.photosynthesys(hour)
freshAir.exist(hour)
froggy.breath(hour)
greenGrass.grow(hour)
froggy.eat(hour)
froggy.move(hour)

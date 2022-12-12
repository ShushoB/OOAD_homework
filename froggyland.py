import datetime
today = datetime.datetime.now()
hour = today.hour
sunrise = 7
sunset = 21
#hour = 3

class Sun:
    def light(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("The Sun is shining")
        else:
            print("The night has come")

class Tree:
    def photosynthesys(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("The tree produces some fresh air")
        else:
            print("The tree is waiting for dark times to end")

class Grass:
    def grow(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("The green grass grows")
        else:
            print("The grass stopped growing")

class Air:
    def exist(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("There's enough air to breath")
        else:
            print("No fresh air is being produced")

class Frog:
    def sleep(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("The frog is awake")
        else:
            print("The frog is sleeping, tsss")

    def breath(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("The frog breathes")

    def eat(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("The frog eats fresh grass")

    def move(self, hour):
        if hour >= sunrise and hour <= sunset:
            print("The frog travels across the Froggyland")


theSun = Sun()
oak = Tree()
greenGrass = Grass()
freshAir = Air()
froggy = Frog()

print("Let's see what happens in Froggyland at this hour")

theSun.light(hour)
froggy.sleep(hour)
oak.photosynthesys(hour)
freshAir.exist(hour)
froggy.breath(hour)
greenGrass.grow(hour)
froggy.eat(hour)
froggy.move(hour)

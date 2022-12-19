class Dog:
    def __init__(self, name, breed, gender, age):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age

    def dogid(self, name, breed, gender, age):
        print(self.name + "'s breed is: " + self.breed + ", the gender is: " + self.gender + ", and it's " + self.age + " years old")

    def dog_run(self):
        print(self.name + " is running")

    def dog_bark(self):
        print(self.name + " says Wooof!")

    def dog_sleep(self):
        print(self.name + " is sleeping")

    def dog_eat(self):
        print(self.name + " is eating")

mydog = Dog("Betty", "Labrador Retriever", "female", "2")
mydog.dogid("Betty", "Labrador Retriever", "female", "2")
mydog.dog_bark()
mydog.dog_eat()
mydog.dog_run()

print()

class Helicopter:
    def __init__(self, name, max_height, max_speed, national_origin, color):
        self.name = name
        self.max_height = max_height
        self.max_speed = max_speed
        self.national_origin = national_origin
        self.color = color

    def helicopter_id(self, name, max_height, max_speed, national_origin, color):
        print(self.name + " can raise to the maximum height of " + self.max_height + " meters and gain maximum speed of " + self.max_speed + " km/h. It comes from " + self.national_origin + " it's color is: " + self.color)
    def helicopter_takeoff(self):
        print(self.name + " is taking off")
    def helicopter_landing(self):
        print(self.name + " is laneding")

myhelicopter = Helicopter("Bell 206", "60000", "250", "USA", "camouflage" )
myhelicopter.helicopter_id("Bell 206", "60000", "250", "USA", "camouflage" )   
myhelicopter.helicopter_takeoff()
myhelicopter.helicopter_landing()

print()

class Hospital:
    def __init__(self, name, nb_doctors, nb_nurses, nb_adminitrative_stuff, floors, operating_rooms, hospital_chambers, ambulance_cars):
        self.name = name
        self.nb_doctors = nb_doctors
        self.nb_nurses = nb_nurses
        self.nb_adminitrative_stuff = nb_adminitrative_stuff
        self.floors = floors
        self.operating_rooms = operating_rooms
        self.hospital_chambers = hospital_chambers
        self.ambulance_cars = ambulance_cars

    def hospital_id(self, name, nb_doctors, nb_nurses, nb_adminitrative_stuff, floors, operating_rooms, hospital_chambers, ambulance_cars):
        print(self.name + " hostpital has " + self.nb_doctors + " qualified doctors, " + self.nb_nurses + " nurses and " + self.nb_adminitrative_stuff + " administrative workers. The hospital has " + self.floors + " floors with " + self.operating_rooms + " fully-equipped operating rooms and " + self.hospital_chambers + " chambers in total. The hospital can accept " + self.ambulance_cars + " ambulance brigades at once.")
    def hospital_emergency(self):
        print("Attention, an ambulance car is arriving at " + self.name)

myhospital = Hospital("Yerevan Medical Complex", "40", "250", "50", "4", "20", "160", "10")
myhospital.hospital_id("Yerevan Medical Complex", "40", "250", "50", "4", "20", "160", "10")
myhospital.hospital_emergency()

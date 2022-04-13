class Vehicle:
    def __init__(self, number_of_wheels, type_of_tanks, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tanks = type_of_tanks
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    def drive(self):
        if (self.number_of_wheels == '4'):
            print("The vehicle is on driving mode now.")
        else:
            print("The vehicle is not on drving mode now.")
            

vios = Vehicle('4','petrol',5,180)
bmw = Vehicle('6','diesel',10,120)

print("Vios number of wheels = " + vios.number_of_wheels)
print("bmw.number of wheels = " + bmw.number_of_wheels)

print("vios type of tank = " + vios.type_of_tanks)
print("bmw type of tank = " + bmw.type_of_tanks)

print("vios seating capacity = " + str(vios.seating_capacity))
print("bmw seating capacity = " + str(bmw.seating_capacity))

print("vios maximum velocity = " + str(vios.maximum_velocity))
print("bmw maximum velocity = " + str(bmw.maximum_velocity))

vios.drive()
bmw.drive()

class Computer:
    def __init__(self, cpu, type_of_ram, hard_disk, name_of_game):
        self.cpu = cpu
        self.type_of_ram = type_of_ram
        self.hard_disk = hard_disk
        self.name_of_game = name_of_game

    def playGame(self):
         print("The computer is power on now and running", self.name_of_game,"game")
         
class Laptop(Computer):
    def __init__(self, cpu, hard_disk, name_of_game):
        Computer.__init__(self, cpu, "SODIMM", hard_disk, name_of_game)

class Desktop(Computer):
    def __init__(self, cpu, hard_disk, name_of_game):
        Computer.__init__(self, cpu, "DIMM", hard_disk, name_of_game)

acer = Laptop('i7','500','Minecraft')
acer.playGame()
print("Using " + acer.type_of_ram)

hp = Desktop('i9','1000',"LOL")
hp.playGame()
print("Using " + hp.type_of_ram)

        

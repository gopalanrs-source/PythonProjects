class Vehicle:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

    def moves(self):
        print("The vehicle moves")

    def get_car_dtl(self):
        print(f"I'm a {self.year} made {self.make}'s {self.model}")

my_car = Vehicle("Toyota", "Corolla", 2020)

my_car.moves()
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.get_car_dtl()

my_new_car = Vehicle("Hyundai", "Creta", 2025)
my_new_car.get_car_dtl()
my_new_car.moves()


print('\n\n')

class Airplane(Vehicle):
    def __init__(self, make, model, year,FAA_id):
        super().__init__(make, model, year)
        self.FAA_id = FAA_id
    
    def moves(self):
        print("The airplane flies")

class Boat(Vehicle):
    def moves(self):
        print("The boat sails")

class Motorcycle(Vehicle):
    pass

cessna = Airplane("Cessna", "172", 2018, "N12345")
cessna.get_car_dtl()
print(cessna.FAA_id)
cessna.moves()

yacht = Boat("Sunseeker", "Predator", 2021)
yacht.get_car_dtl()
yacht.moves()

twowheeler = Motorcycle("Honda", "CBR500R", 2019)
twowheeler.get_car_dtl()
twowheeler.moves()

#polymorphism
print('\n\n')
for v in (my_car, cessna, yacht, twowheeler):
    v.get_car_dtl()
    v.moves()






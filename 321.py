# Problema: Vehicule

# Creează o ierarhie de clase pentru vehicule:

# Clasa de bază Vehicle
# Atribute: brand, year
# Metodă: get_info() → afișează Brand: ..., Year: ...
# Subclase:
# Car
# Adaugă atribut: seats 
# Suprascrie get_info() ca să afișeze și numărul de locuri
# Bike
# Adaugă atribut: type (ex: mountain, road)
# Suprascrie get_info() ca să afișeze și tipul bicicletei

# Truck
# Adaugă atribut: load_capacity
# Suprascrie get_info() ca să afișeze și capacitatea de încărcare
# Cerințe polimorfism:
# Creează o listă cu diferite obiecte Car, Bike, Truck
# Parcurge lista și apelează get_info() pentru fiecare obiect, fără să te uiți la tipul lui concret


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        print(f"Brand: {self.brand}. Year: {self.year}")

class Car(Vehicle):
    
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

    def get_info(self):
        print(f"Brand: {self.brand}. Year: {self.year}. Seats: {self.seats}.")
class Bike(Vehicle):



   
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type
        

    def get_info(self):
        
        
        # while True:  
        #     self.type = input("Scrie tipul bicicletei (mountain bmx road electric):")  
        #     if self.type in ["bmx", "mountain", "road", "electric"]:
        #         break
        #     else:
        #         print("Scrie un tip de bicicleta din lista!\n")
        
        print(f"{self.brand}, {self.year}, {self.type}")

class Truck(Vehicle):
    def __init__(self, load_capacity, brand, year):
        super().__init__(brand, year)
        self.load_capacity = load_capacity

    def get_info(self):
        return print(f"Capacitatea incarcare: {self.load_capacity}", end=" "), super().get_info(), 


bicicleta1 = Bike("Oreol", 2025, "Bmx")
# bicicleta1.get_info()

masina1 = Car("Audi", 2022, 5)
# print(masina1.get_info())

camion1 = Truck("3 tone", "Volvo", 2015)
# camion1.get_info()

lista_v = [bicicleta1, masina1, camion1]

for i in lista_v:
    i.get_info()


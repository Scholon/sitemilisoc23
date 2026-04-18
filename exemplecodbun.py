# ___________________________________________________
# LUCRU CU CLASELE SI SUBCLASELE

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



# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

#     def get_info(self):
#         print(f"Brand: {self.brand}. Year: {self.year}")

# class Car(Vehicle):
    
#     def __init__(self, brand, year, seats):
#         super().__init__(brand, year)
#         self.seats = seats

#     def get_info(self):
#         print(f"Brand: {self.brand}. Year: {self.year}. Seats: {self.seats}.")
# class Bike(Vehicle):



   
#     def __init__(self, brand, year, type):
#         super().__init__(brand, year)
#         self.type = type
        

#     def get_info(self):
        
        
#         # while True:  
#         #     self.type = input("Scrie tipul bicicletei (mountain bmx road electric):")  
#         #     if self.type in ["bmx", "mountain", "road", "electric"]:
#         #         break
#         #     else:
#         #         print("Scrie un tip de bicicleta din lista!\n")
        
#         print(f"{self.brand}, {self.year}, {self.type}")

# class Truck(Vehicle):
#     def __init__(self, load_capacity, brand, year):
#         super().__init__(brand, year)
#         self.load_capacity = load_capacity

#     def get_info(self):
#         return print(f"Capacitatea incarcare: {self.load_capacity}", end=" "), super().get_info(), 


# bicicleta1 = Bike("Oreol", 2025, "Bmx")
# # bicicleta1.get_info()

# masina1 = Car("Audi", 2022, 5)
# # print(masina1.get_info())

# camion1 = Truck("3 tone", "Volvo", 2015)
# # camion1.get_info()

# lista_v = [bicicleta1, masina1, camion1]

# for i in lista_v:
#     i.get_info()

# ___________________________________________________
# # ENUMERAREA TEMELOR (DESPARTITE PRINTRUN SIMBOL) SI DESPARTIREA LOR DACA AU SPATII INTRE ELE

# lista_teme = """
# • Colonizarea greacă
# • Civilizaţia Romană*
# • Geto-dacii şi lumea greacă*
# • Modele de organizare politică în Grecia antică
# • Imperiul lui Alexandru Macedon. Elenismul
# • Forme de organizare politico-statală în Roma antică
# • Dacia pe timpul lui Burebista
# • Fărâmiţarea statului dac şi refacerea unităţii lui pe timpul lui
# Decebal*
# • Dacia şi Imperiu Roman: războaiele daco-romane; romanizarea
# geto-dacilor
# • Organizarea socială la geto-daci*
# • Traco-geto-dacii în viziunea autorilor antici*
# • Cultura şi religia geto-dacilor
# • Criza societăţii antice şi formele ei de manifestare
# • Marile migraţiuni şi declinul lumii antice. Căderea Imperiului
# Roman de Apus"""



# lista_noua = lista_teme.split("•")                              # SA SE DESPARTA DACA ARE SIMBOLUL "•"

# lista_noua = [i.strip() for i in lista_noua if i.strip()]       # DACA ARE SPATII PRIN PARTI SAU "\n" SA SCOATA SPATIILE

# lista_noua = [x for x in lista_noua if "*" not in x]            # DACA ARE UN SIMBOL ANUMIT, SA NU INCLUDA ACEL ELEMENT

# for x in lista_noua:                                            
#     if "*" not in x:                                            # DACA ARE UN SIMBOL ANUMIT, SA NU INCLUDA ACEL ELEMENT
#         noua_lista.append(x)


# for i,teme in enumerate(lista_noua, start=1):                   # SA ENUMERE TOATE TEMELE
#     print(i,teme)
# ___________________________________________________
# VERIFICAREA ALARMEI (TARZIU / DEVREME / LA TIMP)

# from datetime import timedelta, datetime


# def v_alarma(timp_trez: str, timp_alarma: str):
#     
#     timp_trez = datetime.strptime(timp_trez, "%H:%M")
#     timp_alarma = datetime.strptime(timp_alarma, "%H:%M")    
    
#     if timp_trez > timp_alarma + timedelta(minutes = 10):
#         print("Te-ai trezit tarziu!")
    
#     elif timp_trez < timp_alarma:
#         timp_ramas = timp_alarma - timp_trez

#         print("Teai trezit devreme! Mai ai: ", timp_ramas)
#     else:
#         print("Te-ai trezit la timp!")


# v_alarma("05:05", "06:00")
# ___________________________________________________
# GHICIRE DE NUMAR
# import random

# n_random = random.randint(1,100)

# print(n_random)

# while True:
#     cifra = int(input("Cifra: "))
#     if cifra > n_random + 5:
#         print("Cifra prea mare!")
#     elif cifra < n_random - 5:
#         print("Cifra este prea mica!")
#     elif n_random < cifra < n_random + 5:
#         print("Fierbinte! (cifra >)")
#     elif n_random - 5 < cifra < n_random:
#         print("Fierbinte! (cifra <)")
#     elif cifra == n_random:
#         print("Corect!")
#         break
# ___________________________________________________
litera_user = input("Scrie litera")
raspuns = "cuvant random"

for litera in range(len(raspuns)):
    if raspuns[litera] == litera_user:
        print(litera)
    

# raspuns = [litera for sublista in cuv_random for litera in sublista]      PENTRU A SCOATE O LISTA DE SUB ALTA LISTA

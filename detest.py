# _________________________________________________
# SIMPLIFICARE IF 1
# 
# bogat = True
# casamare = True
# eligibil = True if bogat and not casamare else False
# # print(eligibil)
# ___________________________________________________
# SIMPLIFICARE IF 2
# 
# varsta = 22
# pensie = False if 18 <= varsta <= 65 else True
# ___________________________________________________
# FOR LOOP CU RANGE 

# numar = 2
# for numar in range(1, 4, 2): (1,4 - range, 2 - peste cate sa paseasca(step))
#     print("Numarul se repeta de:", numar + 3, "ori.")
# ___________________________________________________
# PAROLA CU HASH

# parola = "sandu"
# hash = "".join(chr(ord(H)+10) for H in parola)
# parola_user = "".join(chr(ord(H)+10) for H in hash)
# print("Scrie parola. Ai 3 incercari:")
      
# while incercari >= 0:
#     input_user = input("")
#     hash_user = "".join(chr(ord(H)+10) for H in input_user)
#     if hash_user == hash:
#         print("Parola corecta!")
#         break;
#     elif hash_user == hash:
#         print("De unde ai Hash-ul?")
#     elif hash_user != hash:
#         print("\nParola incorecta! Mai ai", incercari, "incercari!")
#         incercari -= 1
#         print("Hash-ul tau:", hash_user, "\nHash-ul care trebuie:", hash )
#     if incercari == -1:
#         print("\nNu mai aveti incercari!")
#         print("Hash-ul tau:", hash_user, "Hash-ul care trebuie:", hash )
# ___________________________________________________
 #NESTED LOOP + FORMATTED STRING LITERAL

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")
# ___________________________________________________
# CUM SA GASESTI UN CARACTER INTR-UN TYPE
# caracteruldorit = "B"
# lista1 = (str(type(caracteruldorit)))
# start = 8
# stop = lista1.find('\'>')
# print(lista1)
# print(lista1[start:stop])
 # ___________________________________________________
# TIPURI DE OUTPUT CU LISTE

# shopping_cart = ["oua", "cartofi", "paste"]
# lista2 = "oua"
# list1 = ["oua","cartofi"]

# for item in shopping_cart:
#     print(item)

# print(shopping_cart)

# for item in lista2:
#     print(item)
# ___________________________________________________
# CUM SA FACI UN CMD (INTERESANT) !!!!
# command = ""
# while command.lower != "quit":
#     command = input(">")
#     print("ECHO", command) 
# ___________________________________________________
# VERIFICARE DACA E PAR

# lista = list(range(1,9))
# print(lista)
# countpar = 0
# for numar in lista:
#     if numar % 2 == 0: 
#        print(numar)
#        countpar += 1
# print(f"We have {countpar} even numbers")
# ___________________________________________________
# CUM SA FACI O FUNCTIE

# def salutare(prenume, nume):
#     print(f"Bun venit {prenume} {nume}!")
#     print("Va salutam cu drag!")

# salutare('Sandu', 'Osipov')
# salutare("John", "Smith")
# ___________________________________________________
# DICTIONARE
# 1.
# country = {'codul' : 'MD', 'nume' : 'Moldova', 'Populatia' : 2.2, 'Mare' : False}
# print(country['nume'])

# 2. 
# sandu = dict(prenume="Sandu",nume="Osipov",varsta="18",inaltime="175")
# print(sandu["nume"])

# for key, value in sandu.items():
#     print(key, "-", value)

# sandu.pop('nume') #sterge un element
# print(country.values()) #arata doar raspunsurile la coduri
# print(country.keys()) #arata dora codurile
# sandu ["prenume"] = "Alexandru" #schimba codul

# oameni = {
#     "sandu" :{
#         "nume" : "Osipov",
#         "prenumee" : "Sandu",
#         "varsta" : 18,
#         "originea" : "Moldova"
#     },
    
#     "Alexandru" : {
#         "nume" : "Popescu",
#         "prenume" : "Alexandru",
#         "varsta" : 20,
#         "originea" : "Moldova"
#     }
    
     
# }   

# print(oameni["sandu"]["originea"])
# ___________________________________________________
# MULTIMI (NU SE REPETA ELEMENTELE SI SUNT RANDOM)
# data = set("sandu")

# data.add(32) #adauga nou element
# data.update(['32', True, 4, 6]) #adauga mai multe elemente
# data.remove(True) #sterge un element
# data.pop() #sterge primul element
# data.clear() #sterge toate elementele

# new_data = frozenset({32, True, 4, 'd', 'u', 6, 'a', 'n', 's', '32'}) #nu se poate adauga nimic in el (se foloseste in dictionare)
# print(new_data)
# ___________________________________________________
# FUNCTII CU LAMBDA
# nume = input("Scrie numele tau:")
# lambda nume: print(f"Bun venit {nume}") 
# ___________________________________________________
# file = open('C:/projects/python/text.txt', 'w')

# file.write('Hello')

# file.close()


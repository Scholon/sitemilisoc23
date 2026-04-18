import random

lista_cuvinte = "mere, calculator, telefon, mouse, noapte, drum, muzica, masina, copii, soare, apele, munte, drum, oras, floare, visare, norilor, campul, lemnul, vanturi, focuri, piatra, noaptea, lunara, steaua, gradina, padure"

cuv_random = list(random.choice(lista_cuvinte.split(",")).strip())

raspuns = [litera for sublista in cuv_random for litera in sublista]

litera_asc = ["_" for _ in raspuns]

litera_asc2 = [litera for sublista in litera_asc for litera in sublista]



pozitia = []
progres = ""
sanse = len(cuv_random) + 2

print("Cuvantul:", cuv_random)
print("Sanse:", sanse)
print("Literele:", " ".join(litera_asc))

while True:
    litera_user = input("Scrie litera")
    cuv_ascuns = raspuns
    
    if litera_user in cuv_ascuns:
        for litera in range(len(cuv_ascuns)):
            if cuv_ascuns[litera] == litera_user:
                # print(litera)
                pozitia.append(cuv_ascuns[litera])
                print(pozitia)
                print(pozitia[-1])

                print(progres)
                


                
                # litera_asc[litera].replace([0], pozitia[-1])
                # print(litera_asc)
                # print(litera)
                
                
                # progres = 
                # print(f"Ai ghicit o litera! Progresul = {cuv_ascuns[litera]}")
                # print("Progresul =", progres)
            
               
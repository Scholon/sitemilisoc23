import random

lista_cuvinte = "mister, valuri, taina, frumos, linie, focuri, umbre, visuri, clipe, izvor, magie, codru, zbori, sange, munca, gand, pasari, cetate, izvoare, flori"
cuv_random = list(random.choice(lista_cuvinte.split(",")).strip())
raspuns = [litera for sublista in cuv_random for litera in sublista]
cenzura = ["_" for n in raspuns]
cuvant_nou=""
hangman = {0: """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |""",
1: """
=========
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
2: """
=========
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
3: """
=========
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
4: """
=========
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
5: """
=========
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
6: """
=========
  +---+
  |   |
      |
      |
      |
      |
=========
""",
7: """

=========
  +---+
      |
      |
      |
      |
      |
=========

""",
8: """
=========
    O   - SALVEAZA-MA!
   /|\  
   / \\
=========

"""

}
litere_ghicite = dict(lit_ghicite = [])
cuvant_cenzurat = dict(cuv_ascuns = cenzura)
dict_raspuns = dict(rasp = raspuns)
info = dict(
    mister = "ceva necunoscut sau greu de înțeles",
    valuri = "succesiune de creste și văi ale apei",
    taina = "ceva ascuns, secret sau misterios",
    frumos = "plăcut vizual sau sufletește",
    linie = "șir de puncte sau marcaje aliniate",
    focuri = "manifestări vizibile ale arderii",
    umbre = "zone întunecate create de lipsa luminii",
    visuri = "imaginații sau dorințe în timpul somnului",
    clipe = "unități scurte de timp, momente",
    izvor = "loc de unde izvorăște apa",
    magie = "acțiuni sau fenomene supranaturale",
    codru = "pădure mare și densă",
    zbori = "acțiunea de a te deplasa prin aer",
    sange = "lichid roșu care circulă în corp",
    munca = "efort depus pentru a obține ceva",
    gand = "proces mental de reflecție sau idee",
    pasari = "animale vertebrate care au pene și pot zbura",
    cetate = "oraș fortificat sau construcție defensivă",
    izvoare = "mai multe locuri de unde izvorăște apa",
    flori = "reprezentanți ai plantelor cu flori, decorative"
)
for litera in raspuns:
        cuvant_nou += "".join(str(litera)) 

def main_menu():
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    BUN VENIT LA HANGMAN!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
         
        • AI (LUNGIMEA CUVANTULUI) + 2 INCERCARI        =========
                                                          +---+   
        • GHICESTE CUVANTUL PENTRU A CASTIGA              |   |
                                                              |
                                                              |
                                                              |
                                                              |
                                                        =========
        
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    PENTRU A INCEPE SCRIE: START   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
          """)
    start = input("> ")
    
    if start.lower() == "start":
        main_joc()
def main_joc():
    print(f"""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   INDICIU: {info[cuvant_nou]}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""")
    sanse = 9
    
    while True:
        
        litera_user = input(f"Mai ai {sanse} incercari. Scrie litera: ")
        if litera_user in dict_raspuns["rasp"]:
            for i in range(len(dict_raspuns["rasp"])):
                if dict_raspuns["rasp"][i] == litera_user:
                    litere_ghicite["lit_ghicite"].append(dict_raspuns["rasp"][i])
                    # print(litere_ghicite["lit_ghicite"])
                    cuvant_cenzurat["cuv_ascuns"][i] = litera_user
                    
               
                    print(f"""
                    ========================================================================================================
                                                    Ai ghicit litera {dict_raspuns['rasp'][i]}                              
                                                    PROGRESUL: {cuvant_cenzurat["cuv_ascuns"]} 
                    ========================================================================================================
        """)
                    sanse -= 1 
      

        if litera_user not in dict_raspuns["rasp"]:
            sanse -= 1
            print(f"""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   LITERA "{litera_user}" NU EXISTA IN CUVANT!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                   {hangman[sanse]}""")
        if cuvant_cenzurat["cuv_ascuns"] == dict_raspuns["rasp"]:
            main_castig()
            
        if sanse == 0:
            main_lose()
            break
def main_lose():
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   AI PIERDUT!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                             =========
                                                                +---+
                                                                |   |
                                                                O   |
                                                               /|\  |
                                                               / \  |
                                                                    |                                                     
                                                             =========
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    PENTRU A INCEPE DIN NOU SCRIE: START   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""")
    user_input_lose = input(">")
    if user_input_lose.lower() == "start":
        main_joc()
def main_castig():
    print(f"""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   BRAVO! L-AI SALVAT PE BULA!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                         =========
                                                            +---+
                                                            |   |
                                             MERSI! <------ O   |
                                                           /|\  |
                                                           / \  |
                                                                |                                                     
                                                         =========
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    PENTRU A JUCA IAR SCRIE: START   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""")  
    user_input = input("> ")
    if user_input.lower() == "start":
        main_joc()

main_menu()
import random
lista_cuvinte = "mister, valuri, taina, frumos, linie, focuri, umbre, visuri, clipe, izvor, magie, codru, zbori, sange, munca, gand, pasari, cetate, izvoare, flori"
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
def generare():
    cuv_random = list(random.choice(lista_cuvinte.split(",")).strip())
    raspuns = [litera for sublista in cuv_random for litera in sublista]
    cenzura = ["_" for n in raspuns]    
    cuvant_nou=""
    litere_ghicite = dict(lit_ghicite = [])
    toate_literele = []
    cuvant_cenzurat = dict(cuv_ascuns = cenzura)
    dict_raspuns = dict(rasp = raspuns)
    for litera in raspuns:
        cuvant_nou += "".join(str(litera)) 
    return hangman, litere_ghicite, cuvant_cenzurat, dict_raspuns,info,cuvant_nou,toate_literele
def main_menu():
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    BUN VENIT LA HANGMAN!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
         
        • AI 9 INCERCARI                                 =========
                                                            +---+   
        • GHICESTE CUVANTUL PENTRU A CASTIGA                |   |
                                                                |
                                                                |
                                                                |
                                                                |
                                                          =========
        
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    PENTRU A INCEPE SCRIE: START   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
          """)
    while True:    
        start = input("> ")
        if start.lower() == "start":
            main_joc()
        else:
            print("""        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  SCRIE \"START\" PENTRU A INCEPE!  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")
            continue
def main_joc():
    hangman, litere_ghicite, cuvant_cenzurat, dict_raspuns,info,cuvant_nou,toate_literele = generare()
    print(f"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   INDICIU: {info[cuvant_nou]}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""")
    sanse = 9
    
    while True:
        litera_user = input(f"Mai ai {sanse} incercari. Scrie litera: ")
        toate_literele.append(litera_user)
        if toate_literele.count(litera_user) != 1:
            print(f"""        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  AI SCRIS DEJA LITERA {litera_user}!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< """)
            continue
        if len(litera_user) > 1 or not litera_user.isalpha():
            print(f"""        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  SCRIE DOAR O LITERA!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< """)
            continue
       
        if litera_user in dict_raspuns["rasp"] and len(litera_user) == 1:
            for i in range(len(dict_raspuns["rasp"])):
                if dict_raspuns["rasp"][i] == litera_user:
                    litere_ghicite["lit_ghicite"].append(dict_raspuns["rasp"][i])
                    cuvant_cenzurat["cuv_ascuns"][i] = litera_user
                    if litera_user in litere_ghicite["lit_ghicite"]:
                        print(f"""
                    ========================================================================================================
                                                    Ai ghicit litera {dict_raspuns['rasp'][i]}                              
                                                    PROGRESUL: {cuvant_cenzurat["cuv_ascuns"]} 
                    ========================================================================================================

                                                                
        """)
                        sanse -= 1 
       
        if litera_user not in dict_raspuns["rasp"] and len(litera_user) == 1:
            sanse -= 1
            print(f"""
                ========================================================================================================
                                            LITERA "{litera_user}" NU EXISTA IN CUVANT!   

                                            INDICIU: {info[cuvant_nou]}  
                ========================================================================================================
                {hangman[sanse]}

        """)
        if cuvant_cenzurat["cuv_ascuns"] == dict_raspuns["rasp"]:
            main_castig()
            break
            
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
    
    while True:
        user_input_lose = input(">")
        if user_input_lose.lower() == "start":
            generare()
            main_joc()
        else:
            print("""        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  SCRIE \"START\" PENTRU A INCEPE!  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")
            continue
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
    
    while True:
        user_input = input("> ")
        if user_input.lower() == "start":
            main_joc()
        else:
            print("""        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  SCRIE \"START\" PENTRU A INCEPE!  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")
            continue
main_menu()



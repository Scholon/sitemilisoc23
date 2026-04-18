class Carte:
    def __init__(self):
        autor, titlu, disponibil = input("Scrie autorul, titlul si daca este disponibil (y/n), separate prin spațiu: ").split()
        self.titlu = titlu
        self.autor = autor
        self.disponibil = True if disponibil.lower() == "y" else False
        self.starea_cartii = input("Scrie starea cartii:")

    def imprumuta(self):
        if self.disponibil:
            self.disponibil = False
            return f"Ai împrumutat cartea {self.titlu}"
        else:
            return f"Cartea {self.titlu} nu este disponibilă"

    def returneaza(self):
        if not self.disponibil:
            self.disponibil = True
            return f"Ai returnat cartea {self.titlu}"
        else:
            return f"Cartea {self.titlu} nu era împrumutată"

    def afiseaza_info(self):
        stare = "Disponibilă" if self.disponibil else "Împrumutată"
        print(f"Titlu: {self.titlu}, Autor: {self.autor}, Starea cărții: {stare}, Info: {self.starea_cartii}")


# Test
carte1 = Carte()
carte1.afiseaza_info()
print(carte1.imprumuta())
print(carte1.afiseaza_info())
print(carte1.returneaza())
print(carte1.afiseaza_info())
class Student:
    def __init__(self, nume, nota):
        self.nume = nume
        self.nota = nota

    def este_promovat(self):
        if self.nota >= 5:
            return True
        else:
            return False

student1 = Student("Sandu", 2)
student2 = Student("Andrei", 2)

print(student1.nume, ":", "Promovat" if student1.este_promovat() else "Nepromovat")
print(student2.nume, ":", "Promovat" if student2.este_promovat() else "Nepromovat")
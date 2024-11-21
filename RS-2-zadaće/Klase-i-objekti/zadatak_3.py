class Student:
    ime = ""
    prezime = ""
    godine = 0
    ocjene = []

    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

    def __repr__(self):
        return f"Student(ime='{self.ime}', prezime='{self.prezime}', godine={self.godine}, ocjene={self.ocjene})"
    

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = []
najbolji_prosjek = 0

for student in studenti:
    novi_student = Student(student["ime"], student["prezime"], student["godine"], student["ocjene"])
    studenti_objekti.append(novi_student)

for student in studenti_objekti:
    student_prosjek = student.prosjek()
    print(f"{student.ime} {student.prezime} ima prosjek ocjena: {student_prosjek:.2f}")
    
    najbolji_prosjek, najbolji_student = (student_prosjek, student) if student_prosjek > najbolji_prosjek else (najbolji_prosjek, najbolji_student)

print(f"\nNajbolji student je: {najbolji_student.ime} {najbolji_student.prezime} sa prosjekom od {najbolji_prosjek:.2f}")

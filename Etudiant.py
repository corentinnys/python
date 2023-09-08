class Etudiant:
    def __init__(self, nom, note1, note2):
        self.nom = nom
        self.note1 = note1
        self.note2 = note2

    def calc_moy(self):
        return (self.note1 + self.note2) / 2

    def afficher(self):
        print("Etudiant: ", self.nom, " moyenne: ", self.calc_moy())


nom = input("Entrer le nom: ")
note1 = int(input("Entrer la note 1: "))
note2 = int(input("Entrer la note 2: "))
E = Etudiant(nom, note1, note2)
E.afficher()
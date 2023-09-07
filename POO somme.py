

class Somme:
    def __init__(self, nbr1=0, nbr2=0):
        self.n1 = nbr1
        self.n2 = nbr2

    def som(self):
        return n1 + n2

n1 = int(input("Entrer N1:"))
n2 = int(input("Entrer N1:"))
obj = Somme(n1,n2)
print("Le resultat de l'addition est :",obj.som())
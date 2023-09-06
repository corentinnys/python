

def calculate_TTC():
    reponse = input('quittez ?')
    while(reponse != '0'):

        price = int(input('entrer un prix ?'))
        TTC = price*(1 + (21/ 100))
        print(TTC)
        reponse = input('quittez ?')

calculate_TTC()
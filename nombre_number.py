import random
essaie = 5
numberAleatoire= round(random.random()*10)
responeUser =int(input("Entrer un chiffre"))
essaie-=1
while numberAleatoire!=responeUser and essaie!=0:
    responeUser = int(input("Entrer un chiffre"))
    if responeUser>numberAleatoire:
        print('plus bas')
    elif responeUser <numberAleatoire:
        print('plus haut')
    essaie -=1
    print(essaie)

if numberAleatoire!=responeUser and essaie==0:
    print(f'vous avez epuisez toutes vos essaies la reponse etais {numberAleatoire}')
else:
    print(f'vous avez trouver la reponse felicitaion {numberAleatoire}')
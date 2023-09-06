import math

def cone(rayon,hauteur):
    result =round(math.pi*(rayon**2)*hauteur)/3
    return result

print(cone(10,20))
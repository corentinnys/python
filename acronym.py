def acronym(str) :
    letter ="";
    arrayString =str.split(" ")
    for index,i in  enumerate(arrayString):
        letter+=i[0:1].capitalize()
    return letter

print(acronym(' Portable Network Graphics'))
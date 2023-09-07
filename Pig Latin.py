voyelles = ['a','e','i','o','u','y'];
consonnes = ["z",'r','t','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n'];


def Pig_Latin(word):
    result =''
    for items in voyelles:
        if items == word[0]:
           word = word+'ay'
           result =word
           break
    for items in consonnes:
        if items == word[0]:
            firstLetter = word[0]
            word =  word.strip(word[0])
            result=word+firstLetter+'ay'
            break
    return  result

print(Pig_Latin('alex'))
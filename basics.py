#1.Create a variable name that contain the value "Alan Turing"

name = "Alan Turing";


#2.Create a variable age  that contain the value 42

age = 42;


#3.Create a variable person that contains a list with the following values: name, age and "mathematician"

person =[name,age,"mathematician"];


#4. Create a variable text that contains "Hello, my name is Alan Turing, I am 42 years old and I am a mathematician." Use the format() method and the variable person to do this.

text = " Hello, my name is {}, I am {} years old and I am a mathematician.".format(name,age);
print(text)


# Create a variable age that contains value 32
age = 32

#Add 10 to variable age
age +=10;

#Create a variable textDiv that contains the character string "42 divided by 7 equals 6".
textDiv = "{} divided by 7 equals 6".format(age)
print(textDiv)
# Create a variable divAge and assign it the value of the age divided by 7

divAge = age/7
print(divAge)

#Create a variable restDiv that contains the rest of the variable age divided by 7

restDiv =age//7;


#Create a variable expDiv that contains the value of restDiv to the 3rd power

expDiv = restDiv**3


#Calculate the sum of all items and store it in a orderPrice variable
orderPrice =2*0.45 + 3*3.85+0.9+0.77+1,87


#Write a program that asks you to enter 2 values and displays the smallest of the 2 values
# nbe_one =input("Entrer un nombre")
# nbe_twoo =input("Entrer un nombre")
#
# if nbe_one >nbe_twoo:
#     print(nbe_twoo)
# else:
#     print(nbe_one)

#Write a script that asks you to enter 2 strings and displays the largest of the 2 strings (the one with the most characters).
# str_one =input("Entrer une phrase")
# str_two =input("Entrer une phrase")
#
# if len(str_one)> len(str_two):
#     print(str_one)
# else:
#     print(str_two)

#Display all students in the students list in alphabetical order.


students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]
# students.sort()
#
# for student in students:
#     print(student)

#Display only the names which begin with the letter "M".

# for student in students:
#
#     if student[0:1]=='M':
#         print(student)


#Display integers from 0 to 15 not included, using a for loop and the range() instruction.
# for i in range(15):
#     print(i)

#Create a for loop that displays integers from 1 to 10 included, but use the break instruction to interrupt it at 5.

# for i in range(15):
#     if i == 5:
#         break

# Create a for loop that displays integers from 1 to 10 included, but use the continue to modify its execution at 5.


for i in range(15):
    if i == 5:
        continue;

#Sort and display the list

list_of_numbers = [17, 38, 10, 25, 72]

# list_of_numbers.sort()
# print(list_of_numbers)
# for i in list_of_numbers:
#     print(i)

#Add item 12 to the list and display the list.
list_of_numbers.append(12);
# print(list_of_numbers)

#Reverse and display the list.
list_of_numbers.reverse()
print(list_of_numbers)

#Display the index of element 17.

for index,i in enumerate(list_of_numbers) :
    if i == 17:
        print(index)

#Remove item 38 and display the list

list_of_numbers.remove(38);
print(list_of_numbers);


#Display the sub-list of the 2nd to 3rd element
# secondElement = list_of_numbers[1:2]
# thirdElement = list_of_numbers[2:3]
# array =[];
# array.append(secondElement)
# array.append(thirdElement)
# print(array);


# Write an algorithm that:
#Asks the user to enter a number.
# numberArray =[];
# userNumber =int(input('entrer un nombre '))
#
# for i in range(userNumber):
#     numberArray.append(i)
# numberArray.reverse()
# print(numberArray);


#The price is right !

# numberAleatoire = 15
# def game():
#     userNumber =int(input("quel prix?"))
#     while userNumber != numberAleatoire :
#
#         if userNumber>numberAleatoire:
#             print("it's less")
#         else:
#             print("it s more")
#         userNumber =  int(input("quel prix?"));
#
# game()
#
#
# print("Well done , you won ")


#Display all students with the sentence "NAME is an alumni.

#
# all_students = [
#     ["David", "Justine", "Valentin", "Axel", "Redouane"],
#     ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"],
# ]
#
# for group in all_students:
#     for student in group:
#         print(f"{student} est un ancien eleve");
#

# Display all elements. If the element is part of the first list, display - "ELEMENT_HERE is a backend language?" - and if the element is part of the second list, display - "ELEMENT_HERE is a frontend language?"


languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]
elements_to_check = ["PHP", "Java", "C#", "HTML", "CSS", "Javascript", "Python"]

for element in elements_to_check:
    if element in languages[0]:
        print(f"{element} is a backend language?")
    elif element in languages[1]:
        print(f"{element} is a frontend language?")
    else:
        print(f"{element} is not in either list.")

#Drill functions

#1. Say Hello

# def hello(name=None):
#
#     if name  != None:
#         print(f"Hello {name} ")
#
#     else:
#         print("Hello Anonymous")
#
# hello('Corentin');
# hello();


#2. Count students


# def sum_of_students(students):
#     sum = 0;
#     for group in students:
#         sum+= len(group)
#     return sum;
#
#
#
# sum_of_students([["Jean", "Alice", "Edwige", "Peter", "James"],
#                ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]])


#3. Is divisible ?
# def is_divisible(n, x, y):
#   return n%x ==0 and n%y ==0 ;
#
# print(is_divisible(3, 1, 3))
# print(is_divisible(12, 2, 6))
# print(is_divisible(100, 5, 3))
# print(is_divisible(12, 7, 5))

#4. Abbreviate a two-word name

# def abbreviate_name(name):
#     words = name.split(' ');
#     firstLetter =words[0][0].capitalize()
#     lastLetter =words[1][0].capitalize()
#
#     return firstLetter+"."+lastLetter
# print(abbreviate_name("soazic nys"))



#5. Sum of positive


# def positive_sum(numbers):
#     sum = 0
#     for item in numbers:
#         if item >0:
#             sum+=item
#     return sum
# print(positive_sum([1,-4,7,12]))


#6. Sum mixed array

# def mixed_sum(array):
#     sum = 0;
#     for items in array:
#         sum+= int(items);
#     return sum;
#
# print(mixed_sum(['5', '0', 9, 3, 2, 1, '9', 6, 7]) )

#7. Return the day


# def get_weekday(number):
#     if number == 1:
#         return "Sunday"
#     elif number == 2:
#         return "Monday"
#     elif number == 3:
#         return "Tuesday"
#     elif number == 4:
#         return "Wednesday"
#     elif number == 5:
#         return "Thursday"
#     elif number == 6:
#         return "Friday"
#     elif number == 7:
#         return "Saturday"
#     else:
#         return "Wrong, please enter a number between 1 and 7"
#
# # Test the function
# number = int(input("Enter a number between 1 and 7: "))
# print(get_weekday(number))


#8. Summation


# def summation(number):
#     sum = 0
#     for i in range(1,number+1):
#         sum+=i;
#     return sum
#
# print(summation(8))

# def count_sheep(number):
#     numberOfSheep = ""
#     for i in range(1, number+1):
#         numberOfSheep +=(f"{i} moutons...")
#     return numberOfSheep
#
# print(count_sheep(8))



#10. Student's final grade



def final_grade(exam_grade, completed_projects):
    result = 0;
    if exam_grade>=90 or completed_projects>10 :
        result = 100
    elif  exam_grade>=75 and  completed_projects>=5:
        result = 90
    elif exam_grade>=50 and  completed_projects>=2:
        result = 75

    return result




print(final_grade(75, 10))
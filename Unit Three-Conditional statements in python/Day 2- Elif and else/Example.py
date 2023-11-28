# number_grade = 76

# if number_grade >=80:
#     print("A")
# if number_grade >=70:
#     print("B")
# if number_grade >=60:
#     print("C")
# if number_grade >=50:
#     print("D")
# if number_grade <=50:
#     print("F")

# prints B C D on seperate lines because three conditions were true 

# number_grade = 76

# if number_grade >=80:
#      print("A")
# if 70 <= number_grade < 80:
#      print("B")
# if 60 <= number_grade < 70:
#     print("C")
# if 50 <= number_grade < 60:
#      print("D")
# if number_grade < 50:
#      print("F")

#The following code has 5 seperate if statements - evaluates 5 conditions ^
#Prints B (Works as intended)

# number_grade = 76

# if number_grade >=80:
#     print("A")
# elif number_grade >=70:
#     print("B")
# elif number_grade >=60:
#     print("C")
# elif number_grade >=50:
#     print("D")
# elif number_grade <=50:
#     print("F")

# number_grade = 76

# if number_grade >=80:
#     print("A")
# elif number_grade >=70:
#     print("B")
# elif number_grade >=60:
#     print("C")
# elif number_grade >=50:
#     print("D")
# else: 
#     print("F")
# #if-Elif^on repeat-else


#Practice
def inspect_number(x):
    if x > 0:
        print("positive")
    elif x < 0:
        print("negative")
    else:
        print("zero")

inspect_number(-23)
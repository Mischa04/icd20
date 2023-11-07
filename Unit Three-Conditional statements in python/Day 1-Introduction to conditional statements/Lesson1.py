#Check if number is positive
number = 89
if number > 0:
    print(f"{number} is positive")

if number <=0:
    print(f"{number} is not positive")

#Determine if a person can vote (age 18 years and older)
age = int(input("Please enter your age: "))
if number >=18:
    print("is allowed to vote")
if number <18:
    print("You are not eligable to vote")

#Check if a string is empty
str=input("Please enter a string")
if len(str) == 0:
    print("the string is empty")
if len(str) !=0:
    print("the string is not empty")

#Write a function that returns the maximum of two numbers.
def max_number(a, b):
    if a>b:
        return a
    return b

#Use the function for testing
print(max_number(4,5))
print(max_number(14,5))

#Check if a user's input is equal to a secrt password
def password_checker(password, user_input):
    if password == user_input:
        return True
    return False

pwd = input("password")
secret = "HIII"
#########

#Write a function that schecks if a number is within a specific range (lower-upper inclusive)

def range_checker(num, lower, upper)
    if lower <=num <=upper:
        return True
    return False
a =int(input("please enter a number between 1 and 10: "))
if range_checker(a, 1, 10)
print("Good person you listen to instructions!!!")

if range_checker(a, 1, 10)
print("AGH im not happy YOU DONT LISEN")


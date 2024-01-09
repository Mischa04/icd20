# #Problem 1: Print the numbers from 1 to 10 using range() without specifying the start value
# for number in range(1, 11):
#     print(number)

# #Problem 2: Print even numbers from 2 to 10 ujsing range() with a step
# for number in range(2, 11, 2):
#     print(number)

#Problem 3:Calculate and print the sum of odd numbers from 1 to 7 using range() with a step
# sum_odd = 0
# for number in range(1, 8, 2):
#     sum_odd += number
# print(sum_odd)


#Problem 4: Print the numbers from 10-1 using range() with a negative step
# for number in range(10, 0, -1):
#     print(number)

# #Problem 5: Print multiples of 4 from 4-20 using range() with appropriate start and step values
# for number in range(4, 21, 4):
#     print(number)

#Problem 6: Calculate and print the product of the first 5 naturel numbers using range() and a loop
# product = 1
# for number in range(1, 6):
#     product *= number

# print(product)

# #Question 7: Print the numbers from 3 to 12 but only if they are divisable by 3, using range() with a loop using if statement
# for number in range(3, 13):
#     if number % 3 == 0:
#         print(number)

# #Question 8: Generate a countdown from 5-1 and print "blast off" at the end
# for number in range(5, 0, -1):
#     print(number)

# print("Blast off!")

#Question 9: Print the square of numbers from 1 to 5 using range() with both start and stop values
# for number in range(1, 6):
#     square = number * number
#     print(f"The square of {number} is {square}")

#Question 10: Calculate and print the factorial of the first 7 naturel numb ers using range() and a loop
# for num in range(1, 8):
#     product = 1
#     for i in range(num, 0, -1):
#         product *= i
#     print(product)

#Question 11: Create and print a new string that contains every character of the word "WONDERFUL"
# str = "WONDERFUL"
# result=""
# for i in range(1,len(str),2):
#     print(str[i])

#Question 13: COunt and print the amount of vowels (a, e, i, o, u) in the word "COMPUTER" usig a for loop
# word = "COMPUTER"
# vowel_count = 0

# for str in word:
#     if str.upper() in ['A', 'E', 'I', 'O', 'U']:
#         vowel_count += 1

# print(vowel_count)

#Question 14: Check and print wheather the word "RACECAR" is a palindrome ising a for loop
# backwards = ""
# forwards = "RACECAR"

# for index in range(len(forwards)-1,-1,-1):
#     backwards +=forwards[index]

# if backwards == forwards:
#     print("Yes")
# else:
#     print("No")
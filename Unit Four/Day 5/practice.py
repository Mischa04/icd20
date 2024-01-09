#Problem 1: Print the numbers from 1 to 10 using range() without specifying the start value
for number in range(1, 11):
    print(number)

#Problem 2: Print even numbers from 2 to 10 ujsing range() with a step
for number in range(2, 11, 2):
    print(number)

Problem 3:Calculate and print the sum of odd numbers from 1 to 7 using range() with a step
sum_odd = 0
for number in range(1, 8, 2):
    sum_odd += numb er
print(sum_odd)

#Problem 4: Print the numbers from 10-1 using range() with a negative step
for number in range(10, 0, -1):
    print(number)

#Problem 5: Print multiples of 4 from 4-20 using range() with appropriate start and step values
for number in range(4, 21, 4):
    print(number)

#Problem 6: Calculate and print the product of the first 5 naturel numbers using range() and a loop
product = 1
for number in range(1, 6):
    product *= number

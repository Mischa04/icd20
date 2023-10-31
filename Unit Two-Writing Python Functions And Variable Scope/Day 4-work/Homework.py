def middleThree(s):
   
    middle_index = len(s) // 2

   
    middle_three = s[middle_index - 1:middle_index + 2]

    return middle_three

print(middleThree("Candy"))  
print(middleThree("and"))    
print(middleThree("solving")) 

#Question 2
def lastChars(a, b):
 
    if len(a) == 0:
        first_char = "@"
    else:
        first_char = a[0]

  
    if len(b) == 0:
        last_char = "@"
    else:
        last_char = b[-1]

   
    result = first_char + last_char

    return result


print(lastChars("last", "chars")) 
print(lastChars("yo", "java"))   
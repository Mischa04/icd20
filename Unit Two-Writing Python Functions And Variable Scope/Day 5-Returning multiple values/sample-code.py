print("="*10)

print("Hello"*4)

print("-"*45)

def sample_function():
    x=7
    y=8
    z=9
    return x,y,z
a,b,c = sample_function()

print(a)  #7
print(c)  #9
print(sample_function()) #(7, 8, 8)
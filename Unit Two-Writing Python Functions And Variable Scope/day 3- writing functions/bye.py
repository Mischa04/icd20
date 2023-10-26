def calcultae_cylinder_volume(radius, height):
    return 3.14*radius**2*height
radius=int(input("please enter a radius: "))
height=int(input("Please enter a height: "))
volume=calcultae_cylinder_volume(radius,height)
print(volume)
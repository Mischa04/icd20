import random
customers = random.randint(5,10)

print(customers)

weather = ["cold and sunny", "hot and sunny", "rainy"]
weather_multiplier = [1.2, 2.2, 0.2]

weather_type = random.randint(0,2)
print(weather_type)

weath = weather[weather_type]
multiplier = weather_multiplier[weather_type]
print(weather[weather_type])
print(weather_multiplier[weather_type])

customers *=multiplier

print(customers)


while(not gameover):
    #Play 1 day of the game
    #ask if they want to play again
    #if no gameover = true

#Day 1 work
name = input("Please enter your name: ")

#Game 1
print("Game 1")
opponent_1=input("Please enter opponents 1's name: ")
your_points_game_1=int(input("Please enter your points game 1: "))
opponent_points_game_1=int(input("Please enter your opponents' score in game 1: "))
Percentage_1= (f"{your_points_game_1/36:.2%}") 
line_1 = (f"{opponent_1:<10} {your_points_game_1:>10} {opponent_points_game_1:>15} {Percentage_1:>10} ")


#Game 2
print("Game 2")
opponent_2=input("Please enter opponents 2's name: ")
your_points_game_2=int(input("Please enter your points game 2: "))
opponent_points_game_2=int(input("Please enter your opponents' score in game 2: "))
Percentage_2= (f"{your_points_game_2/36:.2%}") 
line_2 = (f"{opponent_2:<10} {your_points_game_2:>10} {opponent_points_game_2:>15} {Percentage_2:>10} ")

#Game 3
print("Game 3")
opponent_3=input("Please enter opponents 3's name: ")
your_points_game_3=int(input("Please enter your points game 3: "))
opponent_points_game_3=int(input("Please enter your opponents' score in game 3: "))
Percentage_3= (f"{your_points_game_3/36:.2%}") 
line_3 = (f"{opponent_3:<10} {your_points_game_3:>10} {opponent_points_game_3:>15} {Percentage_3:>10} ")

#Game 4 
print("Game 4")
opponent_4=input("Please enter opponents 4's name: ")
your_points_game_4=int(input("Please enter your points game 4: "))
opponent_points_game_4=int(input("Please enter your opponents' score in game 4: "))
Percentage_4= (f"{your_points_game_4/36:.2%}") 
line_4 = (f"{opponent_4:<10} {your_points_game_4:>10} {opponent_points_game_4:>15} {Percentage_4:>10} ")

#Game 5

print("Game 5")
opponent_5=input("Please enter opponents 5's name: ")
your_points_game_5=int(input("Please enter your points game 5: "))
opponent_points_game_5=int(input("Please enter your opponents' score in game 5: "))
Percentage_5= (f"{your_points_game_5/36:.2%}") 
line_5 = (f"{opponent_5:<10} {your_points_game_5:>10} {opponent_points_game_5:>15} {Percentage_5:>10} ")

print("Dots and Box Score Tracker")
print(f"Players name: {name}")

#Day 2 work

#Output
print(f"{'Opponent':<10} {'Your Points':<10} {'Opponent Points':<15} {'Box %':>10}")
divider = (f"{'===================================================='}")
print(divider)
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(divider)

total_points= your_points_game_1 + your_points_game_2 + your_points_game_3 + your_points_game_4 + your_points_game_5
total_points_opponents= opponent_points_game_1 + opponent_points_game_2 + opponent_points_game_3 + opponent_points_game_4 + opponent_points_game_5
total_points_percentage = (f"{total_points/(5*36):.2%}")

print("Summary:")
print(f"Total points: {total_points}")
print(f"Total opponent's points: {total_points_opponents}")
print(f"Percentage points received: {total_points_percentage}")

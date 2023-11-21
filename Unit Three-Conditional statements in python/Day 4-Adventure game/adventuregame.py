import random

def create_character():
    #First is name
    character_name =input("Please enter your characters name: ")

    #Character class
    print("Choose character class: Warrior: 1, Mage: 2, Archer: 3")
    
    class_choice = input("Enter the number of your choice (1-3): ")
    
    if class_choice == '1':
        character_class = 'Warrior'
    elif class_choice == '2':
        character_class = 'Mage'
    elif class_choice == '3':
        character_class = 'Archer'
    else:
        print("Invalid choice. Defaulting to Warrior.")
        character_class = 'Warrior'
   
    #Character health
    initial_health = random.randint(50,100)
    print(f"The initial health is {initial_health}")
    return character_name, character_class, initial_health
    
    

##############FUNCTION 2######################

def game_intro():
    character_name, character_class, initial_health = create_character()
    print(f"Hello {character_name}, you are a {character_class} from the planet pluto.")
    print("In order to return to your homeland you need to survive the challenges ahead of you, Goodluck!")
    print(f"your initial health is {initial_health}")
    return initial_health
    
#game_intro()


##############FUNCTION 3######################
def make_decision():
    direction = input("Please enter '1' for left or '2' for right to choose your path: ")

    if direction == '1':
        path = 'left'
    elif direction == '2':
        path = 'right'
    else:
        print("invalid entry, defaulting to 1 for left")
        path = 'left'

    return direction


##############FUNCTION 4#########################

def encounter(direction):
    if direction == '1':
        print("You have been hit by an asteroid. You have lost 90 points!")
        damage_taken = -90
    else:
        print("You have been flown back to pluto. You have gained 90 points!")
        damage_taken = 90
    return damage_taken  

################FUBTION 5##################
def manage_health(initial_health, damage_taken):
    current_health = initial_health + damage_taken
    print(f"Your current health after the encounter is {initial_health}")
    print(f"Your damage after the encounter is {damage_taken}")
    print(f"Your current health is {current_health}")
    return current_health
    #return current_health
    #print(f"Your current health after the encounter is {current_health}")

initial_health = game_intro()
direction = make_decision()
damage_taken = encounter(direction)
current_health = manage_health(initial_health, damage_taken)

#print(f"Your damage after the encounter is - second time {damage_taken}")



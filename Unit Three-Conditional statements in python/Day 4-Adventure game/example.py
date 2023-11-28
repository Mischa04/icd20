def make_decision():
    decision = input("Please enter left or right to choose your path: ")

if decision == 'left':
    path = 'left'
elif decision == 'right':
    path = 'right'
else:
    print("Invalid choice. Default to left")
    path = 'left'

return path
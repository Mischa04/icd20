def input_bug_count(bug_type):
    count=int(input(f"Please enter number of {bug_type}:"))
    return count

    return bugtype1
bug_1=(input("Enter the type of bug: "))
#bug_1_count(number of bugs)

def input_bug_count(bugtype2):
    return bugtype2
bug_2=(input("Enter the type of bug: "))
bug_2_count=int(input(f"Please enter number of {bug_2}:"))
#bug_2_count(number of bugs)

def input_bug_count(bugtype3):
    return bugtype3
bug_3=(input("Enter the type of bug: "))
bug_3_count=int(input(f"Please enter number of {bug_3}:"))
#bug_3_count(number of bugs)

total= bug_2_count + bug_2_count + bug_3_count

#percentages
bug_1_percentage=(f"{100/total*bug_1_count:.2%}")
bug_2_percentage=(f"{100/total*bug_2_count:.2%}")
bug_3_percentage=(f"{100/total*bug_3_count:.2%}")
#############################################################
#Lines for output
line_1=(f"{bug_1:<10}{bug_1_count:>10}{bug_1_percentage:>15}")
line_2=(f"{bug_2:<10}{bug_2_count:>10}{bug_2_percentage:>15}")
line_3=(f"{bug_3:<10}{bug_3_count:>10}{bug_3_percentage:>15}")
###############################################################
#OUTPUT
print(f"{'Bug Type':<10} {'Count':>10} {'Percentage':>15}")
print("="*35)
print(line_1)
print(line_2)
print(line_3)
print("="*35)
print(f"{'total':<10}{total:>10}{'100.00%':>15}")

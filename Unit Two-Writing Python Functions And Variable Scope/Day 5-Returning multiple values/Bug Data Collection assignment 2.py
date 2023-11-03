def input_bug_count(bug_type):
    count=int(input(f"Please enter number of {bug_type}:"))
    return count

def calculate_percent(total, count):
    return (f"{count/total:.2%}")

def input_bug_type_and_count():
    bug_type=input("Enter bug type: ")
    bug_count=input_bug_count(bug_type)
    return bug_type, bug_count

#########################################
bug1, count1 = input_bug_type_and_count()
bug2, count2 = input_bug_type_and_count()
bug3, count3 = input_bug_type_and_count()

total = count1+count2+count3

percent1 = calculate_percent(total,count1)
percent2 = calculate_percent(total,count2)
percent3 = calculate_percent(total,count3)
##########################################



def display_table(bug1, count1, bug2, count2, bug3, count3):
    print(f"{'Bug Type':<10}{'Count':>10}{'Percentage':>15}")
    print("="*35)
    print (f"{bug1:<10}{count1:>10}{percent1:>15}")
    print (f"{bug2:<10}{count2:>10}{percent2:>15}")
    print (f"{bug3:<10}{count3:>10}{percent3:>15}")
    print("="*35)
    print(f"{'Total':<10}{total:>10}{'100%':>15}")


table=display_table(bug1, count1, bug2, count2, bug3, count3)

print(table)





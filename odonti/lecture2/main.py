# conditions 
"""
using operators in python to come up with condition
a == b
a > b
a < b
a >= b
a <= b
a != b
"""

# # users input and compare to your number and print yes:
# def numbers():
#     num = int(input("what is your number?: "))
#     number = 8
#     if num == number:
#         print("Yes")
#     else:
#         print("No")
# numbers()


# negation conditions
# def number():
#     num = int(input("whats your number?: "))
#     number = 6
#     if num != 6:
#         print("No")
# number()


# control flow: using the if, elif, and else condition:
# 
# def check_num():
#     value = int(input("choose one number from 1 to 20"))
#     target = 11
#     if value > target:
#         print("Greater")
#     elif 


# take users input to check for the week of the days:
def days_of_week():
    week = input("whats today?: ")
    if week == "Monday":
        print("this is", week)
    elif week == "Tuesday":
        print("This is" , week)
    elif week == "Wednesday":
        print("This is", week)
    elif week == "Thursday":
        print("Thursday")
    elif week == "Friday":
        print("Friday")
    elif week == "Saturday":
        print("Saturday")
    else:
        print("Sunday")
days_of_week()



def days_of_week():
    week = input("Enter day of the week?: ")
    match week:
        case "Monday":
            print("Monday")
        case "Tuesday":
            print("Tuesday")
        case "Wednesday":
            print("Wednesday")
        case "Thursday":
            print("Thursday")
days_of_week()

    
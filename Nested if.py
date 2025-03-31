#NESTED IF
#Get age from the user.
# If age is greater than or equal to 18.get height from the user.
# If not print(“Sorry you need to be atleast 18 years old to ride”).
# if height is greater than or equal to 1.4 print(“you are eligible
# to ride the roller coaster”) else print(“Sorry,you need to be atleast
# 1.4 meters tall to ride”)

"""age=int(input("Enter your age"))
if age>=18:
    height=float(input("Enter your height"))
    if height>=1.4:
        print("you are eligible to ride the roller coaster")
    else:
        print("Sorry,you need to be atleast 1.4 meters tall to ride")
else:
    print("Sorry you need to be atleast 18 years old to ride")

#Get input for salary and age.
#If salary greater than or equal to 20000 or age greater than 18 and less than or equal to 25,get input
#for required loan amount. If not print you are not eligible for loan.
#If required loan amount is less than or equal to 50,000 print You are eligible for loan.
#If it is greater than 50,000 print You are eligible for loan

salary=int(input("Enter your salary"))
age=int(input("Enter your age"))
if salary>=20000 and age>18 or age<=25:
    loan=int(input("Enter your loan amount"))
    if loan<=50000:
        print("You are eligible for loan")
    else:
        print("maximum loan amount is 50000")
else:
    print("you are not eligible for loan")

#Get input for the user's age.
# If the age is greater than or equal to 12 and lesser than or equal to 65,
# get input for the number of tickets needed.
# Else, print "You are not eligible for a discount.
# " If the number of tickets is greater than 4, print "Maximum 4 tickets allowed.
# else print “Tickets booked”

age=int(input("Enter your age"))
if age>=12 and age<=65:
    tickets_allowed=int(input("Enter the number of tickets"))
    if tickets_allowed>4:
        print("Maximum 4 tickets allowed")
    else:
        print("tickets booked")
else:
    print("You are not eligible for a discount")

#Write a Python program for an ATM machine that checks whether a user can withdraw
#a specified amount of money from their account.
#The program should consider the following conditions:
#The account must be active.
#The entered PIN must be correct.
#The withdrawal amount must not exceed the account balance.
#If all conditions are met, the withdrawal should be successful, and the account balance should be updated.
#If any condition is not met, an appropriate message should be displayed.

money=int(input("Enter the amount"))
account=True
pin="abcd"
withdrawal_amount<=2500
if account==True:
    print("the account must be active")
    if pin=="abcd":
        print("the entered pin is correct")
    else:
        print("the entered pin is wrong")
        if withdrawal_amount<=2500:
            print("the money will be withdrawn")
        else:
            print("the money will not be withdrawn")
            
else:
    print("the account must be inactive")

the_account=True
set_pin=1357
account_balance=100000

if the_account==True:
    print("the account is active")
    entered_pin = int(input("Enter your pin"))
    if set_pin==entered_pin:
        withdrawal_ammount = int(input("Enter your ammount"))
        if withdrawal_ammount<=account_balance:
            print("the money will be withdrawn")
            account_balance-=withdrawal_ammount
            print("account_balance=",account_balance)
        else:
            print("the money will not be withdrawn")


    else:
        print("the password is incorrect")
else:
    print("the account is inactive")"""

#Write a Python program for an ATM machine that checks whether a user can withdraw
#a specified amount of money from their account.
#The program should consider the following conditions:
#The account must be active.
#The entered PIN must be correct.
#The withdrawal amount must not exceed the account balance.
#If all conditions are met, the withdrawal should be successful, and the account balance should be updated.
#If any condition is not met, an appropriate message should be displayed.

the_account=True
set_pin=1234
account_balance=50000

if the_account==True:
    print("The account is active")
    entered_pin=int(input("Enter your pin"))
    if set_pin==entered_pin:
        print("The entered pin is correct")
        withdrawal_ammount=int(input("Enter the ammount"))
        if withdrawal_ammount<=account_balance:
            print("the money will be withdrawn")
            account_balance-=withdrawal_ammount#account_balance=account_balance-withdrawal_ammount
        else:
            print("the money will not be withdrawn")
        print("the entered pin is incorrect")
    else:
        print("incorrect pin")
else:
    print("The account is inactive")






















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








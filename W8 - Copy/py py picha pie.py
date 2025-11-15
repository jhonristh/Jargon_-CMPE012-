#SIMPLE ATM MACHINE FLOW
"""
#high level code
welcome_messages ():
card_reader(isCardInsterted) :
input_and_validate_pin_number(pinNumber): return isValid
transaction_selection(transaction):
amount_and_account_selection (amount) :
transaction_validation(amount, balance) return isValid
card_ejection():
cesh_dispensing():
print receipt(amount, balance) :

while condition
parang if, pag true true, wn;t stop will only stop when nag false na
-void loop
-void setup
"""
####how to clear console like refreshing
import time
import os
#def clear_console
amount = 0
balance = 1000
pin_number = "0000"

def welcome_messages():
    time.sleep(1)
    print("---- Welcome to Apatronics Bank of the Philippines! ----")
    time.sleep(1)
    print("........................................................")
    time.sleep(1)
    print("Please enter you card.")

def card_reader(isCardInserted):
    if isCardInserted == "YES":
        print("Card is inserted")
        return True
    else:
        return False
def input_and_validate_pin_number():
    for i in range(4):
        if i == 3:
            print("Card Blocked...Access Denied")
            return False
        inputPinNumber = input("Enter pin number: ")
        if inputPinNumber == pin_number:
            return True
        else:
            print("Pin Number Incorrect, try again")
def transaction_selection():
    transaction = input("Please select transaction: ")
    return transaction
def transaction_validation(amount, balance):
    if balance > amount:
        return True
    else:
        print("Insufficient Fund...Transaction validation failed, please try again")
        return False
def card_ejection():
    print("Card Ejected. Please get your card.")
def cash_dispensing():
    print("Cash dispensing. Please get your card.")
def print_receipt(amount):
    global balance
    balance = balance - amount
    print("Your Remmaining balance is:" + str(balance))
    print("Please get your receipt")


######
while True: ##to loop continuously
    welcome_messages()
    isCardInserted = input("Is card inserted? (YES/NO): ")
    if not card_reader(isCardInserted.upper()): #false
        #print("Card is not inserted")
        continue
    print("Next Steps...>")
    if not input_and_validate_pin_number():
        continue
    print("Next Steps...SUCCESS")

    transaction = transaction_selection()
    if transaction.lower() == "withdraw":
        amount = int(input("Please enter your amount: "))
        if transaction_validation(amount, balance):
            print("Withdraw operation started")
            time.sleep(2)
            card_ejection()
            time.sleep(2)
            cash_dispensing()
            time.sleep(2)
            print_receipt(amount)
            time.sleep(1)
        else:
            card_ejection()
            continue
    elif transaction.lower() == "Check Balance":
        print("Check balance operation started . . .")
    else:
        card_ejection()
        continue

#stepinto
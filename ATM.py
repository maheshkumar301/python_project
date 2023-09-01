from cardholder import cardholder

def print_menu():
    print("Please choose from one of the following option")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.show Balance")
    print("4.Exit")

def deposit(cardholder):
    try:
        deposit=float(input("Enter a amount to deposit:"))
        cardholder.set_balance(cardholder.get_balance() + deposit)
        print("Thankyou for deposit.Your new balance is :",str(cardholder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardholder):
    try:
        withdraw=float(input("Enter a amount to withdraw:"))
        if (cardholder.get_balance() < withdraw):
            print("Insufficient balance:(")
        else:
            cardholder.set_balance(cardholder.get_balance() - withdraw)
            print("You are good to go!Thankyou:)")
    except:
        print("Invalid input")

def check_balance(cardholder):
    print("Your current balance is:",cardholder.get_balance())

if __name__=="__main__":
    current_user=cardholder("","","","","")
    list_of_cardholders=[]
    list_of_cardholders.append(cardholder("123456789",1234,"Mahesh","kumar",1500))
    list_of_cardholders.append(cardholder("987654321",9876,"Arun","kumar",1200.50))
    list_of_cardholders.append(cardholder("43216789",4321,"Leo","mk",1234.75))

    debitCardnum=""
    while True:
        try:
            debitCardnum=input("Please insert your debit card:")
            debitMatch=[holder for holder in list_of_cardholders if holder.cardnum==debitCardnum]
            if (len(debitMatch))>0:
                current_user=debitMatch[0]
                break
            else:
                print("Card number not recognized.please try again.")
        except:
            print("Card number not recognized.please try again.")
    
    while True:
        try:
            userPin=int(input("Enter your PIN number:"))
            if (current_user.get_pin()==userPin):
                break
            else:
                print("Invalid PIN. Please try again")
        except:
            print("Invalid PIN. Please try again")
    
    print("Welcome",current_user.get_firstname(),":)" )
    option=0
    while(True):
        print_menu()
        try:
            option=int(input())
        except:
            print("Invalid input.Please try again")
        if (option==1):
            deposit(current_user)
        elif (option==2):
            withdraw(current_user)
        elif (option==3):
            check_balance(current_user)
        elif(option==4):
            break
        else:
            option=0
    print("Thank You .Have a nice day :)")




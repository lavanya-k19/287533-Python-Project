amount= 0

def Income():
    global amount
    print("Enter the income: ")
    income = int(input())
    amount += income
    Menu()

def Expense():
    global amount
    print("Enter the amount spend: ")
    spend =  int(input())
    amount = amount - spend
    Menu()

def Balance():
    global amount
    print(amount)
    Menu()

def Decide_Reset():
    global amount
    print("This command will erase all data. Do you want to continue ?")
    print("\nPress 0 to return\nPress 1 to reset data")
    reset =  int(input())
    if(reset == 0):
        one = Menu()
    elif(reset == 1):
        amount = 0
    else:
        print("Enter a valid option")
    Menu()

def Exit():
    print("Are you sure you want to quit ?")
    print("\nPress 0 to return to menu\nPress 1 to quit")
    e =  int(input())
    if(e== 0):
        Menu()
    elif(e == 1):
        exit()
    else:
        print("Enter a valid option.")
    Menu()

def Menu():
    print("Select an Option : \n1.Income\n2.Expenditure")
    print("3.Balance\n4.Reset Data\n5.Exit\n")
    option = int(input())
    if(option == 1):
        Income()
    elif(option == 2):
         Expense()
    elif(option == 3):
        Balance()
    elif(option == 4):
        Decide_Reset()
    elif(option == 5):
        Exit()
    else:
        print("Enter a valid option.")
    Menu()
Menu()
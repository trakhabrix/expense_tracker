#Storage
number_expense = 0
expense_list = []
#Create Expense
def add_expense():
    global number_expense
    print("\n=====Add Section=====")
    item = input("Input the Expense: ")
    amount = float(input("Input the Amount: "))
    number_expense += 1
    #Store
    expense_data = {"ID": number_expense, 
                    "ITEM": item,
                    "AMOUNT": amount}
    expense_list.append(expense_data)
    print (f"Expense Added +{number_expense}")


#View EXpense
def view_expense(): 
    if not expense_list:
        print("\nNot Yet Record")
    print ("=====Expense List=====")
    for expense in expense_list:
        print(f"{expense['ID']}  {expense['ITEM']}  ₱{expense['AMOUNT']}\n")

def expense_menu ():
    while True:
        print ("""====Expense Tracker====
1 - Add Expense
2 - View Expense Records
3 - Update Expense Records
4 - Delete Expense Records
5 - Exit""")
        #Input
        choice_menu = (input("Enter your choice (1-5): ")).strip()
        #If (for whitespace / empty / letters)
        if choice_menu == "" or not choice_menu.isdigit():
            print("Please Input Only Valid Number")
            continue
        choice_menu = int(choice_menu)
        #If-Else (for choice)
        if choice_menu == 1:
            print ('1')
        elif choice_menu == 2:
            print ('2')
        elif choice_menu == 3:
            print ('3')
        elif choice_menu == 4:
            print ('4')
        elif choice_menu == 5:
            print ('Exiting...\nThanks for Using!!')
            break
        else:
            print ('Invalid Choice')

expense_menu()

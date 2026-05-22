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
    expense_data = {"NUM": number_expense, 
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
        print(f"# {expense['NUM']}  NAME: {expense['ITEM']}  AMOUNT: ₱{expense['AMOUNT']}\n")

#Update Expense
def update_expense():
    view_expense()
    if not expense_list:
        print("No records found.")
        return

    num_choose = int(input("Enter number to update: "))
    #Update Part
    for expense in expense_list:
        if expense["NUM"] == num_choose:

            new_item = input("Enter new expense name: ")
            new_amount = float(input("Enter new amount: "))

            expense["ITEM"] = new_item
            expense["AMOUNT"] = new_amount

            print("Expense Updated Successfully!\n")
            return
    print("Expense number not found.\n")
        
#Delete Expense
def delete_expense():
    view_expense()
    if not expense_list:
        print("No records found.")
        return
    
    num_choose = int(input("Enter number to delete: "))

    for expense in expense_list:
        if expense["NUM"] == num_choose:
            
            expense_list.remove(expense)
            print("Expense Deleted Successfully!\n")
            return

    print("Expense number not found.\n")
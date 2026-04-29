while True:
    def expense_menu():
        print ("""Expense Tracker
        1 - Create/Input User
        2 - Update User
        3 - Saved User Info
        4 - Delete User Info
        5 - Exit""")
        
        choice_menu = int(input("Enter your choice (1-5): "))
        if choice_menu < 1 or choice_menu > 5:
            print ("Invalid Choice")
            choice_menu = int(input("Enter your choice (1-5): "))
        elif choice_menu == " ":
            print ("Please Enter Your Choice")
            choice_menu = int(input("Enter your choice (1-5): "))

    expense_menu()
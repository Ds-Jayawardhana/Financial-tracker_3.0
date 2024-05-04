'''
Date:-27/04/2024
Name:Disandu Sanhida
IIT Student ID:-20230469
Westminster Student Id:-2083055
'''


#IMporitng Tkinter Module
#Importing the JSON module for handling data
import tkinter as tk
from tkinter import ttk
import json
# Global dictionary to store transactions
transactions = {}

#Defining A class
class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("850x450")
        self.root.resizable(False,False)
        #Icont for the programme
        self.root.iconbitmap("iit.ico")
        self.logo_image=tk.PhotoImage(file="Finance Tracker GuI Logo.png")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")
    #Defining the functions Create Widgets


    def create_widgets(self):
        # Frame for table and scrollbar
        self.table_frame=ttk.Frame(self.root)
        #self.search_frame=ttk.Frame(self.root) 
        # Treeview for displaying transactions
        self.label=ttk.Label(self.table_frame,image=self.logo_image)
        self.label.pack()
        self.Heading_label=ttk.Label(self.table_frame,text="Welcome To Personal Finance Tracker 3.0")
        self.Heading_label.pack()
        self.Heading_label.config(font=("Arial",17, "bold"))
          


        self.main_table=ttk.Treeview(self.table_frame,columns=("Index","Purpose","Amount","Date"),show="headings",height=10)
        self.main_table.heading("Index",text="Index")
        self.main_table.heading("Purpose",text="Purpose",command=lambda: self.sort_by_column("Purpose", False))
        self.main_table.heading("Amount",text="Amount",command=lambda: self.sort_by_column("Amount", False))
        self.main_table.heading("Date",text="Date",command=lambda: self.sort_by_column("Date", False))
        self.main_table.column("Index",width=100,anchor="center",minwidth=100,stretch=False)
        self.main_table.column("Purpose",width=250,minwidth=250,stretch=False)
        self.main_table.column("Amount",width=250,anchor="center",minwidth=250,stretch=False)
        self.main_table.column("Date",width=200,minwidth=200,stretch=False)

        self.table_frame.pack()
        self.main_table.pack(side='left', fill='both', expand=True)
        # Scrollbar for the Treeview
        self.ver_scroll=ttk.Scrollbar(self.table_frame,orient="vertical",command=self.main_table.yview)
        self.ver_scroll.pack(side="right",fill="y")
        self.main_table.configure(yscrollcommand = self.ver_scroll.set)
        
        # Search bar and button
        self.search_frame=ttk.Frame(self.root)
        self.search_entry=ttk.Entry(self.search_frame)
        self.search_button=ttk.Button(self.search_frame,text="Search",command=self.search_transactions)

        #Image for the Search Button
        img=tk.PhotoImage(file="search_img.png")
        self.search_entry.pack(pady=10)
        self.search_button.config(image=img,compound="right")
        self.search_button.img=img
        self.search_button.pack()
        self.search_frame.pack()

        
    #Defining the function to load transactions to load the transactions int he tree view
    def load_transactions(self,file_path="transactions.json"):
        file_path = "transactions.json"
        try:
                with open(file_path, "r") as json_file:
                    transactions = json.load(json_file)
                return transactions
        except FileNotFoundError:
            print("JSON File is Not Exsisting ")
            return {}
        except json.decoder.JSONDecodeError:
           print()
           transactions = {}
           #if the file not found initalize transactions list as empty
           return    
    #Defining the the display transactions one       
    def display_transactions(self, transactions):
        #Remove exsisiting transactions
       for item in self.main_table.get_children():
            self.main_table.delete(item)


        #Add transactions To the treeview
       index=1
       #Getting the purpose in the tranactions list to the tree view
       for purpose, transaction_list in transactions.items():
            for datas in transaction_list:
                    
                    amount=datas["amount"]
                    date=datas["date"]
                    self.main_table.insert("","end",values=(index,purpose,amount,date))
                    index=index+1

            
    #Definig the search transactiosn to search data in treeview
    def search_transactions(self):
        # Placeholder for search functionality
        self.search_query=self.search_entry.get().lower()
        self.main_table.selection_remove(self.main_table.selection())
        
        #getting the data in the tree view
        for item_id in self.main_table.get_children():
            item_values=self.main_table.item(item_id)["values"]
            
            
            if any(self.search_query in str(value).lower() for value in item_values):
                self.main_table.selection_add(item_id)
             
            

    #Defining the sorting Function
    def sort_by_column(self, col, reverse):
        self.data=[(self.main_table.set(child,col),child)for child in self.main_table.get_children("")]
        if col == "Amount":
            self.data.sort(key=lambda x: float(x[0]), reverse=reverse)
        else:
            self.data.sort(reverse=reverse)

        for index, item in enumerate(self.data):
            self.main_table.move(item[1], "", index)

        self.main_table.heading(col, command=lambda: self.sort_by_column(col, not reverse))
        


# Function to load transactions from JSON file (improved error handling)
def load_transactions(file_path="transactions.json"):
   global transactions
   #calling the gloabal transactions list
   file_path = "transactions.json"
    #error handling ifthere isn't exsist a file in the directory
   try:
        #Attempting to open the JSON file and load its contents into the 
        with open(file_path, "r") as json_file:
            transactions = json.load(json_file)
   except FileNotFoundError:
        print("File not found. Creating a new file...")
        transactions = {}
        return#if file not found,initalize transactions
    #Decode json file if there isn't any data in the file when programme intilizly start
   except json.decoder.JSONDecodeError:
        print()
        transactions = {}#if the file not found initalize transactions list as empty
        return
# Function to save transactions to JSON file
def save_transactions():
    global transactions# Accessing the global 'transactions' Variable
    ans = input("Do You Want To Save Changes(yes/no): ").lower()
    #Asking user to confirm the changes
    if ans == "yes":
    #if User enters yes    
        file_path = "transactions.json"
        with open(file_path, "w") as json_file:
            json.dump(transactions, json_file,indent=2)
            #Save user entered data to JSON File2
        print("Changes Saved Successfully...")
        
    elif ans == "no":
        print("Changes are not stored ")
    else:
        print("Incorrect Input please enter Yes/No")



# Function defined to read bulk of transactions from a exsisiting file
def read_bulk_transactions_from_file(bulk_file_name):
    global transactions
    
    #Calling the global transactions
    with open(bulk_file_name, 'r') as file:
        current_transaction = {}
        for line in file:
            #Split the line in the file into 2 parts by :
            parts = line.strip().split(":")
            if parts[0] == "Transaction":
                current_transaction = {}
                #Defining a new dictionary if part 1 of the line is transaction

            elif parts[0] == "Purpose":
                current_transaction["Purpose"] = parts[1].strip().capitalize()

            elif parts[0] == "Amount":
                current_transaction["Amount"] = parts[1].strip()

            elif parts[0] == "Date":
                current_transaction["Date"] = parts[1].strip()
            elif parts[0] == "Type":
                current_transaction["Type"] = parts[1].strip().lower()    
                transactions.setdefault(current_transaction["Purpose"].capitalize(), []).append({
                    "amount": int(current_transaction["Amount"]),
                    "type": current_transaction["Type"],
                    "date": current_transaction["Date"]
                })                   
        save_transactions()            
    return transactions

# Function to add a transaction (assuming 'transactions' is a dictionary)
def add_transaction():
    
    global transactions

    load_transactions()
    print("---------------------Add Transactions------------------------")
    #Asking user to input the purpose
    purpose = input("Enter the transaction purpose: ").capitalize()
    #Check whether the user inputed purpose exsist in the transactions
    if purpose in transactions:
        print("This transaction already exists. Do you want to add details to it?")
        pur_ans = input("Enter Yes or No: ").strip().lower()
        #converting user inputed answer into the lower case
        if pur_ans == "yes":
            #Using Error handling to handle the Valueerror if user input strings for the amount
            try:
                amount = float(input("Enter the Amount: Rs."))
                if amount <= 0:
                  print("Amount cannot be negative.")
                  return   
            except ValueError:
                print("Please Enter a Amount in Integers.")
                return
            #Check the user entered amount is less than 0 or equals to zero    
            #Asking user what is the type of transaction    
            trs_type = str(input("Enter the Transaction Type (Income/Expense): ")).strip().lower()
            #Check whether the user input Income, expense word correctly
            if trs_type not in ("income", "expense"):
                print("Invalid type. Please enter 'Income' or 'Expense'.")
                #if user input wrong it return s to enter it again
                return
            date = input("Enter the Date in Format YYYY-MM-DD: ")
            #Appending user inputed data into a dictionary with keys
            transactions[purpose].append({"amount": amount, "type": trs_type, "date": date})

  
        elif pur_ans == "no":
            return
            '''
            try:
                amount = float(input("Enter the Amount: Rs."))
            except ValueError:
                print("Please Enter Only Integers")
                return
            if amount < 0:
                print("Amount cannot be negative.")
                return
            trs_type = input("Enter the Transaction Type (Income/Expense): ").strip().lower()
            if trs_type not in ("income", "expense"):
                print("Invalid type. Please enter 'Income' or 'Expense'.")
                return
            date = input("Enter the Date in Format DD/MM/YY: ")
            transactions[purpose] = [{"amount": amount, "type": trs_type, "date": date}]
            '''
        else:
            print("Please Enter only (Yes/No)")
    else:
        try:
          amount = int(input("Enter the Amount: Rs."))
          if amount <= 0:
            print("Amount cannot be negative.")
            return
        except ValueError:
          print("Enter Only Integers for the Amount")
          return
        #Check the user entered amount is less than 0 or equals to zero    
        trs_type = input("Enter the Transaction Type (Income/Expense): ").strip().lower()
        if trs_type not in ("income", "expense"):
            print("Invalid type. Please enter 'Income' or 'Expense'.")
            return
        date = input("Enter the Date in Format YYYY-MM-DD: ")
        transactions[purpose] = [{"amount": amount, "type": trs_type, "date": date}]

    save_transactions()



#Function Defined to View saved transaction in JSON File
def view_transactions():

    global transactions

    #Creating the Gui window under View Transactions Function
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    if transactions:
        app.display_transactions(app.transactions)
        #User can update the details of transactions of transactions While opening the GUI Window
        root.mainloop()
    else:
        print("-------------------------------------")
        print("There are no transactions to display.")
        print("-------------------------------------")
        #Destroy the window if there isn't Transactions in the Json File
        root.destroy()     
    return

#Defining Function for Updating Transactions                                                    
def update_transaction():
    load_transactions()
    #view_transactions()
    if transactions:
        trans_purpose_update = input("Enter the Transaction Purpose Which you want to Update: ").capitalize()
        #Asking user what purpose want to update
        #Check whether the user entered purpose is in transactions
    else:
        return    
    if trans_purpose_update not in transactions:
        print("Enter an Existing Transaction Purpose to Update.")
        #root.destroy()
        return
    else:
        transactions_under_purpose = transactions[trans_purpose_update]
        #assingning the length of the transactiosn under purpose to the Num transactions
        num_transactions = len(transactions_under_purpose)
        print(f"There are {num_transactions} transactions under {trans_purpose_update}.")
        try:
            trans_number_updt = int(input(f"Enter the transaction number to update (1 to {num_transactions}): "))
        #Handles the value Error    
        except ValueError:
            print("Enter the Transaction Number Only In Integers")
            return
        #checking user entered transaction     
        if trans_number_updt <= 0 or trans_number_updt > len(transactions_under_purpose):
            print(f"Please enter a number between 1 and {num_transactions}.")
            return
        else:
            #Subtracting one from user entered index to get correct index
            trans_number_updt -= 1
            trans_data = transactions_under_purpose[trans_number_updt]
            
            print("----------------------------------------------------------------")
            print("Current Transaction Details:")
            #print(f"Amount: Rs. {trans_data['amount']}, Type: {trans_data['type']}, Date: {trans_data['date']}")
            print("----------------------------------------------------------------")
            
            trans_value_updt = input("Enter the field to update (amount, type, or date): ").lower()
            if trans_value_updt == "amount":
                try:
                    new_amount = float(input("Enter the new amount: Rs. "))
                except ValueError:
                    print("Enter Integers Only")
                    return
                transactions_under_purpose[trans_number_updt]["amount"] = new_amount
            elif trans_value_updt == "type":
                new_type = input("Enter the new transaction type (income/expense): ").strip().lower()
                if new_type not in ("income", "expense"):
                    print("Invalid type. Please enter 'income' or 'expense'.")
                    return
                #Updating Type to user Inputr=ed New type
                transactions_under_purpose[trans_number_updt]["type"] = new_type
            elif trans_value_updt == "date":
                #Updating Date into new transaction date
                new_date = input("Enter the new date in format YYYY/MM/DD: ")
                transactions_under_purpose[trans_number_updt]["date"] = new_date
            else:
                print("Invalid field. Please enter 'amount', 'type', or 'date'.")
                return
    save_transactions()

#function to delete transactions
def delete_transaction():
    delete_answer = 0
    # call the function view transaction to view the list of transactions existing
    #view_transactions()
    # assign the value None to the num variable
    
    print("------------------------------ Delete Transactions-------------------------------")
    if not transactions:
        return
    print("If you want to Delete All transactions under one purpose?")
    print("Enter yes If you want to delete All Transactions In a Purpose")
    print("Enter No to delete one transaction under a purpose")
    delete_answer = input("Enter Yes Or No: ").lower()
    if delete_answer == "yes":
        delete_purpose = input("Enter the transaction Purpose You want to delete: ").capitalize()
        if delete_purpose not in transactions:
            print("There is Not Such Purpose In Transactions List")
        else:
            del transactions[delete_purpose]
            print(f"Transactions under {delete_purpose} deleted Successfully...")
            save_transactions()
    elif delete_answer == "no":
        delete_purpose = input("Enter the transaction Purpose You want to delete: ").capitalize()
        #check whether user entered purpose is exsisting
        if delete_purpose not in transactions:
            print("There is Not Such Purpose In Transactions List")
        else:
            transactions_under_purpose = transactions[delete_purpose]
            num_transactions = len(transactions_under_purpose)
            try:    
                dlt_trans_num = int(input(f"Enter the Transaction Number to Delete between 1 to {num_transactions}: "))
                dlt_trans_num -= 1
            except ValueError:
                print("Enter Transaction Number Only in integers")   
                return 
                #Check user entered transactions number is less than 0 or greater than number of transactions in specific purpose
                if dlt_trans_num <= 0 or dlt_trans_num > len(transactions_under_purpose):
                   print(f"Please enter a number between 1 and {num_transactions+1}.") 
            #delete the specific transactions under a purpose
            del transactions[delete_purpose][dlt_trans_num]
            print(f"Transaction In purpose {delete_purpose} deleted Successfully")
            #when clearing one by one transactions under a purpose 
            #the json file remains the purpose without transactions
            #This 2 lines delete that remaining purpose before destroying it
            if transactions[delete_purpose]==[]:
               del transactions[delete_purpose]
               save_transactions()
            else:    
               save_transactions()
    else:
        print("Please Enter only (Yes/No)")


#Defining the the display summary function
def display_summary():
    global transactions
    print("------------------------------ Display Summary -------------------------------")
    # Initializing total_incomes
    total_incomes = 0
    # Initializing total_expenses
    total_expenses = 0
    # Initializing count_E
    count_E = 0
    # Initializing count_I
    count_I = 0
    # Check if there are any transactions in the transactions list
    if not transactions:
        print("There aren't any transactions to display Summary.")
    else:
        for purpose, details in transactions.items():
            for transaction in details:
                amount = float(transaction["amount"])
                if len(transaction)==3:
                    if transaction["type"] == "income":
                        count_I += 1
                        total_incomes += amount  
                    elif transaction["type"] == "expense":
                        count_E += 1
                        total_expenses += amount     
        print(f"The total Amount of Incomes are:- {total_incomes}")   
        print(f"The Total Amount of Expenses Are:-{total_expenses}")           
        print(f"Number of Incomes Are:- {count_I}")  
        print(f"Number of Expenses Are:- {count_E}")    
        print(f"Net Value is:{total_incomes-total_expenses}")


def main_menu():
    #call function to load transactions
    load_transactions()

    while True:
        #print main menu header
        print("\n-----------------------Personal Finance Tracker---------------------------") 
        #disaplay add transaction as option 01
        print("(1) Add Transaction")
        #disaplay view transaction as 2
        print("(2) View Transactions With GUI")
        #display update transactioon as 3
        print("(3) Update Transaction")
        #disaplay delete transaction as option 4
        print("(4) Delete Transaction")
        #display display summary as option 5
        print("(5) Display Summary")
        #display exit as option 6
        print("(6) Read Bulk Transactions from File")
        #display exit as option 6
        print("(7) Exit\n")
        #prompt user to enter the choice
        choice = input("Enter your choice: ")
      

        #call the add transaction function if user enters one
        if choice == '1':
            add_transaction()
        #call the view transaction function if user enters one    
        elif choice == '2':
            view_transactions()
        #call the update transaction function if user enters one
        elif choice == '3':
            update_transaction()
        #call the delete transaction function if user enters one    
        elif choice == '4':
            delete_transaction()
        #call the display function if user enters one    
        elif choice == '5':
            display_summary()
        elif choice == '6':
            try:
               bulk_file_name=input("Enter a File name to Read Transactions in Bulk:-")
               read_bulk_transactions_from_file(bulk_file_name)
            except FileNotFoundError:
                print("File Not Found Please enter a Exsisting File")


        #if user enters 7 exit from the program   
        elif choice == '7':
            save_transactions()
            print("Data Saved...")
            print("Exiting program...")
           
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("850x450")
        self.root.resizable(False,False)
        self.root.iconbitmap("iit.ico")
        self.logo_image=tk.PhotoImage(file="Finance Tracker GuI Logo.png")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")
        
    

    def create_widgets(self):
        
        # Frame for table and scrollbar
        self.table_frame=ttk.Frame(self.root,)
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
        self.main_table.column("Amount",width=250,minwidth=250,anchor="center",stretch=False)
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
        

    def load_transactions(self,file_path="transactions.json"):
        file_path = "transactions.json"
        try:
                with open(file_path, "r") as json_file:
                    transactions = json.load(json_file)
                return transactions
        except FileNotFoundError:
                return {}
        except json.decoder.JSONDecodeError:
           print("There isn't Any Transactions")
           transactions = {}#if the file not found initalize transactions list as empty
           return           
    def display_transactions(self, transactions):
        #Remove exsisiting transactions
       for item in self.main_table.get_children():
            self.main_table.delete(item)

        #Add transactions To the treeview
       index=1
       for purpose, transaction_list in transactions.items():
            for datas in transaction_list:
                    
                    amount=datas["amount"]
                    date=datas["date"]
                    self.main_table.insert("","end",values=(index,purpose,amount,date))
                    index=index+1
            

    def search_transactions(self):
        # Placeholder for search functionality
        self.search_query=self.search_entry.get().lower()
        self.main_table.selection_remove(self.main_table.selection())

        for item_id in self.main_table.get_children():
            item_values=self.main_table.item(item_id)["values"]
            

            if any(self.search_query in str(value).lower() for value in item_values):
                self.main_table.selection_add(item_id)
             
            

    def sort_by_column(self, col, reverse):
        self.data=[(self.main_table.set(child,col),child)for child in self.main_table.get_children("")]
        if col == "Amount":
            self.data.sort(key=lambda x: int(x[0]), reverse=reverse)
        else:
            self.data.sort(reverse=reverse)

        for index, item in enumerate(self.data):
            self.main_table.move(item[1], "", index)

            self.main_table.heading(col, command=lambda: self.sort_by_column(col, not reverse))
     
def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

if __name__ == "__main__":
    main()

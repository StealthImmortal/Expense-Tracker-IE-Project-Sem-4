    import sqlite3
    
    # Database Initialization
    conn = sqlite3.connect('budget_tracker.db')
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY, amount REAL, category TEXT, type TEXT, date TEXT, comment TEXT)''')
    
    # Function to add transaction
    def add_transaction(amount, category, type, date, comment):
        c.execute("INSERT INTO transactions (amount, category, type, date, comment) VALUES (?, ?, ?, ?, ?)",
                  (amount, category, type, date, comment))
        conn.commit()
    
    # Function to view transactions
    def view_transactions():
        c.execute("SELECT * FROM transactions")
        transactions = c.fetchall()
        for transaction in transactions:
            print(transaction)
    
    # Function to view balance
    def view_balance():
        c.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        income = c.fetchone()[0] or 0
        c.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        expense = c.fetchone()[0] or 0
        balance = income - expense
        print("Income:", income)
        print("Expense:", expense)
        print("Balance:", balance)
    
    # Function to categorize transactions
    def categorize_transactions(category):
        c.execute("SELECT * FROM transactions WHERE category=?", (category,))
        transactions = c.fetchall()
        for transaction in transactions:
            print(transaction)
    
    # Main function
    def main():
        categories = ["Food", "Travel", "Fuel", "Shopping", "Bills & Misc"]
        while True:
            print("\n1. Add Transaction")
            print("2. View All Transactions")
            print("3. View Balance")
            print("4. View Categorized Transactions")
            print("5. Exit")
            print("Categories - 1.Food 2.Travel 3.Fuel 4.Shopping 5.Bills & Misc")
    
            choice = input("Enter your choice: ")
    
            if choice == '1':
                amount = float(input("Enter amount: "))
                print("Select category:")
                for i, cat in enumerate(categories, 1):
                    print(f"{i}. {cat}")
                category_choice = int(input("Enter category choice (1-5): "))
                category = categories[category_choice - 1]
                transaction_type = input("Enter type (income/expense): ")
                date = input("Enter date (DD-MM-YYYY): ")
                comment = input("Enter comment: ")
                add_transaction(amount, category, transaction_type, date, comment)
            elif choice == '2':
                view_transactions()
            elif choice == '3':
                view_balance()
            elif choice == '4':
                category_choice = int(input("Enter category choice (1-5): "))
                category = categories[category_choice - 1]
                categorize_transactions(category)
            elif choice == '5':
                break
            else:
                print("Invalid choice")
    
        conn.close()
    
    if __name__ == "__main__":
        main()

from datetime import datetime
from typing import List, Dict
from decimal import Decimal, InvalidOperation
from pathlib import Path


class ExpenseManager:
    def __init__(self, username: str):
        self.username = username.lower()
        self.filename = Path("expense.txt")

    def add_expense(self, category: str, amount: float) -> None:
        """Add a new expense entry."""
        try:
            amount = Decimal(str(amount)).quantize(Decimal("0.01"))
            if amount <= 0:
                raise ValueError("Amount must be positive")
            
            expense_entry = {
                "user": self.username,
                "category": category.lower(),
                "amount": float(amount),
                "date": datetime.today().strftime('%Y-%m-%d')
            }
            
            self._write_expense(expense_entry)
            print(f"\n{category.capitalize()} expense added successfully!")
            self.show_category_summary(category)
            
        except (ValueError, InvalidOperation) as e:
            print(f"Error: Invalid amount - {str(e)}")
        except Exception as e:
            print(f"Error adding expense: {str(e)}")

    def _write_expense(self, expense_entry: Dict) -> None:
        """Write expense entry to file."""
        entry_line = f"{expense_entry['user']},{expense_entry['category']},{expense_entry['amount']},{expense_entry['date']}\n"
        
        try:
            with open(self.filename, "a") as file:
                file.write(entry_line)
        except Exception as e:
            print(f"Error writing to file: {str(e)}")
            raise

    def get_expenses(self) -> List[Dict]:
        """Get all expenses for the current user."""
        expenses = []
        try:
            if not self.filename.exists():
                return expenses

            with open(self.filename, "r") as file:
                for line in file:
                    user, category, amount, date = line.strip().split(",")
                    if user == self.username:
                        expenses.append({
                            "category": category,
                            "amount": float(amount),
                            "date": date
                        })
        except Exception as e:
            print(f"Error reading expenses: {str(e)}")
        
        return expenses

    def show_expenses(self) -> None:
        """Display all expenses and totals."""
        expenses = self.get_expenses()
        
        if not expenses:
            print("No expenses found.")
            return

        print(f"\nExpenses for {self.username.capitalize()}:")
        category_totals = {}
        total = Decimal("0")

        for expense in expenses:
            category = expense["category"]
            amount = Decimal(str(expense["amount"]))
            date = expense["date"]
            
            print(f"{category.capitalize()} Expense: ₹{amount} (Added on {date})")
            
            category_totals[category] = category_totals.get(category, Decimal("0")) + amount
            total += amount

        print("\nCategory Totals:")
        for category, amount in category_totals.items():
            print(f"{category.capitalize()}: ₹{amount}")
        
        print(f"\nTotal Expenses: ₹{total}")

    def show_category_summary(self, category: str) -> None:
        """Display summary for a specific category."""
        expenses = self.get_expenses()
        category = category.lower()
        
        category_expenses = [
            expense for expense in expenses 
            if expense["category"] == category
        ]
        
        if category_expenses:
            total = sum(Decimal(str(expense["amount"])) for expense in category_expenses)
            print(f"\nCategory Summary for {category.capitalize()}:")
            for expense in category_expenses:
                print(f"₹{expense['amount']} (Added on {expense['date']})")
            print(f"Category Total: ₹{total}")
        else:
            print(f"No expenses found for category: {category}")


def main():
    print("Welcome to Expense Tracker!")
    username = input("Enter your name: ").strip()
    
    if not username:
        print("Error: Username cannot be empty")
        return

    manager = ExpenseManager(username)
    
    while True:
        print("\nChoose an action:")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            category = input("Enter category: ").strip().lower()
            if not category:
                print("Error: Category cannot be empty")
                continue
                
            try:
                amount = float(input(f"Enter {category} expense amount: "))
                manager.add_expense(category, amount)
            except ValueError:
                print("Error: Please enter a valid number for amount")
                
        elif choice == "2":
            manager.show_expenses()
        elif choice == "3":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



            


    
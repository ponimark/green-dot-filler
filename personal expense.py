from datetime import datetime

class add:
    def __init__(self, u):
        self.u = u
        self.filename = "expense.txt"

    def expense(self, category):
        self.c = category
        z = eval(input(f"Enter {self.c} expense amount: "))
        today = datetime.today().strftime('%Y-%m-%d')

        updated_lines = []
        found = False

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        user, cat, amt, date = parts
                        if user == self.u and cat == self.c:
                            new_amt = float(amt) + z
                            updated_lines.append(f"{user},{cat},{new_amt},{today}\n")
                            found = True
                        else:
                            updated_lines.append(line)
                    else:
                        updated_lines.append(line)  # keep malformed lines just in case
        except FileNotFoundError:
            pass

        if not found:
            updated_lines.append(f"{self.u},{self.c},{z},{today}\n")

        with open(self.filename, "w") as file:
            file.writelines(updated_lines)

        print(f"\n{category.capitalize()} expense added!\n")
        self.show()

    def show(self):
        print(f"Expenses for {self.u.capitalize()}")
        total = 0
        cat_total = 0
        found = False

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        user, cat, amt, date = parts
                        if user == self.u:
                            amt = float(amt)
                            if hasattr(self, 'c') and cat == self.c:
                                print(f"{cat.capitalize()} Expense: {amt} (Added on {date})")
                                cat_total += amt
                                found = True
                            total += amt
        except FileNotFoundError:
            pass

        if found:
            print(f"{self.c.capitalize()} Total: ₹{cat_total}")
        if total > 0:
            print(f"Total for {self.u.capitalize()}: ₹{total}")
        elif not found:
            print("No expenses found.")

# ----------------------

u = input("Enter your name: ").lower()
user = add(u)

print("\nChoose an action:")
print("1. Add Expense")
print("2. Show Expense")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    cat_choice = input("Enter category: ").lower()
    user.expense(cat_choice)

elif choice == '2':
    user.show()
else:
    print("Invalid choice.")

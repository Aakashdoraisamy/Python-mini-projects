import csv
from datetime import datetime

FILENAME = "expenses.csv"

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    with open(FILENAME, "w", newline="") as f:
        fieldnames = ["date", "category", "amount", "note"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")
    expenses.append({"date": date, "category": category, "amount": amount, "note": note})
    print("Expense added!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nDate       | Category | Amount | Note")
    print("-"*40)
    for e in expenses:
        print(f"{e['date']} | {e['category']} | {e['amount']} | {e['note']}")

def view_by_category(expenses):
    category = input("Enter category: ")
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    if not filtered:
        print(f"No expenses found for {category}")
        return
    print(f"\nExpenses for {category}:")
    for e in filtered:
        print(f"{e['date']} | {e['amount']} | {e['note']}")
    total = sum(e["amount"] for e in filtered)
    print(f"Total: {total}")

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. View by Category\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

import json
from datetime import datetime

# Define the file to store expense data
EXPENSE_FILE = 'expenses.json'

# Load existing data from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

# Save data to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    amount = input("Enter the amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter the category (e.g., food, transportation, entertainment): ").strip().lower()
    description = input("Enter a brief description: ").strip()

    month = date.strftime("%Y-%m")
    if month not in expenses:
        expenses[month] = {}

    if category not in expenses[month]:
        expenses[month][category] = []

    expenses[month][category].append({"date": date_str, "amount": amount, "description": description})

    save_expenses(expenses)
    print(f"Expense added under {category} on {date_str}.")

# View monthly summary
def view_monthly_summary(expenses):
    month = input("Enter the month to view summary (YYYY-MM): ").strip()
    if month in expenses:
        print(f"\nSummary for {month}:")
        total = 0
        for category, items in expenses[month].items():
            category_total = sum(item["amount"] for item in items)
            total += category_total
            print(f"  {category.capitalize()}: {category_total}")
        print(f"Total: {total}\n")
    else:
        print("No expenses found for this month.")

# View category-wise expenditure
def view_category_summary(expenses):
    month = input("Enter the month (YYYY-MM): ").strip()
    category = input("Enter the category: ").strip().lower()

    if month in expenses and category in expenses[month]:
        print(f"\n{category.capitalize()} expenses in {month}:")
        total = 0
        for item in expenses[month][category]:
            print(f"  {item['date']}: {item['description']} - ${item['amount']}")
            total += item["amount"]
        print(f"Total spent on {category.capitalize()}: {total}\n")
    else:
        print(f"No expenses found for {category} in {month}.")

# Main user interface
def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_monthly_summary(expenses)
        elif choice == '3':
            view_category_summary(expenses)
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-4.")

if __name__ == "__main__":
    main()

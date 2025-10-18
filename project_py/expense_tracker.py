from expense import Expense
import os
from typing import List
import datetime
import calendar

def main():
    print("🚀Running Expense Tracker💸")
    budget =  20000

    # Get user input for expense.
    expense = get_user_expense()
    expense_file_path = "expenses.csv"

    # Write their expense csv file.
    write_expense_file(expense, expense_file_path)

    # Read and Summarize their expense.
    summarize_expense(expense_file_path, budget)


def get_user_expense():
    print("Getting User Expense ")
    expense_name = input("Enter Your Expense Name: ")
    expense_amount = float(input("Enter Your Expense Amount: "))
   
   # creating expense category in a list

    expense_categories = [
        "🏠 Rent",
        "🍽️  Food",
        "💊 Medical Bills",
        "💰 Savings",
        "🧾 Miscellaneous"
    ]    

    while True: 
        print("Select a category: ")

        for i, category_name in enumerate(expense_categories): # gives you both the index and the item in each iteration.
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]" # To enter user from the range of 1 to 5

        selected_index = int(input(f"Enter a Category Number {value_range}: ")) - 1 # -1 is to 0-based indexing in Python
      

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Enter a Valid Number")
        



def write_expense_file(expense, expense_file_name = "expenses.csv"):
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the full path inside project_py folder
    expense_file_path = os.path.join(current_dir, expense_file_name)

    print(f"Saving Your Expense File: {expense} to {expense_file_path} ")
    with open(expense_file_path, 'a', encoding='utf-8') as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")
    

def summarize_expense(expense_file_path, budget):
    print(f"🔍Summarizing Your Expense ")
    expenses: List[Expense] = [ ]
    current_dir = os.path.dirname(os.path.abspath(__file__)) # To save csv file in the same directory as same as other py. files
    expense_file_path = os.path.join(current_dir, "expenses.csv")
    with open(expense_file_path, "r", encoding="utf-8") as f: # "utf-8 --> Explicitly tell Python to read the file as UTF-8 (the same encoding you used when writing it)."
        lines = f.readlines()
        for line in lines:
            if not line.strip():
                continue  # skip empty lines
            parts = [x.strip() for x in line.strip().split(",")]
            if len(parts) != 3:
                print("⚠️ Skipping invalid line:", line.strip())
                continue

            expense_name, expense_category, expense_amount = parts

            line_expense = Expense(
                name=expense_name, category=expense_category, amount=expense_amount
            )
            
            expenses.append(line_expense)
    
    amount_by_category = { }

    for expense in expenses:
        key = expense.category # Use the category of the expense as the key for grouping/summing
        if key in amount_by_category:  # Check if this category already exists in the dictionary
            amount_by_category[key] += expense.amount # if the key exists it update to the existing value
        else: 
            amount_by_category[key] = expense.amount #If Not, initialize the category in the dictionary with this expense amount
    print("📊 Expenses by Category: ")

    for key, amount in amount_by_category.items():
        print(f"  {key: <20}:  ₹{amount: .2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"💸 Total Spent: ₹{total_spent: .2f}")

    remaining_budget = budget - total_spent
    print(f"🎯 Remaining budget: {remaining_budget: .2f}")

    # Get the current date
    now = datetime.datetime.now()

    #Get the no.of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate the remaining number of days in the current month

    remaining_days = days_in_month - now.day
    print("📅 Remaining Days in the current month: ", remaining_days)

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day:  ₹{daily_budget: .2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"




if __name__ == "__main__": # This condition checks whether the script is being run directly (not imported as a module into another script).
    main()
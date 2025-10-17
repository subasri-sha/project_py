from expense import Expense

def main():
    print("Running Expense Tracker! ")

    # Get user input for expense.
    expense = get_user_expense()
    print(expense)

    # Write their expense csv file.
    write_expense_file()

    # Read and Summarize their expense.
    summarize_expense()


def get_user_expense():
    print("Getting user expense ")
    expense_name = input("Enter your expense name: ")
    expense_amount = float(input("Enter your expense amount: "))
   
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

        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1 # -1 is to 0-based indexing in Python
      

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Enter a valid number")
        



def write_expense_file():
    print("Writing expense file")
    

def summarize_expense():
    print("Read and Summarize their expense")


if __name__ == "__main__": # This condition checks whether the script is being run directly (not imported as a module into another script).
    main()
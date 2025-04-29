import csv
import matplotlib.pyplot as plt
import pandas as pd

FILENAME = 'expenses.csv'

# Load data from CSV
def load_expenses(filename):
    try:
        data = pd.read_csv(filename)
        if 'Amount' in data.columns and 'Category' in data.columns:
            data['Category'] = data['Category'].str.strip().str.title()  # 🔥 important fix
            return data['Amount'], data['Category']
        else:
            print("CSV must contain 'Amount' and 'Category' columns.")
            return [], []
    except FileNotFoundError:
        print("Expenses file not found.")
        return [], []

# Add a new expense
def add_expense(filename, category, amount):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])
    print(f"✅ Added: {category} - ₹{amount}")

# Plot pie chart
def show_expenses(amounts, categories):
    import matplotlib.pyplot as plt
    import pandas as pd

    # Combine amounts and categories
    df = pd.DataFrame({'Category': categories, 'Amount': amounts})
    
    # 🔥 Group by Category and Sum
    grouped = df.groupby('Category').sum()

    # Plot
    plt.figure(figsize=(8, 8))
    plt.pie(grouped['Amount'], labels=grouped.index, autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.show()


# Main menu
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. View Pie Chart")
        print("2. Add Expense")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            categories, amounts = load_expenses(FILENAME)
            show_expenses(categories, amounts)
        elif choice == '2':
            category = input("Enter category: ")
            amount = input("Enter amount (in ₹): ")
            try:
                amount = float(amount)
                add_expense(FILENAME, category, amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == '__main__':
    main()

import os
from utility import *

def main():
    while True:
        os.system('cls')
        print("1. Category Registration")
        print("2. Show Categories")
        print("3. Edit Category")
        print("4. Transaction Registration")
        print("5. Show Transactions")
        print("6. Edit Transaction")
        print("7. Total Amount")
        print("8. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            os.system('cls')
            name = input("Enter category name: ")
            description = input("Enter category description: ")
            categoryReg(name, description)
        elif choice == 2:
            os.system('cls')
            showCategory()
        elif choice == 3:
            os.system('cls')
            id = int(input("Enter category id to edit: "))
            new_name = input("Enter new category name: ")
            new_description = input("Enter new category description: ")
            editCategory(id, new_name, new_description)
        elif choice == 4:
            os.system('cls')
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            print("Select a category from the list below:")
            with open('categoryList.txt', 'r') as f:
                for line in f:
                    print(line, end='')
            category_id = int(input("Enter the id of the category: "))
            category_name = ''
            category_description = ''
            with open('categoryList.txt', 'r') as f:
                for line in f:
                    category_data = line.split(' - ')
                    if len(category_data) > 1 and int(category_data[0]) == category_id:
                        category_name = category_data[1]
                        category_description = category_data[2].strip()
                        break
            category = Category(id=category_id, name=category_name, description=category_description)
            transactionReg(amount, description, category)
        elif choice == 5:
            os.system('cls')
            showTransaction()
        elif choice == 6:
            os.system('cls')
            id = int(input("Enter transaction id to edit: "))
            new_amount = float(input("Enter new amount: "))
            new_description = input("Enter new description: ")
            new_category = input("Enter new category: ")
            editTransaction(id, new_amount, new_description, new_category)
        elif choice == 7:
            os.system('cls')
            print(f"Total Amount: {totalAmount()}")
        elif choice == 8:
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid choice")
        input("Press any key to continue...")

if __name__ == "__main__":
    main()
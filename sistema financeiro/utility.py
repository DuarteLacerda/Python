import os
from category import Category
from transaction import Transaction
from random import randint


def categoryReg(name, description):
    newCategory = Category(id = randint(1,10), name = name, description= description)
    with open('categoryList.txt', 'a') as f:
        f.write(f'{newCategory.id} - {newCategory.name} - {newCategory.description}\n')
    return newCategory

def editCategory(id, new_name, new_description):
    with open('categoryList.txt', 'r') as f, open('categoryList_temp.txt', 'w') as f_temp:
        for line in f:
            category_data = line.split(' - ')
            if len(category_data) > 1 and float(category_data[0]) == id:
                f_temp.write(f'{id} - {new_name} - {new_description}\n')
            else:
                f_temp.write(line)
    os.replace('categoryList_temp.txt', 'categoryList.txt')

def showCategory():
    print("Category List")
    with open('categoryList.txt', 'r') as f:
        for line in f:
            print(line, end='')

def transactionReg(amount, description, category):   
    newTransaction = Transaction(id = randint(1,10), amount = amount, description = description, category = category)
    with open('transactionList.txt', 'a') as f:
        f.write(f'{newTransaction.id} - {newTransaction.amount} - {newTransaction.description} - {newTransaction.category.name}\n')
    return newTransaction

def editTransaction(id, new_amount, new_description, new_category):
    with open('transactionList.txt', 'r') as f, open('transactionList_temp.txt', 'w') as f_temp:
        for line in f:
            transaction_data = line.split(' - ')
            if len(transaction_data) > 1 and float(transaction_data[0]) == id:
                f_temp.write(f'{id} - {new_amount} - {new_description} - {new_category}\n')
            else:
                f_temp.write(line)
    os.replace('transactionList_temp.txt', 'transactionList.txt')

def showTransaction():
    print("Transaction List")
    with open('transactionList.txt', 'r') as f:
        for line in f:
            print(line, end='')

def totalAmount():
    total = 0
    with open('transactionList.txt', 'r') as f:
        for line in f:
            transaction_data = line.split(' - ')
            if len(transaction_data) > 1:
                total += float(transaction_data[1])
    return total
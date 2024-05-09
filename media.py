print('Media 1.0')

length = int(input("Enter the length of the list: "))
num = float(0)
total = float(0)
for i in range(length):
    num = float(input(f"Enter the number: "))
    total += num
print(f'The average of the numbers is: {total/length}')
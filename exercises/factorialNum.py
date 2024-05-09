num = input("Enter a number: ")
if num == 0:
    print("0! = 1")
else:
    factorial = 1
    for i in range(1, int(num) + 1):
        factorial *= i
    print(num + "! =", factorial)
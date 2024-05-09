print("Calculator 2.0")
print('Supported operators: +, -, *, /, %, **, //')
print('Sum: +,\nSubtraction: -,\nMultiplication: *,\nDivision: /,\nModulus: %,\nExponentiation: **,\nFloor division: //\n')
num1 = int(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))


match op:
    case "+":
        print('Result: ',num1 + num2)
    case "-":
        print('Result: ', num1 - num2)
    case "*":
        print('Result: ', num1 * num2)
    case "/":
        print('Result: ', num1 / num2)
    case "%":
        print('Result: ', num1 % num2)
    case "**":
        print('Result: ', num1 ** num2)
    case "//":
        print('Result: ', num1 // num2)
    case _:
        print("Invalid operator")
    

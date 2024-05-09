num = int(input("Enter a number: "))

def is_prime(num):
    res = False
    if num % 2 == 0:
        res = True
    else:
        res = False
            
    return res

if is_prime(num) == True:
    print(f"{num} is a par.")
else:
    print(f"{num} is not a par.")
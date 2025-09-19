num1 = int(input("pleae tell your first number : "))
num2 = int(input("pleae tell your second number : "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")

else:
    print("Both the numbers are same")
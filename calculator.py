#Simple Calculator in python
#Step1: Ask user to input the first number
#Step2: Ask user to input the second number
#Step3: Ask the user for arithmetic operations
#Step4: Perform and display all calculations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
addition_result = num1 + num2
minus_result = num1 - num2
multiplication_result = num1 * num2
division_result = num1 / num2

print(f"\nYou chose the operation: '{operation}' ")
print(f"Addition ({num1} + ({num2}): {addition_result}")
print(f"Minus ({num1} - {num2}): {minus_result}")
print(f"Multiplication ({num1} * {num2}): {multiplication_result}")
print(f"Division ({num1} / {num2}): {num1 / num2}")
print("\n----------")

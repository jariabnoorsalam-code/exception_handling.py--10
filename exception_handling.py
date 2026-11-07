# Program to Handle Exceptions Using Try-Except Blocks
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Program execution completed.")

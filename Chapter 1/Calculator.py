import time

Exit = False
while not Exit:
     time.sleep(1)
     print('''
Select the type of problem you want to solve:''')
     time.sleep(1)
     print("1. Addition")
     time.sleep(1)
     print("2. Subtraction")
     time.sleep(1)
     print("3. Multiplication")
     time.sleep(1)
     print("4. Division")
     time.sleep(1)
     print("5. Exponentiation")
     time.sleep(1)
     print("6. Exit")
     time.sleep(1)
     choice = input("Enter your choice (1-6): ")
     
     if choice == '6':
         Exit = True
         time.sleep(1)
         print("Exiting the Calculator Program. Goodbye!")
     else:
            Problem = choice

            if Problem == '1':
                time.sleep(1)
                num1 = int(input("Enter first number: "))
                time.sleep(1)
                num2 = int(input("Enter second number: "))
                result = num1 + num2
                time.sleep(1)
                print(f"The result of {num1} + {num2} is: {result}")
            elif Problem == '2':
                time.sleep(1)
                num1 = int(input("Enter first number: "))
                time.sleep(1)
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")        
            elif Problem == '3':
                time.sleep(1)
                num1 = int(input("Enter first number: "))
                time.sleep(1)
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif Problem == '4':
                time.sleep(1)
                num1 = int(input("Enter first number: "))
                time.sleep(1)
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
                else:
                    time.sleep(1)
                    print("Error: Division by zero is not allowed.")
            elif Problem == '5':
                time.sleep(1)
                base = int(input("Enter the base number: "))
                time.sleep(1)
                exponent = int(input("Enter the exponent number: "))
                time.sleep(1)
                result = base ** exponent
                print(f"The result of {base} raised to the power of {exponent} is: {result}")
            else:
                time.sleep(1)
                print("Invalid input. Please select a valid problem type (1-5).")
                



print("Select an operation to perform:")
print("1, ADD")
print("2, SUBTRACT")
print("3, MUTLIPLY")
print("4, DIVIDE")
print("5, SQUARE ROOT")
print("6, POWER")

operation = input()

if operation == "1": #ADDITION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2": #SUBTRACTION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "3": #MULTIPLICATION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "4": #DIVISION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) / int(num2)))
elif operation == "5": #SQUARE ROOT
    num = int(input("Enter first number: "))
    print("The square root is %f " %(math.sqrt(num)))
elif operation == "6": #SQUARE A NUMBER
    num = int(input("Enter first number: "))
    power = int(input("Enter the number you want to raise the power to: "))
    
    print("The result is %d " %(pow(num, power)))
else:
    print("Invalid Entry")
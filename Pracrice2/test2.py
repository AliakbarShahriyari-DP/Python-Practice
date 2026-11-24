
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# match operator:

#     case "+":
#         result = num1 + num2

#     case "-":
#         result = num1 - num2

#     case "*":
#         result = num1 * num2

#     case "/":
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             print("Error: Cannot divide by zero")

#     case _:
#         print("Invalid operator")  

# if operator in ["+", "-", "*", "/"] and num2 != 0 or operator != "/":
#     if result == int(result):
#         print("Result:", int(result))
#     else:
#         print("Result:", result)
# else:
#     print("Result:", result)


# Second Way...


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2 if num2 != 0 else "Cannot divide by zero(0).."
}

result = operations.get(operator, "Error.Invalid operator")

if result == int(result):
    print("Result:", int(result))
else:
    print("Result:", result)
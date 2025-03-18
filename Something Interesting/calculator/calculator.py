print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opr = input("Enter operation (1,2,3,4) : ")

if opr == "1":
    print(num1, "+", num2, "=", num1 + num2)
elif opr == "2":
    print(num1, "-", num2, "=", num1 - num2)
elif opr == "3":
    print(num1, "*", num2, "=", num1 * num2)
elif opr == "4":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid operation")


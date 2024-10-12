# define the functions needed: add, sub, mul, div
# print the options to the user
#ask for values
#call the functions
#while loop to continue the program until the user wants to exit
def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")
    
def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")
    
def mul(a, b):
    answer = a * b
    print(f"{a} x {b} = {answer}")
    
def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")
    
while True:
    print("A. addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. division")
    print("E. exit")

    choice = input("input your choice: ").upper()

    if choice == "A":
        print("Addition")
        a = int(input("enter the first number: "))
        b = int(input("enter the second number: "))
        add(a, b)
    elif choice == "B":
        print("Subtraction")
        a = int(input("enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a, b)
    elif choice == "C":
        print("Multiplication")
        a = int(input("enter the first number: "))
        b = int(input("Enter the second number: "))
        mul(a, b)
    elif choice == "D":
        print("Division")
        a = int(input("enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a, b)
    elif choice == "E":
        print("Program ended!!")
        quit()
    else:
        print("enter a valid  choice: ")
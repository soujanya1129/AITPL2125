#menu driven program to perform arithmetic operations using functions
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
print("""Please select operation """ \
      """1. Add """ \
      """2. Subtract """ \
      """3. Multiply """ \
      """4. Divide """)
select = int(input("Select operations form 1, 2, 3, 4 :"))
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
if select == 1:
    print(num_1, "+", num_2, "=",
          add(num_1, num_2))
elif select == 2:
    print(num_1, "-", num_2, "=",
          subtract(num_1, num_2))
elif select == 3:
    print(num_1, "*", num_2, "=",
          multiply(num_1, num_2))
elif select == 4:
    print(num_1, "/", num_2, "=",
          divide(num_1, num_2))
else:
    print("Invalid input")
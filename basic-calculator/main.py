from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  should_continue = True

  while should_continue:
    for operation in operations:
      print(operation)

    operation = input("Pick an operation: ")

    num2 = float(input("What's the next number?: "))

    calc_function = operations[operation]
    result = calc_function(num1, num2)

    print(f"{num1} {operation} {num2} = {result}")

    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation.: ").lower()

    if choice == 'n':
      should_continue = False
      calculator()
    else:
      num1 = result

calculator()

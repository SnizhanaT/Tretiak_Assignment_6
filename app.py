import sys


def add(a, b):
   """Adds two numbers A and B."""
   return a + b


def subtract(a, b):
   """Subtracts number B from A."""
   return a - b


if __name__ == '__main__':
   if len(sys.argv) < 4:
       print("Usage: python app.py [add|subtract] num1 num2")
       sys.exit(1)


   operation = sys.argv[1]
   a = float(sys.argv[2])
   b = float(sys.argv[3])


   if operation == 'add':
       result = add(a, b)
       print(f'{a} + {b} = {result}')
   elif operation == 'subtract':
       result = subtract(a, b)
       print(f'{a} - {b} = {result}')
   else:
       print("Unknown operation. Use 'add' or 'subtract'.")




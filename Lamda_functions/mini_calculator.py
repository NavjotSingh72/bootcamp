def operators(op):
      if op == '+':
         return lambda x, y: x + y
      elif op == '-':
         return lambda x, y: x - y
      elif op == '*':
         return lambda x, y: x * y
      elif op == '/':
         return lambda x, y: x / y
      else:
         raise ValueError('Invalid operator')
      

add = operators('+')
subtract = operators('-')
multiply = operators('*')
divide = operators('/')

input1 = float(input("Enter an num1: "))
input2 = float(input("Enter an num2: "))
op = input("Enter an operator (+, -, *, /): ")

result = operators(op)(input1, input2)
print(result)
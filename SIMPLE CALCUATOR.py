a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter (+,-,*,/): ")
if operation == '+':
   result = a+b
elif operation == '-':
   result = a-b
elif operation == '*':
   result = a*b
elif operation == '/':
  if (b!=0):
   result = a/b
  else: 
   result = "Invalid division"
else:
   result = "Invalid operation"
print("Result: ",result)
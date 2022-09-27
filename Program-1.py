class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = Calculator(a, b)
result = ""
operation = input("Enter type of operation: ")
if operation == "addition":
    result = obj.addition()
elif operation == "subtraction":
    result = obj.subtraction()
elif operation == "multiplication":
    result = obj.multiplication()
else:
    result = obj.division()
output = "The {} of {} and {} equals to {}."
print(output.format(operation, a, b, result))
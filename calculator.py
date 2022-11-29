var1 = float(input("Write first variable: "))
var2 = float(input("Write second variable: "))
operator = input("What are you want? (+, -, *, /) ")
if operator == "+":
    print(var1 + var2)
elif operator == "-":
    print(var1 - var2)    
elif operator == "*":
    print(var1 * var2)
elif operator == "/":
    print(var1 / var2)
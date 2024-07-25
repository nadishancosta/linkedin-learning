def calculate(num1,num2,op):
    if op=="+":
        return num1+num2
    elif op=="/":
        return num1/num2
    elif op=="*":
        return num1*num2
    elif op=="-":
        return num1-num2
    else:
        return 0

num1 = float(input("Enter the first number pls: "))
op = input("Please enter the operator: ")
num2 = float(input("Enter the second number pls: "))
print("The answer is: "+ str(calculate(num1,num2,op)))


try:
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    opertor = input("Enter a opertor for calculation like '+, -, *,/'")
    
    if opertor == "+":
        print("Result",num1 + num2)
        
    elif opertor == "-":
        print("Result",num1 - num2)
    
    elif opertor == "*":
        print("Result",num1 * num2)
        
    elif opertor == "/":
        if num2 == 0:
            print("Number cannot divisble by Zero")
        else:
            print("Result",num1 / num2)
    
    else:
        print("only opertors are aloowed like '+, -, *,/'")

except ValueError:
    print("Only numbers are accepted")

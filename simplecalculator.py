#Simple calculator
print("----------------simple calculator--------------")
print("0.Quit")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.square")
print("6.cube")
print("7.Factorial")
print("8.Square root")
while True:
    choice=int(input("Choose a operation:"))
    if choice==1:
        a=int(input("Enter a number:"))
        b=int(input("Enter second number:"))
        print("Addition of two number:",a+b)
    elif choice==2:
        a=int(input("Enter a number:"))
        b=int(input("Enter second number:"))
        print("Subtraction of two number:",a-b)
    elif choice==3:
        a=int(input("Enter a number:"))
        b=int(input("Enter second number:"))
        print("Multiplcation of two number:",a*b)
    elif choice==4:
        try:
            a=int(input("Enter a number:"))
            b=int(input("Enter second number:"))
            print("Division of two number:",a//b,"remainder:",a%b)
        except:
            print("You cannot divide by zero")
    elif choice==5:
        a=int(input("Enter a number:"))
        print("Square of number:",a**2)
    elif choice==6:
        a=int(input("Enter a number:"))
        print("Cube of number:",a**3)
    elif choice==7:
        a=int(input("Enter a number:"))
        tem=a
        if a==0 or a==1:
            n=1
            print("Factorial of",a,"is",n)
        else:
            for i in range(2,a):
                a=a*i
            print("Factorial of ",tem,"is",a)
    elif choice==8:
        a=int(input("Enter a number:"))
        print("Square root of",a,"is",a**0.5)
    elif choice==0:
        break
    else:
        print("Invalid choice")

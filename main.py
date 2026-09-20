"""
add, sub,multi,divide,mod,pow,exit
"""
def add(x,y):
    sum=x+y
    print(f"sum of {x} and {y}= {sum}")
def sub(x,y):
    d=x-y
    print(f"difference of {x} and {y}= {d}")
def product(x,y):       
    p=x*y
    print(f"product of {x} and {y}= {p}")
def divide(x,y):
    try:
        q = x / y
        print(f"division of {x} and {y} = {q}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
def mod(x,y):
    try:
        r = x % y 
        print(f"remainder of {x} and {y} = {r}") 
    except ZeroDivisionError:
        print("Error: Cannot find remainder with zero.")
def power(x,y):
    e=x**y
    print(f"power of {x} to {y}= {e}")
n=0
while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        break 
    except ValueError:
        print("Error: Please enter numbers only.")
while(n!=7):
    try:
        n = int(input( "\nEnter " 
        "\n1. Addition" 
        "\n2. Subtraction" 
        "\n3. Product" 
        "\n4. Division" 
        "\n5. Finding remainder" 
        "\n6. Power" 
        "\n7. Exit" 
        "\n" ))
        if n==1:
            add(a,b)
            
        elif n==2:
                sub(a,b)
                
        elif n==3:
                product(a,b)
                
        elif n==4:
                divide(a,b)
                
        elif n==5:
            mod(a,b)
                            
        elif n==6:
                power(a,b)
        elif n==7:
            print("program exited")
        else:
            print("Invalid choice! Please enter 1 to 7.") 
    except ValueError:
        print("Error: Please enter numbers only.")
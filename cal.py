def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def divide(x,y):
    return x/y

print("select your option")
print("1")
print("2")
print("3")

while True:
    choice=input("choose 1 , 2 , 3 ")

if choice in ("1" , "2 " , "3"):
    try:
        num1=float(input("enter first number"))
        num2=float(input("enter second number"))
    except ValueError:
        print("invalid choice")
     




if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
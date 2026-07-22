# If is used to check the condition,if condition is true, the block under the staement is executed.
x=11
if (x%2==0):
    print("Even")
else:
    print("Odd")

signal="go"
if (signal=="Red"):
    print("Stop")
elif (signal=="Yellow"):
    print("Get ready")
else:
    print("Go")

gender="female"
age=25
if gender=="female":
    print("Ticket is free")
else:
    if age<5:
        print("Ticket is free")
    elif age<=12:
        print("You get a child discount")
    elif age>=60:
        print("You get a senior citizen discount")
    else:
        print("You need to pay full fare.")

#Q1 Positive, Negative or Zero
num=int(input("Enter a number: "))
if (num>0):
    print("Positive Number")
elif(num<0):
    print("Negative Number")
else:
    print("Zero")

#Q2 Student Grade
marks=int(input("Enter your marks: "))
if(90<=marks<=100):
    print("Grade A")
elif(80<=marks<=89):
    print("Grade B")
elif(70<=marks<=79):
    print("Grade C")
elif(60<=marks<=69):
    print("Grade D")
else:
    print("Fail")

#Q3 Largest of three numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if (a>b and a>c):
    print("a is largest",a)
elif(b>a and b>c):
    print("b is largest",b)
else:
    print("c is largest",c)

#Q4 Electricity bill
unit=int(input("Enter number of units consumed: "))
if unit <= 100:
    bill = unit * 2
elif unit <= 200:
    bill = unit * 4
else:
    bill = unit * 6

print("Total Bill:", bill)

#Q5 Simple Login system
username="Geetha"
password="python123"
user=input("Enter a username: ")
paswod=input("Enter a password: ")
if (user==username and paswod==password):
    print("Login Successful")
elif(user!=username):
    print("Invalid username")
else:
    print("Invalid Password")

age=int(input("Enter your age: "))
if (age<13):
    print("Child")
elif(13<=age<=19):
    print("Teenager")
elif(20<=age<=59):
    print("Adult")
else:
    print("Senior Citizen")
#Function is a reusable block of code that performs specific task.
def greet():
    print("Hello, Good morning")
greet()
greet()
greet()
greet()
greet()

def marriage(boy,girl):
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")
marriage("Chandan","Chandana")

#Q1
def greet():
    print("Hello, Welcome to Python!")
greet()

#Q2
def function(name):
    print(f"Hello {name}")
function("Geetha")

#Q3
def add(a,b):
    print("Sum: ",a+b)
add(10,20)

#Q4
def square(num):
    print(num**2)
square(6)

#Q5
def message(msg):
    print(f"Your message is: {msg}")
message("Good Morning")

#Q6
def multiply(a,b):
    print(a*b)
multiply(2,3)

#Q7
def even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
even_odd(5)
even_odd(6)

#Q8
def largest(a,b):
    if a>b:
        print(a)
    else:
        print(b)
largest(15,8)

#Q9
def repeat(word):
    for i in range(3):
        print(word)

repeat("Python")

#Q10
def table(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
table(5)
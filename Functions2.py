#*args and **kwargs used to accept variable number of arguments
def add(*a):
    print(a)
    print(type(a))
add(1,2,3,4)

def add(*numbers):
    return sum(numbers)
print(add(1,2))

def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
student_info(name="Geetha",age=20,course="")

double=lambda x:x*2
print(double(5))

def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
print(student_info(name="Veda",age=8))

#Recursion=Function calls itself
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))

def greet(name):
    print(f"Hello, {name}! Welcome to Python")
greet("Geetha")

def find_sum(*numbers):
    return sum(numbers)
print(find_sum(10,20,30,40))

def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
student_info(name="Veda",age=8,city="Banglore")

number=lambda x:x**3
print(number(3))

def print_numbers(n):
    if n==1:
        print(1)
    else:
        print_numbers(n-1)
        print(n)

print(print_numbers(5))
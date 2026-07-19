#Variables

a=10 #int
b=20
name="Geetha" #string
print(a)
print("a")
print(a+b)
x=y=z=50
print(x)

#Data Types

print(f"I am {name}")
print(type(a))
weight=45.6 #float
is_Employee=True #bool
print(type(name))
print(type(weight))
print(type(is_Employee))

is_Employee="Yes" #String
print(type(is_Employee))

#Type Conversion

x="20"
x=float(x)
print(x)

a=5
a=str(a)
print(type(a))

#Arithmetic Operations
x=10
y=5
print(x+y) #addition
print(x-y) #Subtraction
print(x*y) #Multiplication
print(x/y) #Division
print(x//y) #Floor division(Gives exact answer)
print(x**2) #Exponentiation 

#Questions
#Tye
name="Geetha"
print("Name: ",name)
print(type(name))
age=20
print("Age: ",age)
print(type(age))
height=5.4
print("Height: ",height)
print(type(height))
student=True
print("Student: ",student)
print(type(student))

#Finding Area
length=int(input("Enter a length: "))
breadth=int(input("Enter a breadth: "))
Area=length*breadth
print(Area)  

#Converting celsius to fahrenheit
c=float(input("Enter a temperatur in celcius: "))
F=(c*9/5)+32
print(F)


#Even or odd
x=int(input("Enter a number: "))
if x%2==0:
  print(f"{x} is Even")
else:
  print(f"{x} is Odd") 

#Exponents
base=int(input("Enter a base: "))
exponent=int(input("Enter a exponent: "))
Answer=base**exponent
print(Answer)

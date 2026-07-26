#Q1
print("Welcome to Python")

#Q2
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"My name is {name}")
print(f"I am {age} years old")

#Q3
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

#Q4
number=int(input("Enter a number: "))
if number%2==0:
    print("Even")
else:
    print("Odd")
    
#Q5
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")
    
#Q6
text="Python Programming" 
print(text[0])
print(text[-1])
print(len(text))
print(text.upper())

#Q7
vowels=['a','e','i','o','u']
string="Geetha"
count=0
for letter in string:
    if letter in vowels:
        count=count+1
print(count)

#Q8
word=input("Enter a word: ")

#Q9
numbers=[5,10,15,20,25]
sum=0
for i in numbers:
    sum=sum+i
print("Sum: ",sum)

#Q10
numbers=[12,5,18,7,20,15]
for i in numbers:
    if i%2==0:
        print(i)

#Q11
numbers=[10,20,10,30,40,20]
set={num for num in numbers}
print(set)

#Q12
fruits=("Apple","Mango","Banana","Orange")
for i in fruits:
    print(i)

#Q13
student={
    "Name":"Geetha",
    "Age":20,
    "Course":"CSE"
}
print(student.keys())

#Q14
student={
    "Name":"Geetha",
    "Age":20,
    "Course":"CSE"
}
print(student.values())

#Q15
marks={
    "Ram":85,
    "Sita":95,
    "John":45,
    "Anu":60
}
for student,mark in marks.items():
    print(student, mark)
        
#Q16
for i in range(1,21):
    if i%4==0:
        continue
    print(i)

#Q17
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
    
#Q18
for i in range(2,6):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")

#Q19
list=[1,8,27,64,125,216,343,512,729,1000]
cubes=[i**3 for i in range(1,11)]
print(cubes)

#Q20
numbers=[1,2,3,4,5,6,7,8,9,10]
dictionary={i:i*2 for i in range(1,11)}
print(dictionary)

#Q21
i=1
while i<=30:
    if i%3==0:
        print("Fizz")
    else:
        print(i)
    i=i+1

#Q22
numbers=[12,25,8,17,30,45,50]
even_count=0
odd_count=0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers: ",even_count)
print("Odd numbers: ",odd_count)


#Q23
numbers=[1,2,3,4,5,6,7,8,9,10]
list=[num**3 for num in numbers if num%2!=0]
print(list)

#Q24
marks={
    "Ram":85,
    "Sita":42,
    "John":76,
    "Anu":35,
    "Ravi":91
}
dictionary={student:mark for student,mark in marks.items() if mark>=50}
print(dictionary)
 
#Q25
marks={
    "Ram":85,
    "Sita":42,
    "John":76,
    "Anu":35,
    "Ravi":91
}
topper=""
highest=0
for student,mark in marks.items():
        if mark>highest:
            highest=mark
            topper=student
print("Topper: ",topper)
print("Marks: ",highest)

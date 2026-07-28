#Homework Day1
name="Geetha"
print(f"Namasthe, nanna hesaru {name}")

a,b=10,20
a=a+b
b=a-b
a=a-b
print(a)
print(b)

name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")

sentence=input("Enter a sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","-"))
print(sentence.strip())

print("Hello\n\tworld\nThis is a backslash")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a>10 and b>10)

list=["Coffee","Tea","Milk","Biscuit","Bred"]
list.append("Glucose")
list.insert(2,"Horlicks")
print(list)
list.pop(1)
print(list)

numbers=[1,4,7,2,5,8]
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)

#Q1
i=1
while(i<=25):
    if(i%2!=0):
        print(i)
    i+=1
    
#Q2
i=1
sum=0
while(i<=10):
    sum=sum+i
    i+=1
print("Sum: ",sum)

#Q3
numbers=[12,5,18,9,20,7,30]
for i in numbers:
    if(i>10):
        print(i)
    i=i+1

#Q4
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
    
#Q5
numbers=[15,8,23,42,7,18]
count=0
for i in numbers:
    if(i>20):
        count=count+1
    i=i+1
print("Count: ",count)

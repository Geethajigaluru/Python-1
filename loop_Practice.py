#List comprehension
l=[1,23,45,67,21]
total=0
for i in l:
    total=total+i
print(total)

s=[23,56,7,26,98]
dl=[]
for num in s:
    dl.append(s)
    print(dl)

student_marks={"Veda":100,"Geetha":99,"Kavya":98}
for students in student_marks.items():
    print(students)

students=["Veda","Geetha","Kavya"]
marks=[100,98,99]
student_marks={}
for index,student in enumerate(students):
    student_marks[student]=marks[index]
print(student_marks)

students1=["Chinni","Geetha","Kavya"]
marks=[90,37,68]
student_marks={}
for i in range(0,len(students1)):
    student_marks[students1[i]]=marks[i]
print(student_marks)

l=[1,2,3,4,5]
dl=[item*2 for item in l]
print(dl)

x=[1,2,3,4,5,6,7,8]
print(x)
edl=[s**2 for s in x if s%2==0]
print(edl)

names=["Geetha","Veda","Kavya"]
students=[letters[1] for letters in names]
print(students)

names1=["Anand","Geetha","Kumar"]
d={item:len(item) for item in names1}
print(d)

cities=["Banglore","Mysore","Gadag","Dharwad","Koppala"]
villages={city:len(city) for city in cities}
print(villages)

city_population={"Bengaluru":84, "Mysore":11,"Hubballi":9,"Mangaluru":5}
large_cities={key:value for key,value in city_population.items() if value>10}
print(large_cities)

print("List input practice")
x=input("Enter list of integers: ")
print(x.split())

#Q1
numbers=[12,5,8,17,20,25,30]
even=[num for num in numbers if num%2==0]
print(even)

#Q2
numbers=[5,10,15,20]
sum=0
for i in numbers:
    sum=sum+i
print("sum: ",sum)

#Q3
letters=['a','b','e','f','i','o','u','x']
vowels=['a','e','i','o','u']
count=0
for letter in letters:
    if letter in vowels:
        count=count+1
print(count)

#Q5
numbers=[1,2,3,4,5,6,7,8,9,10]
squares=[num**2 for num in numbers]
print(squares)

#Q6
numbers=[3,8,11,14,17,20,25]
count=0
for i in numbers:
    if i%2!=0:
        count=count+1
print(count)

#Q7
numbers = [12,45,8,90,23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)
    
#Q8
numbers=[10,15,22,31,44,57]
odd_numbers=[num for num in numbers if num%2!=0]
print(odd_numbers)

#Q9
marks={"Ram":75,
       "Sita":90,
       "John":45,
       "Anu":60
       }
pass_marks={student:marks for student,marks in marks.items() if marks>=50}
print(pass_marks)

#Q10
marks={
    "Ram":75,
    "Sita":90,
    "John":45,
    "Anu":60
}
pass_marks={student:marks for student,marks in marks.items() if marks>=50}
print(pass_marks)

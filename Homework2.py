dishes={
    "Banglore":"Bisi ble Bath",
    "Mysore":"Mysore Pak",
    "Mangaluru":"Neer dosa",
    "Mandya":"Ragi mudde",
    "Udupi":"Meenu"
}
#Adding
dishes["Chikkamagaluru"]="Coffee"
print(dishes)
#updating
dishes["Banglore"]="Uppittu"
print(dishes)
#removing
del dishes["Udupi"]
print(dishes)
print(dishes.keys())

d={
    "friend_1":{
        "name":"Veda",
        "subject":"Science",
        "Class":"2nd"
    },
    "friend_2": {
        "name":"Geetha",
        "subject":"Maths",
        "class":"15th"
    }
}
print(d["friend_1"]["subject"])
print(d["friend_2"]["class"])

i = 1
while(i<=10):
    print(i)
    i=i+1
    
seats=8
while(seats>0):
    print("Book one seat")
    seats=seats-1
    print("Remaining seats: ",seats)
print("All seats are booked")

import time
i=10
while(i>0):
    print("Count down: ",i)
    time.sleep(1)
    i=i-1
    if(i==0):
        print("Happy new year!!")

sum=0
i=1
for i in range(1,11):
    sum=sum+i
print(sum)

vowels="aeiou"
name="Geetha"
count=0
for i in name:
    if i in vowels:
        count=count+1
print("Count: ",count)

foods=["Idli","Dosa","poori"]
dish_food=[i.upper() for i in foods]
print(dish_food)

items={
    "pen":10,
    "pencil":5,
    "paper":20,
    "Eraser":5,
    "sharpner":5
}
total=0
for key,value in items.items():
    total=total+value
print(total)

l=[num**2 for num in range(1,11)]
print(l)

rows=int(input("Enter number of rows: "))
matrix=[]
for i in range(rows):
    x=[int(num) for num in input(f"Enter row{i+1}: ").split()]
print(matrix)

#Q1
numbers=[2,5,2,8,10,5,12,8,14]
l=set(numbers)
print(l)
for i in l:
    if i%2==0:
        print(i,end=" ")
new_list=[num**2 for num in l if num%2==0] 
print(new_list)

#Q2
text=input("Enter a string: ")

count={}

for ch in text:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1

print(count)
#Q3
table={i:i*7 for i in range(1,11)}

print(table)

#Q4
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

#Q5
students={
    "Asha":85,
    "Rahul":42,
    "Sneha":91,
    "Kiran":65,
    "Priya":38
}
passed = {student: marks for student, marks in students.items() if marks >= 50}

print(passed)
average = sum(passed.values()) / len(passed)
print("Average:", average)
topper = max(students, key=students.get)
print("Topper:", topper, students[topper])
# Lists is a collection of items which are ordered mutable and allows duplicate elements.
Lists=["Geetha","Veda","Kavya","Abhi","Ashwini"]
print(Lists)

#Q1
Fruits=['Apple','Banana','Mango','Orange','Grapes']
print("Fruits: ",Fruits)
print("First fruit: ",Fruits[0])
print("Last fruit: ",Fruits[-1])
print("Total fruits: ",len(Fruits))

#Q2 
colors=["Red","Blue","Green"]
colors.append("Yellow")
colors.insert(1,"Black")
print(colors)

#Q3
animals=["Dog","Cat","Lion","Tiger","Elephant"]
animals.remove("Lion")
animals.pop()
print(animals)

#Q4
numbers=[10,20,30,40,50,60]
print(numbers[0:3])
print(numbers[-3:])
numbers.reverse()
print(numbers)

#Q5
marks=[96,75,89,92,68]
print(marks)
print("Maximum marks: ",max(marks))
print("Minimum marks: ",min(marks))
print("Total number of marks: ",len(marks))


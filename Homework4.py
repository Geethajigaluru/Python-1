#Q1
def second_largest(numbers):
    unique_numbers=list(set(numbers))
    if len(unique_numbers)<2:
        print("no second largest element")
    unique_numbers.sort()
    return unique_numbers[-2]
print(second_largest([10,30,20,20,50,40]))

#Q2
t=(10,20,30,40,50)
tuple=tuple(num for num in t if num>=25)
print(tuple)

#Q3
student={
    "name":"Geetha",
    "marks":[85,90,95]
}
total=sum(student["marks"])
count=len(student["marks"])
average=total/count
print("Average: ",average)

#Q4
sum=0
while True:
    n=int(input("Enter a number: "))
    if n==0:
        break
    sum=sum+n
print("Total sum: ",sum)

#Q5
for i in range(1,7):
    for j in range(1,i):
        print(j,end="")
    print()
#Q6
def count_even(numbers):
    count=0
    for i in numbers:
        if i%2==0:
            count=count+1
    return count
print(count_even([2,5,8,9,10]))

#Q6
marks={
    "A":85,
    "B":92,
    "C":78,
    "D":96
}
highest=0
highest_key=""
for key,value in marks.items():
    if value>highest:
        highest=value
        highest_key=key
print(highest_key)

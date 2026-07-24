#for loop is used to repeat a block of code at fixed number of times or once for each element in a sequence.
cities=["Bengaluru","mysore","Mandya","Gadag","Dharwad"]
for city in cities:
    print(city)

for i in range(1,11):
    
    # To print in one line use end
    print(i,end=" ")

bag=["red","Blue","Pink"]
for color in bag:
    print(color, end=" ")

for i in range(1,11,2):
    print(i, end=" ")

name="Geetha"
for letter in name:
    print(letter)
    print(letter*5,end=" ")

name="Veda"
for letter in enumerate(name):
    print(letter*5)

name1="Geetha"
for index,letter in enumerate(name1):
    print(letter*(index+1))
    print(f"{letter} is in {index} th index.")

d={"name":"Geetha","Age":20,"college":"Garden city university"}
for key,value in d.items():
    print(key," ",value)
    
for i in range(2,11):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
        
#Q1 
for i in range(1,21):
    print(i)
    
#Q2
for i in range(20,0,-1):
    print(i)
    
#Q3 
for i in range(1,50,2):
    print(i)
    
#Q4 
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")
    
#Q5
sum=0
for i in range(1,101):
    sum=sum+i
print("sum: ",sum) 

#Q6
for i in range(2,6):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}") 

#Q7
for i in range(5):
    for j in range(5):
        print("*",end="")
    print() 

#Q8
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
    
#Q9
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
    
#Q 10
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

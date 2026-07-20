'''
#Tuples are ordered, unchangeable and allows duplicate elements.
tuple=("Cherry","Orange","Grapes")
print(tuple)
t=(1,)*3
print(t)

print(tuple[1:3])
print("apple" in tuple)
tuple1=("Kavya","Geetha","Veda")
tuple2=("Abhishek","Ashwini")
tuples=tuple1+tuple2
print(tuples)

t1=(1,6,4,2,1,8,7,5)
print(t1.count(1))
print(t1.index(4))
'''

#Q1
Tuple=("Python","Java","C","C++")
print(Tuple)
print(Tuple[0])
print(Tuple[2])
print(Tuple[-1])

#Q2
numbers=(10,20,30,40,50,60)
print(numbers[0:3])
print(numbers[-2:])
print(numbers[::-1])

#Q3
fruits=("Apple","Banana","Mango","Apple","Orange")
print(fruits.count("Apple"))
print(fruits.index("Mango"))

#Q4
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=tuple1+tuple2
print(tuple3)

#Q5
colors=("Red","Blue","Green")
if ("Blue"in colors):{
    print("Blue is present")
}
else:{
    print("Blue is not present")
}

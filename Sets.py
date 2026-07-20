# Sets is a collection of unique elements, unordered, unindexed and does not allow duplicate elements.
Set={"Television","Refrigerator","Washing machine","Scooty","Chair"}
print(Set)

#union | (Combines all elements from both sets and removes duplicates)
Set1={1,4,6,3}
Set2={2,3,6,7}
Set3=Set1|Set2
print(Set3)

#intersection & (Returns elements that are common in both sets)
Set4=Set1&Set2
print(Set4)

#difference - (Returns elements that are in first set but not in the second set)
Set5=Set1-Set2
print(Set5)

#Symmetric difference ^ (Returns elements that are in either of the set but not in both)
Set6=Set1^Set2
print(Set6)

#Adding an element
Set.add("Door")
print(Set)

# Remove() -Removes an element but it raises error if not found
Set.remove("Television")
print(Set)

# discard() - Removes an elements and not raises an error
Set.discard("Kurchi")
print(Set)

#Q1 
set={"Red","Blue","Green","Yellow"}
print(set)

#Q2
animals={"Dog","Cat","Lion"}
animals.add("Tiger")
print(animals)
animals.remove("Cat")
print(animals)

#Q3
set1={1,2,3}
set2={3,4,5}
sets=set1|set2
print(sets)

#Q4
set1={1,2,3}
set2={3,4,5}
sets1=set1&set2
print(sets1)

#Q5
fruits={"Apple","Banana","Mango"}
if "Banana" in fruits:
    print("Banana found")
else:
    print("Banana not found")
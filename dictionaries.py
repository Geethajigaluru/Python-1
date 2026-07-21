# dictionary is a collection of key value pairs.
# dictionaries are unordered an changeable.
# We can create dictionaries using {} brackets.
birthday={
    "Geetha":"17-01-2006",
    "Veda":"28-10-2018",
    "Kavya":"27-07-2003"
}
print(birthday)

Karnataka_Food={
    "Banglore":"Masaladosa",
    "Mysore":"Mysore Pak",
    "Gadag":"Jolada Rotti",
    "Mandya":"Mudde",
    "Ramanagara":"Reshme"
}
print(Karnataka_Food)

#we can access elements using keys.
print(Karnataka_Food["Mysore"])
print(type(Karnataka_Food))
#We can also use get() to access values and it doesn't throw an error.

print(Karnataka_Food.get("Gadag"))
print(Karnataka_Food.get("Dharwad","Not found"))

#Adding 
Karnataka_Food["Shivamogga"]="Kadubu"
print(Karnataka_Food)

#updating
print(Karnataka_Food["Banglore"])
print("Updating.....")
Karnataka_Food["Banglore"]="Idli"
print(Karnataka_Food["Banglore"])

#Removing
x=Karnataka_Food.pop("Ramanagara")
print(x)
del Karnataka_Food["Mysore"]
print(Karnataka_Food)

Karnataka_Food["Manglore"]="Neer dosa"
print(Karnataka_Food)
print(Karnataka_Food.items())
print(Karnataka_Food.keys())
print(Karnataka_Food.values())

new_dishes={"Channapatna":"Gombe"}
Karnataka_Food.update(new_dishes)
print(Karnataka_Food)

#Q1
Self={
    "Name":"Geetha",
    "Age":20,
    "College":"Garden city university",
    "Branch":"Computer Science"
}
print(Self)
print(Self["Name"])
print(Self["College"])

#Q2
Student={
    "Name":"Geetha",
    "Age":20
}
Student["City"]="Banglore"
Student["Age"]=21
print(Student)

#Q3
book={
    "Title":"Python",
    "Author":"Guido",
    "Price":500
}
x=book.pop("Price")
print(book)

#Q4
fruits={
    "A":"Apple",
    "B":"Banana",
    "M":"Mango"
}
print(fruits.keys())
print(fruits.values())
print(fruits.items())
print(len(fruits))

#Q5
student={
    "Name":"Geetha",
    "Age":20,
    "Branch":"CSE"
}
if ("Age" in student):
  print("Age key found");
else:
  print("Age key not found")
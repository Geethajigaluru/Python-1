#input is used to take input from the user.
# The data entered by the user is always string so we need to convert intodifferent data type like int() or float()

boy_name=input("Enter boy_name: ")
boy_age=int(input("Enter boy_age: "))
girl_name=input("Enter girl name: ")
girl_age=int(input("Enter girl_age: "))
age_diff=abs(boy_age-girl_age)
print(f"{boy_name} loves {girl_name}. Age difference is {age_diff}")
# if boy is younger than girl it gives - to avoid this use abs


#Q1 Greeting Program
name=input("Enter Name: ")
city=input("Enter city: ")
print(f"Hello {name}! Welcome from {city}")


#Q2 String length
lang=input("Enter your favorite language: ")
print(lang)
print(len(lang))


#Q3 uppercase and lower case
sentence=input("Enter a sentence: ")
print("Original: ",sentence)
print("Uppercase: ",sentence.upper())
print("lowercase: ",sentence.lower()) 

# Q4 Remove extra spaces
name=input("Enter your name: ")
print(name.strip())

#Q5 Profile
name=input("Enter Name: ")
age=int(input("Enter your age: "))
college=input("Enter college: ")
lang=input("Enter programming language: ")
print("Name: ",name)
print("Age: ",age)
print("College: ",college)
print("Favorite Language: ",lang)
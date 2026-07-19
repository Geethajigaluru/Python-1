first_name="Geetha"
last_name="Jigalur"
full_name=first_name +" "+ last_name
print(full_name)

message="This is a Warning "
print(message*5)
print(message.upper())
print(message.lower())
print(message.strip()*2)  #removes spaces
print(message.replace("Warning", "Yeccharike"))

college="Garden City University "
print(college.strip()*5)

name='''I am "Geetha" I am studying "engineering" '''
print(name)
print(len(name))
print(name[3])

#indexing starts from 0, negative indexing at the end starts from -1
school="Amara"
print(school[0])
print(school[1:5])
print(school[2:5])
print(school[:4])
print(school[1:])
print(school[-1])
print(school)

#[start:end:step]
subject="chemistry"
print(subject[0: :2])

#Greeting program
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Hello, "+name+"! You are "+str(age)+ " years od.")
print(f"Hello, {name}! You are {age} years old.")

sentence="I love Gcu"
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","_"))
print(sentence.strip()*2)


#Q1 String slicing
name=input("Enter your name: ")
print(name[0])
print(name[-1])
print(name[ :3])
print(name[-3:])

#Q2 Replace a word
sentence="I am learning Python"
print(sentence.replace("Python","Java"))


# Q3 Reverse a string
word=input("Enter a word: ")
print("Reverse: ",word[ ::-1])

#Q4 Username Generator
First_name=input("Enter your First name: ")
Last_name=input("Enter your Last name: ")
Username=First_name+"_"+Last_name
print("Username: ",Username.lower())


#Q5 Count Characters
sentence=input("Enter a sentence: ")
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.strip())

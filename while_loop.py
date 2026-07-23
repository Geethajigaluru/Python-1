'''is_failed=True
i=1
while is_failed and i<=100:
    if i%2!=0:
        i=i+1
        continue
    print(f"Attempt{i}") 
    i=i+1
    if i>100:
        break
print("I gave up")

i=0
while(i<10):
    if i%2!=0:
        i=i+1
        continue
    print(i)
    i=i+1
    if i>11:
        break

pin=1234
trails=0
while trails<3:
    user_pin=int(input("Enter your pin: "))
    trails=trails+1
    if pin==user_pin:
        print("Correct")
        break
    else:
        print("Incorrect")

username="Geetha"
trails=1
while trails<3:
    input_user=input("Enter username: ")
    trails=trails+1
    if username==input_user:
        print("Login success")
        break
    else:
        print("login failed")

#Q1 Printing numbers
i=1
while (i<=10):
    print(i)
    i=i+1
    
#Q2 Sum of first N numbers
n=int(input("Enter a Number: "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("sum: ",sum)

#Q3 Multiplication table
num=int(input("Enter a number: "))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1
    '''

#Q4 Count digits
number = int(input("Enter a number: "))

digits = 0

while number > 0:
    digits = digits + 1
    number = number // 10

print("Number of digits:", digits)
'''
#Q5 Guess the secret number
secret=7
trails=0
while True:
    user_secret=int(input("Enter a secret number: "))
    trails=trails+1
    if secret==user_secret:
        print("Correct Guess!")
        break
    else:
        print("Try again")
'''
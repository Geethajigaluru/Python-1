#Q1
def even_odd(numbers):
    even=0
    odd=0
    for i in numbers:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print("Even: ",even)
    print("Odd: ",odd)
even_odd([2,5,8,9,10,7])

#Q2
def smallest(number):
    smallest=number[0]
    for i in number:
        if i<smallest:
            smallest=i
    print("Smallest: ",smallest)
smallest([8,4,6,2,10,5])

#Q3
def vowels(text):
    vowels=('a','e','i','o','u')
    vowels_count=0
    for letter in text:
        if letter in vowels:
            vowels_count=vowels_count+1
    print("Vowels: ",vowels_count)
vowels("Programming")

#Q4
def ascending(numbers):
        if numbers==sorted(numbers):
            print("sorted")
        else:
            print("not sorted")
ascending([1,2,3,4,5])
ascending([4,5,2,1,3])

#Q5
def even(numbers):
    for i in numbers:
        if i%2==0:
            print(i)
            break
        else:
            print("No even number")
even([5,7,9,12,8])


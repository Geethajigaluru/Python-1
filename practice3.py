#Q1
def second_largest(numbers):
    Unique=list(set(numbers))
    Unique.sort()
    print("Second largest: ",Unique[-2])
second_largest([5,3,9,2,9,7])

#Q2
def positive(numbers):
    positive=0
    for num in numbers:
        if num>0:
            positive=positive+1
    print("Positive numbers: ",positive)
positive([5,-2,0,8,-1,10])

#Q3
def smallest(numbers):
    small=numbers[0]
    for num in numbers:
        if num<small:
            small=num
    print(small)
smallest([8,3,15,2,10])

#Q4
def sum_even(numbers):
    sum=0
    for num in numbers:
        if num%2==0:
            sum=sum+num
    print(sum)
sum_even([2,5,8,7,10])

#Q5
def vowels_count(text):
    vowels=('a','e','i','o','u')
    vow_count=0
    for word in text:
        if word in vowels:
            vow_count=vow_count+1
    print("Vowels: ",vow_count)
vowels_count("geetha")

#Q6
def reverse_string(text):
    result=""
    for ch in text:
        result=ch+result
    print(result)
reverse_string("Python")

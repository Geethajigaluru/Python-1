#Q1
def even_odd():
    numbers=list(map(int, input().split()))
    even=0
    odd=0
    for i in numbers:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print("Even: ",even)
    print("Odd: ",odd)
even_odd()

#Q2
def second_largest(n):
    largest=n[0]
    second_largest=n[0]
    for i in n:
        if i>largest:
            second_largest=largest
            largest=i
        elif(i>second_largest and i!=largest):
            second_largest=i
    print("second_largest: ",second_largest)
second_largest([10,5,8,20,15])

#Q3
def reverse(text):
    words=text.split()
    result=" "
    for word in words: 
        result=result+word[::-1]+" "
    print(result)
reverse("Hello world python")
#Q4
def vowels_count(sentence):
    words=sentence.split()
    vowels=('a','e','i','o','u')
    for word in words:
        count=0
        for ch in word:
            if ch in vowels:
                count=count+1
        print(word,count)
vowels_count("hello world")

#Q5
def repeated_number(numbers):
    seen=[]
    for i in numbers:
        if i in seen:
            print(i)
            break
        seen.append(i)
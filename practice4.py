#Q1
def odd(numbers):
    count=0
    for num in numbers:
        if num%2!=0:
            count=count+1
    print(count)
odd([2,5,8,7,10,3])

#Q2
def longest_word(words):
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
    print("Longest: ",word)
longest_word(["cat","elephant","dog","tiger"])

#Q3
def perfect_square(number):
    i=1
    while i<=number:
        square=i*i
        if square==number:
            print("Perfect square")
            break
        elif square>number:
            print("Not a perfect square")
            break
        else:
            i=i+1
number=int(input("enter a number: "))
perfect_square(number)

#Q4
def reverse(sentence):
    words=sentence.split()
    reversed_sentence=""
    for word in words:
        reversed_sentence=reversed_sentence+word[::-1]+" "
    print(reversed_sentence)
reverse("I love python")

#Q5
def common_element(list1,list2):
    for num1 in list1:
        for num2 in list2:
            if num1==num2:
                print(num1)
common_element([1,2,3,4],[3,4,5,6])

            
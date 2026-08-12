#Q1
def vowels_count(sentence):
    vowels=('a','e','i','o','u')
    vow_coun=0
    l=sentence.split()
    for i in l:
        if i[0] in vowels:
            vow_coun=vow_coun+1
    print(vow_coun)
vowels_count("apple is an orange")

#Q2
def longest(sentence):
    l=sentence.split()
    longest_word=""   
    for i in l:
        if len(i)>len(longest_word):
            longest_word=i
    print(longest_word)
longest("Python is very intresting")

#Q3
def replacing(sentence):
    print(sentence)
    l=sentence.replace(" ","-")
    print(l)
replacing("hello world python")

#Q4
def greater_average(numbers):
    average=sum(numbers)/len(numbers)
    count=0
    for i in numbers:
        if i>average:
            count=count+1
    print(count)
greater_average([10,20,30,40,50])

#Q5
def remove_duplicate(string):
    result=""
    for i in string:
        if i not in result:
            result=result+i
    print(result)
remove_duplicate("programming")


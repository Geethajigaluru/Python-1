#Q1
def function(numbers):
    positive=0
    negative=0
    zero=0
    for i in numbers:
        if i>0:
            positive=positive+1
        elif(i<0):
            negative=negative+1
        else:
            zero=zero+1

    print("Positive: ",positive)
    print("Negative: ",negative)
    print("Zero: ",zero)
(function([5,-2,0,7,-8,0,10]))

#Q2
numbers=[3,7,5,2,7,8,5]
seen=set()
for num in numbers:
    if num in seen:
        print(num)
        break
    else:
        seen.add(num)
else:
    print("No repeating element")
    
#Q3
String="Programming"
vowels={'a','e','i','o','u'}
consonants={'b','c','d','f','g','h','j','k','l','m','n','p','q','e','s','t','v','w','x','y','z'}
vowels_count=0
consonants_count=0
for i in String:
    if i in vowels:
        vowels_count=vowels_count+1
    else:
        consonants_count=consonants_count+1
print("Vowels: ",vowels_count)
print("Consonants: ",consonants_count)
    
#Q4
numbers=[1,2,2,3,4,4,5,1]
for num in numbers:
    if numbers.count(num)==1:
        print(num)
        
#Q5
sentence="Python us awesome"
words=sentence.split()
for word in words:
    print(word[::-1])
    
#Q6
sentence="Python is awesome"
words=sentence.split()
for word in words:
    print(word[::-1],end=" ")


#Q6
numbers = [8, 4, 6, 2, 10, 5]

smallest = float('inf')
second = float('inf')

for num in numbers:
    if num < smallest:
        second = smallest
        smallest = num
    elif smallest < num < second:
        second = num

if second == float('inf'):
    print("No second smallest number")
else:
    print("Second smallest:", second)
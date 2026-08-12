#Q1
'''
def replacing(sentence):
    word=sentence.replace(" ","-")
    print(word)
replacing("I love Python")

#Q2
def characters(sentence):
    word=sentence.split()
    for ch in word:
        if(len(ch)>=4):
            print(ch)
characters("I love learning Python")

#Q3
def person(name):
    word=name.split()
    for ch in word:
        print(ch[0],end="")
person("Geetha K Jigaluru")
'''
#Q4
def first_last(text):
    if text[0]==text[-1]:
        print("same")
    else:
        print("different")
first_last(input())

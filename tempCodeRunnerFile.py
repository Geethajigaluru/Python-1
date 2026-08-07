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
import random
# num = int(input("Enter the number "))

def sqr(num):
    sqrt = num ** (1/2)

def checkNum(num):
    if(num < 0):
        print("Number is Negeative")
    elif(num == 0):
        print("Number is zero")
    else:
        print("Number is positive")

def oddEvenCheck(num):
    if(num % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

def checkLeapYear(num):
    if(num % 4 == 0):
        print("The year is leap year")
    else:
        print("Year is not leap year")

def greaterThree():
    num1 = num/2
    num2 = num*2
    num3 = num

    if(num1 > num2):
        if(num1>num3):
            print("Num1 is greter")
        else:
            print("Num3 is greter")
    else:
        if(num2>num3):
            print("Num2 is greater among all")
        else:
            print("Num3 is gretaer")

def generalInfo():
    # Using numbers directly
    print(max(10, 20, 5))      # 20

    # Using a list
    nums = [4, 7, 1, 9, 2]
    print(max(nums))            # 9

    # Using a string (max character by Unicode)
    print(max("python"))        # 'y'

    # Using numbers directly
    print(min(10, 20, 5))      # 5

    # Using a list
    nums = [4, 7, 1, 9, 2]
    print(min(nums))            # 1

    # Using a string (min character by Unicode)
    print(min("python"))        # 'h'

def checkPrime(num):
    flag = True
    for i in range(2,int(num/2)):
        if(num % i == 0):
            flag = False
            break

    if(flag):
        print("Number is Prime")
    else:
        print("Number is non-prime")

def generateRandomNumber():
    val = random.randint(10,20)
    print(val)

def tablePrint(num):
    try:
        for i in range(1,11):
            print(f"{num} x {i} = {int(num)*i}")
    except Exception as e:
        print(e)
    print("Hello World, sorry error occur")

tablePrint("hi")
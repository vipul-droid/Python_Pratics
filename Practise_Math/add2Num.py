num1 = int(input("Enter the first number "))
num2 = int(input("Enter the Second number "))

def sumNum (a, b):
    sum = a + b
    return sum

# ans = sumNum(num1, num2)
print(sumNum(num1, num2))



# Area of triangle 
base = float(input("Enter the base of triangle "))
height = float(input("Enter the Height of triangle "))

def areaOfTriangle(b, h):
    area = (1/2)*base*height
    return area

print(f"The area of triangle is {areaOfTriangle(base, height)}")


# Swap two variable
val1 = 23
val2 = 17

# Type one
val = val1
val1 = val2
val2 = val
print(f"The value of val1 {val1} and value of val2 is {val2}")

# Type two

val1 = val1 + val2
val2 = val1 -val2
val1 = val1 - val2
print(f"The value of val1 {val1} and value of val2 is {val2}")



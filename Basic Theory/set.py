# unordered, set is immutable but the values inside the set is immtutable

num = {2, 4, 6,7,4}

print(num)
print(type(num))
print(len(num))



for val in num:
    print(val)

num.add("hello")

num.remove(4)

print(num)
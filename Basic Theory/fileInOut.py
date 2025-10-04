# relative path
# r -> read / r+ -> read & write. / w -> write / w+ -> read & write
'''
f = open("Basic Theory/demo.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)

'''


'''
Append the file , Adding some comment there
f = open("Basic Theory/demo.txt", "a")
f.write("Hello world")
f.close()
'''

f = open("Basic Theory/demo.txt", "r")
data = f.read()

updateData = data.split()


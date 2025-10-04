# Unordered , mutable , Key is unique


info = {
    "name" : "Vipul",
    "age" : 26,
    "topics" : ["Sport", "Politics", "Game"],
    23 : "count",
    "flag" : True
}

# print(info)
# print(len(info))
# print(type(info))

# print(info["name"])
# Updating Value 
info["name"] = "Tiwari"

#  Add value 
info["Native"] = "Bihar"
print(info)
#  Remove Value
del info["Native"]
print(info)

# Looping 
# for key in info:
#     print(info[key])


# for value in info.values():
#     print(value)

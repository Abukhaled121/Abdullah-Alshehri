# Problem L1: List Info
nums = [10, 20, 30, 40, 50]

print("Count:", len(nums))
print("Sum:", sum(nums))
print("First:", nums[0])
print("Last:", nums[-1])

print("__"*9)

shopping = ["bread", "milk", "eggs"]

shopping.append("cheese")
shopping.remove("milk")

print(shopping)

print("__"*9)
colors = {"red", "blue", "green"}

colors.add("yellow")
colors.add("red")

print("Size:", len(colors))
print("red in set:", "red" in colors)
print("yellow in set:", "yellow" in colors)

print("__"*9)
# Problem S1: Create and Add
colors = {"red", "blue", "green"}
colors.add("yellow")

colors.add("red")

print("__"*9)

# Problem S2: Remove Duplicates from a List

nums = [1, 2, 2, 3, 4, 4, 5, 1]
print(list(set(nums)))
print(len(set(nums)))




print("__"*9)
# Problem S3: Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("union:",a|b)
print("intersection:",a&b)
print("In a but not in b:",a-b)

#TUPLES
print("__"*9)
# Problem T1: Create and Access
person = ("Sara", 25, "Riyadh")
print("name:", person[0])
print("age:", person[1])
print("city:",person[2])
print("__"*9)
#Problem T2: Immutability Check
colors = ("red", "green", "blue")


print("Length:",len(colors))
print("red in tuple:", "red" in colors)

print("__"*9)

# DICTS

# Problem D1: Create and Access

student = {"name": "Ali", "age": 17, "grade": "11"}
print("name:",student["name"])
print("age:",student["age"])
print("grade:",student["grade"])

print("__"*9)

# Problem D2: Add and Update

prices = {"apple": 3, "banana": 2}

prices["mango"] = 5
prices["apple"]=4
print (prices)



print("__"*9)
#Problem D3: Keys and Membership
user = {
    "name": "Sara",
    "email": "sara@example.com",
    "city": "Jeddah"
}

print("Keys:", list(user.keys()))

print("'name' in dict:", "name" in user)

print("'phone' in dict:", "phone" in user)






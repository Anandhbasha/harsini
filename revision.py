# datatype
# dict
list = [20,40,80,55] #index 20=0 40=1 80=2 55=3
# print(list[1])
# key value
# method 1
# Literal
student = {
    "name":"raja","age":20 ,"isComing":True #name,age is key && raja and 20 value
}
# method 2
# dict constructor
student1 = dict(name="harshini",age=17)

print(student["name"])
print(student1["name"])
print(student.get("age"))

# characterstics
    # unordered
    #key must be unique
    #key must be immutable
    # value can be anything("str","int")

# list of tuple
user = dict([("a",10),("b",20)])
# fromkeys()
keys = ["a","b","c"]
# d= dict.fromkeys(keys,10)
# print(d)

# zip
# keys = ["a","b","c"]
# value = [50,80]
# res = dict(zip(keys,value))
# print(res)


person = {
    "name":"arya",
    "age":30
}
person["name"] = "ajay"
person["city"] = "CBE"
print(person)

person.update({"city":"Erode"})
print(person)

employee= dict(zip(("name","salary","age"),("arun",52222,30)))

# delete
# pop
person.pop("city")
print(person)
employee.popitem()
print(employee)
employee.clear()
print(employee)

print("name" in person )
print("city" in person )

# pretty
import pprint
user = {"name":"kumar","details":{"age":30,"city":"chennai"}}
pprint.pprint(user)

# freq
nums = [1,1,1,2,2,2,3,3,3,3,3,4]
freq={}
for i in nums: #1
    if i in freq:
        freq[i]+=1 #1 2 3
    else:
        freq[i] = 1 
print(freq)



# freq{1:3,2:3,3:4,4:1}

from collections import Counter

print(Counter(nums))
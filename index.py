a,b,c = 50,30,60

# temp = a
# a=b # a=30
# b=c #b=60
# c=temp

c,a,b = a,b,c
print(a,b,c)


# datatypes
a=10
print(type(a))
a=10.2
print(type(a))
a="20"
print(type(a))
a=True
print(type(a))

# complex
list1 = [10,20.0,"abc",True]  #indexing

# print(list1[0])
# list1[0] = 50

# print(list1[0])
# a = list1.append(80)
# print(a)

print(type(list1))
list1.insert(4,80)
print(list1)

# tuple
tuple = (50,80,90,True)
print(type(tuple))

# set
sets = {101,101,105,105,108,108,102,106,103,104}
print(sets)
# dictionary
person = {
    "name":"abc",
    "age":20,
    "city":"CBE",
    "family":{
        "father":"gfghjgh",
        "mother":"kjhghjk",
        "siblings":{
            "Brother":"hffy",
            "sister":"ighffd"
        }
    }
}
print(person["family"]["siblings"]["Brother"])
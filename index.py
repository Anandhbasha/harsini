# a,b,c = 50,30,60

# # temp = a
# # a=b # a=30
# # b=c #b=60
# # c=temp

# c,a,b = a,b,c
# print(a,b,c)


# # datatypes
# a=10
# print(type(a))
# a=10.2
# print(type(a))
# a="20"
# print(type(a))
# a=True
# print(type(a))

# # complex
# list1 = [10,20.0,"abc",True]  #indexing

# # print(list1[0])
# # list1[0] = 50

# # print(list1[0])
# # a = list1.append(80)
# # print(a)

# print(type(list1))
# list1.insert(4,80)
# print(list1)

# # tuple
# tuple = (50,80,90,True)
# print(type(tuple))

# # set
# sets = {101,101,105,105,108,108,102,106,103,104}
# print(sets)
# # dictionary
# person = {
#     "name":"abc",
#     "age":20,
#     "city":"CBE",
#     "family":{
#         "father":"gfghjgh",
#         "mother":"kjhghjk",
#         "siblings":{
#             "Brother":"hffy",
#             "sister":"ighffd"
#         }
#     }
# }
# print(person["family"]["siblings"]["Brother"])




# names = str(input("Enter the Name"))
# rev = ""

# # Harsini
# for ch in names:
#     rev = ch +rev
#     print(rev)
    # H
    # Ha


    # H + "" = H
    # a+H = ah
    # r+ah = rah
    # srah
    # israh
    # nisrah
    # inisrah
# print(rev)



# Conditional
# userAge = int(input("Enter your Age:"))

# if userAge>19:
#     print("He is Adult")
# elif userAge<13:
#     print("He is Kid")
# else:
#     print("He is Teenager")

# if userAge>19:
#     print("He is Adult")
# elif userAge>13 and userAge<19:
#     print("He is Teenager")
# else:
#     print("He is Kid")


# age = 18
# state = "TN"

# if age >=18:
#     if state=="TN":
#         print("He is Elible to Vote")
#     else:
#         print("He is out of TN")
# else:
#     print("Age is under 18")       




# pyramid pattern
row = int(input("Enter the No of Rows:"))
for i in range(1,row+1):
    print(" "*(row-i),"*"*(2*i-1)) #1 #2+1


#     *
#    ***
#   *****
#  *******
# *********
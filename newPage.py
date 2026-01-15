# dict memeory and dict2 memory is same

# dict={"dog":10,"cat":20}
# dict2 = dict
# dict2["cat"] = 40
# print(dict)


# dict memeory and dict2 different memory is same
dict={"dog":10,"cat":20}
# dict2 = dict.copy()
# dict2["cat"] = 40
# print(dict)

# key = 10
# print(dict.pop(11))



# d= {"a":2,"b":3,"c":1}

# e = {}

# for i in d:
#     e[d[i]] = i  #e[2] = a = 2:a  d[i] =i  a:a
# print(d)



# d= {"a":2,"b":3,"c":1}

# e = {}
# for a,b in d.items():
d = {'a': 10, 'b': 20}

d['b'], d['a'] = d['a'], d['b']


print(d)

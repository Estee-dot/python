my_dictionary = {"name" : "Alice", "age" : 25, "city" : "New York"} #print(my_dictionary["name"])

keys = {"name" : "Alice", "age" : 25}
values = {"city" : "New york", "age" : 26}

for key, value in my_dictionary.items():
	my_dictionary[key] = value
print(my_dictionary)


#keys = ["name", "age", "city"]
#values = ["Alice", "25" ,"New york"]

#for key, value in zip(keys, values):
	#my_dictionary[key] = value

#print(my_dictionary)

#even = {count: count**2 for count in range(2, 11, 2)}
#print(even)

#squared = {x: x**2 for x in range(1,6)} print squared

#for key,value in my_dictionary.items():
	#print(f"{key}: {value}")

#for key in my_dictionary.values():
	#print(key)

#for value in my_dictionary:
	#print(value)


#if "city" in my_dictionary:
	#print("City is in the Dictionary")

#del my_dictionary["city"]
#print (my_dictionary)

#print(my_dictionary.get("names"))
	#print(my_dictionary.get("salary" , "not Avaliable")
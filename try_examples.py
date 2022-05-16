#1 Ask the user for scientist’s name and birthday to add to the dictionary,
#  and update the JSON file you have on disk with the scientist’s name.
#  If you run the program multiple times and keep adding new names,
#  your JSON file should keep getting bigger and bigger.

# import json
# birthday = {}
# def add_entry():
# 	name = input(f"Enter a name ").title()
# 	date = input(f"Ebter a birthday ")
# 	birthday[name] = date
# 	with open("birthday.json", "a") as f:
# 		json.dump(birthday,f)
# 	print (f"done.")
# add_entry()


#2 By using list comprehension, please write a program to print the list after removing the value 24
# lst = [12,24,35,24,88,120,155]
# lst_after_removing = [x for x in lst if x!=24]
# print(lst_after_removing)

#3 Write a program in Python that asks the user to input ten integers of their choice and return them a dictionary
#whose keys are the integers entered and whose values are the lists of divisors of the numbers entered.

# def listDiv (n):
#     lst = []
#     for i in range (1, n + 1):
#         if n % i == 0:
#             lst.append (i)
#     return lst
# typed_number = []
# try:
# 	for i in range (0, 10):
# 		n = int (input ("Type an integer"))
# 		typed_number.append(n)
# except ValueError:
# 	print ("you have value error")
# d = dict ({})
# for n in typed_number:
#     d [n] = listDiv (n)
# print(d)


#4 Write a Python program to insert a given string at the beginning of all items in a list.
#Sample list : [1,2,3,4], string : emp

# num = [1,2,3,4]
# print(['emp{0}'.format(i) for i in  num])
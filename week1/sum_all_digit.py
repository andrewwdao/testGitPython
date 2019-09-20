num_string=input("Type in the number: ")
num=0
for i in num_string:
	if i==".":
		pass
	else:
		num+=int(i)
print(num)

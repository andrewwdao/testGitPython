def isPrime():
	for i in range(2,num):
		if ((num%i)==0):
			return False
	return True


if __name__=="__main__":
	num=int(input("Type in number:" ))

	if isPrime():
		print("This is a prime number")
	else:
		print("This is NOT a prime number")


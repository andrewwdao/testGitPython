
def max(num1,num2):
	if(num1>num2):
		return num1
	else:
		return num2
def gcd(num1,num2):
	for i in range(max(num1,num2),2,-1): # 3 parameter as: start, stop, step
		if ((num1%i)==0) and ((num2%i)==0):
			return i

	return 1

if __name__ == "__main__":
	num01=int(input("Type in the first number: "))
	num02=int(input("Type in the second number: "))
	print("Greatest Common Divisor of ",num01," and ",num02," is: ",gcd(num01,num02))


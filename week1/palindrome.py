theString=input("Type in your string: ")
def palindrome():
	for i in range(len(theString)):
#		if (theString[i]!=theString[len(theString)-i-1]):
		if (theString[i]!=theString[-i-1]):
			return False
	return True

if __name__=="__main__":
	if (palindrome()):
		print("This is a palindrome string!")
	else:
		print("This is NOT a palindrome string!")


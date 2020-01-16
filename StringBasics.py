class StringFunctions:
	def reverseString(self, str):
		left, right = 0, len(str) - 1
		sList = list(str)
		while left < right:
			temp = sList[left]
			sList[left] = sList[right]
			sList[right] = temp
			left += 1
			right -= 1
		return ("").join(sList)


sf = StringFunctions()
print(sf.reverseString("payal")) 

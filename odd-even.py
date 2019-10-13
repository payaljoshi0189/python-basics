def odd_even(n):
	if n % 2 == 1:
		print("Odd number!")
	else:
		print("Even number!")



if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1 :
		odd_even(int(sys.argv[1]))
	else :
		print("Enter an input")
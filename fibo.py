#understanding the concepts of module

# This is a global variable that stores the name of the module, if not specified, 
# it is the same as the file name.
#__name__ = 'fibonacci' 

def fib(n):
	a, b = 0, 1
	count = 0
	
	while count < n:
		print(a,  end = ' ')
		next = a + b
		a = b
		b = next
		count+=1


if __name__ == "__main__":
	import sys
	if len(sys.argv ) < 2:
		print("Please provide an input")
	else:
		fib(int(sys.argv[1]))

		

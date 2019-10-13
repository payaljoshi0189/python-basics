#in progress

def list_less_than_ten(a):
	x = []
	for elem in a:
		if elem < 10:
			x.append(elem)

	for elem in x:
		print(elem, end = ' ')



if __name__ == "__main__":
	a = [50, 45, 12, 9, 4, 2, 67, 89]
	list_less_than_ten(a)
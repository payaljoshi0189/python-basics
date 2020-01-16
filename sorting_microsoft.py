class Sorting:
	def sorting(self, arr):
		n = len(arr)

		def getMax(arr, endIndex):
			maxVal = arr[0]
			idx = -1
			for i in range(endIndex+1):
				if maxVal <= arr[i]:
					idx = i
					maxVal = arr[i]

			#print(maxVal)
			return idx

		def swap(idx, arr):
			temp = arr[idx]
			arr[idx] = arr[0]
			arr[0] = temp

		def swapSort(arr):
			pos = n - 1

			for i in range(n):
				maxIdx = getMax(arr,pos)
				swap(maxIdx, arr) #bring the max to zeroth index
				#print("arr, pos", arr, pos)
				swap(pos, arr) # swap the max with its correct position
				#print("arr, pos", arr, pos)
				pos -= 1


		swapSort(arr)




arr = [6, 8, 1, 9, 3]
sortArr = Sorting()
sortArr.sorting(arr)
print(arr)






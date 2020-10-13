# Sort a list using Bubble Sort
# Swap the first 2 numbers if they are in wrong order and repeat the process upto last element and again use this iteration.
# Input  : [5, 3, 8, 7, 2, 90, 78, 9, 1]
# Output : [1, 2, 3, 5, 7, 8, 9, 78, 90]

def bubble_sort(unsorted):
	for i in range(len(unsorted)-1,0,-1):
		for j in range(i):
			if(unsorted[j]>unsorted[j+1]):
				unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
	return unsorted

unsorted = [5, 3, 8, 7, 2, 90, 78, 9, 1]
print(bubble_sort(unsorted))
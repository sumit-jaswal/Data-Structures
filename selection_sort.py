# Selection Sort : Find the minimum element in each iteration and place at its correct positon.
# Input  : [15, 31, 7, 6, 2]
# Outpit : [2, 6, 7, 15, 31]

def selection_sort(lis):
	for i in range(0,len(lis)-1):
		min = i
		for j in range(i,len(lis)):
			if(lis[j]<lis[min]):
				min = j
		lis[min],lis[i] = lis[i],lis[min]
	return lis

lis = [15, 31, 7, 6, 2]
print(selection_sort(lis))
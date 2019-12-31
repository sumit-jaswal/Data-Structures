# Lenear Search - Searching for a one by one by comparing it with each element in the list.
def linear_search(l,num):
	for i in range(len(l)):
		if(l[i]==num):
			found = True
			break
		else:
			found = False
	if(found is True):
		return True
	else:
		return False
			
	# Pythonic way to search an element
	'''if(search in lis):
		return True	
	else:
		return False'''	

lis = [8,4,78,232,89,213]
search = 213
print(linear_search(lis,search))

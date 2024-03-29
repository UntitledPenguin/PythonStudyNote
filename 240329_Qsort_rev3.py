
def quicksort(arr):
	if len(arr)<=2:
		return arr
	else:
		p=arr[0]
		leftarr=[x for x in arr[1:] if x<=p]
		rightarr=[x for x in arr[1:] if x>=p]
		return quicksort(leftarr)+[p]+quicksort(rightarr)

a=[1,9,10,8,7,2,6,4,5]
print(quicksort(a))

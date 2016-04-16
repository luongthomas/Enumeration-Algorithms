# /* Simplification & delegation for max subarray
#
#
# 	max subarray either has value
#
# 	1. MAXSUBARRAY(a[1, ..., n/2]),
# 	2. MAXSUBARRAY(a[n/2,..., n]),
# 	3. MAXSUFFIX(a[1, ..., n/2]) + MAXPREFIX(a[n/2,..., n])
#
# 	compute MAX SUFFIX and MAXPREFIX in linear time by
# 	modifying previous algorithm
#
# 	divide & conquer
#
# 	MAXSUBARRAY(a[1,..., n]) = max {MAXSUBARRAY(a[1, ..., n/2]),
# 								   {MAXSUBARRAY(a[n/2,..., n]),
# 								   {MAXSUFFIX(a[1, ..., n/2]) + MAXPREFIX(a[n/2,..., n])
#
#
#
#
#
# 	analysis (O(n) time for non-recursive work) x (O(logn)depth) = O(nlogn)
#
#
#
# */




def maxMiddle(array, start, middle, end):
	sum = 0
	left_sum = 0

	# left
	i = middle
	for index in range(start, i):
		sum += array[index]
		if (sum > left_sum):
			left_sum = sum

	# right
	sum = 0
	right_sum = 0
	i = middle + 1
	for index in range(i, end):
		sum += array[index]
		if(sum > right_sum):
			right_sum = sum

	return left_sum + right_sum



def maxSub(array, start, end):
	# type: (object, object, object) -> object
	if(start == end):
		return array[start]

	middle = (start + end) / 2
	result = max(max(maxSub(array, start, middle), maxSub(array, middle+1, end)), maxMiddle(array, start, middle, end))

	print("max(",start,"-",end,") = ", result )

	return result


def divConquer(array):
	length = len(array) - 1   #accounts for zero-index
	result = maxSub(array, 0, length)
	print("The result of divConquer is:", result)
	return







myList = [-5, 10, -100, 3, -100, 5, -9]

greatest_number = divConquer(myList)
print(greatest_number)






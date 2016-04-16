# /* Recursion Inversion for max subarray

# 	the max subarray either uses the last element or doesn't:

# 		MAXSUBARRAY(a[1,..., n]) = max  {MAXSUBARRAY(a[1, ..., n-1]),
# 										{MAXSUFFIX(a[1,...,n])
# 		MAXSUFFIX(a[1,..., n]) = max {MAX(0, a[1, ..., n-1]) + a[n] }

# 	dynamic programming 	evaluate this non-recursively by computing

# 	1. first MAXSUBARRAY(a[1]) and MAXSUFFIX(a[1])
# 	2. then MAXSUBARRAY(a[1,2]) and MAXSUFFIX(a[1,2] from above
# 	3. then MAXSUBARRAY(a[1,2,3]) and MAXSUFFIX(a[1,2,3] from above
# 	4. and so on

	

# 	analysis computing MAXSUBARRAY(a[1,..., n]) and  MAXSUFFIX(a[1, ..., n])
# 		from MAXSUBARRAY(a[1,..., n-1]) and  MAXSUFFIX(a[1, ..., n-1])
# 			takes O(1) time

# 	O(n) things to compute = O(n) time



#  pseudocode from lecture
# 	MAX_SUB_ARRAY_LINEAR(A)
# 		n = A.length
# 		maxsum = -infinity
# 		for j = 1 to n
# 			endingHereHigh = j
# 			if endingHereSum > 0
# 				endingHereSum = endingHereSum + A[j]
# 			else endingHereLow = j
# 				endingHereSum = A[j]
# 			if endingHereSum > maxSum
# 				maxSum = endingHereSum
# 				low = endingHereLow
# 				high = endingHereHigh
# 		return(low, high, max-sum)



		





# */






# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# Kadane's algorithm
def max_subarray(array):
    max_ending_here = max_so_far = 0
    for x in array:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far



myList = [-5, 10, -100, 3, -100, 5, -9]

greatest_number = max_subarray(myList)
print(greatest_number)
















